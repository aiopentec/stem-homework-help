---
layout: question
title: Motivation for interpreting algebraic actions as homomorphisms into transformation
  structures
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Motivation for interpreting algebraic
  actions as homomorphisms into transformation structures'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1. Restating the question in plain language  

The student is asking:

*Why do we usually describe an “action’’ of an algebraic object (a group, a ring, a monoid, …) on another object by a homomorphism into a collection of self‑maps of the latter?*  

In particular they want:

* a conceptual (and historical) explanation of this “action‑as‑homomorphism’’ viewpoint;  
* a description of what algebraic structure (group, monoid, ring, …) the target of the homomorphism must have;  
* an explanation of the role played by the ambient category (e.g. **Set**, **Ab**, **Modₙ**, …) that contains the object being acted upon.

The answer will illustrate the idea with the familiar examples of  

* a left \(R\)-module \(M\) (ring action → ring homomorphism \(R\to \operatorname{End}_{\mathbb Z}(M)\)),  
* a group \(G\) acting on a set \(X\) (group homomorphism \(G\to \operatorname{Aut}_{\mathbf{Set}}(X)\)), and  
* a monoid \(M\) acting on a set \(X\) (monoid homomorphism \(M\to \operatorname{End}_{\mathbf{Set}}(X)\)).

The goal is to make clear **why** this pattern is natural, **where** it comes from historically, and **what** the categorical picture looks like.

---

## 2. Detailed step‑by‑step explanation  

### 2.1. The abstract notion of an action  

1. **Definition (action)**  
   Let \(\mathcal{C}\) be a category, and let \(A\) be an algebraic object (group, monoid, ring, …) that can be regarded as a *single‑sorted algebra* with a binary operation (or several operations) and possibly an identity element.  
   An **action** of \(A\) on an object \(X\) of \(\mathcal{C}\) is a rule  

   \[
   A\times X\;\longrightarrow\; X,\qquad (a,x)\mapsto a\cdot x,
   \]

   satisfying the same equations that the operations of \(A\) satisfy (e.g. \(1\cdot x=x\), \((ab)\cdot x=a\cdot(b\cdot x)\) for a monoid).

2. **What does “the same equations’’ mean?**  
   The equations are exactly the **axioms** that define the algebraic structure of \(A\).  
   - For a **group**: \(e\cdot x = x\) and \((gh)\cdot x = g\cdot(h\cdot x)\).  
   - For a **ring**: \(1\cdot m = m\) and \((rs)\cdot m = r\cdot(s\cdot m)\), together with distributivity over the addition in \(M\).  

   In each case the action must turn the underlying set of \(X\) into a *left module* (or *left \(A\)‑set*) for the algebraic theory of \(A\).

### 2.2. From an action to a homomorphism  

3. **Currying (exponential law)**  
   In any **cartesian closed** category (in particular in **Set**, **Ab**, **Mod\_R**, …) there is a natural bijection  

   \[
   \operatorname{Hom}_{\mathcal{C}}(A\times X,\,X)
   \;\cong\;
   \operatorname{Hom}_{\mathcal{C}}(A,\,X^{X}),
   \]

   where \(X^{X} = \operatorname{Hom}_{\mathcal{C}}(X,X)\) is the **endomorphism object** of \(X\).  
   In concrete categories the right‑hand side is simply the set (or group, ring, …) of all endomorphisms of \(X\).

4. **Preserving the algebraic structure**  
   The axioms of an action translate, under this bijection, into the requirement that the curried map  

   \[
   \widehat{\alpha}\colon A\longrightarrow \operatorname{End}_{\mathcal{C}}(X)
   \]

   be a **homomorphism of algebraic structures** (group homomorphism, monoid homomorphism, ring homomorphism, …).  
   - The identity axiom \(e\cdot x = x\) says \(\widehat{\alpha}(e)=\operatorname{id}_{X}\).  
   - The associativity axiom \((ab)\cdot x = a\cdot(b\cdot x)\) says \(\widehat{\alpha}(ab)=\widehat{\alpha}(a)\circ\widehat{\alpha}(b)\).  

   Thus an action is *exactly* a homomorphism into the endomorphism object.

5. **Why sometimes we take only the *invertible* endomorphisms**  
   The target \(\operatorname{End}_{\mathcal{C}}(X)\) inherits the algebraic structure of \(A\) (it is always a monoid under composition).  
   - If \(A\) itself is a **group**, then a homomorphism from a group must land in the **group of units** of the target monoid, because the image of an invertible element must be invertible.  
   - Consequently we replace \(\operatorname{End}_{\mathcal{C}}(X)\) by its subgroup of units \(\operatorname{End}_{\mathcal{C}}(X)^{\times}= \operatorname{Aut}_{\mathcal{C}}(X)\).  
   - If \(A\) is only a monoid (or a ring), there is no requirement that the image be invertible, so the whole endomorphism monoid (or endomorphism ring) can be used.

### 2.3. Concrete examples  

