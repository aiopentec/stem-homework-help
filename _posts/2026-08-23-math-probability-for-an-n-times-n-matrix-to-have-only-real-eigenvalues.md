---
layout: post
title: Probability for an $n\times n$ matrix to have only real eigenvalues
author: StemFix Bot
category: math
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We have an \(n\times n\) matrix  

\[
A=\bigl(a_{ij}\bigr)_{1\le i,j\le n},
\qquad a_{ij}\stackrel{\text{i.i.d.}}{\sim}\text{Uniform}[0,1],
\]

and we would like to know  

\[
\boxed{\;P_n:=\Pr\bigl(\text{all eigenvalues of }A\text{ are real}\bigr)\;}
\]

for a given size \(n\).  
In words: *pick a matrix at random from the unit cube \([0,1]^{n^{2}}\) (all entries are independent and uniformly distributed); what is the chance that the matrix has no complex eigenvalues?*  

The question is non‑trivial because the eigenvalues are complicated polynomial functions of the entries, and the set  

\[
\mathcal R_n=\{A\in\mathbb R^{n\times n} : \text{all eigenvalues of }A\text{ are real}\}
\]

is neither open nor closed in the usual Euclidean topology.  

---

## 2.  Step‑by‑step analysis  

### 2.1  Small dimensions  

| \(n\) | Reasoning | \(P_n\) |
|------|-----------|---------|
| 1 | A \(1\times1\) matrix is just a real number, so its (single) eigenvalue is always real. | \(1\) |
| 2 | For a \(2\times2\) matrix \(\begin{pmatrix}a&b\\c&d\end{pmatrix}\) the eigenvalues are real iff the discriminant \((a-d)^2+4bc\) is non‑negative.  Because \(b,c\ge 0\) (the entries lie in \([0,1]\)), the term \(4bc\) is never negative, hence the discriminant is always \(\ge0\).  Consequently every such matrix has real eigenvalues. | \(1\) |

Thus the problem becomes interesting only from \(n\ge 3\).

---

### 2.2  The set of “real‑eigenvalue” matrices  

For \(n\ge 3\) let  

\[
p_A(\lambda)=\det(\lambda I -A)=\lambda^{n}+c_{1}(A)\lambda^{n-1}+ \dots +c_{n}(A)
\]

be the characteristic polynomial.  All coefficients \(c_k(A)\) are **polynomial** functions of the entries of \(A\) (they are (up to sign) elementary symmetric functions of the eigenvalues).  

A real‑coefficient polynomial of degree \(n\) has **only real roots** iff its **discriminant** \(\Delta(p_A)\) is non‑negative (for \(n\ge 3\) the discriminant is a polynomial of degree \(2n-2\) in the coefficients).  Hence

\[
\mathcal R_n = \{A\in[0,1]^{n^{2}} \; :\; \Delta(p_A)\ge 0\}.
\]

The map  

\[
\Phi : [0,1]^{n^{2}} \longrightarrow \mathbb R^{n},\qquad 
\Phi(A)=(c_{1}(A),\dots ,c_{n}(A))
\]

is polynomial, thus absolutely continuous with respect to Lebesgue measure on \(\mathbb R^{n}\).  Consequently the probability we are looking for can be written as the volume of the image region defined by the inequality \(\Delta\ge0\):

\[
P_n = \frac{\operatorname{Vol}_{n^{2}}\bigl(\{A\in[0,1]^{n^{2}}:\Delta(p_A)\ge0\}\bigr)}
            {\operatorname{Vol}_{n^{2}}\bigl([0,1]^{n^{2}}\bigr)} .
\]

Because \(\Delta(p_A)\) is a non‑constant polynomial, the set \(\{A:\Delta(p_A)=0\}\) has Lebesgue measure zero.  Therefore the probability of hitting the *boundary* (multiple eigenvalues) is zero, and we may replace “\(\ge0\)” by “\(>0\)’’ without changing the value of \(P_n\).

---

### 2.3  Why a closed‑form answer is not known  

For the **Gaussian (real Ginibre) ensemble** the joint density of the eigenvalues is known explicitly, and one can integrate it to obtain the exact probability

\[
P_n^{\text{Ginibre}} = 2^{-\,n(n-1)/4}\qquad (n\ge 1).
\]

The crucial point is the rotational symmetry of the Gaussian law; the eigenvalue density factorises in a way that makes the integration possible.

The uniform law on \([0,1]\) **lacks rotational invariance**; the joint eigenvalue density is not known in a tractable form.  Consequently no closed elementary expression for \(P_n\) is available at present.  The problem reduces to evaluating a high‑dimensional integral of the indicator of the set \(\{\Delta>0\}\), which is computationally intractable for symbolic calculation beyond the smallest sizes.

---

### 2.4  What is known about the magnitude of \(P_n\)  

Even though an exact formula is missing, a number of results give the **asymptotic behaviour** of \(P_n\) for *any* continuous distribution with a density (including the uniform distribution).  The key facts are:

| Fact | Statement |
|------|------------|
| **Universality of the leading exponent** | For i.i.d

*Original question: [Probability for an $n\times n$ matrix to have only real eigenvalues](https://math.stackexchange.com/questions/3770846/probability-for-an-n-times-n-matrix-to-have-only-real-eigenvalues) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
