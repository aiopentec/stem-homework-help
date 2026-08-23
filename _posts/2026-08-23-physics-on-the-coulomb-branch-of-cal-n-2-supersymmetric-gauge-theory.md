---
layout: post
title: 'On the Coulomb branch of ${\cal N}=2$ supersymmetric gauge theory'
author: StemFix Bot
category: physics
tags: [physics]
render_with_liquid: false
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

For a four‑dimensional \(\mathcal N=2\) supersymmetric quantum field theory we can look at the set of **Coulomb‑branch operators** – the scalar operators that sit in short \(\mathcal N=2\) multiplets and are neutral under the \(SU(2)_R\) symmetry.  

The *chiral ring* on the Coulomb branch is the set of all products of such operators, modulo any relations that might exist among them.  

The question is:

*Is it always true that this chiral ring has **no non‑trivial relations** – i.e. it is a freely‑generated polynomial ring?*  

If the answer is yes, we want to see **why** this follows directly from the structure of the \(\mathcal N=2\) super‑conformal (or supersymmetry) algebra, and we also want a clear definition of the Coulomb branch in theories that do **not** have a known Lagrangian description.

---

## 2. Step‑by‑step answer

### 2.1  Definition of the Coulomb‑branch operators

In a 4d \(\mathcal N=2\) **SCFT** an operator \(\mathcal O\) belongs to the *Coulomb‑branch chiral ring* iff

| Property | Symbolic condition |
|---|---|
| Lorentz spin | scalar, \(j=\bar j =0\) |
| \(SU(2)_R\) representation | singlet (\(R=0\)) |
| \(U(1)_r\) charge | some non‑negative number \(r\) |
| Shortening | annihilated by all \(\bar Q_{\dot\alpha}^{\,i}\) (the anti‑chiral supercharges) |

Multiplets that satisfy these conditions are called **\(\mathcal E_r\) multiplets** (sometimes denoted \(\widehat{\mathcal B}_R\) for \(R=0\)). The superconformal primary \( \mathcal O\) of an \(\mathcal E_r\) multiplet obeys the **unitarity bound**

\[
\Delta = r\,,\qquad r\ge 0,
\]

so the scaling dimension is *exactly* the \(U(1)_r\) charge and cannot be corrected by quantum effects.

Thus the **Coulomb‑branch chiral ring** \(\mathcal R_{\rm C}\) is the set of all local operators that are primaries of \(\mathcal E_r\) multiplets, closed under the ordinary operator product.

---

### 2.2  The product of two \(\mathcal E\)‑operators

Take two Coulomb‑branch operators  

\[
\mathcal O_1\in\mathcal E_{r_1}\,,\qquad
\mathcal O_2\in\mathcal E_{r_2}.
\]

Their OPE is constrained by the superconformal algebra:

1. **\(SU(2)_R\) singlet** – the product of two singlets is again a singlet.
2. **\(U(1)_r\) charge additive** – the total \(r\)-charge is \(r_1+r_2\).
3. **Shortening condition** – because each factor is annihilated by all \(\bar Q\)’s, the product is also annihilated by the same \(\bar Q\)’s (the \(\bar Q\)’s act as derivations). Hence the only possible superconformal primary appearing on the right‑hand side is itself a \(\mathcal E_{r_1+r_2}\) primary.

Therefore the OPE takes the simple form

\[
\boxed{\;
\mathcal O_1(x)\,\mathcal O_2(0) \;=\; C_{12}\, \mathcal O_{12}(0) \;+\; \text{(descendants)}\;},
\qquad
\mathcal O_{12}\in\mathcal E_{r_1+r_2},
\]

with a *non‑vanishing* structure constant \(C_{12}\). The non‑vanishing follows from the fact that the product of holomorphic functions on a complex variety is never zero unless one of the factors is zero.

Consequences:

* The product of any number of Coulomb‑branch operators is again a unique Coulomb‑branch operator with charge equal to the sum of the individual charges.
* There is **no room** for another independent primary (with the same quantum numbers) to appear, because the unitary representation theory of \(\mathfrak{su}(2,2|2)\) tells us that for each pair \((\Delta=r,R=0,r)\) there is **exactly one** short multiplet \(\mathcal E_r\).

---

### 2.3  Why there cannot be relations

Assume, for contradiction, that there is a non‑trivial polynomial relation among a set of generators \(\{u_i\}\) of the Coulomb‑branch ring:

