---
layout: question
title: How to show that $e^{a_1 z} ,...,e^{a_n z}$ is Linearly independent over $\mathbb{C}$
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: How to show that $e^{a_1 z} ,...,e^{a_n
  z}$ is Linearly independent over $\mathbb{C}$'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem asks  

We are given **distinct** complex numbers  

\[
a_{1},a_{2},\dots ,a_{n}\in\mathbb C ,\qquad a_i\neq a_j\;(i\neq j),
\]

and we consider the functions  

\[
f_i(z)=e^{a_i z}\qquad (i=1,\dots ,n)
\]

defined on the whole complex plane.  
The task is to prove that these \(n\) functions are *linearly independent* over \(\mathbb C\); i.e.

\[
c_{1}e^{a_{1}z}+c_{2}e^{a_{2}z}+\dots +c_{n}e^{a_{n}z}=0\quad\text{for all }z\in\mathbb C
\Longrightarrow c_{1}=c_{2}= \dots =c_{n}=0 .
\]

In other words, the only linear combination of the exponentials that vanishes identically is the trivial one.



--------------------------------------------------------------------

## 2.  Full proof  

We give two proofs; you may keep the one you find most convenient.

### Proof A – Using the *Wronskian* (determinant of derivatives)

For \(k\ge 0\) let  

\[
f_i^{(k)}(z)=\frac{d^{\,k}}{dz^{k}}e^{a_i z}=a_i^{\,k}e^{a_i z}.
\]

Form the \(n\times n\) Wronskian matrix  

\[
W(z)=\Bigl[f_i^{(j-1)}(z)\Bigr]_{\,i,j=1}^{n}
     =\begin{pmatrix}
        e^{a_1z} & e^{a_2z} & \dots & e^{a_nz}\\[2pt]
        a_1e^{a_1z}& a_2e^{a_2z}& \dots & a_ne^{a_nz}\\[2pt]
        \vdots & \vdots & & \vdots\\[2pt]
        a_1^{\,n-1}e^{a_1z}& a_2^{\,n-1}e^{a_2z}&\dots & a_n^{\,n-1}e^{a_nz}
      \end{pmatrix}.
\]

Factor out the exponentials from each column:

\[
W(z)=\bigl(\operatorname{diag}(e^{a_1z},\dots ,e^{a_nz})\bigr)\,
      V,\qquad 
V=\begin{pmatrix}
   1&1&\dots &1\\
   a_1&a_2&\dots &a_n\\
   \vdots&\vdots&&\vdots\\
   a_1^{\,n-1}&a_2^{\,n-1}&\dots &a_n^{\,n-1}
  \end{pmatrix}.
\]

The matrix \(V\) is the **Vandermonde matrix** built from the numbers \(a_1,\dots ,a_n\).  
Its determinant is well‑known:

\[
\det V=\prod_{1\le i<j\le n}(a_j-a_i).
\]

Because the \(a_i\) are distinct, every factor \((a_j-a_i)\) is non‑zero, hence  

\[
\det V\neq 0 .
\]

Now  

\[
\det W(z)=\Bigl(\prod_{i=1}^{n}e^{a_i z}\Bigr)\det V
          =\Bigl(\prod_{i=1}^{n}e^{a_i z}\Bigr)\,
            \prod_{1\le i<j\le n}(a_j-a_i)\neq 0
\]

for **every** \(z\in\mathbb C\) (the product of exponentials is never zero).  
Thus the Wronskian of the functions \(e^{a_1z},\dots ,e^{a_nz}\) never vanishes.

A standard result from the theory of linear ordinary differential equations (or directly from the definition of linear independence for analytic functions) says:

> If the Wronskian of a set of analytic functions is not identically zero on a domain, the functions are linearly independent on that domain.

Consequently the exponentials are linearly independent on \(\mathbb C\).

---

### Proof B – Using derivatives at a single point (often \(z=0\))

Assume a linear relation

\[
c_{1}e^{a_{1}z}+c_{2}e^{a_{2}z}+\dots +c_{n}e^{a_{n}z}=0\qquad(\forall z\in\mathbb C).
\]

