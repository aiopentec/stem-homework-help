---
layout: question
title: How does the bistable spring tape in a slap bracelet (or retractable tape measure)
  work?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How does the bistable spring tape in
  a slap bracelet (or retractable tape measure) work?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. Restatement – What the question is asking  

A snap‑bracelet (or the thin “blade” that lives inside a self‑retracting tape measure) is a narrow metal strip that can be **flat‑straight** or **curled**.  
The strip has two *stable* shapes:

| Shape | Direction of curvature | How it looks |
|------|------------------------|--------------|
| **Longitudinally straight** (the “ruler” state) | Curved **across** the width (the strip is cupped upward) – i.e. it has **transverse curvature** but **no longitudinal curvature**. |
| **Tightly curled** (the “bracelet” state) | Curved **along** its length (the strip makes a tube) – i.e. it has **longitudinal curvature** but **no transverse curvature**. |

The problem asks:

* **Why does the metal strip prefer one curvature direction at a time?**  
* **What gives it two distinct, stable configurations (bistability)?**  
* **How is the strip manufactured and what is its micro‑structure that makes this possible?**

In short: give a complete physical explanation of the bistable spring tape, from geometry through material mechanics to the production steps.

---

## 2. Detailed Explanation  

### 2.1. Geometry of a thin strip – Gauss curvature

A thin plate (thickness \(t \ll\) width \(w \ll\) length \(L\)) can bend in two principal directions:

* **Longitudinal direction** (along the length \(L\))
* **Transverse direction** (across the width \(w\))

If the strip bends **only** in one direction, its *Gaussian curvature* \(K = \kappa_{1}\kappa_{2}\) is zero because one principal curvature \(\kappa\) is zero.  

If it bends **simultaneously** in both directions (e.g. trying to make a spherical dome), the Gaussian curvature becomes non‑zero, and a *flat* sheet would have to stretch or compress in‑plane – an energetically expensive process for a metal that does not easily stretch.  

Hence a thin metal strip will naturally adopt **developable** shapes (zero Gaussian curvature). The two developable families relevant here are:

| Developable shape | Principal curvature(s) |
|-------------------|------------------------|
| **Cylindrical surface** (tube) | \(\kappa_{\text{long}} \neq 0,\; \kappa_{\text{trans}} = 0\) |
| **Cylindrical surface with the axis across the width** (cupped ribbon) | \(\kappa_{\text{long}} = 0,\; \kappa_{\text{trans}} \neq 0\) |

Both are energetically cheap because the metal only bends, it does not stretch.

### 2.2. Energy of bending a thin plate  

For an isotropic elastic plate the bending energy per unit area is  

\[
U_b = \frac{1}{2} D \left[(\kappa_{1} + \kappa_{2})^{2} - 2(1-\nu)\kappa_{1}\kappa_{2}\right]
\]

where  

* \(D = \dfrac{E t^{3}}{12(1-\nu^{2})}\) is the flexural rigidity,  
* \(E\) is Young’s modulus,  
* \(\nu\) is Poisson’s ratio,  
* \(\kappa_{1},\kappa_{2}\) are the two principal curvatures.

If only one curvature is present (\(\kappa_{2}=0\)) the energy simplifies to  

\[
U_b = \frac{1}{2} D \kappa_{1}^{2}.
\]

If both curvatures are non‑zero, the term \(-2(1-\nu)\kappa_{1}\kappa_{2}\) can *lower* the energy **only** when the material is pre‑stressed (as we will see). In a stress‑free strip the minimum energy is obtained by setting one curvature to zero → the two cylindrical families above.

Thus a flat metal strip **wants** to be either:

* a tube (curved along its length) **or**  
* a cup (curved across its width)

but not a combination.

### 2.3. Introducing a built‑in “pre‑stress” – the bistable spring  

The bistability arises because the strip is **manufactured with a permanent curvature in one direction**, and then **released** so that the opposite curvature can also be accessed.

#### 2.3.1. The “pre‑curved” state  

