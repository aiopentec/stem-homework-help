---
layout: question
title: Eigenvector structure of a Hamiltonian invariant under binary tree symmetries.
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Eigenvector structure of a Hamiltonian
  invariant under binary tree symmetries.'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We are given  

* a **finite binary tree** (every internal node has exactly two children),  
* a Hilbert space whose orthonormal basis consists of the **edge states** of that tree, e.g.  

\[
|e_1\rangle =|N\rangle ,\;|e_2\rangle =|P\rangle ,\;|e_3\rangle =|J\rangle ,\dots ,|e_{15}\rangle =|H\rangle ,
\]

* a **unitary (hence normal) Hamiltonian** \(H\) that **commutes with every symmetry of the tree**.  
  The symmetry group is the group of graph‑automorphisms of the tree – i.e. the set of all permutations of the edges that can be obtained by swapping the left and right sub‑trees at any internal node.

The student wants to know

1. **What can be said about the eigenvectors of \(H\) only from the knowledge that \(H\) is invariant under the tree symmetries?**  
   In particular, how are the eigenvectors organised into independent families (a basis)?

2. **If we force the two “parent” components (the edges attached to the root) to be zero, do the remaining eigenvectors automatically become “localised’’ on one of the sub‑trees?**  
   And is there a systematic way to build a basis that respects the tree symmetry?

---

## 2.  Symmetry → representation theory

### 2.1  The symmetry group of a binary tree  

For a binary tree with \(L\) internal nodes (including the root) the automorphism group is the **wreath product**

\[
\mathcal G \;=\; C_{2}\wr C_{2}\wr\cdots\wr C_{2}\;(L\ \text{times}),
\]

i.e. a direct product of a copy of the two‑element group \(C_{2}\) (swap left/right) for each internal node, together with the obvious way those swaps compose.  
Concretely:

* At the root we may exchange the whole left subtree with the whole right subtree.
* Inside each of those sub‑trees we may again exchange its own left and right children, etc.

Hence every element of \(\mathcal G\) is a *product of independent swaps* at the various nodes.

### 2.2  What invariance means  

The Hamiltonian satisfies  

\[
[H,\,U_g]=0 \qquad\forall g\in\mathcal G,
\]

where \(U_g\) is the unitary operator that permutes the edge basis exactly as the graph automorphism \(g\) does.  
Since \(H\) commutes with *all* \(U_g\), it belongs to the **commutant (centraliser)** of the representation of \(\mathcal G\) on the edge Hilbert space.

The Hilbert space therefore decomposes into **isotypic components** (direct sums of irreducible representations, irreps) of \(\mathcal G\):

\[
\mathcal H = \bigoplus_{\lambda} \bigl(\mathbb C^{m_\lambda}\otimes V_\lambda\bigr),
\]

where  

* \(V_\lambda\) is an irrep of \(\mathcal G\),  
* \(m_\lambda\) is its multiplicity (how many copies appear).

Because \(H\) commutes with every group element, **Schur’s Lemma** tells us that on each isotypic component \(H\) acts as

\[
H\big|_{\mathbb C^{m_\lambda}\otimes V_\lambda}= \mathbf{1}_{V_\lambda}\otimes h_\lambda,
\]

i.e. it is **block‑diagonal**: one block for every irrep, and within a block it is the same operator \(h_\lambda\) on every copy.

Consequences:

* We can **choose a basis** that first picks an irrep label \(\lambda\), then a copy index \(a=1,\dots,m_\lambda\), then a vector inside that irrep.  
* Each eigenvector of \(H\) is either entirely **symmetric** or **antisymmetric** (or more generally transforms according to a definite irrep) under the swaps at every node.

---

## 3.  Concrete construction for a binary tree  

Below we give a *recursive* way to build an orthonormal basis that respects the symmetry. The construction works for any depth; we illustrate it on the picture in the question (a tree of depth 3).

### 3.1  Basis at a single internal node  

Consider a node with two child edges \(e_L\) and \(e_R\). Define

\[
\begin{aligned}
|e_{\text{sym}}\rangle &= \frac{1}{\sqrt{2}}\bigl(|e_L\rangle+|e_R\rangle\bigr) ,\\[2pt]
|e_{\text{asym}}\rangle&= \frac{1}{\sqrt{2}}\bigl(|e_L\rangle-|e_R\rangle\bigr) .
\end{aligned}
\]

*Under the swap that interchanges the left and right child, the first vector is **even** (trivial irrep), the second is **odd** (sign irrep).*  

These two vectors are orthonormal and span the same two‑dimensional subspace as \(\{|e_L\rangle,|e_R\rangle\}\).

### 3.2  Recursion down the tree  

Starting at the leaves and moving upward:

1. **Leaves** have no children, so each leaf edge stays as a one‑dimensional trivial irrep.  
2. **At each internal node** we replace the pair of child basis vectors by the two combinations (sym, asym) defined above.  
3. The **sym** combination becomes the *effective* edge that feeds into the next higher node; the **asym** combination is **already a complete irrep that never mixes with the rest of the tree**, because any higher‑level swap leaves it unchanged (it lives entirely within that node’s two children).

Repeating this procedure yields a global orthonormal set

