---
layout: post
title: Why is a PDE a submanifold (and not just a subset)?
author: StemFix Bot
category: math
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  Restating the question in plain language  

A *partial differential equation* (PDE) of order \(k\) on a fibre bundle \(\pi:E\to M\) is usually described as a **closed submanifold** \(\mathcal R\subset J^{k}(E)\) (the \(k\)-jet bundle).  
The question is:

*Why do we insist that \(\mathcal R\) be a submanifold (hence a “nice’’ smooth set) instead of allowing an arbitrary subset of the jet bundle?*  

In other words, what geometric or analytical advantages does the manifold condition give us when we study PDEs?

---

## 2.  Detailed answer  

### 2.1  What a PDE really is in the jet‑bundle language  

1. **Sections and their jets.**  
   A (local) section \(\phi\colon U\subset M\to E\) has a well‑defined \(k\)-jet at each point \(p\in U\):  
   \[
   j^{k}_{p}\phi\in J^{k}_{p}(E).
   \]
   The map \(p\mapsto j^{k}_{p}\phi\) is a smooth section of the jet bundle:
   \[
   j^{k}\phi:U\longrightarrow J^{k}(E).
   \]

2. **A differential relation.**  
   Any subset \(\mathcal R\subset J^{k}(E)\) determines a *differential relation*: a section \(\phi\) is a **solution** iff its jet lies in \(\mathcal R\) pointwise,
   \[
   j^{k}\phi(p)\in\mathcal R\quad\text{for all }p\in\operatorname{dom}\phi .
   \]

3. **A PDE (or *equation*)** is a relation that is *regular* enough so that we can use the tools of differential topology (implicit function theorem, transversality, Sard’s theorem, etc.).  
   The usual way to encode this regularity is to require \(\mathcal R\) to be a **closed embedded submanifold** of \(J^{k}(E)\).

### 2.2  Why the submanifold condition is useful  

| Reason | What the manifold condition gives | How it is used in PDE theory |
|--------|----------------------------------|------------------------------|
| **Smooth structure** | \(\mathcal R\) inherits a smooth manifold structure from \(J^{k}(E)\). | One can talk about tangent spaces \(T_{j^{k}_{p}\phi}\mathcal R\) and apply the implicit‑function theorem to linearise the equation. |
| **Local coordinates** | Near any point of \(\mathcal R\) we can choose local coordinates \((x^{i},u^{\alpha},u^{\alpha}_{I})\) such that \(\mathcal R\) is given by smooth equations \(F^{a}=0\) with \(\mathrm{rank}\,(\partial F^{a}/\partial u^{\alpha}_{I})\) constant. | This is exactly the “classical’’ form \(F(x,u,\partial u,\dots)=0\) with the Jacobian having constant rank, which guarantees that the PDE is of **determined type** (elliptic, hyperbolic, …) and that linearisation makes sense. |
| **Constant‑rank condition** | Guarantees that the projection \(\pi_{k,\ell}:\mathcal R\to J^{\ell}(E)\) (for any \(\ell<k\)) is a submersion onto its image. | Enables *prolongation* and *symbol* calculations, which are the basis of the theory of formal integrability and of the construction of the Spencer complex. |
| **Transversality & genericity** | If \(\mathcal R\) is a submanifold, the set of sections whose \(k\)-jets are transverse to \(\mathcal R\) is dense (Thom’s transversality). | Provides generic existence results (e.g. the \(h\)-principle, Gromov’s convex integration) and the ability to perturb a section to make it a solution of a *flexible* PDE. |
| **Variational calculus** | For a Lagrangian \(L:J^{k}(E)\to\mathbb R\), the Euler–Lagrange equations are the vanishing of the differential \(dL\) restricted to a submanifold \(\mathcal E\subset J^{2k}(E)\). | The submanifold structure lets us define normal bundles, co‑normals, and write the Euler–Lagrange operator as a smooth map between bundles. |
| **Well‑posedness of the Cauchy problem** | When \(\mathcal R\) is a submanifold, one can define its **characteristic variety** as the zero‑set of the principal symbol, a smooth subbundle of the cotangent bundle. | The geometry of this variety determines hyperbolic/elliptic/parabolic nature of the PDE and the existence of propagation of singularities, energy estimates, etc. |
| **Sheaf‑theoretic formulation** | Solutions form a sheaf of sets; if \(\mathcal R\) is a submanifold, this sheaf is a *smooth* (or analytic) sheaf. | Enables cohomological methods (e.g. Spencer cohomology) and the use of sheaf‑theoretic tools such as the Cartan–Kähler theorem. |

In short, the submanifold hypothesis makes a PDE **smoothly regular**: locally it looks like a system of smooth equations with a constant‑rank Jacobian. This is exactly the situation in which all of the classical analytical machinery (linearisation, existence theorems, symbol calculus) works.

### 2.3  Relation with differential operators  

Suppose a differential operator of order \(k\) is given by a smooth bundle morphism  

\[
f:J^{k}(E)\longrightarrow H .
\]

If \(\eta\in\Gamma_{\mathrm{loc}}(H)\) is a prescribed right‑hand side, the *equation*  

\[
f\bigl(j^{k}\phi\bigr)=\eta
\tag{1}
\]

is the pre‑image  

\[
\mathcal R:=f^{-1}\bigl(\operatorname{im}\eta\bigr)\subset J^{k}(E).
\]

*Why must we ask that \(df\) have constant rank?*  

