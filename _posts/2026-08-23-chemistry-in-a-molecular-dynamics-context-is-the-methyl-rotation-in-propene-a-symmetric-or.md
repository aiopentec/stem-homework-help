---
layout: post
title: In a molecular dynamics context, is the methyl rotation in propene a symmetric
  or asymmetric internal rotor?
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The student wants to know how to classify the **internal rotation of the methyl group in propene** when we look at it from the point of view of a molecular‑dynamics (MD) simulation, i.e. when the nuclei have kinetic energy and are free to move.  

* Is the rotating fragment a **symmetric internal rotor** (like a three‑fold symmetric top) or an **asymmetric internal rotor** (a general top with three different moments of inertia)?  

The difficulty comes from the fact that  

* the **methyl group** itself is three‑fold symmetric (the three H atoms are equivalent), but  
* the **rest of the molecule** (the \(\ce{C=C–CH2}\) fragment) is not symmetric, and the rotation axis does **not** pass through the centre of mass of the whole molecule.

We have to decide which part of the system determines the “symmetry of the internal rotor” that appears in the kinetic‑energy term of the MD Hamiltonian.

---

## 2.  Step‑by‑step analysis  

### 2.1.  Internal‑rotation Hamiltonian in the Born–Oppenheimer picture  

For a molecule that can be split into two fragments (A = rotating part, B = the remaining “frame”) the **classical** kinetic energy of the internal rotation about the bond axis (taken as the \(z\)‑axis) can be written as  

\[
T_{\rm int}= \frac{1}{2}\,I_{\rm red}\,\dot\phi^{2},
\qquad 
I_{\rm red}= \frac{I_{A}I_{B}}{I_{A}+I_{B}},
\tag{1}
\]

where  

* \(\phi\) is the torsional angle (the methyl rotation angle),  
* \(I_{A}\) and \(I_{B}\) are the moments of inertia of the two fragments **about the same axis** (the C–C bond), and  
* \(I_{\rm red}\) is the **reduced moment of inertia** that appears in the internal‑rotation term of the Hamiltonian.

If the fragments were free to rotate independently about *any* axis, we would have to use the full **inertia tensor** \(\mathbf{I}\) of each fragment and the kinetic energy would contain cross‑terms (Coriolis coupling).  In the usual internal‑rotation treatment the only coordinate that changes is the torsional angle \(\phi\); all other rotational degrees of freedom are treated separately.

### 2.2.  Symmetry of the **rotor itself** (fragment A)

The methyl group \(\ce{CH3}\) has a **local \(C_{3v}\) symmetry** about the C–C bond:

* The three H atoms are related by a \(120^{\circ}\) rotation.
* Consequently its inertia tensor (expressed in its own principal‑axis system) has two equal moments,
  \[
  I_{A}^{(x)} = I_{A}^{(y)} \neq I_{A}^{(z)} .
  \]
  This is the definition of a **symmetric top** (or **symmetric internal rotor**).

Thus, **as a fragment taken by itself, the methyl group is a symmetric rotor**.

### 2.3.  Symmetry of the **frame** (fragment B)

The remainder of propene, \(\ce{CH2=CH–}\), has no three‑fold symmetry about the same axis; its inertia tensor has three distinct principal moments:

\[
I_{B}^{(x)}\neq I_{B}^{(y)}\neq I_{B}^{(z)} .
\]

Therefore the *frame* is an **asymmetric top**.

### 2.4.  What does “internal‑rotor symmetry” mean in MD?

In an MD simulation the **whole molecule** moves, i.e. the two fragments share the same angular momentum.  The kinetic energy of the *combined* system can be written (in the body‑fixed frame) as

\[
T = \frac{1}{2}\,\boldsymbol{\omega}^{\!\top}\,\mathbf{I}_{\rm tot}\,\boldsymbol{\omega}
      + \frac{1}{2}\,I_{\rm red}\,\dot\phi^{2}
      + \text{Coriolis terms},
\tag{2}
\]

where \(\boldsymbol{\omega}\) is the overall rotational angular velocity and
\(\mathbf{I}_{\rm tot}\) is the inertia tensor of the *whole* molecule, evaluated about its centre of mass.

Because the internal‑rotation axis (the C–C bond) **does not pass through the centre of mass**, the tensor \(\mathbf{I}_{\rm tot}\) is **not diagonal** in the basis \(\{x,y,z\}\) that contains the bond axis.  Off‑diagonal elements appear, mixing the internal rotation \(\dot\phi\) with the overall rotation \(\boldsymbol{\omega}\).  In the language of rotor classification this coupling makes the *effective* internal rotor **asymmetric**:

