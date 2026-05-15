
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# =========================
# データ読み込み
# =========================
base = "./FDE_run_2026-04-28/dat/"

p1 = np.loadtxt(base + "planck_2018_matterpower.dat")
p2 = np.loadtxt(base + "test_matterpower.dat")

k1, pk1 = p1[:,0], p1[:,1]
k2, pk2 = p2[:,0], p2[:,1]

# =========================
# 共通範囲
# =========================
kmin = max(k1.min(), k2.min())
kmax = min(k1.max(), k2.max())

mask = (k1 >= kmin) & (k1 <= kmax)
k = k1[mask]
pk1_cut = pk1[mask]

# =========================
# 補間
# =========================
f = interp1d(k2, pk2, kind="cubic", fill_value=np.nan, bounds_error=False)

ratio = f(k) / pk1_cut

# NaN除去
valid = np.isfinite(ratio)
k = k[valid]
ratio = ratio[valid]

# =========================
# プロット
# =========================
plt.figure()
plt.plot(k, ratio)
plt.xscale("log")
plt.axhline(1.0, color="black", linestyle="--")
plt.xlabel("k")
plt.ylabel("P(k) ratio (FDE / Planck)")
plt.title("FDE vs ΛCDM Matter Power Spectrum")
plt.show()


