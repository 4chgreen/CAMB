import numpy as np
import matplotlib.pyplot as plt

files = [
"results/fde_lg_m00_scalCls.dat",
"results/fde_lg_m01_scalCls.dat",
"results/fde_lg_m03_scalCls.dat",
"results/fde_lg_m05_scalCls.dat",
"results/fde_lg_m07_scalCls.dat",
"results/fde_lg_m10_scalCls.dat",
]

plt.figure()

for f in files:
    data = np.loadtxt(f)
    l = data[:,0]
    Cl = data[:,1]
    plt.plot(l, Cl, label=f.split("/")[-1])

plt.yscale("log")
plt.xlabel("l")
plt.ylabel("C_l")
plt.title("Cℓ comparison across λ")
plt.legend()
plt.grid()
plt.show()
