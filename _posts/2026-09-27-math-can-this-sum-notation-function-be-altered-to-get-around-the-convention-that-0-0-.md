---
layout: question
title: Can this Sum-Notation function be altered to get around the convention that
  $0^0 = 1$?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Can this Sum-Notation function be
  altered to get around the convention that $0^0 = 1$?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (plain language)

You have a compact formula  

\[
d_{m,n}(t)=\frac{1}{n!}\sum_{i=1}^{2^{m}}
\Bigl((-1)^{S(i)}\;\max\!\bigl(0,\;t-T_m(i)\bigr)^{\,n}\Bigr) \tag{1}
\]

that works for all integers \(n\ge 1\).  
When \(n=0\) the factor  

\[
\max\!\bigl(0,\;t-T_m(i)\bigr)^{\,0}
\]

is interpreted by most computer algebra systems as \(1\) **even when the argument is
\(0\)** (the usual convention \(0^{0}=1\)). Consequently every term in the sum
contributes \((-1)^{S(i)}\) and the whole expression becomes a constant (the
alternating sum of the first \(2^{m}\) Thue–Morse signs), i.e. a flat line.

What you really want for the case \(n=0\) is a *step‑like* behaviour:

* on the interval \([T_m(i),\,T_m(i+1))\) the term should be \((-1)^{S(i)}\);
* on the interval \((-\infty,\,T_m(i))\) the term should be **zero**.

In other words you would like the factor \(\max(0,\;t-T_m(i))^{0}\) to be
\(1\) **only when** \(t>T_m(i)\) and \(0\) otherwise.  
The question is: *Can we rewrite (1) so that this happens without returning to an
explicit piece‑wise definition?*

---

## 2.  Detailed solution

### 2.1  Replace the “max‑to‑power‑0’’ with a Heaviside (step) function  

The Heaviside step function \(H(x)\) is defined as  

\[
H(x)=\begin{cases}
0, & x\le 0,\\[2pt]
1, & x>0 .
\end{cases}
\]

(Any value at \(x=0\) may be chosen; we shall take \(H(0)=0\) to obtain the
half‑open intervals required in the problem.)  
Notice that for any real \(x\),

\[
\max(0,x)=x\,H(x).
\]

Hence for a **positive integer** \(n\),

\[
\max(0,x)^{\,n}=x^{\,n}H(x) .
\]

When \(n=0\) we *define*  

\[
\max(0,x)^{\,0}=H(x), \qquad\text{(definition for the present purpose)} \tag{2}
\]

so that the factor is \(1\) only when \(x>0\) and \(0\) otherwise.

### 2.2  Insert the step function into the sum

Using (2) we can rewrite (1) as  

\[
\boxed{
d_{m,n}(t)=\frac{1}{n!}\sum_{i=1}^{2^{m}}
\Bigl((-1)^{S(i)}\;(t-T_m(i))^{\,n}\,H\!\bigl(t-T_m(i)\bigr)\Bigr)
}\tag{3}
\]

where the exponent \(n\) may be any non‑negative integer.  

* For \(n\ge 1\) the factor \((t-T_m(i))^{n}\) already forces the term to be zero
  whenever \(t\le T_m(i)\); the extra \(H\) does not change the value.
* For \(n=0\) the factor \((t-T_m(i))^{0}=1\) and the whole term reduces to
  \((-1)^{S(i)} H(t-T_m(i))\), i.e. a **step** that is \(0\) on
  \((-\infty,T_m(i)]\) and \((-1)^{S(i)}\) on \((T_m(i),\infty)\).

Thus on each half‑open interval \([T_m(i),T_m(i+1))\) the sum (3) contributes the
single non‑zero term with index \(i\) and yields precisely \((-1)^{S(i)}\),
exactly the behaviour requested.

### 2.3  Verify the result for a simple example  

Take \(m=2\) (so \(2^{m}=4\)) and let  

\[
T_{2} = (0,\,1,\,2,\,3) .
\]

The Thue–Morse signs are \((-1)^{S(i)} = (1,-1,-1,1)\).  
Using (3) with \(n=0\),

