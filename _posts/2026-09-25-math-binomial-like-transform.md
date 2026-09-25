---
layout: question
title: Binomial like transform
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Binomial like transform'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1. What the problem is asking  

We are given a sequence \(\{a_n\}_{n\ge 0}\) and we form a new sequence  

\[
s_n=\sum_{r\ge 0}\binom{n+r}{r}\,a_{n+r}\qquad (n=0,1,2,\dots)
\]

The question is:  

* What is this “binomial‑like’’ transformation?  
* Does it have a name?  
* What are its basic algebraic properties (generating‑function description, inverse formula, growth‑rate consequences, etc.)?  

We shall answer all of these points in a completely explicit, step‑by‑step way.

---

## 2. Step‑by‑step analysis  

### 2.1 Rewrite the sum with a single index  

Put \(k=n+r\) (so \(k\ge n\)). Then  

\[
s_n=\sum_{k=n}^{\infty}\binom{k}{n}\,a_k .
\tag{1}
\]

The binomial coefficient \(\displaystyle\binom{k}{n}=\binom{k}{k-n}\) is the entry of the (infinite) lower‑triangular matrix  

\[
B=\bigl(b_{n,k}\bigr)_{n,k\ge 0},\qquad  
b_{n,k}= \begin{cases}
\displaystyle\binom{k}{n}, & k\ge n,\\[4pt]
0, & k<n .
\end{cases}
\]

Thus the transformation \(\{a_k\}\mapsto\{s_n\}\) is **multiplication by the matrix \(B\)**.

---

### 2.2 Ordinary generating functions  

Define the ordinary generating functions (OGFs)

\[
A(z)=\sum_{k\ge 0}a_kz^k ,\qquad   
S(z)=\sum_{n\ge 0}s_nz^n .
\]

Insert (1) into the definition of \(S(z)\) and interchange the two sums (formal power‑series manipulations are legitimate because each coefficient involves only finitely many terms):

\[
\begin{aligned}
S(z) &=
\sum_{n\ge 0}\Bigl(\sum_{k\ge n}\binom{k}{n}a_k\Bigr)z^n
      =\sum_{k\ge 0}a_k\sum_{n=0}^{k}\binom{k}{n}z^n  \\[4pt]
     &=\sum_{k\ge 0}a_k(1+z)^k
      =A(1+z).
\end{aligned}
\tag{2}
\]

**Result:** the OGF of the transformed sequence is obtained by the simple substitution  

\[
\boxed{S(z)=A(1+z)} .
\]

This identity completely characterises the transformation.

---

### 2.3 Inverting the transformation  

The matrix \(B\) is invertible. Its inverse is the classic *binomial‑inverse* matrix

\[
(B^{-1})_{n,k}=(-1)^{k-n}\binom{k}{n},\qquad k\ge n .
\]

Indeed, a short verification:

\[
\sum_{j=n}^{k} \binom{j}{n}(-1)^{k-j}\binom{k}{j}
 =\delta_{n,k},
\]

where \(\delta_{n,k}\) is the Kronecker delta (use the binomial theorem for \((1-1)^{k-n}\)).  

Multiplying (1) by this inverse gives the **inverse formula**

\[
\boxed{a_n=\sum_{r\ge 0}(-1)^{r}\binom{n+r}{r}\,s_{n+r}}
\qquad (n\ge 0).
\tag{3}
\]

In generating‑function language, (2) implies  

\[
A(z)=S(z-1),
\]

which is exactly the same inversion.

---

### 2.4 Growth / convergence considerations  

If the original OGF \(A(z)\) converges for \(|z|<R\) (radius of convergence \(R>0\)), then (2) tells us that  

\[
S(z)=A(1+z)
\]

converges for \(|1+z|<R\); i.e. the disc centred at \(-1\) with radius \(R\).  
When we re‑expand \(S(z)\) about the origin, its radius of convergence is the distance from \(0\) to the nearest singularity of \(A(1+z)\), namely  

\[
\rho = R-1\quad\text{(if }R>1\text{)}.
\]

Consequently, the coefficient growth of \(\{s_n\}\) is essentially the same as that of \(\{a_n\}\); more precisely, if  

\[
a_n = O(\alpha^{\,n})\quad(\alpha<R^{-1}),
\]

then  

\[
s_n = O\bigl((\alpha)^{\,n}\bigr)
\]

as well (the binomial factor \(\binom{n+r}{r}\) grows only polynomially, not exponentially).

---

### 2.5 Naming the transform  

The mapping  

\[
a_n\;\longmapsto\; s_n=\sum_{k=n}^{\infty}\binom{k}{n}a_k
\]

is known as the **(right) binomial transform of the second kind** or **inverse binomial transform**.  
It differs from the *standard* (first‑kind) binomial transform  

\[
b_n=\sum_{k=0}^{n}\binom{n}{k}a_k,
\]

but the two are related by a simple index reversal.  
References: Riordan, *Combinatorial Identities*; Wilf, *generatingfunctionology* (Section 2.2).

---

## 3. Final answer  

* The transformation is the binomial transform of the second kind, equivalently multiplication by the lower‑triangular matrix \(b_{n,k}=\binom{k}{n}\).  

* **Generating‑function description**  

  \[
  S(z)=\sum_{n\ge0}s_nz^n = A(1+z),
  \]
  where \(A(z)=\sum_{k\ge0}a_kz^k\).

* **Inverse transformation**  

  \[
  a_n = \sum_{r\ge0}(-1)^r\binom{n+r}{r}\,s_{n+r},
  \qquad\text{or }A(z)=S(z-1).
  \]

* **Growth / convergence** – the radius of convergence of \(S\) is the radius of convergence of \(A\) shifted by \(-1\); polynomial binomial factors do not change exponential growth rates.

Thus the series transformation is completely understood via its generating function \(A(1+z)\) and the simple binomial‑inverse formula (3).

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing the indices** and writing \(\displaystyle s_n=\sum_{r\ge0}\binom{n}{r}a_{n+r}\). | The correct coefficient is \(\binom{n+r}{r}=\binom{n+r}{n}\). | Replace \(r\) by \(k-n\) (or set \(k=n+r\)) to see the proper binomial entry. |
| **Treating the sum as finite** because \(\binom{n+r}{r}=0\) for large \(r\). | Binomial coefficients never become zero for \(r\ge0\); the sum is (generally) infinite. | Keep the sum to \(\infty\) and rely on convergence of the generating function, not on vanishing terms. |
| **Using the first‑kind binomial transform formula** \(b_n=\sum_{k=0}^n\binom{n}{k}a_k\). | That transform is different; the matrix entries are \(\binom{k}{n}\), not \(\binom{n}{k}\). | Remember the matrix is lower‑triangular with entries \(\binom{k}{n}\) (row index \(n\), column index \(k\)). |
| **Missing the sign \((-1)^r\) in the inverse** and writing \(a_n=\sum\binom{n+r}{r}s_{n+r}\). | The inverse matrix carries the factor \((-1)^{k-n}\). | Derive the inverse by solving \(B^{-1}B=I\) or by using the generating‑function identity \(A(z)=S(z-1)\). |
| **Assuming the radius of convergence stays the same** after the transform. | Substituting \(z\mapsto1+z\) shifts the disc of convergence; the new radius is \(R-1\) (if \(R>1\)). | Translate the domain condition \(|1+z|<R\) into a statement about \(|z|\). |

Keeping these points in mind will prevent the usual pitfalls when working with

*Original question: [Binomial like transform](https://math.stackexchange.com/questions/5150367/binomial-like-transform) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
