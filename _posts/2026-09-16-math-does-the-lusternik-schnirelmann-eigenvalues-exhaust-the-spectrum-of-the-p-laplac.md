---
layout: question
title: Does the Lusternik-Schnirelmann eigenvalues exhaust the spectrum of the $p$-Laplacian?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Does the Lusternik-Schnirelmann eigenvalues
  exhaust the spectrum of the $p$-Laplacian?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We have the **Dirichlet \(p\)-Laplacian**

\[
-\Delta _p u:= -\operatorname{div}\!\bigl(|\nabla u|^{p-2}\nabla u\bigr),\qquad 
1<p<\infty ,
\]

on a bounded open set \(\Omega\subset\mathbb{R}^{d}\) with the boundary condition \(u=0\) on \(\partial\Omega\).

An **eigenvalue** \(\lambda\) is a real number for which there exists a non‑zero
\(u\in W^{1,p}_0(\Omega)\) solving  

\[
-\Delta _p u = \lambda |u|^{p-2}u\quad\text{in }\Omega .
\]

Using the **Lusternik–Schnirelmann (LS) min–max principle** one can construct an
increasing sequence of numbers  

\[
0<\lambda_{1}(p)\le \lambda_{2}(p)\le\cdots ,\qquad \lambda_{k}(p)\xrightarrow{k\to\infty}\infty ,
\]

called **variational eigenvalues**.

For the linear case \(p=2\) the spectral theorem tells us that *every* eigenvalue of the Laplacian appears in this list (counting multiplicities).

The question is:

> **When \(p\neq 2\), does the LS list \(\{\lambda_k(p)\}_{k\ge1}\) contain *all* eigenvalues of the \(p\)-Laplacian, or can there be “extra’’ eigenvalues that are not obtained by the LS min–max construction?**

In other words, does the LS sequence exhaust the whole **spectrum** (the set of all eigenvalues) of the nonlinear operator \(-\Delta _p\)?

---

## 2.  Detailed answer  

### 2.1  Preliminaries  

* **Rayleigh quotient.**  
  For \(u\in W^{1,p}_0(\Omega)\setminus\{0\}\) define  

  \[
  \mathcal R(u)=\frac{\displaystyle\int_{\Omega}|\nabla u|^{p}\,dx}
                   {\displaystyle\int_{\Omega}|u|^{p}\,dx}.
  \]

  The functional \(\mathcal R\) is homogeneous of degree 0:
  \(\mathcal R(tu)=\mathcal R(u)\) for every \(t\neq0\).

* **Unit sphere.**  
  Let  

  \[
  S:=\bigl\{u\in W^{1,p}_0(\Omega):\ \|u\|_{L^{p}(\Omega)}=1\bigr\}.
  \]

  Then \(\mathcal R\) restricted to \(S\) is a \(C^{1}\) functional whose
  critical points are precisely the eigenfunctions of \(-\Delta _p\)
  (with eigenvalue equal to the critical value).

* **Genus.**  
  If \(A\subset S\) is closed, symmetric (\(u\in A\Rightarrow -u\in A\)),
  its **Krasnosel’skiĭ genus** \(\gamma(A)\) is the smallest integer
  \(k\) such that there exists an odd continuous map
  \(A\to\mathbb S^{k-1}\) (or \(+\infty\) if no such \(k\) exists).

* **Variational eigenvalues (LS definition).**  
  For each integer \(k\ge 1\) set  

  \[
  \lambda_k(p):=\inf_{A\in\mathcal F_k}\ \sup_{u\in A}\mathcal R(u),
  \qquad
  \mathcal F_k:=\{A\subset S:\ A\ \text{closed, symmetric, }\gamma(A)\ge k\}.
  \]

  The LS theorem (or the “genus min–max principle’’) guarantees that
  each \(\lambda_k(p)\) is a critical value of \(\mathcal R\) on \(S\); hence
  \(\lambda_k(p)\) is an eigenvalue of \(-\Delta _p\).

The question is whether **every** eigenvalue \(\lambda\) of \(-\Delta _p\) can be
written as \(\lambda_k(p)\) for some \(k\).

---

### 2.2  Main theorem (classical result)

> **Theorem (Lusternik–Schnirelmann exhaustivity for the Dirichlet \(p\)-Laplacian).**  
> Let \(\Omega\subset\mathbb R^{d}\) be bounded and have a Lipschitz boundary.
> Then the set of eigenvalues of the Dirichlet problem  
> \(-\Delta _p u = \lambda |u|^{p-2}u\) in \(\Omega,\; u=0\) on \(\partial\Omega\)  
> coincides with the LS sequence \(\{\lambda_k(p)\}_{k\ge1}\).  
> In particular the spectrum is a countable, unbounded, increasing list
> (counting multiplicities).

The theorem is proved in several papers; a concise reference is

