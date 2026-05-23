import numpy as np
import camb

# =====================================
# Fixed cosmology
# =====================================

H0 = 67.36
ombh2 = 0.02237
omch2 = 0.1200
tau = 0.0544
As = 2.1e-9
ns = 0.965

# =====================================
# Reference LCDM sigma8
# =====================================

lcdm_sigma8 = 0.8115

# =====================================
# Grid around best point
# =====================================

grid = [

    (5.5, 0.07),
    (6.0, 0.06),
    (6.0, 0.07),
    (6.0, 0.08),
    (6.5, 0.07),

]

# =====================================
# Scan
# =====================================

print()
print("=== C2 Curvature Scan ===")
print()

for lam, eps in grid:

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

    suppression = lcdm_sigma8 - sigma8

    # proxy curvature quantity
    proxy_chi2 = (suppression / 0.002)**2

    print(
        f"lambda={lam:.2f}, "
        f"eps={eps:.3f}, "
        f"sigma8={sigma8:.5f}, "
        f"suppression={suppression:.5f}, "
        f"proxy_chi2={proxy_chi2:.2f}"
    )
