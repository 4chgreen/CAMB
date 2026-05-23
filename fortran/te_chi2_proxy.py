import numpy as np

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
# TE spectra
# =====================================

TE_lcdm = lcdm[:,4]
TE_fde = fde[:,4]

# =====================================
# Avoid crossing singularities
# =====================================

mask = (
    (ells > 30)
    &
    (np.abs(TE_lcdm) > 1e-2)
)

# =====================================
# Fractional residual
# =====================================

res = (
    (TE_fde[mask] - TE_lcdm[mask])
    / TE_lcdm[mask]
)

ells_use = ells[mask]

# =====================================
# Proxy chi2
# =====================================

proxy = np.sum(res**2)

rms = np.sqrt(np.mean(res**2))

max_abs = np.max(np.abs(res))

# =====================================
# Report
# =====================================

print()
print("=== TE Proxy Diagnostics ===")
print()

print("multipoles used =", len(res))

print("RMS residual =", rms)

print("max |residual| =", max_abs)

print("proxy chi2 =", proxy)

print()

# =====================================
# High-l split
# =====================================

high = ells_use > 1500

if np.sum(high) > 0:

    res_high = res[high]

    print("=== High-l TE ===")
    print()

    print("RMS high-l =", np.sqrt(np.mean(res_high**2)))

    print("max high-l =", np.max(np.abs(res_high)))
