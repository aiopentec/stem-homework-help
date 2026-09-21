---
layout: question
title: Electron-electron interactions in polyelectronic atoms
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Electron-electron interactions in polyelectronic
  atoms'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

For an atom that has more than one electron the exact Schrödinger equation contains a term  

\[
\hat V_{ee}= \sum_{i<j}\frac{e^{2}}{4\pi\varepsilon_{0}\,r_{ij}}
\]

that couples the motion of all the electrons.  
Because this term makes the problem non‑separable, textbooks first **ignore** it, solve the “independent‑electron’’ problem, and then **add** the electron‑electron interaction back as a perturbation.

The student wants to know:

* **Why is it reasonable to treat the electron‑electron term as a small correction?**  
  (Is there a physical picture such as “the electrons spend most of the time far apart’’ that justifies it?)

* **Are there quantitative arguments or explicit calculations that show the approximation works?**  
  (e.g. order‑of‑magnitude estimates, first‑order perturbation results for real atoms.)

Below is a step‑by‑step answer that addresses both points.

---

## 2.  Detailed reasoning and calculations  

### 2.1  The full Hamiltonian for an \(N\)-electron atom  

\[
\hat H = \underbrace{\sum_{i=1}^{N}\Big[-\frac{\hbar^{2}}{2m}\nabla_i^{2}
-\frac{Z e^{2}}{4\pi\varepsilon_{0}\,r_i}\Big]}_{\displaystyle \hat H_{0}\;(\text{independent electrons})}
\;+\;
\underbrace{\sum_{i<j}\frac{e^{2}}{4\pi\varepsilon_{0}\,r_{ij}}}_{\displaystyle \hat V_{ee}\;(\text{electron–electron repulsion})}.
\]

* \(\hat H_{0}\) is a sum of **hydrogen‑like** Hamiltonians with nuclear charge \(Z\).  
* \(\hat V_{ee}\) couples the electrons; it is the only piece that prevents exact separation.

The idea is to treat \(\hat V_{ee}\) as a perturbation to \(\hat H_{0}\).

---

### 2.2  Physical picture – why might \(\hat V_{ee}\) be “small’’?

1. **Dominance of the nuclear attraction**  
   For a given electron the attractive potential is \(-Z/r\).  
   The average distance of an electron from the nucleus in a hydrogen‑like orbital scales as  

   \[
   \langle r\rangle \sim \frac{a_{0}}{Z_{\text{eff}}}
   \]

   where \(a_{0}\) is the Bohr radius and \(Z_{\text{eff}}\) is the **effective** nuclear charge felt by that electron (typically close to \(Z\) for inner shells, and a bit smaller for outer shells because of screening).

2. **Screening reduces the repulsion**  
   The repulsive term between two electrons behaves as \(+1/r_{12}\).  
   In a many‑electron atom each electron is partially screened by the others, so the **average** inter‑electronic distance is **larger** than the average electron–nucleus distance.  

   Roughly  

   \[
   \langle r_{12}\rangle \;\approx\; \langle r_{1}\rangle+\langle r_{2}\rangle \;\sim\; \frac{2a_{0}}{Z_{\text{eff}}}.
   \]

3. **Order‑of‑magnitude ratio**  

   \[
   \frac{\langle V_{ee}\rangle}{\langle V_{en}\rangle}
   \sim\frac{e^{2}/\langle r_{12}\rangle}{Z e^{2}/\langle r\rangle}
   \sim\frac{1}{Z}\,\frac{\langle r\rangle}{\langle r_{12}\rangle}
   \sim\frac{1}{Z}\,\frac{1}{2}\;=\;\mathcal O\!\left(\frac{1}{Z}\right).
   \]

   For **large \(Z\)** the electron‑electron repulsion is a **\(1/Z\)** correction to the dominant nuclear attraction.  
   Even for relatively small \(Z\) (e.g. He, \(Z=2\)) the ratio is only about 0.5, which still allows a perturbative treatment—especially because the repulsion is spread over many pairs of electrons.

Thus the **central‑field picture** (each electron moves in an average, spherically symmetric potential created by the nucleus plus the smeared‑out charge of the other electrons) captures the bulk of the physics; the residual part of \(\hat V_{ee}\) that is not already included in the averaged field is left for perturbation theory.

---

### 2.3  First‑order perturbation theory – a concrete example (Helium)

Take the simplest multi‑electron atom, He (\(Z=2\), two electrons).  

1. **Zeroth‑order (independent‑electron) wavefunction**  

   Each electron is placed in the hydrogenic 1s orbital with nuclear charge \(Z\).  

   \[
   \psi^{(0)}(\mathbf r_1,\mathbf r_2)=\phi_{1s}^{Z}(\mathbf r_1)\,\phi_{1s}^{Z}(\mathbf r_2),
   \qquad
   \phi_{1s}^{Z}(\mathbf r)=\frac{Z^{3/2}}{\sqrt{\pi a_{0}^{3}}}\,e^{-Zr/a_{0}} .
   \]

2. **Zeroth‑order energy**  

   \[
   E^{(0)} = 2\bigl(-\frac{Z^{2}}{2}R_{\infty}\bigr)= -2Z^{2}R_{\infty}
          = -2(2)^{2}\,13.6057\;\text{eV}
          = -108.8\;\text{eV}.
   \]

   (Here \(R_{\infty}=13.6057\;\text{eV}\) is the Rydberg.)

