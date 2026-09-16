---
layout: question
title: Conversion of 2,3-dihydroxy-thioxanthone to the corresponding ethyl halide
  ether
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Conversion of 2,3-dihydroxy-thioxanthone
  to the corresponding ethyl halide ether'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the student is trying to do (plain‑language restatement)

The starting material is **2,3‑dihydroxy‑thioxanthone** (a catechol fused to a thioxanthone skeleton).  
The goal is to replace **both phenolic OH groups** with **2‑halo‑ethyl ethers** so that the product looks like  

```
   O‑CH2‑CH2‑X
   |
   (thioxanthone core)
   |
   O‑CH2‑CH2‑X
```

where **X = Br** (or Cl). In other words we need a **bis‑(2‑haloethyl) ether** of the catechol.

The student has already tried:

* Direct SN2 alkylation with a protected ethyl‑tosylate – the first ether forms easily but the second is extremely sluggish and oxidation of the catechol occurs.
* Mitsunobu coupling of each phenol with a halo‑alcohol – the first coupling works, the second stalls even after days, and the reaction mixture is littered with phosphine‑oxide and DIAD‑derived by‑products that are hard to remove.

The problem therefore is **how to install the second 2‑haloethyl ether cleanly despite steric crowding and the oxidative sensitivity of the catechol**.

Below is a complete, step‑by‑step synthetic solution that avoids the pitfalls encountered so far.

---

## 2.  Worked solution (step‑by‑step)

### Overview of the chosen strategy  

1. **Mitsunobu coupling of each phenol with *unprotected* 2‑hydroxyethanol** → bis‑(2‑hydroxyethyl) ether.  
   *Why?* The primary alcohol is a far better nucleophile in the Mitsunobu reaction than a halide. Using the *same* reagent for both phenols guarantees identical reaction conditions for the two sites and eliminates the need for a protected (and sterically bulky) tosylate.  

2. **Conversion of the two primary alcohols to bromides** (or chlorides) by a clean Appel‑type halogenation (CBr₄/PPh₃) or by a two‑step mesylate‑then‑Finkelstein sequence.  
   *Why?* Both methods work under neutral, non‑basic conditions, preserving the thioxanthone core and avoiding oxidation of the catechol.  

3. **Optional work‑up / purification** – simple aqueous work‑up removes phosphine‑oxides, and flash chromatography on silica (with a small amount of Et₃N to suppress phenolic adsorption) gives the pure bis‑(2‑haloethyl) ether.

---

### Step 1 – Bis‑(2‑hydroxyethyl) ether via a *double* Mitsunobu reaction  

| Reagents (per phenolic OH) | Typical scale (0.5 mmol SM) |
|----------------------------|-----------------------------|
| 2‑Hydroxyethanol (HO‑CH₂‑CH₂‑OH) | 2.2 equiv (≈1.1 mmol) |
| Triphenylphosphine (PPh₃) | 2.2 equiv (≈1.1 mmol) |
| DIAD (di‑isopropyl azodicarboxylate) | 2.2 equiv (≈1.1 mmol) |
| Dry THF (or dry 1,4‑dioxane) | 0.05 M (≈10 mL) |
| 4 Å molecular sieves (activated) | 1 g (per 0.5 mmol SM) |
| N₂ atmosphere, dark (to avoid photolysis) | – |

**Procedure**

1. **Set up** a dry 50 mL Schlenk flask under N₂. Add **activated 4 Å molecular sieves** (to trap the water that is generated in the Mitsunobu step).  
2. Dissolve **2,3‑dihydroxy‑thioxanthone** (0.5 mmol) in **dry THF** (≈10 mL). The solution will be faint yellow; stir until a homogeneous slurry forms.  
3. Add **triphenylphosphine** (1.1 mmol, 288 mg) in one portion. Stir for 5 min at **0 °C** (ice bath).  
4. Add **2‑hydroxyethanol** (1.1 mmol, 99 µL) dropwise via syringe while maintaining 0 °C. The mixture becomes slightly turbid.  
5. With a syringe pump (or dropwise by syringe), add a solution of **DIAD** (1.1 mmol, 224 µL) in dry THF (2 mL) **slowly over 10 min** while still at 0 °C.  
6. After the addition is complete, allow the mixture to **warm to rt** and stir **overnight (≈16 h)**. TLC (hexane/ethyl acetate = 3:1, visualized with UV and KMnO₄) should show disappearance of the starting phenols and appearance of **two very close spots** corresponding to the mono‑alkylated intermediate and the bis‑alkylated product.  
7. **Quench** by adding sat. NH₄Cl (10 mL) at 0 °C, then extract with EtOAc (3 × 20 mL). Wash the combined organic layers with sat. NaHCO₃ (10 mL) and brine (10 mL). Dry over Na₂SO₄, filter, and concentrate.  

