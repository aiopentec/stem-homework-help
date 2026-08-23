---
layout: post
title: Orbifold CFT of $SU(2)/G$ and $SO(3)/G$
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The poster wants a **catalogue** of the rational conformal field theories that are obtained by **orbifolding** the  
\(SU(2)_k\) Wess–Zumino–Witten (WZW) model (and its \(SO(3)_k\) cousin) by a **finite normal subgroup** \(G\subset SU(2)\).

For each such orbifold the student would like to know  

|   | Desired information |
|---|----------------------|
| a) | concrete examples (e.g. \(G= \mathbb Z_2,\;D_n,\;H_8\)…) together with the **modular \(S\)‑ and \(T\)-matrices** and the **fusion rules** of the resulting anyons (the “quasiparticles’’ of the 2+1‑d bulk topological field theory). |
| b) | the **central charge** \(c\) of the 1+1‑d CFT, and the **ground‑state degeneracy on a spatial torus** (i.e. the number of simple objects of the bulk TQFT). |
| c) | if possible, a description of the bulk theory as a **twisted quantum double** \(D^{\omega}(G')\) of some finite group \(G'\). |

The answer must give the above data explicitly (or at least the general formulas that allow one to compute it) for the most common sub‑groups of \(SU(2)\) – cyclic, dihedral and the three binary polyhedral groups – and work out the case \(G=D_2\simeq\mathbb Z_2\times\mathbb Z_2\) (the quaternion group \(H_8\) is isomorphic to the binary dihedral group of order 8).

---

## 2.  Orbifolding a WZW model – the general construction

### 2.1  The parent theory \(SU(2)_k\)

* **Chiral algebra**: the affine Lie algebra \(\widehat{\mathfrak{su}}(2)_k\).  
* **Central charge**  
  \[
  c\;=\;\frac{3k}{k+2}\; .
  \tag{2.1}
  \]
* **Primary fields** (integrable highest‑weight representations) are labelled by a spin  
  \[
  j = 0,\;\frac12,\;1,\;\dots,\;\frac{k}{2}.
  \]
  Their conformal weights are  
  \[
  h_j = \frac{j(j+1)}{k+2}.
  \tag{2.2}
  \]

The theory possesses a **global symmetry** given by the centre of \(SU(2)\),
\[
Z(SU(2))=\{1,-\mathbf 1\}\cong\mathbb Z_{2},
\]
which acts on a primary of spin \(j\) by the phase \((-1)^{2j}\).  More generally any **finite subgroup** \(G\subset SU(2)\) (the *binary* polyhedral groups) acts as an **automorphism** of the chiral algebra – the action is simply the usual left multiplication on the group‑valued field \(g(z,\bar z)\) of the WZW model.

### 2.2  The orbifold theory \( \bigl(SU(2)_k\bigr)/G \)

Given a finite group \(G\) of automorphisms, the **orbifold** is defined by

1. **Projection to \(G\)-invariant states** (the *untwisted* sector).  
2. **Adding twisted sectors** labelled by conjugacy classes \([g]\) of \(G\); a twisted sector is a copy of the original theory with boundary condition \(g\) around the spatial circle.  
3. **Implementing the \(G\)-projection inside each twisted sector** (the *twist‑field* projection).  

The resulting **chiral algebra** is the **\(G\)-invariant sub‑algebra** of the original one, and the **simple objects** (primary fields) of the orbifold are in one‑to‑one correspondence with the pairs  

\[
\boxed{ \; (\,C,\;\rho\,) \;}
\qquad
\begin{array}{c}
C \;=\; \text{conjugacy class of }G,\\[2pt]
\rho \;=\; \text{irreducible representation of the centraliser }N_g:=\{h\in G\mid hg=gh\},
\end{array}
\tag{2.3}
\]

where we pick any representative \(g\in C\).  This is precisely the **label set of the (possibly twisted) quantum double** \(D^{\omega}(G)\).  

*If the original CFT is **holomorphic** (central charge a multiple of 8) the orbifold is *exact

*Original question: [Orbifold CFT of $SU(2)/G$ and $SO(3)/G$](https://physics.stackexchange.com/questions/91178/orbifold-cft-of-su2-g-and-so3-g) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
