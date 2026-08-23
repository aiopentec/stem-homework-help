---
layout: post
title: Finding primes so that $x^p+y^p=z^p$ is unsolvable in the $p$-adic units
author: StemFix Bot
category: math
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem asks  

Let  

\[
f_{p}(a)= (a+1)^{p}-a^{p}-1 ,\qquad a\in \mathbb Z ,\; p>2\text{ prime}.
\]

Because \(f_{p}(a)\equiv0\pmod p\) for every integer \(a\) (reduce the
binomial expansion modulo \(p\)), the congruence  

\[
f_{p}(a)\equiv0\pmod {p^{2}}
\tag{1}
\]

asks for **an extra factor \(p\)**.  

Define  

\[
\mathcal P:=\{p\text{ prime }:\; \exists a\in\mathbb Z,\;
p\nmid a(a+1)\text{ and }(1)\text{ holds}\}.
\]

The exam problem proved that  

*   \(x^{p}+y^{p}=z^{p}\) has a solution in the group of \(p\)-adic units
    \(\mathbb Z_{p}^{\times}\) **iff** \(p\in\mathcal P\).

The question we have to answer is:

*   **For which primes does (1) have a solution?**  
    In particular we want to know what happens for primes \(p\equiv2\pmod3\) and to prove that both the “good’’ primes (those **not** in \(\mathcal P\)) and the “bad’’ primes (those **in** \(\mathcal P\)) occur infinitely often.

--------------------------------------------------------------------

## 2.  A convenient reformulation

Write  

\[
u\equiv a\pmod{p^{2}},\qquad u\in(\mathbb Z/p^{2}\mathbb Z)^{\times } .
\]

Using the binomial theorem and the fact that \(\binom{p}{k}=p\frac{(p-1)!}{k!(p-k)!}\) is
divisible by \(p\) for \(1\le k\le p-1\), we obtain  

\[
\begin{aligned}
 (a+1)^{p}
    &= a^{p}+p\,a^{p-1}
      +\frac{p(p-1)}{2}\,a^{p-2}+\cdots +p\,a+1\\[2mm]
    &\equiv a^{p}+1+p\sum_{k=1}^{p-1}\frac{1}{k}\binom{p-1}{k-1}a^{p-k}
      \pmod{p^{2}} .
\end{aligned}
\]

Hence (1) is equivalent to  

\[
\sum_{k=1}^{p-1}\frac{1}{k}\binom{p-1}{k-1}a^{p-k}\equiv0\pmod p .
\tag{2}
\]

The sum in (2) is the **Fermat quotient** of the unit \(a+1\) minus the
Fermat quotient of the unit \(a\):

\[
q_{p}(b):=\frac{b^{p-1}-1}{p}\pmod p .
\]

Indeed, a short calculation gives  

\[
q_{p}(a+1)-q_{p}(a)\equiv\sum_{k=1}^{p-1}\frac{1}{k}\binom{p-1}{k-1}a^{p-k}
\pmod p .
\]

Consequently

\[
\boxed{\; (a+1)^{p}\equiv a^{p}+1\pmod{p^{2}}
       \iff q_{p}(a+1)\equiv q_{p}(a)\pmod p\

*Original question: [Finding primes so that $x^p+y^p=z^p$ is unsolvable in the $p$-adic units](https://math.stackexchange.com/questions/1827475/finding-primes-so-that-xpyp-zp-is-unsolvable-in-the-p-adic-units) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
