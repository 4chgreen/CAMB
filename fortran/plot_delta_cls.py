import numpy as np
import matplotlib.pyplot as plt

def load(file):
    d = np.loadtxt(file)
    ell = d[:,0]
    cl  = d[:,1]   # TT = 1列目Cl
    return ell, cl

# ΛCDM
ell0, cl0 = load("lambda_0_scalCls.dat")

# FDE
ellp, clp = load("lambda_p5e3_scalCls.dat")
ellm, clm = load("lambda_m5e3_scalCls.dat")

# ΔCℓ/Cℓ
dcl_p = (clp - cl0) / cl0
dcl_m = (clm - cl0) / cl0

plt.figure()

plt.plot(ell0, dcl_p, label="λ = +5e-3")
plt.plot(ell0, dcl_m, label="λ = -5e-3")

plt.axhline(0, color='black', linewidth=0.8)

plt.xlabel("ℓ")
plt.ylabel("ΔCℓ / Cℓ")
plt.title("FDE-60: CMB TT fractional change")
plt.legend()

plt.tight_layout()
plt.savefig("delta_cls.png", dpi=200)
plt.show()
