---
layout: question
title: Finding $\displaystyle \sup_{x \in [1,\infty)} x e^{-tx}$ when $t \ge 0$
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Finding $\displaystyle \sup_{x \in
  [1,\infty)} x e^{-tx}$ when $t \ge 0$'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

For a fixed non‑negative parameter \(t\) we consider the function  

\[
f_t(x)=x\,e^{-t x}, \qquad x\in[1,\infty).
\]

We have to determine the **supremum** (the least upper bound) of the set  

\[
\{f_t(x):x\in[1,\infty)\}
\]

for each possible value of \(t\ge 0\).  
In other words: “How large can the product \(x e^{-t x}\) become when we are allowed to choose any \(x\ge 1\)?”  

---

## 2.  Detailed solution  

### 2.1  The case \(t=0\)

If \(t=0\) then  

\[
f_0(x)=x e^{0}=x .
\]

On the interval \([1,\infty)\) the function is just the identity, so it grows without bound:

\[
\sup_{x\ge 1} f_0(x)=\sup_{x\ge 1} x =+\infty .
\]

---

### 2.2  The case \(t>0\)

#### 2.2.1  First derivative  

\[
f_t(x)=x e^{-t x}, \qquad t>0.
\]

Differentiate (product rule):

\[
f'_t(x)=e^{-t x}+x(-t)e^{-t x}=e^{-t x}(1-tx).
\]

Because the exponential factor is never zero, the critical points are the solutions of  

\[
1-tx=0\quad\Longrightarrow\quad x=\frac{1}{t}.
\]

#### 2.2.2  Where does the critical point lie?  

Our domain is \([1,\infty)\).  
The point \(x=\frac{1}{t}\) belongs to this interval **iff** \(\frac{1}{t}\ge 1\), i.e. iff  

\[
0<t\le 1 .
\]

Thus we have two sub‑cases:

* **(a) \(0<t\le 1\)** – the critical point is inside the domain.  
* **(b) \(t\ge 1\)** – the critical point is to the left of the domain; on \([1,\infty)\) the derivative never changes sign.

#### 2.2.3  Behaviour for large \(x\)

Regardless of \(t>0\),

\[
\lim_{x\to\infty} x e^{-t x}=0 .
\]

A quick proof with L’Hôpital:

\[
\lim_{x\to\infty}\frac{x}{e^{t x}}
 =\lim_{x\to\infty}\frac{1}{t e^{t x}}=0 .
\]

Hence the function cannot have its supremum at \(+\infty\).

#### 2.2.4  Sub‑case (a): \(0<t\le 1\)

Here \(x_0=1/t\) belongs to the interval, and the derivative changes sign:

* For \(1\le x<1/t\), we have \(1-tx>0\) → \(f'_t(x)>0\) (increasing).  
* For \(x>1/t\), we have \(1-tx<0\) → \(f'_t(x)<0\) (decreasing).

Thus \(x_0\) gives the *global maximum* on \([1,\infty)\).  
Its value is  

\[
f_t\!\left(\frac{1}{t}\right)=\frac{1}{t}\,e^{-t\cdot\frac{1}{t}}=
\frac{1}{t}\,e^{-1}= \frac{1}{t e}.
\]

Because the limit at infinity is \(0\) and \(f_t(1)=e^{-t}<\frac{1}{t e}\) for \(0<t\le1\), the supremum equals this value:

\[
\boxed{\displaystyle \sup_{x\ge 1} f_t(x)=\frac{1}{t e}\qquad (0<t\le 1)}.
\]

#### 2.2.5  Sub‑case (b): \(t\ge 1\)

Now \(1/t\le 1\), so the critical point is **outside** the domain.  
For every \(x\ge 1\),

\[
1-tx\le 1-t\le 0\quad\Longrightarrow\quad f'_t(x)\le 0 .
\]

Hence \(f_t\) is *strictly decreasing* on \([1,\infty)\).  
The largest value is therefore attained at the left endpoint \(x=1\):

\[
f_t(1)=e^{-t}.
\]

Since the limit at infinity is \(0\), we obtain

\[
\boxed{\displaystyle \sup_{x\ge 1} f_t(x)=e^{-t}\qquad (t\ge 1)}.
\]

#### 2.2.6  Summary for \(t>0\)

Putting the two sub‑cases together,

\[
\sup_{x\ge 1} x e^{-t x}= 
\begin{cases}
\dfrac{1}{t e}, & 0<t\le 1,\\[6pt]
e^{-t}, & t\ge 1 .
\end{cases}
\]

Notice that the two formulas coincide at \(t=1\) because \(\frac{1}{1e}=e^{-1}\).

---

### 2.3  Final answer (all \(t\ge 0\))

\[
\boxed{
\sup_{x\in[1,\infty)} x e^{-t x}= 
\begin{cases}
+\infty, & t=0,\\[6pt]
\dfrac{1}{t e}, & 0<t\le 1,\\[8pt]
e^{-t}, & t\ge 1 .
\end{cases}}
\]

The supremum is actually a **maximum** in every case (it is attained at \(x=\infty\) when \(t=0\), at \(x=1/t\) when \(0<t\le1\), and at \(x=1\) when \(t\ge1\)).

---

## 3.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Ignoring the restriction \(x\ge 1\)** when locating the critical point. | The derivative gives \(x=1/t\), but if \(t>1\) this point lies left of the interval, so it cannot be a candidate for the supremum. | After solving \(f'(x)=0\), always check whether the solution belongs to the given domain. |
| **Assuming the supremum is always at the critical point**. | When the critical point is outside the domain the function is monotone on the whole interval, and the extremum occurs at an endpoint. | Examine the sign of \(f'(x)\) on the interval; if it never changes sign, the extremum is at an endpoint. |
| **Treating \(\lim_{x\to\infty} x/e^{t x}\) as “\(\infty/\infty\)” and stopping**. | The indeterminate form must be resolved (e.g., by L’Hôpital’s rule) to see that the limit is actually \(0\). | Apply L’Hôpital (or compare growth rates: exponential dominates any polynomial) to compute the limit. |
| **Missing the case \(t=0\)**. | For \(t=0\) the function reduces to \(x\), which is unbounded, so the supremum is \(+\infty\). | Separate the analysis into \(t=0\) and \(t>0\) right at the start. |
| **Writing \(\sup\lim\) instead of \(\sup\)**. | “\(\sup\lim\)” is not a standard notation; we first take the supremum of the function values, not of a limit. | Use the correct notation: \(\displaystyle \sup_{x\in[1,\infty)} f_t(x)\). |

Keeping these points in mind will help you solve similar optimisation‑over‑unbounded‑interval problems without error.

*Original question: [Finding $\displaystyle \sup_{x \in [1,\infty)} x e^{-tx}$ when $t \ge 0$](https://math.stackexchange.com/questions/5148858/finding-displaystyle-sup-x-in-1-infty-x-e-tx-when-t-ge-0) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
