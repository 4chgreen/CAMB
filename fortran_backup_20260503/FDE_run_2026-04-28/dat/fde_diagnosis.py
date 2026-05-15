import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

base = "./"

p1 = np.loadtxt(base + "planck_2018_matterpower.dat")
p2 = np.loadtxt(base + "test_matterpower.dat")

k1, pk1 = p1[:,0], p1[:,1]
k2, pk2 = p2[:,0], p2[:,1]

kmin = max(k1.min(), k2.min())
kmax = min(k1.max(), k2.max())

mask = (k1 >= kmin) & (k1 <= kmax)
k = k1[mask]
pk1_cut = pk1[mask]

def compute_ratio(kind):
    f = interp1d(k2, pk2, kind=kind, bounds_error=False, fill_value=np.nan)
    return f(k) / pk1_cut

plt.figure()
plt.plot(k, compute_ratio("linear"), label="linear")
plt.plot(k, compute_ratio("cubic"), label="cubic")
plt.plot(k, compute_ratio("nearest"), label="nearest")

plt.xscale("log")
plt.axhline(1.0, color="black", linestyle="--")
plt.legend()
plt.title("FDE Stability Diagnostic")
plt.show()
