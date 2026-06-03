import numpy as np
import matplotlib.pyplot as plt

k0,P0 = np.loadtxt(
    "Pk_champion.dat",
    unpack=True
)

cases = [
    ("Pk_lambda5_eps005.dat",
     "lambda=5.0 eps=0.05"),

    ("Pk_lambda6_eps004.dat",
     "lambda=6.0 eps=0.04"),
]

plt.figure(figsize=(10,6))

for fname,label in cases:

    k,P = np.loadtxt(fname,unpack=True)

    dP = (P-P0)/P0

    plt.plot(k,dP,label=label)

    imax = np.argmax(np.abs(dP))

    idx01 = np.argmin(np.abs(k-0.1))
    idx02 = np.argmin(np.abs(k-0.2))
    idx05 = np.argmin(np.abs(k-0.5))
    idx1  = np.argmin(np.abs(k-1.0))
    idx2  = np.argmin(np.abs(k-2.0))
    idx5  = np.argmin(np.abs(k-5.0))

    print("\n========================")
    print(label)
    print("========================")

    print(
        f"max |ΔP/P| = {np.abs(dP[imax]):.6f}"
    )

    print(
        f"k(max)     = {k[imax]:.6f}"
    )

    print(
        f"ΔP/P @0.1  = {dP[idx01]:.6f}"
    )

    print(
        f"ΔP/P @0.2  = {dP[idx02]:.6f}"
    )

    print(
        f"ΔP/P @1.0  = {dP[idx1]:.6f}"
    )

    print(
        f"ΔP/P @0.5  = {dP[idx05]:.6f}"
    )

    print(
        f"ΔP/P @2.0  = {dP[idx2]:.6f}"
    )

    print(
        f"ΔP/P @5.0  = {dP[idx5]:.6f}"
    )


plt.axhline(
    0,
    color='black',
    linestyle='--'
)

plt.axvspan(
    0.5,
    5.0,
    alpha=0.15,
    color='red',
    label='Ly-alpha sensitive'
)


for x in [0.1, 0.2, 0.5, 1.0, 2.0, 5.0]:
    plt.axvline(
        x=x,
        color='gray',
        linestyle=':',
        alpha=0.3
    )

plt.xscale('log')

plt.xlabel("k [h/Mpc]")
plt.ylabel("ΔP/P")

plt.title(
    "Phase H2b : Matter Power Difference"
)

plt.legend()

plt.grid(True,alpha=0.3)

plt.show()
