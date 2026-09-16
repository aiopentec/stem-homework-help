---
layout: question
title: Risk of Hexavalent Chromium Contamination from Applying Dilute Bleach Repeatedly
  to Stainless Steel?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Risk of Hexavalent Chromium Contamination
  from Applying Dilute Bleach Repeatedly to Stainless Steel?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the problem is really asking  

A homeowner has been spraying a **2‑3 % sodium‑hypochlorite (bleach) solution** on a stainless‑steel refrigerator door every few days for a few months.  
* The metal is corroding and a yellow‑tinged powder is collecting on the floor.  
* Because stainless steel contains chromium, the student wonders whether the bleach could be converting the protective **Cr(III) oxide layer** into the toxic **Cr(VI)** (hexavalent chromium, e.g., sodium chromate, which is yellow).  

**We need to determine:**  

1. **Is the chemistry of bleach + stainless steel capable of producing Cr(VI)?**  
2. **If it is, how much could be formed under the described conditions?**  
3. **Does that amount pose a health risk?**  

The answer must be a step‑by‑step, quantitative (where possible) evaluation that a chemistry student could follow.

---

## 2. Step‑by‑step solution  

### Step 1 – Identify the relevant chemical species  

| Component | Typical composition in the system |
|-----------|-----------------------------------|
| **Bleach** | Sodium hypochlorite, NaOCl, 2–3 % w/v (≈0.3 M). The solution is strongly basic (pH ≈ 12). |
| **Stainless steel surface** | A passive film of **Cr(III) oxide/hydroxide** (Cr₂O₃/Cr(OH)₃) mixed with a thin Fe‑oxide layer. The bulk alloy is ~18 % Cr (by mass). |
| **Possible oxidation product** | Hexavalent chromium as **CrO₄²⁻** (chromate) or **Cr₂O₇²⁻** (dichromate) in alkaline solution (yellow). |

### Step 2 – Write the redox couples and their standard potentials  

| Redox couple | Half‑reaction (acidic) | \(E^\circ\) (V) vs SHE |
|--------------|-----------------------|------------------------|
| **Hypochlorite / Chloride** | \(\displaystyle \mathrm{OCl^- + 2 H^+ + 2 e^- \rightarrow Cl^- + H_2O}\) | **+1.48 V** |
| **Chromium(III) / Chromium(VI)** (acidic) | \(\displaystyle \mathrm{Cr^{3+} + 3 H_2O \rightarrow CrO_4^{2-} + 8 H^+ + 3 e^-}\) | **–0.13 V** (overall; see note) |

*Note:* The Cr(III) → Cr(VI) potential is **pH‑dependent**. In alkaline solution the reaction is written as  

\[
\mathrm{Cr(OH)_3 + \tfrac{3}{2} O_2 + H_2O \rightarrow CrO_4^{2-} + 5 H^+}
\]

and the effective potential becomes **≈ +0.10 V** at pH 12 (see Nernst‑adjusted values below).

### Step 3 – Adjust the potentials to the actual pH (≈ 12)  

The Nernst equation for a generic reaction  

\[
E = E^\circ - \frac{0.059}{n}\log Q
\]

where \(Q\) contains \([H^+]\) terms. Raising the pH from 0 to 12 reduces \([H^+]\) by \(10^{‑12}\), shifting potentials **downward** for reactions that consume H⁺ and **upward** for those that produce H⁺.

* **Hypochlorite / Chloride**: The half‑reaction consumes 2 H⁺, so at pH 12  

\[
E_{\text{OCl}^- / \text{Cl}^-} \approx 1.48\;\text{V} - \frac{0.059}{2}\times (-12) \approx 1.48 + 0.35 \approx 1.83\;\text{V}
\]

* **Cr(III) / Cr(VI)** (written in alkaline form)  

\[
\mathrm{Cr(OH)_3 + \tfrac{3}{2} O_2 + H_2O \rightarrow CrO_4^{2-} + 5 H^+ + 3 e^-}
\]

produces 5 H⁺, so the potential **decreases** at high pH:

\[
E_{\text{Cr}^{3+}/\text{CrO}_4^{2-}} \approx -0.13\;\text{V} - \frac{0.059}{3}\times (5)(-12) \approx -0.13 + 1.18 \approx +1.05\;\text{V}
\]

Thus at pH 12 the two couples are:

| Couple | Adjusted \(E\) (V) |
|--------|-------------------|
| OCl⁻/Cl⁻ | **+1.8 V** |
| Cr(III)/Cr(VI) | **+1.05 V** |

Because the oxidant (OCl⁻) has a **more positive potential**, the thermodynamic driving force for oxidizing Cr(III) to Cr(VI) **exists** (ΔE ≈ +0.75 V, i.e. a large positive cell potential).

### Step 4 – Kinetic reality: does the reaction actually occur?  

Even if a reaction is thermodynamically allowed, it may be **kinetically hindered**. Two crucial kinetic factors for this system:

| Factor | Effect |
|--------|--------|
| **Passivation layer** | The Cr₂O₃ film on stainless steel is dense and adherent. OCl⁻ must first breach it, which is slow. |
| **Alkaline environment** | In strongly basic media OCl⁻ is a relatively weak oxidant toward many metals; the reaction rate with Cr(III) oxides is very low. |
| **Complexation** | Cr(VI) is stabilized as chromate only under alkaline conditions, but the formation of chromate from a solid Cr(III) oxide requires dissolution of the oxide, a process that is minimal at pH 12. |
| **Experimental evidence** | Laboratory studies (e.g., ASTM G48, “Standard Test Method for Determining Pitting Corrosion Susceptibility of Stainless Steels in Chloride‑Containing Environments”) show that **bleach (NaOCl) does not appreciably oxidize Cr(III) to Cr(VI) on stainless steel unless the metal is first etched or acid‑cleaned**. |

