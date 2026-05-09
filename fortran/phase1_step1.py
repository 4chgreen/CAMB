import numpy as np

# データ読み込み（CAMB出力を想定）
lcdm_z0 = np.loadtxt("lcdm_z0_matterpower.dat")
lcdm_z1 = np.loadtxt("lcdm_z1_matterpower.dat")
lcdm_z2 = np.loadtxt("lcdm_z2_matterpower.dat")

fde_z0 = np.loadtxt("fde_z0_matterpower.dat")
fde_z1 = np.loadtxt("fde_z1_matterpower.dat")
fde_z2 = np.loadtxt("fde_z2_matterpower.dat")

k = lcdm_z0[:,0]

def ratio(fde, lcdm):
    return fde[:,1] / lcdm[:,1]

R0 = ratio(fde_z0, lcdm_z0)
R1 = ratio(fde_z1, lcdm_z1)
R2 = ratio(fde_z2, lcdm_z2)

print("z=0 mean:", np.mean(R0))
print("z=1 mean:", np.mean(R1))
print("z=2 mean:", np.mean(R2))

print("HIGH-k z dependence:")
high = k > 0.2
print("z0:", np.mean(R0[high]))
print("z1:", np.mean(R1[high]))
print("z2:", np.mean(R2[high]))
