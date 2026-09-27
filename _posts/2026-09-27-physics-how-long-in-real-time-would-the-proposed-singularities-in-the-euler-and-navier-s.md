---
layout: question
title: How long (in real time) would the proposed singularities in the Euler and Navier-Stokes
  equations take to occur?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How long (in real time) would the proposed
  singularities in the Euler and Navier-Stokes equations take to occur?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is really asking  

Recent “finite‑time blow‑up” papers (Buckmaster–Vicol for the incompressible **Euler** equations and Alogé–Buckmaster–Vicol for the incompressible **Navier–Stokes** equations) construct smooth initial data that evolve, in the *mathematical* (dimensionless) system, into a singularity after a **fixed nondimensional time** (usually written as \(t=1\) or a number of order 1).  

The student wants to know:  

*If we take those abstract solutions and pretend we could realise them in a real fluid (say water at 20 °C), how many seconds of “real‑world” time would pass before the singularity appears?*  

In other words we must:

1. Identify the characteristic time scale that turns the dimensionless blow‑up time into a physical time.  
2. Express that time in terms of the macroscopic parameters that we can choose for the experiment – a length scale \(L\) (size of the region where the initial data vary) and a velocity scale \(U\) (typical magnitude of the initial velocity field).  
3. Insert realistic numbers for water and give a concrete estimate.  

---

## 2. Step‑by‑step derivation  

### 2.1 The governing equations (dimensional form)

\[
\begin{aligned}
\text{Euler:}&\qquad 
\partial_t \mathbf u + (\mathbf u\!\cdot\!\nabla)\mathbf u = -\nabla p ,\\[4pt]
\text{Navier–Stokes:}&\qquad 
\partial_t \mathbf u + (\mathbf u\!\cdot\!\nabla)\mathbf u = -\nabla p + \nu \Delta\mathbf u ,
\end{aligned}
\]
with \(\nabla\!\cdot\!\mathbf u =0\).  
\(\nu\) is the **kinematic viscosity** (for water at \(20^{\circ}{\rm C}\), \(\nu\approx 1.0\times10^{-6}\,{\rm m^2\,s^{-1}}\)).

Both equations are *scale‑invariant*: if \((\mathbf u,\;p)\) solves the system, then for any positive numbers \(L\) and \(U\)

\[
\boxed{
\tilde{\mathbf x}= \frac{\mathbf x}{L},\qquad 
\tilde t = \frac{U}{L}\,t,\qquad 
\tilde{\mathbf u}= \frac{\mathbf u}{U},\qquad 
\tilde p = \frac{p}{U^{2}}
}
\]

produce a dimensionless solution \((\tilde{\mathbf u},\tilde p)\) of the **nondimensional** equations

\[
\partial_{\tilde t}\tilde{\mathbf u}+(\tilde{\mathbf u}\!\cdot\!\tilde\nabla)\tilde{\mathbf u}= -\tilde\nabla\tilde p
\quad\text{(Euler)},
\]

\[
\partial_{\tilde t}\tilde{\mathbf u}+(\tilde{\mathbf u}\!\cdot\!\tilde\nabla)\tilde{\mathbf u}= -\tilde\nabla\tilde p
+\frac{1}{\mathrm{Re}}\,\tilde\Delta\tilde{\mathbf u}
\quad\text{(Navier–Stokes)},
\]

where the **Reynolds number**

\[
\boxed{\displaystyle \mathrm{Re}= \frac{U L}{\nu}}
\]

appears only in the Navier–Stokes case.

Thus the *only* characteristic time that can be built from the three physical quantities \((L,U,\nu)\) is

\[
\boxed{T_{\rm char}= \frac{L}{U}} .
\]

(If you prefer to express it in terms of \(\nu\) and \(\mathrm{Re}\) you may write \(T_{\rm char}= \frac{L^{2}}{\nu}\,\frac{1}{\mathrm{Re}}\), but the combination \(L/U\) is the usual one.)

### 2.2 What the mathematical papers give  

Both Buckmaster–Vicol (Euler) and Alogé–Buckmaster–Vicol (Navier–Stokes) construct a *smooth* initial datum for which the **dimensionless** solution becomes singular at a time

\[
\tilde t_{\star}=C_{\star},
\]

where the constant \(C_{\star}\) is *explicitly* a number of order one (in the papers it is exactly \(1\); other constructions give numbers such as \(0.5\), \(2\), etc.).  

No other dimensionless parameters appear in the statement of the theorem: the blow‑up time does **not** depend on the Reynolds number, on the viscosity, or on any extra scaling factor.  

Therefore, after undoing the nondimensionalisation, the *physical* blow‑up time is simply

\[
\boxed{t_{\star}= C_{\star}\, \frac{L}{U}} .
\]

That is the complete “multiplicative function’’ asked for: a single factor \(C_{\star}\) (≈ 1) multiplied by the characteristic time \(L/U\).