During production a long steel ribbon (typically 0.2 mm–0.5 mm thick) is **cold‑rolled** while it is forced to follow a **large radius cylindrical die**. The die bends the strip in the *transverse* direction, giving it a gentle “cup” shape (concave upward). The curvature radius \(R_{\text{trans}}\) is chosen such that the bending strain is well below the yield strain, so the material remains elastic.

#### 2.3.2. Setting a *neutral axis* offset (the “bias”)  

After the strip leaves the die it is **heat‑treated** (or simply left to relax) while **clamped at its two ends**. Because the ends are held straight, the strip cannot adopt the transverse curvature everywhere. The interior tries to curl, but the ends force a straight segment. The result is a **built‑in bending moment** \(M_0\) distributed along the length; the strip stores elastic energy in a *pre‑stressed* state.

Mathematically, the stored moment is  

\[
M_0 = D \, \kappa_{\text{trans}} \, (1-\nu).
\]

This moment is the **source of the bistability**: it can be released by allowing the strip to flip its curvature direction.

#### 2.3.3. From pre‑curved to bistable  

When the strip is later **released from its end constraints**, two equilibrium configurations are possible:

1. **Stay in the transverse‑curved (cup) mode** – the strip keeps the original curvature, the stored moment is balanced by the internal stress.
2. **Snap into the longitudinal‑curved (tube) mode** – the strip rotates the curvature axis by 90°, converting the stored transverse moment into a longitudinal bending moment. Because the tube shape also has zero Gaussian curvature, the energy required is comparable, and the strip can settle there.

Both configurations have **the same total bending energy** (within a few percent), so they are **stable**; the strip will stay in whichever shape it is placed unless an external disturbance (a tap) provides enough energy to overcome the *energy barrier* separating them.

### 2.4. The energy barrier – why a tap makes it snap  

The barrier corresponds to a transient state where the strip has *both* curvatures non‑zero (it must bend in two directions simultaneously while flipping). The Gaussian curvature becomes non‑zero, forcing in‑plane stretching. The extra stretching energy is roughly  

\[
U_{\text{stretch}} \approx \frac{E t}{2} \left(\frac{\epsilon^{2}}{1-\nu^{2}}\right) A,
\]

where \(\epsilon \sim (t/R)^{2}\) is the strain induced by forcing a doubly‑curved shape. Because \(t\) is tiny but \(E\) is large (≈200 GPa for spring steel), the barrier is **a few millijoules** – enough that a modest impulse (the “tap”) can push the strip over it.

Once past the barrier, the strip relaxes into the other developable shape and the stored elastic energy is released, producing the audible “snap”.

### 2.5. Why the two specific stable states are useful  

| Application | Desired stable state | Reason |
|-------------|---------------------|--------|
| **Snap bracelet** | **Longitudinal tube** (tight coil) | Gives a compact band that hugs the wrist; the tube geometry provides high stiffness in the radial direction, so the bracelet does not flatten under the skin. |
| **Self‑retracting tape measure** | **Transverse cup** (flat‑straight) while extended | The cup shape stiffens the tape against sagging under its own weight; the upward concavity creates a restoring moment that pushes the tape back onto the spool when released. |

Both devices exploit the *same* bistable strip, just oriented differently.

### 2.6. Manufacturing steps in practice  

