---
layout: question
title: Higher order terms of $\operatorname{grad}$ on a perturbed Morse flowline
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Higher order terms of $\operatorname{grad}$
  on a perturbed Morse flowline'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We have a *Morse gradient flow* on a Riemannian manifold \((M,g)\)

\[
\frac{d u}{ds}+ \operatorname{grad} f(u)=0 ,
\qquad L:=\frac{d}{ds}+ \operatorname{grad} f .
\]

A **pre‑glued** trajectory is written as  

\[
u(s)=\beta_{-}(s)\bigl(u_{-}(s)+\psi_{-}(s)\bigr)
        +\beta_{0}(s)\bigl(u_{0}(s)+\psi_{0}(s)\bigr)
        +\beta_{+}(s)\bigl(u_{+}(s)+\psi_{+}(s)\bigr),
\]

where  

* the three “building blocks’’ \(u_{\star}\) are *exact* gradient flow lines,  
* \(\psi_{\star}\) are small perturbations (sections of \(u_{\star}^{*}TM\)) that lie in the \(L^{2}_{1}\)–orthogonal complement of \(\ker D_{u_{\star}}\),  
* \(\beta_{\star}\) are smooth cut–off functions that add up to \(1\).

When we apply the operator \(L\) to \(u\) we obtain

\[
L(u)=\beta_{+}\Theta_{+}(\psi_{+},\psi_{0})
     +\beta_{0}\Theta_{0}(\psi_{+},\psi_{0},\psi_{-})
     +\beta_{-}\Theta_{-}(\psi_{0},\psi_{-}),
\]

and each \(\Theta_{\star}\) contains a *linear* part (the linearisation \(D_{u_{\star}}\psi_{\star}\) and the derivative of the cut‑offs) **plus** a remainder \(H(\psi_{\star})\).  

The question is:

> **What exactly is the “higher–order term’’ \(H(\psi_{\star})\) that comes from expanding \(\operatorname{grad} f(u_{\star}+\psi_{\star})\) beyond the linear term?**  

We have to write down the Taylor expansion of the vector field \(\operatorname{grad} f\) in a covariant way, keep all quadratic (and higher) contributions, and identify them with the symbol \(H(\psi_{\star})\).

---

## 2.  Full derivation (no steps omitted)

### 2.1  Linearisation of the gradient flow equation

Fix a smooth flow line \(u\colon\mathbb R\to M\) satisfying  

\[
\partial_s u + \operatorname{grad} f(u)=0 .
\tag{2.1}
\]

Let \(\psi\in\Gamma(u^{*}TM)\) be a section (the perturbation).  
Write a *perturbed* curve using the exponential map:

\[
\widetilde u(s)=\exp_{u(s)}\bigl(\psi(s)\bigr).
\tag{2.2}
\]

The gradient flow equation for \(\widetilde u\) reads  

\[
\partial_s\widetilde u + \operatorname{grad}f(\widetilde u)=0 .
\tag{2.3}
\]

We expand the left‑hand side in powers of \(\psi\).  
Recall two standard formulas for the exponential map (see e.g. Klingenberg, *Riemannian Geometry*):

* For a vector field \(X\) along \(u\),

\[
\frac{D}{ds}\exp_{u}\bigl(X\bigr) 
   = \bigl( D_{u}X \bigr) + O(|X|^{2}),
\tag{2.4}
\]

where \(D_{u}X:=\nabla_{\partial_s}X+\nabla_{X}\operatorname{grad}f(u)\) is the **linearisation** of the gradient flow operator.

* For any smooth vector field \(Y\) on \(M\),

\[
Y\bigl(\exp_{u}(X)\bigr)
   = Y(u) + \nabla_{X}Y(u) 
     + \frac12 \nabla^{2}_{X,X}Y(u) + O(|X|^{3}).
\tag{2.5}
\]

In (2.5) we use the **covariant Taylor expansion**: \(\nabla_{X}Y\) is the directional derivative of the vector field \(Y\) along the vector \(X\); \(\nabla^{2}_{X,X}Y\) is the second covariant derivative, i.e.  

\[
\nabla^{2}_{X,X}Y
   := \nabla_{X}\bigl(\nabla_{X}Y\bigr)-\nabla_{\nabla_{X}X}Y .
\]

Apply (2.5) with \(Y=\operatorname{grad}f\) and \(X=\psi(s)\). Because \(\operatorname{grad}f\) is a vector field, we obtain

\[
\operatorname{grad}f\bigl(\exp_{u}\psi\bigr)
   = \operatorname{grad}f(u) 
     + \nabla_{\psi}\operatorname{grad}f(u) 
     + \frac12 \nabla^{2}_{\psi,\psi}\operatorname{grad}f(u)
     + O(|\psi|^{3}).
\tag{2.6}
\]

Now substitute (2.4) and (2.6) into (2.3):

\[
\begin{aligned}
0
&= \partial_s\bigl(\exp_{u}\psi\bigr)
   + \operatorname{grad}f\bigl(\exp_{u}\psi\bigr) \\[4pt]
&= \underbrace{\bigl(\partial_s\psi + \nabla_{\psi}\operatorname{grad}f(u)\bigr)}_{\displaystyle D_{u}\psi}
   \;+\;
   \underbrace{\frac{d\beta}{ds}\,u}_{\text{cut‑off term (if any)}}
   \;+\;
   \underbrace{\frac12 \nabla^{2}_{\psi,\psi}\operatorname{grad}f(u)}_{\displaystyle H(\psi)}
   \;+\; O(|\psi|^{3}) .
\end{aligned}
\tag{2.7}
\]

