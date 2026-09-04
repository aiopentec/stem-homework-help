---
layout: question
title: New multi-grade solutions $x_1^k+x_2^k+x_3^k=y_1^k+y_2^k+y_3^k=z_1^k+z_2^k+z_3^k,
  k&lt;5$
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: New multi-grade solutions $x_1^k+x_2^k+x_3^k=y_1^k+y_2^k+y_3^k=z_1^k+z_2^k+z_3^k,
  k&lt;5$'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

We are looking for **three different triples of integers**

\[
(x_{1},x_{2},x_{3}),\qquad (y_{1},y_{2},y_{3}),\qquad (z_{1},z_{2},z_{3})
\]

such that the three *power‑sums* are all the same, namely  

\[
\begin{aligned}
x_{1}^{k}+x_{2}^{k}+x_{3}^{k}&=y_{1}^{k}+y_{2}^{k}+y_{3}^{k}=z_{1}^{k}+z_{2}^{k}+z_{3}^{k}=N\\
&\qquad\text{for every }k=1,2,3,4 .
\end{aligned}
\]

(Only the powers \(k<5\) are required.)  
If such a configuration exists we call it a **multigrade chain of length three** for the exponents
\(k=1,2,3,4\).

The question is: **Do any non‑trivial (i.e. not just a permutation of the same three numbers) solutions exist?**  
If they exist we would like to exhibit at least one, otherwise we would like to prove that none exist.

--------------------------------------------------------------------

## 2.  The complete solution

### 2.1  From power sums to elementary symmetric sums  

For a triple \((a,b,c)\) define the *power sums*

\[
p_k(a,b,c)=a^{k}+b^{k}+c^{k}, \qquad k=1,2,3,4,
\]

and the *elementary symmetric sums*

\[
\begin{aligned}
\sigma_1 &=a+b+c,\\
\sigma_2 &=ab+bc+ca,\\
\sigma_3 &=abc .
\end{aligned}
\]

The three elementary symmetric sums are the coefficients (up to sign) of the monic cubic
\[
\Phi_{a,b,c}(t)= (t-a)(t-b)(t-c)=t^{3}-\sigma_1 t^{2}+\sigma_2 t-\sigma_3 .
\]

The link between the power sums and the elementary symmetric sums is given by **Newton’s identities**:

\[
\begin{aligned}
p_1 &=\sigma_1,\\[2mm]
p_2 &=\sigma_1p_1-2\sigma_2,\\[2mm]
p_3 &=\sigma_1p_2-\sigma_2p_1+3\sigma_3,\\[2mm]
p_4 &=\sigma_1p_3-\sigma_2p_2+\sigma_3p_1 .
\end{aligned}
\tag{1}
\]

These identities hold for *any* numbers \(a,b,c\) (integers, rationals, reals …).

--------------------------------------------------------------------

### 2.2  Equality of the first three power sums forces equality of the elementary sums  

Assume we have **two** triples \((a,b,c)\) and \((d,e,f)\) such that

\[
p_k(a,b,c)=p_k(d,e,f)\quad\text{for }k=1,2,3.
\tag{2}
\]

Denote by \(\sigma_i\) the elementary sums of \((a,b,c)\) and by \(\tau_i\) those of \((d,e,f)\).

From the first line of (1) we obtain immediately  

\[
\sigma_1=p_1(a,b,c)=p_1(d,e,f)=\tau_1 .
\tag{3}
\]

Insert (3) into the second line of (1):

\[
p_2=\sigma_1p_1-2\sigma_2 \quad\Longrightarrow\quad
2\sigma_2 = \sigma_1p_1-p_2 .
\]

Because the right‑hand side is the same for both triples (by (2) and (3)), we get  

\[
\sigma_2 = \tau_2 .
\tag{4}
\]

Now use the third line of (1). With \(\sigma_1=\tau_1\) and \(\sigma_2=\tau_2\) we have

\[
p_3 = \sigma_1p_2-\sigma_2p_1+3\sigma_3
      = \tau_1p_2-\tau_2p_1+3\tau_3 .
\]

Since the left‑hand side is the same for the two triples, we obtain  

\[
3\sigma_3 = 3\tau_3 \;\Longrightarrow\; \sigma_3 = \tau_3 .
\tag{5}
\]

Thus **equality of the first three power sums forces equality of all three elementary symmetric sums**.

--------------------------------------------------------------------

### 2.3  Consequence: the two triples are the same up to order  

If \(\sigma_i=\tau_i\) for \(i=1,2,3\) then the two cubic polynomials are identical:

\[
(t-a)(t-b)(t-c) = t^{3}-\sigma_1t^{2}+\sigma_2t-\sigma_3
               = (t-d)(t-e)(t-f).
\]

