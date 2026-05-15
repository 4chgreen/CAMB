import numpy as np

def load(file):
    d = np.loadtxt(file)
    return d[:,0], d[:,1]

def find_peak(ell, cl):
    idx = np.argmax(cl)
    return ell[idx], cl[idx]

ell0, cl0 = load("lambda_0_scalCls.dat")
ellp, clp = load("lambda_p5e3_scalCls.dat")
ellm, clm = load("lambda_m5e3_scalCls.dat")

p0 = find_peak(ell0, cl0)
pp = find_peak(ellp, clp)
pm = find_peak(ellm, clm)

print("λ=0 peak :", p0)
print("λ=+ :     ", pp)
print("λ=- :     ", pm)
