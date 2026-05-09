# plot_cmb_tt_ratio.py

import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) != 3:
    print("Usage: python3 plot_cmb_tt_ratio.py lcdm_scalCls.dat fde_scalCls.dat")
    sys.exit()

file_lcdm = sys.argv[1]
file_fde   = sys.argv[2]

# CAMB scalCls.dat:
# ℓ  TT  EE  BB  TE ...
data_lcdm = np.loadtxt(file_lcdm)
data_fde   = np.loadtxt(file_fde)

ell_l = data_lcdm[:,0]
cl_l  = data_lcdm[:,1]   # TT only

ell_f = data_fde[:,0]
cl_f  = data_fde[:,1]    # TT only

# ℓ一致前提（CAMBなら通常一致）
ell = ell_l

ratio = cl_f / cl_l

# ----------------------
# プロット1：絶対比較
# ----------------------
plt.figure()
plt.plot(ell, cl_l, label="LCDM")
plt.plot(ell, cl_f, label="FDE")
plt.xlabel("ℓ")
plt.ylabel("C_ℓ (TT)")
plt.title("CMB TT Spectrum Comparison")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.show()

# ----------------------
# プロット2：比
# ----------------------
plt.figure()
plt.plot(ell, ratio)
plt.axhline(1.0, linestyle="--")
plt.xlabel("ℓ")
plt.ylabel("FDE / LCDM")
plt.title("CMB TT Ratio")
plt.xscale("log")
plt.show()
