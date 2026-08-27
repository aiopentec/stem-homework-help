---
layout: question
title: Are material strains additive or multiplicative?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Are material strains additive or multiplicative?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A 1‑m aluminium rod is first **cooled** so that it becomes **10 ppm shorter** (a strain of –10 × 10⁻⁶).  
After it is warmed back to room temperature it is **loaded** in tension so that it becomes **10 ppm longer** (a strain of +10 × 10⁻⁶).

*If the two actions are performed **together**, what is the total change in length?*  

The student wonders whether the two strains **add** (‑10 ppm + +10 ppm = 0) or **multiply** (1–10 ppm × 1+10 ppm ≈ 0.9999 → a 0.01 % shortening).  
The same question is raised for a much larger strain (±10 %).  

In other words: **Are strains additive or multiplicative?**  

---

## 2.  Detailed solution  

### 2.1.  Definitions  

| Symbol | Meaning |
|--------|----------|
| \(L_0\) | Original length (1 m) |
| \(\lambda\) | Stretch ratio = final length / original length |
| \(\varepsilon\) | Engineering strain = \((L-L_0)/L_0\) (dimensionless) |
| \(\alpha\) | Coefficient of linear thermal expansion (≈ 23 × 10⁻⁶ K⁻¹ for Al) |
| \(\Delta T\) | Temperature change |
| \(\sigma\) | Axial stress |
| \(E\) | Young’s modulus of aluminium (≈ 70 GPa) |

The **engineering strain** \(\varepsilon\) is additive for small deformations (the usual linear‑elastic regime).  
For **finite** deformations the true (logarithmic) strain or the stretch ratio \(\lambda\) is used and the *multiplicative* decomposition of deformation gradients becomes appropriate.

---

### 2.2.  Small‑strain case (≈ 10 ppm)

1. **Thermal strain**  
   \[
   \varepsilon_{\text{th}} = \alpha\,\Delta T
   \]
   The cooling was chosen so that \(\varepsilon_{\text{th}} = -10\times10^{-6}\).

2. **Mechanical strain** (tension)  
   \[
   \varepsilon_{\text{mech}} = \frac{\sigma}{E}
   \]
   The weight was chosen so that \(\varepsilon_{\text{mech}} = +10\times10^{-6}\).

3. **Superposition (additivity)**  
   In the linear‑elastic regime the total engineering strain is the **sum** of the individual strains:
   \[
   \varepsilon_{\text{total}} = \varepsilon_{\text{th}} + \varepsilon_{\text{mech}}
                               = (-10\times10^{-6}) + ( +10\times10^{-6}) = 0 .
   \]

4. **Resulting length**  
   \[
   L = L_0\,(1+\varepsilon_{\text{total}}) = 1\ \text{m}\times(1+0)=1.000\ \text{m}.
   \]

   **Conclusion:** For the realistic 10 ppm values the two effects cancel *exactly* (to the precision of the linear model). The cold‑plus‑loaded rod is the same length as the original.

---

### 2.3.  Large‑strain case (≈ 10 % change)

A 10 % strain is **not** “small” – the linear approximation is no longer accurate.  
We must work with the *stretch ratio* \(\lambda = 1+\varepsilon\) (or with true/logarithmic strain).

1. **Individual stretches**  

   * Thermal shrinkage: \(\lambda_{\text{th}} = 0.90\)  (10 % shorter).  
   * Mechanical elongation: \(\lambda_{\text{mech}} = 1.10\) (10 % longer).

2. **Multiplicative combination**  

   The total deformation gradient for a body subjected to two *sequential* deformations is the product of the individual stretch ratios:
   \[
   \lambda_{\text{total}} = \lambda_{\text{mech}}\,\lambda_{\text{th}}
                         = 1.10 \times 0.90 = 0.99 .
   \]

