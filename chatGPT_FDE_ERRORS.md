# FDE-60 ERROR LOG
# Known pitfalls and implementation hazards

## ERROR-001
Problem:
Large negative lambda_growth improves sigma8
but destroys Planck TTTEEE fit.

Observed:
lambda_growth < -0.03
causes rapid chi2 increase.

Conclusion:
growth-only modification has structural tension
with lensing + TTTEEE.

---

## ERROR-002
Problem:
Overwriting total dgrho directly can break baryon sector.

Dangerous pattern:
dgrho = dgrho_matter * mu_fde

Reason:
This modifies all matter contributions blindly.

Correct approach:
Modify CDM contribution only.

Safe pattern:
dgrho_modified =
    grhoc_t * clxc * mu_fde
  + grhob_t * clxb

---

## ERROR-003
Problem:
evaluate sampler may appear non-deterministic
if nuisance parameters are not fixed.

Solution:
Use fully fixed nuisance YAML.

---

## ERROR-004
Problem:
Lambda convention confusion.

Correct convention:
lambda = physical length scale in Mpc

Always use:
k * lambda

Never:
k / lambda

---

## ERROR-005
Problem:
Phase A modifies growth equation only.

Result:
Potential Phi remains LCDM-like.

Implication:
lensing cannot be fully controlled.

Phase B required:
Modified Poisson sector.

---

## ERROR-006
Problem:
Overly large modifications destabilize TT peaks.

Observed:
High-l multipoles highly sensitive
to growth-sector forcing.

Implication:
Need smoother scale-dependent response.

---

## ERROR-007
Problem:
Phenomenological interpretation overstated.

Correction:
Current model is NOT a closed gravity theory.

Current status:
Phenomenological perturbation-sector model.

