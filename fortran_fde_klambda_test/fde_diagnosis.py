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
# テスト関数
# =========================
def compute_ratio(kind):
    f = interp1d(
        k2, pk2,
        kind=kind,
        bounds_error=False,
        fill_value=np.nan
    )
    pk2_i = f(k)
    ratio = pk2_i / pk1_cut
    return ratio


# =========================
# 3種類比較
# =========================
ratio_linear = compute_ratio("linear")
ratio_cubic  = compute_ratio("cubic")
ratio_near   = compute_ratio("nearest")


# =========================
# 可視化
# =========================
plt.figure()

plt.plot(k, ratio_linear, label="linear")
plt.plot(k, ratio_cubic, label="cubic")
plt.plot(k, ratio_near, label="nearest")

plt.xscale("log")
plt.axhline(1.0, color="black", linestyle="--")

plt.xlabel("k")
plt.ylabel("P(k) ratio (FDE / Planck)")
plt.title("FDE Stability Diagnostic")
plt.legend()

plt.show()


# =========================
# 自動判定（簡易）
# =========================
def summary(name, r):
    print(f"\n[{name}]")
    print("min:", np.nanmin(r))
    print("max:", np.nanmax(r))
    print("std:", np.nanstd(r))


summary("linear", ratio_linear)
summary("cubic", ratio_cubic)
summary("nearest", ratio_near)

