import numpy as np
import matplotlib.pyplot as plt

# --- ファイル読み込み ---
lcdm = np.loadtxt("LCDM_Pk_Phase1_Pk.dat")
test = np.loadtxt("TEST_growth_clean_test_growth_Pk.dat")

# --- 列分解 ---
k = lcdm[:,0]
P_lcdm = lcdm[:,1]
P_test = test[:,1]

# --- ratio計算 ---
ratio = P_test / P_lcdm

# --- プロット ---
plt.figure()
plt.semilogx(k, ratio)
plt.axhline(1.0, linestyle="--")
plt.xlabel("k")
plt.ylabel("P_test / P_LCDM")
plt.title("P(k) Ratio Check")
plt.show()
