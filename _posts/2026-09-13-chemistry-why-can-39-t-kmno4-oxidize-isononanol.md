---
layout: question
title: Why can&#39;t KMnO4 oxidize isononanol?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Why can&#39;t KMnO4 oxidize isononanol?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What is the question asking?  

The student heard (in a YouTube video) that **potassium permanganate (KMnO₄) does not oxidise “isononanol” to the corresponding carboxylic acid, isononanoic acid**.  
The task is to explain, in a step‑by‑step way, **why KMnO₄ fails (or works very poorly) on this substrate** even though the alcohol is *primary* (i.e., not a tertiary alcohol that is normally resistant to oxidation).

---

## 2.  Detailed answer – why KMnO₄ does not give a good oxidation of isononanol  

### 2.1  Identify the substrate  

*Isononanol* is a **branched C₉ primary alcohol**.  
The most common isomer is **2‑methyl‑1‑octanol**  

```
CH3‑CH(CH3)‑(CH2)6‑CH2‑OH
```

(The exact position of the methyl branch is not crucial – any branched primary alcohol of this size behaves similarly.)

### 2.2  How KMnO₄ normally oxidises a primary alcohol  

Under **basic, hot aqueous conditions** the overall transformation is  

```
R‑CH2‑OH   →   R‑COOH
   (primary)       (carboxylic acid)
```

The mechanistic sequence (simplified) is:

| Step | What happens | Why it works for a simple primary alcohol |
|------|--------------|--------------------------------------------|
| 1️⃣  | Formation of the alkoxide:  R‑CH₂‑OH + OH⁻ → R‑CH₂‑O⁻ + H₂O | The alcohol is deprotonated by the strong base (OH⁻). |
| 2️⃣  | Hydride (or β‑hydrogen) transfer from the carbon bearing the O⁻ to MnO₄⁻ (the oxidant).  This gives a **manganate ester** which collapses to an aldehyde. | The α‑C–H bond is relatively accessible; Mn(VII) is a very strong oxidant. |
| 3️⃣  | The aldehyde is further oxidised (again by MnO₄⁻) to the carboxylate. | Aldehydes are easily attacked by water and further oxidised under the same conditions. |
| 4️⃣  | Acidic work‑up (if required) converts the carboxylate into the free acid. | Straightforward. |

Key requirements for the sequence to proceed efficiently:

* **Good contact** between the substrate (usually dissolved in water or a water‑miscible solvent) and the oxidant.
* **Access** of the base to the α‑hydrogen that must be removed in step 2.
* **No steric blockage** that would prevent the formation of the alkoxide or the hydride transfer.

### 2.3  What goes wrong with isononanol under the conditions used in the video  

| Problem | Explanation | Consequence |
|---------|-------------|-------------|
| **(a) Very poor solubility in water** | Isononanol is a C₉‑hydrocarbon with only one –OH group. Its **log P** is ≈ 3.5, meaning it prefers the organic phase. In the usual KMnO₄ oxidation (aqueous KOH, heated), the alcohol stays as a *tiny droplet* or a separate layer, so the concentration of substrate in the aqueous phase is essentially zero. | The effective molarity of substrate seen by MnO₄⁻ is far too low → the reaction is extremely slow or undetectable. |
| **(b) Steric hindrance at the α‑carbon** | The α‑carbon (the one bearing the –OH) is **secondary‑substituted**: it is attached to a methyl group and a long (CH₂)₆ chain. The β‑hydride that must be transferred to Mn is **shielded** by the adjacent methyl. In a linear primary alcohol (e.g., 1‑nonanol) the α‑C–H is freely accessible, but in 2‑methyl‑1‑octanol the methyl side‑chain creates steric crowding. | The rate of hydride transfer (step 2) drops dramatically; even if a small amount of alkoxide forms, it cannot easily hand over the hydrogen to MnO₄⁻. |
| **(c) Requirement for strongly basic conditions** | The video used *neutral* or *acidic* aqueous KMnO₄ (as is common for “oxidation of alkenes”). In acidic media, KMnO₄ is **reduced to Mn²⁺** but **does not generate the alkoxide** needed for primary‑alcohol oxidation; instead it prefers to act as a *dehydrogenating* agent for C=C bonds. | No alkoxide → no β‑hydride elimination → oxidation stops at the alcohol stage. |
| **(d) Competing side reactions** | In the presence of excess oxidant and heat, KMnO₄ can **cleave C–C bonds** adjacent to the alcohol (oxidative cleavage) or over‑oxidise the product to CO₂. With a branched substrate, the oxidation may be diverted to *fragmentation* rather than clean conversion to the acid, giving a messy mixture that appears as “no reaction”. | Even if some oxidation occurs, the desired carboxylic acid is not isolated. |

