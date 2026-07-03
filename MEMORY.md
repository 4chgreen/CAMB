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


---

# Phase D — Memory Field Phase

(To be completed)

---

# Phase E — Memory Field Refinement

(To be completed)

---

# Phase H15–H24 — Q-ridge Era

(To be completed)

---

# Phase H25–H27 — HMF and Cross Geometry

(To be completed)

---

# Phase H28 — Planck Baseline and Birth Surface
## Objectives

Phase H28では、背景宇宙論をPlanck2018 Baselineへ統一し、Memory Fieldの影響を評価するための基準宇宙論を再構築した。

主な目的は以下の4点である。

- Planck2018固定背景宇宙論への移行
- Birth Surfaceの再構築
- HMFデータベースの再生成
- H29以降のObservation解析の基盤整備

---

## Background Cosmology

解析では以下のPlanck2018 Baseline Cosmologyを固定した。

| Parameter | Value |
|-----------|------:|
| H0 | 67.36 |
| ombh2 | 0.02237 |
| omch2 | 0.12000 |
| ns | 0.965 |
| tau | 0.0544 |
| logA | 3.05 |

FDE側では

- fde_eps_mu
- fde_lambda_mem
- fde_alpha
- fde_kd
- fde_ac
- fde_da

を固定し、

λ_growthのみを変更して比較を実施した。

---

## Main Results

Planck2018固定宇宙論のもとで、

Birth Surfaceを再構築した。

代表的な結果は以下である。

| λ_growth | Birth Redshift |
|-----------|---------------:|
| 0.02482 | 2.124 |
| 0.02550 | 1.792 |
| 0.02600 | 1.581 |
| 0.02650 | 約1.34 |
| 0.02700 | 約1.08 |
| 0.02750 | 約0.81 |
| 0.02800 | 約0.45 |

Birth Redshiftはλ_growthの増加とともに単調に減少することを確認した。

---

## Generated Data

Phase H28では各λについて

- hmf_matrix
- lnM_vec
- redshift_vec

を保存し、

以降のCross解析およびBirth Surface解析の基礎データベースを構築した。

代表的な保存ファイルは

- hmf_matrix_H28_planck02482.npy
- hmf_matrix_H28_planck02550.npy
- hmf_matrix_H28_planck02600.npy
- hmf_matrix_H28_planck02650.npy
- hmf_matrix_H28_planck02700.npy
- hmf_matrix_H28_planck02750.npy
- hmf_matrix_H28_planck02800.npy

である。

---

## Conclusions

Phase H28により、

- Planck2018 Baseline Cosmologyへの統一
- Birth Surfaceの再構築
- HMFデータベースの再生成

が完了した。

この成果はPhase H29以降のObservation解析およびBirth Surface解析の基盤となった。
(To be completed)

---

# Phase H29 — Observation Audit
## Objectives

Phase H29では、Phase H28で構築したPlanck2018 Baseline CosmologyおよびBirth Surfaceを基盤として、Observation解析・CNCLike解析・Birth Surfaceの再現性を総合的に検証した。

主な目的は以下の5点である。

- Observation解析の独立監査
- SO_sim_0（CNCLike）の監査
- Birth Surfaceの再現性確認
- Master Equationの構築
- 外部検証（External Validation）の実施

---

## Observation Audit

Planck2018固定背景宇宙論の下でObservation解析を実施した。

代表点は以下の通りである。

| λ_growth | σ8 | Total Clusters | Birth z |
|-----------|------:|---------------:|---------:|
| 0.02460 | 0.806607 | 14700.379 | 2.230 |
| 0.02520 | 0.806747 | 14723.755 | 1.928 |
| 0.02620 | 0.806979 | 14762.782 | 1.445 |
| 0.02720 | 0.807212 | 14801.893 | 0.961 |
| 0.02780 | 0.807351 | 14825.399 | 0.599 |

Birth Redshift、σ8、およびCluster数はλ_growthに対して連続的かつ単調な変化を示した。

---

## Birth Surface Reproducibility