3. **First‑order correction**  

   \[
   E^{(1)} = \langle\psi^{(0)}|\hat V_{ee}|\psi^{(0)}\rangle
          = \biggl\langle\frac{e^{2}}{4\pi\varepsilon_{0}r_{12}}\biggr\rangle .
   \]

   The integral can be evaluated analytically (or looked up):

   \[
   \boxed{E^{(1)} = \frac{5}{4}\,Z\,R_{\infty}} .
   \]

   For helium (\(Z=2\))  

   \[
   E^{(1)} = \frac{5}{4}\times 2 \times 13.6057\;\text{eV}
          = 34.01\;\text{eV}.
   \]

4. **First‑order total energy**

   \[
   E_{\text{He}}^{(0+1)} = E^{(0)}+E^{(1)}
                        = -108.8\;\text{eV}+34.0\;\text{eV}
                        = -74.8\;\text{eV}.
   \]

   The **experimental** ground‑state energy of He is \(-78.98\;\text{eV}\) (ionisation energy 24.59 eV).  

   The error after the *first* perturbative correction is only **≈5 %**.  

5. **Second‑order correction** (optional, shows rapid convergence)  

   Using standard non‑degenerate perturbation theory one finds  

   \[
   E^{(2)}\approx -1.0\;\text{eV},
   \]

   giving  

   \[
   E^{(0+1+2)}\approx -75.8\;\text{eV},
   \]

   already within **4 %** of the exact value.  More sophisticated treatments (variational Hylleraas, configuration interaction) push the error below \(10^{-4}\) eV, but the *trend* is clear: the electron‑electron term is a modest correction.

---

### 2.4  Scaling to larger atoms  

For a general atom with many electrons, one can repeat the same reasoning:

* The **zeroth‑order** Hamiltonian is a sum of hydrogenic orbitals with **effective nuclear charges** \(Z_{\text{eff}}(n\ell)\) that account for the average screening.  Values of \(Z_{\text{eff}}\) are given by Slater’s rules or obtained self‑consistently in a Hartree–Fock calculation.

* The **first‑order** energy correction is the expectation value of the **residual** part of the electron‑electron repulsion, i.e.

  \[
  E^{(1)} = \frac12\sum_{i\neq j}\bigl(J_{ij}-K_{ij}\bigr),
  \]

  where  

  \[
  J_{ij}= \iint |\phi_i(\mathbf r_1)|^{2}\,\frac{e^{2}}{4\pi\varepsilon_{0}r_{12}}\,|\phi_j(\mathbf r_2)|^{2}\,d^3r_1d^3r_2
  \]

  (Coulomb integral) and  

  \[
  K_{ij}= \iint \phi_i^{*}(\mathbf r_1)\phi_j(\mathbf r_1)\,
          \frac{e^{2}}{4\pi\varepsilon_{0}r_{12}}\,
          \phi_j^{*}(\mathbf r_2)\phi_i(\mathbf r_2)\,d^3r_1d^3r_2
  \]

  (exchange integral).  

  In Hartree–Fock the **exchange term** is already included in the self‑consistent field, so the remaining part to be treated perturbatively is usually **small** (a few percent of the total binding energy).

* **Quantitative benchmark** – Neon (\(Z=10\)).  

  * Hartree–Fock (self‑consistent field) total energy: \(-1285.0\;\text{eV}\).  
  * Adding the second‑order Møller–Plesset (MP2) correlation correction: \(-1290.2\;\text{eV}\).  
  * Exact non‑relativistic energy (from full CI calculations) ≈ \(-1290.6\;\text{eV}\).  

  The MP2 correction (the perturbative treatment of the *correlation* beyond the mean field) accounts for **≈0.4 %** of the total energy, confirming that the independent‑electron picture captures the overwhelming majority of the binding.

---

### 2.5  Summary of the justification  

| Argument | What it tells us |
|----------|------------------|
| **Order‑of‑magnitude estimate** \(\displaystyle \frac{V_{ee}}{V_{en}} \sim \frac{1}{Z}\) | Electron‑electron repulsion is a \(1/Z\) correction; for \(Z\ge 2\) it is already smaller than the main nuclear term. |
| **Screening & average distances** | The average inter‑electronic distance is larger than the electron‑nucleus distance, further reducing the repulsion. |
| **Perturbation theory on simple atoms** (He, Li\(^+\), Be\(^{2+}\), …) | First‑order correction already gives energies within a few percent of the exact result. |
| **Hartree–Fock + MP2/CI** for many‑electron atoms | Correlation (the part not captured by the averaged field) contributes at the level of \(10^{-3}\)–\(10^{-2}\) of the total binding energy. |
| **Variational principle** | The Hartree–Fock (independent‑electron) energy is an upper bound; adding the perturbative correction lowers the energy, moving it toward the exact value. |

Hence, **the independent‑electron model plus perturbative

*Original question: [Electron-electron interactions in polyelectronic atoms](https://physics.stackexchange.com/questions/876240/electron-electron-interactions-in-polyelectronic-atoms) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
