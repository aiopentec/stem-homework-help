---
layout: post
title: Rationalising diastereoselectivity of hydroboration using stereoelectronics
author: StemFix Bot
category: chemistry
tags:
- chemistry
render_with_liquid: false
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The student wants to know **why, in many hydroborations with a bulky borane (e.g., 9‑BBN), the product that is formed is the *1,2‑anti* diastereomer**.  

* A steric (allylic‑strain) argument can explain many cases, but it does not always predict the observed selectivity.  
* Houk suggested that a **stereoelectronic effect** in the transition state also contributes, but he did not spell out what that effect actually is.  

So we need to:

1. Identify the **specific orbital interactions** that define the stereoelectronic component of the hydroboration transition state.  
2. Explain **how those interactions bias the transition‑state geometry** (endo vs. exo approach).  
3. State **when the stereoelectronic factor is expected to dominate** over simple steric considerations.  

---

## 2.  Step‑by‑step analysis  

### 2.1  Hydroboration is a concerted, pericyclic‑like addition  

```
   B‑H   →   B‑C   +   H‑C
   (σ)        (σ)       (σ)
```

*The B–H σ bond and the C=C π bond interact in a *six‑electron* cyclic transition state that resembles a chair‑like 6‑membered ring.*  
Two key orbital overlaps must be satisfied simultaneously:

| Interaction | What it does | Geometric requirement |
|-------------|--------------|-----------------------|
| σ_B‑H → π* _(C=C)_ | Donation of electron density from the B–H bond into the antibonding π* orbital of the alkene, which initiates C–B bond formation. | The B–H bond must be **antiperiplanar** (≈ 180°) to the C=C bond. |
| π _(C=C)_ → σ* _B‑C_ | Back‑donation that assists formation of the new C–B σ bond. | The forming C–B bond must be **syn‑periplanar** to the π bond (i.e., the new C–B bond lies in the same plane as the original double bond). |

Because the reaction is concerted, the two interactions are satisfied only in one specific orientation of the reagents relative to the alkene – the **“endo” transition state** (the boron approaches from the same side as the developing C–B bond, the H from the opposite side).  

> **Stereoelectronic rule for hydroboration** – *the B–H bond must approach the alkene anti‑ to the C–C bond that will become the new C–B bond* (i.e., the B–H bond is antiperiplanar to the C=C π*).  

If the borane approaches from the opposite (exo) face, the required antiperiplanar alignment is impossible; the transition state suffers from poor orbital overlap and is higher in energy.

### 2.2  Two possible transition‑state conformers  

For a substituted alkene (e.g., a cyclohexene bearing an axial substituent **X**) we can draw two competing TSs:

```
   (A)  Endo approach (favoured by stereoelectronics)
        B–H antiperiplanar to the C=C π*  →  good overlap
        B‑C bond forms on the same face as X (anti product)

   (B)  Exo approach (disfavoured)
        B–H cannot be antiperiplanar → poor overlap
        B‑C bond forms on the opposite face (syn product)
```

Both TSs also differ in **allylic (A‑value) strain**:

* In the endo TS, the bulky substituent **X** is placed pseudo‑axial (or pseudo‑equatorial) depending on the ring; the strain is minimized when **X** occupies the less‑crowded position.  
* In the exo TS, **X** may have to adopt a sterically disfavoured orientation.

Thus the **overall activation energy** = steric penalty + stereoelectronic penalty.

### 2.3  How the stereoelectronic component “wins”  

| Situation | Steric bias | Stereoelectronic bias | Result |
|-----------|--------------|-----------------------|--------|
| **Bulky borane (9‑BBN)** attached to a rigid bicyclic framework | Strong – the reagent cannot easily flip to the sterically less‑favoured face. | The rigid framework forces the B–H bond to lie in a fixed orientation that is *already* antiperiplanar to the π* of the alkene when the boron approaches the “anti” face. | **Anti product** (1,2‑anti) is overwhelmingly favoured. |
| **Small borane (BH₃·THF)** | Weak – both faces are accessible. | Still needs antiperiplanar alignment; the less‑strained face is chosen, but the steric difference may dominate, giving a mixture. | Moderate selectivity. |
| **Allylic substituent that can donate (e.g., O‑Me, SiR₃)** | May increase steric crowding on one face. | **Hyperconjugative stabilization** of the developing C‑B σ* by a σ‑C‑X lone‑pair (σ → σ*) is possible only in the endo TS where the C‑X bond is antiperiplanar to the forming C‑B bond. | **Stereoelectronic effect dominates** → higher selectivity for the anti product even if sterics are not dramatically different. |
| **Conjugated diene or aryl‑substituted alkene** | Steric differences often small. | The π‑system can delocalise the developing positive charge on the carbon that receives B⁺; the best delocalisation occurs when the B‑H bond is antiperiplanar to the π* of the *more substituted* double bond. | Selectivity follows *electronic* (more substituted carbon gets B) rather than pure steric control. |

