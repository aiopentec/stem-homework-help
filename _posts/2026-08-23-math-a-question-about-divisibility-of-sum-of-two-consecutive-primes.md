---
layout: post
title: A question about divisibility of sum of two consecutive primes
author: StemFix Bot
category: math
tags:
- math
render_with_liquid: false
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We are looking for the **smallest positive integer \(k\)** with the following property  

> “There are only finitely many *pairs of consecutive primes* \((p_n ,p_{n+1})\) such that  
> \(p_n+p_{n+1}\) is a multiple of \(k\).”

In other words, for every integer \(k\) we ask whether the set  

\[
\mathcal{S}_k=\Bigl\{n\in\mathbb N\;:\;k\mid (p_n+p_{n+1})\Bigr\}
\]

is infinite or finite.  
The problem asks for the first \(k\) for which \(\mathcal{S}_k\) is **finite**.

--------------------------------------------------------------------

## 2.  What is known for the small values of \(k\)

| \(k\) | Reason why \(\mathcal{S}_k\) is infinite |
|------|--------------------------------------------|
| \(1\) | Trivial – every integer is divisible by 1. |
| \(2\) | All primes larger than 2 are odd, so the sum of any two consecutive odd primes is even. |
| \(3\) | For every prime \(p>3\) we have \(p\equiv 1\) or \(2\pmod 3\).  Hence the residues of two consecutive primes are always opposite, so their sum is \(0\pmod 3\) infinitely often.  (A more formal proof uses Dirichlet’s theorem.) |
| \(4\) | Apart from the pair \((2,3)\) the sum of any two consecutive odd primes is a multiple of 4. |
| \(6\) | Every prime \(>3\) is \(\equiv \pm1\pmod 6\); consecutive primes therefore have opposite residues, giving a sum divisible by 6. |

Thus \(k=1,2,3,4,6\) **do not** satisfy the requirement.

--------------------------------------------------------------------

## 3.  Why we cannot yet decide the answer for larger \(k\)

### 3.1  What would we have to prove?

For a given \(k\) we would need to show **one** of the following:

* either that there are *infinitely many* consecutive‑prime pairs with sum \(0\pmod{k}\);  
* or that there are *only finitely many* such pairs.

The second alternative is what the problem asks for.  
Unfortunately, proving either alternative for an arbitrary modulus \(k\) is **beyond the reach of current number‑theoretic technology**.

### 3.2  Comparison with known open problems  

Write the consecutive primes as \(p\) and \(p' = p+g\) where \(g\) is the prime gap.  
The condition  

\[
k\mid (p+p')\qquad\Longleftrightarrow\qquad k\mid (2p+g)
\]

means that the gap \(g\) must satisfy a congruence that depends on the (unknown) value of \(p\).  
Thus the problem is **not** reduced to a fixed gap (as in the Twin‑Prime or Polignac conjectures) but to a *congruence condition that moves with the prime itself*.  

No theorem at present can guarantee that a given congruence condition on the sum of **consecutive** primes occurs infinitely often.  
The best results we have are:

* For moduli that divide \(6\) we can give an elementary proof (the table above).  
* For many other moduli we can exhibit *some* examples (e.g. \((3,5)\) gives sum 8, \((13,17)\) gives sum 30, \((53,59)\) gives sum 112, etc.), but we have **no proof of infinitude**.  

A proof that for a particular \(k\) there are *only finitely* many such pairs would be a major breakthrough; it would imply, for instance, that the set of prime gaps satisfying a certain linear condition is finite, something that is currently completely open.

### 3.3  What the literature says  

The statement  

> “For every integer \(k\ge 1\) there are infinitely many pairs of consecutive primes whose sum is divisible by \(k\)”

is **conjectural** (it

*Original question: [A question about divisibility of sum of two consecutive primes](https://math.stackexchange.com/questions/527495/a-question-about-divisibility-of-sum-of-two-consecutive-primes) on Mathematics Stack Exchange, licensed CC BY-SA.*
{% endraw %}
