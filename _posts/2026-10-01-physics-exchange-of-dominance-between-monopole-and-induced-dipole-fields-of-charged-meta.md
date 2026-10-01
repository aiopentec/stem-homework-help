---
layout: question
title: Exchange of dominance between monopole and induced dipole fields of charged
  metal sphere
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Exchange of dominance between monopole
  and induced dipole fields of charged metal sphere'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the problem is asking  

We have two almost identical arrangements of charges  

* **Diagram (b)** – three *point* charges: two identical charges +q placed symmetrically about point **R**, and a third charge +2q a little farther away (the “top‑right” charge).  

* **Diagram (c)** – the two +q charges are unchanged, but the +2q point charge is replaced by a *conducting sphere* that carries the same total charge +2q.  

Point **R** is exactly halfway between the two +q charges, so the electric field produced by those two charges cancels at R.  

The question: **Is the magnitude of the electric field at R larger, smaller, or the same when the +2q point charge is replaced by the charged conducting sphere?**  

---

## 2. Step‑by‑step solution  

### Step 1 – Write the field at R for diagram (b)  

Because the two +q charges are equal and opposite in position with respect to R, their contributions cancel:

\[
\mathbf E_{+q}^{(\text{left})}(R)+\mathbf E_{+q}^{(\text{right})}(R)=\mathbf 0 .
\]

Therefore the only contribution is the field of the single point charge +2q.  
If the distance from that charge to R is \(r\),

\[
\boxed{E_{(b)} = \frac{k\,2q}{r^{2}}}\qquad\text{(directed away from the +2q charge)} .
\]

\(k=1/4\pi\varepsilon_{0}\) is Coulomb’s constant.

---

### Step 2 – What changes when the point charge becomes a conducting sphere?  

A conducting sphere with total charge +2q still produces the *same* monopole (overall) field as a point charge **as long as we look at points outside the sphere**.  
Mathematically, for any point whose distance from the centre of the sphere is \(R_{\text{out}} > a\) (where \(a\) is the sphere radius),

\[
\mathbf E_{\text{monopole}}(R_{\text{out}})=\frac{k\,2q}{R_{\text{out}}^{2}}\;\hat{\mathbf r},
\]

exactly the same expression we used in diagram (b).

However, the **external +q charges polarise the sphere**. Positive charge is repelled to the side opposite the +q’s, leaving a relative deficit of positive charge on the near side. The resulting charge distribution can be represented (to first order) by a **dipole moment** \(\mathbf p\) that points **away from the two +q charges**.

Consequences:

* The monopole term still points away from the sphere’s centre (same direction as in (b)).
* The dipole term produces an additional field that, at the location of R, points **toward** the sphere (i.e. opposite to the monopole field).  

Hence the two contributions partially cancel.

---

### Step 3 – Write the field at R for diagram (c) (outside‑sphere approximation)

For points outside a uniformly charged sphere the field can be expanded in a multipole series. Keeping only the monopole and dipole terms (the next terms are \(\propto 1/R^{4}\) and are much smaller) gives

\[
\mathbf E_{(c)}(R)=
\underbrace{\frac{k\,2q}{r^{2}}}_{\text{monopole}}
\; \hat{\mathbf r}
\;+\;
\underbrace{\frac{1}{4\pi\varepsilon_{0}}\,
\frac{3(\mathbf p\!\cdot\!\hat{\mathbf r})\hat{\mathbf r}-\mathbf p}{r^{3}}}_{\text{dipole}} .
\]

Because the induced dipole \(\mathbf p\) points *away* from the two +q charges, the scalar product \(\mathbf p\!\cdot\!\hat{\mathbf r}\) is **negative** at point R. The dipole term therefore points **opposite** to \(\hat{\mathbf r}\) and reduces the magnitude of the total field.

In symbols, let the dipole contribution at R be \(-\,\Delta E\) with \(\Delta E>0\). Then

\[
E_{(c)} = \frac{k\,2q}{r^{2}} - \Delta E .
\]

Since \(\Delta E\) is non‑zero (the external +q’s certainly polarise the sphere), we have

\[
\boxed{E_{(c)} \;<\; E_{(b)} } .
\]

---

### Step 4 – Physical interpretation (intro‑physics language)  

* The two +q charges try to push the sphere’s positive charge to the far side.  
* Because some of the +2q charge is now **farther** from point R than before, the net repulsive field that reaches R is weaker.  
* The effect is exactly the same as saying: “the sphere looks like a point charge +2q **plus** a little dipole that pulls the field back toward the sphere.”

Thus the magnitude of the electric field at R is **smaller** when the point charge is replaced by a conducting sphere carrying the same total charge.

---

## 3. Final answer  

\[
\boxed{\displaystyle
\left| \mathbf E_{\text{(c)}}(R) \right|
\; < \;
\left| \mathbf E_{\text{(b)}}(R) \right|
}
\]

The field at R in the configuration with the conducting sphere is weaker than the field in the configuration with the isolated +2q point charge.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the sphere’s charge stays uniformly spread** | Conductors redistribute charge in response to external fields; the +q charges will polarise the sphere. | Remember that a conductor’s surface charge is *not* fixed when other charges are nearby. |
| **Treating the sphere as a point charge *and* ignoring induced dipole** | The monopole term is correct, but the dipole term (first‑order correction) changes the field direction at R, making it smaller. | Use the multipole idea: “point‑charge field + correction due to induced dipole.” |
| **Thinking the fields from the two +q’s do not cancel** | Because R is exactly halfway between them, the horizontal components cancel perfectly; only the vertical components (which are zero by symmetry) could remain. | Write the vector expression for the two +q fields and show they sum to zero. |
| **Confusing “farther away” with “larger distance from the centre”** | The relevant distance is the *effective* distance of the charge that actually contributes to the field at R. Polarisation moves charge to the far side, increasing that effective distance. | Visualise the induced charge as a little “cloud” shifted away from R. |
| **Using the image‑charge method without justification** | Introductory students may not know the image‑charge technique, leading to an over‑complicated answer. | Stay with the qualitative monopole‑plus‑dipole picture; a quantitative image‑charge calculation is not required. |

Keeping these points in mind will help students answer the question correctly using only the tools typically taught in a second‑semester introductory physics course.

*Original question: [Exchange of dominance between monopole and induced dipole fields of charged metal sphere](https://physics.stackexchange.com/questions/876495/exchange-of-dominance-between-monopole-and-induced-dipole-fields-of-charged-meta) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
