---
layout: post
title: 'Are these equivalent (for p-values): super-uniform, stochastically larger
  than / dominating the uniform, conservative?'
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  Restating the question in plain language  

A student has seen three different expressions that seem to describe the same idea about *p‑values*  

| phrase used in the literature | informal meaning |
|------------------------------|-------------------|
| “stochastically larger than (or dominating) a Uniform(0, 1) variable” | the random p‑value **U** satisfies  \(P(U\le t)\le t\) for every \(t\in[0,1]\). |
| “super‑uniform” | the same inequality is written as “the CDF of the p‑value is everywhere **below** the CDF of a Uniform(0, 1)”. |
| “conservative p‑value” (or “conservative test”) | under the null hypothesis the p‑value’s distribution is *at least* as “large” as a Uniform(0, 1); i.e. it is super‑uniform. |

The question is: **Are these three expressions mathematically equivalent?** If not, what are the precise relationships among them?

---

## 2.  Detailed answer – step‑by‑step  

### 2.1.  Basic definitions  

1. **Uniform(0, 1) distribution**  
   \[
   U\sim\mathsf{Unif}(0,1),\qquad 
   F_U(t)=P(U\le t)=\begin{cases}
   0,&t<0\\[2pt]
   t,&0\le t\le 1\\[2pt]
   1,&t>1 .
   \end{cases}
   \]

2. **First‑order stochastic dominance (FSD)**  
   For two random variables \(X\) and \(Y\) we write \(X\;\succeq_{\text{FSD}}\;Y\) (or “\(X\) dominates \(Y\)”) if  
   \[
   P(X\le t)\;\le\; P(Y\le t)\qquad\text{for every }t\in\mathbb R .
   \]
   Equivalently, \(P(X\ge t)\ge P(Y\ge t)\) for all \(t\).

3. **Super‑uniform random variable**  
   A random variable \(P\) taking values in \([0,1]\) is called *super‑uniform* if  
   \[
   F_P(t)=P(P\le t)\le t\qquad\forall\,t\in[0,1].
   \]
   (The inequality is strict for at least one \(t\) when the distribution is *strictly* super‑uniform.)

4. **Conservative p‑value / conservative test**  
   In hypothesis testing, a test that, under the null hypothesis \(H_0\), produces a p‑value \(P\) satisfying  
   \[
   P(P\le \alpha\mid H_0)\;\le\;\alpha\qquad\forall\,\alpha\in[0,1]
   \]
   is called *conservative* (or the p‑value is *conservative*). The condition is exactly the super‑uniform condition applied to the null distribution of the p‑value.

### 2.2.  Showing the equivalence  

| Concept | Formal condition | Relation to Uniform(0, 1) |
|---------|------------------|--------------------------|
| “Stochastically larger than Uniform(0, 1)” | \(F_P(t)\le F_U(t)=t\) for all \(t\in[0,1]\) | By definition, \(P\) **first‑order dominates** the uniform. |
| “Super‑uniform” | Same inequality \(F_P(t)\le t\) for all \(t\in[0,1]\) | Identical to the stochastic‑dominance condition. |
| “Conservative p‑value (under \(H_0\))” | \(P(P\le\alpha\mid H_0)\le\alpha\;\forall\alpha\) | This is precisely the super‑uniform condition applied to the null distribution of the p‑value. |

Thus, for a random variable that lives on \([0,1]\):

\[
\boxed{\;P\text{ is super‑uniform } \Longleftrightarrow 
P\;\text{s.t. } P\;\succeq_{\text{FSD}}\;U(0,1)\;\Longleftrightarrow\;
\text{p‑value is conservative under }H_0\;}
\]

The three phrases refer to the *same mathematical property*.  

The only practical distinction is **context**:

* “Stochastically larger than Uniform” is a generic probability‑theory phrasing.  
* “Super‑uniform” is the term most often used in the multiple‑testing literature (e.g., Benjamini & Hochberg 1995; Storey 2002).  
* “Conservative p‑value” is a testing‑theory phrase: it says that *the test* yields a p‑value whose null distribution satisfies the super‑uniform property.

### 2.3.  Supporting references  

| Source | How it defines the concept |
|--------|----------------------------|
| **Lehmann & Romano (2005), *Testing Statistical Hypotheses***, §2.2 | “A p‑value is *super‑uniform* if under \(H_0\) its CDF is bounded above by the identity on \([0,1]\).” |
| **Benjamini & Hochberg (1995)** | Introduce the “*null p‑values are independent and uniformly distributed*” assumption and later note that the results hold when they are *super‑uniform* (i.e., conservative). |
| **Storey (2002), “A direct approach to false discovery rates”** | Uses the term “*super‑uniform*” for the null p‑value distribution. |
| **Shaked & Shanthikumar (2007), *Stochastic Orders*** | Define first‑order stochastic dominance; when the dominating variable is Uniform(0, 1) we obtain the super‑uniform condition. |
| **Wikipedia – Stochastic dominance** | Gives the FSD definition; substituting \(B=U(0,1)\) yields the same inequality as super‑uniform. |

---

## 3.  Final answer  

Yes.  

* A random variable \(P\) is **super‑uniform** iff its CDF satisfies \(F_P(t)\le t\) for all \(t\in[0,1]\).  
* This inequality is exactly the statement that \(P\) **first‑order stochastically dominates** a Uniform(0, 1) random variable (i.e., is “stochastically larger than uniform”).  
* In hypothesis‑testing terminology, a test whose null‑distribution p‑values satisfy the same inequality is called **conservative**; therefore a *conservative p‑value* is a super‑uniform random variable.

Hence the three expressions are mathematically equivalent; the differences lie only in the terminology used by different research communities.

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing “larger” with “larger CDF”.** | “Stochastically larger” means *larger in the sense of first‑order dominance* (i.e., smaller CDF), not that the random variable takes larger numeric values. | Remember the definition: \(X\succcurlyeq_{\text{FSD}}Y\) ⇔ \(F_X(t)\le F_Y(t)\) for all \(t\). |
| **Thinking a super‑uniform p‑value must be exactly Uniform.** | Super‑uniform only requires the CDF to be **below** the uniform CDF; it can be strictly lower (e.g., a point mass at 0.9). | Write the inequality \(F_P(t)\le t\); equality need not hold everywhere. |
| **Using the term “conservative” for any test with size ≤ α.** | “Conservative” in the p‑value sense specifically refers to the *distribution* of the p‑value under the null, not just the overall type‑I error rate. | Distinguish between “conservative test (type‑I error ≤ α)” and “conservative p‑value (super‑uniform)”. |
| **Applying the definitions outside \([0,1]\).** | The super‑uniform condition is only meaningful for variables supported on \([0,1]\). | Verify the support before invoking the equivalence. |
| **Assuming strict inequality is required.** | “Super‑uniform” (or stochastic dominance) allows equality everywhere (the Uniform case). Strict inequality for some \(t\) is only needed to talk about *strict* dominance. | State clearly whether you need “strictly super‑uniform” (i.e., truly conservative) or “weakly super‑uniform” (includes the exact uniform). |

---

*Original question: [Are these equivalent (for p-values): super-uniform, stochastically larger than / dominating the uniform, conservative?](https://stats.stackexchange.com/questions/419005/are-these-equivalent-for-p-values-super-uniform-stochastically-larger-than) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