\[
\begin{aligned}
d_{2,0}(t)
&= \sum_{i=1}^{4} (-1)^{S(i)} H\!\bigl(t-T_{2}(i)\bigr)\\
&= 1\cdot H(t-0)\;-\;1\cdot H(t-1)\;-\;1\cdot H(t-2)\;+\;1\cdot H(t-3).
\end{aligned}
\]

Evaluating on the intervals gives  

| interval                     | value of \(d_{2,0}(t)\) |
|------------------------------|-------------------------|
| \([0,1)\)                     | \(+1\)                  |
| \([1,2)\)                     | \(-1\)                  |
| \([2,3)\)                     | \(-1\)                  |
| \([3,\infty)\)                | \(+1\)                  |

exactly the alternating pattern required, while the function is \(0\) for
\(t<0\) (because all Heaviside factors are zero).  

For any larger \(n\) the same formula (3) reproduces the original polynomial
pieces because the extra \(H\) factor is redundant.

### 2.4  Final compact definition

Putting everything together, the **modified** definition that works for every
\(n\in\{0,1,\dots ,m\}\) is  

\[
\boxed{
d_{m,n}(t)=\frac{1}{n!}\sum_{i=1}^{2^{m}}
(-1)^{S(i)}\;(t-T_m(i))^{\,n}\;H\!\bigl(t-T_m(i)\bigr)
}\qquad (n\ge 0).
\]

If you prefer to keep the original “max’’ notation, you can state it as  

\[
d_{m,n}(t)=\frac{1}{n!}\sum_{i=1}^{2^{m}}
(-1)^{S(i)}\;\bigl[\max\!\bigl(0,\,t-T_m(i)\bigr)\bigr]^{\,n},
\quad\text{with the convention } \bigl[\max(0,x)\bigr]^{0}=H(x).
\]

Either version eliminates the unwanted constant‑line behaviour for the case
\(n=0\) while remaining a single summation, not a piece‑wise definition.

---

## 3.  Final answer

**Answer:**  
Introduce the Heaviside step function \(H\) (or equivalently define
\(\max(0,x)^{0}=H(x)\)) and write  

\[
\boxed{%
d_{m,n}(t)=\frac{1}{n!}\sum_{i=1}^{2^{m}}
(-1)^{S(i)}\,(t-T_m(i))^{\,n}\,H\!\bigl(t-T_m(i)\bigr)
}
\]

for all integers \(0\le n\le m\).  
For \(n\ge 1\) this coincides with the original expression; for \(n=0\) it
produces a step function that is zero on \((-\infty,T_m(i)]\) and \((-1)^{S(i)}\)
on \((T_m(i),\infty)\), giving the desired sequence of positive, zero, and
negative segments without resorting to an explicit piece‑wise definition.

---

## 4.  Common mistakes

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating \(0^{0}=1\) everywhere** | This makes the \(n=0\) term non‑zero even when \(t\le T_m(i)\), destroying the intended interval structure. | Replace the power‑zero case by a step function: \( \max(0,x)^{0}=H(x)\). |
| **Using the “standard’’ Heaviside with \(H(0)=\tfrac12\)** | The half‑open intervals \([T_m(i),T_m(i+1))\) require the value at the left endpoint to be zero; a value of \(1/2\) would create spurious jumps. | Adopt the convention \(H(0)=0\) (or write the condition as \(t>T_m(i)\) explicitly). |
| **Omitting the factor \(H(t-T_m(i))\) for \(n\ge 1\)** | For \(n\ge 1\) the factor is technically unnecessary, but keeping it makes the formula uniform and prevents accidental inclusion of the \(n=0\) case. | Keep the step function in every term; it is harmless when \(n\ge 1\). |
| **Confusing the Thue–Morse sign \((-1)^{S(i)}\) with the sequence values** | The sign must be applied to each term of the sum; mixing up the exponent can flip the pattern. | Remember that \(S(i)\) is the *binary digit sum modulo 2*; compute \((-1)^{S(i)}\) correctly. |

By watching for these pitfalls you can reliably implement the compact
summation for all required values of \(n\).

*Original question: [Can this Sum-Notation function be altered to get around the convention that $0^0 = 1$?](https://math.stackexchange.com/questions/5150513/can-this-sum-notation-function-be-altered-to-get-around-the-convention-that-00) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
