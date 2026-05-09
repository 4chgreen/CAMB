import numpy as np
import matplotlib.pyplot as plt

# lensedCls.datの列：ell, TT, EE, BB, TE
l_l, tt_l, ee_l, bb_l, te_l = np.loadtxt("cls_lcdm.dat", unpack=True)
l_f, tt_f, ee_f, bb_f, te_f = np.loadtxt("cls_fde_004.dat", unpack=True)

fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# TT ratio
axes[0].semilogx(l_l, tt_f/tt_l)
axes[0].axhline(1.0, linestyle="--", color="gray")
axes[0].axhline(1.005, linestyle=":", color="red")
axes[0].axhline(0.995, linestyle=":", color="red")
axes[0].set_ylabel("FDE / LCDM")
axes[0].set_title("CMB TT ratio (λ=-0.04 vs ΛCDM)")
axes[0].set_ylim(0.98, 1.02)
axes[0].set_xlabel("ℓ")

# EE ratio
axes[1].semilogx(l_l, ee_f/ee_l)
axes[1].axhline(1.0, linestyle="--", color="gray")
axes[1].axhline(1.005, linestyle=":", color="red")
axes[1].axhline(0.995, linestyle=":", color="red")
axes[1].set_ylabel("FDE / LCDM")
axes[1].set_title("CMB EE ratio (λ=-0.04 vs ΛCDM)")
axes[1].set_ylim(0.98, 1.02)
axes[1].set_xlabel("ℓ")

# TE ratio
axes[2].semilogx(l_l, te_f/te_l)
axes[2].axhline(1.0, linestyle="--", color="gray")
axes[2].axhline(1.005, linestyle=":", color="red")
axes[2].axhline(0.995, linestyle=":", color="red")
axes[2].set_ylabel("FDE / LCDM")
axes[2].set_title("CMB TE ratio (λ=-0.04 vs ΛCDM)")
axes[2].set_ylim(0.98, 1.02)
axes[2].set_xlabel("ℓ")

plt.tight_layout()
plt.savefig("cmb_ratio_004.png", dpi=150)
print("saved: cmb_ratio_004.png")
