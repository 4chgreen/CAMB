#!/usr/bin/env python3
import numpy as np
import sys
import matplotlib.pyplot as plt

file0 = sys.argv[1]
file1 = sys.argv[2]

k0, pk0 = np.loadtxt(file0, unpack=True)
k1, pk1 = np.loadtxt(file1, unpack=True)

# 共通kに揃える（安全側：単純補間）
pk1_interp = np.interp(k0, k1, pk1)

ratio = pk1_interp / pk0

plt.figure()
plt.loglog(k0, pk0, label="LCDM")
plt.loglog(k0, pk1_interp, label="FDE")
plt.legend()

plt.figure()
plt.semilogx(k0, ratio)
plt.axhline(1.0, color='black', linestyle='--')
plt.title("P(k) ratio: FDE / LCDM")

plt.show()
