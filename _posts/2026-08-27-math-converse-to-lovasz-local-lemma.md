---
layout: question
title: Converse to Lovasz Local Lemma?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Converse to Lovasz Local Lemma?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We are given a finite family of events  

\[
\mathcal A=\{A_1,\dots ,A_n\}
\]

together with a *dependency graph* \(G=([n],E)\):  
\(A_i\) is independent of all the events \(\{A_j: (i,j)\notin E\}\).

The (asymmetric) Lovász Local Lemma (LLL) says that **if we can find numbers**
\(x_1,\dots ,x_n\in[0,1)\) **satisfying**

\[
\boxed{\; \Pr(A_i)\;\le\; x_i\prod_{(i,j)\notin E}(1-x_j)\qquad\forall i\;}
\tag{1}
\]

then the probability that *none* of the bad events occurs is positive:

\[
\Pr\Bigl(\bigcap_{i=1}^{n}A_i^{c}\Bigr)\;\ge\;\prod_{i=1}^{n}(1-x_i)>0 .
\tag{2}
\]

The question is the *reverse*:  

> Suppose we already know that  
> \(\displaystyle \Pr\Bigl(\bigcap_{i=1}^{n}A_i^{c}\Bigr)>0\).  
> Does this guarantee the existence of numbers \(x_i\in[0,1)\) that satisfy (1)?
> If not, under what extra conditions does such a choice become possible?

The asker also wants to apply the same reasoning to a second family
\(\{B_i\}\) whose individual probabilities are “close” to those of the \(A_i\)’s.

---

## 2.  Detailed answer  

### 2.1  The LLL condition is **not** necessary

The condition (1) is only a *sufficient* condition for positivity of the
intersection.  In general it is **not** necessary.  
A very simple counter‑example already shows that the converse fails.

#### Counter‑example (two dependent events)

*Take \(n=2\) and let the dependency graph contain the edge \((1,2)\);*  
hence the two events may be arbitrarily dependent.

Let  

\[
p:=\Pr(A_1)=\Pr(A_2)=0.9 ,\qquad 
\Pr(A_1\cap A_2)=0.81 .
\]

(These numbers are admissible because the maximum possible
\(\Pr(A_1\cap A_2)\) is \(\min(p,p)=0.9\).)

Then  

\[
\Pr(A_1^{c}\cap A_2^{c}) = 1-\Pr(A_1\cup A_2)
   = 1-(p+p-0.81)=0.01>0 .
\]

Thus the intersection of the complements has positive probability.

Assume we could find \(x_1,x_2\in[0,1)\) satisfying (1).  
Since the graph is complete, the product in (1) for each \(i\) is just
\((1-x_j)\) with \(j\neq i\).  Hence we would need

\[
p\le x_1(1-x_2),\qquad p\le x_2(1-x_1).
\tag{3}
\]

Multiplying the two inequalities gives  

\[
p^{2}\le x_1x_2(1-x_1)(1-x_2)\le \Bigl(\frac{x_1+x_2}{2}\Bigr)^{2}
     \Bigl(1-\frac{x_1+x_2}{2}\Bigr)^{2}\le\frac14,
\]

the last step because the function \(t(1-t)\) attains its maximum
\(1/4\) at \(t=1/2\).  Hence \(p^{2}\le 1/4\), i.e. \(p\le 1/2\), which is
false for \(p=0.9\).  Therefore **no choice of \(x_1,x_2\) can satisfy (1)**,
even though \(\Pr(A_1^{c}\cap A_2^{c})>0\).

The same phenomenon can be amplified to any size \(n\); the LLL
condition is strictly stronger than the mere existence of a
good outcome.

---

### 2.2  The *exact* condition: Shearer’s theorem  

The precise (and optimal) condition for the existence of a point
\((x_1,\dots ,x_n)\) with (1) is given by **Shearer’s Lemma** (also called
Shearer’s version of the LLL).  Define, for a vector of probabilities
\(\mathbf p=(p_1,\dots ,p_n)\) with \(p_i=\Pr(A_i)\),

\[
Q_S(\mathbf p)=\sum_{\substack{I\subseteq S\\ I\text{ independent}}}
               (-1)^{|I|}\,\prod_{i\in I}p_i ,\qquad S\subseteq[n].
\tag{4}
\]

Shearer’s theorem states:

> **Theorem (Shearer, 1985).**  
> Let \(G\) be a dependency graph for the events \(\{A_i\}\).  
> Then  

\[
\Pr\Bigl(\bigcap_{i=1}^{n}A_i^{c}\Bigr)>0
\quad\Longleftrightarrow\quad
Q_S(\mathbf p)>0\;\text{ for **every** }S\subseteq[n].
\tag{5}
\]

Moreover, the region  

\[
\mathcal S(G)=\bigl\{\mathbf p\in[0,1]^n\;:\;Q_S(\mathbf p)>0\;\forall S\bigr\}
\]

