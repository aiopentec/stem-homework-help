---
layout: post
title: Ring structure on the absolute Galois group of a finite field
author: StemFix Bot
category: math
tags:
- math
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking  

*Let \(F\) be a finite field, \(\overline{F}\) a separable closure and  
\(G=\operatorname{Gal}(\overline{F}/F)\) its absolute Galois group.*  

1.  We know that \(G\) is (as a topological group) isomorphic to the
    profinite completion \(\widehat{\mathbb Z}\).  
    Via this identification one can *declare* a multiplication on \(G\) by
    transporting the usual multiplication of \(\widehat{\mathbb Z}\):
    if \(\sigma,\tau\in G\) correspond to \(\hat n,\hat m\in\widehat{\mathbb Z}\) then
    \(\sigma*\tau\) is the element that corresponds to \(\hat n\hat m\).

2.  The problem asks for an **intrinsic** description of the product
    \(*\) that does **not** appeal to the explicit isomorphism
    \(G\cong\widehat{\mathbb Z}\).  
    In other words: given two automorphisms \(\sigma,\tau\) of
    \(\overline{F}\) fixing \(F\), can we write down \(\sigma*\tau\) using only
    the structure of the field extensions, the Frobenius map, etc.?

3.  Moreover, it asks why a **ring** structure appears at all: which
    extra data on the Galois (or étale) category of \(F\) forces its
    fundamental group to be a topological ring rather than merely a
    profinite group?

The answer below gives

* an intrinsic definition of the product \(*\);
* a conceptual explanation in terms of the *canonical Frobenius
  endomorphism* of the étale site (or of the fiber functor);
* a short list of typical pitfalls when one works with this situation.

---

## 2.  The canonical Frobenius and the intrinsic description of \(*\)

### 2.1  The arithmetic Frobenius is canonical  

Let \(|F|=q\) (\(q=p^{r}\) with \(p\) prime).  
For every finite étale \(F\)-algebra \(A\) there is a distinguished
\(F\)-endomorphism
\[
\Phi_{A}:A\longrightarrow A,\qquad a\mapsto a^{q}.
\]
When \(A\) is a finite field extension \(L/F\) the map \(\Phi_{L}\) is the
usual *arithmetic Frobenius* (it sends \(x\) to \(x^{q}\)).  

If we view a finite étale \(F\)-algebra as a finite set equipped with a
continuous action of the absolute Galois group,
\(\Phi_{A}\) is exactly the action of a single element
\(\operatorname{Fr}_{F}\in G\), the **Frobenius automorphism** of \(\overline{F}\) :

\[
\operatorname{Fr}_{F}(\alpha)=\alpha^{q}\qquad(\alpha\in\overline{F}).
\]

The element \(\operatorname{Fr}_{F}\) is characterised **intrinsically** as
the unique element of \(G\) whose restriction to any finite Galois
extension \(L/F\) coincides with the arithmetic Frobenius of \(L\).
Thus the generator of the pro‑cyclic group \(G\) does not depend on any
choice of isomorphism with \(\widehat{\mathbb Z}\).

### 2.2  Exponents in \(\widehat{\mathbb Z}\) are defined by restriction  

For any \(\sigma\in G\) and any finite Galois extension \(L/F\) we have a
restriction homomorphism
\[
\operatorname{res}_{L}\colon G\longrightarrow \operatorname{Gal}(L/F).
\]
Since each \(\operatorname{Gal}(L/F)\) is a *finite cyclic* group generated
by \(\operatorname{Fr}_{L}:=\operatorname{Fr}_{F}|_{L}\), there exists a
unique element \(e_{L}(\sigma)\in\mathbb Z/| \operatorname{Gal}(L/F) |\mathbb Z\)
such that
\[
\operatorname{res}_{L}(\sigma)=\operatorname{Fr}_{L}^{\,e_{L}(\sigma)} .
\tag{1}
\]

The family \(\{e_{L}(\sigma)\}_{L}\) is compatible when \(L\subseteq
L'\) (because the restriction maps commute with powers of Frobenius).  
Therefore the compatible system determines a unique element
\[
e(\sigma)\in\widehat{\mathbb Z}=\varprojlim_{L}\mathbb Z/| \operatorname{Gal}(L/F) |\mathbb Z
\]
such that \(e_{L}(\sigma)\) is the image of \(e(\sigma)\) in the finite
quotient.  In other words, \(e(\sigma)\) is the **exponent of \(\sigma\)**
with respect to the canonical generator \(\operatorname{Fr}_{F}\).

The map
\[
e\colon G\longrightarrow\widehat{\mathbb Z},\qquad \sigma\mapsto e(\sigma)
\]
is a continuous isomorphism of topological groups; it is characterised
by the single condition
\[
e(\operatorname{Fr}_{F})=1.
\tag{2}
\]

### 2.3  Intrinsic definition of the product  

Now we can *define* the product \(*\) on \(G\) without mentioning the
identification \(G\cong\widehat{\mathbb Z}\) at the outset.

> **Definition.**  
> For \(\sigma,\tau\in G\) let \(e(\sigma),e(\tau)\in\widehat{\mathbb Z}\) be
> their exponents defined above.  Set
> \[
> \boxed{\;\sigma * \tau\;:=\;\operatorname{Fr}_{F}^{\,e(\sigma)\,e(\tau)}\;}.
> \tag{3}
> \]

Because the exponent map \(e\) is a group isomorphism, (3) makes \(G\)
into a *ring* whose additive structure is the original group law and
whose multiplication satisfies
\[
\operatorname{Fr}_{F}^{\,a} * \operatorname{Fr}_{F}^{\,b}
    =\operatorname{Fr}_{F}^{\,ab}\qquad (a,b\in\widehat{\mathbb Z}),
\]
exactly the rule that was used in the original “computational’’ description.
No external isomorphism has been used: the only data employed are

* the canonical Frobenius element \(\operatorname{Fr}_{F}\), and
* the fact that every finite quotient of \(G\) is cyclic generated by the
  restriction of \(\operatorname{Fr}_{F}\).

Thus (3) is an **intrinsic** formula for \(*\).

---

## 3.  Why a ring structure appears: the categorical point of view  

### 3.1  The fiber functor and its natural endomorphisms  

Let \(\mathcal C\) be the Galois category of finite étale \(F\)-algebras.
Fix the usual fiber functor
\[
\omega\colon \mathcal C \longrightarrow \mathbf{FinSet},\qquad
A\longmapsto \operatorname{Hom}_{F}(A,\overline{F}).
\]

For each integer \(n\ge 0\) the map
\[
\Phi^{(n)}_{A}\colon\omega(A)\longrightarrow\omega(A),\qquad
\varphi\mapsto\varphi^{\,q^{\,n}}
\]
is natural in \(A\); the collection \(\{\Phi^{(n)}\}_{n\in\mathbb Z}\) gives a
continuous homomorphism
\

*Original question: [Ring structure on the absolute Galois group of a finite field](https://math.stackexchange.com/questions/570122/ring-structure-on-the-absolute-galois-group-of-a-finite-field) on Mathematics Stack Exchange, licensed CC BY-SA.*
