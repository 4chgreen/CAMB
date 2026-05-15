import numpy as np
import matplotlib.pyplot as plt

base = "./FDE_run_2026-04-28/dat/"

# =========================
# 読み込み
# =========================
p0   = np.loadtxt(base + "lambda_0_transfer_out.dat")
pm   = np.loadtxt(base + "lambda_m5e3_transfer_out.dat")
pp   = np.loadtxt(base + "lambda_p5e3_transfer_out.dat")

k = p0[:,0]

T0 = p0[:,1]
Tm = pm[:,1]
Tp = pp[:,1]

# =========================
# 比較（ratio）
# =========================
r_m = Tm / T0
r_p = Tp / T0

# =========================
# プロット
# =========================
plt.figure()

plt.plot(k, r_m, label="lambda -5e3 / lambda 0")
plt.plot(k, r_p, label="lambda +5e3 / lambda 0")

plt.xscale("log")
plt.axhline(1.0, color="black", linestyle="--")

plt.xlabel("k")
plt.ylabel("Transfer ratio")
plt.title("FDE Lambda effect on transfer function")
plt.legend()

plt.show()
