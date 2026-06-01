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
# LCDM / FDE
# ============================================================

ell, cls_lcdm = get_cls(0.0, 0.0)

_, cls_fde = get_cls(5.0, 0.05)

mask = ell >= 2

# ============================================================
# Extract spectra
# ============================================================

TT_lcdm = cls_lcdm[:,0]
EE_lcdm = cls_lcdm[:,1]
TE_lcdm = cls_lcdm[:,3]

TT_fde = cls_fde[:,0]
EE_fde = cls_fde[:,1]
TE_fde = cls_fde[:,3]

# ============================================================
# Differences
# ============================================================

delta_TT = TT_fde - TT_lcdm
delta_EE = EE_fde - EE_lcdm
delta_TE = TE_fde - TE_lcdm

# ============================================================
# Fractional residuals
# ============================================================

frac_TT = delta_TT / TT_lcdm
frac_EE = delta_EE / EE_lcdm

frac_TE = np.full_like(delta_TE, np.nan)

safe_TE = np.abs(TE_lcdm) > 1e-10

frac_TE[safe_TE] = (
    delta_TE[safe_TE] / TE_lcdm[safe_TE]
)

# ============================================================
# Plot
# ============================================================

fig, axes = plt.subplots(3, 1, figsize=(10,12))

# ------------------------------------------------------------
# TT
# ------------------------------------------------------------

axes[0].semilogx(
    ell[mask],
    frac_TT[mask] * 100,
    'b-'
)

axes[0].axhline(
    0,
    color='k',
    linestyle='--',
    alpha=0.3
)

axes[0].set_ylabel('ΔTT/TT [%]')

axes[0].grid()

# ------------------------------------------------------------
# EE
# ------------------------------------------------------------

axes[1].semilogx(
    ell[mask],
    frac_EE[mask] * 100,
    'r-'
)

axes[1].axhline(
    0,
    color='k',
    linestyle='--',
    alpha=0.3
)

axes[1].set_ylabel('ΔEE/EE [%]')

axes[1].grid()

# ------------------------------------------------------------
# TE
# ------------------------------------------------------------

axes[2].semilogx(
    ell[mask],
    frac_TE[mask] * 100,
    'g-'
)

axes[2].axhline(
    0,
    color='k',
    linestyle='--',
    alpha=0.3
)

axes[2].set_ylabel('ΔTE/TE [%]')

axes[2].set_xlabel('ell')

axes[2].grid()

# ============================================================
# Save
# ============================================================

plt.tight_layout()

plt.savefig(
    'TT_EE_TE_compare.png',
    dpi=150,
    bbox_inches='tight'
)

print("\nsaved: TT_EE_TE_compare.png")

# ============================================================
# Statistics
# ============================================================

mask_600_1500 = (
    (ell >= 600) &
    (ell <= 1500)
)

print("\n=== STD DEV (600-1500) ===")

print(
    f"TT std = "
    f"{np.nanstd(frac_TT[mask_600_1500] * 100):.2f}%"
)

print(
    f"EE std = "
    f"{np.nanstd(frac_EE[mask_600_1500] * 100):.2f}%"
)

print(
    f"TE std = "
    f"{np.nanstd(frac_TE[mask_600_1500] * 100):.2f}%"
)

# ============================================================
# Max amplitudes
# ============================================================

print("\n=== MAX ABS FRACTIONAL ===")

print(
    f"max |TT| = "
    f"{np.nanmax(np.abs(frac_TT))*100:.2f}%"
)

print(
    f"max |EE| = "
    f"{np.nanmax(np.abs(frac_EE))*100:.2f}%"
)

print(
    f"max |TE| = "
    f"{np.nanmax(np.abs(frac_TE))*100:.2f}%"
)

plt.show()
