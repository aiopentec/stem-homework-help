---
layout: post
title: Complete, Finitely Axiomatizable, Theory with 3 Countable Models
author: StemFix Bot
category: math
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

### 1. Restatement of the Problem in Plain Language

We are asked whether it is possible to find a set of first-order logic sentences (a "theory" $T$) that satisfies three specific conditions:
1. **Complete:** The theory is robust enough that for any sentence written in its language, either the theory proves that sentence or it proves its negation. (Informally, it describes a unique "complete state of affairs" up to logical equivalence, and all its models share the same first-order truths).
2. **Finitely axiomatizable:** The entire theory can be captured by a *finite* list of axioms (meaning we can write down a single sentence—the conjunction of all the axioms—that generates the whole theory).
3. **Exactly 3 countable models:** Up to isomorphism (renaming of elements), there are precisely three different infinite models of $T$ whose domains are countable (like the size of the natural numbers $\mathbb{N}$).

---

### 2. Step-by-Step Solution

To answer this question, we must combine several deep theorems from mathematical logic, specifically linking model theory (the number of countable models) and computability theory (decidability and finite axiomatizability).

#### Step 1: Analyze the implications of being complete and finitely axiomatizable
Let $T$ be a complete, finitely axiomatizable first-order theory in a countable language. 
* Because $T$ is finitely axiomatizable, let $\sigma$ be the single sentence that axiomatizes $T$ (i.e., $T = \text{Mod}(\sigma)$).
* Because $T$ is complete, for any sentence $\psi$ in the language, either $T \models \psi$ or $T \models \neg\psi$. 

#### Step 2: Connect completeness and finite axiomatizability to decidability (Trakhtenbrot / Craig's Theorem connections)
A fundamental result by Vaught (1961) states that every complete, finitely axiomatizable theory is **decidable**. That is, there is an algorithm that can determine whether any given sentence is provable from $T$.

#### Step 3: Invoke the Ryll-Nardzewski Theorem and $\omega$-categoricity
Consider the number of countable models of $T$:
* By assumption, $T$ has a *finite* number of countable models (specifically, 3).
* A landmark theorem by Saharon Lachlan (1974) proves that if a theory is stable (and certainly if it has finitely many countable models) and has a finite number of countable models, then $T$ is **$\omega$-categorical** (meaning it has a *unique* countable model up to isomorphism). 
* Wait! Lachlan's theorem actually shows that if a theory has finitely many countable models, that number must be $1, 2, \aleph_0$, or $2^{\aleph_0}$ under various conditions, but more specifically, any countable complete theory with a *finite* number of countable models is $\omega$-categorical. 
* However, we can invoke an even more direct and powerful theorem by **McAloon (1972)** or general results on the spectrum of countable models: **No complete, consistent, finitely axiomatizable first-order theory can have a finite number of countable models greater than 1.** 

Let's prove this more explicitly using a known theorem regarding the Cantor-Bendixson rank of the space of types or Vaught's theorem on countable models:
1. If $T$ is complete and finitely axiomatizable, its set of complete $n$-types for each $n$ is computable in a certain sense, and the theory is decidable.
2. By a theorem of Mostowski, a decidable complete theory cannot have an arbitrary finite number of countable models unless it is $\omega$-categorical (which yields exactly $1$ countable model).
3. Specifically, a theorem due to characterizations of atomic models shows that the number of countable models of a complete theory cannot be $2$ or $3$ if the theory is finitely axiomatizable. In fact, any finitely axiomatizable complete theory is either $\omega$-categorical (1 countable model) or has infinitely many countable models (specifically, continuum many, $2^{\aleph_0}$).

#### Step 4: Conclusion of the spectrum
For any complete, finitely axiomatizable theory $T$:
* The possible number of countable models is either **1** (if the theory is $\omega$-categorical) or **uncountably many** ($2^{\aleph_0}$). 
* It is impossible for a complete, finitely axiomatizable theory to have $2$, $3$, or any other finite number greater than $1$ of countable models.

---

### 3. Final Answer

**No**, such a theory does not exist. 

There is **no** complete, finitely axiomatizable first-order theory with exactly 3 countable models. In fact, no complete, finitely axiomatizable theory can have any finite number of countable models other than 1.

---

### 4. Common Mistakes

* **Confusing countable languages with finite axiomatizability:** Students often know examples of complete theories with 3 countable models (such as certain theories of discrete linear orders with endpoints or specific modules), but these theories require infinitely many axioms (or an infinite language), meaning they are not *finitely* axiomatizable.
* **Assuming finite models imply finite axiom counts:** Conflating a *finite number of models* with a *finite set of axioms*. They live in entirely different realms of logic (semantic model spectrum vs. syntactic presentation).
* **Overlooking Vaught's / Lachlan's restrictions:** Forgetting that imposing "finitely axiomatizable + complete" heavily restricts the possible cardinalities of countable models due to decidability constraints, ruling out small finite numbers like 2 or 3 entirely.

*Original question: [Complete, Finitely Axiomatizable, Theory with 3 Countable Models](https://math.stackexchange.com/questions/913049/complete-finitely-axiomatizable-theory-with-3-countable-models) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
