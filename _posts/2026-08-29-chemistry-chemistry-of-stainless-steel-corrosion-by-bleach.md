---
layout: question
title: Chemistry of stainless steel corrosion by bleach
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Chemistry of stainless steel corrosion
  by bleach'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. Restating the question in plain language  

A student wants to know what actually happens when **bleach (aqueous NaOCl)** contacts **stainless steel**.  

* Stainless steel is an alloy that contains iron (Fe), chromium (Cr) and sometimes nickel (Ni).  
* The alloy’s corrosion‑resistance comes from a thin, self‑healing surface film of **chromium(III) oxide, Cr₂O₃**.  
* When bleach is added, does the powerful oxidiser **hypochlorite (ClO⁻)** attack both Fe and Cr equally, or is one of them attacked faster (kinetically favored) while the other remains protected?  

We need to write the relevant redox half‑reactions, look at their standard potentials, consider the passivation layer, and decide which metal will dissolve (or be oxidised) under typical bleach conditions (pH ≈ 11–12, ~0.5–5 % NaOCl).

---

## 2. Step‑by‑step solution  

### 2.1. What is “bleach” chemically?  

Commercial bleach is an aqueous solution of **sodium hypochlorite**:

\[
\ce{NaOCl -> Na+ + OCl-}
\]

In water the hypochlorite ion exists in equilibrium with hypochlorous acid (HOCl):

\[
\ce{OCl- + H2O <=> HOCl + OH-} \qquad K_\mathrm{a}\approx 3\times10^{-8}
\]

At the high pH of bleach (≈ 11–12) the equilibrium lies far to the left, so the dominant oxidiser is **OCl⁻**.  

The overall redox couple we are interested in is  

\[
\ce{ClO- + H2O + 2 e- <=> Cl- + 2 OH-}
\]

Standard potential (E°) at pH 14 (i.e. in 1 M OH⁻) is **+0.89 V** vs SHE (standard hydrogen electrode).  
If we express it at pH 0 (acidic) the potential is **+1.48 V**. The high value shows that hypochlorite is a strong oxidiser for many metals.

### 2.2. Possible oxidation reactions of the alloy components  

| Metal (oxidation state) | Possible oxidation half‑reaction (acidic) | E° (V) vs SHE* |
|--------------------------|-------------------------------------------|----------------|
| Fe → Fe²⁺                | \(\ce{Fe -> Fe^{2+} + 2 e-}\)              | –0.44 |
| Fe → Fe³⁺                | \(\ce{Fe -> Fe^{3+} + 3 e-}\)              | –0.04 |
| Cr → Cr³⁺                | \(\ce{Cr -> Cr^{3+} + 3 e-}\)              | –0.74 |
| Cr → CrO₄^{2-} (oxidation to +6) | \(\ce{CrO4^{2-} + 3 e- + 4 H2O -> Cr(OH)3 + 5 OH-}\) (reverse) | +0.13 (as reduction) |
| Ni → Ni²⁺                | \(\ce{Ni -> Ni^{2+} + 2 e-}\)              | –0.25 |

\*Values are for standard conditions (1 M, pH 0). For alkaline media the potentials shift by \(-0.059\,\text{V}\times \text{pH}\) per electron transferred (Nernst equation).  

**Key observations**

* The **standard oxidation potential of Fe → Fe²⁺** is **–0.44 V**, i.e. Fe is *easily* oxidised (negative sign means Fe wants to lose electrons).  
* **Cr → Cr³⁺** is even more negative (–0.74 V), meaning Cr metal is *thermodynamically* a stronger reducing agent than Fe.  
* However, the **passivation layer** of **Cr₂O₃** (or Cr(OH)₃ under alkaline conditions) blocks the direct oxidation of Cr metal.  

### 2.3. Role of the protective Cr₂O₃ film  

