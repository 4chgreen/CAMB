import numpy as np
import matplotlib.pyplot as plt

lcdm = np.loadtxt("phaseC2_LCDM_pure_scalCls.dat")
fde  = np.loadtxt("phaseC2_FDE_pure_scalCls.dat")

ell = lcdm[:,0]

TT = (fde[:,1] - lcdm[:,1]) / lcdm[:,1]
EE = (fde[:,2] - lcdm[:,2]) / lcdm[:,2]
TE = (fde[:,4] - lcdm[:,4]) / lcdm[:,4]

plt.figure(figsize=(12,7))

plt.plot(ell, TT, label="TT fractional")
plt.plot(ell, EE, label="EE fractional")
plt.plot(ell, TE, label="TE fractional")

plt.xscale("log")

plt.xlabel(r"$\ell$")
plt.ylabel(r"$\Delta C_\ell / C_\ell$")

plt.legend()
plt.grid()

plt.show()
