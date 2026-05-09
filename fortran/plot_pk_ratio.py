import numpy as np
import matplotlib.pyplot as plt

# データ読み込み
lcdm = np.loadtxt("isw_lcdm_matterpower_lcdm.dat")
fde  = np.loadtxt("isw_fde_matterpower_fde.dat")

k = lcdm[:,0]
P_lcdm = lcdm[:,1]
P_fde  = fde[:,1]

ratio = P_fde / P_lcdm

# ---- プロット ----
plt.figure(figsize=(7,5))
plt.plot(k, ratio, label="FDE / LCDM")
plt.axhline(1.0, linestyle="--", color="black")

plt.xscale("log")
plt.xlabel("k [h/Mpc]")
plt.ylabel("Power Ratio")
plt.title("P(k) Ratio Structure")

plt.legend()
plt.grid(True)
plt.show()
