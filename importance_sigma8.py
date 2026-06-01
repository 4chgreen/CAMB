from getdist import loadMCSamples
import camb

samples = loadMCSamples('./fde_c2_mcmc')

params = samples.getParams()

print("Loaded chain")

for i in range(10):

    pars = camb.set_params(
        H0=params.H0[i],
        ombh2=params.ombh2[i],
        omch2=params.omch2[i],
        tau=params.tau[i],
        ns=params.ns[i],
        As=params.As[i],
        lmax=2500
    )

    pars.WantTransfer = True

    results = camb.get_results(pars)

    sigma8 = results.get_sigma8()

    print(i, sigma8)
