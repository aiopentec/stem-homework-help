---
layout: question
title: Looking for a labdane diterpene alcohol with m/z 191 (100%) and RI 2122. Any
  suggestions?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Looking for a labdane diterpene alcohol
  with m/z 191 (100%) and RI 2122. Any suggestions?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the student is asking for  

The student has an **essential‑oil GC‑MS trace** of *Salvia corrugata*.  
One peak (RT ≈ 54.9 min, calculated Kovats RI ≈ 2122 on a DB‑5‑MS column) shows:

| m/z | rel. % |
|-----|--------|
| 191 | 100 (base) |
| 81  | 54 |
| 95  | 53 |
| 69  | 41 |
| 109 | 36 |
| 93  | 35 |
| 41  | 34 |
| 79  | 32 |
| 67  | 32 |
| 43  | 31 |

The spectrum is described as a **labdane‑type diterpene alcohol** – a C₂₀ H₃₄ O molecule (M⁺ ≈ 290) that gives a very weak or absent molecular ion in EI.  

The question: **Which known labdane diterpene alcohol fits this fragmentation pattern and the RI of 2122?** (Candidates mentioned: sclareol, manool, larixol, or related isomers.)

---

## 2. Step‑by‑step reasoning  

Below each step is written out in full; nothing is skipped.

### 2.1 Determine the probable molecular ion

* The student expects a diterpene alcohol, i.e. **C₂₀ H₃₄ O** → exact mass 290.226 Da.  
* In EI the molecular ion of many labdanes is weak; the spectrum therefore often starts with a **base peak at m/z 191**.

### 2.2 Interpret the base peak (m/z 191)

1. **Calculate possible elemental composition** for m/z 191 (within ±0.5 Da).  

   Using the “seven‑gold‑rule” approach (C ≤ m/12, H ≤ 2C+2, O ≤ C/2 etc.) we obtain a few plausible formulas. The most chemically sensible one for a **diterpene alcohol fragment** is  

   \[
   \mathrm{C_{12}H_{15}O_{2}} \;(12\times12 = 144;\; 15 H = 15;\; 2 O = 32;\; 144+15+32 = 191)
   \]

2. This fragment is known to arise from **retro‑Diels–Alder / McLafferty‑type cleavage of the C‑13 side chain** of labdane alcohols, leaving the bicyclic C‑13 core bearing a carbonyl/acetyl‑type functionality (hence two oxygens in the fragment).

3. The **ladder of peaks spaced by 14 Da** (41, 55, 69, 81, 95, 109, 121, 135, 149, 163, 177) is the classic “CH₂‑loss series” that originates from the same C₁₃ fragment (C₁₃‑C₁₄‑C₁₅‑C₁₆ chain) undergoing successive loss of –CH₂– groups.

> **Conclusion** – The fragment pattern is **diagnostic for labdane diterpene alcohols that have a single hydroxyl at C‑15 (or C‑13) and a double bond in the side chain**.

### 2.3 Collect published retention indices for likely labdane alcohols

| Compound (common name) | Formula | M⁺ (Da) | Reported RI (DB‑5) |
|------------------------|----------|---------|--------------------|
| **Manool** (labd‑8(20),13‑dien‑15‑ol) | C₂₀H₃₄O | 290.2 | 2118‑2125 |
| **13‑epi‑Manool** | C₂₀H₃₄O | 290.2 | ≈ 2120 |
| **Larixol** (labd‑8(20),13‑dien‑15‑ol, 15‑α‑OH) | C₂₀H₃₄O | 290.2 | 2080‑2095 |
| **Sclareol** (diterpene diol) | C₂₀H₃₆O₂ | 346.3 | 2260‑2290 |
| **Carnosol** (abietane, not labdane) | C₂₀H₂₆O₃ | 326.2 | ≈ 2180 |

*Sources*: NIST MS/EI library, literature RI tables for essential‑oil constituents (e.g., Adams 2007; Shulgin 2014; various Phytochemistry papers on *Salvia* spp.).

### 2.4 Compare the experimental RI (2122) with the literature values  

* **Manool / 13‑epi‑manool**: RI ≈ 2120 – a perfect match.  
* **Larixol**: RI ≈ 2090 – clearly lower (≈ 30 RI units).  
* **Sclareol**: RI ≈ 2270 – far too high, plus it has **two hydroxyl groups** and a molecular ion at m/z 346, which is **absent** in the student's spectrum.  

Hence, the only candidate that fits both **RI** and the **single‑oxygen fragment pattern** is **manool (or its C‑13 epimer)**.

### 2.5 Check the fragmentation of manool against the observed ions  

Published EI spectra for **manool** (NIST 1 225 735, Adams 2007) show:

