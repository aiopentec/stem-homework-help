---
layout: question
title: Extent of sp mixing in heteronuclear molecule NF
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Extent of sp mixing in heteronuclear
  molecule NF'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the problem is asking (in plain language)

The student wants to know **how the molecular‑orbital (MO) energy levels of the heteronuclear diatomic molecule NF are ordered**, and in particular how much *sp‑mixing* (mixing of the σ‑bond formed from the 2s orbitals with the σ‑bond formed from the 2p z orbitals) occurs.  

In other words:

* Which σ, π and σ* orbitals lie lowest and which lie highest in NF?  
* Does the σ(2s)–σ(2p z) interaction lower the σ(2s) level and raise the σ(2p z) level, as it does for CO and NO?  
* What is the resulting bond order?

---

## 2. Step‑by‑step solution  

Below we build the NF MO diagram from the ground up, explicitly showing every decision that determines the ordering.

### 2.1 Atomic‑orbital (AO) energies of N and F  

| Atom | 2s (eV) | 2p (eV) |
|------|--------|--------|
| N    | –19.2  | –13.4  |
| F    | –31.4  | –18.6  |

*(Values taken from spectroscopic data; only relative ordering matters.)*  

* The **2s of F** is much lower than the 2s of N.  
* The **2p of F** is lower than the 2p of N, but the 2p‑2p gap (≈ 5 eV) is smaller than the 2s‑2p gaps (≈ 6 eV for N, ≈ 13 eV for F).

Because the two atoms are very different in electronegativity, the resulting MOs will be **strongly polarized** (one AO contributes most of the electron density).

### 2.2 Symmetry of the interacting AOs  

* The **σ‑symmetry** AOs are the two 2s orbitals (σ2s) and the two 2p z orbitals (σ2p_z).  
* The **π‑symmetry** AOs are the 2p x and 2p y orbitals on each atom (π2p_x, π2p_y).  

Only orbitals of the same symmetry can combine. Consequently, **σ2s and σ2p_z can mix** (sp‑mixing), while the π set remains unmixed.

### 2.3 Qualitative picture of σ‑mixing  

The mixing strength depends on the **energy gap** between the two interacting AOs:

\[
\text{mixing} \propto \frac{H_{12}}{E_{2p_z}-E_{2s}}
\]

where \(H_{12}\) is the off‑diagonal Hamiltonian element (overlap + resonance integral).  

* For **CO**, the gap between C 2s (‑21 eV) and C 2p (‑11 eV) is ≈ 10 eV, so σ2s–σ2p mixing is appreciable.  
* For **NF**, the gap between N 2s (‑19 eV) and N 2p (‑13 eV) is **≈ 6 eV**, **smaller** than in CO, but the *average* gap of the two atoms (because the MOs are heavily weighted toward the more electronegative F) is larger (≈ 9 eV). Consequently, the **extent of sp‑mixing in NF is moderate – noticeable, but not as strong as in CO**.

Result of mixing:

* The **bonding σ(2s)** MO is pushed **down** (stabilised) and becomes dominated by the **F 2s** AO.  
* The **bonding σ(2p_z)** MO is pushed **up** (destabilised) and contains a larger N 2p contribution.  
* The corresponding antibonding σ* orbitals show the opposite polarity (σ*2s is mainly N 2s, σ*2p_z mainly F 2p_z).

### 2.4 Constructing the MO diagram  

1. **Lowest level – σ2s (bonding)**  
   * Mostly F 2s, small N 2s admixture, lowered by sp‑mixing.  

2. **Next – σ*2s (antibonding)**  
   * Mostly N 2s, a little F 2s, slightly raised because the bonding partner has been stabilised.  

3. **π2p (bonding)** – two degenerate orbitals (π2p_x, π2p_y)  
   * Almost pure N 2p (the higher‑energy AO) because the F 2p is lower and contributes little to the bonding π set.  

4. **σ2p_z (bonding)** – the mixed σ(2p_z)  
   * Dominantly N 2p_z (≈ 60 % N, 40 % F) and **raised** relative to a pure σ2p_z because of the σ–σ mixing.  