Two monic polynomials are equal iff they have the same set of roots (counted with multiplicity).  
Hence the multisets \(\{a,b,c\}\) and \(\{d,e,f\}\) are equal; the three numbers of one triple are just a **permutation** of the three numbers of the other triple.

In particular, any *non‑trivial* triple \((a,b,c)\) cannot have a distinct triple \((d,e,f)\) with the same power sums for \(k=1,2,3\).

--------------------------------------------------------------------

### 2.4  Adding the fourth power – no new information  

If the power sums are already equal for \(k=1,2,3\), the fourth identity in (1) shows that the fourth power sums are automatically equal:

\[
p_4 = \sigma_1p_3-\sigma_2p_2+\sigma_3p_1
\]

and the right‑hand side depends only on \(\sigma_1,\sigma_2,\sigma_3\) and on the already equal power sums \(p_1,p_2,p_3\).  
Therefore the condition for \(k=4\) does **not** introduce any extra restriction; it is a consequence of the first three.

--------------------------------------------------------------------

### 2.5  Extending to three triples  

Suppose we have **three** triples \((x_1,x_2,x_3), (y_1,y_2,y_3), (z_1,z_2,z_3)\) satisfying

\[
p_k(x)=p_k(y)=p_k(z)\qquad\text{for }k=1,2,3,4 .
\tag{6}
\]

Apply the result of §2.3 to the pair \((x)\) and \((y)\): they must be the same multiset.
Apply the same argument to the pair \((x)\) and \((z)\): they also must be the same multiset.
Consequently all three triples consist of the **same three numbers**, perhaps in a different order.

Thus there is **no** way to obtain three *different* triples with the same power‑sums for the exponents \(1,2,3,4\).

--------------------------------------------------------------------

### 2.6  Final statement

> **Theorem.**  
> Let \((a,b,c),(d,e,f),(g,h,i)\) be integer (or rational) triples.  
> If for every \(k=1,2,3,4\)
> \[
> a^{k}+b^{k}+c^{k}=d^{k}+e^{k}+f^{k}=g^{k}+h^{k}+i^{k},
> \]
> then the three triples are identical up to permutation; i.e.  
> \(\{a,b,c\}=\{d,e,f\}=\{g,h,i\}\).

Therefore **non‑trivial multigrade chains of length three do not exist for the exponents \(k<5\)**. The red cells in the table of the original post must stay empty.

--------------------------------------------------------------------

## 3.  Final answer

No non‑trivial integer (or rational) solutions exist for

\[
x_1^k+x_2^k+x_3^k = y_1^k+y_2^k+y_3^k = z_1^k+z_2^k+z_3^k\quad\text{for all }k=1,2,3,4 .
\]

If the equalities hold for the three exponents \(k=1,2,3\) (and consequently for \(k=4\)), the three triples must be the same set of numbers, possibly reordered. Hence a “multigrade chain’’ with three distinct triples cannot be constructed for any \(k<5\).

--------------------------------------------------------------------

## 4.  Common mistakes for this type of problem  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the four equations are independent.** | The fourth power‑sum is a *consequence* of the first three via Newton’s identities; it adds no new condition. | Write down Newton’s identities and check the dependence before trying to solve the system. |
| **Treating the three power‑sum equations as linear in the unknown numbers.** | Power sums are highly non‑linear; linear methods (e.g., Gaussian elimination) are not applicable. | Use symmetric‑function theory (Newton’s identities) to translate the problem into statements about elementary symmetric sums. |
| **Searching for solutions by brute force without using the symmetry.** | The search space grows explosively (≈ \(N^{3}\) for numbers up to size \(N\)). | First prove that a non‑trivial solution cannot exist; then a brute‑force search is unnecessary. |
| **Confusing “different triples’’ with “different orderings’’** | Permuting the entries of a triple does not give a new solution; it is the same multiset. | After obtaining equal elementary symmetric sums, conclude that the sets of numbers are identical, regardless of order. |
| **Neglecting the possibility of repeated numbers (e.g., \(a=b\)).** | Repeated entries still satisfy the same symmetric‑function relations; the proof works for any multiplicities. | Keep the proof general; no assumption about distinctness is needed. |

By keeping these points in mind, one can avoid dead‑ends and reach the decisive conclusion that multigrade chains of length three for \(k=1,2,3,4\) are impossible.

*Original question: [New multi-grade solutions $x_1^k+x_2^k+x_3^k=y_1^k+y_2^k+y_3^k=z_1^k+z_2^k+z_3^k, k&lt;5$](https://math.stackexchange.com/questions/5148623/new-multi-grade-solutions-x-1kx-2kx-3k-y-1ky-2ky-3k-z-1kz-2kz-3k) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