The first bracket is exactly the **linearised operator**

\[
D_{u}\psi := \partial_s\psi + \nabla_{\psi}\operatorname{grad}f(u) .
\tag{2.8}
\]

All remaining terms are *quadratic or higher* in \(\psi\).  
Hence we *define* the higher‑order remainder by

\[
\boxed{
   H(\psi)\;:=\;
   \frac12 \,\nabla^{2}_{\psi,\psi}\operatorname{grad}f\bigl(u\bigr)
   \;+\; O\bigl(|\psi|^{3}\bigr) .
}
\tag{2.9}
\]

Because we work in a *Euclidean chart* around each critical point (the paper assumes a flat metric in a \(2\epsilon\)-ball), the curvature terms that would appear in the full covariant expression disappear, and the above formula reduces to the ordinary Euclidean Taylor expansion.

---

### 2.2  Explicit coordinate form (for the reader’s intuition)

Pick normal coordinates \((x^{1},\dots,x^{n})\) centred at a critical point \(p\).  
In these coordinates the Levi‑Civita connection vanishes at the centre, and the metric is the identity matrix up to \(O(|x|^{2})\).  

Write \(\psi = (\psi^{1},\dots,\psi^{n})\) and \(\operatorname{grad}f = (\partial_{1}f,\dots,\partial_{n}f)\).  
Then

\[
\begin{aligned}
\bigl(\operatorname{grad}f\bigr)^{i}\bigl(u+\psi\bigr)
&= \partial_{i}f(u) 
   + \sum_{j}\partial_{j}\partial_{i}f(u)\,\psi^{j}
   + \frac12\sum_{j,k}\partial_{j}\partial_{k}\partial_{i}f(u)\,
        \psi^{j}\psi^{k}
   + O(|\psi|^{3}) .
\end{aligned}
\]

The first two terms give \(\operatorname{grad}f(u)+\nabla_{\psi}\operatorname{grad}f(u)\).  
The quadratic part is exactly  

\[
\bigl(H(\psi)\bigr)^{i}
   = \frac12\sum_{j,k}
        \partial_{j}\partial_{k}\partial_{i}f(u)\,
        \psi^{j}\psi^{k}
   \;+\; O(|\psi|^{3}) .
\tag{2.10}
\]

Thus, in Euclidean coordinates the abstract covariant expression (2.9) becomes the familiar third‑order partial‑derivative term of the Taylor series.

---

### 2.3  Plugging the expansion into the three pieces \(\Theta_{\pm},\Theta_{0}\)

Recall the definitions from the question:

\[
\begin{aligned}
\Theta_{+}(\psi_{+},\psi_{0})
   &= D_{u_{+}}\psi_{+}
      + \frac{d\beta_{0}}{ds}\,(u_{0}+\psi_{0})
      + H(\psi_{+}),\\[4pt]
\Theta_{0}(\psi_{+},\psi_{0},\psi_{-})
   &= D_{u_{0}}\psi_{0}
      + \frac{d\beta_{+}}{ds}\,\exp_{u_{+}}(\psi_{+})
      + \frac{d\beta_{-}}{ds}\,\exp_{u_{-}}(\psi_{-})
      + H(\psi_{0}),\\[4pt]
\Theta_{-}(\psi_{0},\psi_{-})
   &= D_{u_{-}}\psi_{-}
      + \frac{d\beta_{0}}{ds}\,(u_{0}+\psi_{0})
      + H(\psi_{-}) .
\end{aligned}
\]

The **only place** where the higher–order term appears is the `\(H(\psi_{\star})\)` written above.  
Because each \(u_{\star}\) already satisfies the unperturbed flow equation, the linear part \(\partial_{s}u_{\star}+ \operatorname{grad}f(u_{\star})\) vanishes, leaving the three displayed terms as the complete expansion.

Thus the **expanded version of \(H\)** is precisely

\[
\boxed{
   H(\psi_{\star})(s)
   \;=\;
   \frac12\,\nabla^{2}_{\psi_{\star}(s),\,\psi_{\star}(s)}\!\bigl(\operatorname{grad}f\bigr)
   \bigl(u_{\star}(s)\bigr)
   \;+\; O\!\bigl(\|\psi_{\star}(s)\|^{3}\bigr) .
}
\tag{2.11}
\]

If one wishes to keep the cubic and higher terms explicitly, write

\[
H(\psi_{\star})
   =\sum_{k\ge 2}
      \frac{1}{k!}
      \nabla^{k}_{\underbrace{\psi_{\star},\dots,\psi_{\star}}_{k}}
        \bigl(\operatorname{grad}f\bigr)(u_{\star}) .
\tag{2.12}
\]

In the *flat* chart the covariant derivatives become ordinary partial derivatives, so (2.12) is exactly the usual multivariate Taylor series of the

*Original question: [Higher order terms of $\operatorname{grad}$ on a perturbed Morse flowline](https://math.stackexchange.com/questions/5149499/higher-order-terms-of-operatornamegrad-on-a-perturbed-morse-flowline) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
