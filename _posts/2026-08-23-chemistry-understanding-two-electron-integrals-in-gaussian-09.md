---
layout: post
title: Understanding two-electron integrals in Gaussian 09
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A student calculated the **electron‑repulsion integrals (ERIs)** for a water molecule with a minimal Huzinaga basis set using three quantum‑chemistry programs:

| Program | How the ERIs are printed |
|---------|--------------------------|
| **GAMESS** ( NPRINT=4 ) | every *unique* integral, **without** any symmetry factor |
| **Molpro** ( INT,SPRI=2 ) | unique integrals, but the numbers are sometimes multiplied by 2, 4 or 8 |
| **Gaussian 09** ( SCF(Conventional) IOp(3/33=6) Symmetry=None ) | the printed numbers look “odd”: some are 2‑ or 4‑times larger, some have opposite sign, and many are accompanied by a small integer (1, 2, 4 or 8).  

The student wants to know:

1. **Why Gaussian’s output looks different from the other packages.**  
2. **How to interpret the numbers that Gaussian prints** so that they can be compared directly with GAMESS or Molpro.

The answer must explain the role of *permutational symmetry* (the “redundancy factors”) and any sign conventions that differ between the codes.

---

## 2.  Background – the definition of an ERI and its symmetry

For a set of (real) basis functions \(\{\chi_i\}\) the chemist’s two‑electron integral is

\[
(ij|kl)=\iint \chi_i(\mathbf r_1)\,\chi_j(\mathbf r_1)\,
          \frac{1}{r_{12}}\,
          \chi_k(\mathbf r_2)\,\chi_l(\mathbf r_2)\; d\mathbf r_1 d\mathbf r_2 .
\]

Because the Coulomb operator \(1/r_{12}\) is symmetric with respect to exchange of the two electrons, the integral obeys **eight** symmetry relations:

\[
\begin{aligned}
(ij|kl)&=(ji|kl)=(ij|lk)=(ji|lk) \\
       &=(kl|ij)=(lk|ij)=(kl|ji)=(lk|ji) .
\end{aligned}
\tag{1}
\]

Consequences:

| Situation | Number of *distinct* permutations | Redundancy factor that appears in the **full** 4‑index tensor |
|-----------|-----------------------------------|--------------------------------------------------------------|
| \(i=j,\;k=l,\;i\neq k\) (two pairs equal) | 2 (the two distinct pairs) | 4 |
| All four indices different | 8 | 8 |
| All four indices the same (\(i=j=k=l\)) | 1 | 1 |
| One pair equal, the other two different (e.g. \(i=j\neq k\neq l\)) | 4 | 4 |
| ... | … | … |

Many codes **store only the “unique” integrals** (the ones that satisfy a canonical ordering such as \(i\ge j,\;k\ge l\) and \((i,j)\) precedes \((k,l)\) in a lexicographic sense). When the integral is later used to build the Fock matrix, the program **multiplies** the stored value by the appropriate redundancy factor so that the full 8‑fold symmetry of Eq. (1) is restored.

---

## 3.  What each program actually prints

| Program | What is printed | How to obtain the conventional \((ij|kl)\) |
|---------|-----------------|-------------------------------------------|
| **GAMESS** (NPRINT=4) | The *raw* unique integral **without** any factor. | Already the conventional value; no further scaling needed. |
| **Molpro** (INT,SPRI=2) | The raw unique integral **followed by an integer** (1, 2, 4, 8) that tells how many symmetry‑equivalent copies exist. The integer is *not* multiplied into the printed number. | Multiply the printed number by the integer to get the value that would appear in the fully symmetrised tensor. |
| **Gaussian 09** (IOp(3/33)=6) | For each integral a line such as  

```
   ERI   1   2   3   4   =   0.123456   *   4
```

  where the number after the asterisk is the **redundancy factor**. The number **before** the asterisk is the *unique* integral. | Multiply the number before the asterisk by the factor after the asterisk. The product is the *conventional* \((ij|kl)\) that would be used in a Fock‑matrix construction. |

Thus the “odd” numbers that the student saw in Gaussian are simply the **unscaled** integrals; the factor printed on the same line tells exactly how to rescale them.

### 3.1 Example from the water calculation

Suppose Gaussian prints

```
   ERI   2   5   6   7   =  -0.001234567   *   4
```

*Interpretation*

* Basis‑function indices (Cartesian order) → (2,5|6,7) is a *unique* integral because the indices obey the canonical ordering.  
* The raw value is \(-1.234567\times10^{-3}\) a.u.  
* The factor **4** tells us that there are four symmetry‑equivalent permutations (e.g. (5 2|6 7), (2 5|7 6), …).  

The **conventional** chemist’s ERI is therefore  

