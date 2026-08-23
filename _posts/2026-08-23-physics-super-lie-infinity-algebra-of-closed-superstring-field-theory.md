---
layout: post
title: Super Lie-infinity algebra of closed superstring field theory?
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What is being asked?  

The question is:

*In bosonic closed string field theory (CSFT) the whole set of tree‑level amplitudes is encoded in an **\(L_{\infty}\)** (i.e. Lie‑infinity) algebra.  Is there an analogous **“super” \(L_{\infty}\)** algebra that governs **closed super‑string field theory** (heterotic, type II, etc.)?  If such a structure exists, how is it built from the world‑sheet data (BRST operator, picture‑changing operators, …) and what are the references that spell it out?*  

In other words we have to answer **yes/no** and, if the answer is “yes”, we must exhibit the algebraic construction and cite the modern literature that completes the picture left open in the 2004 Okawa–Zwiebach paper.

---

## 2.  Step‑by‑step construction  

Below we give a complete, self‑contained derivation of the **super‑\(L_{\infty}\)** (sometimes called a **graded‑\(L_{\infty}\)** or **cyclic \(L_{\infty}\)**) that underlies closed super‑string field theory.  
The derivation proceeds in the same spirit as the bosonic case, but we must keep track of two extra ingredients that are specific to the superstring:

| Feature | Bosonic CSFT | Closed Super‑CSFT |
|---------|--------------|-------------------|
| State space \(\mathcal H\) | Graded by ghost number only | **\(\mathbb Z\)-ghost number** **\(\oplus\) \(\mathbb Z_{2}\) world‑sheet fermion parity** (i.e. a *super* vector space). |
| Picture number | Not present | Physical states live at picture \((-1,-1)\) (NS–NS) or \((-1/2,-1/2)\) (R‑R).  The string field is taken in the **small Hilbert space** (no \(\xi\) zero‑mode). |
| BRST operator | \(Q\) (nilpotent, degree +1) | Same \(Q\) **plus** the picture‑raising operators \(X\) and the inverse picture‑lowering operators \(Y\) that change the picture while preserving cohomology. |
| Inner product | BPZ even symplectic form \(\langle\,,\,\rangle\) (odd degree) | Same BPZ form **restricted to the small Hilbert space**; it is *odd* and **graded‑symmetric** with respect to the total degree (ghost + fermion parity). |

Because the state space is a **super‑vector space**, the multilinear maps we will define must be graded‑symmetric with the *total* degree.  This is precisely the definition of a **super‑\(L_{\infty}\)** algebra.

### 2.1  The underlying graded vector space  

Let  

\[
\mathcal H \;=\; \mathcal H_{\text{NS}} \;\oplus\; \mathcal H_{\text{R}}
\]

be the space of *small‑Hilbert‑space* closed super‑string states.  
Each state carries:

* **Ghost number** \({\rm gh}(\Phi)\in\mathbb Z\);
* **World‑sheet fermion parity** \(\epsilon(\Phi)\in\{0,1\}\) (0 = even, 1 = odd);
* **Picture number** \({\rm pic}(\Phi)\in\frac12\mathbb Z\).

We define the **total degree**

\[
|\Phi|\;=\;{\rm gh}(\Phi)+\epsilon(\Phi)\quad(\text{mod }2),
\]

i.e. the parity of the state.  The vector space \(\mathcal H\) equipped with this \(\mathbb Z_{2}\) grading is the *super* space on which the \(L_{\infty}\) brackets act.

### 2.2  The odd symplectic form  

The BPZ inner product on the sphere,

\[
\omega(\Phi_{1},\Phi_{2})\;:=\;\langle \Phi_{1},\Phi_{2}\rangle_{\text{BPZ}},
\]

has the following properties:

* \(\omega\) is **odd**: \(\deg\omega = -1\) (it lowers ghost number by one);
* \(\omega\) is **graded‑antisymmetric**:

\[
\omega(\Phi_{1},\Phi_{2}) = -(-1)^{|\Phi_{1}||\Phi_{2}|}\,\omega(\Phi_{2},\Phi_{1}).
\]

Thus \((\mathcal H,\omega)\) is a **cyclic** (odd) symplectic super‑vector space, exactly the structure required for a BV formulation.

### 2.3  Multilinear maps from world‑sheet correlators  

For each \(k\ge 1\) we define a multilinear map  

\[
\ell_{k}:\underbrace{\mathcal H^{\otimes k}}_{\text{graded}} \longrightarrow \mathcal H,
\qquad \deg(\ell_{k}) = 1 .
\]

The definition mimics the bosonic case, but we must insert the appropriate picture‑changing operators so that the correlator is non‑vanishing on the sphere:

\[
\boxed{\;
\omega\bigl(\Phi_{0},\ell_{k}(\Phi_{1},\dots,\Phi_{k})\bigr)
   \;=\;
   \frac{1}{k!}\,
   \big\langle\,
      \Phi_{0}(0)\,
      \Phi_{1}(z_{1})\dots \Phi_{k}(z_{k})\,
      \underbrace{X(z_{0})\dots X(z_{0})}_{k-1\;\text{times}}
   \,\big\rangle_{\!\!S^{2}} .
\;}

\]

* \(\Phi_{i}\) are **vertex operators** inserted at distinct points on the sphere (conventionally at \(z_{i}\));
* The operator \(X(z)=\{Q,\xi(z)\}\) is the **picture‑raising** operator of picture +1; we insert \(k-1\) copies so that the total picture number of the correlator is \((-2,-2)\), which is required for a non‑zero BPZ inner product in the small Hilbert space;
* The factor \(1/k!\) removes the over‑counting due to permutations of the integrated vertices.

Because the BPZ inner product is cyclic, the definition of \(\ell_{k}\) is *graded‑symmetric*:

\[
\ell_{k}(\Phi_{\sigma(1)},\dots,\Phi_{\sigma(k)})
   = (-1)^{\epsilon(\sigma;\Phi)}\,
     \ell_{k}(\Phi_{1},\dots,\Phi_{k}),
\]

where \(\epsilon(\sigma;\Phi)\) is the Koszul sign coming from moving the super‑states past each other.

### 2.4  The \(L_{\infty}\) relations  

The maps \(\{\ell_{k}\}_{k\ge1}\) satisfy the **\(L_{\infty}\)** (homotopy‑Lie) identities

\[
\sum_{i+j=n+1}
\!\!
\sum_{\sigma\in\operatorname{Sh}(i,n-i)}
(-1)^{\epsilon(\sigma;\Phi)}\,
\ell_{j}\Bigl(
   \ell_{i}(\Phi_{\sigma(1)},\dots,\Phi_{\sigma(i)}),
   \Phi_{\sigma(i+1)},\dots,\Phi_{\sigma(n)}
\Bigr)=0,
\qquad\forall n\ge 1 .
\tag{2.4

*Original question: [Super Lie-infinity algebra of closed superstring field theory?](https://physics.stackexchange.com/questions/27208/super-lie-infinity-algebra-of-closed-superstring-field-theory) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