Birth Surfaceの再現解析を実施し、Cross GeometryからBirth Redshiftを安定して再現できることを確認した。

代表例：

- λ_growth = 0.02460
- Birth Bracket = 2.2147 – 2.2449
- Birth Redshift ≈ 2.230

Birth SurfaceはPhase H28の結果と整合し、高い再現性を示した。

---

## External Validation

H29ではMaster Equationを構築し、Birth Redshift、σ8、およびCluster数を同時に近似した。

検証結果は以下の通りである。

| Quantity | RMS Error |
|----------|----------:|
| Birth Redshift | 約0.031 |
| σ8 | 約2×10⁻⁵ |
| Total Clusters | 約3.4 |

これにより、State Variable間に強い経験的相関が存在することを確認した。

---

## SO_sim_0 Audit

CNCLike解析にはcosmocnc付属のSO_sim_0モックカタログを使用した。

監査の結果、

SO_sim_0のfiducial cosmologyは現時点では確認できなかった。

そのため、

CNCLike解析は観測制約ではなく、

「内部構造解析」

として扱う方針を採用した。

Observation解析との直接比較は行わない。

---

## Main Conclusions

Phase H29では以下を確認した。

- Planck2018固定背景宇宙論でBirth Surfaceを再現した。
- Observation解析とBirth Surface解析の整合性を確認した。
- Master Equationによる経験的再現式を構築した。
- SO_sim_0は内部構造解析として位置付けた。
- Observation解析とCNCLike解析を明確に区別する方針を採用した。

これらの成果はPhase H30以降のObservation解析およびState Space構築の基礎となった。
(To be completed)

---

# Phase H30 — Observation Minimum Region
## Objectives

Phase H30では、Planck2018 Baseline Cosmologyの下で、Observation解析・CNCLike解析・Birth Surfaceを同一のλ_growth系列で統一的に評価した。

主な目的は以下の4点である。

- Observation Minimum Regionの特定
- SO_sim_0（CNCLike）の探索
- Birth Surface消失条件の確認
- Observation解析とCluster解析の関係整理

---

## Fixed Cosmology

背景宇宙論はPlanck2018 Baselineを固定した。

| Parameter | Value |
|-----------|------:|
| H0 | 67.36 |
| ombh2 | 0.02237 |
| omch2 | 0.12000 |
| ns | 0.965 |
| tau | 0.0544 |
| logA | 3.05 |

FDE側では

- fde_eps_mu
- fde_lambda_mem
- fde_alpha
- fde_kd
- fde_ac
- fde_da

を固定し、

λ_growthのみ変更した。

---

## Observation Scan

λ_growth = 0.0246〜0.0290の広域スキャン、および0.0270〜0.0275の高密度スキャンを実施した。

Observation χ²は

λ_growth ≈ 0.0265〜0.0272

においてほぼ一定の最小領域を形成することを確認した。

この結果から、

**Observation ChampionではなくObservation Minimum Region**

として扱う方針を採用した。

---

## Birth Surface

Birth Surface解析では

| λ_growth | Birth Status |
|-----------|--------------|
| 0.0280 | Birth確認 |
| 0.0290 | Birth消失 |

となり、

Birth Surfaceは

**λ≈0.028〜0.029**

の区間で消失することを確認した。

Cross Geometryも同時に消失したことから、

Birth SurfaceとCross Geometryは密接に対応することが示された。

---

## SO_sim_0 Analysis

CNCLike解析では、

λ_growthの増加に伴いχ²_CNCLikeは探索範囲内で単調に改善した。

一方、

SO_sim_0のfiducial cosmologyは未確認である。

そのため、

Observation解析とCNCLike解析は独立に扱う方針を採用した。

現段階では総合Championは定義しない。

---

## Main Conclusions

Phase H30では以下を確立した。

- Observation Minimum Regionを定義した。
- Birth Surface消失条件を確認した。
- Cross Geometry消失とBirth Surface消失の対応を確認した。
- SO_sim_0解析は内部構造解析として位置付けた。
- Observation解析とCNCLike解析を統合しない方針を正式に採用した。

