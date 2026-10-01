---
layout: question
title: Intersecting system of finite sets with two properties must be finite?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Intersecting system of finite sets
  with two properties must be finite?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

We are given a collection  

\[
\mathcal F=\{A\subseteq X:\;A\text{ is finite}\}
\]

of **finite** subsets of some (possibly infinite) ground set \(X\).  
The family \(\mathcal F\) has to satisfy two conditions  

| condition | meaning |
|-----------|----------|
| **(1)**   | For every \(A\in\mathcal F\) and every element \(x\in A\) there is another set \(B\in\mathcal F\) whose intersection with \(A\) is exactly the single point \(\{x\}\). |
| **(2)**   | If a finite set \(S\subseteq X\) meets every member of \(\mathcal F\) (i.e. \(S\cap A\neq\varnothing\) for all \(A\in\mathcal F\)), then \(S\) already **contains** a whole member of \(\mathcal F\) as a subset. |

In other words, \(\mathcal F\) is an *intersecting* family (any two members intersect), it is “pairwise‑point‑separable’’ (condition 1), and it is “maximally intersecting’’ (condition 2).

The question is:

> **Must such a family \(\mathcal F\) be finite?**  

If the answer is *yes*, we have to prove that an infinite family cannot exist; if the answer is *no*, we have to exhibit an infinite family that satisfies both (1) and (2).

--------------------------------------------------------------------

## 2.  The answer

**Yes – every family that satisfies (1) and (2) must be finite.**  

The proof proceeds by showing that an infinite family would allow us to construct a *finite* set that hits all members of \(\mathcal F\) but does **not** contain any member, contradicting condition (2).

--------------------------------------------------------------------

## 3.  Detailed proof  

### 3.1  Preliminary notation  

* Let  

  \[
  m:=\min\{|A| : A\in\mathcal F\}
  \]

  (the size of a smallest member of \(\mathcal F\)).  
  Because every set in \(\mathcal F\) is finite, this minimum exists.

* Fix one *minimal* set  

  \[
  A_{0}\in\mathcal F,\qquad |A_{0}|=m .
  \]

* For any set \(A\in\mathcal F\) and any element \(x\in A\) we denote by  

  \[
  B(A,x)\in\mathcal F
  \]

  a set guaranteed by condition (1), i.e.  

  \[
  A\cap B(A,x)=\{x\}.
  \]

  (When several choices are possible we pick one arbitrarily; the proof works for any choice.)

--------------------------------------------------------------------

### 3.2  Two elementary observations  

1. **All members intersect each other.**  
   This is given in the statement (“\(\mathcal F\) is an intersecting system”).

2. **No member of \(\mathcal F\) can be a proper subset of another member.**  
   If \(A\subsetneq B\) were possible, then \(A\cap B=A\neq\varnothing\) but condition (1) would be violated for any \(x\in A\) because any set intersecting \(B\) in exactly \(\{x\}\) would have to miss the rest of \(A\), contradicting the fact that \(A\subseteq B\). Hence every two distinct members intersect **but none contains the other**.

   Consequently all members have size **exactly** \(m\).  
   Indeed, suppose \(C\in\mathcal F\) had \(|C|>m\). Choose \(a\in A_{0}\setminus C\) (possible because \(|A_{0}|=m\) is the minimum). By (1) there exists \(D\in\mathcal F\) with  

   \[
   A_{0}\cap D=\{a\}.
   \]

   Since \(C\) meets every member of \(\mathcal F\), it meets \(D\); the intersection point cannot be \(a\) (because \(a\notin C\)), so \(C\cap D\neq\varnothing\) lies outside \(A_{0}\). But then \(C\) and \(A_{0}\) would intersect in at least two points (the point just found and some point of \(A_{0}\cap C\)), contradicting the fact that **any** two distinct members intersect in exactly one point (the previous paragraph). Therefore \(|C|=m\) for all \(C\in\mathcal F\).

   Hence **every member of \(\mathcal F\) has the same size \(m\)** and any two distinct members intersect in exactly one element.

   In combinatorial language, \(\mathcal F\) is a *finite linear* (or *pairwise‑wise‑1‑intersecting*) hypergraph whose edges all have the same cardinality \(m\).

--------------------------------------------------------------------

### 3.3  A counting argument  

Let us look at the *incidence graph* whose vertex‑set is  

\[
V:=\bigl\{(A,x):A\in\mathcal F,\;x\in A\bigr\}.
\]

For each ordered pair \((A,x)\) we draw an edge to the unique set  

\[
B(A,x)\quad\text{with}\quad A\cap B(A,x)=\{x\}.
\]

Because of the discussion in §3.2, for a fixed \(A\) the sets \(B(A,x)\;(x\in A)\) are all **different** (if \(x\neq y\) then \(B(A,x)\neq B(A,y)\); otherwise the two would intersect \(A\) in two points).  

Consequently each member \(A\) of \(\mathcal F\) gives rise to exactly \(m\) distinct neighbours in the incidence graph.  

Since every set in \(\mathcal F\) has \(m\) elements, the total number of vertices equals  

\[
|V

*Original question: [Intersecting system of finite sets with two properties must be finite?](https://math.stackexchange.com/questions/5150870/intersecting-system-of-finite-sets-with-two-properties-must-be-finite) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
