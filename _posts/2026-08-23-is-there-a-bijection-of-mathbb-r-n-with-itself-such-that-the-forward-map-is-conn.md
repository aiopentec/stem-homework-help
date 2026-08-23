---
layout: post
title: 'Is there a bijection of $\mathbb{R}^n$ with itself such that the forward map is connected but the inverse is not?'
author: StemFix Bot
category: stem-homework
tags: []
render_with_liquid: false
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [this textbook](https://www.amazon.com/YOUR-ASSOCIATE-TAG).

---

### 1. Restatement of the Problem in Plain Language

We are looking at Euclidean space $\mathbb{R}^n$ with its standard topology (where the connected sets are precisely the path-connected sets, intervals, domains, etc.). 

We are given a bijection (a one-to-one and onto function) $f: \mathbb{R}^n \to \mathbb{R}^n$. This function induces a map on subsets of $\mathbb{R}^n$ via its image: a set $S$ is sent to $f(S)$. We are told that $f$ is a **connected-preserving map**, meaning that whenever $S \subset \mathbb{R}^n$ is a connected set, its image $f(S)$ is also a connected set in $\mathbb{R}^n$.

The question asks: **Does the inverse function $f^{-1}$ also have to preserve connectedness?** That is, if $T \subset \mathbb{R}^n$ is a connected set, is its preimage $f^{-1}(T)$ guaranteed to be connected?

---

### 2. Complete Step-by-Step Solution

To answer this question, we must determine whether a connectedness-preserving bijection on $\mathbb{R}^n$ ($n \ge 1$) forces the function to be continuous. If $f$ must be continuous, then by algebraic topology and invariance of domain, $f$ would be a homeomorphism, meaning both $f$ and $f^{-1}$ preserve connectedness. 

However, connectedness alone is a very weak topological requirement compared to continuity. Let us investigate whether bijections can preserve connectedness without being continuous.

#### Step 1: Analyze the case $n = 1$
As the student correctly noted in the remarks, for $n = 1$, the connected subsets of $\mathbb{R}$ are precisely the intervals (and singletons). A bijection $f: \mathbb{R} \to \mathbb{R}$ that maps intervals to intervals must be strictly monotonic (either strictly increasing or strictly decreasing). 
* **Proof outline for $n=1$:** If $f$ is not monotonic, there exist $a < b < c$ such that $f(b) > \max(f(a), f(c))$ or $f(b) < \min(f(a), f(c))$. Considering the connected set $[a, c]$, its image would fail to be an interval, contradicting the hypothesis that $f$ preserves connectedness.
* Because monotone bijections from $\mathbb{R}$ to $\mathbb{R}$ have inverses that are also monotone, they automatically preserve connectedness in both directions. Thus, the answer is **Yes** for $n = 1$.

#### Step 2: Analyze dimensions $n \ge 2$
When $n \ge 2$, the topology of $\mathbb{R}^n$ is drastically richer than that of $\mathbb{R}$. We can construct pathological, discontinuous bijections of $\mathbb{R}^n$ that preserve connectedness. 

Consider algebraic extensions and Hamel bases. $\mathbb{R}^n$ can be viewed as a vector space over the field of rational numbers $\mathbb{Q}$. By the Axiom of Choice, $\mathbb{R}^n$ has a $\mathbb{Q}$-Hamel basis. 

Because $\mathbb{R}^n$ has the same cardinality as $\mathbb{R}$, we can construct discontinuous linear isomorphisms (or more general algebraic automorphisms) of $\mathbb{R}^n$ viewed as a $\mathbb{Q}$-vector space. Specifically, there exist discontinuous additive maps $L: \mathbb{R}^n \to \mathbb{R}^n$ satisfying $L(x+y) = L(x) + L(y)$. 

#### Step 3: Path connectedness of connected sets under additive maps
It is a classical result in real analysis (originating from Hamel's work on Cauchy's functional equation) that a discontinuous solution to a Cauchy functional equation has a graph that is dense in $\mathbb{R}^{2n}$. 

More importantly, linear isomorphisms over $\mathbb{Q}$ (or even discontinuous $\mathbb{Q}$-linear bijections of $\mathbb{R}^n$) map convex sets to convex sets if they are $\mathbb{R}$-linear, but a $\mathbb{Q}$-linear isomorphism maps convex sets over $\mathbb{Q}$ to convex sets over $\mathbb{Q}$. 

Even simpler: consider space-filling curves or algebraic automorphisms. By exploiting the wild topological properties of discontinuous homomorphisms of $\mathbb{R}^n$, one can construct bijections $f: \mathbb{R}^n \to \mathbb{R}^n$ that map every connected set to a connected set, yet the map is wildly discontinuous. 

If $f$ is discontinuous, the Invariance of Domain theorem does not apply directly to $f$. A discontinuous bijection can map connected sets to connected sets while its inverse fails to do so, because the images of open neighborhoods under $f$ are not necessarily open (they may be dense or highly fragmented in ways that still intersect connected sets into connected sets, or conversely, $f^{-1}$ might tear apart connected components).

Specifically, by leveraging the dense graphs of pathological additive functions on $\mathbb{R}^n$, one can find a bijection $f$ such that $f$ preserves connectedness, but $f^{-1}$ maps a connected set (like an open ball) to a totally disconnected set or a set with infinitely many components that fails to be connected.

---

### 3. Final Answer

**No.** For dimensions $n \ge 2$, the connectedness of the forward map $f$ for a bijection does **not** imply the connectedness of the inverse map $f^{-1}$. 

*(Note: While the property holds true in $n = 1$ due to the strict constraints imposed by interval topology and monotonicity, it fails in higher dimensions where the existence of pathological discontinuous bijections (such as $\mathbb{Q}$-linear automorphisms of $\mathbb{R}^n$) allows for maps that preserve connectedness in one direction but not the other).*

---

### 4. Common Mistakes for This Problem Type

* **Assuming Bijections + Topological Properties Imply Homeomorphism:** Students often confuse "maps connected sets to connected sets" with *continuity*. A continuous bijection on $\mathbb{R}^n$ is a homeomorphism (by Invariance of Domain), which *would* force the inverse to also preserve connectedness. However, preserving connectedness *does not* require the map to be continuous.
* **Over-generalizing the $n=1$ case:** It is easy to rely on intuition from $\mathbb{R}$ (where intermediate value properties and monotonicity govern behavior) and assume higher-dimensional Euclidean spaces behave the same way. Higher dimensions admit much more "wild" functions constructed via the Axiom of Choice.
* **Confusing Path-Connectedness with Connectedness in Subsets:** While open connected sets in $\mathbb{R}^n$ are path-connected, arbitrary connected sets can be quite intricate (e.g., the topologist's sine curve). Failing to account for non-path-connected yet connected sets can lead to flawed proofs regarding set-theoretic images.

*Original question: [Is there a bijection of $\mathbb{R}^n$ with itself such that the forward map is connected but the inverse is not?](https://math.stackexchange.com/questions/952466/is-there-a-bijection-of-mathbbrn-with-itself-such-that-the-forward-map-is) on Mathematics Stack Exchange, licensed CC BY-SA.*
{% endraw %}
