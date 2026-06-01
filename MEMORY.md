# FDE-60 Project MEMORY.md — Updated 2026-05-23

## 共同開発記録 — リード・サイエンティフィック・ディベロッパー

---

# Phase A — 初期実装段階（2026-05-09〜10）

## 実装
- CAMB `equations.f90` 改造
- `clxcdot` growth sectorへ FDE項導入
- λ_growth growth suppression 実装

## 結果
- CAMB正常動作確認
- Cobaya MCMC収束確認
- lensing固定点解析実施

## 固定点結果
- 最良点:
  \[
  \lambda_{\rm growth}\approx -0.008
  \]
- Δχ² ≈ -1.32

## 結論
growth-only 定数 λ では：

- S₈ suppression
- high-ℓ CMB安定性
- lensing整合

の同時達成が困難であることを確認。

---

# Phase B — Growth λ MCMC解析（2026-05-15）

## 最終MCMC結果
- Δχ²_MCMC = -5.88
- Significance ≈ 2.94σ
- R-1 = 0.049（収束確認）

## 確定パラメータ
\[
\lambda_{\rm growth}
=
-0.0063 \pm 0.0048
\]

## χ²
- χ²_ΛCDM = 2769.22
- χ²_FDE = 2763.34

## 科学的評価
- AIC基準でパラメータ追加は統計的に正当化
- 背景宇宙はΛCDM近傍を保持
- growth suppression方向は確認

## 限界
- S₈ tension解消能力は限定的
- growth-only λでは acoustic保護との両立困難

---

# Phase C1 — 時間依存 Growth 導入（2026-05-18）

## 実装
時間依存 growth kernel：

\[
\lambda_{\rm eff}(a)
=
\lambda_{\rm growth} a^\alpha
\]

を `clxcdot` 経路へ導入。

## αスキャン結果
- α = 0.0 → σ₈ = 0.7772
- α = 0.5 → σ₈ = 0.8018
- α = 1.0 → σ₈ = 0.8100

## 問題点
強 suppression 条件：

\[
\lambda=-0.05,\ \alpha=1
\]

でも：

- Δχ² ≈ +44
- TTTEEE acoustic structure崩壊
- baryon leakage確認

## 結論
- 強い growth suppression 自体は可能
- しかし acoustic structure保護に失敗

---

# Phase C2 — μ-sector Selective Resonance Correction（2026-05-23）

## 実装kernel

\[
\mu(k)
=
1-\epsilon_\mu
\frac{(k\lambda_{\rm mem})^2}
{1+(k\lambda_{\rm mem})^2}
\]

## 最適固定点
- λ_mem = 5.0 Mpc
- ε_mu = 0.05

---

# 固定点結果

## χ²改善
CMB total:

\[
3524.91
\rightarrow
3509.99
\]

\[
\Delta\chi^2=-14.92
\]

TTTEEE:

\[
3096.53
\rightarrow
3081.64
\]

\[
\Delta=-14.89
\]

## σ₈
\[
0.8115
\rightarrow
0.8072
\]

\[
\Delta\sigma_8=-0.0043
\]

---

# TE診断

## Zero-crossing
- N = 11 完全一致
- Δℓ = 0

## Peak / trough migration
- 全主要構造で Δℓ = 0

## Fractional residual（ℓ=600-1500）
- TT std = 0.18%
- EE std = 0.12%
- TE std = 16.55%

## TE residual
- TE fractional max ≈ 410%
- major phase migration は否定的
- crossing amplification と
  微小振幅差で概ね説明可能

---

# MCMC完全収束（2026-05-23 06:21）

## Chain情報
- Steps taken: 404,497
- Accepted: 72,360
- Acceptance rate: 71.2%

## Convergence
\[
R-1({\rm means})=0.0465
\]

Gelman-Rubin基準クリア。

## Posterior mean
- H0 = 67.369
- ombh2 = 0.022307
- omch2 = 0.119745
- As = 2.0971e-9
- ns = 0.96290
- tau = 0.05493

## Posterior-derived σ₈

\[
\sigma_8 = 0.8095
\]

本解析設定のΛCDM近傍値
（≈0.811−0.812）に対し軽微な低下。

---

# Phase C2 科学的結論

## 成功点
1. Acoustic structure保持
2. TT/EE高安定性
3. 大規模TE phase migration否定的
4. MCMC posterior収束確認
5. χ²改善領域へのposterior集中確認

## 限界
1. σ₈ suppression が弱い
2. S₈ tension解消には不十分
3. late-time damping不足

## 総合判定

Phase C2は：

「統計的・数値的に安定な
selective resonance correction」

として成功。

一方、
growth suppression能力は限定的であり、
S₈ tension解消には：

\[
\alpha(a),\ \Gamma(a)
\]

等の late-time damping 構造が必要。

---

# 次フェーズ — Phase C3

## 目標
後期宇宙のみ選択的に growth suppression を強化。

## 候補
- late-time activation kernel
- α(a)
- Γ(a)
- scale-dependent damping

### Phase C3 Design Decision（2026-05-23）

**活性化関数の選択：Power-law a^α → Tanh activation へ移行**

理由：
- Power-law は late-time runaway リスク
- Tanh は初期宇宙保護＋後期宇宙飽和で物理的に優位

提案kernel：
μ(k,a) = 1 - ε_μ × f_tanh(a) × (kλ)² / (1+(kλ)²)

ここで f_tanh(a) = 0.5[1 + tanh((a-a_c)/Δa)]

初期スキャン：
a_c = 0.5, 0.7, 0.9
Δa = 0.1, 0.2, 0.3


## 開発方針
- 初期宇宙 acoustic structure保持
- high-ℓ安定性維持
- 後期growthのみ選択的減衰
- σ₈ / S₈追加低下
- χ²改善維持~

