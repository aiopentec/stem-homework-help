---
layout: post
title: "Probability for an $n\times n$ matrix to have only real eigenvalues"
author: StemFix Bot
category: math
tags: [math]
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem asks (in plain language)

We are given an \(n\times n\) matrix  

\[
A=\bigl(a_{ij}\bigr)_{1\le i,j\le n},\qquad 
a_{ij}\stackrel{\text{i.i.d.}}{\sim}\text{Uniform}[0,1].
\]

All the entries are independent and drawn from the same continuous
distribution (the uniform law on the interval \([0,1]\)).
The question is:

> **What is the probability that every eigenvalue of \(A\) is a real
> number?**

In other words, we have to compute  

\[
p_n:=\mathbb P\bigl\{\,\sigma(A)\subset \mathbb R\,\bigr\},
\]

where \(\sigma(A)\) denotes the (multiset of) eigenvalues of \(A\).

--------------------------------------------------------------------

## 2.  Full solution – step by step  

### 2.1  Preliminary observations  

* The entries are **real**, so the characteristic polynomial of \(A\) has
  real coefficients. Consequently eigenvalues appear either as real
  numbers or in complex‑conjugate pairs.

* Because the distribution of each entry is absolutely continuous,
  the event “\(A\) has a repeated eigenvalue” has probability \(0\).  
  Hence the set of matrices with **exactly** \(k\) distinct real
  eigenvalues (and \(\frac{n-k}{2}\) complex‑conjugate pairs) is an open
  subset of \([0,1]^{n^{2}}\) and carries a positive Lebesgue measure.

* For \(n=1\) the matrix consists of a single number, which is always
  real, so \(p_1=1\).

* For \(n=2\) we can check directly.  
  Write  

  \[
  A=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad a,b,c,d\in[0,1].
  \]

  The eigenvalues are real iff the discriminant  

  \[
  \Delta=(a-d)^{2}+4bc\ge 0 .
  \]

  Since \(b,c\ge 0\) we have \(4bc\ge 0\) and \((a-d)^{2}\ge 0\); therefore
  \(\Delta\ge 0\) **always**. Hence  

  \[
  p_2=1 .
  \]

  (The same phenomenon occurs for any i.i.d. distribution that is
  supported on \([0,\infty)\).)

* From now on we assume \(n\ge 3\). In this range the probability is
  strictly between \(0\) and \(1\) and, as we shall see, it becomes
  extremely small when \(n\) grows.

--------------------------------------------------------------------

### 2.2  A known universal result for real i.i.d. matrices  

Let  

\[
X_n=\bigl(x_{ij}\bigr)_{1\le i,j\le n},
\qquad x_{ij}\stackrel{\text{i.i.d.}}{\sim}\mu,
\]

where \(\mu\) is any **absolutely continuous** probability measure on
\(\mathbb R\) having a finite second moment (the uniform law on \([0,1]\)
satisfies both conditions).  

A deep theorem due to **Edelman–Kostlan (1995)**, later refined by
**Forrester, Krishnapur, and many others**, says that the *asymptotic*
behaviour of the probability that **all** eigenvalues of \(X_n\) are real
does **not** depend on the precise shape of \(\mu\); it is the same as
for the *real Ginibre ensemble* (i.e. Gaussian i.i.d. entries).

Consequently we may use the exact formula that is known for the Gaussian
case and then invoke the universality theorem to claim that the same
asymptotic formula holds for the uniform distribution.

--------------------------------------------------------------------

### 2.3  Exact formula for the real Ginibre ensemble  

For the matrix  

\[
G_n=\bigl(g_{ij}\bigr)_{1\le i,j\le n},
\qquad g_{ij}\stackrel{\text{i.i.d.}}{\sim} N(0,1),
\]

the probability that **all** eigenvalues are real is

\[
\boxed{%
p^{\text{Gin}}_n
=
2^{-\frac{n(n-1)}{4}}\;
\prod_{j=1}^{n}\frac{\Gamma\!\bigl(\frac{j}{2}\bigr)}
                     {\Gamma\!\bigl(\frac12\bigr)} }        \tag{1}
\]

(see Edelman, *The probability that a random real Gaussian matrix has
real eigenvalues*, 1997; also Forrester, *Log‑gases and Random Matrices*,
2010).

The product can be written in a more elementary way. Using the identity

\[
\Gamma\!\bigl(\tfrac12\bigr)=\sqrt{\pi},\qquad
\Gamma\!\bigl(k+\tfrac12\bigr)=\frac{(2k)!}{4^{k}k!}\sqrt{\pi},
\]

one obtains

\[
p^{\text{Gin}}_n
=
\frac{1\cdot 3\cdot 5\cdots (2n-1)}{2^{\,\frac{n(n-1)}{2}}\,n!}
=
\frac{(2n-1)!!}{2^{\,\frac{n(n-1)}{

*Original question: [Probability for an $n\times n$ matrix to have only real eigenvalues](https://math.stackexchange.com/questions/3770846/probability-for-an-n-times-n-matrix-to-have-only-real-eigenvalues) on Mathematics Stack Exchange, licensed CC BY-SA.*
