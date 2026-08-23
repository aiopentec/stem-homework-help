---
layout: post
title: "MNDO integrals in the global coordinate system"
author: StemFix Bot
category: chemistry
tags: [chemistry]
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

In semi‑empirical methods such as **MNDO**, **PMx**, **AM1**, **MNDO/d**, … the two‑center two‑electron Coulomb integrals  

\[
(\mu\nu|\lambda\sigma)
\]

are not evaluated analytically.  
Instead a **classical multipole expansion** (monopole, dipole, quadrupole …) is built **in a local coordinate system that is aligned with the internuclear axis** of the two atoms that carry the basis functions \(\mu,\nu\) and \(\lambda,\sigma\).  

After the local‑frame multipole integrals are obtained, they have to be **rotated back into the global molecular Cartesian frame** (the frame in which the SCF equations are solved).  

The student is asking:

* **How is that rotation performed?**  
  – Which rotation matrix is used?  
  – How are the different multipole ranks (scalar, vector, rank‑2 tensor) transformed?  

A closely related issue appears in the **OMx** orthogonalisation‑based methods, where the resonance (bond‑order) integrals are also computed in a diatomic frame and then rotated.

Below is a **complete, step‑by‑step derivation** of the transformation, written so that you could implement it in a computer program.

---

## 2.  Step‑by‑step derivation  

### 2.1  Geometry – define the two frames  