* The three principal moments of the *combined* system are all different.
* The reduced inertia \(I_{\rm red}\) depends on the orientation of the frame, i.e. the kinetic‑energy term cannot be written as a simple \(\frac{1}{2}I\dot\phi^{2}\) with a single constant \(I\) that respects a three‑fold symmetry.

Hence, **in a full MD treatment the internal rotation is described by an asymmetric‑top Hamiltonian** (the so‑called “hindered asymmetric rotor”).

### 2.5.  Why the two viewpoints are not contradictory  

| Perspective | What is held fixed | Rotor symmetry |
|-------------|-------------------|----------------|
| **Fragment‑only picture** (spectroscopy, rigid‑rotor approximation) | The rest of the molecule is taken as a fixed frame; only \(\phi\) changes | **Symmetric top** (the methyl) |
| **Full MD picture** | Nothing is frozen; the centre of mass moves, the bond axis is offset | **Asymmetric top** (overall inertia tensor has three different eigenvalues) |

Both statements are correct; they refer to *different* objects:

* **Symmetric internal rotor** = “the rotating fragment by itself”.
* **Asymmetric internal rotor** = “the whole molecule when the fragment rotates about an axis that is not a principal axis of the whole system”.

Because the MD Hamiltonian must describe the motion of *all* nuclei, the latter is the appropriate classification.

### 2.6.  Quantitative illustration (optional)

Take atomic masses (u): C = 12, H = 1.  

Place the C–C bond along the \(z\)‑axis, origin at the centre of mass of propene (computed from the Cartesian coordinates).  Computing the inertia tensor \(\mathbf{I}_{\rm tot}\) gives (values are illustrative)

\[
\mathbf{I}_{\rm tot} \approx
\begin{pmatrix}
  19.3 & 0.0 & 2.4\\
  0.0 & 18.7 & -1.8\\
  2.4 & -1.8 & 12.5
\end{pmatrix}\; \text{amu·Å\(^2\)} .
\]

The eigenvalues (principal moments) are  

\[
I_{A}=11.9,\qquad I_{B}=18.5,\qquad I_{C}=20.0 \;\text{amu·Å\(^2\)} ,
\]

all distinct → **asymmetric top**.  

If we artificially freeze the frame (set its contribution to the tensor to zero) we obtain for the methyl alone  

\[
\mathbf{I}_{\rm CH_3}=
\begin{pmatrix}
  5.4 & 0 & 0\\
  0 & 5.4 & 0\\
  0 & 0 & 1.1
\end{pmatrix},
\]

which is a **symmetric top** (two equal moments).

---

## 3.  Final answer  

*The methyl group in propene is a **symmetric top** when considered by itself, because its three hydrogens are related by a three‑fold rotational symmetry about the C–C bond.*  

*However, in a molecular‑dynamics simulation where the whole molecule is allowed to translate and rotate, the internal‑rotation axis does not coincide with a principal axis of the total inertia tensor. Consequently the **combined system behaves as an asymmetric top**, and the internal‑rotation term couples to overall rotation. Therefore, in the MD context the methyl rotation is **effectively an asymmetric internal rotor**.*

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Identifying rotor symmetry with the symmetry of the whole molecule.** | The whole molecule may have no \(C_{3}\) axis, but the rotating fragment can still be symmetric. | Distinguish between *fragment* symmetry (local) and *overall* inertia symmetry (global). |
| **Neglecting the offset of the rotation axis from the centre of mass.** | Assuming the axis passes through the COM makes the inertia tensor diagonal, hiding the asymmetric coupling. | Compute the inertia tensor about the COM; check for off‑diagonal elements. |
| **Using only the potential‑energy periodicity (three‑fold) to label the rotor as symmetric.** | Periodicity of the torsional potential tells you about the *potential* symmetry, not about the kinetic‑energy (inertia) part. | Remember that rotor classification depends on the *kinetic* term (moments of inertia). |
| **Treating the internal rotation as completely independent of overall rotation.** | In MD the two motions are coupled via Coriolis terms; ignoring them leads to an incomplete Hamiltonian. | Write the full kinetic energy (Eq. 2) and notice the cross‑terms. |
| **Assuming that “symmetric rotor” always means a spherical top.** | A symmetric top has two equal moments, not necessarily three. | Recall the definition: \(I_{a}=I_{b}\neq I_{c}\). |

By keeping these points in mind, one can correctly decide whether an internal rotation should be modeled as a symmetric or asymmetric rotor in any given theoretical or computational framework.

*Original question: [In a molecular dynamics context, is the methyl rotation in propene a symmetric or asymmetric internal rotor?](https://chemistry.stackexchange.com/questions/76175/in-a-molecular-dynamics-context-is-the-methyl-rotation-in-propene-a-symmetric-o) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
