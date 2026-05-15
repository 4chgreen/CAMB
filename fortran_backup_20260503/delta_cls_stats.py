import numpy as np

files = {
    "0": "lambda_0_scalCls.dat",
    "+": "lambda_p5e3_scalCls.dat",
    "-": "lambda_m5e3_scalCls.dat"
}

def load(file):
    data = np.loadtxt(file, comments="#")
    ell = data[:,0]
    TT = data[:,1]
    EE = data[:,2]
    TE = data[:,3]
    return ell, TT, EE, TE

ell0, TT0, EE0, TE0 = load(files["0"])
ellp, TTp, EEp, TEp = load(files["+"])
ellm, TTm, EEm, TEm = load(files["-"])

def delta(x, x0):
    return (x - x0) / x0

dTTp = delta(TTp, TT0)
dTTm = delta(TTm, TT0)

dTEp = delta(TEp, TE0)
dTEm = delta(TEm, TE0)

dEEp = delta(EEp, EE0)
dEEm = delta(EEm, EE0)

print("\n=== ΔCℓ STATISTICS ===")

def stats(name, d):
    print(name)
    print("RMS:", np.sqrt(np.mean(d**2)))
    print("MAX:", np.max(np.abs(d)))
    print("MEAN:", np.mean(d))
    print("--------------------")

stats("TT +", dTTp)
stats("TT -", dTTm)

stats("TE +", dTEp)
stats("TE -", dTEm)

stats("EE +", dEEp)
stats("EE -", dEEm)