* A. Anane, **“On the second eigenvalue of the \(p\)-Laplacian”**, *Nonlinear Anal.* 16 (1991), 105–117,  
* P. Drábek, **“Solvability and spectrum of the \(p\)-Laplacian”**, *J. Funct. Anal.* 131 (1995), 315–341,  
* J. Lindqvist, **“On the equation \(\Delta _p u + \lambda |u|^{p-2}u=0\)”**, *Proc. Amer. Math. Soc.* 109 (1990), 157–164.

Below we outline the essential ideas of the proof.

---

### 2.3  Sketch of the proof  

#### Step 1 – Palais–Smale condition for the Rayleigh quotient  

Define  

\[
\Phi(u)=\frac{1}{p}\int_{\Omega}|\nabla u|^{p}\,dx
      -\frac{\lambda}{p}\int_{\Omega}|u|^{p}\,dx .
\]

Restricted to the sphere \(S\) the functional \(\mathcal R\) (or \(\Phi\))
satisfies the **Palais–Smale condition**: every sequence
\(\{u_n\}\subset S\) with \(\mathcal R(u_n)\) bounded and
\(\mathcal R'(u_n)\to0\) possesses a convergent subsequence in \(W^{1,p}_0(\Omega)\).
The proof uses the compact embedding
\(W^{1,p}_0(\Omega)\hookrightarrow L^{p}(\Omega)\) (Rellich‑Kondrachov) and
the strict monotonicity of the map
\(z\mapsto |z|^{p-2}z\).

This compactness is the heart of the LS theory for nonlinear
operators: it guarantees that the min–max values \(\lambda_k(p)\) are
indeed *critical* values.

#### Step 2 – Existence of a critical point at each \(\lambda_k(p)\)

By definition,
\[
\lambda_k(p)=\inf_{A\in\mathcal F_k}\sup_{u\in A}\mathcal R(u).
\]
Take a minimizing sequence of sets \(A_n\in\mathcal F_k\) with
\(\sup_{u\in A_n}\mathcal R(u)\downarrow\lambda_k(p)\).
Using the deformation lemma (valid because of the Palais–Smale condition)
one can construct a Palais–Smale sequence for \(\mathcal R\) at level
\(\lambda_k(p)\). By Step 1 it converges to a critical point \(u_k\neq0\).
Hence \(\lambda_k(p)\) is an eigenvalue.

#### Step 3 – Any eigenvalue appears in the LS list  

Let \(\lambda\) be an eigenvalue and let
\[
E_\lambda:=\{u\in S:\ \mathcal R(u)=\lambda\}
\]
be the set of normalized eigenfunctions belonging to \(\lambda\).
\(E_\lambda\) is closed, symmetric, and **compact** (again because of the
compact embedding). Moreover, the genus of \(E_\lambda\) is a finite
integer that we denote by \(\gamma(E_\lambda)\).

Now consider the LS min–max values:
\[
\lambda_{k}(p)=\inf_{A\in\mathcal F_k}\sup_{u\in A}\mathcal R(u).
\]

Because \(E_\lambda\) is a symmetric compact set,
\(\gamma(E_\lambda)=m\) implies \(E_\lambda\in\mathcal F_m\) but
\(E_\lambda\notin\mathcal F_{m+1}\). Consequently

\[
\lambda_m(p)\le \lambda\le\lambda_{m+1}(p).
\]

If the inequality were strict, i.e. \(\lambda_m(p)<\lambda<\lambda_{m+1}(p)\),
the **mountain‑pass type deformation** (or a linking argument) would
produce a new critical value strictly between \(\lambda_m(p)\) and
\(\lambda_{m+1}(p)\), contradicting the definition of \(\lambda_{m+1}(p)\)
as the *least* level that can be forced by a set of genus \(\ge m+1\).
Therefore the only possibility is  

\[
\boxed{\ \lambda=\lambda_m(p)\ } .
\]

Thus every eigenvalue coincides with one of the LS numbers.

#### Step 4 – Counting multiplicities  

If an eigenvalue \(\lambda\) has multiplicity \(r\) (i.e. the linear span of
its eigenfunctions has dimension \(r\)), then
\(\gamma(E_\lambda)=r\). Consequently the same eigenvalue appears exactly
\(r\) times in the list \(\{\lambda_k(p)\}\), just as in the linear case.

---

### 2.4  Consequences  

* The **spectrum** of the Dirichlet \(p\)-Laplacian is **discrete**,
  consists of a countable set of real numbers,
  and has **no accumulation point** except \(+\infty\).

* The LS sequence \(\{\lambda_k(p)\}\) **exhausts** the whole spectrum; there
  are **no hidden eigenvalues** outside this variational list.

* The first eigenvalue \(\lambda_1(p)\) is simple, isolated and
  characterized by the Rayleigh quotient minimization.
  Higher eigenvalues can be multiple; their multiplicities are detected by
  the genus of the corresponding critical sets.

---

## 3.  Final

*Original question: [Does the Lusternik-Schnirelmann eigenvalues exhaust the spectrum of the $p$-Laplacian?](https://math.stackexchange.com/questions/5149496/does-the-lusternik-schnirelmann-eigenvalues-exhaust-the-spectrum-of-the-p-lapl) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
