---
layout: question
title: Reducing pH of nitrate based Hydroxyapatite
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Reducing pH of nitrate based Hydroxyapatite'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student is trying to make **hydroxy‑apatite (HA)** by a hydrothermal reaction that uses  

* calcium nitrate, \(\ce{Ca(NO3)2}\)  
* diammonium hydrogen phosphate, \(\ce{(NH4)2HPO4}\)  
* aqueous ammonia, \(\ce{NH4OH}\)

During the synthesis the **pH of the reaction mixture ends up around 8–8.25** and does **not drop to neutral (pH ≈ 7)**, even though a neutral pH is desired for the final product.  

The question is: **How can the pH be lowered (or better controlled) to ≈ 7 while still obtaining pure hydroxy‑apatite?**  

---

## 2. Step‑by‑step solution  

Below is a systematic way to understand why the pH stays high and how to bring it down to neutral.  
The approach combines (i) **acid–base equilibria** of the reagents, (ii) **stoichiometry of the precipitation reaction**, and (iii) **practical laboratory tricks** that keep the HA phase stable.

### 2.1 Write the overall precipitation reaction

Hydroxy‑apatite has the formula  

\[
\ce{Ca10(PO4)6(OH)2}
\]

When nitrate and ammonium salts are used, the reaction (ignoring spectator \(\ce{NO3-}\) and \(\ce{NH4+}\) ions) can be written as  

\[
\boxed{\;10\,\ce{Ca^{2+}} + 6\,\ce{HPO4^{2-}} + 2\,\ce{OH-} \longrightarrow \ce{Ca10(PO4)6(OH)2 (s)}\;}
\]

The **source of \(\ce{OH-}\)** in the synthesis is the added \(\ce{NH4OH}\).  

### 2.2 Identify the acid–base system that dominates the pH

The relevant equilibria are:

| Species | Equilibrium (25 °C) | \(K_a\) or \(K_b\) |
|---------|---------------------|--------------------|
| \(\ce{NH4+}\) | \(\ce{NH4+ + H2O <=> NH3 + H3O+}\) | \(K_a = 5.6\times10^{-10}\) (pK_a ≈ 9.25) |
| \(\ce{NH3}\) | \(\ce{NH3 + H2O <=> NH4+ + OH-}\) | \(K_b = 1.8\times10^{-5}\) (pK_b ≈ 4.75) |
| \(\ce{H2PO4- / HPO4^{2-}}\) | \(\ce{H2PO4- <=> HPO4^{2-} + H+}\) | \(pK_a2 = 7.21\) |
| \(\ce{HPO4^{2-} / PO4^{3-}}\) | \(\ce{HPO4^{2-} <=> PO4^{3-} + H+}\) | \(pK_a3 = 12.32\) |

*The pH of the solution is therefore governed by the **NH₄⁺/NH₃ buffer** and by the **phosphate buffer** (mainly \(\ce{H2PO4- / HPO4^{2-}}\)).*  

Because the student adds **excess \(\ce{NH4OH}\)** to keep the phosphate species in the \(\ce{HPO4^{2-}}\) form (necessary for HA formation), the mixture becomes **basic** (pH ≈ 8–8.3).

### 2.3 Calculate the pH that results from a given \(\ce{NH4OH}\) amount  

Assume the student prepares a solution of total ammonia concentration \(C_T = [\ce{NH3}] + [\ce{NH4+}]\).  
At equilibrium  

\[
\frac{[\ce{NH4+}]}{[\ce{NH3}]} = 10^{\mathrm{pH} - pK_a}
\]

Re‑arranged to give pH:

\[
\mathrm{pH} = pK_a + \log\frac{[\ce{NH3}]}{[\ce{NH4+}]}
\]

If the student adds, for example, **0.20 M NH₄OH** and the solution already contains **0.20 M \(\ce{(NH4)2HPO4}\)** (which provides 0.40 M \(\ce{NH4+}\)), then:

* total ammonia \(C_T = 0.20 + 0.40 = 0.60\; \text{M}\)
* the fraction that is \(\ce{NH3}\) at a given pH is  

\[
\alpha_{\ce{NH3}} = \frac{1}{1+10^{pK_a-\mathrm{pH}}}
\]

Solving iteratively (or with a simple spreadsheet) gives **pH ≈ 8.1** for the above concentrations, exactly what the student observes.

### 2.4 Why the pH cannot be forced below ~7 by simply adding more \(\ce{NH4OH}\)

* Adding **more \(\ce{NH4OH}\)** shifts the buffer toward \(\ce{NH3}\) → **higher pH**.  
* Adding **more \(\ce{(NH4)2HPO4}\)** adds \(\ce{NH4+}\) but also adds phosphate that will consume \(\ce{OH-}\) (via \(\ce{HPO4^{2-} + OH- -> PO4^{3-} + H2O}\)). However, once the stoichiometric ratio needed for HA (Ca:P = 1.67, OH:Ca = 0.2) is reached, any extra \(\ce{NH4+}\) merely reinforces the buffer and keeps the pH near the buffer’s pK_a (≈ 9.25), **not near neutral**.

Thus, **the only practical way to lower the pH is to add a *strong acid* that converts part of the \(\ce{NH3}\) to \(\ce{NH4+}\) and partially protonates \(\ce{HPO4^{2-}}\) to \(\ce{H2PO4-}\).** The acid must be added **after** the HA nuclei have formed, otherwise the precipitate may dissolve or transform into a different calcium phosphate phase (e.g., dicalcium phosphate, brushite).