この成果はPhase H31におけるObservation Layerの整理、およびPhase H32のState Space構築の基盤となった。
(To be completed)

---

# Phase H31 — Observation Layer
# Phase H31 — Observation Constraint and Master Table（2026-06）

## Objectives

Phase H31では、Phase H28〜H30までに取得したObservation解析・CNCLike解析・Birth解析を統合し、Observation χ²によるλ_growth制約を評価するとともに、H32以降のState Space解析の基盤となるMaster Tableを構築した。

---

## Fixed Cosmology

Planck2018 Baseline Cosmologyを固定した。

- H0 = 67.36
- ombh2 = 0.02237
- omch2 = 0.12000
- ns = 0.965
- tau = 0.0544
- logA = 3.05

固定FDEパラメータ

- fde_eps_mu = 0.075
- fde_lambda_mem = 4.25
- fde_alpha = 0.025
- fde_kd = 1000000
- fde_ac = 0.90
- fde_da = 0.05
- β_D = 1.5

探索自由度はλ_growthのみとした。

---

## Main Results

- Observation χ²を系統的に評価した。
- Observation・CNCLike・Birth・σ8・Clusterを統合したH31 Master Tableを完成した。
- H31 Master Tableは20 Universe（U001〜U020）で構成した。
- Observation χ²はλ_growth≈0.0272付近で極めて平坦なMinimum Regionを形成することを確認した。
- Observation単独ではλ_growthを一意に拘束できないことを確認した。

---

## Statistical Audit

Observation統計量を

χ²Observation
=
χ²CMB
+
χ²DES
+
χ²BAO
+
χ²SN

として定義した。

CNCLikeについてはCobaya出力を監査し、

chi2__CNCLike = -2logL

であることを確認した。

Joint量

J = χ²Observation + (-2logL)

を数学的目的関数として定義した。

なお、本PhaseではJoint Likelihood、AIC、BIC、Bayesian Evidence等の統計学的解釈は導入していない。

---

## Generated Files

主要成果物

- H31_master_table.csv
- FDE_Master_Feature_Table_v20.csv

解析コード

- H31_observation_fit.py
- H31_observation_constraint.py
- H31_joint_definition_audit.py
- H31_champion_definition.py

---

## Conclusions

Phase H31ではObservation Constraintを定量化するとともに、20 UniverseからなるMaster Tableを完成させた。

Observation・CNCLike・Birth・σ8・Clusterを単一データベースへ統合したことにより、Phase H32におけるFeature Correlation解析、Canonical State Vector構築、およびState Space解析の基盤を確立した。
---
(To be completed)

# Phase H32 — State Space

# Phase H32 — State Space Construction（2026-07）

## Objectives

Phase H32では、Phase H31までに構築した20 UniverseのMaster Tableを基盤として、FDE宇宙の状態空間（State Space）を構築した。

主な目的は以下の5点である。

- State Databaseの構築
- Feature Correlation解析
- Canonical State Vectorの導出
- Gradient解析による状態変化の評価
- H33以降のState Metric理論の基盤整備

---

## Input Database

Phase H31で完成した

- H31_master_table.csv

および

- FDE_Master_Feature_Table_v20.csv

を基礎データとして採用した。

Master Tableは20 Universe（U001〜U020）で構成される。

各Universeについて

- λ_growth
- Birth Redshift
- σ8
- Total Clusters
- Peak Value
- Low / Mid / High Fraction

などの特徴量を統合した。

---

## Feature Analysis

各UniverseについてFeature解析を実施した。

主な解析項目

- Peak Value
- Low Fraction
- Mid Fraction
- High Fraction
- Gradient
- Feature Correlation

その結果、

各特徴量はλ_growthに対して連続的かつ滑らかに変化し、State Space上に連続した構造を形成することを確認した。

---

## Canonical State Vector

Feature Correlation解析を行い、各特徴量間の相関を評価した。

その結果、

Birth、σ8、Peak Value、Mass Fractionを中心とした状態量により、宇宙状態を記述できることを確認した。

Canonical State Vectorは、State Spaceを表現する最小状態量として採用した。

