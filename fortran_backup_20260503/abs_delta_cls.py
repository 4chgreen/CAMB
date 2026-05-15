import numpy as np
import matplotlib.pyplot as plt

def load(file):
    d = np.loadtxt(file)
    return d[:,0], d[:,1]

l0, TT0 = load("lambda_0_scalCls.dat")
lp, TTp = load("lambda_p5e3_scalCls.dat")
lm, TTm = load("lambda_m5e3_scalCls.dat")

dTp = np.abs((TTp - TT0) / TT0)
dTm = np.abs((TTm - TT0) / TT0)

plt.plot(l0, dTp, label="+λ")
plt.plot(l0, dTm, label="-λ")

plt.xlabel("ℓ")
plt.ylabel("|ΔCℓ| / Cℓ")
plt.legend()
plt.title("FDE absolute ΔCℓ check")
plt.show()
