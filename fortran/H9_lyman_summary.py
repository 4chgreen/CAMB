import numpy as np
import matplotlib.pyplot as plt

# ========================
# Phase H9a
# Ly-alpha visibility test
# ========================

k = np.array([
    0.5,
    1.0,
    2.0,
    5.0
])

# λ=5.0 , ε=0.05
dP_lambda5 = np.array([
    0.0176,
    0.0369,
    0.0494,
    0.0582
])

# λ=6.0 , ε=0.04
dP_lambda6 = np.array([
    0.0237,
    0.0516,
    0.0694,
    0.0820
])

# 観測精度の目安
err3 = np.full(len(k), 0.03)
err5 = np.full(len(k), 0.05)

plt.figure(figsize=(10,6))

plt.semilogx(
    k,
    dP_lambda5*100,
    marker='o',
    linewidth=2,
    label='lambda=5.0 eps=0.05'
)

plt.semilogx(
    k,
    dP_lambda6*100,
    marker='s',
    linewidth=2,
    label='lambda=6.0 eps=0.04'
)

plt.semilogx(
    k,
    err3*100,
    '--',
    linewidth=2,
    label='3% reference'
)

plt.semilogx(
    k,
    err5*100,
    '--',
    linewidth=2,
    label='5% reference'
)

for ki, yi in zip(k, dP_lambda5*100):
    plt.text(
        ki,
        yi,
        f"{yi:.1f}%",
        fontsize=9
    )

for ki, yi in zip(k, dP_lambda6*100):
    plt.text(
        ki,
        yi,
        f"{yi:.1f}%",
        fontsize=9
    )

plt.xlabel("k [h/Mpc]")
plt.ylabel("|ΔP/P| [%]")

plt.title(
    "Phase H9a : Ly-alpha Visibility Test"
)

plt.grid(True, which='both', alpha=0.3)

plt.legend()

plt.tight_layout()

plt.show()

print("\n========================")
print("Phase H9a Summary")
print("========================")

print("\nlambda=5.0 eps=0.05")
for ki, yi in zip(k, dP_lambda5):
    print(
        f"k={ki:.1f}  |ΔP/P|={100*yi:.2f}%"
    )

print("\nlambda=6.0 eps=0.04")
for ki, yi in zip(k, dP_lambda6):
    print(
        f"k={ki:.1f}  |ΔP/P|={100*yi:.2f}%"
    )

print("\nReference lines")
print("3% : possible visibility threshold")
print("5% : strong visibility threshold")