Putting these points together:

*The combination of **hydrophobicity**, **steric crowding** at the α‑carbon, and **non‑basic reaction conditions** makes the oxidation of isononanol by KMnO₄ **extremely slow** and practically invisible. In the experimental set‑up shown in the video (room‑temperature aqueous KMnO₄, no strong base, limited mixing), the substrate simply does not get oxidised to isononanoic acid.*

### 2.4  How to make the oxidation work (if one really wants the acid)

| Adjustment | Why it helps |
|------------|--------------|
| **Add a water‑miscible organic co‑solvent** (e.g., t‑butanol, acetone, dioxane) | Increases the concentration of the alcohol in the same phase as KMnO₄. |
| **Use a strong base (KOH, NaOH) and heat** (≈ 80 °C) | Generates the alkoxide and drives the β‑hydride transfer. |
| **Employ a phase‑transfer catalyst** (e.g., tetrabutylammonium bromide) | Shuttles the oxidant into the organic phase. |
| **Switch to a more powerful, non‑aqueous oxidant** (e.g., Jones reagent, PCC, Swern, or Dess–Martin) | Bypasses the solubility problem altogether. |

When those conditions are applied, even branched primary alcohols such as 2‑methyl‑1‑octanol can be converted to the corresponding acid, albeit usually in **moderate yields** (30–60 %) because the steric hindrance still slows the key hydride‑transfer step.

---

## 3.  Final answer  

> **KMnO₄ does not efficiently oxidise isononanol to isononanoic acid because the substrate is poorly soluble in the aqueous medium, the α‑carbon is sterically hindered by a neighboring methyl group, and the oxidation requires strongly basic (hot) conditions that were not employed in the experiment. Under the neutral/acidic, low‑temperature conditions shown in the video, the alkoxide cannot form and the hydride‑transfer to MnO₄⁻ is too slow, so essentially no oxidation occurs.**

---

## 4.  Common mistakes when tackling this type of problem  

| Mistake | Why it is wrong |
|---------|-----------------|
| **Assuming “all primary alcohols are oxidised by KMnO₄”.** | Only primary alcohols that are *accessible* to the oxidant and are present in the *same phase* as the oxidant under *basic, hot* conditions are reliably oxidised. |
| **Ignoring solubility/phase issues.** | A hydrophobic substrate that does not dissolve in the aqueous KMnO₄ solution will react only at the interface, giving negligible conversion. |
| **Treating KMnO₄ as a universal oxidant regardless of pH.** | In acidic media KMnO₄ does **not** generate the alkoxide needed for primary‑alcohol oxidation; it mainly oxidises alkenes and aromatic rings. |
| **Overlooking steric effects at the α‑carbon.** | Bulky substituents next to the –OH hinder formation of the alkoxide and the crucial β‑hydride transfer, slowing or preventing oxidation. |
| **Failing to recognise that “no reaction” may be due to competing side reactions.** | Strong oxidants can cleave C–C bonds or over‑oxidise products; a messy mixture may be mistaken for “no oxidation”. |

Keeping these points in mind will help you evaluate whether a given alcohol will undergo a clean KMnO₄ oxidation and, if not, how to modify the conditions or choose a different oxidant.

*Original question: [Why can&#39;t KMnO4 oxidize isononanol?](https://chemistry.stackexchange.com/questions/195868/why-cant-kmno4-oxidize-isononanol) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
