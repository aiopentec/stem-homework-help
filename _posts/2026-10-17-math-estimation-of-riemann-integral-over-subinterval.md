---
layout: question
title: Estimation of Riemann integral over subinterval
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Estimation of Riemann integral over
  subinterval'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

*We are given a real‑valued function*  

\[
f:[0,L]\longrightarrow \mathbb R ,
\qquad\text{which is Riemann‑integrable on }[0,L].
\]

*Its total integral is*  

\[
I=\int_{0}^{L}f(x)\,dx .
\]

The **average value** of \(f\) on the whole interval is  

\[
\mu=\frac{I}{L}.
\]

For a fixed length \(r\;(0<r\le L)\) we look at all sub‑intervals of that length,
\([a,a+r]\subset[0,L]\) (so \(a\in[0,L-r]\)).  
For each such sub‑interval we can compute the integral

\[
\int_{a}^{a+r}f(x)\,dx .
\]

The question is:

> **For which positive numbers \(r\) can we be *sure* (no matter which
> integrable \(f\) we start with) that there is at least one sub‑interval of
> length \(r\) whose integral equals \(\displaystyle\frac{Ir}{L}= \mu r\)?**

In other words, for which \(r\) does the equality  

\[
\int_{a}^{a+r} f(x)\,dx = \frac{Ir}{L}
\tag{1}
\]

hold for some \(a\in[0,L-r]\) for **every** integrable \(f\)?

---

## 2.  Proof – every \(r\in(0,L]\) works  

### 2.1  A convenient auxiliary function  

Define the *cumulative integral* (also called the *primitive*)  

\[
F(x)=\int_{0}^{x}f(t)\,dt ,\qquad x\in[0,L].
\]

Because \(f\) is Riemann‑integrable, \(F\) is **continuous** on \([0,L]\).

Now introduce  

\[
\Phi(x)=F(x)-\mu x\;=\; \int_{0}^{x}f(t)\,dt-\frac{I}{L}x .
\tag{2}
\]

\(\Phi\) is continuous as a difference of continuous functions and satisfies  

\[
\Phi(0)=0,\qquad \Phi(L)=\int_{0}^{L}f(t)\,dt-\frac{I}{L}L=0 .
\tag{3}
\]

Thus \(\Phi\) starts and ends at the same value.

### 2.2  Sliding‑window function  

For a fixed length \(r\;(0<r\le L)\) define  

\[
G_{r}(a)=\Phi(a+r)-\Phi(a),\qquad a\in[0,L-r].
\tag{4}
\]

Using (2),

\[
\begin{aligned}
G_{r}(a) 
&= \Bigl(\int_{0}^{a+r}f-\mu (a+r)\Bigr)-\Bigl(\int_{0}^{a}f-\mu a\Bigr)\\[2mm]
&= \int_{a}^{a+r}f(t

*Original question: [Estimation of Riemann integral over subinterval](https://math.stackexchange.com/questions/5152089/estimation-of-riemann-integral-over-subinterval) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
