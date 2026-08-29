---
layout: question
title: Maximizing the distance between consecutive vertices of a cycle graph
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Maximizing the distance between consecutive
  vertices of a cycle graph'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is really asking  

We have the *cycle graph*  

\[
C_n=\bigl\{0,1,\dots ,n-1\bigr\},\qquad 
\{i,i+1\}\in E(C_n)\;( \text{indices mod }n).
\]

The ordinary distance between two vertices is the length of the shorter walk on the cycle; for an even number of vertices the largest possible distance is \(\frac{n}{2}\) (the opposite vertex).

An **\(S\)-Hamiltonian cycle** is a permutation  

\[
(v_0,v_1,\dots ,v_{n-1})
\]

of the vertices such that for every \(i\) the two consecutive vertices
\(v_i\) and \(v_{i+1}\) (indices taken modulo \(n\)) can be joined by a walk whose
length belongs to a prescribed set \(S\subseteq \mathbb N\).
In the case of a cycle graph the only walks we need to consider are the
shortest ones, so “the length belongs to \(S\)” simply means that the
*distance* \(\operatorname{dist}(v_i,v_{i+1})\) is an element of \(S\).

The question is:

*For even \(n\) (so \(n=2m\)), find an \(S\)-Hamiltonian cycle with \(|S|\ge 2\) that makes the distance between consecutive vertices as large as possible.*  
In other words we want to maximise the **minimum** distance that occurs
between two consecutive vertices; the set \(S\) will be exactly the set of
distances that appear in the cycle.

--------------------------------------------------------------------

## 2.  Preliminary observations  

* The largest distance that can ever appear on \(C_n\) is \(\frac{n}{2}=m\).
* If we used only the distance \(m\) (i.e. we always jumped to the opposite
  vertex) we would obtain the 2‑cycle  

  \[
  0\to m\to 0\to m\to\cdots ,
  \]

  which clearly is **not** a Hamiltonian cycle – it visits each vertex only
  twice. Hence \(|S|\) must be at least two.
* Let  

  \[
  d_1<d_2\le m
  \]

  be the two distances we will actually use.  
  Our aim is to make \(d_1\) as large as possible; then the minimum distance
  in the whole cycle will be \(d_1\).

--------------------------------------------------------------------

## 3.  The optimal value of the minimum distance  

Write \(n=2m\).

*If \(m\) is even* (i.e. \(n\equiv 0\pmod 4\))

\[
\boxed{\displaystyle d_{\max}=m-1=\frac{n}{2}-1 } .
\]

*If \(m\) is odd* (i.e. \(n\equiv 2\pmod 4\))

\[
\boxed{\displaystyle d_{\max}=m-2=\frac{n}{2}-2 } .
\]

These two numbers are the largest possible minima; any larger value would
force every step to be \(\ge m-1\) (or \(\ge m\) when \(m\) is odd), and a
simple parity/gcd argument shows that a Hamiltonian cycle cannot then be
constructed while using at least two different distances.

--------------------------------------------------------------------

## 4.  Proof of optimality  

### 4.1  Why we cannot beat the stated bounds  

Assume we have an \(S\)-Hamiltonian cycle in which every distance is at least
\(m-1\).

*If a step has distance \(m\)*, the two vertices are opposite each other.
If we ever use a step of length \(m\) **twice in a row**, we return to the
starting vertex, producing a 2‑cycle – impossible. Therefore a step of length
\(m\) can be followed only by a step of length \(m-1\) (or smaller).

*If the minimum distance were \(m\)*, all steps would be of length \(m\);
the argument above shows this cannot give a Hamiltonian cycle.
Hence the minimum distance cannot be larger than \(m-1\).

Now suppose the minimum distance were \(m-1\) when \(m\) is odd
(\(n\equiv 2\pmod 4\)).  
Let the two distances be \(m-1\) and \(m\).  
Because \(m\) is odd, the two numbers \(m-1\) and \(n=2m\) have a common
factor \(2\):

\[
\gcd(m-1,2m)=2 .
\]

Consequently the walk that repeatedly adds \(m-1\) (mod \(

*Original question: [Maximizing the distance between consecutive vertices of a cycle graph](https://math.stackexchange.com/questions/5148176/maximizing-the-distance-between-consecutive-vertices-of-a-cycle-graph) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
