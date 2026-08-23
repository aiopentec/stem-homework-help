---
layout: post
title: "How to calculate transition dipole moment from two known wavefunctions"
author: StemFix Bot
category: chemistry
tags: [chemistry]
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [this textbook](https://www.amazon.com/YOUR-ASSOCIATE-TAG).

---

## 1.  What the question is asking (plain language)

You have two *one‑electron* wavefunctions – usually the ground‑state (state 1) and an excited‑state (state 2) – that are expressed as linear combinations of atomic orbitals (AOs).  
From the MO‑coefficient matrices of the two states you want to obtain the **transition dipole moment (TDM)**  

\[
\boldsymbol\mu_{12}= \langle\Psi_1|\hat{\boldsymbol\mu}|\Psi_2\rangle
\]

for each Cartesian direction ( X, Y, Z ).  
The problem is to write down, in a step‑by‑step way, how to construct the *transition density matrix* from the two coefficient matrices and then contract it with the dipole‑integral matrix (the “multipole matrix” in the OP).  

---

## 2.  Full derivation – every step shown

Below we assume  

* a **real** Gaussian AO basis (the formulas are the same for complex orbitals, only a complex‑conjugate appears);
* the AO basis is **orthonormal** or, if not, the overlap matrix **S** is known; we will give the expressions for both cases;
* the calculation is performed in the **restricted (closed‑shell)** case, i.e. we have separate α‑ and β‑spin blocks but the same spatial orbitals for the two spins.  The open‑shell case follows the same algebra, just keep the two spin blocks separate.

### 2.1  Molecular‑orbital (MO) coefficient matrices

For state 1 (ground) we have  

\[
\mathbf{C}^{(1)} = \bigl[\,\mathbf{C}^{(1)}_{\alpha}\;\; \mathbf{C}^{(1)}_{\beta}\,\bigr]
\]

where  

* \(\mathbf{C}^{(1)}_{\alpha}\) (size \(N_{\text{AO}}\times N_{\text{occ}}^{\alpha}\)) contains the coefficients of the occupied α‑MOs,  
* \(\mathbf{C}^{(1)}_{\beta}\) contains the occupied β‑MOs.

For state 2 (excited) we have the analogous matrices  

\[
\mathbf{C}^{(2)} = \bigl[\,\mathbf{C}^{(2)}_{\alpha}\;\; \mathbf{C}^{(2)}_{\beta}\,\bigr].
\]

(If the excited state is a *single‑excitation* from the ground state you will usually have the same number of occupied orbitals, only one of them is replaced by a virtual orbital – the formalism does **not** change.)

### 2.2  The ordinary (ground‑state) density matrix

For a closed‑shell determinant the (spin‑summed) one‑particle density matrix is  

\[
\mathbf{P}^{(1)} = \mathbf{P}^{(1)}_{\alpha}+\mathbf{P}^{(1)}_{\beta}
               = \mathbf{C}^{(1)}_{\alpha}\,(\mathbf{C}^{(1)}_{\alpha})^{\!T}
               + \mathbf{C}^{(1)}_{\beta}\,(\mathbf{C}^{(1)}_{\beta})^{\!T}.
\]

If the AO basis is not orthonormal the *orthonormalised* density is  

\[
\boxed{\;
\mathbf{P}^{(1)} = \mathbf{C}^{(1)}_{\alpha}\,(\mathbf{C}^{(1)}_{\alpha})^{\!T}\,\mathbf{S}^{-1}
                  + \mathbf{C}^{(1)}_{\beta}\,(\mathbf{C}^{(1)}_{\beta})^{\!T}\,\mathbf{S}^{-1}
\;}
\tag{1}
\]

where \(\mathbf{S}\) is the AO overlap matrix (\(S_{\mu\nu}= \langle\chi_\mu|\chi_\nu\rangle\)).

### 2.3  The **transition density matrix**  

The transition density is the one‑particle operator that connects the two states:

\[
\boxed{\;
\mathbf{P}^{(12)} = \mathbf{P}^{(12)}_{\alpha}+\mathbf{P}^{(12)}_{\beta}
\;}
\tag{2}
\]

with  

\[
\mathbf{P}^{(12)}_{\alpha}= \mathbf{C}^{(1)}_{\alpha}\,(\mathbf{C}^{(2)}_{\alpha})^{\!T},
\qquad
\mathbf{P}^{(12)}_{\beta}= \mathbf{C}^{(1)}_{\beta}\,(\mathbf{C}^{(2)}_{\beta})^{\!T}.
\]

If the AO basis is non‑orthogonal one must insert the overlap matrix (or its inverse) **once** to convert the bra‑side coefficients into the AO metric:

\[
\boxed{\;
\mathbf{P}^{(12)}_{\alpha}= \mathbf{C}^{(1)}_{\alpha}\,(\mathbf{C}^{(2)}_{\alpha})^{\!T}\,\mathbf{S}^{-1},
\qquad
\mathbf{P}^{(12)}_{\beta}= \mathbf{C}^{(1)}_{\beta}\,(\mathbf{C}^{(2)}_{\beta})^{\!T}\,\mathbf{S}^{-1}.
\;}
\tag{3}
\]

> **Why only one \( \mathbf{S}^{-1}\) ?**  
> The bra‑state coefficient matrix multiplies the AO basis from the left, the ket‑state from the right.  The overlap matrix is needed to raise (or lower) one index; it is *not* needed on both sides because the transition density is a **mixed** matrix (bra from state 1, ket from state 2).

The total transition density matrix is then  

\[
\mathbf{P}^{(12)} = \mathbf{C}^{(1)}_{\alpha}(\mathbf{C}^{(2)}_{\alpha})^{T}\mathbf{S}^{-1}
                  + \mathbf{C}^{(1)}_{\beta}(\mathbf{C}^{(2)}_{\beta})^{T}\mathbf{S}^{-1}.
\tag{4}
\]

> **Note on spin** – if the excited state is a pure singlet, the α‑ and β‑contributions are *identical* and you may simply double the α‑part.  For a triplet the two blocks have opposite sign (the transition dipole of a spin‑forbidden transition is zero in the non‑relativistic approximation).

### 2.4  Dipole‑integral (multipole) matrix  

For each Cartesian direction \(k\in\{x,y,z\}\) you have an AO matrix

\[
\boldsymbol{\mu}^{(k)}_{\mu\nu}= -\langle\chi_\mu|\hat{k}|\chi_\nu\rangle
      = -\int \chi_\mu(\mathbf{r})\, k \,\chi_\nu(\mathbf{r})\,\mathrm{d}\mathbf{r},
\]

where the minus sign is the **electronic** charge convention (the nuclear contribution is added later).

These three matrices are often supplied by quantum‑chemistry programs under the name *dipole integrals* or *multipole matrix*.

### 2.5  Contracting the transition density with the dipole matrix  

The *electronic* part of the transition dipole vector is simply the trace of the product of the transition density with each dipole matrix:

\[
\boxed{\;
\mu^{\text{el}}_k = \operatorname{Tr}\!\bigl[\,\mathbf{P}^{(12)}\,\boldsymbol{\mu}^{(k)}\,\bigr]
                 = \sum_{\mu\nu} P^{(12)}_{\mu\nu}\,\mu^{(k)}_{\nu\mu}.
\;}
\tag{5}
\]

Because \(\mathbf{P}^{(12)}\) is *not* symmetric the order of indices matters, but the trace eliminates the ordering issue (the product is a square matrix, then you sum the diagonal).

### 2.6  Adding the nuclear term  

The **nuclear** contribution to the dipole moment is the same for both electronic states because the nuclei do not move during an electronic transition (the Born–Oppenheimer approximation).  Therefore, when you evaluate a transition moment you may **omit** the nuclear term – it cancels out when the matrix element is taken between two electronic wavefunctions at the same geometry.

If you still wish to write the full expression, it is

\[
\boxed{\;
\mu_{k}^{(12)} = \mu^{\text{el}}_{k} + \mu^{\text{nuc}}_{k},
\qquad
\mu^{\text{nuc}}_{k}= \sum_{A} Z_A\,R_{A,k},
\;}
\tag{6}
\]

where \(Z_A\) is the atomic number of nucleus \(A\) and \(R_{A,k}\) its Cartesian coordinate.

Since \(\mu^{\text{nuc}}_{k}\) is identical for state 1 and state 2, the **transition dipole** that appears in spectroscopy is simply the electronic part, Eq. (5).

### 2.7  Summary – algorithm in matrix notation

1. **Read** the AO overlap matrix \(\mathbf{S}\) (identity if the basis is orthonormal).  
2. **Read** the MO‑coefficient blocks \(\mathbf{C}^{(1)}_{\alpha},\mathbf{C}^{(1)}_{\beta},\mathbf{C}^{(2)}_{\alpha},\mathbf{C}^{(2)}_{\beta}\).  
3. **Form** the transition density (Eq. 4)  

   \[
   \mathbf{P}^{(12)} = 
   \bigl[\mathbf{C}^{(1)}_{\alpha}(\mathbf{C}^{(2)}_{\alpha})^{\!T}
       +\mathbf{C}^{(1)}_{\beta}(\mathbf{C}^{(2)}_{\beta})^{\!T}\bigr]\,
   \mathbf{S}^{-1}.
   \]

4. **Load** the three dipole‑integral matrices \(\boldsymbol{\mu}^{(x)},\boldsymbol{\mu}^{(y)},\boldsymbol{\mu}^{(z)}\).  
5. **Contract** for each Cartesian component  

   \[
   \mu^{\text{el}}_k = \operatorname{Tr}\!\bigl[\mathbf{P}^{(12)}\,\boldsymbol{\mu}^{(k)}\bigr],
   \qquad k=x,y,z .
   \]

6. **(Optional)** add the nuclear term of Eq. (6).  
7. **Result**: the transition dipole vector  

   \[
   \boxed{\;\boldsymbol\mu_{12}= (\mu^{\text{el}}_x,\mu^{\text{el}}_y,\mu^{\text{el}}_z)\;}
   \]

   whose magnitude \(|\boldsymbol\mu_{12}|\) is the quantity that enters the Einstein‑A coefficient, oscillator strength, etc.

---

## 3.  Final answer (concise form)

For a closed‑shell system, the transition dipole moment between electronic states 1 and 2 is

\[
\boxed{
\boldsymbol\mu_{12}= -\!\operatorname{Tr}
\Bigl[
\bigl(
\mathbf{C}^{(1)}_{\alpha}(\mathbf{C}^{(2)}_{\alpha})^{\!T}
+\mathbf{C}^{(1)}_{\beta}(\mathbf{C}^{(2)}_{\beta})^{\!T}
\bigr)\mathbf{S}^{-1}
\,
\boldsymbol{\mu}
\Bigr]
+ \sum_A Z_A\mathbf{R}_A
}
\]

where  

* \(\boldsymbol{\mu}\) is the **3‑component** dipole‑integral matrix (one matrix per Cartesian direction),  
* \(\mathbf{S}\) is the AO overlap matrix (use the identity if the basis is orthonormal),  
* the nuclear term is geometry‑dependent and cancels for a pure electronic transition, so the *spectroscopic* TDM is usually just the trace term.

If the basis is orthonormal (\(\mathbf{S}= \mathbf{I}\)), the expression simplifies to

\[
\boldsymbol\mu_{12

*Original question: [How to calculate transition dipole moment from two known wavefunctions](https://chemistry.stackexchange.com/questions/47529/how-to-calculate-transition-dipole-moment-from-two-known-wavefunctions) on Chemistry Stack Exchange, licensed CC BY-SA.*