* Cr₂O₃ is a **stable, insoluble oxide** that adheres strongly to the alloy surface.  
* In alkaline solution it can transform to **chromate (CrO₄²⁻)** or **hydroxochromate (Cr(OH)₄⁻)** only at **high pH and high oxidising potential**.  
* The film is **self‑healing**: if a defect forms, dissolved Cr(III) ions from the alloy re‑oxidise (by O₂ or OCl⁻) to Cr(III) hydroxide/oxide and reseal the spot.  

Thus, as long as the Cr₂O₃ layer stays intact, **Cr atoms beneath it are kinetically protected** from direct attack by hypochlorite.

### 2.4. What does hypochlorite actually oxidise?  

Because the Cr₂O₃ layer blocks Cr, the **most accessible species** for OCl⁻ are:

1. **Fe atoms at surface imperfections** (scratches, grain boundaries, pits) where the Cr‑oxide is thin or absent.  
2. **Fe(II) that may already be present** (e.g., from prior corrosion).  
3. **Ni (if present)**, which is less noble than Fe but more noble than Cr.

The net reaction for Fe oxidation by hypochlorite in alkaline solution can be written as:

\[
\begin{aligned}
\text{Oxidation (Fe)} &: \ \ce{Fe + 2 OH- -> Fe(OH)2 + 2 e-} \\
\text{Reduction (hypochlorite)} &: \ \ce{OCl- + H2O + 2 e- -> Cl- + 2 OH-} \\
\hline
\text{Overall} &: \ \ce{Fe + OCl- + H2O -> Fe(OH)2 + Cl-}
\end{aligned}
\]

If enough OCl⁻ is present, Fe(OH)₂ can be further oxidised to Fe(III) hydroxide/oxide:

\[
\ce{Fe(OH)2 + OCl- + H2O -> Fe(OH)3 + Cl-}
\]

**Resulting corrosion products** are typically **hydrated iron(III) oxides** (Fe₂O₃·nH₂O, FeOOH) that are **rust‑colored** and **soluble enough** to be washed away.  

### 2.5. Possibility of Cr oxidation (when the film is breached)  

If a defect allows OCl⁻ to contact **metallic Cr**, the thermodynamics favour oxidation to **Cr(III)** rather than Cr(VI) under the mildly alkaline conditions of bleach:

\[
\begin{aligned}
\ce{Cr + 3 OH- -> Cr(OH)3 + 3 e-} \qquad (E^\circ_\text{ox} = +0.74\ \text{V})\\
\ce{OCl- + H2O + 2 e- -> Cl- + 2 OH-} \qquad (E^\circ = +0.89\ \text{V})
\end{aligned}
\]

Balancing electrons (multiply Cr half‑reaction by 2, OCl⁻ half‑reaction by 3) gives:

\[
\boxed{\ce{2 Cr + 3 OCl- + 3 H2O -> 2 Cr(OH)3 + 3 Cl-}}
\]

**However**, the Cr(III) hydroxide quickly precipitates and **re‑forms the protective layer**, so the attack stops unless the environment is strongly complexing (e.g., high concentrations of carbonate, phosphate, or strong acids) that keep Cr(III) in solution.

If the solution is **very concentrated** (e.g., > 10 % NaOCl, pH < 10) and **heated**, the potential of OCl⁻ can reach values that oxidise Cr(III) to **chromate (CrO₄²⁻, Cr(VI))**:

\[
\ce{Cr(OH)3 + 3 OCl- + 3 OH- -> CrO4^{2-} + 3 Cl- + 4 H2O}
\]

But this is **rare in ordinary household bleach**; it requires aggressive conditions and the formation of Cr(VI) is kinetically slow.

### 2.6. Kinetic comparison – which metal is attacked faster?  

