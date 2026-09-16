---
layout: question
title: Prove non-necessity without logical impasse
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Prove non-necessity without logical
  impasse'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1. What the problem is asking (in plain language)

In a category a **morphism** \(f\colon A\to B\) can have two special properties  

* **Monic** (or **monomorphism**): \(f\) can be cancelled on the left; i.e. if \(g_1,g_2\colon X\to A\) satisfy \(f\circ g_1 = f\circ g_2\) then \(g_1=g_2\).  
* **Epic** (or **epimorphism**): \(f\) can be cancelled on the right; i.e. if \(h_1,h_2\colon B\to Y\) satisfy \(h_1\circ f = h_2\circ f\) then \(h_1=h_2\).

In many familiar categories (sets, groups, vector spaces, …) a morphism that is both monic **and** epic is automatically an **isomorphism** (it has a two‑sided inverse).  

The exercise asks us to **show that this is *not* true in general**: give a concrete category together with a morphism that is both monic and epic but **fails** to be an isomorphism.  

The second part of the question is more philosophical: instead of proving “\(P\) does **not** imply \(Q\)” by a *reductio ad absurdum* (assume \(P\Rightarrow Q\) and derive a contradiction), we should give a **direct counterexample**. The solution will illustrate how a single example settles the “non‑necessity’’ claim.

---

## 2. Step‑by‑step construction of a counterexample  

### Step 1 – Choose a simple category where intuition fails  

The easiest place to find a morphism that is monic and epic but not invertible is the category **\(\mathbf{Set}_{\!*}\)** of **pointed sets** and **base‑point‑preserving functions**.

* An **object** is a pair \((X,x_0)\) where \(X\) is a set and \(x_0\in X\) is a distinguished element (the *base point*).  
* A **morphism** \(\;f\colon (X,x_0)\to (Y,y_0)\) is a function \(f\colon X\to Y\) such that \(f(x_0)=y_0\).

Why this category?  
* It contains many morphisms that are not bijections, yet the usual “cancellation” properties can still hold.  
* It is small enough to write down an explicit map.

### Step 2 – Define the objects and the morphism  

Take the following two pointed sets:

\[
A=(\{0,1\},0),\qquad B=(\{0\},0).
\]

Thus  

* \(A\) has two elements, with \(0\) the base point.  
* \(B\) has a single element, which is necessarily the base point.

Define a morphism  

\[
f\colon A\longrightarrow B,\qquad f(0)=0,\;f(1)=0 .
\]

Because both source and target base points are sent to the target base point, \(f\) is indeed a morphism in \(\mathbf{Set}_{\!*}\).

### Step 3 – Show that \(f\) is **monic**  

Take any two morphisms \(g_1,g_2\colon (X,x_0)\to A\) such that  

\[
f\circ g_1 = f\circ g_2 .
\]

Both composites are maps \(X\to B\) that must send every element of \(X\) to the unique element \(0\) of \(B\); thus they are *identical* functions.  

But the only way two base‑point‑preserving maps into \(A\) can give the same composite is that they agree on **every** element of \(X\). Indeed, for any \(x\in X\),

\[
f\bigl(g_1(x)\bigr)=0 = f\bigl(g_2(x)\bigr),
\]

and the only pre‑image of \(0\) under \(f\) is the whole set \(\{0,1\}\). However, the base‑point condition forces \(g_i(x_0)=0\).  
If there existed an \(x\) with \(g_1(x)=1\) while \(g_2(x)=0\), the composites would still be equal (both give \(0\)). Hence we need a more careful argument:

Because the target \(B\) has **only one** element, the equality \(f\circ g_1 = f\circ g_2\) tells us nothing about the values of \(g_1\) and \(g_2\).  
In fact, **any** two morphisms into \(A\) satisfy the equality of composites, because the composite lands in the one‑point set.  

Consequently, the *cancellation condition* for monomorphisms is **vacuously true**: there is **no** pair \(g_1\neq g_2\) that could violate it, because the premise “\(f\circ g_1 = f\circ g_2\)” is always satisfied, but the conclusion “\(g_1=g_2\)” is not required in the definition of a monomorphism.  

Wait—this is a subtle point. In the definition of monomorphism we require:  

> For *all* objects \(X\) and *all* morphisms \(g_1,g_2\colon X\to A\),  
> \(f\circ g_1 = f\circ g_2 \implies g_1 = g_2\).

Because the implication’s antecedent is **always true**, the only way the implication could fail is if we could find \(g_1\neq g_2\) with the same composite. But in \(\mathbf{Set}_{\!*}\) we *can* find such a pair: take \(X=A\) and let \(g_1=\operatorname{id}_A\), \(g_2\) be the constant map sending both elements to the base point \(0\). Both are base‑point‑preserving, and

\[
f\circ g_1 = f = f\circ g_2 .
\]

Thus the implication **fails**; consequently \(f\) is **not** monic.  

Our earlier attempt was wrong! We need a different category where the monic condition really holds.

### Step 4 – Switch to a better category: **\(\mathbf{Ring}\)** (commutative rings with unity)  

In the category **\(\mathbf{Ring}\)** a morphism is a unital ring homomorphism.  

Consider the inclusion  

\[
i\colon \mathbb{Z} \longrightarrow \mathbb{Q},
\]

the canonical embedding of the integers into the rational numbers.

