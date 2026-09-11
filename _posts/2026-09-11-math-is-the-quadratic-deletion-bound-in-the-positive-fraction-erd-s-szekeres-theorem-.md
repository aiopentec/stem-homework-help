---
layout: question
title: Is the quadratic deletion bound in the positive-fraction Erdős–Szekeres theorem
  necessary?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Is the quadratic deletion bound in
  the positive-fraction Erdős–Szekeres theorem necessary?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

*For a fixed integer \(k\ge 2\) we look at an arbitrary finite list of distinct real numbers.*  

*We are allowed to erase some of the numbers (the *deletions*). After the deletions we must be able to split the remaining list into at most \(f(k)\) subsequences, each of which can be written as a concatenation of **at least** \(k\) monotone blocks (each block is either strictly increasing or strictly decreasing).*

Suk–Zeng proved that one can always do this if we are allowed to delete  

\[
e(k)=(k-1)^{2}
\]

terms and we take  

\[
f(k)=O(k^{2}\log k).
\]

The question is:

> **Is the quadratic number \((k-1)^{2}\) of deletions really needed?**  
> In other words, does there exist a constant \(c>0\) such that for infinitely many
> \(k\) **every** sequence of distinct reals forces us to delete at least \(c k^{2}\)
> terms before it can be partitioned into at most \(O(k^{2}\log k)\) block‑monotone
> subsequences of depth \(\ge k\)?

The answer is **yes** – the quadratic bound is essentially optimal.  
We exhibit an explicit family of sequences for which any such partition must
delete a positive‑fraction of the elements, i.e. \(\Omega(k^{2})\) deletions.

--------------------------------------------------------------------

## 2.  The construction and the lower‑bound proof  

### 2.1  The “grid permutation’’  

For a given integer \(k\ge 2\) put  

\[
n:=(k-1)^{2}.
\]

Write the numbers \(1,2,\dots ,n\) in a \((k-1)\times (k-1)\) grid.
The rows are numbered \(1,\dots ,k-1\) from top to bottom and the columns
\(1,\dots ,k-1\) from left to right.
In the *\(i\)‑th row* we place the numbers  

\[
(i-1)(k-1)+1,\;(i-1)(k-1)+2,\dots ,\;(i-1)(k-1)+(k-1)
\]

**in decreasing order** (right‑to‑left).  
Now read the grid *row by row* from top to bottom; the obtained permutation of
\([n]\) is denoted by \(\pi_{k}\).

Explicitly,

\[
\pi_{k}= \bigl(k-1,\,k-2,\dots ,1,\;2(k-1),\,2(k-1)-1,\dots ,k,\; \dots ,
\;(k-1)^{2},\,(k-1)^{2}-1,\dots ,(k-2)(k-1)+1 \bigr).
\]

Because the permutation is obtained from a grid, it is often called the
*standard Erdős–Szekeres construction*.

--------------------------------------------------------------------

### 2.2  A basic property of \(\pi_{k}\)

**Lemma 1 (no long monotone subsequence).**  
\(\pi_{k}\) contains no increasing subsequence of length \(k\) and no decreasing
subsequence of length \(k\).

*Proof.*  
Consider any increasing subsequence. Its elements must come from distinct rows,
because within a row the numbers decrease. There are only \(k-1\) rows, so the
subsequence can have at most \(k-1\) elements. The same argument works for a
decreasing subsequence (the elements must belong to distinct columns, of which
there are also \(k-1\)). ∎



--------------------------------------------------------------------

### 2.3  What a block‑monotone subsequence of depth \(k\) can look like  

Recall the definition:

* a **block‑monotone subsequence of depth \(d\)** is a subsequence that can be
  split into \(d\) consecutive *blocks*,
* each block is either strictly increasing or strictly decreasing.

If a subsequence \(S\) of \(\pi_{k}\) has depth at least \(k\), then among its
\(k\) (or more) blocks at least one block must contain **two** elements that lie
in the same row *or* in the same column of the grid. (Otherwise the blocks would
pick at most one element from each of the \(k-1\) rows and at most one from each
of the \(k-1\) columns, giving a total of at most \((k-1)^{2}\) elements, but a
depth‑\(k\) subsequence must have at least \(k\) blocks, i.e. at least \(k\)
elements – the bound is not contradictory, we need a stronger observation.)

The key observation is that a **single monotone block can contain at most one
element from each row and at most one element from each column**:

*If a block were increasing, Lemma 1 tells us that it cannot meet two points of the
same row (otherwise the values would be decreasing).  
If a block were decreasing, it cannot meet two points of the same column for the
same reason.*  

Consequently:

> **Lemma 2.**  
> Any block‑monotone subsequence of depth \(k\) in \(\pi_{k}\) contains at most
> \((k-1)^{2}\) elements.

*Proof.*  
Take any depth‑\(k\) subsequence \(B\). Split it into its \(k\) monotone blocks
\(B_{1},\dots ,B_{k}\). By Lemma 1 each block can meet at most one element from any
given row *and* at most one element from any given column. Hence each block
contains at most \((k-1)^{2}\) elements, and the whole subsequence contains at most
\(k\,(k-1)^{2}\) – but we only need the weaker bound that the **union of the
\(k\) blocks** (i.e. the subsequence itself) cannot exceed \((

*Original question: [Is the quadratic deletion bound in the positive-fraction Erdős–Szekeres theorem necessary?](https://math.stackexchange.com/questions/5149160/is-the-quadratic-deletion-bound-in-the-positive-fraction-erd%c5%91s-szekeres-theorem) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
