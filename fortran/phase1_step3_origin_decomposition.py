import numpy as np

# --- load z=0 ---
lcdm = np.loadtxt("H-k_lcdm_phase1_matterpower_lcdm.dat")
fde  = np.loadtxt("H-k_fde_phase1_matterpower_fde.dat")

k = lcdm[:,0]

P_l0 = lcdm[:,1]
P_f0 = fde[:,1]

# --- ratio ---
R0 = P_f0 / P_l0

# --- σ8-like window ---
W2 = np.exp(-(k/0.2)**2)

# --- integrated σ8 proxy ---
def sigma(P):
    return np.trapz(k**3 * P * W2, k)

sigma_l0 = sigma(P_l0)
sigma_f0 = sigma(P_f0)

print("\n===== GLOBAL σ8 SHIFT (z=0) =====")
print("LCDM σ8 proxy:", sigma_l0)
print("FDE  σ8 proxy:", sigma_f0)
print("ratio:", sigma_f0 / sigma_l0)

# --- k-band split ---
low  = k < 0.05
mid  = (k >= 0.05) & (k < 0.2)
high = k >= 0.2

def band(R):
    return (
        np.nanmean(R[low]),
        np.nanmean(R[mid]),
        np.nanmean(R[high])
    )

print("\n===== k-dependence test =====")
print("LOW MID HIGH:", band(R0))

# --- diagnostic slopes (growth fingerprint) ---
logk = np.log(k)

# slope in k-space (detect Poisson-like structure)
dR = np.gradient(R0, logk)

print("\n===== k-gradient diagnostic =====")
print("mean dR/dlnk (LOW):", np.nanmean(dR[low]))
print("mean dR/dlnk (HIGH):", np.nanmean(dR[high]))