* It is **monic**: ring homomorphisms in \(\mathbf{Ring}\) are always monomorphisms iff they are injective as functions, and \(i\) is injective.  
* It is **epic**: surprisingly, \(i\) is an epimorphism in \(\mathbf{Ring}\) even though it is not surjective.  
  * Proof of epicness: let \(\varphi,\psi\colon \mathbb{Q}\to R\) be ring homomorphisms (with \(R\) any ring) such that \(\varphi\circ i = \psi\circ i\).  
    This means \(\varphi(n)=\psi(n)\) for every integer \(n\).  
    Any rational number can be written as \(n/m\) with \(n,m\in\mathbb{Z}\), \(m\neq 0\). Because homomorphisms preserve addition and multiplication and send \(1\) to \(1\), the value of \(\varphi\) on \(n/m\) is forced to be \(\varphi(n)\,\varphi(m)^{-1}\) (the inverse of \(\varphi(m)\) exists because \(\varphi(m)\) must be a unit in any ring that receives a homomorphism from a field). The same holds for \(\psi\). Since \(\varphi\) and \(\psi\) agree on all integers, they agree on all fractions, hence \(\varphi=\psi\).  
  Therefore \(i\) is epic.

* Yet \(i\) is **not** an isomorphism: it is not surjective, so no inverse homomorphism \(\mathbb{Q}\to\mathbb{Z}\) exists.

Thus we have a morphism that is both monic and epic but not an isomorphism.

### Step 5 – Verify each property formally  

| Property | Verification |
|----------|---------------|
| **Monic** | In \(\mathbf{Ring}\), a morphism \(f\) is monic ⇔ the underlying function of sets is injective. The map \(\mathbb{Z}\to\mathbb{Q}\) sends distinct integers to distinct rationals, so it is injective ⇒ monic. |
| **Epic** | Let \(\alpha,\beta:\mathbb{Q}\to R\) be ring homomorphisms with \(\alpha\circ i = \beta\circ i\). For any \(q\in\mathbb{Q}\) write \(q=n/m\). Then \(\alpha(q)=\alpha(n)\,\alpha(m)^{-1} = \beta(n)\,\beta(m)^{-1} = \beta(q)\). Hence \(\alpha=\beta\). Thus \(i\) is epic. |
| **Not an isomorphism** | An isomorphism in \(\mathbf{Ring}\) must be a bijective ring homomorphism. The inclusion \(\mathbb{Z}\hookrightarrow\mathbb{Q}\) is not surjective, therefore it cannot have a two‑sided inverse. |

### Step 6 – Concluding the logical point  

Because we have **explicitly produced** an object (the morphism \(i:\mathbb{Z}\to\mathbb{Q}\)) that satisfies the antecedent “monic **and** epic’’ while failing the consequent “isomorphism”, we have *directly* demonstrated that the implication

\[
\text{(monic \(\wedge\) epic)} \;\Longrightarrow\; \text{isomorphism}
\]

is **not universally valid** in the category \(\mathbf{Ring}\). No proof by contradiction is needed; a single counterexample suffices.

---

## 3. Final answer  

A morphism can be both monic and epic without being an isomorphism.  

**Counterexample:** In the category **\(\mathbf{Ring}\)** of (commutative) rings with unity, the canonical inclusion  

\[
i\colon \mathbb{Z}\hookrightarrow \mathbb{Q}
\]

is  

* **monic** (injective as a function),  
* **epic** (any two ring homomorphisms out of \(\mathbb{Q}\) that agree on the integers must agree everywhere),  

but it is **not** an isomorphism (it is not surjective, so no inverse homomorphism exists).  

Therefore the statement “every morphism that is both monic and epic is an isomorphism’’ is **false** in general. The existence of this single example settles the “non‑necessity’’ claim without any need for a proof‑by‑contradiction.

---

## 4. Common Mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using a set‑theoretic intuition** (“monic = injective, epic = surjective”) and concluding that monic + epic ⇒ bijective. | In many concrete categories (Set, Group, Vect) this equivalence holds, but it fails in categories where epimorphisms are not surjective (e.g., \(\mathbf{Ring}\), \(\mathbf{Top}\)). | Remember that “epic’’ is a *categorical* cancellation property, not necessarily surjectivity. |
| **Choosing a category where the morphism is not monic** (as happened with the pointed‑set example). | If the morphism fails one of the two required properties, the example does not address the claim. | Verify *both* monic and epic conditions before declaring a counterexample. |
| **Thinking that a counterexample must be “exotic’’** (very large or abstract). | Simple, well‑known algebraic categories often contain the needed example. | Look first at standard algebraic categories (rings, modules, topological spaces) before resorting to more sophisticated constructions. |
| **Relying on a proof by contradiction** to show “not every monic‑epic is iso”. | While valid, it does not provide the concrete information the problem asks for. | Provide an explicit morphism that satisfies the hypothesis but not the conclusion; that directly exhibits the failure of the implication. |
| **Confusing “epic in a subcategory’’ with “epic in the ambient category”.** | A morphism may be epic in a subcategory (e.g., monoids) but not in the larger one. | State clearly which category you are working in and verify the epic property **in that category**. |

By checking each property carefully and presenting the explicit inclusion \(\mathbb{Z}\to\mathbb{Q}\) as above, we avoid these pitfalls and give a clean, rigorous answer.

*Original question: [Prove non-necessity without logical impasse](https://math.stackexchange.com/questions/5149501/prove-non-necessity-without-logical-impasse) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
