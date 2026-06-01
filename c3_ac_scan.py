import camb

H0 = 67.36857489210549
ombh2 = 0.02230673963865737
omch2 = 0.11974506030718282
tau = 0.05493221992679812
As = 2.0971371902723783e-9
ns = 0.9628970757657817

fde_eps_mu = 0.07
fde_lambda_mem = 6.0
fde_da = 0.2

ac_values = [0.5, 0.7, 0.9]

for ac in ac_values:

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

        pars.fde_eps_mu = fde_eps_mu
        pars.fde_lambda_mem = fde_lambda_mem
        pars.fde_ac = ac
        pars.fde_da = fde_da

        results = camb.get_results(pars)

        sigma8 = results.get_sigma8_0()
        suppression = 0.8115 - sigma8

        print(
            f"a_c={ac:.2f}, "
            f"sigma8={sigma8:.5f}, "
            f"suppression={suppression:.5f}"
        )

    except Exception as e:
        print(f"FAILED: a_c={ac}")
        print(e)
