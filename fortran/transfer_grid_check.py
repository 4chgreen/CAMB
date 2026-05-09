import numpy as np
import matplotlib.pyplot as plt

base = "./FDE_run_2026-04-28/dat/"

# GRID別 transfer（もしあれば）
t50  = np.loadtxt(base + "test_GRID50_transfer_out.dat")
t100 = np.loadtxt(base + "test_GRID100_transfer_out.dat")
t200 = np.loadtxt(base + "test_GRID200_transfer_out.dat")

k = t50[:,0]

p50  = t50[:,1]
p100 = t100[:,1]
p200 = t200[:,1]

r100 = p100 / p50
r200 = p200 / p50

plt.figure()

plt.plot(k, r100, label="GRID100 / GRID50")
plt.plot(k, r200, label="GRID200 / GRID50")

plt.xscale("log")
plt.axhline(1.0, color="black", linestyle="--")

plt.xlabel("k")
plt.ylabel("Transfer ratio")
plt.title("TRANSFER GRID convergence test")
plt.legend()

plt.show()
