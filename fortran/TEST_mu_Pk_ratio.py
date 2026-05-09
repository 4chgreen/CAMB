import numpy as np
import matplotlib.pyplot as plt

lcdm = np.loadtxt("LCDM_Pk_Phase1_Pk.dat")
test = np.loadtxt("TEST_Pk_Phase1_Pk.dat")

k_l = lcdm[:,0]
k_t = test[:,0]

P_lcdm = lcdm[:,1]
P_test = test[:,1]

# kが一致しているか確認
print(np.max(np.abs(k_l - k_t)))

ratio = P_test / P_lcdm

plt.semilogx(k_l, ratio)
plt.axhline(1.0, linestyle="--")
plt.xlabel("k")
plt.ylabel("P_test / P_LCDM")
plt.title("Matter Power Ratio")
plt.show()
