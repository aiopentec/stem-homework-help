---
layout: question
title: Formal mapping between infinite branch cuts and finite singularities in improper
  evaluations
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Formal mapping between infinite branch
  cuts and finite singularities in improper evaluations'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The student has three intertwined ideas:

1. **Integral in the real line**  
   \[
   I=\int_{1}^{\infty}\frac{1}{x\sqrt{x^{2}-1}}\;dx .
   \]

2. **A change of variable that “inverts’’ the whole problem**  
   \[
   x=\frac{1}{u}\qquad (u\in(0,1])\;,
   \]
   which turns the infinite upper limit into a finite one and gives  
   \[
   I=\int_{0}^{1}\frac{1}{\sqrt{1-u^{2}}}\;du .
   \]

3. **A complex‑analytic way of evaluating the same integral** by using an antiderivative that involves a complex logarithm,
   \[
   F(x)=-i\ln\!\Bigl(\frac1x+i\sqrt{1-\frac{1}{x^{2}}}\Bigr),
   \]
   and then letting \(x\to\infty\) to obtain \(F(\infty)-F(1)=\pi/2\).

The student wants to know:

* Does the inversion \(x=1/u\) **prove** that the “infinite branch cut’’ (the cut that we normally place on the complex plane from \(-\infty\) to \(-1\) and from \(1\) to \(+\infty\) for the function \(\sqrt{x^{2}-1}\)) is **topologically the same** as the “finite singularity’’ we see after the change of variable?

* Is there a known theorem in complex geometry that states, in precise terms, that this mapping collapses the two different topologies into one and that the logarithmic limit is therefore legitimate?

Below we answer both parts by working out the integral, explaining the effect of the inversion on the Riemann surface of \(\sqrt{z^{2}-1}\), and quoting the relevant theorems.

---

## 2.  Detailed solution  

### 2.1  Direct evaluation of the real integral  

Write the integrand as a derivative of an elementary function.  For \(x>1\) we have  

\[
\frac{d}{dx}\,\operatorname{arcosh}x=\frac{1}{\sqrt{x^{2}-1}}\;,
\qquad
\frac{d}{dx}\,\ln\!\bigl(x+\sqrt{x^{2}-1}\bigr)=\frac{1}{\sqrt{x^{2}-1}} .
\]

Multiplying by \(1/x\) we obtain  

\[
\frac{1}{x\sqrt{x^{2}-1}}=\frac{d}{dx}\Bigl[-i\ln\!\Bigl(\frac{1}{x}+i\sqrt{1-\frac{1}{x^{2}}}\Bigr)\Bigr] .
\]

Hence an antiderivative is  

\[
F(x)=-i\ln\!\Bigl(\frac{1}{x}+i\sqrt{1-\frac{1}{x^{2}}}\Bigr),
\qquad x>1 .
\]

Now evaluate the limits:

* At the lower endpoint \(x=1\) we have \(\sqrt{1-1/x^{2}}=0\) and \(\frac1x=1\).  
  Using the principal branch of the logarithm (\(\ln 1=0\)) we get  
  \[
  F(1)=-i\ln(1)=0 .
  \]

* As \(x\to\infty\) we expand the argument of the logarithm:
  \[
  \frac1x+i\sqrt{1-\frac1{x^{2}}}
  =\frac1x+i\Bigl(1-\frac{1}{2x^{2}}+O\!\bigl(\frac1{x^{4}}\bigr)\Bigr)
  =i\Bigl(1+\frac{1}{ix}+O\!\bigl(\frac1{x^{2}}\bigr)\Bigr).
  \]
  The logarithm of a number that tends to \(i\) is \(\ln i = i\pi/2\) (principal branch). Thus
  \[
  \lim_{x\to\infty}F(x)=-i\bigl(i\pi/2\bigr)=\frac{\pi}{2}.
  \]

Therefore  

\[
\boxed{I=\int_{1}^{\infty}\frac{dx}{x\sqrt{x^{2}-1}}=
\frac{\pi}{2}} .
\]

---

### 2.2  Change of variable \(x=1/u\)  

Set \(x=\dfrac1u\).  Then \(dx=-\dfrac{du}{u^{2}}\) and  

\[
\frac{1}{x\sqrt{x^{2}-1}}dx=
\frac{1}{(1/u)\sqrt{1/u^{2}-1}}\Bigl(-\frac{du}{u^{2}}\Bigr)
=
\frac{1}{\sqrt{1-u^{2}}}\,du .
\]

When \(x\) runs from \(1\) to \(+\infty\), the new variable runs from \(u=1\) down to \(u=0\).  Flipping the limits removes the minus sign:

\[
I=\int_{0}^{1}\frac{du}{\sqrt{1-u^{2}}}.
\]

This is the standard integral that defines the arcsine function:

\[
\int_{0}^{1}\frac{du}{\sqrt{1-u^{2}}}= \bigl[\arcsin u\bigr]_{0}^{1}
= \frac{\pi}{2}.
\]

So the change of variable gives the same value, and **no hidden branch cut appears** because the function \(\sqrt{1-u^{2}}\) is analytic on the interval \([0,1]\) when we take the principal branch (its cut is on \((-\infty,-1]\cup[1,\infty)\), which does not intersect \([0,1]\)).

---

### 2.3  What happens to the branch cut under the inversion  

The multivalued function  

\[
w(z)=\sqrt{z^{2}-1}
\]