---

## Gradient Analysis

State Space上でGradient解析を実施した。

各Universe間の状態変化率を比較した結果、

状態変化は不連続ではなく、滑らかな勾配場を形成することを確認した。

Critical RegionではGradientが大きく変化し、状態遷移領域の候補となることが示された。

---

## Main Results

Phase H32では以下を達成した。

- 20 UniverseからなるState Databaseを構築した。
- Master Feature Tableを完成した。
- Feature Correlation解析を実施した。
- Canonical State Vectorを導出した。
- Gradient解析によりState Spaceの連続性を確認した。

---

## Generated Files

主要成果物

- FDE_Master_Feature_Table_v20.csv
- FDE_Feature_Correlation_v1.csv
- FDE_Feature_Correlation_Ranking_v1.csv
- FDE_Gradient_Critical_v1.csv
- FDE_Gradient_Robustness_v1.csv
- FDE_State_Database_v1.csv
- FDE_State_Database_v2.csv
- FDE_State_Database_v3.csv

---

## Conclusions

Phase H32では、FDE宇宙を離散的な解析点ではなく、連続したState Spaceとして扱う枠組みを構築した。

Phase H25〜H32は観測・数値解析によるState Database構築の段階であり、Phase H33以降では、このState Spaceに対してState Metric、Distance、Curvature、Geodesicなどの数学的構造を導入し、FDE理論の幾何学的定式化へ進む。

(To be completed)

---

# Phase H35 Theory Freeze (2026-07-04)

## Phase Summary

Phase H33〜H35では、State Spaceの幾何学的基盤を整理し、
Growth Dynamicsを構築するための最小数学構造を完成させた。

H35では完全なGrowth Equationは導出せず、
その構築に必要な最小数学構造のみを理論的に確立した。

Theory Freezeを実施し、H36以降で物理機構を導入する方針を正式決定した。

---

## H35 Final Results

### D1–D6

- Minimal Control Variables
- Minimal Kinetic Term
- Minimal Potential
- Minimal State Action
- Minimal State Lagrangian
- Variational Principle

完成。

### D7

Euler–Lagrange方程式より

d²Q/dτ² + kQ = 0

を導出。

これはState Space上の最小State Dynamicsであり、
宇宙論的Growth Equationとは区別する。

---

### D8

Observation Mappingを導入。

State VariableからObservation Spaceへの
局所写像を定義。

---

### D9

Local Reparameterizationを導入。

採用した最小条件

- Local Invertibility
- Monotonicity
- C¹ Smoothness

τ=f(a)の具体形はH36以降で決定する。

---

### D10

Structural Conditions for Constructing the Cosmological Growth Equation

以下の三つの局所構造が

- State Dynamics
- Observation Mapping
- Local Reparameterization

互いに矛盾なく同時に定義可能であることを示した。

---

### D11

Minimal Structural Proposition

H35では、

Growth Equationそのものではなく、

Growth Dynamicsを構成するための
最小数学構造が同時に定義可能であること

を命題として整理した。

---

## Terminology

正式採用

- State Dynamics
- Growth Dynamics
- Background Dynamics
- Observation Mapping
- Constructibility
- Local Linear Prototype
- CAMB Interface

採用しない用語

- Emergence
- Correspondence Principle
- Projection to CAMB
- Generate
- Produce
- Create

---

## Git Freeze

Repository

4chgreen/-cosmocnc

Commit

a1f7fcd

Commit message

Freeze H35 v1.0: Minimal mathematical foundation

GitHub Push

Completed

---

## Conclusions

H35では、

State Space上にGrowth Dynamicsを構成するための
最小数学構造を確立した。

これにより、

Background Dynamics

Memory Field

Geometry Coupling

Effective Gravity

Dissipation

Mode Interaction

をH36以降で順次導入するための理論基盤が完成した。

---

## Next Phase

Phase H36

- Background Dynamics
- Memory Field
- Geometry Coupling
- Effective Gravity
- Dissipation
- Mode Interaction
- Complete Growth Equation
- CAMB / Cobaya implementation
