import numpy as np
import matplotlib.pyplot as plt

k0,P0 = np.loadtxt(
    "Pk_z5_champion.dat",
    unpack=True
)

cases = [
    ("Pk_z5_lambda5.dat",
     "lambda=5.0 eps=0.05"),
    
    ("Pk_z5_lambda6.dat",
     "lambda=6.0 eps=0.04"),
]

plt.figure(figsize=(10,6))

for fname,label in cases:

    k,P = np.loadtxt(fname,unpack=True)

    dP = (P-P0)/P0

    print("\n========================")
    print(label)
    print("========================")

    mask1 = np.abs(dP) > 0.01

    if np.any(mask1):
        idx_break = np.argmax(mask1)
        print(
            f"k_break(1%) = {k[idx_break]:.6f}"
        )
    else:
        print(
            "k_break(1%) = not reached"
        )

    mask3 = np.abs(dP) > 0.03

    if np.any(mask3):
        idx_break3 = np.argmax(mask3)
        print(
            f"k_break(3%) = {k[idx_break3]:.6f}"
        )
    else:
        print(
            "k_break(3%) = not reached"
        )

    mask5 = np.abs(dP) > 0.05

    if np.any(mask5):
        idx_break5 = np.argmax(mask5)
        print(
            f"k_break(5%) = {k[idx_break5]:.6f}"
        )
    else:
        print(
            "k_break(5%) = not reached"
        )

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

plt.axhline(
    0.01,
    color='red',
    linestyle='--',
    alpha=0.5,
    label='1%'
)

plt.axhline(
    0.03,
    color='orange',
    linestyle='--',
    alpha=0.5,
    label='3%'
)

plt.axhline(
    0.05,
    color='green',
    linestyle='--',
    alpha=0.5,
    label='5%'
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
    "Phase H7 : z=5 Matter Power Difference"
)

plt.legend()

plt.grid(True,alpha=0.3)

plt.show()
