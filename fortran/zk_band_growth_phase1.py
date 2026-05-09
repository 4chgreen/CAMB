import numpy as np

# --- load ---
lcdm0 = np.loadtxt("H-k_lcdm_phase1_matterpower_lcdm.dat")
lcdm1 = np.loadtxt("H-k_lcdm_phase1_matterpower_2.dat")
lcdm2 = np.loadtxt("H-k_lcdm_phase1_matterpower_3.dat")

fde0  = np.loadtxt("H-k_fde_phase1_matterpower_fde.dat")
fde1  = np.loadtxt("H-k_fde_phase1_matterpower_2.dat")
fde2  = np.loadtxt("H-k_fde_phase1_matterpower_3.dat")

# --- ratio（安全版）---
def ratio(f, l):
    return np.where(l[:,1] != 0, f[:,1] / l[:,1], np.nan)

R0 = ratio(fde0, lcdm0)
R1 = ratio(fde1, lcdm1)
R2 = ratio(fde2, lcdm2)

# --- k（zごとに保持）---
k0 = lcdm0[:,0]
k1 = lcdm1[:,0]
k2 = lcdm2[:,0]

# --- band定義関数 ---
def band_stats(k, R):
    low  = k < 0.05
    mid  = (k >= 0.05) & (k < 0.2)
    high = k >= 0.2

    return (
        np.nanmean(R[low]),
        np.nanmean(R[mid]),
        np.nanmean(R[high])
    )

# --- 出力 ---
print("\n===== z = 0 =====")
print("LOW MID HIGH:", band_stats(k0, R0))

print("\n===== z = 1 =====")
print("LOW MID HIGH:", band_stats(k1, R1))

print("\n===== z = 2 =====")
print("LOW MID HIGH:", band_stats(k2, R2))
