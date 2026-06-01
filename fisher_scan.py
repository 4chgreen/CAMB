import numpy as np
import camb
from camb import model
import matplotlib.pyplot as plt

# ==========================================
# Baseline posterior mean values
# ==========================================

H0 = 67.36857489210549
ombh2 = 0.02230673963865737
omch2 = 0.11974506030718282
tau = 0.05493221992679812
As = 2.0971371902723783e-9
ns = 0.9628970757657817

# ==========================================
# Scan ranges
# ==========================================

lambda_vals = np.linspace(3.0, 7.0, 9)
eps_vals = np.linspace(0.02, 0.08, 9)

results_grid = np.zeros((len(lambda_vals), len(eps_vals)))

# ==========================================
# Fisher/local curvature scan
# ==========================================

for i, lam in enumerate(lambda_vals):
    for j, eps in enumerate(eps_vals):

        pars = camb.set_params(
            H0=H0,
            ombh2=ombh2,
            omch2=omch2,
            tau=tau,
            As=As,
            ns=ns,
            lmax=2500
        )

        pars.WantTransfer = True

        # FDE parameters
        pars.fde_lambda_mem = float(lam)
        pars.fde_eps_mu = float(eps)

        try:
            results = camb.get_results(pars)

            sigma8 = results.get_sigma8_0()

            results_grid[i, j] = sigma8

            print(
                f"lambda={lam:.2f}, "
                f"eps={eps:.3f}, "
                f"sigma8={sigma8:.5f}"
            )

        except Exception as e:

            results_grid[i, j] = np.nan

            print(
                f"FAILED: lambda={lam}, eps={eps}"
            )
            print(e)

# ==========================================
# Plot
# ==========================================

plt.imshow(
    results_grid,
    origin='lower',
    aspect='auto',
    extent=[
        eps_vals[0],
        eps_vals[-1],
        lambda_vals[0],
        lambda_vals[-1]
    ]
)

plt.xlabel("eps_mu")
plt.ylabel("lambda_mem")
plt.title("FDE C2 Local Curvature Scan")

plt.colorbar(label="sigma8")

plt.savefig("fisher_scan.png")

print("saved: fisher_scan.png")
