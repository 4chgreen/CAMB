import numpy as np
import matplotlib.pyplot as plt
import sys

# -----------------------------
# 入力ファイル
# -----------------------------
lcdm_file = sys.argv[1]
fde_file  = sys.argv[2]

# -----------------------------
# データ読み込み
# (k, P(k)) 2列想定
# -----------------------------
k_lcdm, pk_lcdm = np.loadtxt(lcdm_file, unpack=True)
k_fde,  pk_fde  = np.loadtxt(fde_file, unpack=True)

# -----------------------------
# 安全のためソート
# -----------------------------
idx_l = np.argsort(k_lcdm)
idx_f = np.argsort(k_fde)

k_lcdm, pk_lcdm = k_lcdm[idx_l], pk_lcdm[idx_l]
k_fde,  pk_fde  = k_fde[idx_f], pk_fde[idx_f]

# -----------------------------
# 共通k領域に補間
# -----------------------------
pk_fde_interp = np.interp(k_lcdm, k_fde, pk_fde)

# -----------------------------
# 比率
# -----------------------------
ratio = pk_fde_interp / pk_lcdm

# -----------------------------
# プロット
# -----------------------------
plt.figure(figsize=(8,5))
plt.plot(k_lcdm, ratio, label="FDE / LCDM")

plt.axhline(1.0, color="black", linestyle="--", linewidth=1)

plt.xscale("log")

plt.xlabel("k [h/Mpc]")
plt.ylabel("P(k) ratio")
plt.title("BAO / P(k Comparison: FDE vs LCDM")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# -----------------------------
# 参考数値出力
# -----------------------------
print("=== Summary ===")
print("min ratio:", np.min(ratio))
print("max ratio:", np.max(ratio))
print("mean ratio:", np.mean(ratio))
