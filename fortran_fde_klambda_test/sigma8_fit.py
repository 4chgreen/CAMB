import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# =========================
# ■ データ（あなたのCAMB結果）
# =========================
lam = np.array([0.00, -0.01, -0.03, -0.05, -0.07,
                -0.10, -0.12, -0.15, -0.20])

sigma8 = np.array([0.7793, 0.7778, 0.7751, 0.7725, 0.7698,
                   0.7658, 0.7631, 0.7590, 0.7521])

# =========================
# ■ モデル定義
# =========================

# 線形
def linear(x, a, b):
    return a*x + b

# 2次
def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

# 指数
def exponential(x, A, B, C):
    return A*np.exp(B*x) + C

# =========================
# ■ フィッティング
# =========================
p_lin, _  = curve_fit(linear, lam, sigma8)
p_quad, _ = curve_fit(quadratic, lam, sigma8)
p_exp, _   = curve_fit(exponential, lam, sigma8, maxfev=10000)

# =========================
# ■ 予測曲線
# =========================
x_plot = np.linspace(min(lam), 0.0, 200)

y_lin  = linear(x_plot, *p_lin)
y_quad = quadratic(x_plot, *p_quad)
y_exp  = exponential(x_plot, *p_exp)

# =========================
# ■ 誤差（χ²）
# =========================
def chi2(model, params):
    return np.sum((sigma8 - model(lam, *params))**2)

chi_lin  = chi2(linear, p_lin)
chi_quad = chi2(quadratic, p_quad)
chi_exp  = chi2(exponential, p_exp)

print("===== FIT RESULTS =====")
print("Linear      χ² =", chi_lin)
print("Quadratic   χ² =", chi_quad)
print("Exponential χ² =", chi_exp)

print("\n===== PARAMETERS =====")
print("Linear      a,b =", p_lin)
print("Quadratic   a,b,c =", p_quad)
print("Exponential A,B,C =", p_exp)

# =========================
# ■ グラフ
# =========================
plt.figure(figsize=(7,5))

plt.scatter(lam, sigma8, label="CAMB data", color="black")
plt.plot(x_plot, y_lin,  label="Linear")
plt.plot(x_plot, y_quad, label="Quadratic")
plt.plot(x_plot, y_exp,  label="Exponential")

plt.xlabel("lambda_growth")
plt.ylabel("sigma8")
plt.title("sigma8(lambda) fit comparison")

plt.legend()
plt.grid()

plt.show()
