import numpy as np
import matplotlib.pyplot as plt

# =====================================
# Load spectra
# =====================================

lcdm = np.loadtxt(
    "LCDM_output/phaseC2_LCDM_pure_scalCls.dat"
)

fde = np.loadtxt(
    "C2F_output/phaseC2_F_scalCls.dat"
)

ells = lcdm[:,0]

# =====================================
# TT EE TE
# =====================================

TT_lcdm = lcdm[:,1]
EE_lcdm = lcdm[:,2]
TE_lcdm = lcdm[:,4]

TT_fde = fde[:,1]
EE_fde = fde[:,2]
TE_fde = fde[:,4]

# =====================================
# Residuals
# =====================================

TT_res = (TT_fde - TT_lcdm)/TT_lcdm
EE_res = (EE_fde - EE_lcdm)/EE_lcdm

mask = np.abs(TE_lcdm) > 1e-2

TE_res = np.full_like(TE_lcdm, np.nan)

TE_res[mask] = (
    (TE_fde[mask] - TE_lcdm[mask])
    / TE_lcdm[mask]
)

# =====================================
# Plot
# =====================================

plt.figure(figsize=(10,6))

plt.plot(ells, TT_res, label="TT")
plt.plot(ells, EE_res, label="EE")
plt.plot(ells, TE_res, label="TE")

plt.xlim(2,2500)
plt.ylim(-0.5,0.5)

plt.xlabel(r"$\ell$")
plt.ylabel("fractional residual")

plt.title("Phase C2-F Safety Scan")

plt.legend()

plt.savefig("c2f_residuals.png")

print("saved: c2f_residuals.png")

# =====================================
# STD diagnostics
# =====================================

tt_std = np.nanstd(
    TT_res[(ells>600)&(ells<1500)]
)

ee_std = np.nanstd(
    EE_res[(ells>600)&(ells<1500)]
)

te_std = np.nanstd(
    TE_res[(ells>600)&(ells<1500)]
)

print()
print("=== STD (600<l<1500) ===")
print("TT:", tt_std)
print("EE:", ee_std)
print("TE:", te_std)
