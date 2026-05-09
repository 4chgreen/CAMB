import numpy as np

# --- データ読み込み ---
lcdm = np.loadtxt("H-k_lcdm_phase1_matterpower_lcdm.dat")
fde  = np.loadtxt("H-k_fde_phase1_matterpower_fde.dat")

k = lcdm[:,0]
P_lcdm = lcdm[:,1]
P_fde  = fde[:,1]

# --- window（すでに使っているものがあればそれでもOK） ---
# ここでは簡易版（Phase1診断用）
W2 = np.exp(-(k/0.2)**2)   # σ8スケールの代表的重み

# --- integrand ---
I_lcdm = k**3 * P_lcdm * W2
I_fde  = k**3 * P_fde  * W2

# --- k-band 定義 ---
low  = (k < 0.05)
mid  = (k >= 0.05) & (k < 0.2)
high = (k >= 0.2)

# --- 積分 ---
def band(x, y):
    return np.trapz(y, x)

print("\n===== σ8 k-band decomposition =====")

print("LOW  LCDM:", band(k[low], I_lcdm[low]))
print("LOW  FDE  :", band(k[low], I_fde[low]))

print("MID  LCDM:", band(k[mid], I_lcdm[mid]))
print("MID  FDE  :", band(k[mid], I_fde[mid]))

print("HIGH LCDM:", band(k[high], I_lcdm[high]))
print("HIGH FDE :", band(k[high], I_fde[high]))

print("\n===== contribution ratio (FDE/LCDM) =====")
print("LOW  :", band(k[low], I_fde[low]) / band(k[low], I_lcdm[low]))
print("MID  :", band(k[mid], I_fde[mid]) / band(k[mid], I_lcdm[mid]))
print("HIGH :", band(k[high], I_fde[high]) / band(k[high], I_lcdm[high]))
