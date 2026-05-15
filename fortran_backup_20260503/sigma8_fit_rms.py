import numpy as np
from scipy.optimize import curve_fit

# -----------------------
# データ
# -----------------------
lam = np.array([0.0, -0.01, -0.03, -0.05, -0.07, -0.10, -0.12, -0.15, -0.20, -1.0])
sigma8 = np.array([0.7791, 0.7778, 0.7751, 0.7725, 0.7698, 0.7658, 0.7631, 0.7590, 0.7521, 0.6290])

# -----------------------
# モデル
# -----------------------
def linear(x, a, b):
    return a*x + b

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

def exponential(x, A, B, C):
    return A*np.exp(B*x) + C

# -----------------------
# フィット
# -----------------------
p_lin, _ = curve_fit(linear, lam, sigma8)
p_quad, _ = curve_fit(quadratic, lam, sigma8)
p_exp, _ = curve_fit(exponential, lam, sigma8, maxfev=10000)

# -----------------------
# 評価（残差）
# -----------------------
def rms(y, yhat):
    return np.sqrt(np.mean((y - yhat)**2))

print("\n=== FIT RESULT ===")

print("Linear RMS     :", rms(sigma8, linear(lam, *p_lin)))
print("Quadratic RMS  :", rms(sigma8, quadratic(lam, *p_quad)))
print("Exponential RMS:", rms(sigma8, exponential(lam, *p_exp)))

print("\n=== PARAMETERS ===")
print("Linear:", p_lin)
print("Quadratic:", p_quad)
print("Exponential:", p_exp)
