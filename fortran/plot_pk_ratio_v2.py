import numpy as np
import matplotlib.pyplot as plt

# --- load latest CAMB outputs ---
lcdm = np.loadtxt("LCDM_Pk_Phase1_Pk.dat")
fde  = np.loadtxt("FDE_Pk_Phase1_Pk.dat")

k = lcdm[:,0]
P_lcdm = lcdm[:,1]
P_fde  = fde[:,1]

ratio = P_fde / P_lcdm

# --- plot ---
plt.figure(figsize=(7,5))
plt.plot(k, ratio, label="FDE / LCDM")
plt.axhline(1.0, linestyle="--", color="black")

plt.xscale("log")
plt.xlabel("k [h/Mpc]")
plt.ylabel("Power Ratio")
plt.title("P(k) Ratio Structure")

plt.legend()
plt.grid(True)
plt.show()
