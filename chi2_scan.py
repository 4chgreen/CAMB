import numpy as np
import camb
from camb import model

# ==========================================
# Posterior mean cosmology
# ==========================================

H0 = 67.36857489210549
ombh2 = 0.02230673963865737
omch2 = 0.11974506030718282
tau = 0.05493221992679812
As = 2.0971371902723783e-9
ns = 0.9628970757657817

# ==========================================
# Reference point
# ==========================================

lambda_ref = 5.0
eps_ref = 0.05

# ==========================================
# Scan ranges
# ==========================================

lambda_vals = [4.0, 4.5, 5.0, 5.5, 6.0]
eps_vals = [0.03, 0.04, 0.05, 0.06, 0.07]

# ==========================================
# Main scan
# ==========================================

for lam in lambda_vals:

    for eps in eps_vals:

        try:

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

            pars.fde_lambda_mem = lam
            pars.fde_eps_mu = eps

            results = camb.get_results(pars)

            sigma8 = results.get_sigma8_0()

            # crude proxy stability score
            suppression = 0.8115 - sigma8

            print(
                f"lambda={lam:.2f}, "
                f"eps={eps:.3f}, "
                f"sigma8={sigma8:.5f}, "
                f"suppression={suppression:.5f}"
            )

        except Exception as e:

            print(
                f"FAILED: lambda={lam}, eps={eps}"
            )

            print(e)
