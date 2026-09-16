---
layout: question
title: 0K boundary condition for temperature Green&#39;s function
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: 0K boundary condition for temperature
  Green&#39;s function'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the problem is asking

In the Matsubara (imaginary‑time) formalism the **thermal Green function** of a set of operators  
\[
A_{1}(\tau _1),A_{2}(\tau _2),\dots ,A_{n}(\tau _n)
\qquad (0<\tau_i\le\beta )
\]
is defined as  

\[
G(\tau _1,\dots ,\tau _n)=\frac{1}{Z}\,
\operatorname{Tr}\!\Big[ e^{-\beta H}\,
T_\tau\big\{A_{1}(\tau _1)\cdots A_{n}(\tau _n)\big\}\Big] ,
\qquad 
Z=\operatorname{Tr}e^{-\beta H}.
\]

Rickayzen states that **if one of the times is equal to the end‑point of the interval,**
\[
\tau_i =0\quad\text{or}\quad \tau_i=\beta ,
\]
then the Green function satisfies the *boundary condition*

\[
\boxed{ \; G(\tau _1,\dots ,0,\dots ,\tau _n)=
-\;\epsilon\; G(\tau _1,\dots ,\beta ,\dots ,\tau _n)\; } 
\tag{1}
\]

where  

* \(\epsilon =+1\) for **bosonic** operators (they commute)  
* \(\epsilon =-1\) for **fermionic** operators (they anticommute).

The question is: *Why does (1) hold for **any** number of operators?*  
The asker tried a concrete example with three operators and seemed to obtain a contradiction. The resolution lies in a careful use of the **cyclic property of the trace** together with the (anti)‑periodicity of Heisenberg operators in imaginary time.

---

## 2.  Step‑by‑step derivation

### 2.1  Definition of the thermal Green function

Write the Green function explicitly:

\[
G(\tau _1,\dots ,\tau _n)=\frac{1}{Z}
\operatorname{Tr}\!\Big[ e^{-\beta H}\,
T_\tau\big\{A_{1}(\tau _1)\cdots A_{n}(\tau _n)\big\}\Big].
\tag{2}
\]

The **time‑ordering operator** \(T_\tau\) orders the factors from *later* to *earlier* imaginary times:
\[
T_\tau\{A_{i_1}(\tau_{i_1})\cdots A_{i_n}(\tau_{i_n})\}
=
\epsilon^{p}\,
A_{j_1}(\tau_{j_1})\cdots A_{j_n}(\tau_{j_n}),
\]
where \(\tau_{j_1}\ge \tau_{j_2}\ge\cdots\ge\tau_{j_n}\) and  
\(p\) is the number of **pairwise interchanges of fermionic operators** that are needed to bring the arguments into that order.  
Thus each interchange of two fermionic operators contributes a factor \(-1\); interchanges of bosonic operators do nothing.  
In compact form we write the overall sign as \(\epsilon^{p}\) with

\[
\epsilon = \begin{cases}
+1 & \text{bosons (commuting)}\\[2pt]
-1 & \text{fermions (anticommuting)}.
\end{cases}
\tag{3}
\]

### 2.2  The Heisenberg picture in imaginary time

For any operator \(A\) in the Heisenberg picture

\[
A(\tau)=e^{\tau H} A\, e^{-\tau H},\qquad 0\le\tau\le\beta .
\tag{4}
\]

Consequently

\[
A(\beta)=e^{\beta H} A e^{-\beta H}.
\tag{5}
\]

Insert (5) into the trace:

\[
e^{-\beta H} A(0)=e^{-\beta H}A
= A(\beta) e^{-\beta H}.
\tag{6}
\]

No extra sign appears in (6); the sign will come from the **cyclic property of the trace**.

### 2.3  Cyclic property of the trace for fermionic/bosonic operators

For an ordinary (bosonic) operator \(B\),

\[
\operatorname{Tr}(XY)=\operatorname{Tr}(YX).
\]

If **one** of the operators, say \(X\), is **fermionic** (i.e. it contains an odd number of fermionic creation/annihilation operators) then moving it through another fermionic operator picks up a minus sign:

\[
\operatorname{Tr}\big( X Y \big)= -\,\operatorname{Tr}\big( Y X \big)
\qquad\text{if both \(X\) and \(Y\) are fermionic}.
\tag{7}
\]

More generally, when we move a **single fermionic operator** past a **product of operators** that contains an **odd** number of fermionic factors, we acquire a factor \(\epsilon=-1\); if the product contains an **even** number of fermionic factors the sign is \(+1\).  
This is precisely the factor \(\epsilon\) appearing in (1).

### 2.4  Moving the operator at \(\tau_i=0\) to the back of the trace

Assume that the \(k^{\text{th}}\) argument of the Green function is the one we want to replace:
\[
\tau_k =0 .
\]

Write the definition (2) with the operators explicitly ordered **before** the time‑ordering symbol:

\[
G(\ldots ,0,\ldots)=\frac{1}{Z}
\operatorname{Tr}\!\Big[ e^{-\beta H}\,
T_\tau\{ \ldots A_k(0) \ldots\}\Big].
\tag{8}
\]

