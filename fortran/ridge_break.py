import numpy as np
import matplotlib.pyplot as plt

k = np.array([
    0.1,
    0.2,
    0.5,
    1.0,
    2.0,
    5.0
])

case5 = np.array([
    0.000125,
    0.001573,
    0.016082,
    0.034310,
    0.046316,
    0.054956
])

case6 = np.array([
   -0.000006,
    0.001270,
    0.021652,
    0.047897,
    0.065009,
    0.077296
])

plt.figure(figsize=(8,5))

plt.plot(
    k,
    np.abs(case5),
    marker='o',
    label='lambda=5.0 eps=0.05'
)

plt.plot(
    k,
    np.abs(case6),
    marker='s',
    label='lambda=6.0 eps=0.04'
)

plt.axvline(
    0.5,
    color='gray',
    linestyle=':'
)

plt.axvline(
    1.0,
    color='gray',
    linestyle=':'
)

plt.axvline(
    5.0,
    color='gray',
    linestyle=':'
)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('k [h/Mpc]')
plt.ylabel('|ΔP/P|')

plt.title(
    'Phase H4 : Degeneracy Ridge Breakdown'
)

plt.legend()
plt.grid(True, which='both', alpha=0.3)

plt.show()
