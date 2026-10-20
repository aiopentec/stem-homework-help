---
layout: question
title: Why divinyl ketone derivatives absorb UV radiation as if their enone π-systems
  were separate?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Why divinyl ketone derivatives absorb
  UV radiation as if their enone π-systems were separate?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  Restating the question in plain language  

A student has learned the Wood‑Fieser (WF) rules for estimating the longest‑wavelength UV‑vis absorption (λ_max) of conjugated carbonyl compounds (enones).  
When a **divinyl‑ketone** (a carbonyl flanked by two C=C double bonds) is encountered, the WF tables tell us to **ignore one of the two vinyl groups** and to calculate λ_max only from the conjugated diene that is *directly* attached to the carbonyl.  

The student therefore wonders:

* **Why does the “far” vinyl group not contribute to the UV‑vis absorption?**  
* **Why do two different molecules—one having the extra vinyl group (compound A) and one lacking it (compound B)—show essentially the same λ_max?**  

In other words: *What is the electronic‑structure reason that the π‑system of the carbonyl plus the adjacent diene behaves as if the second vinyl group were absent?*  

---

## 2.  Step‑by‑step explanation  

### 2.1  Review of the relevant electronic transitions  

| Transition | Type of excitation | Typical wavelength range (nm) |
|------------|-------------------|------------------------------|
| **π → π\*** | electron promoted from a bonding π orbital to an antibonding π\* orbital | 200–300 (isolated C=C), 300–350 (conjugated C=C) |
| **n → π\*** | non‑bonding lone‑pair (n) on O → antibonding π\* of C=O | 300–350 (isolated carbonyl), red‑shifted when conjugated |

For an **enone** (C=O conjugated to a C=C), the most intense band is the **π → π\*** transition of the *combined* conjugated system (C=C‑C=O). Conjugation lowers the energy (red‑shifts) because the π‑system is extended: the HOMO becomes more delocalised (higher energy) and the LUMO more stabilised (lower energy).  

### 2.2  What the Wood‑Fieser rules actually count  

The WF rules are **empirical**: they start from a base value for a simple chromophore (e.g., an isolated enone) and then **add** increments for each of the following:

* additional double bonds **conjugated** to the chromophore (≈+30 nm each)  
* alkyl substituents attached to the conjugated chain (≈+5 nm each)  
* exocyclic double bonds (≈+5 nm each)  

The crucial word is **“conjugated to the chromophore.”** Only those π‑bonds that can **delocalise** electron density **through overlapping p‑orbitals** with the carbonyl contribute an increment.  

### 2.3  Geometry of a divinyl‑ketone  

Consider the generic skeleton:

```
   C=C   C=C
    \   /
     C=O
```

The carbonyl carbon is **sp²‑hybridised**; its p‑orbital (π) is **perpendicular** to the plane of the carbonyl C=O bond. The two adjacent C=C bonds each lie in a plane that can be **coplanar** with the carbonyl π‑system, **or** they can be twisted.  

In practice, the **most stable conformation** of a divinyl‑ketone places **only one of the two C=C bonds** in the same plane as the carbonyl π‑orbital (the *conjugated side*). The other C=C is forced, by steric and orbital‑symmetry reasons, to adopt a **torsion angle of ~90°** relative to the carbonyl π system.  

#### Why does this happen?

1. **Orbital symmetry** – The carbonyl π‑orbital can overlap with **only one** adjacent p‑orbital at a time. If both C=C bonds tried to align, the central carbon would have to be **sp³**‑like (four p‑orbitals), which is impossible.  
2. **Steric strain** – Simultaneous coplanarity would bring the two alkenyl substituents too close, raising the energy.  
3. **Hybridisation of the carbonyl carbon** – It is already **sp²**; adding a second p‑orbital to the same carbon would break the trigonal planar geometry.

Consequently, **only one vinyl group is truly conjugated** to the carbonyl. The other vinyl group is essentially an **isolated alkene** that is orthogonal to the carbonyl π system, so its p‑orbitals do **not** overlap with the carbonyl π‑orbitals.

### 2.4  Molecular orbital picture  

#### 2.4.1  The conjugated side (enone + diene)  

*The relevant π‑system*:  

```
C=C–C=O–C=C   (4 conjugated double bonds)
```

The linear combination of p‑orbitals creates **four π molecular orbitals** (two bonding, two antibonding). The HOMO is a **delocalised π orbital** spread over the whole chain; the LUMO is the corresponding π\* orbital.  

The **π → π\*** excitation involves moving an electron from this delocalised HOMO to the delocalised LUMO, giving a **single, strong absorption** whose wavelength is predicted by the WF increments for a *conjugated diene* attached to an enone.

