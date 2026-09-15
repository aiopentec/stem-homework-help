---
layout: question
title: How to find $\eta$, $\eta&#39;$ and $\xi$ for a repeated root in a system of
  linear differential equations?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: How to find $\eta$, $\eta&#39;$ and
  $\xi$ for a repeated root in a system of linear differential equations?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We have the linear system  

\[
\frac{d}{dt}\begin{pmatrix}x\\y\end{pmatrix}=A\begin{pmatrix}x\\y\end{pmatrix},
\qquad 
A=\begin{pmatrix}3&-4\\[2pt]1&-1\end{pmatrix}.
\]

The characteristic polynomial of \(A\) is  

\[
\det(A-\lambda I)=\lambda ^2-2\lambda+1=(\lambda-1)^2,
\]

so the only eigenvalue is the **repeated** root \(\lambda =1\) (algebraic multiplicity 2).  

Because there is only **one** linearly‑independent eigenvector, the matrix is not diagonalizable.  
The teacher wrote the two independent solutions in the form  

\[
X(t)=\eta e^{t}, \qquad   
Y(t)=(\eta'+\xi t)\,e^{t},
\]

and gave the vectors  

\[
\eta=\begin{pmatrix}2\\1\end{pmatrix},\qquad 
\eta'=\begin{pmatrix}0\\-1\end{pmatrix},\qquad 
\xi=\begin{pmatrix}2\\1\end{pmatrix}.
\]

We have to **show how these vectors are obtained** and explain how the same procedure works for any linear system that has a repeated eigenvalue.

--------------------------------------------------------------------

## 2.  Step‑by‑step construction for the given 2 × 2 system  

### 2.1  Find the eigenvector \(\eta\)

Solve  

\[
(A-\lambda I)\eta =0\qquad\text{with }\lambda =1 .
\]

\[
A-I = \begin{pmatrix}3-1 & -4 \\ 1 & -1-1\end{pmatrix}
     =\begin{pmatrix}2&-4\\ 1&-2\end{pmatrix}.
\]

The linear equations are  

\[
\begin{cases}
2\eta_1-4\eta_2 = 0\\
\eta_1-2\eta_2 = 0
\end{cases}
\Longrightarrow \eta_1 = 2\eta_2 .
\]

Choosing \(\eta_2=1\) we obtain the (non‑zero) eigenvector  

\[
\boxed{\;\eta=\begin{pmatrix}2\\1\end{pmatrix}\;}
\]

(any non‑zero scalar multiple would be equally acceptable).

---

### 2.2  Find a *generalised* eigenvector \(\eta'\)

Because the geometric multiplicity is 1, we need a second vector that satisfies  

\[
(A-\lambda I)\,\eta' = \eta .
\tag{1}
\]

Write \(\eta' =\begin{pmatrix}a\\b\end{pmatrix}\).  
Using the same matrix \(A-I\),

\[
\begin{pmatrix}2&-4\\ 1&-2\end{pmatrix}
\begin{pmatrix}a\\b\end{pmatrix}
=
\begin{pmatrix}2\\1\end{pmatrix}.
\]

This gives the linear system  

\[
\begin{cases}
2a-4b = 2\\
a-2b = 1 .
\end{cases}
\]

Both equations are the same, so we have one degree of freedom.  
Pick the convenient value \(a=0\); then  

\[
-2b = 1 \quad\Longrightarrow\quad b=-\frac12 .
\]

Thus one possible generalized eigenvector is  

\[
\eta'_0=\begin{pmatrix}0\\-\dfrac12\end{pmatrix}.
\]

Any scalar multiple of a solution of (1) is also a solution, because if
\((A-\lambda I)\eta'_0=\eta\) then \((A-\lambda I)(c\eta'_0)=c\eta\).
Multiplying the vector by \(2\) gives the teacher’s choice  

\[
\boxed{\;\eta'=\begin{pmatrix}0\\-1\end{pmatrix}\;}
\]

(which satisfies \((A-I)\eta' = 2\eta\); the extra factor \(2\) is absorbed by the arbitrary constant that multiplies the second solution).

---

### 2.3  Identify \(\xi\)

For a \(2\times2\) Jordan block the polynomial in front of \(t\) is **exactly the eigenvector** that generated the chain.  
Hence  

\[
\boxed{\;\xi = \eta = \begin{pmatrix}2\\1\end{pmatrix}\;}
\]

(the teacher wrote it separately only to emphasise the role of the \(t\)-term).

---

### 2.4  Write the two independent solutions

With the vectors found above the two linearly independent solutions are  

\[
\begin{aligned}
X_1(t) &= \eta \,e^{t}
        = \begin{pmatrix}2\\1\end{pmatrix}e^{t},\\[4pt]
X_2(t) &= (\eta' + t\,\xi )e^{t}
        =\Bigl(\begin{pmatrix}0\\-1\end{pmatrix}
               +t\begin{pmatrix}2\\1\end{pmatrix}\Bigr)e^{t}.
\end{aligned}
\]

The **general solution** of the system is therefore  

\[
\boxed{
\begin{pmatrix}x(t)\\ y(t)\end{pmatrix}
=
c_1\begin{pmatrix}2\\1\end{pmatrix}e^{t}
+
c_2\Bigl(\begin{pmatrix}0\\-1\end{pmatrix}
          +t\begin{pmatrix}2\\1\end{pmatrix}\Bigr)e^{t}},\qquad
c_1,c_2\in\mathbb{R}.
\]

--------------------------------------------------------------------

## 3.  Generalisation to an \(n\times n\) system  

Consider  

\[
\dot{\mathbf{x}} = A\mathbf{x},\qquad A\in\mathbb{R}^{n\times n}.
\]

### 3.1  Eigenvalues and algebraic multiplicity  

Find the characteristic polynomial \(\det(A-\lambda I)=0\).  
If an eigenvalue \(\lambda\) has algebraic multiplicity \(m\) (it appears \(m\) times as a root) we must check its **geometric multiplicity** – the dimension of \(\ker(A-\lambda I)\).

* If the geometric multiplicity equals \(m\) we obtain \(m\) independent eigenvectors and the matrix is diagonalizable; the solutions are simply \(e^{\lambda t}\) times those eigenvectors.

* If the geometric multiplicity is smaller (the case of a **repeated root** with fewer eigenvectors), we need **generalised eigenvectors**.

### 3.2  Jordan chains (generalised eigenvectors)

A **Jordan chain** of length \(k\) for eigenvalue \(\lambda\) is a sequence of vectors  

\[
v_1,\;v_2,\;\dots,\;v_k
\]

that satisfy  

\[
\begin{aligned}
(A-\lambda I)v_1 &= 0 &&\text{(ordinary eigenvector)}\\
(A-\lambda I)v_2 &= v_1\\
(A-\lambda I)v_3 &= v_2\\
&\ \vdots\\
(A-\lambda I)v_k &= v_{k-1}.
\end{aligned}
\]

The chain is built by solving successive linear systems.  
Because each new equation is linear, it always has a solution (the matrix
\((A-\lambda I)\) is singular, but the right‑hand side lies in its column space by construction).

For a given eigenvalue the sum of the lengths of all Jordan chains equals its algebraic multiplicity.

### 3.3  Solutions associated with a chain  

If a chain has length \(k\) the associated linearly independent solutions are  

\[
e^{\lambda t}\bigl(v_1\bigr),\qquad
e^{\lambda t}\bigl(v_2 + t v_1\bigr),\qquad
e^{\lambda t}\bigl(v_3 + t v_2 + \tfrac{t^{2}}{2!}v_1\bigr),\; \dots,\;
e^{\lambda t}\bigl(v_k + t v_{k-1} + \tfrac{t^{2}}{2!}v_{k-2} + \cdots + \tfrac{t^{k-1}}{(k-1)!}v_1\bigr).
\]

In other words, a chain of length \(k\) contributes a factor \(t^{j}\) (with \(j=0,\dots ,k-1\)) multiplied by the appropriate vector in the chain, all multiplied by the common factor \(e^{\lambda t}\).

### 3.4  Algorithmic recipe  

1. **Compute eigenvalues** \(\lambda\).  
2. **For each eigenvalue**  
   * Find a basis of \(\ker(A-\lambda I)\) → eigenvectors \(\{v^{(1)}_1,\dots ,v^{(p)}_1\}\).  
   * If the algebraic multiplicity \(m>p\), build \(m-p\) additional vectors by solving  
     \((A-\lambda I)v^{(r)}_2 = v^{(r)}_1\) (choose any eigenvector on the right‑hand side), then  
     \((A-\lambda I)v^{(r)}_3 = v^{(r)}_2\), etc., until the required total of \(m\) vectors is reached.  
3. **Write the solution** as the sum of all terms \(e^{\lambda t}\) times the polynomial‑in‑\(t\) expressions described above, with arbitrary constants in front of each independent term.

--------------------------------------------------------------------

## 4.  Common mistakes and how to avoid them  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the matrix is diagonalizable** just because the characteristic polynomial has a repeated root. | A repeated root may have only one eigenvector (as in this problem). | Always

*Original question: [How to find $\eta$, $\eta&#39;$ and $\xi$ for a repeated root in a system of linear differential equations?](https://math.stackexchange.com/questions/5149479/how-to-find-eta-eta-and-xi-for-a-repeated-root-in-a-system-of-linear) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
