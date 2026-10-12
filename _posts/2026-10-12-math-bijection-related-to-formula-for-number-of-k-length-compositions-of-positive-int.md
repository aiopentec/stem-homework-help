---
layout: question
title: Bijection related to formula for number of $k$ length compositions of positive
  integer $n$ and subsets of a set
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Bijection related to formula for
  number of $k$ length compositions of positive integer $n$ and subsets of a set'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We are given a positive integer \(n\) and a positive integer \(k\le n\).  
A **composition of \(n\) into \(k\) parts** is an ordered \(k\)-tuple  

\[
(a_1,a_2,\dots ,a_k),\qquad a_i\in\mathbb Z_{>0},\;a_1+\dots +a_k=n .
\]

The book claims that the number of such compositions is  

\[
\boxed{\displaystyle \binom{n-1}{\,k-1\,}} .
\]

The question is:

* Why does this binomial coefficient count the compositions?
* How is this count related to a **bijection** with subsets of a set?
* What exactly is a bijection and its inverse in this context?

---

## 2.  Step‑by‑step solution  

### 2.1  Stars–and–bars picture  

Write \(n\) as a row of \(n\) indistinguishable “stars”

\[
\underbrace{*\,*\,\dots *}_{n\text{ stars}} .
\]

To obtain a composition into \(k\) positive parts we must split this row into \(k\) blocks,
each block containing at least one star.  
We do this by inserting \(k-1\) **bars** (vertical separators) in the gaps **between** consecutive stars.

```
* * * * * * * * * *      (n = 10)
^ ^ ^ ^ ^ ^ ^ ^ ^       (9 gaps)
```

There are exactly \(n-1\) gaps where a bar could be placed (the positions **between** the stars).  
Choosing any set of \(k-1\) of those gaps determines a unique placement of the bars, and therefore a unique composition:

* The number of stars before the first chosen gap is \(a_1\).
* The number of stars between the first and second chosen gaps is \(a_2\).
* … and so on, until the number of stars after the last chosen gap is \(a_k\).

Because each block must contain at least one star, we are *forced* to place the bars only in the gaps; we never place a bar at the very left or right end of the row. Hence every choice of \(k-1\) gaps yields a composition with all parts \(>0\).

Conversely, given a composition \((a_1,\dots ,a_k)\) we can recover the set of gaps:
after the first \(a_1\) stars we put a bar, after the next \(a_2\) stars another bar, etc.  
Thus the two constructions are inverse to each other.

### 2.2  From bars to subsets  

Identify the set of gaps with the set \(\{1,2,\dots ,n-1\}\), where gap \(i\) is the one **between** star \(i\) and star \(i+1\).

*Choosing a set of \(k-1\) gaps* is exactly the same as *choosing a subset of size \(k-1\) of the set \(\{1,\dots ,n-1\}\)*.

Therefore we have a **bijection**

\[
\begin{aligned}
\Phi :\;&\{\text{compositions of }n\text{ into }k\text{ positive parts}\}\\
        &\longleftrightarrow
\{\text{subsets }S\subseteq\{1,\dots ,n-1\}\mid |S|=k-1\}.
\end{aligned}
\]

The map \(\Phi\) sends a composition \((a_1,\dots ,a_k)\) to the set of gap‑indices that lie after the cumulative sums  

\[
a_1,\;a_1+a_2,\; \dots ,\; a_1+\dots +a_{k-1}.
\]

The inverse map \(\Phi^{-1}\) takes a subset \(S=\{s_1< s_2<\dots < s_{k-1}\}\) and returns the composition  

\[
(s_1,\; s_2-s_1,\; \dots ,\; s_{k-1}-s_{k-2},\; n-s_{k-1}).
\]

Both directions are well‑defined and undo each other, which is precisely what “bijection” means: a one‑to‑one correspondence that is both **injective** (different inputs give different outputs) and **surjective** (every possible output is obtained).