| Factor | Iron (Fe) | Chromium (Cr) |
|--------|-----------|---------------|
| **Thermodynamic drive** (E°) | Moderate (–0.44 V) | Stronger (–0.74 V) – would oxidise even more readily if exposed |
| **Surface protection** | No intrinsic passive film; relies on Cr₂O₃ coverage | Covered by a **stable Cr₂O₃** film that is self‑healing |
| **Observed rate in bleach** | **Fast** where film is imperfect; visible rust‑like staining | **Very slow**; only measurable when film is damaged, then quickly re‑passivates |
| **Overall practical outcome** | **Dominant corrosion product** is Fe(III) hydroxide/oxide | Cr remains largely as part of the protective oxide; negligible dissolution |

**Conclusion:** In typical bleach (≈ 5 % NaOCl, pH ≈ 11), **iron is the kinetically favoured target**. The Cr component stays protected by its oxide layer, and even if a few Cr atoms are oxidised, the newly formed Cr(III) hydroxide immediately rebuilds the passivation film.

### 2.7. Full picture of the corrosion process  

1. **Initial contact** – NaOCl solution wets the stainless surface.  
2. **Film integrity check** – Any scratches or micro‑cracks expose Fe (or Ni) atoms.  
3. **Electron transfer** – Fe atoms lose electrons; OCl⁻ gains them, producing Cl⁻ and OH⁻.  
4. **Hydrolysis** – Fe²⁺/Fe³⁺ hydrolyses to Fe(OH)₂ → Fe(OH)₃ → FeOOH/Fe₂O₃·nH₂O.  
5. **Film repair** – Dissolved Cr³⁺ from any oxidised Cr recombines with OH⁻ to reform Cr(OH)₃ → Cr₂O₃, sealing the spot.  
6. **Result** – Visible rust‑like discoloration where Fe has corroded; the bulk alloy remains largely unchanged because the Cr‑oxide layer survives.

---

## 3. Final answer  

- **Hypochlorite (OCl⁻) is a strong oxidiser that can oxidise both Fe and Cr.**  
- **In practice, the Cr in stainless steel is protected by a self‑healing Cr₂O₃ (or Cr(OH)₃) surface film.**  
- **Iron atoms at defects are oxidised much more quickly**, giving Fe(II) → Fe(III) hydroxides/oxides and releasing Cl⁻.  
- **Chromium oxidation is kinetically hindered**; only when the passive film is breached does Cr briefly form Cr(III) hydroxide, which instantly reforms the protective layer.  
- Consequently, **the corrosion of stainless steel by bleach is dominated by iron oxidation**, while chromium remains largely inert under normal household bleach conditions.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming both Fe and Cr dissolve at the same rate because their standard potentials are similar.** | Standard potentials ignore the protective oxide layer; kinetics dominate. | Always consider surface passivation and real‑world film stability, not just thermodynamics. |
| **Writing the hypochlorite reduction as \(\ce{Cl2 + 2 e- -> 2Cl-}\).** | In alkaline bleach the dominant species is \(\ce{OCl-}\), not molecular chlorine. | Use the correct half‑reaction \(\ce{OCl- + H2O + 2 e- -> Cl- + 2 OH-}\) for high‑pH conditions. |
| **Neglecting the effect of pH on potentials.** | Potentials shift by \(-0.059\text{ V}\times\text{pH}\) per electron; at pH 12 the effective E° for OCl⁻ is lower than the acidic value. | Apply the Nernst equation when dealing with strongly alkaline solutions. |
| **Claiming that bleach will convert Cr(III) to toxic Cr(VI) in ordinary use.** | Formation of Cr(VI) from Cr(III) by OCl⁻ is kinetically very slow and requires high temperature, high OCl⁻ concentration, and low pH. | State the required extreme conditions and note that normal household bleach does **not** produce measurable Cr(VI). |
| **Ignoring the role of nickel (Ni) when it’s present.** | Ni can also be oxidised, but its standard potential is less negative than Fe, so it corrodes slower. | Mention Ni only as a secondary pathway; focus on Fe as the primary corrosion partner. |

---

*Original question: [Chemistry of stainless steel corrosion by bleach](https://chemistry.stackexchange.com/questions/195895/chemistry-of-stainless-steel-corrosion-by-bleach) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