\[
(25|67)=4\times(-0.001234567) = -0.004938268\;\text{a.u.}
\]

If GAMESS printed the same integral, it would already show \(-0.004938268\).

---

## 4.  Why some Gaussian numbers appear with the *opposite sign*

Two additional, subtler, sources of apparent sign differences exist:

1. **Cartesian vs. spherical d (or f) functions**  
   The Huzinaga minimal basis for oxygen contains a **d‑type** set (the 2d functions). Gaussian stores them in **pure spherical** form, whereas many older codes (including GAMESS when run with the default `SCF=CONV`) keep the **Cartesian** set \(\{x^2,\,y^2,\,z^2,\,xy,\,xz,\,yz\}\). The linear transformation from Cartesian to spherical contains coefficients of alternating sign (e.g. \(d_{z^2}= \frac{1}{\sqrt{3}}(2z^2-x^2-y^2)\)). Consequently, an integral that involves a spherical d function can appear with the opposite sign compared with a Cartesian‑only program.

2. **Ordering of the Cartesian components**  
   Different programs adopt different internal orderings for the six Cartesian d functions. Gaussian’s order is  

   \[
   xx,\; yy,\; zz,\; xy,\; xz,\; yz,
   \]

   whereas GAMESS (and the original Huzinaga file) often uses  

   \[
   xx,\; xy,\; xz,\; yy,\; yz,\; zz .
   \]

   If the same numerical integral is written with a different index ordering, the sign may flip because the transformation matrix contains negative elements (e.g. the conversion from the \(zz\) component to the spherical \(d_{z^2}\) has a factor \(-\tfrac{1}{2}\)).

**Bottom line:** after correcting for the redundancy factor **and** making sure that the same *type* (Cartesian vs. spherical) and the same ordering of the d‑functions are used, the numbers from Gaussian agree with GAMESS and Molpro to the printed precision.

---

## 5.  Step‑by‑step recipe to compare Gaussian’s ERIs with another program

1. **Identify the basis‑function ordering** used by each code.  
   *For the Huzinaga minimal set* the typical ordering (Cartesian) is  

   ```
   1  O 1s
   2  O 2s
   3  O 2px
   4  O 2py
   5  O 2pz
   6  H1 1s
   7  H2 1s
   ```

   If the code uses spherical d functions, replace indices 3–5 with the five spherical d’s (the program will tell you the order in the header of the integral printout).

2. **Read each Gaussian line** of the form  

   ```
   ERI   i   j   k   l   =   value   *   factor
   ```

   * Compute `value_scaled = value * factor`.  
   * Keep track of the canonical ordering (Gaussian already enforces it).

3. **If comparing to a program that prints Cartesian d integrals**, apply the Cartesian‑↔‑spherical transformation to the Gaussian numbers *before* scaling. The transformation matrix \(C\) for d‑functions is (Cartesian → spherical):

   \[
   \begin{pmatrix}
   d_{xy}\\ d_{xz}\\ d_{yz}\\ d_{x^2-y^2}\\ d_{z^2}
   \end{pmatrix}
   = C\,
   \begin{pmatrix}
   xy\\ xz\\ yz\\ xx-yy\\ 2zz-xx-yy
   \end{pmatrix},
   \qquad
   C = \begin{pmatrix}
   1 & 0 & 0 & 0 & 0\\
   0 & 1 & 0 & 0 & 0\\
   0 & 0 & 1 & 0 & 0\\
   0 & 0 & 0 & 1 & 0\\
   0 & 0 & 0 & 0 & 1
   \end{pmatrix}
   \]

   (In practice you only need the *sign* of the relevant rows; many libraries already provide a routine to convert integrals.)

4. **Compare the scaled (and, if needed, transformed) numbers** with the values printed by GAMESS or Molpro. They should match to the printed number of decimal places (typically 8–10 for a minimal basis).

5. **If a discrepancy remains**, double‑check:  
   * the *integral screening* thresholds (Gaussian may discard integrals smaller than \(10^{-12}\) a.u.; GAMESS may keep them).  
   * the *convention* for the ERI: some codes use the chemist’s \((ij|kl)\) while others use the physicist’s \(\langle ij|kl\rangle = (ij|kl)\). For real basis functions the two are identical, but a sign change can appear for complex spherical harmonics (not an issue for the Huzinaga set).

---

## 6.  Final answer – why Gaussian looks different and how to read it

*Gaussian prints the **raw unique** two‑electron integrals and, on the same line, the **redundancy factor** (1, 2, 4, 8

*Original question: [Understanding two-electron integrals in Gaussian 09](https://chemistry.stackexchange.com/questions/100338/understanding-two-electron-integrals-in-gaussian-09) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
