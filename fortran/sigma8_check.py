import numpy as np

# データ読み込み
lcdm = np.loadtxt("isw_lcdm_matterpower_lcdm.dat")
fde  = np.loadtxt("isw_fde_matterpower_fde.dat")

k = lcdm[:,0]
P_lcdm = lcdm[:,1]
P_fde  = fde[:,1]

# 比率
ratio = P_fde / P_lcdm

# σ8近似（簡易チェック用：重みなし積分）
sigma_lcdm = np.trapz(P_lcdm, k)
sigma_fde  = np.trapz(P_fde, k)

print("σ_LCDM (relative):", sigma_lcdm)
print("σ_FDE   (relative):", sigma_fde)

print("σ ratio:", sigma_fde / sigma_lcdm)

# 判定
if sigma_fde > sigma_lcdm:
    print("RESULT: σ8 増加（growth強化）")
else:
    print("RESULT: σ8 低下（growth抑制）")
