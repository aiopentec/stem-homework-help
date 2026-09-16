---
layout: question
title: Integer interval $[p_n,p_{n+1}]$ has a prime factor $y_n$ such that $y_n &gt;
  p_{n+1} - p_n - 1$?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Integer interval $[p_n,p_{n+1}]$
  has a prime factor $y_n$ such that $y_n &gt; p_{n+1} - p_n - 1$?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

Let  

\[
p_n<p_{n+1}
\]

be two consecutive *odd* primes and put  

\[
g_n = p_{n+1}-p_n   \qquad(\text{the prime gap}).
\]

The interval  

\[
[p_n ,\,p_{n+1}]
\]

contains the two primes themselves and the \(g_n-1\) composite numbers that lie between them.  

**Claim T** (the statement we have to check) says:

> In every such interval there is a **composite** integer \(x_n\) whose *largest* prime divisor  
> \[
> y_n = P^{+}(x_n)
> \]
> satisfies  

\[
\boxed{ \; y_n > g_n-1 \;}
\]

In other words: *no matter how large the gap between two consecutive odd primes is, one of the numbers that sits inside the gap must have a prime factor that is larger than the length of the gap (minus 1).*  

The question is whether this statement is a known theorem, a conjecture, or already disproved by a counter‑example.

--------------------------------------------------------------------

## 2.  Reformulation in terms of “smooth” numbers  

A positive integer is called **\(y\)-smooth** if **all** of its prime factors are \(\le y\).  
Denote by  

\[
P^{+}(m)=\max\{ \text{prime divisor of } m\}
\]

the largest prime divisor of \(m\).  
Then the condition \(P^{+}(x_n) > g_n-1\) is exactly the negation of

\[
x_n\;\text{is }(g_n-1)\text{-smooth}.
\]

Hence Claim T is equivalent to the following statement:

> **Smooth‑gap conjecture.**  
> For every pair of consecutive odd primes \(p<p'\) the set  
> \(\{p,p+1,\dots ,p'\}\) contains at least one integer that is **not** \((p'-p-1)\)-smooth.

If the conjecture were false, we would have a prime gap \(g\) together with a *run* of \(g-1\) consecutive integers, all of whose prime factors are at most \(g-1\). Such a run is called a *smooth run* of length \(g-1\).

--------------------------------------------------------------------

## 3.  What is known about long smooth runs?

* **Existence of arbitrarily long runs of composites.**  
  Classical constructions (e.g. \(n!+2, n!+3,\dots , n!+n\)) show that for every \(k\) there are \(k\) consecutive composite numbers.  
  However the numbers \(n!+m\) are not guaranteed to be \(k\)-smooth; they may have a prime divisor larger than \(k\).

* **Upper bounds for smooth runs.**  
  Let \( \Psi(x,y) \) denote the number of \(y\)-smooth integers \(\le x\).  A deep result of de Bruijn (and later refinements by Hildebrand, Tenenbaum, etc.) gives  

  \[
  \Psi(x,y)=x\,\rho\!\bigl(\frac{\log x

*Original question: [Integer interval $[p_n,p_{n+1}]$ has a prime factor $y_n$ such that $y_n &gt; p_{n+1} - p_n - 1$?](https://math.stackexchange.com/questions/5149500/integer-interval-p-n-p-n1-has-a-prime-factor-y-n-such-that-y-n-p-n) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