is exactly the set of probability vectors for which there exists a
choice of \(\mathbf x\in[0,1)^n\) satisfying (1).  In other words,
**(1) is equivalent to belonging to the interior of Shearer’s region**.

The condition (5) is *necessary and sufficient*.  The usual LLL
assumption (1) is a convenient *sufficient* way to guarantee that all
the \(Q_S\) are positive, because the inequality (1) implies the
stronger bound  

\[
Q_S(\mathbf p)\;\ge\;\prod_{i\in S}(1-x_i)>0 .
\]

Thus the “converse” of the LLL is *Shearer’s condition*; there is no
simpler universal converse involving only the individual probabilities
\(p_i\) and the graph structure.

---

### 2.3  When can we *derive* an LLL‑type bound from a known positive
intersection?

If we *already* know that \(\Pr(\cap A_i^{c})>0\), we may try to **construct**
\(x_i\)’s ourselves.  One constructive way uses the *probability of
survival* in a certain greedy algorithm (the *Moser–Tardos* resampling
procedure).  For each \(i\) define

\[
x_i:=\frac{\Pr(A_i\mid \bigcap_{j\in\Gamma(i)} A_j^{c})}
           {1+\Pr(A_i\mid \bigcap_{j\in\Gamma(i)} A_j^{c})},
\tag{6}
\]

where \(\Gamma(i)=\{j:(i,j)\in E\}\) is the neighbourhood of \(i\) in the
dependency graph.  One can verify (by Bayes’ rule) that this choice
satisfies (1) **provided** the conditional probabilities on the right
hand side are at most the unconditional ones, i.e. the events are *negatively
correlated* with their neighbours.  This is a *sufficient* additional
assumption, not a theorem that holds for arbitrary families.

In practice, the most common way to transfer a positive‑probability
statement from a family \(\{A_i\}\) to another family \(\{B_i\}\) with
similar marginals is:

1. **Show that the vector \(\mathbf q\) of probabilities
   \(q_i=\Pr(B_i)\) belongs to the same Shearer region** as
   \(\mathbf p\).  Because the region \(\mathcal S(G)\) is open, a small
   perturbation of each coordinate preserves positivity; concretely,
   if \(|p_i-q_i|\le \varepsilon\) for all \(i\) and \(\varepsilon\) is
   smaller than the distance of \(\mathbf p\) to the boundary of
   \(\mathcal S(G)\), then \(\mathbf q\in\mathcal S(G)\).

2. Once \(\mathbf q\in\mathcal S(G)\) is known, **choose any
   feasible \(\mathbf x\)** (for instance the one given by the LLL
   criterion (1) applied to \(\mathbf q\)) and conclude
   \(\Pr(\cap B_i^{c})>0\).

Thus the answer to the original problem is:

*If the probability vector of the \(B_i\)’s stays inside the same
Shearer region as that of the \(A_i\)’s (which is guaranteed when the
differences are sufficiently small), then indeed  
\(\Pr(\cap B_i^{c})>0\).*  

Without such a guarantee, the implication can fail.

---

## 3.  Final answer – succinct statement

* The Lovász Local Lemma condition  

\[
\Pr(A_i)\le x_i\prod_{(i,j)\notin E}(1-x_j)
\]

is **sufficient but not necessary** for  
\(\Pr(\bigcap_i A_i^{c})>0\).  A simple example with two highly
probable, dependent events shows that the converse is false.

* The **exact** necessary and sufficient condition is given by **Shearer’s
theorem**:  

\[
\Pr\Bigl(\bigcap_i A_i^{c}\Bigr)>0\quad\Longleftrightarrow\quad
\forall S\subseteq[n]\;:\;
\sum_{\substack{I\subseteq S\\ I\text{ independent}}}
(-1)^{|I|}\prod_{i\in I}\Pr(A_i) \;>\;0 .
\]

The interior of the set defined by these inequalities is precisely the
set of probability vectors for which a feasible \(\mathbf x\) satisfying
the LLL inequality exists.

* Consequently, to transfer positivity from a family \(\{A_i\}\) to a
family \(\{B_i\}\) with the same dependency graph, it suffices to verify
that the vector \((\Pr(B_i))\) also lies inside the same Shearer region
(e.g., the probabilities are close enough to those of the \(A_i\)’s).
When this holds, one can pick any \(\mathbf x\) that works for the
\(A_i\)’s (or recompute them for the \(B_i\)’s) and obtain
\(\Pr(\cap B_i^{c})>0\).

---

## 4.  Common mistakes to avoid

| Mistake | Why it is wrong | How to correct it |
|---------|----------------|-------------------|
| **Assuming (1) ⇔ positivity** | The LLL inequality is only a *sufficient* condition; many positive‑probability instances violate it (see the two‑event counter‑example). | Remember the direction of the implication. Use Shearer’s theorem for a necessary and sufficient condition. |
| **Confusing “dependency graph” with “independence graph”

*Original question: [Converse to Lovasz Local Lemma?](https://math.stackexchange.com/questions/5148017/converse-to-lovasz-local-lemma) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