| Acting object | Object acted on | Classical description of the action | Curried homomorphism | Target structure |
|---|---|---|---|---|
| **Group** \(G\) | Set \(X\) | \(g\cdot x\) with \(e\cdot x=x,\;(gh)\cdot x=g\cdot(h\cdot x)\) | \(\rho(g) = (x\mapsto g\cdot x)\) | \(\operatorname{Aut}_{\mathbf{Set}}(X)\) (bijections) |
| **Monoid** \(M\) | Set \(X\) | Same axioms, no inverses required | \(\lambda(m) = (x\mapsto m\cdot x)\) | \(\operatorname{End}_{\mathbf{Set}}(X)\) (all functions) |
| **Ring** \(R\) | Abelian group \((M,+)\) | \(r\cdot m\) with distributivity, \(1\cdot m=m\) | \(\varphi(r)= (m\mapsto r\cdot m)\) | \(\operatorname{End}_{\mathbb Z}(M)\) (additive maps, a ring) |
| **Algebra** \(A\) over a field \(k\) | Vector space \(V\) | \(a\cdot v\) with linearity in \(v\) and bilinearity in \(a\) | \(\psi(a) = (v\mapsto a\cdot v)\) | \(\operatorname{End}_{k}(V)\) (linear maps, a \(k\)-algebra) |

In each case the **action axioms** are precisely the statement that the curried map is a homomorphism of the appropriate algebraic type.

### 2.4. Historical motivation  

6. **From permutations to representations**  
   *Early group theory* (Cayley, 1854) observed that any abstract group \(G\) can be realized concretely as a group of permutations of the underlying set \(G\) itself: the **regular action** \(g\cdot h = gh\). This is the first explicit use of a homomorphism \(G\to\operatorname{Sym}(G)=\operatorname{Aut}_{\mathbf{Set}}(G)\).  

7. **Cayley’s Theorem** (every group embeds into a symmetric group) gave the first systematic justification for *studying groups via their actions*.  

8. **Modules and representation theory**  
   In the early 20th century, *linear representations* of groups (or of algebras) were introduced: a group \(G\) acts linearly on a vector space \(V\) iff there is a group homomorphism \(G\to\operatorname{GL}(V)=\operatorname{Aut}_{k\text{-}\mathbf{Vect}}(V)\).  

9. **Universal algebra and Lawvere theories** (1960s) formalised the “action = homomorphism’’ principle: a **model** of a Lawvere theory \(\mathbb{T}\) in a category \(\mathcal{C}\) is a product‑preserving functor \(\mathbb{T}\to\mathcal{C}\). For a *single‑sorted* theory (groups, monoids, rings, …) this functor amounts to a homomorphism from the underlying algebra \(A\) into the endomorphism object of the carrier of the model.  

10. **Categorical viewpoint**  
    In a **monoidal category** \((\mathcal{C},\otimes,I)\) an *action* of a monoid object \(M\) on an object \(X\) is a morphism  

    \[
    \alpha\colon M\otimes X\longrightarrow X
    \]

    satisfying the unit and associativity diagrams. By the internal hom adjunction (\(\mathcal{C}\) closed) this is equivalent to a monoid homomorphism  

    \[
    M\;\longrightarrow\;[X,X],
    \]

    where \([X,X]\) is the internal endomorphism monoid. When the monoid \(M\) is a **group object**, the image necessarily lands in the **group of invertible elements** of \([X,X]\). This abstract picture unifies all the concrete cases above.

### 2.5. The role of the ambient category  

11. **What structure does \(\operatorname{End}_{\mathcal{C}}(X)\) inherit?**  
    - In **Set** it is a *monoid* under composition.  
    - In **Ab** (abelian groups) it is a *ring* (addition = pointwise, multiplication = composition).  
    - In **Mod\_R** it is an *\(R\)-algebra* (addition and scalar multiplication are defined pointwise).  
    - In any **closed** monoidal category it is a *monoid object* \([X,X]\).  

12. **Why the category matters**  
    The *type* of homomorphism we can ask for is dictated by the algebraic structure present in \(\operatorname{End}_{\mathcal{C}}(X)\).  
    - If \(\mathcal{C}\) supplies addition (as in **Ab**) we can talk about **ring homomorphisms** for ring actions.  
    - If \(\mathcal{C}\) supplies only composition (as in **Set**) we are limited to **monoid** (or group) homomorphisms.  

    Moreover, the existence of **exponential objects** (or internal homs) is what makes the curried map \(\widehat{\alpha}\) a genuine morphism in \(\mathcal{C}\); without them we would have to step outside the category.

---

## 3. Final answer – concise statement  

> **Answer.**  
> An “action’’ of an algebraic object \(A\) (group, monoid, ring, …) on an object \(X\) of a category \(\mathcal{C}\) is *exactly* a homomorphism from \(A\) into the endomorphism object \(\operatorname{End}_{\mathcal{C}}(X)=\operatorname{Hom}_{\mathcal{C}}(X,X)\).  
> * The axioms of the action translate, via currying, into the condition that the associated map \(A\to\operatorname{End}_{\mathcal{C}}(X)\) preserve the algebraic operations of \(A\).  
> * If \(A\) is a group, the image must consist of invertible endomorphisms, so the target is the **group of automorphisms** \(\operatorname{Aut}_{\mathcal{C}}(X)\).  
> * If \(A\) is a monoid (or a ring), the whole endomorphism monoid (or endomorphism ring) can be used.  
> * Historically this viewpoint goes back to Cayley’s theorem (every group embeds in a symmetric group) and was later systematised by the theory of representations and by Lawvere’s categorical treatment of algebraic theories.  
> * The surrounding category determines what algebraic structure the endomorphism object carries, and therefore which kind of homomorphism (monoid, group, ring, …) is appropriate

*Original question: [Motivation for interpreting algebraic actions as homomorphisms into transformation structures](https://math.stackexchange.com/questions/5152177/motivation-for-interpreting-algebraic-actions-as-homomorphisms-into-transformati) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
