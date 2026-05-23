import numpy as np
import matplotlib.pyplot as plt

lcdm = np.loadtxt("phaseC2_LCDM_pure_scalCls.dat")
fde  = np.loadtxt("phaseC2_FDE_pure_scalCls.dat")

ell = lcdm[:,0]
mask = ell >= 2

TT = (fde[:,1] - lcdm[:,1]) / lcdm[:,1]
EE = (fde[:,2] - lcdm[:,2]) / lcdm[:,2]
TE = np.full_like(lcdm[:,4], np.nan)
safe = np.abs(lcdm[:,4]) > 1e-10
TE[safe] = (fde[safe,4] - lcdm[safe,4]) / lcdm[safe,4]

# raw TE
TE_lcdm = lcdm[:,4]
TE_fde  = fde[:,4]

print("\n=== Zero crossing check ===")
for i in range(len(ell)-1):
    if TE_lcdm[i] * TE_lcdm[i+1] < 0:
        print("LCDM crossing:", ell[i])
for i in range(len(ell)-1):
    if TE_fde[i] * TE_fde[i+1] < 0:
        print("FDE crossing :", ell[i]
# absolute difference
delta_TE = TE_fde - TE_lcdm

fig, axes = plt.subplots(3, 1, figsize=(12, 14))

# ---Panel 1---{raw TE}---
axes[0].plot(ell, TE_lcdm, label="TE LCDM")
axes[0].plot(ell, TE_fde, label="TE FDE")
axes[0].axhline(0, color='black', linestyle='--')
axes[0].set_xscale("log")
axes[0].set_xlim(2,2500)
axes[0].set_ylabel(r"$C_\ell^{TE}$")
axes[0].legend()
axes[0].grid()

# ---Panel 2---{delta TE}
axes[1].plot(ell, delta_TE, color="green")
axes[1].axhline(0, color='black', linestyle='--')
axes[1].set_xscale("log")
axes[1].set_ylabel(r"$\Delta C_\ell^{TE}$")
axes[1].grid()

# ---Panel 3---{fractional residual}
axes[2].plot(ell, TT, label="TT fractional")
axes[2].plot(ell, EE, label="EE fractional")
axes[2].plot(ell, TE, label="TE fractional")
axes[2].set_xscale("log")
axes[2].set_xlabel(r"$\ell$")
axes[2].set_ylabel(r"$\Delta C_\ell / C_\ell$")
axes[2].legend()
axes[2].grid()

plt.figure(figsize=(10,5))

plt.plot(ell[mask], TE_lcdm[mask], label="TE LCDM")
plt.plot(ell[mask], TE_fde[mask], label="TE FDE")

plt.axhline(0, color='black', linestyle='--')
plt.xlim(200, 800)
plt.xlabel(r"$\ell$")
plt.ylabel(r"$C_\ell^{TE}$")
plt.title("TE Zoom Around Crossing Region")

plt.legend()
plt.grid()

plt.show()
