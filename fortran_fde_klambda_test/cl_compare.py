import numpy as np
import matplotlib.pyplot as plt

lcdm = np.loadtxt("lambda_0_scalCls.dat")
fde  = np.loadtxt("test_scalCls.dat")

ell_lcdm = lcdm[:,0]
Cl_lcdm  = lcdm[:,1]

ell_fde = fde[:,0]
Cl_fde  = fde[:,1]

# 共通ℓを取得
common_ell = np.intersect1d(ell_lcdm, ell_fde)

# インデックス取得
lcdm_idx = np.isin(ell_lcdm, common_ell)
fde_idx  = np.isin(ell_fde,  common_ell)

ell = common_ell
lcdm_cut = Cl_lcdm[lcdm_idx]
fde_cut  = Cl_fde[fde_idx]

# 差分
d = (fde_cut - lcdm_cut) / lcdm_cut

plt.plot(ell, d)
plt.axvline(30, linestyle="--")
plt.xscale("log")
plt.xlabel("ℓ")
plt.ylabel("ΔCℓ / ΛCDM")
plt.title("ISW / CMB deviation")
plt.show()
