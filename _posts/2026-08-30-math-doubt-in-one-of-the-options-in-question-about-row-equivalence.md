---
layout: question
title: Doubt in one of the options in question about row equivalence
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Doubt in one of the options in question
  about row equivalence'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We are given a \(4\times4\) matrix \(A\) that is *row‑equivalent* to  

\[
B=\begin{bmatrix}
1&0&2&0\\[2pt]
0&1&1&0\\[2pt]
0&0&0&1\\[2pt]
0&0&0&0
\end{bmatrix}.
\]

Four statements are offered; we have to decide which one **must be true** for every matrix \(A\) that is row‑equivalent to \(B\).

The statements are  

| Letter | Claim |
|--------|-------|
| A | “\(B\) is **not** the reduced row‑echelon form (RREF) of \(A\).” |
| B | “\(\det(A)\neq0\).” |
| C | “\(\dim\bigl(\operatorname{Null}(A)\bigr)=3\).” |
| D | “If the system \(A\mathbf x=\mathbf b\) is consistent for some non‑zero \(\mathbf b\), then it has infinitely many solutions.” |

We must examine each claim using the information that \(A\) and \(B\) are row‑equivalent.

---

## 2.  Preliminary facts about row‑equivalence  

* Row‑equivalent matrices have the **same rank**.  
* The rank of a matrix equals the number of leading‑1’s (pivots) in its RREF.  
* For an \(m\times n\) matrix,
  \[
  \text{nullity}(A)=n-\operatorname{rank}(A)\qquad\text{(Rank–Nullity Theorem)}.
  \]  
* The RREF of a matrix is **unique**. If a matrix \(B\) is already in RREF, then \(B\) *is* the RREF of every matrix row‑equivalent to it.

So we first determine the rank of \(B\) (hence of \(A\)) and check whether \(B\) itself satisfies the definition of RREF.

---

## 3.  Is \(B\) in reduced row‑echelon form?  

Recall the definition of RREF:

1. All zero rows (if any) are at the bottom.  
2. The first non‑zero entry in each non‑zero row (the **leading entry**) is a 1.  
3. Each leading 1 is the **only** non‑zero entry in its column.  
4. The leading 1 of a lower row lies to the right of the leading 1 of the row above it.

Check \(B\) row by row.

| Row | Leading entry | Column of leading 1 |
|-----|---------------|----------------------|
| 1   | 1             | 1                    |
| 2   | 1             | 2                    |
| 3   | 1             | 4                    |
| 4   | (zero row)    | –                    |

* Condition 1: the zero row is indeed the last row.  
* Condition 2: each non‑zero row starts with a 1.  
* Condition 3: the columns containing the leading 1’s are columns 1, 2, 4. In each of those columns the only non‑zero entry is the leading 1 itself. (Column 3 has non‑zero entries, but it **does not** contain a leading 1, which is allowed.)  
* Condition 4: the leading‑1 columns progress strictly to the right: \(1<2<4\).

All four conditions are satisfied, so **\(B\) **is** already in reduced row‑echelon form**. Because the RREF of a matrix is unique, the RREF of any matrix row‑equivalent to \(B\) is precisely \(B\) itself.

Consequently, statement **A** (“\(B\) is *not* the RREF of \(A\)”) is **false**.

---

## 4.  Rank, determinant, and nullity  

From the RREF we see three pivots (in columns 1, 2, 4). Hence  

\[
\operatorname{rank}(A)=\operatorname{rank}(B)=3.
\]

### 4.1  Determinant (Statement B)

A square matrix is invertible (and thus has non‑zero determinant) **iff** its rank equals its size. Here \(\operatorname{rank}(A)=3<4\), so \(A\) is singular and  

\[
\det(A)=0.
\]

Therefore **B** (“\(\det(A)\neq0\)”) is **false**.

### 4.2  Dimension of the null space (Statement C)

The nullity (dimension of the null space) is

\[
\text{nullity}(A)=n-\operatorname{rank}(A)=4-3=1.
\]

Thus the null space of \(A\) is **one‑dimensional**, not three‑dimensional.  
Statement **C** is **false**.

---

## 5.  Consistency and number of solutions (Statement D)

Because \(\operatorname{rank}(A)=3<4\), the system \(A\mathbf x=\mathbf b\) (if consistent) will always have **one free variable**. A free variable produces infinitely many solutions.

To see this explicitly, solve the equivalent system \(B\mathbf x=\mathbf b\):

\[
\begin{cases}
x_1+2x_3 = b_1,\\[2pt]
x_2 +   x_3 = b_2,\\[2pt]
x_4 = b_3,\\[2pt]
0   = b_4 .
\end{cases}
\]

* Consistency forces \(b_4=0\); the other three components of \(\mathbf b\) can be arbitrary.  
* Variable \(x_3\) does **not** appear as a leading variable, so we may choose it freely.  
* Once a value for \(x_3\) is selected, the equations determine \(x_1, x_2, x_4\) uniquely.

Hence for any non‑zero \(\mathbf b\) with \(b_4=0\) the system is consistent and admits infinitely many solutions (parameterised by the free variable \(x_3\)).

Therefore **Statement D is true**.

---

## 6.  Final answer  

| Letter | True / False | Reason |
|--------|--------------|--------|
| A | **False** | \(B\) *is* already in reduced row‑echelon form, so it *is* the RREF of \(A\). |
| B | **False** | \(\operatorname{rank}(A)=3<4\) ⇒ \(\det(A)=0\). |
| C | **False** | Nullity \(=4-\operatorname{rank}=1\), not 3. |
| **D** | **True** | Rank \(=3\) gives one free variable; any consistent system therefore has infinitely many solutions. |

**The only statement that must be true is D.**  

---

## 7.  Common mistakes for this type of problem  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking any non‑pivot column must be zero** | RREF only requires that *pivot* columns have a single 1; non‑pivot columns may contain arbitrary numbers. | Verify the four RREF conditions directly; ignore the entries in free‑variable columns. |
| **Confusing “rank = 4” with “determinant ≠ 0”** | A \(4\times4\) matrix has non‑zero determinant **iff** its rank is 4. Forgetting this leads to wrong conclusions about invertibility. | Compute rank from the RREF first; then decide about the determinant. |
| **Using rank = 3 to claim the null space has dimension 3** | Nullity = \(n - \text{rank}\); for a \(4\times4\) matrix this is \(4-3=1\). | Apply the Rank–Nullity Theorem explicitly. |
| **Assuming a consistent system can have a unique solution when the number of variables exceeds the rank** | Uniqueness requires rank = number of variables. With rank < variables there is at least one free variable, giving infinitely many solutions. | Check the relationship rank vs \(n\) before deciding about uniqueness vs. infinity. |
| **Ignoring the zero‑row condition in RREF

*Original question: [Doubt in one of the options in question about row equivalence](https://math.stackexchange.com/questions/5148223/doubt-in-one-of-the-options-in-question-about-row-equivalence) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
