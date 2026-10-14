---
layout: question
title: Lower bound on the dimension of a sufficient statistic for a pREC
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Lower bound on the dimension of a
  sufficient statistic for a pREC'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We have a **regular exponential family** with \(p\) free parameters  

\[
f_{\theta}(x)=\exp\Big\{\,B(\theta)^{\!\top}K(x)+H(x)+q(\theta)\Big\},
\qquad \theta\in\Theta\subset\mathbb R^{p},
\]

where  

* \(K(x)=(K_{1}(x),\dots ,K_{d}(x))^{\!\top}\) does **not** depend on \(\theta\);  
* \(B(\theta)=(B_{1}(\theta),\dots ,B_{d}(\theta))^{\!\top}\) is the *natural‑parameter* function;  
* the mapping \(\theta\mapsto B(\theta)\) is one‑to‑one and smooth (this is the *regular* part).

Given an i.i.d. sample \(X_{1},\dots ,X_{n}\) we call a statistic
\(T_{n}=T(X_{1},\dots ,X_{n})\) **sufficient** for \(\theta\) if, after we know
\(T_{n}\), the conditional distribution of the whole sample no longer
depends on \(\theta\).

The student asks:

1. **Is there a universal lower bound on the dimension of a sufficient
statistic?**  
   In particular, must any sufficient statistic have at least \(p\) real
   components (degrees of freedom)?

2. **Is the “identity’’ statistic for a single observation a genuine
   exception?**  

We answer these questions completely, showing exactly when the bound
\(p\) holds and when it can be smaller.

--------------------------------------------------------------------

## 2.  Step‑by‑step solution

### 2.1  Likelihood of a sample from the exponential family

For a sample \(\mathbf X=(X_{1},\dots ,X_{n})\) the joint density is

\[
\begin{aligned}
L(\theta;\mathbf X)
&=\prod_{i=1}^{n}
   \exp\Big\{ B(\theta)^{\!\top}K(X_{i})+H(X_{i})+q(\theta)\Big\}  \\
&= \exp\Big\{ B(\theta)^{\!\top}\underbrace{\sum_{i=1}^{n}K(X_{i})}\_{S_{n}}
               +\sum_{i=1}^{n}H(X_{i}) + n\,q(\theta)\Big\}.
\end{aligned}
\]

All the dependence on \(\theta\) appears **only** through the vector

\[
S_{n}= \sum_{i=1}^{n} K(X_{i})\in\mathbb R^{d}.
\]

Consequently the **factorisation theorem** tells us that

* the statistic \(S_{n}\) is sufficient for \(\theta\);
* any statistic that is a one‑to‑one (measurable) function of \(S_{n}\) is also sufficient.

Thus *the whole problem reduces to the geometry of the vector‑valued
function* \(K(\cdot)\).

--------------------------------------------------------------------

### 2.2  Minimal sufficient statistic

A sufficient statistic \(T_{n}\) is **minimal** if every other sufficient
statistic is a (measurable) function of \(T_{n}\).  
For an exponential family the sum \(S_{n}\) is already minimal (Lehmann–Scheffé theorem).  
Hence the *smallest possible* dimension of a sufficient statistic is the
dimension of the **range** of \(S_{n}\).

### 2.3  How many coordinates does \(S_{n}\) really need?

The vector \(S_{n}\) lives in \(\mathbb R^{d}\), but the *effective*
dimension is the rank of the linear span of the functions
\(K_{1},\dots ,K_{d}\) that are actually used by the natural‑parameter
vector \(B(\theta)\).

Define the **Jacobian matrix** of the natural‑parameter map

\[
J(\theta)=\frac{\partial B(\theta)}{\partial \theta^{\!\top}}
        =\bigl[\partial_{\theta_{j}}B_{i}(\theta)\bigr]_{i=1,\dots ,d\; ;\; j=1,\dots ,p}.
\]

*Regularity* means that \(J(\theta)\) has **full rank \(p\)** for every
\(\theta\in\Theta\).  
Full rank implies that the \(p\)‑dimensional manifold
\(\{B(\theta):\theta\in\Theta\}\) is not contained in any lower‑dimensional
linear subspace of \(\mathbb R^{d}\).

Now consider the linear map

\[
\Phi:\mathbb R^{d}\longrightarrow \mathbb R^{p},
\qquad \Phi(u)=J(\theta_{0})^{\!\top}u,
\]

where \(\theta_{0}\) is any fixed parameter value.  Because \(J(\theta_{0})\)
has rank \(p\), \(\Phi\) is onto \(\mathbb R^{p}\).  Consequently there exists
a **\(p\times d\) matrix** \(A\) (for instance, any left‑inverse of
\(J(\theta_{0})^{\!\top}\)) such that the transformed statistic

\[
T_{n}=A\,S_{n}\in\mathbb R^{p}
\]

still contains *all* the information about \(\theta\).  Indeed,

\[
B(\theta)^{\!\top}S_{n}= \bigl(A^{\!\top}B(\theta)\bigr)^{\!\top}T_{n},
\]

so the likelihood can be written as a function of \(T_{n}\) alone.
Because \(A\) has rank \(p\), the mapping \(S_{n}\mapsto T_{n}\) is
one‑to‑one on the subspace spanned by the likelihood‑relevant part of
\(S_{n}\).  Hence:

* **The minimal sufficient statistic can be taken to be a \(p\)-dimensional
vector.**  
* No sufficient statistic can have dimension **smaller than \(p\)**,
otherwise the likelihood would not be able to distinguish all possible
values of the \(p\)-dimensional parameter.

Thus for a *full‑rank regular* \(p\)-parameter exponential family we have

\[
\boxed{\text{minimum possible dimension of a sufficient statistic}=p},
\]

and the bound does **not** depend on the sample size \(n\).

--------------------------------------------------------------------

### 2.4  What about the “identity’’ statistic when \(n=1\)?

For \(n=1\) the statistic \(X_{1}\) (the identity map) is certainly
sufficient, because the whole sample is just one observation.
However it is **not minimal**: the factorisation above shows that the
single‑observation sufficient statistic can be reduced to

\[
T_{1}=K(X_{1})\in\mathbb R^{d}\quad\text{and further to}\quad
\tilde T_{1}=A\,K(X_{1})\in\mathbb R^{p}.
\]

Thus the “exception’’ is only apparent; the identity statistic merely
contains *extra* irrelevant components that can be discarded without loss
of information.

--------------------------------------------------------------------

### 2.5  When can the lower bound be smaller than \(p\)?

If the exponential family is **not full rank**, i.e. the Jacobian
\(J(\theta)\) has rank \(r<p\) (some linear combination of the natural
parameters is constant), then the likelihood depends on \(\theta\) only
through an \(r\)-dimensional sub‑parameter.  In that situation the minimal
sufficient statistic has dimension \(r\) (which can be strictly less than
\(p\)).  

A simple illustration: a normal distribution with *known variance*,
\(\mathcal N(\mu,1)\).  The parameter space is \(\Theta=\mathbb R\) (so
\(p=1\)).  The natural statistic is \(K(x)=x\) (dimension \(d=1\)),
hence the minimal sufficient statistic is the sample mean, which has
dimension \(1=p\).  If we artificially re‑parameterise by
\(\theta=(\mu,\mu^{2})\) (so \(p=2\) but the two components are not
independent), the family is still the same normal

*Original question: [Lower bound on the dimension of a sufficient statistic for a pREC](https://math.stackexchange.com/questions/5151861/lower-bound-on-the-dimension-of-a-sufficient-statistic-for-a-prec) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