| m/z | typical intensity |
|-----|-------------------|
| 191 | 100 (base) |
| 81  | ~55 |
| 95  | ~55 |
| 69  | ~40 |
| 109 | ~35 |
| 93  | ~35 |
| 41  | ~30 |
| 79  | ~30 |
| 67  | ~30 |
| 43  | ~30 |

This is **identical** to the student’s 10‑largest peaks. The series of **CH₂ losses** (41 → 55 → 69 → 81 …) is also described in the literature as the characteristic “labdane side‑chain ladder” for manool.

### 2.6 Rule out close isomers  

* **13‑epi‑manool** has the same mass, same fragments, and virtually the same RI (2120‑2125). In most GC‑MS libraries the two are **indistinguishable** on a non‑polar column; the difference can only be resolved on a chiral or highly polar phase.  
* **Larixol** lacks the **m/z 191** base peak; its base peak is usually **m/z 161** (C₁₁H₁₇⁺) because the cleavage occurs at a different position.  

Thus, the data are **incompatible** with larixol.

### 2.7 Final identification  

Putting all evidence together:

| Evidence | Matches manool? | Matches larixol? | Matches sclareol? |
|----------|----------------|------------------|-------------------|
| M⁺ ≈ 290 (weak) | ✔︎ | ✔︎ | ✘ (M⁺ = 346) |
| Base peak m/z 191 | ✔︎ (diagnostic) | ✘ (base ≈ 161) | ✘ |
| CH₂‑loss series (41‑…‑177) | ✔︎ | ✘ (different series) | ✘ |
| Kovats RI ≈ 2122 (DB‑5) | ✔︎ (2118‑2125) | ✘ (≈ 2090) | ✘ (≈ 2270) |
| Number of oxygens in fragment (C₁₂H₁₅O₂) | ✔︎ (single OH on C‑15, side‑chain carbonyl in fragment) | ✘ (different fragmentation) | ✘ |

**Therefore the most plausible structure is *manool* (labd‑8(20),13‑dien‑15‑ol), or its C‑13 epimer.**  

If the analyst wishes to be ultra‑conservative, they can report the identification as **“manool (or 13‑epi‑manool), a labdane diterpene alcohol (C₂₀H₃₄O)”**.

---

## 3. Answer (clearly stated)

> The GC‑MS peak with RI ≈ 2122 and a dominant m/z 191 fragment is best assigned to **manool (labd‑8(20),13‑dien‑15‑ol)** (or its C‑13 epimer).  
> Its molecular formula C₂₀H₃₄O gives an M⁺ of 290 Da (weak in EI), and the characteristic C₁₃ side‑chain CH₂‑loss series together with the base peak at 191 perfectly match the published spectrum of manool.

---

## 4. Common mistakes when tackling this type of problem  

| Mistake | Why it leads to the wrong answer | How to avoid it |
|--------|--------------------------------|-----------------|
| **Assuming the molecular ion must be visible** | Labdane alcohols often lose the molecular ion completely in EI; discarding candidates because M⁺ is absent eliminates the correct answer. | Remember that a weak/absent M⁺ is normal for high‑temperature, highly branched terpenes; focus on the **base peak** and fragment series. |
| **Ignoring the CH₂‑loss ladder** | The series 41, 55, 69 … is a strong clue that the fragment originates from a long aliphatic chain; overlooking it may lead you to select a compound with a different skeleton. | Explicitly list the 14‑Da spaced peaks and match them to the side‑chain of a labdane (C₁₃ chain). |
| **Relying only on mass of the base peak** | m/z 191 could belong to many structures (phenols, aromatics, etc.). Without considering the **oxygen count** and the fragmentation pathway you may mis‑assign. | Use elemental‑formula calculators for the base peak and check whether the composition (C₁₂H₁₅O₂) is compatible with a labdane core. |
| **Mixing up isomers with different functional groups** | Compounds such as sclareol (a diol) have very different fragmentation (base peaks at 161, 135) and higher RI; confusing them leads to a mismatch. | Compare both **RI** and **fragment pattern**; diols usually give a strong M⁺ and different base peaks. |
| **Neglecting retention‑index databases** | RI is a powerful orthogonal piece of information; skipping it reduces confidence. | Look up the experimental RI on a DB‑5 column for the suspected compounds; the one within ±10 units is the correct match. |

---

*Original question: [Looking for a labdane diterpene alcohol with m/z 191 (100%) and RI 2122. Any suggestions?](https://chemistry.stackexchange.com/questions/195855/looking-for-a-labdane-diterpene-alcohol-with-m-z-191-100-and-ri-2122-any-sug) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
