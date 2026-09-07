---
layout: question
title: Selectivity of electrophilic substitutions of chlorobenzene
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Selectivity of electrophilic substitutions
  of chlorobenzene'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

When chlorobenzene undergoes an electrophilic aromatic substitution (EAS) – e.g. nitration, sulfonation, halogenation, Friedel‑Crafts acylation, etc. – the new substituent can end up **ortho** (adjacent to Cl), **meta**, or **para** (opposite the Cl).  
Experimentally the **para‑product is formed in larger amount than the ortho‑product**.  

The student wants to know:

* Why does the para isomer dominate?
* Is chlorine really “bulky enough” to make the ortho position less favorable, or is something else going on?

Our job is to give a step‑by‑step, mechanistic explanation that combines **electronic (resonance/inductive)** effects with **steric (size‑related)** effects.

---

## 2.  Detailed solution – every logical step

### 2.1  Identify the directing nature of chlorine

| Property | Effect |
|----------|--------|
| **Inductive (-I)** | Cl is electronegative → withdraws electron density through the σ‑framework → *deactivates* the ring (slower EAS). |
| **Resonance (+R)** | The lone pairs on Cl can donate into the aromatic π‑system, giving resonance structures that place a **positive charge at the ortho and para positions**. This makes Cl an **ortho/para director** despite being deactivating overall. |

**Result:** In a chlorobenzene ring, *ortho* and *para* positions are electronically favored over *meta*.

---

### 2.2  Write the resonance‑stabilised arenium‑ion (σ‑complex) for each possible attack

Below the arrows “→” denote the formation of the σ‑complex after the electrophile (E⁺) adds to the ring.

#### (a) Ortho attack  

```
Cl               Cl
  \             /
   C           C
  / \   +   E⁺  →  [σ‑complex]⁺
 C   C
```

Resonance forms (selected):

```
   +            +               +
Cl–C⁺‑C–C–C–C    ↔   Cl–C=C⁺‑C–C–C   ↔   Cl–C–C=C⁺‑C–C
```

Two of the three resonance structures place the positive charge **adjacent to chlorine**, allowing the lone‑pair donation to delocalise the charge. Thus the ortho σ‑complex enjoys resonance stabilisation.

#### (b) Para attack  

```
Cl               Cl
  \             /
   C           C
  / \   +   E⁺  →  [σ‑complex]⁺
 C   C
```

Resonance forms:

```
   +                +
Cl–C–C–C⁺‑C–C   ↔   Cl–C–C=C⁺‑C–C   ↔   Cl–C⁺‑C–C–C–C
```

Again, the positive charge can be delocalised onto the carbon bearing Cl, giving the same *type* of resonance stabilisation as the ortho case.

#### (c) Meta attack  

```
Cl               Cl
  \             /
   C           C
  / \   +   E⁺  →  [σ‑complex]⁺
 C   C
```

Resonance forms:

```
   +                +
Cl–C–C–C–C⁺‑C   ↔   Cl–C–C–C⁺‑C–C   ↔   Cl–C–C⁺‑C–C–C
```

Here **none** of the resonance contributors place the positive charge on the carbon bearing Cl, so the lone pair cannot help stabilise the σ‑complex. The meta σ‑complex is therefore **less stable** than ortho or para.

**Conclusion of step 2.2:** *Electronic* considerations predict **ortho ≈ para > meta**.

---

### 2.3  Introduce steric (size) considerations

Even though ortho and para are electronically equivalent, the *ortho* position suffers from **steric crowding**:

1. **Cl is not a tiny substituent.**  
   - The C–Cl bond length ≈ 1.78 Å (longer than a C–C bond).  
   - The chlorine atom’s van der Waals radius ≈ 1.75 Å, comparable to a phenyl hydrogen’s radius (≈ 1.2 Å).  
   - When an electrophile approaches the ortho carbon, it must pass **between the chlorine and the hydrogen that already occupies the ortho site**. This creates a repulsive “bump”.

2. **The electrophile itself is often bulky.**  
   - In nitration, the attacking species is the planar nitronium ion (NO₂⁺) – already larger than a proton.  
   - In sulfonation, SO₃ is a trigonal planar molecule with a sizable “face”.  
   - In Friedel‑Crafts acylation, the acylium ion RCO⁺ can be a long alkyl chain.

