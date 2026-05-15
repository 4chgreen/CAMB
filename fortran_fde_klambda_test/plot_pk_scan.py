import numpy as np
import matplotlib.pyplot as plt

base = "test_lg0_matterpower.dat"
cases = [
    ("0.005","test_lg005_matterpower.dat"),
    ("0.01" ,"test_lg01_matterpower.dat"),
    ("0.02" ,"test_lg02_matterpower.dat"),
    ("0.03" ,"test_lg03_matterpower.dat"),
    ("0.05" ,"test_lg05_matterpower.dat"),
]

k0, pk0 = np.loadtxt(base, unpack=True)

plt.figure()
for label, f in cases:
    k, pk = np.loadtxt(f, unpack=True)
    pk_i = np.interp(k0, k, pk)
    ratio = pk_i / pk0
    plt.semilogx(k0, ratio, label=f"lg={label}")

plt.axhline(1.0, linestyle="--")
plt.legend()
plt.title("P(k) ratio vs lambda_growth")
plt.show()