\[
\bigl\{\,|\,\text{root}\,\rangle,\;|\,\text{sym}_1\rangle,\;|\,\text{asym}_1\rangle,\;
|\,\text{sym}_2\rangle,\;|\,\text{asym}_2\rangle,\dots\bigr\},
\]

where the subscript tells **at which node** the antisymmetric combination was taken.

### 3.3  Block‑diagonal form of \(H\)

Because each antisymmetric vector is already an eigenvector of **all** swaps that involve its own node (it picks up a minus sign) and is invariant under all *other* swaps, the Hamiltonian cannot couple an antisymmetric vector of node \(v\) to any vector that is symmetric at that node. Therefore the matrix of \(H\) in the above basis is **block diagonal**:

| Block | Irrep | Dimension | Physical meaning |
|------|-------|-----------|-------------------|
| Root block | trivial (all swaps +) | 1 | the fully symmetric mode that lives on the whole tree |
| For every internal node \(v\) | sign irrep of the swap at \(v\) | 1 | a mode that lives *only* on the two edges attached to \(v\) (difference between left and right child) |
| For every level \(k\) (except the leaves) | trivial irrep of all swaps **below** that level | \(\#\) | modes that are symmetric inside each subtree but may differ between subtrees of the same parent. These are the “global” modes that propagate up the tree. |

Hence the **independent eigenvectors** can be taken as the vectors belonging to each block; inside a block we diagonalise the (usually small) matrix \(h_\lambda\).

---

## 4.  Answer to the specific questions  

### 4.1  What can we know about the structure of the eigenvectors?

* **Each eigenvector transforms according to a single irrep of the tree‑automorphism group.**  
  Practically this means that for every internal node the eigenvector is either **even** (same amplitude on the two children) or **odd** (opposite amplitude).  
* **The Hilbert space splits into orthogonal invariant subspaces** labelled by the pattern of “even/odd’’ choices on the nodes.  
  The number of subspaces equals \(2^{L}\) (all possible patterns), but many of them are equivalent because sub‑trees of the same shape give rise to identical copies (multiplicity).  
* **Within each subspace the Hamiltonian is the same**; therefore the eigenvalues are *degenerate* with a multiplicity equal to the number of copies of that irrep.

In short, the eigenbasis can be chosen so that each basis vector is a product of

1. a **symmetry label** (which pattern of swaps is even/odd), and  
2. a **local wavefunction** inside the corresponding invariant subspace (found by diagonalising the small block \(h_\lambda\)).

### 4.2  If we set the root edges \(N\) and \(P\) to zero, do the remaining eigenvectors localise on sub‑trees?

*Setting the first two components to zero forces the global **trivial irrep** (the completely symmetric mode that has non‑zero weight on the root edges) to be absent.*  
The remaining subspace decomposes into a direct sum of the **sign irreps** at the root swap and the irreps that are symmetric under the root but have at least one antisymmetric choice deeper in the tree.

- The **sign irrep at the root** is precisely the vector  

  \[
  |\,\psi_{\text{root-asym}}\rangle =\frac{1}{\sqrt{2}}\bigl(|N\rangle-|P\rangle\bigr),
  \]

  which lives **only on the two root edges** – it does **not** extend to deeper edges, so it is *already* fully localised.

- All **other irreps** have the property that they are *symmetric* under the root swap (so they have zero amplitude on the root edges) but may be antisymmetric at lower nodes.  
  Consequently, each such eigenvector has support **only on the edges belonging to the subtree where the first antisymmetric node occurs**.  
  In other words, after we delete the root amplitudes, every eigenvector either

  * is confined to a *single* pair of sibling edges (an “odd’’ mode of some internal node), or  
  * lives on an entire *isomorphic* collection of sub‑trees, being identical on each copy.

Hence **localisation is guaranteed only for the modes that are odd at the *first* node where the pattern becomes odd**. Purely symmetric modes (odd nowhere) are impossible once the root edges are forced to zero – they would be the global symmetric mode that we have removed.

### 4.3  How to construct a symmetry‑adapted basis

1. **Start from the leaves** and assign each leaf edge a basis vector \(|\ell\rangle\).  
2. **Proceed upward**: at every internal node with children \(c_L,c_R\) form  

   \[
   \begin{aligned}
   |\text{sym}_v\rangle &=\frac{1}{\sqrt{2}}\bigl(|c_L\rangle+|c_R\rangle\bigr),\\
   |\text{asym}_v\rangle&=\frac{1}{\sqrt{2}}\bigl(|c_L\rangle-|c_R\rangle\bigr).
   \end{aligned}
   \]

   Keep \(|\text{asym}_v\rangle\) as a **stand‑alone basis vector** (it will never mix with anything else).  
   Replace the pair \((|c_L\rangle,|c_R\rangle)\) by the single vector \(|\text{sym}_v\rangle\) for the purpose of constructing the parent node.

3. **Iterate** until you reach the root. At the root you obtain one final symmetric vector \(|\

*Original question: [Eigenvector structure of a Hamiltonian invariant under binary tree symmetries.](https://math.stackexchange.com/questions/5151480/eigenvector-structure-of-a-hamiltonian-invariant-under-binary-tree-symmetries) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
