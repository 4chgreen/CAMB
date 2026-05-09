import numpy as np
import matplotlib.pyplot as plt
import sys

# -------------------------
# input
# -------------------------
file_lcdm = sys.argv[1]
file_fde  = sys.argv[2]

lcdm = np.loadtxt(file_lcdm)
fde  = np.loadtxt(file_fde)

# -------------------------
# extract columns
# CAMB format:
# col0: ell
# col1: TT
# col2: EE
# col3: TE
# col4+: lensing etc
# -------------------------
ell_l = lcdm[:,0]
ell_f = fde[:,0]

cl_lcdm = lcdm[:,1]
cl_fde  = fde[:,1]

# -------------------------
# safety alignment check
# -------------------------
if not np.allclose(ell_l, ell_f):
    print("WARNING: ell mismatch detected")
    ell = np.intersect1d(ell_l, ell_f)
    cl_lcdm = cl_lcdm[:len(ell)]
    cl_fde  = cl_fde[:len(ell)]
else:
    ell = ell_l

# -------------------------
# ratio (numerical safety)
# -------------------------
eps = 1e-30
ratio = cl_fde / (cl_lcdm + eps)

# -------------------------
# plot
# -------------------------
plt.figure(figsize=(10,6))
plt.plot(ell, ratio, label="FDE / LCDM")
plt.axhline(1.0, color="black", linestyle="--")

plt.xlabel("ℓ")
plt.ylabel("Cℓ ratio (TT)")
plt.title("CMB TT Ratio (FDE vs LCDM)")
plt.legend()
plt.grid()

plt.ylim(0.99, 1.01)

plt.show()

# -------------------------
# diagnostics
# -------------------------
print("mean ratio =", np.mean(ratio))
print("std ratio  =", np.std(ratio))
print("max dev    =", np.max(np.abs(ratio-1)))