5. **π*2p (antibonding)** – two degenerate orbitals  
   * Mostly N 2p character (the higher‑energy AO) but now antibonding; lie **above** σ2p_z because the σ2p_z has been pushed up.  

6. **σ*2p_z (antibonding)** – the mixed σ*  
   * Mostly F 2p_z, the highest occupied MO (if electrons were added).  

Putting the levels together (lowest → highest):

```
σ(2s)          ← mostly F 2s, stabilised
σ*(2s)         ← mostly N 2s
π(2p_x), π(2p_y)  ← mainly N 2p
σ(2p_z)        ← mixed, raised (mainly N 2p_z)
π*(2p_x), π*(2p_y)← antibonding, above σ(2p_z)
σ*(2p_z)       ← highest, mixed (mainly F 2p_z)
```

### 2.5 Filling the MOs with the 12 valence electrons  

| MO            | Occupancy | Electrons |
|---------------|-----------|-----------|
| σ(2s)         | 2 (bonding) | 2 |
| σ*(2s)        | 2 (antibonding) | 2 |
| π(2p) (×2)    | 4 (bonding) | 4 |
| σ(2p_z)       | 2 (bonding) | 2 |
| π*(2p) (×2)   | 2 (antibonding) | 2 |
| σ*(2p_z)      | 0          | 0 |
| **Total**     |            | **12** |

### 2.6 Bond order  

\[
\text{BO}= \frac{N_\text{bonding}-N_\text{antibonding}}{2}
          =\frac{(2+4+2)-(2+2)}{2}
          =\frac{8-4}{2}=2
\]

Hence **NF has a double bond** (σ + π). The modest sp‑mixing slightly reduces the σ bond strength compared with a “pure” σ2p_z, which is why NF is not a triple bond like CO.

---

## 3. Final answer  

*The molecular‑orbital energy ordering for NF (from lowest to highest) is*

\[
\boxed{
\sigma(2s) < \sigma^{*}(2s) < \pi(2p_x),\pi(2p_y) < \sigma(2p_z) < \pi^{*}(2p_x),\pi^{*}(2p_y) < \sigma^{*}(2p_z)
}
\]

*The σ(2s)–σ(2p_z) mixing is **moderate** – it lowers σ(2s) and raises σ(2p_z) relative to the unmixed case, but the effect is smaller than in CO because the energy gap between the interacting AOs is larger after the strong polarization toward fluorine.*

*With 12 valence electrons the filling gives a bond order of 2 (one σ and one π bond).*

---

## 4. Common mistakes when tackling this type of problem  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the heteronuclear MO ordering is identical to the homonuclear case** | Different atomic‑orbital energies cause strong polarization; the ordering can change (e.g., σ2p may move above π*). | Always start by writing the AO energies for each atom and consider which AO dominates each MO. |
| **Neglecting σ–σ (sp) mixing** | The σ(2s) and σ(2p_z) have the same symmetry; mixing shifts both levels and changes the relative order of σ(2p) and π*. | Examine the energy gap between the two σ‑type AOs; if the gap is not huge, include a qualitative mixing step. |
| **Placing the π* set below σ(2p_z)** because of a “text‑book diagram” for O₂ | In CO and NF the σ(2p_z) is stabilised by mixing and sits **below** the π* set; the O₂ diagram does not apply. | Compare the NF diagram to that of CO (which also has heteronuclear atoms) rather than to O₂. |
| **Counting electrons incorrectly** (e.g., forgetting the σ*2s electrons) | Leads to an erroneous bond order. | Write the total valence electron count first (N = 5, F = 7 → 12) and fill the diagram stepwise. |
| **Treating the diagram as symmetric** (assigning equal contribution from N and F to every MO) | The large electronegativity difference makes the MOs highly polarized. | After drawing the diagram, annotate each MO with the dominant AO (e.g., “mostly F 2s”). |

Keeping

*Original question: [Extent of sp mixing in heteronuclear molecule NF](https://chemistry.stackexchange.com/questions/196093/extent-of-sp-mixing-in-heteronuclear-molecule-nf) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