Using (6) we replace \(A_k(0)\) by \(A_k(\beta)\) **to the left of the trace**:

\[
e^{-\beta H}A_k(0)=A_k(\beta) e^{-\beta H}.
\]

Hence

\[
G(\ldots ,0,\ldots)=\frac{1}{Z}
\operatorname{Tr}\!\Big[ A_k(\beta)\,
e^{-\beta H}\,
T_\tau\{ \ldots\}\Big].
\tag{9}
\]

Now we **cyclically permute** the factor \(A_k(\beta)\) from the leftmost position to the rightmost position of the trace.  
During this permutation we have to move \(A_k(\beta)\) past **all the other operators that are inside the time‑ordering symbol**. The number of fermionic interchanges performed is exactly the parity of the total number of fermionic operators that appear *outside* of \(A_k\). Denote this parity by \(\epsilon\) (the same symbol as in (1)). The cyclic move therefore yields

\[
\operatorname{Tr}\!\Big[ A_k(\beta)\,
e^{-\beta H}\,
T_\tau\{ \ldots\}\Big]
=
\epsilon\,
\operatorname{Tr}\!\Big[ e^{-\beta H}\,
T_\tau\{ \ldots A_k(\beta) \}\Big].
\tag{10}
\]

(If all operators are bosonic, \(\epsilon=+1\); if an odd number of fermionic operators are present, \(\epsilon=-1\).)

### 2.5  Restoring the time‑ordering

Inside the trace on the right‑hand side of (10) the operator \(A_k(\beta)\) now appears **at the right end** of the ordered product.  
The time‑ordering operator \(T_\tau\) will place it **according to its time argument \(\beta\)**.  
Since \(\beta\) is the *largest* imaginary time, \(A_k(\beta)\) must be moved **to the leftmost position** of the ordered product.  
Moving it past the other \(n-1\) operators involves exactly **\(n-1\) permutations**.  

* For **bosons** each permutation contributes no sign.
* For **fermions** each permutation contributes a factor \(-1\).

Thus the total sign from re‑ordering \(A_k(\beta)\) to its proper position is \((-1)^{n-1}\) for fermions and \(+1\) for bosons.  
Because \((-1)^{n-1}= -\epsilon\) (recall \(\epsilon = -1\) for fermions), the overall factor produced by the two steps—cyclic permutation **and** re‑ordering inside \(T_\tau\)—is exactly \(-\epsilon\).

Putting everything together:

\[
\begin{aligned}
G(\tau_1,\dots ,0,\dots ,\tau_n)
&= \frac{1}{Z}\,
\operatorname{Tr}\!\Big[ e^{-\beta H}\,
T_\tau\{ \dots A_k(0) \dots\}\Big]  \\[4pt]
&= \frac{1}{Z}\,
\epsilon\,
\operatorname{Tr}\!\Big[ e^{-\beta H}\,
T_\tau\{ \dots A_k(\beta) \dots\}\Big]\;(-\epsilon) \\[4pt]
&= -\epsilon\;
\frac{1}{Z}\,
\operatorname{Tr}\!\Big[ e^{-\beta H}\,
T_\tau\{ \dots A_k(\beta) \dots\}\Big] \\[4pt]
&= -\epsilon\; G(\tau_1,\dots ,\beta ,\dots ,\tau_n).
\end{aligned}
\tag{11}
\]

Equation (11) is exactly the statement (1) that Rickayzen wrote.

### 2.6  Why the “counter‑example’’ with three operators fails

In the attempted counter‑example the author compared

\[
\langle A(\beta) B(\tau_2) C(\tau_3) \rangle
\quad\text{with}\quad
\langle B(\tau_2) C(\tau_3) A(0) \rangle .
\]

Both expressions **miss** the crucial ingredients:

1. **The time‑ordering operator** \(T_\tau\) (which would reorder the three operators according to their times).  
2. **The cyclic permutation sign** that appears when moving the operator at \(\tau=0\) through the trace.

If the operators are fermionic, moving \(A(0)\) from the rightmost position to the leftmost position of the trace indeed produces a minus sign. Together with the extra sign that comes from putting \(A(\beta)\) at the leftmost place in the time‑ordered product, the overall factor is \(-\epsilon\), exactly as derived above.  
Therefore the apparent discrepancy disappears once the full definition (2) is used.

---

## 3.  Final answer

For a thermal (imaginary‑time) Green function defined by  

\[
G(\tau_1,\dots ,\tau_n)=\frac{1}{Z}
\operatorname{Tr}\!\big[e^{-\beta H}\,
T_\tau\{A_1(\tau_1)\cdots A_n(\tau_n)\}\big],
\]

the **boundary condition**

\[
\boxed{\,G(\tau_1,\dots ,0,\dots ,\tau_n)=
-\;\epsilon\;G(\tau

*Original question: [0K boundary condition for temperature Green&#39;s function](https://physics.stackexchange.com/questions/875955/0k-boundary-condition-for-temperature-greens-function) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
