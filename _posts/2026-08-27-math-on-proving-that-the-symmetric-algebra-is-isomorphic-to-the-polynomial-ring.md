---
layout: question
title: On proving that the symmetric algebra is isomorphic to the polynomial ring.
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: On proving that the symmetric algebra
  is isomorphic to the polynomial ring.'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What is being asked?

We have  

* a commutative ring \(A\);
* a free \(A\)-module \(M\) of rank \(n\) with basis \(\{x_1,\dots ,x_n\}\);
* the **tensor algebra**  

\[
T_A(M)=\bigoplus_{r\ge 0}T_A^{r}(M),\qquad 
T_A^{0}(M)=A,\; T_A^{r}(M)=\underbrace{M\otimes_A\cdots\otimes_AM}_{r\text{ copies}} .
\]

Inside \(T_A(M)\) we consider the two‑sided ideal  

\[
I:=\big\langle\,x\otimes y-y\otimes x\mid x,y\in M\,\big\rangle .
\]

The **symmetric algebra** of \(M\) is the quotient  

\[
\operatorname{Sym}_A(M)=T_A(M)/I .
\]

The map  

\[
f\colon M\longrightarrow A[X_1,\dots ,X_n],\qquad 
x_i\longmapsto X_i
\]

is \(A\)-linear, hence by the universal property of the tensor algebra it extends uniquely to an
\(A\)-algebra homomorphism  

\[
F\colon T_A(M)\longrightarrow A[X_1,\dots ,X_n].
\]

Because the polynomial ring is commutative we already know \(I\subseteq\ker(F)\).
The problem is to show the reverse inclusion  

\[
\ker(F)\subseteq I,
\]

i.e. that \(F\) factors through the quotient and the induced map  

\[
\bar F\colon \operatorname{Sym}_A(M)=T_A(M)/I\;\longrightarrow\;A[X_1,\dots ,X_n]
\]

is **injective**. Equivalently we must prove that \(\operatorname{Sym}_A(M)\) is (canonically) isomorphic to the polynomial ring.

--------------------------------------------------------------------

## 2.  Full solution, step by step  

### Step 1 – The homomorphism \(F\) and its surjectivity  

The assignment \(x_i\mapsto X_i\) defines an \(A\)-linear map \(f:M\to A[X_1,\dots ,X_n]\).
By the universal property of the tensor algebra there is a unique algebra homomorphism  

\[
F:T_A(M)\longrightarrow A[X_1,\dots ,X_n] ,\qquad 
F(x_{i_1}\otimes\cdots\otimes x_{i_r})=X_{i_1}\cdots X_{i_r}.
\]

Every monomial \(X_{i_1}\cdots X_{i_r}\) occurs as the image of a pure tensor, therefore \(F\) is **surjective**.

---

### Step 2 – The ideal \(I\) is contained in \(\ker(F)\)

For any \(x,y\in M\),

\[
F(x\otimes y-y\otimes x)=F(x)F(y)-F(y)F(x)=0
\]

because the polynomial ring is commutative. Hence the generators of \(I\) map to \(0\), and therefore  

\[
I\subseteq\ker(F).
\]

Thus \(F\) factors through the quotient and we obtain a well‑defined \(A\)-algebra homomorphism  

\[
\bar F:\operatorname{Sym}_A(M)=T_A(M)/I\longrightarrow A[X_1,\dots ,X_n].
\]

\(\bar F\) is still surjective (it has the same image as \(F\)).

---

### Step 3 – Constructing a map in the opposite direction  

Define an \(A\)-algebra homomorphism  

\[
\psi:A[X_1,\dots ,X_n]\longrightarrow \operatorname{Sym}_A(M)
\]

by sending each indeterminate to the class of the corresponding basis element:

\[
\psi(X_i)=\overline{x_i}\in \operatorname{Sym}_A(M)\qquad (i=1,\dots ,n).
\]

Because \(\operatorname{Sym}_A(M)\) is **commutative** (the ideal \(I\) forces all tensors to commute), this assignment respects the relations among the \(X_i\) (there are none besides commutativity), so \(\psi\) extends uniquely to an algebra homomorphism.

---

### Step 4 – \(\psi\) is a two‑sided inverse of \(\bar F\)

*On generators of \(\operatorname{Sym}_A(M)\).*  
Let \(\overline{x_{i_1}\otimes\cdots\otimes x_{i_r}}\) be the class in \(\operatorname{Sym}_A(M)\) of a pure tensor. Then  

