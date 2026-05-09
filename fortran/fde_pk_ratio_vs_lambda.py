import numpy as np
import matplotlib.pyplot as plt

def load(file):
    return np.loadtxt(file)

lcdm = load("cmb_lcdm_matterpower.dat")

k_ref, pk_ref = lcdm[:,0], lcdm[:,1]

# ★ 中k抽出
mask = (k_ref > 0.05) & (k_ref < 0.3)
k_ref = k_ref[mask]
pk_ref = pk_ref[mask]

datasets = {
    "λ=0.05": "cmb_fde_0p05_matterpower_fde.dat",
    "λ=0.1":  "cmb_fde_0p1_matterpower_fde.dat",
    "λ=0.2":  "cmb_fde_0p2_matterpower_fde.dat",
    "λ=0.3":  "cmb_fde_0p3_matterpower_fde.dat",
}

plt.figure()

for label, file in datasets.items():
    data = load(file)
    k, pk = data[:,0], data[:,1]

    mask_fde = (k > 0.05) & (k < 0.3)
    k = k[mask_fde]
    pk = pk[mask_fde]

    pk_interp = np.interp(k_ref, k, pk)
    ratio = pk_interp / pk_ref

    plt.plot(k_ref, ratio, label=label)

plt.axhline(1.0, linestyle="--")
plt.xlabel("k (mid-range)")
plt.ylabel("P_FDE / P_LCDM")
plt.legend()
plt.show()
