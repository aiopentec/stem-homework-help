---
layout: question
title: Condition to fall into 1/r^2 potential
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Condition to fall into 1/r^2 potential'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the problem is asking (in plain language)

A particle of mass \(m\) comes from very far away (effectively from infinity) with a speed \(v_{\infty}\) and a lateral offset (impact parameter) \(b\) with respect to the centre of an attractive potential  

\[
V(r)= -\frac{k}{r^{2}},\qquad k>0 .
\]

Because the particle also carries angular momentum, the centrifugal “push’’ can prevent it from reaching the origin.  
If the impact parameter is **small enough**, the attraction wins and the particle “falls’’ all the way to \(r=0\).

**Question:**  
What is the largest (critical) impact parameter \(b_{\max}\) for which the particle still falls to the centre? How do we obtain it?

---

## 2. Step‑by‑step derivation  

### 2.1. Conserved quantities

* **Energy** (mechanical, because the potential is time‑independent)

\[
E = \frac12 m \dot r^{2}+ \frac{L^{2}}{2mr^{2}} + V(r) .
\]

* **Angular momentum** about the origin (central force → conserved)

\[
L = m r^{2}\dot\theta = \text{constant}.
\]

For a particle that starts at infinity with speed \(v_{\infty}\) and impact parameter \(b\),

\[
L = m v_{\infty} b .
\]

The total mechanical energy far away is simply kinetic, because the potential vanishes as \(r\to\infty\):

\[
E = \frac12 m v_{\infty}^{2}>0 .
\]

---

### 2.2. The effective radial potential  

Group the terms that depend only on \(r\) into an *effective potential*:

\[
V_{\text{eff}}(r)=\frac{L^{2}}{2m r^{2}}+V(r)
                =\frac{L^{2}}{2m r^{2}}-\frac{k}{r^{2}}
                =\frac{1}{r^{2}}\Bigl(\frac{L^{2}}{2m}-k\Bigr).
\]

Thus the radial equation of motion becomes

\[
\frac12 m\dot r^{2}+V_{\text{eff}}(r)=E .
\]

---

### 2.3. When can the particle reach \(r=0\)?

The particle can get arbitrarily close to the origin **iff** the effective potential never rises above the total energy.  
Because \(V_{\text{eff}}\propto 1/r^{2}\), its sign is determined by the coefficient

\[
C \equiv \frac{L^{2}}{2m}-k .
\]

* If \(C>0\) then \(V_{\text{eff}}(r)>0\) for all \(r\); the particle feels a repulsive centrifugal barrier and will have a finite closest approach \(r_{\min}>0\).

* If \(C\le 0\) then \(V_{\text{eff}}(r)\le 0\) and becomes arbitrarily large in magnitude (negative) as \(r\to0\).  
  The radial kinetic term \(\frac12 m\dot r^{2}=E-V_{\text{eff}}(r)\) stays positive for every \(r\), so the particle can keep falling to \(r=0\).

Hence **the capture condition is**

\[
\boxed{\; \frac{L^{2}}{2m}\le k\; } .
\]

---

### 2.4. Translate the condition to the impact parameter  

Insert \(L=m v_{\infty} b\):

\[
\frac{(m v_{\infty} b)^{2}}{2m}\le k
\;\Longrightarrow\;
\frac{m v_{\infty}^{2} b^{2}}{2}\le k .
\]

Solve for \(b\):

\[
b^{2}\le \frac{2k}{m v_{\infty}^{2}}
\qquad\Longrightarrow\qquad
b\le b_{\max}= \sqrt{\frac{2k}{m v_{\infty}^{2}}}.
\]

---

### 2.5. Special case of the statement “potential \(-1/r^{2}\)”

If the problem’s constant is hidden (i.e. the potential is written as \(V(r)=-1/r^{2}\)), then \(k=1\) (in whatever system of units is being used). The critical impact parameter becomes

\[
\boxed{\,b_{\max}= \sqrt{\frac{2}{m v_{\infty}^{2}}}\,}.
\]

If the constant \(k\) is kept explicitly, use the formula with \(k\).

---

## 3. Final answer  

For a particle of mass \(m\) arriving from infinity with speed \(v_{\infty}\) in the attractive inverse‑square potential  

\[
V(r)=-\frac{k}{r^{2}},\qquad k>0,
\]

the largest impact parameter that still leads to a “fall to the centre’’ is  

\[
\boxed{b_{\max}= \sqrt{\frac{2k}{m\,v_{\infty}^{2}}}} .
\]

If the potential is written as \(V(r)=-1/r^{2}\) (i.e. \(k=1\)), this reduces to  

\[
b_{\max}= \sqrt{\frac{2}{m\,v_{\infty}^{2}}}.
\]

Impact parameters larger than \(b_{\max}\) give a finite periapsis distance; the particle never reaches the origin.

---

## 4. Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to fix it |
|---------|----------------|---------------|
| **Forgetting the centrifugal term** and using only \(V(r)\) in the energy equation. | The angular momentum creates an effective repulsive \(L^{2}/(2mr^{2})\) that is essential for the capture condition. | Write the full effective potential \(V_{\text{eff}} = L^{2}/(2mr^{2}) + V(r)\) before analyzing the motion. |
| **Using \(L = m v_{\infty} b\) incorrectly (e.g., missing a factor of \(v_{\infty}\) or using \(b\) instead of \(b^{2}\)).** | The relation follows from \(\mathbf{L}= \mathbf{r}\times m\mathbf{v}\); a missing factor changes the final expression for \(b_{\max}\). | Remember that at infinity the velocity is essentially perpendicular to the radius vector, so \(L = m v_{\infty} b\). |
| **Mixing up signs** (thinking the effective potential is always repulsive). | The attractive \(-k/r^{2}\) can outweigh the centrifugal term, making \(V_{\text{eff}}\) negative. | Keep the sign of each term clear: \(+L^{2}/(2mr^{2})\) (repulsive) and \(-k/r^{2}\) (attractive). |
| **Assuming the particle must have zero total energy to fall.** | The total energy is positive (kinetic at infinity). Capture occurs because the *radial* kinetic energy never vanishes, not because \(E=0\). | Use the inequality \(L^{2}/(2m)\le k\); the value of \(E\) (positive) does not appear in the critical condition. |
| **Neglecting that the condition is *≤* not *<*.** | The borderline case \(L^{2}=2mk\) still leads to a fall (the particle reaches the centre with constant radial speed). | State the capture condition as \(L^{2}\le 2mk\) or equivalently \(b\le b_{\max}\). |

Keeping these points in mind will give the correct critical impact parameter for any inverse‑square attractive potential.

*Original question: [Condition to fall into 1/r^2 potential](https://physics.stackexchange.com/questions/876447/condition-to-fall-into-1-r2-potential) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
