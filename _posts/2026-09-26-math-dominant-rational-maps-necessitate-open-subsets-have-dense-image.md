---
layout: question
title: Dominant rational maps necessitate open subsets have dense image
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Dominant rational maps necessitate
  open subsets have dense image'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

Let  

* \(X\) and \(Y\) be irreducible algebraic varieties over an algebraically closed field,  
* \(\varphi\) a **rational map** from \(X\) to \(Y\).  

A rational map is an equivalence class of morphisms
\[
(U,\varphi_U),\qquad U\subset X\ \text{non‑empty open},\ \varphi_U:U\to Y,
\]
where two representatives \((U,\varphi_U)\) and \((V,\varphi_V)\) are equivalent when they agree on the overlap \(U\cap V\).

Hartshorne says that **\(\varphi\) is dominant** iff for *one* (hence for *every*) such pair the image is dense in \(Y\).

The task is to prove the “hence for every’’ part:

> If there exists a representative \((U,\varphi_U)\) with \(\overline{\varphi_U(U)}=Y\), then for **any** other representative \((V,\varphi_V)\) we also have \(\overline{\varphi_V(V)}=Y\).

Equivalently we must show that the image of the restriction to the common open set
\[
\varphi_{U\cap V}= \varphi_U|_{U\cap V}= \varphi_V|_{U\cap V}
\]
is already dense in \(Y\).

---

## 2.  Proof, step by step  

### 2.1  Basic facts we will use  

1. **Irreducibility of open subsets** – If \(X\) is irreducible, every non‑empty open subset of \(X\) is itself irreducible and dense in \(X\).  
2. **Continuity of morphisms** – A morphism of varieties is a continuous map for the Zariski topology; the preimage of an open set is open.  
3. **Density criterion** – A subset \(A\subset Y\) is dense iff every non‑empty open subset of \(Y\) meets \(A\).

### 2.2  The intersection \(U\cap V\) is a non‑empty dense open in both \(U\) and \(V\)

Because \(X\) is irreducible, the intersection of two non‑empty opens is again a non‑empty open; moreover it is dense in each of them.  
Hence \(U\cap V\) is an irreducible variety and the restriction maps
\[
\varphi_{U\cap V}:= \varphi_U|_{U\cap V}= \varphi_V|_{U\cap V}
\]
are well defined morphisms \(U\cap V\to Y\).

### 2.3  The image of \(\varphi_{U\cap V}\) is dense in \(Y\)

Assume, for contradiction, that \(\overline{\varphi_{U\cap V}(U\cap V)}\neq Y\).  
Then there exists a **non‑empty open** subset \(W\subset Y\) disjoint from \(\varphi_{U\cap V}(U\cap V)\).

Because \(\varphi_U\) is a morphism, the pre‑image
\[
\varphi_U^{-1}(W)\subset U
\]
is open (and non‑empty, since \(\varphi_U(U)\) is dense in \(Y\); the dense image guarantees that \(W\) meets \(\varphi_U(U)\)).  

Now \(U\cap V\) is dense in \(U\), so the open set \(\varphi_U^{-1}(W)\) must intersect \(U\cap V\):
\[
\varphi_U^{-1}(W)\cap (U\cap V)\neq\varnothing .
\]

Pick a point \(x\) in this intersection. Then
\[
x\in U\cap V,\qquad \varphi_U(x)\in W .
\]
But on \(U\cap V\) the two representatives coincide, i.e. \(\varphi_U(x)=\varphi_V(x)=\varphi_{U\cap V}(x)\).  
Thus \(\varphi_{U\cap V}(x)\in W\), contradicting the definition of \(W\) (which was chosen to avoid the image of \(\varphi_{U\cap V}\)).

Hence our assumption was false and we must have  
\[
\overline{\varphi_{U\cap V}(U\cap V)} = Y .
\]

### 2.4  Consequence for any other representative  

Because \(U\cap V\subset V\) we have
\[
\varphi_V(V) \supset \varphi_{U\cap V}(U\cap V) .
\]
Taking closures,
\[
\overline{\varphi_V(V)} \supset \overline{\varphi_{U\cap V}(U\cap V)} = Y .
\]
Thus \(\overline{\varphi_V(V)} = Y\); i.e. the image of **any** representative \((V,\varphi_V)\) is dense in \(Y\).

Therefore a rational map is dominant **iff** one (equivalently, every) representative has dense image.

---

## 3.  Final answer  

If a rational map \(\varphi : X \dashrightarrow Y\) has one representative \((U,\varphi_U)\) whose image is dense in \(Y\), then for every other representative \((V,\varphi_V)\) we also have \(\overline{\varphi_V(V)}=Y\). The key point is that the common open set \(U\cap V\) is dense in both domains, and the restriction of the morphism to this set already has dense image; continuity of morphisms then forces the whole image of any other representative to be dense as well. Hence the definition “dominant if for *some* (and hence *every*) representative the image is dense’’ is correct.

---

## 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking “open ⇒ dense’’** in any topological space. | In the Zariski topology an open set need not be dense (e.g. a proper open subset of a reducible variety). The argument works because the ambient space \(X\) is **irreducible**; then every non‑empty open is dense. | Always remember to use irreducibility when you claim an open set is dense. |
| **Assuming the image of a restriction is automatically dense** because the larger image is dense. | A subset of a dense set can be non‑dense (think of a line missing a point). One must prove density for the restriction, using openness of the pre‑image of a non‑empty open in \(Y\). | Use the density‑criterion argument above: any open \(W\subset Y\) meeting \(\varphi_U(U)\) must already meet the image of the restriction, because the pre‑image of \(W\) is open and meets the dense open \(U\cap V\). |
| **Confusing equality of maps with equality of their images**. | The two representatives agree point‑wise on the overlap, but their *domains* are different, so you cannot directly replace \(\varphi_U(U)\) by \(\varphi_V(V)\). | Work with the common restriction \(\varphi_{U\cap V}\); its image is contained in both images, and its density forces the density of each full image. |
| **Neglecting continuity of morphisms**. | Without using that morphisms pull back open sets to open sets, the argument that the pre‑image of a non‑empty open meets the dense open subset fails. | Explicitly invoke the fact that a morphism of varieties is continuous for the Zariski topology. |

Keeping these points in mind will prevent the typical pitfalls when handling dominant rational maps.

*Original question: [Dominant rational maps necessitate open subsets have dense image](https://math.stackexchange.com/questions/5150437/dominant-rational-maps-necessitate-open-subsets-have-dense-image) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