3. **Transition‑state geometry.**  
   - The σ‑complex is formed via a **σ‑bond‑forming transition state** where the electrophile is directly above the ring carbon. At the ortho site the chlorine forces the electrophile to adopt a *tilted* approach, raising the activation energy (ΔG‡).

4. **Arenium‑ion destabilisation after attack.**  
   - In the ortho σ‑complex, the positive charge sits next to a **partial double bond C–Cl** (the resonance form where Cl donates its lone pair). The resulting **dipole–dipole repulsion** (C⁺–Cl⁻) further destabilises the intermediate.

**Result:** The **ortho pathway is slower** (higher ΔG‡) than the para pathway, even though both are electronically allowed.

---

### 2.4  Quantitative picture (example: nitration of chlorobenzene)

Experimental product distribution (typical values, temperature ≈ 50 °C, mixed acid)  

| Position | Approx. % of total substitution |
|----------|--------------------------------|
| para     | 55–70 % |
| ortho    | 25–35 % |
| meta     | 5–10 % |

These numbers illustrate that **para > ortho** by roughly a factor of 2:1, exactly what we expect from the combination of (i) equal electronic activation and (ii) extra steric penalty for ortho.

---

### 2.5  Putting it together – why para dominates

1. **Electronic directing:** Cl is an ortho/para director → meta is disfavoured.  
2. **Resonance stabilisation:** Both ortho and para σ‑complexes enjoy charge delocalisation onto the C‑Cl bond.  
3. **Steric hindrance:** The ortho approach is hindered by the chlorine atom (size + partial double‑bond character) and by the incoming electrophile → higher activation barrier.  
4. **Overall outcome:** The *para* transition state is the **lowest‑energy** of the three possibilities; the *ortho* transition state is slightly higher; the *meta* transition state is the highest. Consequently, **para product predominates**, ortho is a significant minority, and meta is minor.

---

## 3.  Final answer (clear statement)

When chlorobenzene undergoes electrophilic aromatic substitution, the **para isomer is formed in larger amount than the ortho isomer** because:

* The chlorine atom, through resonance donation, makes **both ortho and para positions electronically favored** (it is an ortho/para director).  
* However, **steric repulsion between the chlorine atom and the incoming electrophile** raises the energy of the ortho transition state and its σ‑complex. Chlorine’s van der Waals radius (~1.75 Å) and the relatively long C–Cl bond make it sufficiently bulky to matter.  
* The para position avoids this steric clash, so its transition state is lower in energy, leading to **higher para‑product yield**.  

Thus, the observed para‑dominance is the **combined result of electronic directing and steric hindrance**; chlorine does not need to be a “large” substituent—its size and the geometry of the reaction are enough to tip the balance.

---

## 4.  Common mistakes students make with this type of problem

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming chlorine only withdraws electrons** and therefore predicts *meta* as the major product. | Ignoring the **+R** (lone‑pair donation) effect that makes Cl an ortho/para director. | Write out the resonance structures of the σ‑complexes first; see where the positive charge can be delocalised. |
| **Treating ortho and para as equally favored** because both are ortho/para‑directed. | Overlooks **steric hindrance** at the ortho position, which raises the activation barrier. | Explicitly consider the size of Cl (vdW radius) and the electrophile; draw a transition‑state sketch to visualise crowding. |
| **Neglecting the deactivating inductive effect** and concluding that substitution will be fast. | Cl’s –I effect makes the whole ring less reactive; rates are slower than for benzene. | Remember that a substituent can be **both** deactivating (overall rate) *and* ortho/para‑directing (regioselectivity). |
| **Using only qualitative language** (“bulky enough”) without quantitative support. | Leaves the argument vague; students cannot see why chlorine’s size matters. | Cite bond lengths (C–Cl ≈ 1.78 Å) and van der Waals radii, or compare with typical electrophiles (NO₂⁺, SO₃). |
| **Confusing “steric hindrance” with “electronic repulsion”** (e.g., blaming the Cl‑C⁺ dipole alone). | Steric and electronic effects are distinct; mixing them leads to incorrect mechanistic pictures. | Separate the discussion: first electronic resonance/induction, then steric geometry of the transition state. |

By keeping both **electronic** and **steric** factors in mind and explicitly drawing the resonance forms, the regioselectivity of chlorobenzene’s electrophilic substitutions becomes clear.

*Original question: [Selectivity of electrophilic substitutions of chlorobenzene](https://chemistry.stackexchange.com/questions/195950/selectivity-of-electrophilic-substitutions-of-chlorobenzene) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
