---
layout: question
title: Which limits and colimits are preserved by the inclusion of locally constant
  sheaves into all sheaves?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Which limits and colimits are preserved
  by the inclusion of locally constant sheaves into all sheaves?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We have two categories that live over a fixed topological space \(X\).

* \(\mathbf{Shv}(X)=\) sheaves of sets on \(X\).
* \(\mathbf{LocConst}(X)=\) **locally constant** sheaves, i.e. those that look locally like a constant sheaf.

The inclusion  

\[
i:\mathbf{LocConst}(X)\hookrightarrow \mathbf{Shv}(X)
\]

is fully faithful.  
The question is:

* Which limits (products, pull‑backs, equalizers, …) does the functor \(i\) preserve?
* Which colimits (coproducts, push‑outs, coequalizers, …) does it preserve?
* Does \(i\) have a left adjoint? a right adjoint?

In other words, we want to know how the sub‑category of locally constant sheaves sits inside the whole category of sheaves from the point of view of universal constructions.

--------------------------------------------------------------------

## 2.  Preliminary facts

### 2.1  Étale spaces  

Every sheaf \(\mathcal F\) on \(X\) has an associated **étale space**  

\[
\pi_{\mathcal F}\colon E(\mathcal F)\longrightarrow X,
\]

and this gives an equivalence  

\[
\mathbf{Shv}(X)\;\simeq\;\mathbf{Ét}(X)
\]

between sheaves and local homeomorphisms (étale spaces).  

A sheaf is locally constant iff its étale space is a **covering space**, i.e. a local homeomorphism that is *locally a product*  

\[
\pi^{-1}(U)\cong I\times U .
\]

Thus  

\[
\mathbf{LocConst}(X)\;\simeq\;\mathbf{Cov}(X)
\]

and the inclusion \(i\) corresponds to the inclusion  

\[
\mathbf{Cov}(X)\hookrightarrow\mathbf{Ét}(X) .
\]

From now on we work with covering spaces and étale spaces, because the statements about limits/colimits are easier to see there.

### 2.2  How limits and colimits are computed  

* In \(\mathbf{Shv}(X)\) (hence also in \(\mathbf{Ét}(X)\)) **limits are computed pointwise**: the stalk at \(x\) of a limit is the limit of the stalks.
* **Colimits are also computed stalkwise** after sheafifying the presheaf‑colimit. For a diagram of étale spaces the underlying set‑colimit is taken fibrewise and then the resulting map \(Y\to X\) is equipped with the unique topology that makes it étale.

Consequently, a property of a sheaf that can be read on the stalks and that is preserved under the relevant set‑theoretic construction will be preserved under the corresponding categorical construction.

--------------------------------------------------------------------

## 3.  Limits preserved by the inclusion

### 3.1  Description of a locally constant sheaf in terms of stalks  

Let \(X\) be any space and let \(\pi_{0}(X)\) be the set of its (path)‑connected components.  
A sheaf \(\mathcal L\) is locally constant iff for each component \(C\subseteq X\) there exists a set \(I_{C}\) such that for every point \(x\in C\)

\[
\mathcal L_{x}\cong I_{C}.
\]

Thus a locally constant sheaf is *constant on each component*.

### 3.2  Limits are pointwise  

Take a diagram \(\{ \mathcal L_{j}\}_{j\in J}\) of locally constant sheaves and form its limit \(\mathcal L=\varprojlim_{j}\mathcal L_{j}\) in \(\mathbf{Shv}(X)\).  
For a point \(x\in X\),

\[
\mathcal L_{x}= \varprojlim_{j}\,(\mathcal L_{j})_{x}.
\]

Each \((\mathcal L_{j})_{x}\) depends only on the component of \(x\); the same is true for the limit, because a limit of a family of **constant** diagrams is again constant. Hence on each component \(C\) the stalks of \(\mathcal L\) are all equal to the set

\[
\varprojlim_{j} I_{C}^{(j)},
\]

where \(I_{C}^{(j)}\) is the constant value of \(\mathcal L_{j}\) on \(C\). Consequently \(\mathcal L\) is locally constant.

Thus **every limit that exists in \(\mathbf{Shv}(X)\) lands again in \(\mathbf{LocConst}(X)\)**, and the inclusion \(i\) preserves *all* limits.

> **Result 1.**  
> The inclusion \(i:\mathbf{LocConst}(X)\hookrightarrow\mathbf{Shv}(X)\) preserves **all limits** (products, equalizers, pull‑backs,

*Original question: [Which limits and colimits are preserved by the inclusion of locally constant sheaves into all sheaves?](https://math.stackexchange.com/questions/5148312/which-limits-and-colimits-are-preserved-by-the-inclusion-of-locally-constant-she) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
