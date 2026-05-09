import numpy as np
import matplotlib.pyplot as plt

k_l, pk_l = np.loadtxt("pk_lcdm.dat", unpack=True)
k_f, pk_f = np.loadtxt("pk_fde.dat", unpack=True)

ratio = pk_f / pk_l

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

ax1.loglog(k_l, pk_l, label="ΛCDM")
ax1.loglog(k_f, pk_f, label="FDE λ=-0.05")
ax1.set_xlabel("k [Mpc⁻¹]")
ax1.set_ylabel("P(k)")
ax1.legend()
ax1.set_title("Matter Power Spectrum")

ax2.semilogx(k_l, ratio)
ax2.axhline(1.0, linestyle="--", color="gray")
ax2.axhline(0.95, linestyle=":", color="red", label="5%線")
ax2.set_xlabel("k [Mpc⁻¹]")
ax2.set_ylabel("P_FDE / P_LCDM")
ax2.set_title("Power Spectrum Ratio")
ax2.legend()
ax2.set_ylim(0.9, 1.05)

plt.tight_layout()
plt.savefig("pk_ratio.png", dpi=150)
print("saved: pk_ratio.png")