| Step | What is done | Result on micro‑structure |
|------|--------------|---------------------------|
| **1. Material selection** | High‑carbon spring steel (≈0.8 % C) is chosen for high yield strength and good fatigue. | Grain size ~10 µm, uniform across the sheet. |
| **2. Cold rolling to final thickness** | The steel is passed through rollers, reducing thickness to 0.2–0.5 mm. | The metal becomes work‑hardened; dislocation density rises, giving a higher elastic modulus in the sheet plane. |
| **3. Pre‑curving (transverse bending)** | Sheet is fed over a large‑radius cylindrical mandrel (R ≈ 5–10 cm). The mandrel may be heated to ~150 °C to avoid cracking. | A permanent elastic curvature is imposed; the outer fibers are in tension, inner fibers in compression. |
| **4. End clamping & heat‑set** | While still on the mandrel the ends are clamped flat (often by a welding jig). The piece is then **annealed** at ~300 °C for a few minutes and quenched. | The anneal relieves residual stresses except those locked by the clamped ends, leaving a *bending moment* \(M_0\). |
| **5. Cutting to length** | The strip is sheared into the required lengths (≈15 cm for bracelets, longer for tape measures). | No additional deformation; the built‑in moment remains. |
| **6. Surface protection** | A thin polymer sheath (PVC, polypropylene) is extrusion‑bonded to both faces, or a separate fabric sleeve is added. | Prevents the sharp edges from cutting skin and provides friction for the tape‑measure reel. |
| **7. Final assembly** | For a tape measure: the strip is spooled onto a spring‑loaded reel with a hook; for a bracelet it is inserted into a fabric sleeve. | The strip’s two stable states are now ready to be used. |

At the microscopic level the strip is **homogeneous metal**; the bistability does **not** rely on a composite or a “spring‑coil” geometry. It is purely a **geometric effect** produced by a permanent bending moment introduced during manufacturing.

### 2.7. Summary of the physics  

1. **Developable surfaces** (zero Gaussian curvature) are the only low‑energy shapes a thin sheet can adopt without stretching.  
2. By **pre‑curving the strip in one direction while restraining its ends**, a **locked bending moment** is stored.  
3. The stored moment makes two *different* developable shapes have almost identical total elastic energy → **bistability**.  
4. Transition between them requires a brief doubly‑curved (high‑energy) configuration; a small tap supplies that energy.  
5. The same strip can be used either as a **tube** (snap bracelet) or a **cup** (retractable tape) depending on how it is initially oriented.

---

## 3. Final Answer  

- The metal tape in a snap‑bracelet or retractable tape measure is a **thin, elastic steel strip that has been cold‑rolled into a permanent transverse curvature while its ends are held straight**.  
- This processing creates a **locked bending moment** (pre‑stress) that makes the strip equally happy to be curved **across its width** (a cupped, straight‑looking shape) **or along its length** (a tight tube). Both shapes are *developable* (zero Gaussian curvature) and therefore require only bending, not stretching.  
- Because the strip stores elastic energy in the pre‑stress, both configurations are **local minima of the bending energy** → the strip is *bistable*.  
- A small impact (a tap) provides enough energy to push the strip over the high‑energy intermediate state where it would have to bend in both directions simultaneously; once over the barrier it snaps into the other stable shape.  
- The manufacturing steps are: (i) select high‑carbon spring steel, (ii) cold‑roll to final thickness, (iii) bend over a large‑radius die while clamping the ends, (iv) anneal/heat‑set to lock the bending moment, (v) cut to length, and (vi) encase in a protective polymer sheath.  

Thus the “directional tendency to curl” comes from **geometric constraints combined with a deliberately introduced bending moment**, not from any special micro‑structure beyond ordinary work‑hardened steel.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|--------|----------------|-----------------|
| **Thinking the strip is a coiled spring** | The strip has *no* helical winding; it is a single flat piece. | Emphasize that the bistability originates from *developable* shapes, not from a coil geometry. |
| **Assuming the two stable shapes have the same curvature magnitude** | The transverse cup and longitudinal tube can have different radii; only the *total bending energy* needs to be comparable. | Show the energy formula and note that the radius may differ by a factor of ~2–3 in real devices. |
| **Neglecting the role of the clamped ends during heat‑setting** | Without end restraint the strip would simply relax to its original cupped shape, losing bistability. | Mention explicitly that

*Original question: [How does the bistable spring tape in a slap bracelet (or retractable tape measure) work?](https://physics.stackexchange.com/questions/875999/how-does-the-bistable-spring-tape-in-a-slap-bracelet-or-retractable-tape-measur) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