\[
P(u_1,\dots,u_k)=0,
\qquad
P\neq 0.
\]

Write \(P\) as a sum of monomials
\[
P=\sum_{a} c_a\, u_{i_1}^{\,a_1}\,u_{i_2}^{\,a_2}\cdots u_{i_{k}}^{\,a_k},
\]
where each monomial is an \(\mathcal E_{r_a}\) primary with
\[
r_a = \sum_j a_j\, r_{i_j}.
\]

All monomials in the sum have the *same* total \(U(1)_r\) charge because the polynomial is homogeneous (otherwise the relation would mix operators of different dimensions, which is impossible for a short‑operator equation).  

Now consider the state obtained by acting with each monomial on the vacuum:
\[
|\,\Psi_a\rangle = u_{i_1}^{\,a_1}\cdots u_{i_k}^{\,a_k} |0\rangle .
\]

Because each monomial creates a distinct \(\mathcal E_{r_a}\) primary, the states \(|\Psi_a\rangle\) are **orthogonal** and have **different scaling dimensions** (unless two different monomials accidentally have the same total charge, which would imply a linear relation among the \(r_i\)). Unitarity of the representation guarantees that a linear combination of orthogonal states with **different dimensions** cannot vanish. Hence the only way the sum could be zero is if the coefficients \(c_a\) are all zero, contradicting the assumption that \(P\neq0\).

Therefore **no polynomial relation can exist**. The same argument works for any (possibly infinite) series: the only way a linear combination of distinct \(\mathcal E_r\) primaries could be null is if the representation contained a *null descendant*, which is forbidden by the unitarity bound for \(\mathcal E_r\) multiplets.

Consequences:

* The set of independent Coulomb‑branch operators is in one‑to‑one correspondence with a basis of the **coordinate ring of the Coulomb‑branch moduli space**.
* The coordinate ring of a complex cone that is a *freely generated* polynomial ring \(\mathbb C[u_1,\dots,u_{r}]\), where \(r=\text{rank of the theory}\). The generators may have **non‑integral scaling dimensions** (as happens in non‑Lagrangian SCFTs), but they are still algebraically independent.

---

### 2.4  Connection with the geometric picture

For any \(\mathcal N=2\) theory (Lagrangian or not) the low‑energy description on the Coulomb branch is a **rigid special Kähler** manifold. In the SCFT case this manifold is a **complex cone** \(\mathcal C\) whose apex is the superconformal point. The holomorphic functions on \(\mathcal C\) are precisely the Coulomb‑branch chiral operators.  

A theorem from algebraic geometry says:

> A normal affine complex cone that is *graded* by a single \(\mathbb C^\*\) action (the \(U(1)_r\) scaling) is the spectrum of a **freely generated** graded polynomial ring **iff** the cone is smooth away from the apex (or, more generally, has only isolated singularities that do not affect the graded ring).

All known \(\mathcal N=2\) SCFT Coulomb‑branch cones satisfy this condition. The grading is given by the \(U(1)_r\) charge, and the generators are exactly the \(\mathcal E_r\) primaries. Hence the chiral ring is a polynomial ring.

---

### 2.5  Summary of the logical chain

| Step | What we use | Result |
|------|--------------|--------|
| 1 | Definition of Coulomb‑branch operators = \(\mathcal E_r\) primaries (SU(2)\(_R\) singlet, \(\bar Q\)‑chiral) | Each has protected dimension \(\Delta=r\). |
| 2 | Superconformal algebra → OPE of two \(\mathcal E\) primaries contains **only** a single \(\mathcal E\) primary with charge \(r_1+r_2\). | Multiplication in the ring is *closed* and *associative* with no extra terms. |
| 3 | Unitarity of \(\mathcal E_r\) representations → distinct charges give orthogonal, non‑null states. | No linear combination of distinct monomials can vanish. |
| 4 | Hence **no algebraic relation** among the generators. | The Coulomb‑branch chiral ring is a **free polynomial ring** \(\displaystyle\mathcal R_{\rm C}= \mathbb C[u_1,\dots,u_{\text{rank}}]\). |
| 5 | Geometric interpretation: the Coul

*Original question: [On the Coulomb branch of ${\cal N}=2$ supersymmetric gauge theory](https://physics.stackexchange.com/questions/27267/on-the-coulomb-branch-of-cal-n-2-supersymmetric-gauge-theory) on Physics Stack Exchange, licensed CC BY-SA.*
{% endraw %}