**Key points that make the second Mitsunobu work**

* **Excess 2‑hydroxyethanol** (2.2 equiv) drives the reaction to the bis‑product.  
* **Molecular sieves** remove the water that otherwise deactivates DIAD and promotes oxidation.  
* **Low temperature during addition** prevents decomposition of DIAD and minimizes side‑reactions.  
* **Extended reaction time (overnight)** gives the second phenol enough opportunity to react even though it is sterically hindered.  

The crude mixture typically contains **triphenylphosphine oxide (TPPO)** and **hydrazine dicarboxylate** by‑products, both of which are removed in the next step.

---

### Step 2 – Conversion of the terminal primary alcohols to bromides  

Two reliable options are presented; the choice depends on what halide you need (Br > Cl) and on equipment availability.

#### Option A – Direct Appel bromination (CBr₄/PPh₃)  

| Reagents (per 0.5 mmol bis‑alcohol) |
|------------------------------------|
| Carbon tetrabromide (CBr₄) | 2.5 equiv (≈1.25 mmol, 350 mg) |
| Triphenylphosphine (PPh₃) | 2.5 equiv (≈1.25 mmol, 327 mg) |
| Dry CH₂Cl₂ (0.05 M) | 10 mL |
| N₂ atmosphere, 0 °C → rt | – |

**Procedure**

1. Dissolve the **bis‑(2‑hydroxyethyl) ether** (crude from Step 1, ≈0.5 mmol) in dry CH₂Cl₂ (10 mL) under N₂ and cool to **0 °C**.  
2. Add **PPh₃** (327 mg) in one portion, stir 5 min.  
3. Add **CBr₄** (350 mg) in one portion, keep the temperature at 0 °C for 10 min, then allow the mixture to **warm to rt** and stir **2 h**. TLC shows disappearance of the alcohol (the spot moves up, indicating a less polar bromide).  
4. Quench with sat. Na₂S₂O₃ (10 mL) to destroy any residual CBr₄, then extract with CH₂Cl₂ (3 × 20 mL). Wash organic layer with sat. NaHCO₃ (10 mL) and brine (10 mL). Dry (Na₂SO₄), filter, concentrate.  
5. **Purify** by flash chromatography (hexane/EtOAc = 4:1, 1 % Et₃N added to the eluent). The pure product is the **bis‑(2‑bromoethyl) ether**.

*Advantages*: One‑pot, neutral, no acidic or basic conditions; TPPO formed is removed on silica.

#### Option B – Two‑step mesylate → Finkelstein  

1. **Mesylation**  
   * Reagents (0.5 mmol bis‑alcohol): MsCl (1.5 equiv, 75 µL), Et₃N (2 equiv, 140 µL), DMAP (0.1 equiv, 6 mg), dry CH₂Cl₂ (0.05 M).  
   * Add MsCl dropwise at 0 °C, stir 1 h at rt. Work‑up (wash with sat. NaHCO₃, brine).  
   * Isolate the **bis‑mesylate** (no chromatography needed; extract into EtOAc).  

2. **Finkelstein substitution**  
   * Dissolve bis‑mesylate (≈0.5 mmol) in dry acetone (10 mL). Add **NaI** (3 equiv, 97 mg). Heat **reflux (≈56 °C)

*Original question: [Conversion of 2,3-dihydroxy-thioxanthone to the corresponding ethyl halide ether](https://chemistry.stackexchange.com/questions/195772/conversion-of-2-3-dihydroxy-thioxanthone-to-the-corresponding-ethyl-halide-ether) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