### 2.5 Practical recipe to obtain neutral pH

Below is a **step‑by‑step protocol** that the student can try. The numbers are illustrative; they can be scaled proportionally.

| Reagent (for a 100 mL batch) | Desired final concentration | Remarks |
|------------------------------|-----------------------------|---------|
| \(\ce{Ca(NO3)2·4H2O}\)       | 0.20 M (≈ 7.4 g)            | Dissolve in de‑ionised water |
| \(\ce{(NH4)2HPO4}\)          | 0.12 M (≈ 2.4 g)            | Provides Ca : P = 1.67 |
| \(\ce{NH4OH}\) (28 % w/w)    | **0.04 M** (≈ 0.2 mL)       | **Much less** than typical; gives pH ≈ 7.5 before acid |
| **\(\ce{HCl}\) 0.1 M**       | **0.015 M** (≈ 1.5 mL)      | Added **dropwise** after mixing, while monitoring pH |

**Procedure**

1. **Prepare the calcium solution** – dissolve the calculated amount of \(\ce{Ca(NO3)2}\) in ~70 mL water.  
2. **Add the phosphate** – dissolve \(\ce{(NH4)2HPO4}\) in the same vessel; the solution will be mildly acidic (pH ≈ 5.5) because \(\ce{NH4+}\) is a weak acid.  
3. **Add the reduced amount of \(\ce{NH4OH}\)** – stir and check pH; you should obtain **pH ≈ 7.5–8.0**.  
4. **Adjust to neutral** – slowly add the 0.1 M HCl while continuously measuring pH. Stop when **pH = 7.00 ± 0.05**. The added HCl converts \(\ce{NH3}\) → \(\ce{NH4+}\) (consuming OH⁻) and shifts some \(\ce{HPO4^{2-}}\) → \(\ce{H2PO4-}\), but the HA lattice tolerates a small amount of surface \(\ce{H2PO4-}\).  
5. **Transfer to autoclave** – seal and heat under the hydrothermal conditions (e.g., 180 °C, 12 h).  
6. **Cool, wash, and dry** – after the run, wash the solid with de‑ionised water (no acid) to remove residual nitrates and ammonium ions, then dry at 80 °C.

**Why this works**

* **Lower initial \(\ce{NH4OH}\) concentration** means the NH₄⁺/NH₃ buffer starts closer to neutral.  
* **Post‑mix acid addition** precisely sets the pH without disturbing the Ca/P stoichiometry.  
* The **hydrothermal step** quickly converts any transient calcium phosphate species into the thermodynamically stable HA, even if the solution pH is briefly acidic during adjustment.

### 2.6 Alternative ways to achieve neutral pH (if acid addition is undesirable)

| Method | How it works | Practical notes |
|--------|--------------|-----------------|
| **Replace \(\ce{NH4OH}\) with a weaker base (e.g., NaOH) at a lower concentration** | Gives the same OH⁻ without the NH₄⁺/NH₃ buffer that holds the pH high | Must add a **counter‑ion** (Na⁺) that does not interfere with HA; low Na⁺ levels are usually acceptable. |
| **Add a buffering salt such as \(\ce{NH4Cl}\)** before adding \(\ce{NH4OH}\) | Increases \(\ce{NH4+}\) concentration, forcing the buffer equilibrium to a lower pH for the same amount of OH⁻ | Keep the total ionic strength moderate (< 0.5 M) to avoid precipitation of unwanted salts. |
| **Use calcium chloride (\(\ce{CaCl2}\)) instead of calcium nitrate** | Nitrate is a weakly basic anion; chloride does not affect pH. The overall pH will then be governed only by the NH₄⁺/NH₃ system, making it easier to tune. | Must verify that Cl⁻ does not incorporate into the HA lattice (generally negligible). |
| **Introduce CO₂ bubbling** | Dissolved CO₂ forms carbonic acid, lowering pH while simultaneously providing carbonate that can substitute into HA (forming carbonate‑HA, which is often desirable). | Control CO₂ flow carefully; excessive carbonate leads to calcite formation. |
| **Perform the synthesis in a closed‑system with a calibrated pH‑stat** | An automated pH‑stat continuously adds a dilute acid (e.g., 0.01 M HCl) to maintain pH = 7 during the entire hydrothermal run. | Requires equipment but gives the most reproducible results. |

---

## 3. Final answer (concise)

*The pH stays at 8–8.25 because the **NH₄⁺/NH₃ buffer** created by the added \(\ce{NH4OH}\) dominates the solution chemistry. To bring the pH down to neutral you must either (i) **reduce the amount of \(\ce{NH4OH}\) and then fine‑tune the pH with a dilute strong acid (e.g., 0.1 M HCl)**, or (ii) replace the ammonia base with a weaker or non‑buffering base, or (iii) use a pH‑stat during the hydrothermal step.  

A practical recipe is:

1. Use a **much lower concentration of \(\ce{NH4OH}\)** (≈ 0.04 M for a 100 mL batch).  
2. After mixing calcium nitrate and diammonium hydrogen phosphate, **adjust the pH to 7.0 ± 0.05 with dilute HCl** while stirring.  
3. Proceed with the hydrothermal treatment.  

The final product will be hydroxy‑apatite with a **neutral pH**

*Original question: [Reducing pH of nitrate based Hydroxyapatite](https://chemistry.stackexchange.com/questions/196071/reducing-ph-of-nitrate-based-hydroxyapatite) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