Differentiate \(k\) times and then set \(z=0\).  
Because \(\frac{d^{k}}{dz^{k}}e^{a_i z}=a_i^{k}e^{a_i z}\), we obtain for every \(k\ge 0\)

\[
c_{1}a_{1}^{k}+c_{2}a_{2}^{k}+ \dots +c_{n}a_{n}^{k}=0 .
\tag{1}
\]

Take the first \(n\) equations, i.e. for \(k=0,1,\dots ,n-1\).  
Written in matrix form they read

\[
\begin{pmatrix}
1&1&\dots &1\\
a_{1}&a_{2}&\dots &a_{n}\\
\vdots &\vdots &&\vdots\\
a_{1}^{\,n-1}&a_{2}^{\,n-1}&\dots &a_{n}^{\,n-1}
\end{pmatrix}
\begin{pmatrix}
c_{1}\\c_{2}\\ \vdots \\c_{n}
\end{pmatrix}
=
\begin{pmatrix}
0\\0\\ \vdots \\0
\end{pmatrix}.
\]

Again the matrix on the left is the Vandermonde matrix \(V\).  
Since the \(a_i\) are pairwise distinct, \(\det V\neq 0\); therefore the only solution of this homogeneous linear system is  

\[
c_{1}=c_{2}= \dots =c_{n}=0 .
\]

Thus the assumed linear relation forces every coefficient to be zero, proving linear independence.

---

Both arguments rely on the fact that the **Vandermonde determinant** is non‑zero precisely when the parameters \(a_{1},\dots ,a_{n}\) are distinct.  

--------------------------------------------------------------------

## 3.  Final statement  

For distinct complex numbers \(a_{1},\dots ,a_{n}\) the functions  

\[
e^{a_{1}z},\;e^{a_{2}z},\dots ,e^{a_{n}z}\qquad (z\in\mathbb C)
\]

are linearly independent over \(\mathbb C\).  
Equivalently, if  

\[
c_{1}e^{a_{1}z}+c_{2}e^{a_{2}z}+\dots +c_{n}e^{a_{n}z}\equiv 0,
\]

then necessarily \(c_{1}=c_{2}= \dots =c_{n}=0\).

--------------------------------------------------------------------

## 4.  Common mistakes to avoid  

| Mistake | Why it is wrong | How to correct it |
|---------|----------------|-------------------|
| **Assuming the relation holds only for some values of \(z\)** | Linear independence concerns equality *for all* \(z\) in the domain. A relation that vanishes at finitely many points does **not** imply dependence. | Explicitly state that the equality holds for **every** complex number \(z\). |
| **Trying to “cancel” exponentials** (e.g. dividing by \(e^{a_1z}\)) | The cancellation is illegal when the exponentials have different exponents; you cannot factor a common term out of a sum. | Work with derivatives or the Wronskian, or evaluate the identity at several points, rather than attempting to factor out an exponential. |
| **Using the Vandermonde determinant without justification** | One must recognise that the matrix formed by the coefficients after differentiating is exactly a Vandermonde matrix, and recall its determinant formula. | Write down the matrix explicitly, point out it is a Vandermonde matrix, and quote \(\det V=\prod_{i<j}(a_j-a_i)\). |
| **Confusing linear independence over \(\mathbb C\) with pointwise independence** | Linear independence means no *global* linear combination is identically zero, not that the functions take different values at each point. | Emphasise the definition: a linear combination that vanishes **identically** (as a function) forces all coefficients to be zero. |
| **Neglecting the case where some \(a_i\) coincide** | If two exponents are equal, the corresponding exponentials are the same function, so they are automatically dependent. | The hypothesis “\(a_i\) are distinct” is essential; make it clear that the proof uses \(\det V\neq 0\) which fails when two \(a_i\) coincide. |

Keeping these points in mind will help you construct a rigorous and clean argument.

*Original question: [How to show that $e^{a_1 z} ,...,e^{a_n z}$ is Linearly independent over $\mathbb{C}$](https://math.stackexchange.com/questions/5149075/how-to-show-that-ea-1-z-ea-n-z-is-linearly-independent-over-mathb) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