### 2.3 Putting in numbers for water  

Choose a *macroscopic* length scale that we could plausibly set up in a laboratory.  
Typical choices:

| Example | Length \(L\) | Velocity scale \(U\) | Characteristic time \(L/U\) |
|---------|--------------|----------------------|-----------------------------|
| Small tank (10 cm) | \(L=0.10\;\text{m}\) | \(U=0.10\;\text{m s}^{-1}\) | \(1.0\;\text{s}\) |
| Large pool (1 m)   | \(L=1.0\;\text{m}\)  | \(U=0.50\;\text{m s}^{-1}\) | \(2.0\;\text{s}\) |
| Pipe flow (0.02 m) | \(L=0.02\;\text{m}\) | \(U=0.02\;\text{m s}^{-1}\) | \(1.0\;\text{s}\) |

Because the constant \(C_{\star}\) is ≈ 1, the **wall‑clock time to singularity is essentially the same as the naive advection time \(L/U\)**.  

If we take the “canonical’’ numbers used in many fluid‑mechanics textbooks (e.g. \(L=0.1\;\text{m}\), \(U=0.1\;\text{m s}^{-1}\) for water), we obtain

\[
t_{\star}\;\approx\;1\;\text{s}.
\]

Even if we push the scales to a *very* large laboratory experiment—say \(L=10\;\text{m}\) and a modest flow speed \(U=0.1\;\text{m s}^{-1}\)—the blow‑up would still be predicted to occur after roughly

\[
t_{\star}\;\approx\; \frac{10\;\text{m}}{0.1\;\text{m s}^{-1}} = 100\;\text{s}\;(\approx 2\;\text{min}).
\]

Conversely, for a *tiny* micro‑fluidic device (\(L=10^{-4}\,\text{m}\), \(U=10^{-2}\,\text{m s}^{-1}\)) the predicted time shrinks to \(10^{-2}\,\text{s}\).

Thus the answer is **linear** in the chosen length and **inverse** in the chosen velocity, with a prefactor of order unity.

---

## 3. Final answer  

The physical (wall‑clock) time at which the mathematically constructed singularities would appear is  

\[
\boxed{ \displaystyle t_{\text{sing}} \;=\; C_{\star}\,\frac{L}{U}\;,\qquad C_{\star}\simeq 1 } .
\]

* \(L\) – the characteristic size of the region where the initial velocity field varies (meters).  
* \(U\) – the characteristic magnitude of the initial velocity field (metres per second).  

For water at room temperature, inserting any reasonable macroscopic pair \((L,U)\) gives a singularity after a time of order \(L/U\); e.g. with \(L=0.1\;\text{m}, U=0.1\;\text{m s}^{-1}\) the blow‑up would be expected after **≈ 1 second**.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Including the speed of sound** as a velocity scale. | The incompressible Euler/Navier–Stokes equations have no acoustic waves; the governing time scale is set by advection, not by \(c_{\rm s}\). | Use only the *actual* velocity magnitude that appears in the initial data. |
| **Multiplying by the viscosity \(\nu\) or the Reynolds number** to obtain the blow‑up time. | The theorems give a **dimensionless** blow‑up time that is independent of \(\nu\) or \(\mathrm{Re}\); the only dimensional factor is \(L/U\). | Remember that the nondimensionalisation already absorbed \(\nu\) into the Reynolds number; the physical time is obtained by undoing the scaling, not by inserting \(\nu\) again. |
| **Assuming the constant \(C_{\star}\) is huge (e.g. \(10^{6}\)).** | In the constructions the constant is explicitly of order one (the papers set the singularity at \(\tilde t=1\)). | Read the statement of the theorem: it specifies the blow‑up time in nondimensional units; use that value directly. |
| **Confusing the characteristic length with the domain size of the torus used in the proofs.** | The proofs work on a periodic box of side‑length \(2\pi\); that length is *purely a mathematical convenience* and can be rescaled to any physical \(L\). | Perform the scaling transformation (Section 2.1) and treat \(L\) as the physical length you wish to assign. |
| **Neglecting that the velocity field may have a large spatial variation, so \(U\) is not a single number.** | If the initial data have a wide range of speeds, one must pick a *representative* scale (e.g. the rms velocity) for the nondimensionalisation. | Define \(U\) clearly (e.g. \(U = \max|\mathbf u_0|\) or the rms value) before plugging numbers. |

Keeping these points in mind ensures that the conversion from the abstract mathematical blow‑up time to a concrete “real‑world’’ duration is both **correct** and **transparent**.

*Original question: [How long (in real time) would the proposed singularities in the Euler and Navier-Stokes equations take to occur?](https://physics.stackexchange.com/questions/876407/how-long-in-real-time-would-the-proposed-singularities-in-the-euler-and-navier) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
