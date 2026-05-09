import numpy as np

lcdm = np.loadtxt("isw_lcdm_matterpower_lcdm.dat")
fde  = np.loadtxt("isw_fde_matterpower_fde.dat")

k = lcdm[:,0]
P_lcdm = lcdm[:,1]
P_fde  = fde[:,1]

# 安全チェック（重要）
assert np.allclose(lcdm[:,0], fde[:,0]), "k mismatch!"

ratio = P_fde / P_lcdm

print("min ratio:", np.min(ratio))
print("max ratio:", np.max(ratio))
print("mean ratio:", np.mean(ratio))

# 波数依存の確認（重要）
print("low-k mean:", np.mean(ratio[:10]))
print("mid-k mean:", np.mean(ratio[len(ratio)//2]))
print("high-k mean:", np.mean(ratio[-10:]))

# 判定
if np.mean(ratio) > 1:
    print("RESULT: 増幅（positive deviation）")
else:
    print("RESULT: 抑制（negative deviation）")