has two branch points at \(z=\pm1\).  The customary choice of a *principal* branch places a cut along the real axis from \(-\infty\) to \(-1\) and from \(1\) to \(+\infty\).  

Consider the Möbius (projective) transformation  

\[
\phi:\widehat{\mathbb C}\longrightarrow\widehat{\mathbb C},\qquad 
\phi(z)=\frac1z .
\]

* \(\phi\) is a **biholomorphism** (conformal map) of the Riemann sphere \(\widehat{\mathbb C}=\mathbb C\cup\{\infty\}\); it sends the point at infinity to \(0\) and vice‑versa.
* Being a homeomorphism, \(\phi\) carries any *topological* feature (e.g., a cut, a loop, an orientation) to a homeomorphic image.

Apply \(\phi\) to the branch cut of \(w(z)\).  The two half‑lines \((-\infty,-1]\) and \([1,\infty)\) are mapped to the intervals  

\[
\phi\bigl((-\infty,-1]\bigr)=[-1,0),\qquad 
\phi\bigl([1,\infty)\bigr)=(0,1] .
\]

Thus **the infinite cut becomes a finite interval that runs from \(-1\) to \(0\) and from \(0\) to \(1\)**.  In the new variable \(u\) the function becomes  

\[
\sqrt{\frac{1}{u^{2}}-1}= \frac{1}{u}\sqrt{1-u^{2}},
\]
so the factor \(1/u\) exactly cancels the Jacobian \(-du/u^{2}\) that appears in the integral, leaving the simple integrand \(1/\sqrt{1-u^{2}}\).

Consequently, the *Riemann surface* of the original integrand (a two‑sheeted cover of the sphere branched at \(\pm1\) and at \(\infty\)) is mapped by \(\phi\) to a **homeomorphic** Riemann surface that is branched only at the three finite points \(-1,0,1\).  Topologically the two surfaces are the same; the only difference is the location of the branch points.

---

### 2.4  Formal theorems that guarantee the above reasoning  

| Theorem | Statement (relevant part) | How it is used here |
|---------|---------------------------|---------------------|
| **Möbius (projective) transformation theorem** | Every Möbius map \(\displaystyle z\mapsto \frac{az+b}{cz+d}\) with \(ad-bc\neq0\) extends to a biholomorphic homeomorphism of the Riemann sphere \(\widehat{\mathbb C}\). | The inversion \(x\mapsto 1/x\) is a Möbius map; therefore it preserves the topology of any curve or cut on the sphere. |
| **Branch‑cut pull‑back lemma** | If \(f\) is a multivalued analytic function defined on a domain \(D\subset\widehat{\mathbb C}\) with a chosen branch cut \(\Gamma\subset D\), and \(\phi:D'\to D\) is a biholomorphism, then \(f\circ\phi\) has a branch cut \(\phi^{-1}(\Gamma)\) and the two Riemann surfaces are biholomorphically equivalent. | Pulling back the cut of \(\sqrt{z^{2}-1}\) by \(\phi(z)=1/z\) yields the finite cut \([-1,0]\cup[0,1]\). |
| **Change‑of‑variables theorem for contour integrals** | If \(\gamma\) is a piecewise‑smooth curve in the domain of a holomorphic map \(\phi\) and \(g\) is holomorphic on \(\phi(\gamma)\), then \(\displaystyle\int_{\gamma} g(\phi(z))\,\phi'(z)\,dz =\int_{\phi\circ\gamma} g(w)\,dw\). | The substitution \(x=1/u\) is precisely this theorem; it guarantees that the value of the integral is unchanged. |
| **Fundamental theorem of calculus for complex antiderivatives** | If \(F'\!(z)=f(z)\) on a simply connected domain avoiding branch points, then \(\displaystyle\int_{\gamma}f(z)dz =F(\gamma(b))-F(\gamma(a))\) for any path \(\gamma\). | The antiderivative \(F(z)=-i\ln\!\bigl(\frac1z+i\sqrt{1-\frac{1}{z^{2}}}\bigr)\) is defined on the cut plane; the integral from \(1\) to \(\infty\) is the difference of the limits of \(F\). |

Taken together, these results **prove rigorously** that:

1. The inversion \(x=1/u\) maps the “infinite branch cut’’ of \(\sqrt{x^{2}-1}\) to a finite cut that does **not** intersect the interval of integration \([0,1]\).  
2. The integral’s value is preserved, and the limit \(\displaystyle\lim_{x\to\infty}F(x)=\pi/2\) is legitimate because \(F\) is an analytic continuation of the antiderivative on the whole (cut) sphere.

Thus the two viewpoints—*an improper integral with a cut extending to infinity* and *a proper integral over a finite interval*—are **topologically identical**; the only change is a relabeling of the point at infinity as the origin via a Möbius transformation.

---

## 3.  Final answer  

*Yes.* The projective inversion \(x=1/u\) is a Möbius transformation that gives a **homeomorphism of the Riemann sphere**. It carries the infinite branch cut of \(\sqrt{x^{2}-1}\) to a finite cut that lies entirely outside the interval \([0,1]\) used after the substitution. Consequently the integral over \([1,\

*Original question: [Formal mapping between infinite branch cuts and finite singularities in improper evaluations](https://math.stackexchange.com/questions/5151232/formal-mapping-between-infinite-branch-cuts-and-finite-singularities-in-improper) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
