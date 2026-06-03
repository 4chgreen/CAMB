import numpy as np
import matplotlib.pyplot as plt

k0,P0 = np.loadtxt(
    "Pk_z0_champion425.dat",
    unpack=True
)

cases = [
    ("Pk_z0_lambda5.dat",
     "lambda=5.0 eps=0.05"),
    
    ("Pk_z0_lambda6.dat",
     "lambda=6.0 eps=0.04"),
]

plt.figure(figsize=(10,6))

for fname,label in cases:

    k,P = np.loadtxt(fname,unpack=True)

    dP = (P-P0)/P0

    if "lambda=5.0" in label:
        dP_lambda5 = dP.copy()

    if "lambda=6.0" in label:
        dP_lambda6 = dP.copy()

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
    0.02,
    color='red',
    linestyle='--',
    alpha=0.5,
    label='2%'
)

plt.axvline(
    0.35,
    color='blue',
    linestyle='-.',
    linewidth=2,
    alpha=0.7,
    label='k_break ≈ 0.35'
)

plt.axhline(
    0.05,
    color='orange',
    linestyle='--',
    alpha=0.5,
    label='5%'
)

plt.axhline(
    0.10,
    color='green',
    linestyle='--',
    alpha=0.5,
    label='10%'
)

plt.axvspan(
    0.5,
    5.0,
    alpha=0.15,
    color='red',
    label='Ly-alpha band'
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
    "Phase H8 : Ridge Visibility in Ly-alpha Band"
)

diff12 = dP_lambda6 - dP_lambda5


mask = k > 0.05

idx_cross = np.where(
    np.diff(
        np.sign(diff12[mask])
    )
)[0]

print("\n=== CROSS CHECK ===")

k2 = k[mask]
d2 = diff12[mask]

for i in idx_cross[:10]:

    print(
        f"k1={k2[i]:.6f} "
        f"diff1={d2[i]:.8f}"
    )

    print(
        f"k2={k2[i+1]:.6f} "
        f"diff2={d2[i+1]:.8f}"
    )

    print("-----")

plt.legend()
plt.grid(True,alpha=0.3)

plt.show()
