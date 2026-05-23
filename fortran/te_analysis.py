import camb
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# FDE Phase C2 : TE diagnostic pipeline
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

    # --------------------------------------------------------
    # FDE parameters
    # --------------------------------------------------------

    pars.fde_lambda_mem = lambda_mem
    pars.fde_eps_mu = eps_mu

    # --------------------------------------------------------
    # Run CAMB
    # --------------------------------------------------------

    results = camb.get_results(pars)

    powers = results.get_cmb_power_spectra(
        pars,
        CMB_unit='muK',
        raw_cl=True
    )

    # total[:,0]=TT
    # total[:,1]=EE
    # total[:,2]=BB
    # total[:,3]=TE

    cls = powers['total']

    ells = np.arange(cls.shape[0])

    return ells, cls


# ============================================================
# Get spectra
# ============================================================

ells_lcdm, cls_lcdm = get_cls(0.0, 0.0)

ells_fde, cls_fde = get_cls(5.0, 0.05)

# ============================================================
# Basic sanity check
# ============================================================

print("\n=== ARRAY SHAPE CHECK ===")
print("LCDM shape:", cls_lcdm.shape)
print("FDE shape :", cls_fde.shape)

print("\n=== FIRST FEW ROWS ===")
print(cls_lcdm[:5])

# ============================================================
# Multipole mask
# ============================================================

mask = ells_lcdm >= 2

# ============================================================
# Extract TE
# ============================================================

te_lcdm = cls_lcdm[mask, 3]
te_fde  = cls_fde[mask, 3]

ells_arr = ells_lcdm[mask]

# ============================================================
# Absolute difference
# ============================================================

delta_te = te_fde - te_lcdm

# ============================================================
# Fractional residual
# ============================================================

safe_mask = np.abs(te_lcdm) > 1e-10

ells_safe = ells_arr[safe_mask]

frac = delta_te[safe_mask] / te_lcdm[safe_mask]

# ============================================================
# Main diagnostic panels
# ============================================================

fig, axes = plt.subplots(3, 1, figsize=(12, 14))

# ============================================================
# Panel 1 : Raw TE
# ============================================================

ax1 = axes[0]

ax1.plot(
    ells_arr,
    te_lcdm,
    'b-',
    lw=1.5,
    label='LCDM',
    alpha=0.8
)

ax1.plot(
    ells_arr,
    te_fde,
    'r-',
    lw=1.5,
    label='FDE (lambda=5, eps=0.05)',
    alpha=0.8
)

ax1.axhline(0, color='k', lw=0.5, ls='--')

ax1.set_xscale("log")

ax1.set_xlim(2, 2500)

ax1.set_xlabel(r'$\ell$')

ax1.set_ylabel(r'$C_\ell^{TE}$')

ax1.set_title('Raw TE Spectrum')

ax1.legend()

ax1.grid()

# ============================================================
# Panel 2 : Delta TE
# ============================================================

ax2 = axes[1]

ax2.plot(
    ells_arr,
    delta_te,
    'g-',
    lw=1.0
)

ax2.axhline(0, color='k', lw=0.5, ls='--')

ax2.set_xscale("log")

ax2.set_xlim(2, 2500)

ax2.set_xlabel(r'$\ell$')

ax2.set_ylabel(r'$\Delta C_\ell^{TE}$')

ax2.set_title(r'$\Delta C_\ell^{TE} = FDE - LCDM$')

ax2.grid()

# ============================================================
# Panel 3 : Fractional residual
# ============================================================

ax3 = axes[2]

ax3.plot(
    ells_safe,
    frac,
    color='purple',
    lw=1.0
)

ax3.axhline(0, color='k', lw=0.5, ls='--')

ax3.set_xscale("log")

ax3.set_xlim(2, 2500)

ax3.set_ylim(-0.2, 0.2)

ax3.set_xlabel(r'$\ell$')

ax3.set_ylabel(
    r'$\Delta C_\ell^{TE} / C_\ell^{TE}(\Lambda CDM)$'
)

ax3.set_title('Fractional TE Residual')

ax3.grid()

# ============================================================
# Save main panels
# ============================================================

fig.tight_layout()

fig.savefig(
    'TE_panels.png',
    dpi=150,
    bbox_inches='tight'
)

print("\nsaved: TE_panels.png")

# ============================================================
# Zoom around crossing region
# ============================================================

plt.figure(figsize=(10,5))

plt.plot(
    ells_arr,
    te_lcdm,
    label='LCDM'
)

plt.plot(
    ells_arr,
    te_fde,
    label='FDE'
)

plt.axhline(0, color='k', ls='--')

plt.xlim(200, 800)

plt.xlabel(r'$\ell$')

plt.ylabel(r'$C_\ell^{TE}$')

plt.title('TE Zoom Around Crossing Region')

plt.legend()

plt.grid()

plt.tight_layout()

plt.savefig(
    'TE_zoom.png',
    dpi=150,
    bbox_inches='tight'
)

print("saved: TE_zoom.png")

# ============================================================
# Zero crossing analysis
# ============================================================

print("\n=== Zero crossing analysis ===")

lcdm_cross = []
fde_cross = []

# ------------------------------------------------------------
# LCDM crossings
# ------------------------------------------------------------

for i in range(len(te_lcdm)-1):

    if te_lcdm[i] * te_lcdm[i+1] < 0:

        lcdm_cross.append(ells_arr[i])

        print(f"LCDM crossing : ell ~ {ells_arr[i]}")

# ------------------------------------------------------------
# FDE crossings
# ------------------------------------------------------------

for i in range(len(te_fde)-1):

    if te_fde[i] * te_fde[i+1] < 0:

        fde_cross.append(ells_arr[i])

        print(f"FDE crossing  : ell ~ {ells_arr[i]}")

# ============================================================
# Crossing shift summary
# ============================================================

print("\n=== Crossing count ===")

print("N_LCDM =", len(lcdm_cross))
print("N_FDE  =", len(fde_cross))

print("\n=== Crossing shifts ===")

for n, (a, b) in enumerate(zip(lcdm_cross, fde_cross)):

    print(
        f"crossing {n}: "
        f"LCDM={a}, "
        f"FDE={b}, "
        f"Delta_ell={b-a}"
    )

# ============================================================
# Show plots
# ============================================================

plt.show()
