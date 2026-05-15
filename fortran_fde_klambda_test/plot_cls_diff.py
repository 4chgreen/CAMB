import numpy as np
import matplotlib.pyplot as plt

def load(fname):
    data = np.loadtxt(fname)
    ell = data[:,0]
    TT  = data[:,1]
    return ell, TT

# データ読み込み
l0, cl0 = load("lambda_0_scalCls.dat")
lp, clp = load("lambda_p5e3_scalCls.dat")
lm, clm = load("lambda_m5e3_scalCls.dat")

# 差分（基準：λ=0）
dplus  = (clp - cl0) / cl0
dminus = (clm - cl0) / cl0

# プロット
plt.figure()

plt.plot(l0, dplus, label="+5e-3")
plt.plot(l0, dminus, label="-5e-3")

plt.axhline(0, color='black', linewidth=0.5)

plt.xlabel("ell")
plt.ylabel("ΔCℓ / Cℓ")
plt.title("FDE effect on CMB TT spectrum")
plt.legend()

plt.xlim(2, 2500)

plt.show()
