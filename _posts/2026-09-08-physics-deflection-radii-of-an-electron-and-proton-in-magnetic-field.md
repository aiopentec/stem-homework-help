---
layout: question
title: Deflection Radii of an Electron and Proton in Magnetic Field
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Deflection Radii of an Electron and Proton
  in Magnetic Field'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. Restating the problem in plain language  

Two particles – an electron and a proton – are fired into a region that contains a uniform magnetic field **B**.  
Both particles are given **the same magnitude of linear momentum** \(p\).  

*Question:*  

- Will the two particles follow circular paths with the same radius, or will the electron’s much smaller mass make its path tighter?  

In other words, does the larger acceleration that the electron experiences (because \(a = F/m\)) change the radius of curvature, or does the equality of momenta guarantee identical radii?

---

## 2. Detailed solution (no steps skipped)

### 2.1. Forces acting on a charged particle in a magnetic field  

A particle of charge \(q\) moving with velocity \(\mathbf{v}\) perpendicular to a uniform magnetic field \(\mathbf{B}\) feels the Lorentz (magnetic) force  

\[
\mathbf{F}_\text{mag}=q\,\mathbf{v}\times\mathbf{B}.
\]

Because the force is always perpendicular to the velocity, it does no work; it only changes the direction of the motion, forcing the particle onto a circle.

The magnitude of the magnetic force is  

\[
F_\text{mag}=|q|\,vB \qquad (\text{for } \mathbf{v}\perp\mathbf{B}).
\]

### 2.2. Relating the magnetic force to the required centripetal force  

For uniform circular motion of radius \(r\) and speed \(v\), the required centripetal force is  

\[
F_\text{cent}= \frac{m v^{2}}{r}.
\]

Setting the magnetic force equal to the centripetal force (the only force providing the centripetal acceleration) gives  

\[
|q|\,vB = \frac{m v^{2}}{r}.
\]

### 2.3. Solving for the radius  

Cancel one factor of \(v\) (the particle is moving, so \(v\neq0\)):

\[
|q| B = \frac{m v}{r}\;\;\Longrightarrow\;\;
r = \frac{m v}{|q| B}.
\]

Introduce the **linear momentum** \(p = m v\). The expression becomes

\[
\boxed{\,r = \frac{p}{|q| B}\,}.
\]

Notice that **the mass \(m\) has disappeared**; the radius depends only on the particle’s momentum, its charge magnitude, and the magnetic field strength.

### 2.4. Apply the formula to the electron and the proton  

Both particles have the same **momentum magnitude** \(p\) (by hypothesis) and the same **charge magnitude** \(|q| = e = 1.602\times10^{-19}\,\text{C}\) (the electron’s charge is \(-e\), the proton’s is \(+e\)).  

Therefore

\[
r_\text{electron}= \frac{p}{e B},
\qquad
r_\text{proton}= \frac{p}{e B},
\]

so  

\[
\boxed{r_\text{electron}=r_\text{proton}}.
\]

The only difference is the **direction** of curvature: the electron’s negative charge makes it curve opposite to the proton’s, but the *size* of the circular path is identical.

### 2.5. Why the “greater acceleration” argument does **not** change the radius  

From the force‑balance we can also write the centripetal acceleration:

\[
a = \frac{v^{2}}{r}= \frac{|q|\,vB}{m}.
\]

If we keep the **momentum** fixed, the speed of each particle is  

\[
v = \frac{p}{m}.
\]

Insert this into the expression for \(a\):

\[
a = \frac{|q|\,B}{m}\,\frac{p}{m}
   = \frac{|q|\,B\,p}{m^{2}}.
\]

Because the electron’s mass is \(\sim 1/1836\) of the proton’s, its *speed* for the same momentum is **much larger**, while the magnetic force (which is proportional to \(v\)) is also larger. The net result is a larger acceleration, but the radius remains \(r = p/(|q|B)\). The increase in acceleration is exactly compensated by the increase in speed, leaving the curvature radius unchanged.

### 2.6. Relativistic extension (optional)

If the particles are moving fast enough that relativistic effects matter, replace the classical momentum \(p=m v\) by the relativistic momentum  

\[
p = \gamma m v,\qquad \gamma = \frac{1}{\sqrt{1-(v/c)^{2}}}.
\]

The magnetic force equation is still \(q v B = \gamma m v^{2}/r\) (the relativistic mass \(\gamma m\) appears in the centripetal term). Solving gives the same compact result

\[
r = \frac{p}{|q|B},
\]

so the conclusion **does not change**: equal momenta ⇒ equal radii, regardless of relativistic speeds.

---

## 3. Final answer  

> **If an electron and a proton enter the same uniform magnetic field with the same magnitude of momentum, they will travel in circular arcs of **identical radius**.**  
> The radius is given by  
> \[
> r = \frac{p}{e B},
> \]  
> where \(p\) is the common momentum, \(e\) the elementary charge, and \(B\) the magnetic‑field magnitude.  
> The electron curves in the opposite sense because its charge is negative, but the size of the circle is the same.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using \(r = mv/qB\) and plugging in the *mass* instead of the *momentum*** | The formula already contains the product \(mv\) (the momentum). Substituting the mass alone ignores the velocity factor. | Write the expression as \(r = (mv)/qB = p/qB\) before inserting numbers. |
| **Thinking a larger acceleration must mean a smaller radius** | Acceleration \(a = v^{2}/r\) and magnetic force \(F = qvB\) both depend on the particle’s speed. For fixed momentum, a lighter particle moves faster, giving a larger \(a\) but also a larger \(v\); the ratio \(v^{2}/a\) (which is \(r\)) stays the same. | Derive \(r\) from force balance; do not compare \(a\) alone. |
| **Ignoring the sign of the charge** | The sign determines the *direction* of curvature, not the magnitude of the radius. | Keep track of \(|q|\) when calculating radius; use the sign only to state the sense of rotation. |
| **Assuming non‑relativistic formulas fail at high speeds** | The relation \(r = p/qB\) is **exact** even relativistically, because \(p\) already includes the Lorentz factor \(\gamma\). | If speeds approach \(c\), compute \(p\) relativistically, then use the same radius formula. |
| **Equating kinetic energy \(K = \frac{1}{2}mv^{2}\) to magnetic energy** | Magnetic fields do no work; the particle’s kinetic energy does not change while it is in the field. | Remember that only the direction of velocity changes, not its magnitude. |

---

*Original question: [Deflection Radii of an Electron and Proton in Magnetic Field](https://physics.stackexchange.com/questions/875779/deflection-radii-of-an-electron-and-proton-in-magnetic-field) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
