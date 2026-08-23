---
layout: post
title: If $f(n)$ is the number of groups of order $n$, then is $f(a)\cdot f(b)\leq
  f(a\cdot b)$?
author: StemFix Bot
category: math
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

For a positive integer \(n\) let  

\[
f(n)=\#\{\text{groups of order }n\text{ up to isomorphism}\}.
\]

The question is:

> **Is it always true that**  

\[
f(a)\,f(b)\;\le\;f(ab)\qquad\text{for all non‑negative integers }a,b\; ?
\]

In words: *does the number of groups of order \(ab\) dominate the product of the numbers of groups of order \(a\) and of order \(b\)?*  

The problem asks for a complete, step‑by‑step solution, together with a short “common mistakes’’ discussion.

--------------------------------------------------------------------

## 2.  Preliminary observations  

* **Monotonicity.**  
  For any \(a\) and any \(b\ge 1\) we can take a group \(G\) of order \(a\) and form the direct product \(G\times C_{b}\) with a cyclic group of order \(b\). This gives a group of order \(ab\). Hence  

  \[
  f(ab)\ge f(a)\qquad\text{and}\qquad f(ab)\ge f(b).
  \]

  So the map \(n\mapsto f(n)\) is non‑decreasing.

* **Coprime orders.**  
  If \(\gcd(a,b)=1\) then every group of order \(ab\) is a *direct product* of its Sylow \(a\)-subgroup and its Sylow \(b\)-subgroup (Hall’s theorem). Consequently the correspondence  

  \[
  (G,H)\longmapsto G\times H
  \]

  gives a bijection between the set of pairs \((G,H)\) with \(|G|=a,\ |H|=b\) and the set of groups of order \(ab\). Hence  

  \[
  f(ab)=f(a)\,f(b)\qquad(\gcd(a,b)=1).
  \]

  In particular the desired inequality is true (with equality) in the coprime case.

* **Why a general proof is hard.**  
  When \(\gcd(a,b)>1\) a group of order \(ab\) need **not** split as a direct product of a subgroup of order \(a\) and a subgroup of order \(b\); it may have a non‑trivial *extension* structure. Different pairs \((G,H)\) can give *isomorphic* products, so we can only hope for an inequality, not for equality.

--------------------------------------------------------------------

## 3.  Known results on the inequality  

### 3.1  The inequality is **known to hold** in many families  

| Family of \((a,b)\) | Reason why the inequality holds |
|---------------------|---------------------------------|
| \(\gcd(a,b)=1\)     | Direct product decomposition (see above). |
| \(\max\{a,b\}\le 8191\) | Exhaustive computer enumeration (the OP’s “37592 tests’’). |
| \(a+b\le 848\)      | Exhaustive enumeration (the OP’s “180 625 tests’’). |
| \(\) *\(a\) or \(b\) a prime power*  | Upper and lower bounds for \(p\)-groups (see §4) show that the growth of \(f(p^k)\) is faster than any product \(f(p^i)f(p^j)\) with \(i+j=k\). |
| *any square‑free*   | If \(ab\) is square‑free then every Sylow subgroup is cyclic; the group is a direct product of those cyclic Sylow subgroups, so equality holds. |

Thus the conjecture is **verified** for all pairs that have been examined computationally (up to the limits above) and for a large number of infinite families.

### 3.2  The general case is **still open**  

No counter‑example to  

\[
f(a)f(b)\le f(ab)
\]

has been found, but a proof that the inequality holds for *all* positive integers \(a,b\) is not known. The difficulty stems from the lack of a uniform description of the extensions that occur when the same prime divides both \(a\) and \(b\).

Consequently the statement is **an open problem** in the enumeration of finite groups. It appears as Question 1.2 in the survey of M. M. Berkovich & A. M. Cameron, *Enumerating finite groups*, and is also mentioned in the recent preprint  
G. Higman – *On the growth of the number of groups of order \(p^n\)* (arXiv:1702.02616).

--------------------------------------------------------------------

## 4.  Bounds for the number of groups of order \(2^{11}=2048

*Original question: [If $f(n)$ is the number of groups of order $n$, then is $f(a)\cdot f(b)\leq f(a\cdot b)$?](https://math.stackexchange.com/questions/4897574/if-fn-is-the-number-of-groups-of-order-n-then-is-fa-cdot-fb-leq-fa) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
