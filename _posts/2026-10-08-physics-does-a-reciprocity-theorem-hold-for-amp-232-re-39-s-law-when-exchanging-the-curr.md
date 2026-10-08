---
layout: question
title: Does a reciprocity theorem hold for Amp&#232;re&#39;s law when exchanging the
  current loop and the integration path?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Does a reciprocity theorem hold for Amp&#232;re&#39;s
  law when exchanging the current loop and the integration path?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (plain language)

We have two *closed* curves in space:

* **\(C_{1}\)** – a thin wire that actually carries a steady current \(I\).  
  It creates a magnetic field \(\mathbf B_{1}(\mathbf r)\).

* **\(C_{2}\)** – an *imaginary* closed curve that we may draw anywhere.  
  If we integrate the field \(\mathbf B_{1}\) round this curve we obtain, by
  Ampère’s law,
  \[
  \oint_{C_{2}}\mathbf B_{1}\!\cdot d\boldsymbol\ell_{2}= \mu_{0}\,I_{\text{enclosed by }C_{2}} .
  \tag{1}
  \]

Now we **swap the roles**:

* The current is removed from the real wire \(C_{1}\) and is instead forced to flow along the previously‑imaginary curve \(C_{2}\) (still the same magnitude \(I\)).  
  This produces a new magnetic field \(\mathbf B_{2}(\mathbf r)\).

* We now integrate \(\mathbf B_{2}\) round the *original* physical wire \(C_{1}\):
  \[
  \oint_{C_{1}}\mathbf B_{2}\!\cdot d\boldsymbol\ell_{1}= \mu_{0}\,I_{\text{enclosed by }C_{1}} .
  \tag{2}
  \]

The question is: **Are the two line integrals always equal?** In symbols,
\[
\boxed{\;\displaystyle 
\oint_{C_{2}}\mathbf B_{1}\!\cdot d\boldsymbol\ell_{2}
=
\oint_{C_{1}}\mathbf B_{2}\!\cdot d\boldsymbol\ell_{1}\;}
\tag{3}
\]

In other words, does Ampère’s law possess a “reciprocity” property analogous to the well‑known mutual‑inductance symmetry \(M_{12}=M_{21}\)?

---

## 2.  Detailed derivation  

### 2.1  Ampère’s law in integral form  

For a **steady** (time‑independent) current distribution in free space,
\[
\oint_{C}\mathbf B\cdot d\boldsymbol\ell =\mu_{0}\,I_{\text{enc}}(C) .
\tag{4}
\]

The right‑hand side is the *total* current that threads any surface
\(S\) whose boundary is the curve \(C\):
\[
I_{\text{enc}}(C)=\int_{S}\mathbf J\cdot d\mathbf a .
\]

Because \(\nabla\!\cdot\!\mathbf J =0\) (steady current), the value of the surface integral is **independent of the particular surface** as long as the surface has the same edge \(C\).  

Consequently the line integral (4) depends only on how many times the curve \(C\) winds around the *physical* current‑carrying wire(s).

### 2.2  Linking number  

Define the **linking number** \(L(C_{1},C_{2})\) of two closed curves as the (signed) number of times one curve winds around the other.  It can be written as a surface integral:

\[
L(C_{1},C_{2})=\frac{1}{4\pi}\oint_{C_{1}}\!\!\oint_{C_{2}}
\frac{(\mathbf r_{1}-\mathbf r_{2})\cdot
\bigl(d\mathbf r_{1}\times d\mathbf r_{2}\bigr)}
{|\mathbf r_{1}-\mathbf r_{2}|^{3}} .
\tag{5}
\]

\(L\) is an *integer* (or zero) and is unchanged by any smooth deformation of either curve that does **not** let one pass through the other.

### 2.3  The line integral produced by a filament current  

Suppose a thin filament carries a current \(I\) along the curve \(C_{1}\).  
Its magnetic field is given by the Biot–Savart law

\[
\mathbf B_{1}(\mathbf r)=\frac{\mu_{0} I}{4\pi}
\oint_{C_{1}}\frac{d\mathbf r_{1}\times(\mathbf r-\mathbf r_{1})}
{|\mathbf r-\mathbf r_{1}|^{3}} .
\tag{6}
\]

Now evaluate the Ampèrian line integral around an *arbitrary* second closed curve \(C_{2}\):

\[
\begin{aligned}
\oint_{C_{2}}\mathbf B_{1}\!\cdot d\boldsymbol\ell_{2}
&= \frac{\mu_{0} I}{4\pi}
\oint_{C_{2}}\!\!\oint_{C_{1}}
\frac{d\mathbf r_{1}\times(\mathbf r_{2}-\mathbf r_{1})}
{|\mathbf r_{2}-\mathbf r_{1}|^{3}}
\cdot d\mathbf r_{2} \\[4pt]
&= \mu_{0} I\;
\underbrace{\frac{1}{4\pi}\oint_{C_{2}}\!\!\oint_{C_{1}}
\frac{(\mathbf r_{2}-\mathbf r_{1})\cdot
\bigl(d\mathbf r_{2}\times d\mathbf r_{1}\bigr)}
{|\mathbf r_{2}-\mathbf r_{1}|^{3}}}_{\displaystyle =\,L(C_{1},C_{2})} .
\end{aligned}
\tag{7}
\]

Thus

\[
\boxed{\displaystyle 
\oint_{C_{2}}\mathbf B_{1}\!\cdot d\boldsymbol\ell_{2}= \mu_{0} I\,L(C_{1},C_{2}) } .
\tag{8}
\]

Exactly the same algebra, with the roles of the curves interchanged,
gives