**Key point:** The *only* way for the transition state to achieve the required antiperiplanar alignment is for the boron to add to the **face that places the B–H bond opposite to the developing C–B bond**. When a bulky borane is forced into that geometry, the anti product is formed. If the substrate can adopt a conformation that satisfies the antiperiplanar requirement *without* a large steric penalty, the stereoelectronic factor will dominate.

### 2.4  Practical “rules of thumb” for invoking the stereoelectronic component  

1. **Check the geometry of the alkene.**  
   * Is the alkene part of a ring or a constrained system?  
   * Does the substituent allow the B–H bond to be antiperiplanar without severe steric clash?  

2. **Identify any neighboring lone‑pair or σ‑donor bonds** (O, N, Si, etc.).  
   * If such a bond can align antiperiplanar to the forming C–B σ bond, a *σ‑C‑X → σ* _C‑B* hyperconjugative interaction* stabilises the TS → favour the anti approach.

3. **Assess the size of the borane.**  
   * Very bulky boranes (9‑BBN, di‑iso‑propyl‑phenyl‑borane) lock the B–H bond in a fixed orientation; the stereoelectronic requirement therefore dictates the face of attack.  

4. **When steric differences between the two faces are ≤ 1 A° (≈1 kcal mol⁻¹)**, the stereoelectronic requirement usually **out‑weighs** steric effects.  

5. **If the substrate contains an electron‑withdrawing group** (e.g., carbonyl, nitrile) adjacent to the double bond, the developing partial positive charge on the carbon that receives boron is better stabilised when that carbon is *syn* to the electron‑withdrawing group. The required antiperiplanar alignment may force the borane to add from the opposite face, again giving the anti product.

---

## 3.  Final answer  

**Nature of the stereoelectronic component**  

Hydroboration proceeds through a six‑electron, cyclic transition state in which the **B–H σ bond must be antiperiplanar to the π* orbital of the alkene** (σ_B‑H → π* C=C) and the **forming C–B σ bond must be syn‑periplanar to the π bond** (π C=C → σ* _C‑B). This **antiperiplanar alignment** is the stereoelectronic requirement.  

Because a bulky borane such as 9‑BBN has a rigid bicyclic framework, the only way to satisfy that orbital overlap is to approach the alkene from the face that gives the **1,2‑anti** product (the “endo” transition state). The opposite (exo) approach would place the B–H bond out of antiperiplanar alignment, leading to a higher‑energy TS despite any steric relief it might afford.

**When to invoke it**  

* When the two possible faces of the alkene differ only slightly in steric bulk (e.g., in cyclic alkenes, in allylic systems with modest substituents).  
* When the substrate bears neighboring heteroatoms or σ‑donor groups that can hyper‑conjugatively stabilise the developing C–B bond **only** in the antiperiplanar orientation.  
* When a very bulky borane is used, because its geometry forces the antiperiplanar arrangement.  
* When conjugation or electron‑withdrawing substituents alter the π‑system such that optimal orbital overlap is only possible from one face.

In those situations the **stereoelectronic requirement outweighs simple steric arguments**, and the reaction gives the 1,2‑anti diastereomer with high selectivity.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating hydroboration as a purely “steric” addition.** | Ignores the mandatory antiperiplanar B–H/π* overlap; predicts the wrong face when steric differences are small. | Always draw the six‑membered cyclic TS and check the antiperiplanar alignment before invoking sterics. |
| **Choosing the “exo” TS because it looks less crowded.** | The exo TS cannot place the B–H bond antiperiplanar to the π*; orbital overlap is poor → high barrier. | Verify that the B–H bond is aligned opposite the forming C–B bond (endo geometry). |
| **Assuming the bulky borane will always avoid the larger substituent.** | Bulky boranes may be forced into a geometry that *does* place them near a larger group if that geometry satisfies the stere

*Original question: [Rationalising diastereoselectivity of hydroboration using stereoelectronics](https://chemistry.stackexchange.com/questions/100417/rationalising-diastereoselectivity-of-hydroboration-using-stereoelectronics) on Chemistry Stack Exchange, licensed CC BY-SA.*
{% endraw %}
