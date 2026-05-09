import numpy as np
import matplotlib.pyplot as plt

# --- 読み込み ---
lcdm = np.loadtxt("LCDM_Pk_Phase1_Pk.dat")
mu   = np.loadtxt("TEST_mu_clean_test_mu_Pk.dat")

# --- 列分解 ---
k = lcdm[:,0]
P_lcdm = lcdm[:,1]
P_mu   = mu[:,1]

# --- ratio ---
ratio = P_mu / P_lcdm

# --- plot ---
plt.figure()
plt.semilogx(k, ratio)
plt.axhline(1.0, linestyle="--")
plt.xlabel("k")
plt.ylabel("P_mu / P_LCDM")
plt.title("μ vs LCDM Matter Power Ratio")
plt.show()
