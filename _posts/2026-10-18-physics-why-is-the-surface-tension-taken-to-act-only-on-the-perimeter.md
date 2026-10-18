---
layout: question
title: Why is the Surface tension taken to act only on the perimeter?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Why is the Surface tension taken to act
  only on the perimeter?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. Restating the question in plain language  

A thin circular disc is placed on the surface of a liquid and we try to lift it straight up.  
The textbook formula for the upward force that the liquid can provide is  

\[
F_{\text{up}} = mg + T\,(2\pi r)
\]

where  

* \(m\) – mass of the disc,  
* \(g\) – gravitational acceleration,  
* \(r\) – radius of the disc,  
* \(T\) – surface‑tension coefficient of the liquid (force per **unit length**).

The student wonders:

* Why does the surface‑tension term contain only the **perimeter** \(2\pi r\) and not the whole area \(\pi r^{2}\) of the disc?  
* When we pull the disc upward the liquid surface that touches the disc becomes (almost) horizontal, so isn’t the surface‑tension force acting **downward over the whole contact area**?

We must explain why surface tension contributes a line force acting only along the contact line and why a vertical component appears only there, not over the whole wetted area.

---

## 2. Detailed step‑by‑step answer  

### 2.1 What *surface tension* really is  

1. **Molecular picture** – At the liquid‑air interface molecules have fewer neighbours on the air side, so they pull each other tighter. This creates an **excess free energy** proportional to the *area* of the interface.  

2. **Mechanical picture** – The excess energy manifests as a **force per unit length** that tries to contract any line drawn on the surface.  
   \[
   T \; \bigl[\text{N m}^{-1}\bigr] = \frac{\text{force}}{\text{length}}
   \]

   Hence surface tension is *not* a pressure (force per area); it is a **line force**.

3. **Direction of the force** – The force always acts **tangentially** to the interface, pulling **along** the surface, *not* perpendicular to it.  

   ![Surface‑tension vector acting along the interface](attachment:surface_tension_vector.png)

### 2.2 How a solid object interacts with the interface  

Consider the circular disc of radius \(r\) that sits on the liquid. The liquid‑air interface meets the solid along a closed **contact line** (the disc’s perimeter).  

* Along that line the surface is curved because the disc pushes the liquid down a little.  
* At every point of the contact line the surface‑tension force \( \mathbf{T} \) points **tangent to the liquid surface**, i.e. **in the plane of the surface**.  

If the local surface makes an angle \(\theta\) with the horizontal (see figure), the tension vector can be decomposed into:

* a horizontal component \(T\cos\theta\) (which cancels around the whole circle by symmetry), and  
* a **vertical component** \(T\sin\theta\) that points **upward** (if the surface is pulled up around the disc).  

Because the disc is axisymmetric, the vertical components from every element of the contact line add up constructively.

### 2.3 Calculating the total vertical contribution  

Take an infinitesimal element of the contact line of length \(\mathrm{d}s = r\,\mathrm{d}\phi\) (where \(\phi\) is the azimuthal angle).  

* The magnitude of the tension force on that element is \(T\,\mathrm{d}s\).  
* Its upward component is \(T\,\mathrm{d}s\sin\theta\).

Integrating around the whole circle:

\[
F_{\text{T,\,up}} = \int_{0}^{2\pi} T\, r\,\mathrm{d}\phi \; \sin\theta
                = T\,(2\pi r)\,\sin\theta .
\]

*If the meniscus is such that \(\theta = 90^{\circ}\) (the surface is vertical right at the contact line), then \(\sin\theta = 1\) and we obtain the simple expression used in the textbook*

\[
\boxed{F_{\text{T,\,up}} = T\,(2\pi r)} .
\]

In reality \(\theta\) is slightly less than \(90^{\circ}\); the exact value depends on the wetting angle and on how far the disc is pulled. The textbook formula assumes the **maximum possible upward contribution** (i.e. the contact line is pinned and the liquid surface is essentially vertical there).

