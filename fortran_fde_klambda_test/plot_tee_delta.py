import numpy as np
import matplotlib.pyplot as plt

def load(file):
    d = np.loadtxt(file)
    return d[:,0], d[:,1], d[:,2], d[:,3]

l0, TT0, TE0, EE0 = load("lambda_0_scalCls.dat")
lp, TTp, TEp, EEp = load("lambda_p5e3_scalCls.dat")
lm, TTm, TEm, EEm = load("lambda_m5e3_scalCls.dat")

def r(x, x0):
    return (x - x0) / x0

plt.plot(l0, r(TTp, TT0), label="TT")
plt.plot(l0, r(TEp, TE0), label="TE")
plt.plot(l0, r(EEp, EE0), label="EE")

plt.axhline(0, color="black", linewidth=0.5)
plt.xlabel("ℓ")
plt.ylabel("ΔCℓ / Cℓ")
plt.legend()
plt.title("FDE response comparison (+λ)")
plt.show()
