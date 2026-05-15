import numpy as np

base = "./FDE_run_2026-04-28/dat/"

p50  = np.loadtxt(base + "test_GRID50_matterpower.dat")
p100 = np.loadtxt(base + "test_GRID100_matterpower.dat")
p200 = np.loadtxt(base + "test_GRID200_matterpower.dat")

print(len(p50), len(p100), len(p200))

print(p50[:5,0])
print(p100[:5,0])
print(p200[:5,0])