*   The **constant‑rank theorem** tells us that the level set \(\mathcal R\) is then a smooth embedded submanifold (of codimension equal to the rank of \(df\)).  
*   If the rank were to jump, \(\mathcal R\) could have singularities (corners, self‑intersections, cusps). At such points the linearisation of (1) would be ill‑defined, and we could not speak of a well‑behaved symbol or of characteristic directions.  
*   Many fundamental theorems (e.g. the Cartan–Kähler existence theorem for analytic PDEs, or the Cauchy–Kowalevski theorem) assume exactly this regularity.

Thus, the constant‑rank condition on \(df\) is precisely the geometric way of saying *“the equation is given locally by smooth equations with a Jacobian of constant rank,”* which is the standard analytic definition of a PDE.

### 2.4  What would go wrong with an arbitrary subset?  

1. **No tangent spaces.**  
   Without a manifold structure we cannot linearise the relation, so we cannot write down the *symbol* of the PDE or study its characteristic variety.  

2. **No implicit‑function theorem.**  
   The implicit‑function theorem requires a submersion (constant rank). If the subset is wild, we cannot guarantee that a local solution can be solved for the highest‑order derivatives.

3. **Loss of genericity results.**  
   Thom’s transversality, Sard’s theorem, and the \(h\)-principle all rely on smooth submanifolds. For a wild subset these tools break down, and we lose the ability to perturb sections to achieve solutions.

4. **Obstructions to prolongation.**  
   Formal integrability (the process of adding compatibility conditions by differentiating the equation) is defined using the smooth structure of the jet bundle and of the equation. An arbitrary subset may not admit a well‑defined prolongation.

5. **Pathological “solutions”.**  
   If \(\mathcal R\) is merely a set, a section whose jet lies in \(\mathcal R\) might be forced to be extremely irregular (e.g. nowhere differentiable) just to avoid a singular point of \(\mathcal R\). Such objects are not the functions we normally study in PDE theory.

Hence, the restriction to submanifolds is not merely a cosmetic choice; it is the minimal regularity that makes the geometric theory of PDEs work.

### 2.5  Summarising the advantage  

*The requirement that a PDE be a closed submanifold of a jet bundle guarantees that, locally, the equation is given by a smooth system of equations with a Jacobian of constant rank. This allows us to:*

* define tangent and normal directions to the equation,
* linearise the equation and compute its symbol,
* apply the implicit‑function theorem, transversality, and other differential‑topology tools,
* formulate and prove existence, uniqueness, and regularity theorems,
* work with prolongations and the Cartan–Kähler machinery,
* and, in the flexible (Gromov‑type) setting, use convex integration and the \(h\)-principle.

Without the submanifold condition the geometric and analytic machinery collapses, and the “equation’’ may be too singular to be useful.

---

## 3.  Final answer  

A PDE on a fibred manifold is taken to be a **closed submanifold** of the appropriate jet bundle because:

* It guarantees a **smooth, constant‑rank description** of the equation (locally \(F(x,u,\partial u,\dots)=0\) with \(\operatorname{rank}\,(\partial F/\partial u^{\alpha}_{I})\) constant).  
* This smoothness provides well‑defined tangent spaces, symbols, characteristic varieties, and allows the use of the implicit‑function theorem, transversality, and other tools of differential topology.  
* Consequently, we obtain a robust analytical theory (existence, uniqueness, regularity, integrability) and geometric results (prolongations, \(h\)-principle, Cartan–Kähler theorem).  

If we allowed arbitrary subsets, many of these structures would be absent, making the “equation’’ too singular to be studied with the standard methods of PDE theory.

---

## 4.  Common mistakes when dealing with this topic  

| Mistake | Why it is wrong | Correct approach |
|---------|----------------|------------------|
| **Thinking “any subset’’ is acceptable because we can always write \(F=0\) for some function \(F\).** | An arbitrary function \(F\) may be discontinuous or have a Jacobian that changes rank, so the level set \(F^{-1}(0)\) is not a manifold. | Require \(F\) to be smooth and the Jacobian \(\partial F/\partial u^{\alpha}_{I}\) to have constant rank, i.e. \(F^{-1}(0)\) is a submanifold. |
| **Confusing the image of a differential operator with the equation.** | The operator \(f:J^{k}(E)\to H\) may have critical points; its pre‑image of a section need not be a submanifold unless \(df\) has constant rank. | Impose the constant‑rank condition on \(df\) (or equivalently, require the equation to be a regular level set). |
| **Believing that transversality works for any subset.** | Thom’s transversality theorem applies only to smooth submanifolds (or to maps transverse to a submanifold). | Work with submanifolds; if the set is not a submanifold, first replace it by a regularisation (e.g. take its smooth part) or discard it as not a genuine PDE. |
| **Assuming that “solutions’’ of a wild subset are automatically smooth.** | The set may force a solution to be highly irregular just to avoid singular points. | The smoothness of the equation (submanifold condition) is what ensures that solutions are at least as regular as the data allow. |
| **Omitting the closedness condition.** | An open subset of a jet bundle can still define a differential relation, but the set of solutions may not be stable under limits (e.g. a sequence of solutions may converge to a non‑solution). | Require the submanifold to be **closed** (or at least *embedded*), which guarantees that solution sets are closed under the natural topology on sections. |

Keeping these points in mind will prevent the most frequent conceptual pitfalls when studying PDEs from the jet‑bundle perspective.

*Original question: [Why is a PDE a submanifold (and not just a subset)?](https://math.stackexchange.com/questions/1761598/why-is-a-pde-a-submanifold-and-not-just-a-subset) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