3. **Corresponding engineering strain**  

   \[
   \varepsilon_{\text{total}} = \lambda_{\text{total}} - 1 = 0.99 - 1 = -0.01
                               = -1\%.
   \]

4. **Resulting length**  

   \[
   L = L_0\,\lambda_{\text{total}} = 1\ \text{m}\times 0.99 = 0.99\ \text{m}.
   \]

   **Conclusion:** When the strain magnitude is large (10 %), the combined effect is **multiplicative**, giving a net 1 % shortening. The cold‑plus‑loaded rod is *shorter* than the original.

---

### 2.4.  Why the two regimes differ  

| Regime | Governing relation | Reason |
|--------|-------------------|--------|
| **Small strains** (\(|\varepsilon| \lesssim 10^{-3}\) i.e. < 0.1 %) | \(\varepsilon_{\text{total}} = \varepsilon_1 + \varepsilon_2\) | Linearised kinematics → superposition holds. |
| **Finite strains** (≥ ~1 %) | \(\lambda_{\text{total}} = \lambda_1\lambda_2\) (or \(\ln\lambda_{\text{total}} = \ln\lambda_1 + \ln\lambda_2\)) | Exact geometry of deformation; multiplication of deformation gradients is required. |

For *engineering practice* (most structural problems) strains are far below 0.1 %, so the **additive** rule is used.  
When dealing with *large* thermal expansions, soft polymers, rubber, shape‑memory alloys, or high‑precision metrology where strains approach a few percent, the **multiplicative** treatment is necessary.

---

## 3.  Final answer  

* **For realistic small strains (10 ppm, i.e. 10⁻⁵)** the thermal and mechanical contributions **add linearly**. The cold‑plus‑loaded rod returns to exactly its original length (to the accuracy of the linear model).  

* **For large strains (e.g., ±10 %)** the correct description is **multiplicative**: the total stretch is the product of the individual stretches, giving a net shortening of 1 % (the rod ends up 0.99 m long).  

Thus, **strains are additive only in the small‑strain (linear‑elastic) regime; for finite strains they combine multiplicatively**.

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming linear superposition for any size strain** | The linear relationship \(\varepsilon = \sigma/E\) is derived by neglecting higher‑order terms in the deformation gradient. It fails when \(|\varepsilon|\) approaches a few percent. | Check the magnitude of the strain. If \(|\varepsilon| < 10^{-3}\) (≈ 0.1 %), additive treatment is fine; otherwise use stretch ratios or true strain. |
| **Confusing engineering strain with true (logarithmic) strain** | Engineering strain \(\varepsilon = \Delta L/L_0\) is not additive for large deformations; true strain \(\varepsilon_{\text{true}} = \ln(1+\varepsilon)\) *is* additive. | For finite deformations convert to true strain, add, then exponentiate back to get the final stretch. |
| **Neglecting the order of operations** (e.g., heating then loading vs loading then heating) | In the finite‑strain regime the product \(\lambda_{\text{mech}}\lambda_{\text{th}}\) is commutative for pure axial stretches, but for more general deformations the order matters because deformation gradients do not commute. | Remember that the simple product works only for coaxial (same direction) stretches; for general cases use full deformation‑gradient multiplication. |
| **Using the coefficient of thermal expansion beyond its linear range** | \(\Delta L = \alpha L_0 \Delta T\) is linear only for modest \(\Delta T\). At very large temperature changes the material’s \(\alpha\) can vary with temperature. | Verify that \(\Delta T\) is small enough, or integrate \(\alpha(T)\) over the temperature interval. |
| **Treating Poisson’s effect as irrelevant** | Axial loading also causes lateral contraction; thermal expansion may be constrained, affecting the axial strain. | Include Poisson’s ratio if the rod is not free to expand laterally or if lateral constraints are present. |

---

*Original question: [Are material strains additive or multiplicative?](https://physics.stackexchange.com/questions/875414/are-material-strains-additive-or-multiplicative) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