#### 2.4.2  The “non‑conjugated” vinyl group  

Because its p‑orbital is orthogonal, its π and π\* orbitals remain **localized** on that alkene alone. The lowest excitation of that isolated vinyl group lies near **~200 nm** (π → π\* of a simple alkene). That band is:

* Much **higher in energy** (shorter λ) than the enone‑diene band, and  
* Usually **weak** (low molar absorptivity) compared with the intense π → π\* of the extended conjugated system.

Thus, in a normal UV‑vis scan (200–400 nm), the **dominant band** is the one from the conjugated enone‑diene; the isolated vinyl’s band is either hidden in the far‑UV or appears as a small shoulder that is ignored in the WF bookkeeping.

### 2.5  Experimental evidence  

*Spectra of simple divinyl‑ketones* (e.g., 2,5‑hexadien-1‑one) show a **single strong band at ≈ 300 nm** that matches the prediction for a **conjugated triene** (C=C‑C=O‑C=C).  
A comparable spectrum of a molecule lacking the remote vinyl group (e.g., 3‑methyl‑2‑buten‑1‑one) shows essentially the same λ_max (within a few nm).  

The **additional vinyl** contributes only a weak, high‑energy band that does not affect the measured λ_max in the region used for WF calculations.  

### 2.6  Putting it together – why the WF rule “ignores” one vinyl  

1. **Only one vinyl can be coplanar with the carbonyl π‑system** → only that side is truly conjugated.  
2. The *other* vinyl is **orthogonal** → its π‑orbitals do not mix with the carbonyl π‑orbitals, so it does **not** lower the HOMO–LUMO gap of the chromophore.  
3. Consequently, the **absorption maximum** is governed solely by the *conjugated* portion (the enone plus the adjacent diene).  
4. The WF tables are built from empirical data that already reflect this behaviour; they therefore **add increments only for the conjugated diene** and ignore the remote vinyl.

Hence compounds **A** (with the extra vinyl) and **B** (without it) display **essentially the same λ_max**, because the extra vinyl does not participate in the chromophore responsible for the observed transition.

---

## 3.  Final answer  

The UV‑vis λ_max of a divinyl‑ketone is determined only by the **conjugated enone–diene fragment**. The second vinyl group is forced out of conjugation (its p‑orbitals are orthogonal to the carbonyl π‑system) and therefore does **not** lower the HOMO–LUMO energy gap. As a result, its presence does not shift the λ_max, and Woodward‑Fieser calculations correctly ignore it. Compounds A and B therefore have essentially identical λ_max values.

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming every double bond adds a WF increment** | The rule adds increments **only for bonds that are conjugated** (i.e., coplanar and able to delocalise). The remote vinyl in a divinyl‑ketone is orthogonal, so it does not count. | Draw the molecule, indicate the plane of the carbonyl π‑orbital, and check which C=C bonds can be coplanar with it. |
| **Counting the extra vinyl as an “exocyclic” double bond** | “Exocyclic” increments apply when the double bond is directly attached to the conjugated ring system. The remote vinyl is *not* exocyclic to the conjugated chain; it is isolated. | Verify the connectivity: the extra vinyl is attached to the carbonyl carbon, not to the conjugated π‑system. |
| **Attributing a high‑energy UV band to the observed λ_max** | The isolated vinyl absorbs in the far‑UV (< 250 nm). The measured λ_max for enones is usually in the 300–350 nm region, dominated by the conjugated system. | Compare the spectrum: the strong band near 300 nm is the one to use for WF calculations; ignore weak far‑UV shoulders. |
| **Neglecting conformational effects** | Assuming the molecule can adopt a fully planar conformation leads to the idea that both vinyl groups are conjugated. In reality, steric and orbital constraints prevent this. | Consider the preferred conformation (torsion ~90° for one side) when deciding which double bonds are conjugated. |
| **Using the “sum of all double bonds” rule for λ_max** | This rule applies only to simple polyenes, not to systems containing a carbonyl where conjugation is limited by the carbonyl geometry. | Apply the specific WF tables for *enones* (or *α,β‑unsaturated carbonyls*), not the polyene tables. |

By keeping these points in mind, you can correctly decide which parts of a molecule contribute to its UV‑vis absorption and apply the Woodward‑Fieser rules without error.

*Original question: [Why divinyl ketone derivatives absorb UV radiation as if their enone π-systems were separate?](https://chemistry.stackexchange.com/questions/196085/why-divinyl-ketone-derivatives-absorb-uv-radiation-as-if-their-enone-%cf%80-systems-w) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
