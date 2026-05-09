import numpy as np
import matplotlib.pyplot as plt

lcdm = np.loadtxt("cls_lcdm.dat")
fde  = np.loadtxt("cls_fde.dat")

ell = lcdm[:,0]

TT_l = lcdm[:,1]
TT_f = fde[:,1]

ratio = TT_f / TT_l

fig, (ax1, ax2) = plt.subplots(2,1, figsize=(8,8))

ax1.loglog(ell, TT_l, label="LCDM")
ax1.loglog(ell, TT_f, label="FDE")
ax1.set_xlabel("ell")
ax1.set_ylabel("D_ell TT")
ax1.legend()

ax2.semilogx(ell, ratio)
ax2.axhline(1.0, linestyle="--")
ax2.set_xlabel("ell")
ax2.set_ylabel("TT ratio")
ax2.set_ylim(0.98, 1.02)

plt.tight_layout()
plt.savefig("cls_ratio.png", dpi=150)

print("saved: cls_ratio.png")