\[
\boxed{\displaystyle 
\oint_{C_{1}}\mathbf B_{2}\!\cdot d\boldsymbol\ell_{1}= \mu_{0} I\,L(C_{2},C_{1}) } .
\tag{9}
\]

But the linking number is **symmetric**:

\[
L(C_{1},C_{2}) = L(C_{2},C_{1}) .
\tag{10}
\]

Combining (8)–(10) we obtain the desired reciprocity:

\[
\boxed{\displaystyle 
\oint_{C_{2}}\mathbf B_{1}\!\cdot d\boldsymbol\ell_{2}
=
\oint_{C_{1}}\mathbf B_{2}\!\cdot d\boldsymbol\ell_{1}
= \mu_{0} I \,L(C_{1},C_{2}) } .
\tag{11}
\]

### 2.4  Interpretation in terms of Ampère’s law  

Equation (11) tells us that the line integral equals \(\mu_{0}I\) multiplied by the **integer linking number**.  From the viewpoint of Ampère’s law, the quantity \(I_{\text{enclosed}}\) in (4) is precisely \(\displaystyle I\;L(C_{1},C_{2})\).  Hence the “enclosed‑current’’ term is the same whichever curve we choose as the integration path, provided the *same* physical current filament is present.

### 2.5  When can the equality fail?  

| Situation | Reason it would **break** the equality |
|-----------|----------------------------------------|
| **No linkage** (\(L=0\)) | Both integrals are zero, so equality still holds (trivial case). |
| **Time‑varying currents** | Ampère’s law must be supplemented by the displacement current term \(\displaystyle \mu_{0}\varepsilon_{0}\,\partial\mathbf E/\partial t\).  The simple form (4) no longer applies; the reciprocity still holds for the *magnetostatic* part but an extra term appears. |
| **Non‑linear, anisotropic, or inhomogeneous magnetic media** | Ampère’s law in the form \(\nabla\times\mathbf B = \mu_{0}\mathbf J\) is replaced by \(\nabla\times\mathbf H = \mathbf J\) with \(\mathbf B = \mu(\mathbf r)\mathbf H\).  The line integral of \(\mathbf B\) now depends on the path because \(\mu\) varies, and the simple link‑number result is lost. |
| **Current distributed over a surface that is cut by one of the loops** | If the “current filament’’ is not a thin wire but a sheet that intersects the integration surface, the notion of a single linking number is ambiguous; the integral equals \(\mu_{0}\) times the *net* current that actually threads the surface, which may differ for the two choices. |
| **Topologically non‑trivial space** (e.g., a space with a hole that the curves can wind around) | The derivation above uses only the linking number, which is a topological invariant defined in any three‑dimensional manifold.  As long as the manifold is oriented and simply‑connected away from the currents, the result still holds.  Exotic manifolds that prevent a surface bounded by a given curve from being defined would violate the premises of Ampère’s law. |

In ordinary laboratory conditions—steady currents flowing in thin wires in ordinary (free‑space or linear, isotropic) media—the equality **always** holds.

---

## 3.  Final answer  

Yes.  
For any two closed curves \(C_{1}\) and \(C_{2}\) in free space, each carrying the same steady current \(I\) (one at a time), the Ampèrian line integrals satisfy  

\[
\boxed{\displaystyle 
\oint_{C_{2}}\mathbf B_{1}\!\cdot d\boldsymbol\ell_{2}
=
\oint_{C_{1}}\mathbf B_{2}\!\cdot d\boldsymbol\ell_{1}
= \mu_{0}\,I\;L(C_{1},C_{2}) } .
\]

The common value is \(\mu_{0}I\) multiplied by the (signed) linking number of the two loops.  Thus the “reciprocity’’ is a direct consequence of Ampère’s law together with the topological invariant linking number; it is equivalent to the well‑known symmetry of mutual inductance \(M_{12}=M_{21}\).

---

## 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing the line integral of \(\mathbf B\) with the flux through a surface.** | Ampère’s law involves a *circulation* \(\oint\mathbf B\!\cdot d\boldsymbol\ell\), not \(\int\mathbf B\!\cdot d\mathbf a\).  The flux appears in the definition of mutual inductance, not directly here. | Remember that Stokes’ theorem converts the *circulation* into the surface integral of \(\nabla\times\mathbf B\), which equals \(\mu_{0}\mathbf J\). |
| **Assuming the equality holds for arbitrary media.** | In a material with spatially varying permeability, \(\mathbf B\) is not proportional to \(\mathbf H\) uniformly, so the integral can depend on the path. | Restrict the proof to free space (or a linear, homogeneous, isotropic medium) where \(\nabla\times\mathbf B = \mu_{0}\mathbf J\) holds. |
| **Neglecting the sign (orientation) of the linking number.** | The direction in which each loop is traversed determines the sign of the integral; swapping the orientation flips the sign. | Keep track of the right‑hand rule: the normal to the surface bounded by \(C\) follows the direction of \(d\boldsymbol\ell\) by the right‑hand rule. |
| **Using the result for time‑varying currents without the displacement current term.** | Ampère’s law in its static form omits \(\mu_{0}\varepsilon_{0}\partial\mathbf E/\partial t\); when fields vary, the extra term contributes. | State explicitly that the currents are steady (magnetostatic). |
| **Thinking that a non‑linked pair of loops must give a non‑zero integral.** | If the

*Original question: [Does a reciprocity theorem hold for Amp&#232;re&#39;s law when exchanging the current loop and the integration path?](https://physics.stackexchange.com/questions/876710/does-a-reciprocity-theorem-hold-for-amp%c3%a8res-law-when-exchanging-the-current-loo) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