\[
(\psi\circ\bar F)\bigl(\overline{x_{i_1}\otimes\cdots\otimes x_{i_r}}\bigr)
   =\psi\bigl(F(x_{i_1}\otimes\cdots\otimes x_{i_r})\bigr)
   =\psi(X_{i_1}\cdots X_{i_r})
   =\overline{x_{i_1}}\cdots\overline{x_{i_r}}
   =\overline{x_{i_1}\otimes\cdots\otimes x_{i_r}} .
\]

Thus \(\psi\circ\bar F =\operatorname{id}_{\operatorname{Sym}_A(M)}\).

*On generators of the polynomial ring.*  
For each \(i\),

\[
(\bar F\circ\psi)(X_i)=\bar F(\overline{x_i})=F(x_i)=X_i .
\]

Since both maps are algebra homomorphisms, they agree on all polynomials, hence  

\[
\bar F\circ\psi=\operatorname{id}_{A[X_1,\dots ,X_n]} .
\]

Consequently \(\bar F\) is bijective and \(\psi\) is its inverse.

---

### Step 5 – The kernel of \(F\) is exactly \(I\)

Because \(\bar F\) is injective, \(\ker(\bar F)=\{0\}\). By definition  

\[
\ker(\bar F)=\bigl(\ker(F)+I\bigr)/I .
\]

Thus \(\ker(F)+I=I\), i.e. \(\ker(F)\subseteq I\). Combined with the inclusion proved in Step 2 we obtain  

\[
\ker(F)=I .
\]

Equivalently, the induced map \(\bar F\) is an isomorphism

\[
\boxed{\operatorname{Sym}_A(M)\;\cong\;A[X_1,\dots ,X_n]} .
\]

--------------------------------------------------------------------

## 3.  Final answer  

For a free \(A\)-module \(M\) of rank \(n\) with basis \(\{x_1,\dots ,x_n\}\) the symmetric algebra
\(\operatorname{Sym}_A(M)\) is canonically isomorphic to the polynomial ring in \(n\) variables over \(A\):

\[
\operatorname{Sym}_A(M)\;\xrightarrow{\;\;\cong\;\;}\;A[X_1,\dots ,X_n],
\qquad 
\overline{x_i}\longmapsto X_i .
\]

The kernel of the canonical map \(F:T_A(M)\to A[X_1,\dots ,X_n]\) is exactly the ideal
\(I=\langle x\otimes y-y\otimes x\mid x,y\in M\rangle\).

--------------------------------------------------------------------

## 4.  Common mistakes to avoid  

| Mistake | Why it is wrong | How to correct it |
|---|---|---|
| **Thinking that surjectivity of \(F\) already gives an isomorphism.** | Surjectivity alone does not control the kernel; one must also prove injectivity. | Build the inverse map \(\psi\) or show the kernel is exactly \(I\). |
| **Ignoring the commutativity of the target ring.** | The ideal \(I\) is precisely what forces commutativity in the quotient. Without using it, you cannot define \(\psi\). | Explicitly use that \(\operatorname{Sym}_A(M)=T_A(M)/I\) is commutative when sending the indeterminates to \(\overline{x_i}\). |
| **Working with arbitrary elements of \(T_A(M)\) without grading.** | Elements are sums of tensors of different degrees; the map \(F\) respects the natural grading, which is crucial for the kernel argument. | Decompose any element into homogeneous components and treat each degree separately (or use the inverse map argument above). |
| **Assuming the polynomial ring is a domain and concluding \(\ker(F)=0\).** | Over a general commutative ring \(A\) the polynomial ring may have zero‑divisors, so “no non‑zero polynomial can map to zero” is false. | Use the explicit inverse \(\psi\) or the basis‑monomial argument; no hypothesis on \(A\) is needed. |
| **Forgetting to mod out by the ideal before defining \(\psi\).** | Directly sending \(X_i\) to \(x_i\in T_A(M)\) would not respect the relations \(x\otimes y-y\otimes x\). | Define \(\psi\) with target \(\operatorname{Sym}_A(M)=T_A(M)/I\); then the relations are already satisfied. |

Keeping these points in mind ensures a clean and rigorous proof that the symmetric algebra of a free module is the usual polynomial ring.

*Original question: [On proving that the symmetric algebra is isomorphic to the polynomial ring.](https://math.stackexchange.com/questions/5148016/on-proving-that-the-symmetric-algebra-is-isomorphic-to-the-polynomial-ring) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