### 2.3  Counting the subsets  

The number of subsets of \(\{1,\dots ,n-1\}\) that have exactly \(k-1\) elements is given by the binomial coefficient  

\[
\binom{n-1}{k-1}.
\]

Because of the bijection above, this is *exactly* the number of compositions of \(n\) into \(k\) positive parts.

Hence  

\[
\boxed{\displaystyle \#\{\text{compositions of }n\text{ into }k\text{ parts}\}= \binom{n-1}{k-1}} .
\]

### 2.4  Why the “replace \(n\) by \(n+k\)” trick does **not** work  

The identity  

\[
\#\{(x_1,\dots ,x_k)\in\mathbb Z_{\ge0} : x_1+\dots +x_k = n\}= \binom{n+k-1}{k-1}
\]

counts **weak** compositions (allowing zeros).  
If we want **strictly positive** parts, we set \(x_i = a_i-1\) with \(a_i>0\). Then  

\[
(a_1-1)+\dots +(a_k-1)=n-k\quad\Longrightarrow\quad
a_1+\dots +a_k = n .
\]

Thus the number of *strict* compositions of \(n\) into \(k\) parts is  

\[
\binom{(n-k)+k-1}{k-1}= \binom{n-1}{k-1}.
\]

The “replace \(n\) by \(n-1\)” you observed is *exactly* the algebraic reflection of the same bijection, not a coincidence. It works because adding \(1\) to each part (to turn a weak composition into a strict one) reduces the total sum by \(k\).

---

## 3.  Final answer  

The number of compositions of a positive integer \(n\) into exactly \(k\) positive parts is  

\[
\boxed{\displaystyle \binom{n-1}{k-1}} .
\]

The proof is a bijection between:

* compositions \((a_1,\dots ,a_k)\) with \(a_i>0\) and \(\sum a_i=n\), and
* subsets of size \(k-1\) of the set \(\{1,2,\dots ,n-1\}\).

The bijection is realized by placing bars between the \(n\) “stars”; the positions of the bars give the subset, and the gaps between consecutive bars give the parts of the composition. The inverse map recovers the composition from the subset by taking successive differences.

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---|---|---|
| **Treating the “\(k-1\) bars” as if they could be placed at the ends** | Bars at the very left or right would create a part of size \(0\), which is not allowed for a composition into positive parts. | Remember that the stars‑and‑bars model for **positive** parts uses only the **\(n-1\) interior gaps**. |
| **Confusing weak and strict compositions** | Using \(\binom{n+k-1}{k-1}\) directly counts compositions that may contain zeroes. | Convert a weak composition \((x_1,\dots ,x_k)\) to a strict one by setting \(a_i = x_i+1\). |
| **Thinking “replace \(n\) by \(n-1\)” is a magical trick** | The replacement is justified only after the shift \(a_i = x_i+1\); without that shift the combinatorial meaning changes. | Explain the algebraic step in terms of the bijection (adding 1 to each part). |
| **Neglecting the order of parts** | A composition cares about order, while a partition does not; forgetting this leads to using \(\binom{n-1}{k-1}\) for the wrong object. | Emphasize that the bars are placed in *specific* gaps, which preserves the order of the resulting blocks. |
| **Mis‑identifying the inverse map** | Giving a formula that does not recover the original composition. | Write the inverse explicitly: from a subset \(\{s_1<\dots <s_{k-1}\}\) produce \((s_1,\,s_2-s_1,\dots ,\,s_{k-1}-s_{k-2},\,n-s_{k-1})\). |

Keeping these points in mind will help you construct correct bijective arguments for similar “stars‑and‑bars’’ problems.

*Original question: [Bijection related to formula for number of $k$ length compositions of positive integer $n$ and subsets of a set](https://math.stackexchange.com/questions/5151707/bijection-related-to-formula-for-number-of-k-length-compositions-of-positive-i) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
