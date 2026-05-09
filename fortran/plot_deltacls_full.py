import numpy as np
import matplotlib.pyplot as plt

def load(file):
    d = np.loadtxt(file)
    # columns: L TT EE TE PP TP
    return d[:,0], d[:,1], d[:,2], d[:,3]

l0, TT0, EE0, TE0 = load("lambda_0_scalCls.dat")
lp, TTp, EEp, TEp = load("lambda_p5e3_scalCls.dat")
lm, TTm, EEm, TEm = load("lambda_m5e3_scalCls.dat")

def delta(x, x0):
    return (x - x0) / x0

plt.figure(figsize=(10,6))

plt.plot(l0, delta(TTp, TT0), label="TT (+λ)", color="blue")
plt.plot(l0, delta(TEp, TE0), label="TE (+λ)", color="orange")
plt.plot(l0, delta(EEp, EE0), label="EE (+λ)", color="green")

plt.axhline(0, color="black", linewidth=0.5)

plt.xlabel("ℓ")
plt.ylabel("ΔCℓ / Cℓ")
plt.title("FDE: full ΔCℓ response (+λ)")
plt.legend()

plt.show()