### 2.4 Why the *area* does **not** appear  

* The liquid exerts a **hydrostatic pressure** on the bottom face of the disc. That pressure acts over the **whole wetted area** and gives the usual buoyant force  
  \[
  F_{\text{buoy}} = \rho_{\ell} g\,V_{\text{submerged}} .
  \]  
  This term is already accounted for (often implicitly) in the \(mg\) part of the force balance, because the disc can be partially submerged.

* **Surface tension itself never acts over an area.** It is a line force, so the only place it can act on a solid is **where the liquid surface meets the solid**, i.e. the *contact line*.  
  Trying to spread the same force over the whole area would give a force of order \(T \times \text{area}\), which is dimensionally incorrect (N m\(^{-1}\) × m\(^{2}\) = N m, not N).

Thus the only correct way to write the contribution of surface tension is to multiply the tension coefficient \(T\) by the **length** of the contact line.

### 2.5 Putting everything together – force balance for lifting the disc  

When the disc is just about to leave the surface, the upward forces equal the weight:

\[
\underbrace{\rho_{\ell} g V_{\text{submerged}}}_{\text{hydrostatic buoyancy}} 
\;+\; \underbrace{T (2\pi r)\sin\theta}_{\text{vertical component of surface tension}}
\;=\; mg .
\]

If the disc is *light* enough that the hydrostatic term alone cannot support its weight, the extra term \(T(2\pi r)\sin\theta\) provides the necessary lift.  
In the special case of a *fully horizontal* free surface (\(\theta=0\)) the vertical component vanishes, and surface tension does **not** help the disc rise.

---

## 3. Final answer  

*Surface tension is a force **per unit length** that acts **tangentially** along the liquid‑air interface. The only place where the liquid surface touches the solid disc is along the **perimeter** (the contact line). Hence the total surface‑tension force that can support the disc is the tension coefficient \(T\) multiplied by the length of that line, i.e. \(T\,(2\pi r)\).*

The vertical component of that line force is \(T(2\pi r)\sin\theta\); in the textbook’s “maximum‑support” approximation \(\sin\theta\approx 1\), giving the simple term \(T(2\pi r)\). The rest of the liquid’s upward support comes from ordinary hydrostatic pressure acting over the disc’s wetted *area*, not from surface tension.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating surface tension as a pressure (force/area).** | Surface tension has units N m\(^{-1}\); pressure has units N m\(^{-2}\). They are different physical quantities. | Remember the definition: *surface tension = force acting along a line*. Use it only on the contact line. |
| **Adding \(T\) over the whole wetted area (\(T\pi r^{2}\)).** | Gives the wrong dimensions (N m) and over‑estimates the force by a factor of order \(r\). | Write the surface‑tension contribution as \(T \times (\text{perimeter})\). |
| **Assuming the surface‑tension force is always vertical.** | The tension vector is tangent to the interface; only its vertical component (proportional to \(\sin\theta\)) contributes upward. | Decompose the tension into vertical and horizontal components; include the contact‑angle factor \(\sin\theta\). |
| **Neglecting hydrostatic pressure and attributing all lift to surface tension.** | The liquid pressure on the bottom of the disc provides buoyancy, which can be comparable or larger than the tension term. | Write the full force balance: weight = buoyancy + vertical component of surface tension. |
| **Thinking the liquid surface must become perfectly horizontal when the disc is lifted.** | The surface near the contact line is curved; that curvature is what creates the vertical component of the tension. | Visualise the meniscus: a curved surface gives a non‑zero \(\theta\) and thus a vertical component. |

By keeping these points in mind, you’ll correctly apply surface tension to problems involving floating or partially submerged objects.

*Original question: [Why is the Surface tension taken to act only on the perimeter?](https://physics.stackexchange.com/questions/877020/why-is-the-surface-tension-taken-to-act-only-on-the-perimeter) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