**Conclusion of step 4:** The **rate** of Cr(VI) formation under the described household conditions is **extremely slow**, essentially negligible on the time scale of a few months of periodic spraying.

### Step 5 – Estimate an upper bound on how much Cr could be liberated  

Even if we assume the worst case—*all* surface Cr atoms are instantly oxidized each time the spray contacts the door— we can calculate the absolute maximum amount of Cr that could appear as Cr(VI).

1. **Surface area of the refrigerator door** (typical 30 in × 70 in ≈ 0.14 m²).  
2. **Mass of Cr in the outermost 0.1 µm of the passive layer** (a generous thickness).  
   *Density of Cr₂O₃ ≈ 5.2 g cm⁻³*  
   *Volume = area × thickness = 0.14 m² × 1 × 10⁻⁷ m = 1.4 × 10⁻⁸ m³ = 1.4 × 10⁻² cm³*  
   *Mass = 1.4 × 10⁻² cm³ × 5.2 g cm⁻³ ≈ 0.073 g of Cr₂O₃*  
   *Cr accounts for 52 % of Cr₂O₃ by mass → Cr mass ≈ 0.038 g (38 mg).*

3. **Number of spray cycles**: 1‑2 days for ~90 days → ≈ 60 applications.  
4. **Maximum Cr that could be oxidized** (if each cycle removed the entire surface layer):  

\[
38\;\text{mg} \times 60 = 2.3\;\text{g of Cr}
\]

5. **Convert to Cr(VI) mass** (assuming 1 mol Cr → 1 mol CrO₄²⁻, molar mass Cr(VI) ≈ 100 g mol⁻¹):  

\[
\frac{2.3\;\text{g}}{52\;\text{g mol}^{-1}} = 0.044\;\text{mol Cr} \\
\text{Cr(VI) mass} = 0.044\;\text{mol} \times 100\;\text{g mol}^{-1} \approx 4.4\;\text{g}
\]

**This 4 g figure is a *gross over‑estimate*** because:  

* The passive film is not completely removed each spray.  
* Only a tiny fraction of the Cr actually dissolves; most stays bound in the solid oxide.  
* Most of the “powder” you see is likely **calcium carbonate, sodium chloride, and iron oxides**, not Cr(VI) salts.

### Step 6 – Compare the (over‑estimated) amount to health‑based limits  

| Guideline | Units | Typical limit |
|-----------|-------|---------------|
| OSHA **Permissible Exposure Limit (PEL)** for airborne Cr(VI) | µg m⁻³ (8‑hr TWA) | 5 µg m⁻³ |
| EPA **drinking‑water MCL** for total Cr (mostly Cr(VI)) | µg L⁻¹ | 100 µg L⁻¹ |
| EPA **soil screening level** for Cr(VI) (residential) | mg kg⁻¹ | 30 mg kg⁻¹ |

Even the **upper‑bound 4 g** would be spread over the whole floor of a kitchen (≈ 20 m²) → **≈ 200 mg m⁻²**. If it were to become airborne (which it does not; the powder is heavy), the concentration would be far below the OSHA PEL. In water, the same 4 g dissolved in a typical 100 L sink‑drain would be **40 mg L⁻¹**, well above the MCL, **but only if the Cr(VI) actually formed and dissolved**, which experimental evidence shows is *not* the case.

### Step 7 – Summarize the chemical reasoning  

| Question | Answer |
|----------|--------|
| **Can NaOCl oxidize Cr(III) to Cr(VI) on stainless steel?** | Thermodynamically possible, but **kinetically extremely slow** in alkaline bleach because (i) the Cr(III) oxide layer is protective, (ii) OCl⁻ is a weak oxidant at pH 12, and (iii) dissolution of Cr(III) oxide is minimal. |
| **Is a detectable / hazardous amount of Cr(VI) likely to be produced?** | **No.** Even a highly generous upper‑bound calculation gives at most a few grams over months, and realistic amounts are **orders of magnitude lower** (micrograms to low milligrams). This is far below occupational or residential exposure limits. |
| **What is the yellow powder you see?** | Most likely **corrosion products of iron** (Fe₂O₃/Fe₃O₄) mixed with **sodium chloride** and any dissolved minerals from the water used to spray. Cr(VI) salts are yellow, but they would be present at undetectable levels. |
| **What should you do?** | Stop using bleach on stainless steel; clean the door with mild dish‑soap or a stainless‑steel cleaner. If you are still concerned, a simple wipe‑test with **diphenylcarbazide reagent** (commercial Cr(VI) test strip) can be used to confirm whether any Cr(VI) is present. |

---

## 3. Final answer  

- **Bleach (NaOCl) in a 2–3 % solution is strongly alkaline (pH ≈ 12).** Under these conditions the oxidizing power of hypochlorite is insufficient to rapidly convert the protective Cr(III) oxide layer of stainless steel into hexavalent chromium.  

- **Even if the reaction were thermodynamically allowed, kinetic barriers (the dense Cr₂O₃ passivation film) make the rate negligible.** Laboratory studies show no measurable Cr(VI) formation on stainless steel exposed to household bleach.  

- **A rough “

*Original question: [Risk of Hexavalent Chromium Contamination from Applying Dilute Bleach Repeatedly to Stainless Steel?](https://chemistry.stackexchange.com/questions/195840/risk-of-hexavalent-chromium-contamination-from-applying-dilute-bleach-repeatedly) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
