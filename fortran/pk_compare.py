import numpy as np
import matplotlib.pyplot as plt

# ファイル読み込み
lcdm = np.loadtxt("cmb_lcdm_matterpower.dat")
fde  = np.loadtxt("cmb_fde_0p05_matterpower_fde.dat")

k_l, pk_l = lcdm[:,0], lcdm[:,1]
k_f, pk_f = fde[:,0], fde[:,1]

# ★ 共通k領域に揃える
k_min = max(k_l.min(), k_f.min())
k_max = min(k_l.max(), k_f.max())

mask_l = (k_l >= k_min) & (k_l <= k_max)
mask_f = (k_f >= k_min) & (k_f <= k_max)

k_l, pk_l = k_l[mask_l], pk_l[mask_l]
k_f, pk_f = k_f[mask_f], pk_f[mask_f]

# ★ ここで補間して揃える
pk_f_interp = np.interp(k_l, k_f, pk_f)

ratio = pk_f_interp / pk_l

plt.loglog(k_l, pk_l, label="LCDM")
plt.loglog(k_l, pk_f_interp, label="FDE")
plt.legend()

plt.figure()
plt.semilogx(k_l, ratio)
plt.axhline(1.0)
plt.show()