| Symbol | Meaning |
|--------|---------|
| \(\mathbf{R}_A\) , \(\mathbf{R}_B\) | Cartesian coordinates of the two atoms that define the local frame |
| \(\mathbf{r}= \mathbf{R}_B-\mathbf{R}_A\) | Bond vector (from A to B) |
| \(d = |\mathbf{r}|\) | Internuclear distance |
| \(\hat{\mathbf{e}}_z = \mathbf{r}/d\) | Unit vector along the bond – becomes the **local‑z** axis |
| \(\hat{\mathbf{e}}_x ,\hat{\mathbf{e}}_y\) | Two orthogonal unit vectors that complete a right‑handed Cartesian triad (any convenient choice, e.g. Gram–Schmidt) |
| \(\mathbf{C}\) | **Rotation matrix** that brings a vector expressed in the local frame \((x',y',z')\) to the global frame \((x,y,z)\) :  \(\mathbf{v}_{\text{global}} = \mathbf{C}\,\mathbf{v}_{\text{local}}\) |

The rotation matrix \(\mathbf{C}\) is just the **direction‑cosine matrix** whose rows (or columns) are the global components of the local unit vectors:

\[
\mathbf{C}= \begin{pmatrix}
\hat{\mathbf{e}}_x^{\;T}\\[2pt]
\hat{\mathbf{e}}_y^{\;T}\\[2pt]
\hat{\mathbf{e}}_z^{\;T}
\end{pmatrix}
=
\begin{pmatrix}
c_{x1}&c_{x2}&c_{x3}\\
c_{y1}&c_{y2}&c_{y3}\\
c_{z1}&c_{z2}&c_{z3}
\end{pmatrix},
\qquad
c_{ij}= \hat{\mathbf{e}}_i\!\cdot\!\hat{\mathbf{e}}_j^{\;(global)} .
\]

*Construction of \(\hat{\mathbf{e}}_x,\hat{\mathbf{e}}_y\)*  

A robust, deterministic recipe (used in most semi‑empirical codes) is:

```text
ẑ = (R_B - R_A) / d
if |ẑ·k̂| < 0.9        # k̂ = (0,0,1) is the global Z direction
    x̂ = normalize( k̂ × ẑ )
else
    x̂ = normalize( î × ẑ )   # î = (1,0,0)
end
ŷ = ẑ × x̂
```

The resulting \(\mathbf{C}\) is orthogonal \((\mathbf{C}\mathbf{C}^T = \mathbf{I})\) and has determinant +1.

---

### 2.2  Multipole expansion in the *local* frame  

For a pair of contracted Gaussian (or Slater‑type) atomic orbitals the **two‑center Coulomb integral** is approximated by a sum over *interaction* of *multipole moments* placed on each atom:

\[
(\mu\nu|\lambda\sigma) \;\approx\;
\sum_{L_A,L_B}
\; M^{(L_A)}_{A} \; \Phi^{(L_A,L_B)}(d) \; M^{(L_B)}_{B},
\]

where  

* \(L=0\) → monopole (scalar)  
* \(L=1\) → dipole (vector)  
* \(L=2\) → quadrupole (second‑rank tensor)  

The **local‑frame moments** are obtained by analytic formulas that depend only on the quantum numbers of the orbitals (e.g., s, p, d) and on the distance \(d\).  In the MNDO family the moments are *pre‑tabulated* (see e.g. the original MNDO paper, Table III).  

For the purpose of the rotation we only need to know their *tensor character*:

| Rank | Symbol in local frame | Component layout |
|------|----------------------|------------------|
| 0    | \(Q^{(0)}\)          | scalar (1 number) |
| 1    | \(\mathbf{Q}^{(1)} = (Q_x,Q_y,Q_z)\) | 3‑vector |
| 2    | \(\mathbf{Q}^{(2)}\) – a **symmetric, traceless** \(3\times 3\) matrix (5 independent components) |

The **interaction kernel** \(\Phi^{(L_A,L_B)}(d)\) is a scalar function of the distance (e.g., \(1/d\) for monopole–monopole, \(1/d^3\) for dipole–dipole, etc.) that is also the same in every orientation, because the local frame is aligned with the bond.

---

### 2.3  Rotation rules for tensors  

The rotation of a Cartesian tensor of rank \(L\) is performed by **\(L\) copies of the rotation matrix**:

* **Rank‑0 (scalar)** – invariant:  

  \[
  Q^{(0)}_{\text{global}} = Q^{(0)}_{\text{local}} .
  \]

* **Rank‑1 (vector)** – one copy of \(\mathbf{C}\):  

  \[
  \mathbf{Q}^{(1)}_{\text{global}} = \mathbf{C}\,\mathbf{Q}^{(1)}_{\text{local}} .
  \]

* **Rank‑2 (second‑rank tensor)** – two copies:  

  \[
  \mathbf{Q}^{(2)}_{\text{global}} = \mathbf{C}\,\mathbf{Q}^{(2)}_{\text{local}}\,\mathbf{C}^{\!T}.
  \]

Because the quadrupole matrix is symmetric and traceless, the transformed matrix will automatically retain those properties (orthogonal similarity transformation).

> **Compact notation**  
> For any rank \(L\) tensor \(T^{(L)}\) we can write  

> \[
> T^{(L)}_{\text{global}} = \underbrace{\mathbf{C}\otimes\cdots\otimes\mathbf{C}}_{L\;\text{times}} \; T^{(L)}_{\text{local}} .
> \]

In practice only \(L=0,1,2\) occur, so the three formulas above are sufficient.

---

### 2.4  Putting the pieces together – the full transformed integral  

1. **Compute the direction‑cosine matrix** \(\mathbf{C}\) from the atomic coordinates (Section 2.1).  

2. **Obtain the local‑frame multipole moments** for the two atoms, e.g.  

   \[
   \begin{aligned}
   Q^{(0)}_A,\quad  \mathbf{Q}^{(1)}_A,\quad  \mathbf{Q}^{(2)}_A,\\
   Q^{(0)}_B,\quad  \mathbf{Q}^{(1)}_B,\quad  \mathbf{Q}^{(2)}_B .
   \end{aligned}
   \]

3. **Rotate the vector and tensor moments** to the global frame:

   \[
   \begin{aligned}
   \mathbf{Q}^{(1)}_{A,g} &= \mathbf{C}\,\mathbf{Q}^{(1)}_{A,l}, &
   \mathbf{Q}^{(1)}_{B,g} &= \mathbf{C}\,\mathbf{Q}^{(1)}_{B,l},\\
   \mathbf{Q}^{(2)}_{A,g} &= \mathbf{C}\,\mathbf{Q}^{(2)}_{A,l}\,\mathbf{C}^{\!T}, &
   \mathbf{Q}^{(2)}_{B,g} &= \mathbf{C}\,\mathbf{Q}^{(2)}_{B,l}\,\mathbf{C}^{\!T}.
   \end{aligned}
   \]

4. **Contract the moments with the distance‑dependent kernels**.  
   For each pair of ranks \((L_A,L_B)\) the contribution is

   \[
   \Delta_{L_A L_B}= 
   \begin{cases}
   Q^{(0)}_A Q^{(0)}_B \, \Phi_{00}(d) , & L_A=L_B=0\\[4pt]
   \mathbf{Q}^{(1)}_{A,g}\!\cdot\!\mathbf{Q}^{(1)}_{B,g}\; \Phi_{11}(d) , & L_A=L_B=1\\[4pt]
   \mathrm{Tr}\!\bigl[ \mathbf{Q}^{(2)}_{A,g}\, \mathbf{Q}^{(2)}_{B,g} \bigr]\; \Phi_{22}(d) , & L_A=L_B=2\\[4pt]
   \text{mixed terms }(0\!-\!1,\;0\!-\!2,\;1\!-\!2) \text{ are treated analogously, using the appropriate scalar products.}
   \end{cases}
   \]

   The scalar kernels are the usual **multipole interaction factors** (Mulliken‑type formulae)

   \[
   \begin{aligned}
   \Phi_{00}(d) &= \frac{1}{d},\\
   \Phi_{11}(d) &= \frac{1}{d^{3}},\\
   \Phi_{22}(d) &= \frac{3}{2\,d^{5}},\;\text{etc.}
   \end{aligned}
   \]

   (The exact numerical prefactors differ slightly between MNDO, AM1, PM6 …; they are taken from the model’s parameter set.)

5. **Sum all contributions**:

   \[
   (\mu\nu|\lambda\sigma) \approx
   \sum_{L_A=0}^{2}\;\sum_{L_B=0}^{2} \Delta_{L_A L_B}.
   \]

   Because many of the mixed rank terms are *zero* for the particular combination of orbitals (e.g. an s–p pair has no quadrupole moment), the actual number of terms is small – that is why the method is computationally cheap.

---

### 2.5  How OMx resonance integrals are handled (analogy)  

In the OMx family the **resonance (bond‑order) integrals** \(\beta_{AB}\) are computed from a *local* overlap matrix \(S_{AB}^{\text{loc}}\) that is first expressed in the diatomic frame and then rotated exactly as described above:

1. Build the **local overlap** between the atomic basis functions of A and B (only depends on the internuclear distance).  

2. Rotate the **vector of p‑type overlaps** (there are three p‑orbitals per atom) with the same \(\mathbf{C}\) matrix used for the dipoles.  

3. The **scalar s–s overlap** stays unchanged.  

4. The resulting global‑frame overlap matrix is inserted into the **orthogonalisation transformation** that yields the OMx \(\beta\) parameters.

Thus the *mathematics* of the rotation is identical; only the physical quantity being rotated (overlap rather than electrostatic moment) is different.

---

## 3.  Final answer – the transformation recipe in a nutshell  

1. **Define the bond vector** \(\mathbf{r}= \mathbf{R}_B-\mathbf{R}_A\) and its length \(d\).  
2. **Construct an orthonormal triad** \(\{\

*Original question: [MNDO integrals in the global coordinate system](https://chemistry.stackexchange.com/questions/132067/mndo-integrals-in-the-global-coordinate-system) on Chemistry Stack Exchange, licensed CC BY-SA.*
{% endraw %}
