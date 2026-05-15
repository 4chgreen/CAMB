import numpy as np
import matplotlib.pyplot as plt

def load_scal(filename):
    data = np.loadtxt(filename)
    l = data[:,0]
    TT = data[:,1]
    EE = data[:,2]
    TE = data[:,3]
    return l, TT, EE, TE

# --- load ---
l0, TT0, EE0, TE0 = load_scal("lambda_0_scalCls.dat")
lp, TTp, EEp, TEp = load_scal("lambda_p5e3_scalCls.dat")
lm, TTm, EEm, TEm = load_scal("lambda_m5e3_scalCls.dat")

# --- ratio ---
def ratio(x, y):
    return x / (y + 1e-30)

TE_TT_0 = ratio(TE0, TT0)
TE_TT_p = ratio(TEp, TTp)
TE_TT_m = ratio(TEm, TTm)

EE_TT_0 = ratio(EE0, TT0)
EE_TT_p = ratio(EEp, TTp)
EE_TT_m = ratio(EEm, TTm)

# --- plot ---
plt.figure(figsize=(10,6))

plt.plot(l0, TE_TT_0, 'k-', label='TE/TT λ=0')
plt.plot(l0, TE_TT_p, 'b-', label='TE/TT λ+')
plt.plot(l0, TE_TT_m, 'r-', label='TE/TT λ-')

plt.plot(l0, EE_TT_0, 'k--', label='EE/TT λ=0')
plt.plot(l0, EE_TT_p, 'g--', label='EE/TT λ+')
plt.plot(l0, EE_TT_m, 'orange', linestyle='--', label='EE/TT λ-')

plt.axhline(0, color='gray', linewidth=0.5)

plt.xlim(0, 2500)
plt.xlabel("ℓ")
plt.ylabel("Ratio (TE/TT, EE/TT)")
plt.title("FDE: TE/TT and EE/TT ratios")
plt.legend()
plt.tight_layout()
plt.show()
