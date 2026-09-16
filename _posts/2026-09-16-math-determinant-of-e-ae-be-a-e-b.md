---
layout: question
title: Determinant of $e^Ae^Be^{-A}e^{-B}$
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Determinant of $e^Ae^Be^{-A}e^{-B}$'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  Restating the problem in plain language  

We are asked to verify the identity  

\[
\operatorname{Det}\!\bigl(e^{A}\,e^{B}\,e^{-A}\,e^{-B}\bigr)=\exp\!\bigl(\operatorname{Tr}[A,B]\bigr),
\qquad [A,B]=AB-BA,
\]

when \(A\) and \(B\) are **finite‑dimensional matrices** (say \(n\times n\) complex matrices).  

The symbol “\(\operatorname{Det}\)” denotes the ordinary matrix determinant, and \(\operatorname{Tr}\) is the usual trace.  
The question is whether the formula holds for any two matrices, or only under extra hypotheses (for instance, when \([A,B]\) is a scalar multiple of the identity).

---

## 2.  Detailed solution  

### 2.1.  Two elementary facts  

1. **Determinant of an exponential**  
   For any square matrix \(X\),

   \[
   \det(e^{X}) = e^{\operatorname{Tr}X}.
   \]

   *Proof.* Write the Jordan (or Schur) decomposition \(X = SJS^{-1}\) with \(J\) upper‑triangular. Then \(e^{X}=Se^{J}S^{-1}\) and \(\det(e^{X})=\det(e^{J})\).  
   Since \(e^{J}\) is also upper‑triangular and its diagonal entries are \(e^{\lambda_i}\) where \(\lambda_i\) are the eigenvalues of \(X\), we have  

   \[
   \det(e^{J})=\prod_i e^{\lambda_i}=e^{\sum_i\lambda_i}=e^{\operatorname{Tr}X}.
   \]

2. **Cyclicity of the trace**  
   For any two matrices \(X,Y\),

   \[
   \operatorname{Tr}(XY)=\operatorname{Tr}(YX).
   \]

   Consequently, \(\operatorname{Tr}[A,B]=\operatorname{Tr}(AB)-\operatorname{Tr}(BA)=0\).

### 2.2.  Computing the left‑hand side  

Using the multiplicativity of the determinant together with fact 1:

\[
\begin{aligned}
\det\!\bigl(e^{A}e^{B}e^{-A}e^{-B}\bigr)
&= \det(e^{A})\;\det(e^{B})\;\det(e^{-A})\;\det(e^{-B}) \\[4pt]
&= e^{\operatorname{Tr}A}\;e^{\operatorname{Tr}B}\;e^{-\operatorname{Tr}A}\;e^{-\operatorname{Tr}B} \\[4pt]
&= 1.
\end{aligned}
\]

Thus the determinant of the product is **always** equal to \(1\), no matter what \(A\) and \(B\) are.

### 2.3.  Computing the right‑hand side  

From fact 2 we have  

\[
\operatorname{Tr}[A,B]=\operatorname{Tr}(AB)-\operatorname{Tr}(BA)=0,
\]

hence  

\[
\exp\!\bigl(\operatorname{Tr}[A,B]\bigr)=\exp(0)=1.
\]

### 2.4.  Comparing the two sides  

Both sides equal \(1\); therefore the identity

\[
\boxed{\displaystyle 
\det\!\bigl(e^{A}e^{B}e^{-A}e^{-B}\bigr)=\exp\!\bigl(\operatorname{Tr}[A,B]\bigr)
}
\]

holds **for every pair of finite‑dimensional matrices** \(A,B\).  
The statement is true but completely trivial in the finite‑dimensional setting because \(\operatorname{Tr}[A,B]=0\).

### 2.5.  Why the formula is interesting in infinite dimensions  

When \(A\) and \(B\) act on an infinite‑dimensional Hilbert space, the ordinary determinant is no longer defined. One replaces it by the **Fredholm (or regularized) determinant** \(\operatorname{Det}\), which is multiplicative only under special circumstances.  
If the commutator \([A,B]\) belongs to the trace‑class ideal, the regularized determinant satisfies  

\[
\operatorname{Det}\!\bigl(e^{A}e^{B}e^{-A}e^{-B}\bigr)=\exp\!\bigl(\operatorname{Tr}[A,B]\bigr),
\]

a non‑trivial result proved by Pincus, Helton, Howe and others.  
For finite matrices the regularized determinant coincides with the ordinary determinant, and the formula collapses to the trivial identity proved above.

---

## 3.  Final answer  

Yes, the formula is **true for all finite matrices** \(A,B\).  
Both sides equal \(1\) because  

* \(\det(e^{X}) = e^{\operatorname{Tr}X}\) gives \(\det(e^{A}e^{B}e^{-A}e^{-B}) = 1\);
* \(\operatorname{Tr}[A,B]=0\) for any pair of matrices, so \(\exp(\operatorname{Tr}[A,B]) = 1\).

Hence the equality holds, albeit in a completely elementary way.

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming \(\operatorname{Tr}[A,B]\neq0\)** for finite matrices. | The trace of any commutator is zero by cyclicity of the trace. | Remember the identity \(\operatorname{Tr}(AB)=\operatorname{Tr}(BA)\). |
| **Using \(\det(AB)=\det(A)\det(B)\) without checking dimensions**. | The multiplicative property holds only for square matrices of the same size. | Verify that all matrices involved are \(n\times n\). |
| **Confusing the ordinary determinant with the Fredholm determinant**. | In infinite dimensions the ordinary determinant is undefined; the quoted formula is about the regularized determinant. | Keep the context clear: for finite matrices the two determinants coincide, making the formula trivial. |
| **Omitting the step \(\det(e^{X}) = e^{\operatorname{Tr}X}\)**. | Without this property the computation cannot be finished. | Prove or cite the exponential‑determinant identity (e.g., via Jordan/Schur form). |
| **Trying to expand the product \(e^{A}e^{B}e^{-A}e^{-B}\) via the Baker–Campbell–Hausdorff formula**. | That expansion is unnecessary and leads to cumbersome higher‑order commutators. | Use the determinant and trace properties directly; they give the result instantly. |

By keeping these points in mind, the problem becomes a straightforward application of two basic linear‑algebra identities.

*Original question: [Determinant of $e^Ae^Be^{-A}e^{-B}$](https://math.stackexchange.com/questions/5149476/determinant-of-eaebe-ae-b) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
