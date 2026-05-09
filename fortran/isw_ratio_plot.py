import numpy as np
import matplotlib.pyplot as plt

lcdm = np.loadtxt("isw_lcdm_scalCls.dat")
fde  = np.loadtxt("isw_fde_scalCls.dat")

# CAMBは通常:
# column 0 = ell
# column 1 = TT (or total Cl)

ell = lcdm[:,0]
cl_lcdm = lcdm[:,1]
cl_fde  = fde[:,1]

ratio = cl_fde / cl_lcdm

plt.plot(ell[:30], ratio[:30])
plt.axhline(1.0, linestyle="--")
plt.xlabel("ℓ")
plt.ylabel("ISW ratio (FDE / LCDM)")
plt.show()
