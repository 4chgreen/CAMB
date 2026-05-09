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
    return ell, TT

def find_peaks(ell, y, n_peaks=5):
    # 簡易ピーク検出（周囲より大きい点）
    peaks = []
    for i in range(1, len(y)-1):
        if y[i] > y[i-1] and y[i] > y[i+1]:
            peaks.append((ell[i], y[i]))
    # 上位n個（振幅順）
    peaks = sorted(peaks, key=lambda x: x[1], reverse=True)
    return peaks[:n_peaks]

ell0, TT0 = load(files["0"])
ellp, TTp = load(files["+"])
ellm, TTm = load(files["-"])

peaks0 = find_peaks(ell0, TT0)
peaksp = find_peaks(ellp, TTp)
peaksm = find_peaks(ellm, TTm)

print("\n=== PEAK SHIFT ANALYSIS ===\n")

def show(name, peaks):
    print(name)
    for l, v in peaks:
        print("ℓ =", int(l), "  TT =", v)
    print("--------------------")

show("lambda = 0", peaks0)
show("lambda +", peaksp)
show("lambda -", peaksm)

print("\nNOTE: Compare ℓ positions across cases.")
