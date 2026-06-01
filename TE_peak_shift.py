import camb
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Get spectra
# ============================================================

def get_cls(lambda_mem=0.0, eps_mu=0.0):

    pars = camb.set_params(
        H0=67.36,
        ombh2=0.02237,
        omch2=0.1200,
        tau=0.0544,
        As=2.1e-9,
        ns=0.965,
        lmax=2500,
        lens_potential_accuracy=1
    )

    pars.fde_lambda_mem = lambda_mem
    pars.fde_eps_mu = eps_mu

    results = camb.get_results(pars)

    powers = results.get_cmb_power_spectra(
        pars,
        CMB_unit='muK',
        raw_cl=True
    )

    cls = powers['total']

    ells = np.arange(cls.shape[0])

    return ells, cls

# ============================================================
# Load spectra
# ============================================================

ell, cls_lcdm = get_cls(0.0, 0.0)

_, cls_fde = get_cls(5.0, 0.05)

TE_lcdm = cls_lcdm[:,3]
TE_fde  = cls_fde[:,3]

# ============================================================
# Restrict region
# ============================================================

mask = (ell >= 600) & (ell <= 1500)

ell_cut = ell[mask]

TE_lcdm_cut = TE_lcdm[mask]
TE_fde_cut  = TE_fde[mask]

# ============================================================
# Peak finder
# ============================================================

def find_peaks(x, y):

    peaks = []

    troughs = []

    for i in range(1, len(y)-1):

        # peak
        if y[i] > y[i-1] and y[i] > y[i+1]:
            peaks.append((x[i], y[i]))

        # trough
        if y[i] < y[i-1] and y[i] < y[i+1]:
            troughs.append((x[i], y[i]))

    return peaks, troughs

# ============================================================
# Find peaks/troughs
# ============================================================

lcdm_peaks, lcdm_troughs = find_peaks(
    ell_cut,
    TE_lcdm_cut
)

fde_peaks, fde_troughs = find_peaks(
    ell_cut,
    TE_fde_cut
)

# ============================================================
# Compare peaks
# ============================================================

print("\n=== PEAK SHIFTS ===")

N = min(len(lcdm_peaks), len(fde_peaks), 10)

for i in range(N):

    ell_l = lcdm_peaks[i][0]
    ell_f = fde_peaks[i][0]

    delta = ell_f - ell_l

    print(
        f"peak {i}: "
        f"LCDM={ell_l}, "
        f"FDE={ell_f}, "
        f"Delta_ell={delta}"
    )

# ============================================================
# Compare troughs
# ============================================================

print("\n=== TROUGH SHIFTS ===")

N = min(len(lcdm_troughs), len(fde_troughs), 10)

for i in range(N):

    ell_l = lcdm_troughs[i][0]
    ell_f = fde_troughs[i][0]

    delta = ell_f - ell_l

    print(
        f"trough {i}: "
        f"LCDM={ell_l}, "
        f"FDE={ell_f}, "
        f"Delta_ell={delta}"
    )

# ============================================================
# Plot
# ============================================================

plt.figure(figsize=(12,6))

plt.plot(
    ell_cut,
    TE_lcdm_cut,
    label='LCDM'
)

plt.plot(
    ell_cut,
    TE_fde_cut,
    label='FDE'
)

# LCDM peaks
for p in lcdm_peaks[:10]:

    plt.axvline(
        p[0],
        color='blue',
        alpha=0.15
    )

# FDE peaks
for p in fde_peaks[:10]:

    plt.axvline(
        p[0],
        color='red',
        alpha=0.15
    )

plt.axhline(
    0,
    color='black',
    linestyle='--'
)

plt.xlabel(r'$\ell$')

plt.ylabel(r'$C_\ell^{TE}$')

plt.title('TE Peak Migration')

plt.legend()

plt.grid()

plt.tight_layout()

plt.savefig(
    'TE_peak_shift.png',
    dpi=150,
    bbox_inches='tight'
)

print("\nsaved: TE_peak_shift.png")

plt.show()
