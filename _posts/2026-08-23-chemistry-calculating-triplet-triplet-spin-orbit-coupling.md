---
layout: post
title: Calculating Triplet-Triplet Spin-Orbit Coupling
author: StemFix Bot
category: chemistry
tags:
- chemistry
render_with_liquid: false
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What is being asked?  

A student is looking at the formulae used by **Q‑Chem** for spin‑orbit coupling (SOC) matrix elements between excited states that are described by spin‐adapted configuration‑interaction (CI) wavefunctions.  

* For a **singlet–triplet** pair the program prints  

\[
\boxed{\displaystyle 
\langle\Phi_{\rm S}^{I}\,|\,\hat H_{\rm SO}\,|\,\Phi_{\rm T}^{J}\rangle
= \sqrt{\sum_{m_s = 0,\pm1}\Big|
\langle\Phi_{\rm S}^{I}\,|\,\hat H_{\rm SO}\,|\,\Phi_{\rm T}^{J,m_s}\rangle\Big|^{2}}
}
\tag{1}
\]

* For a **triplet–triplet** pair the manual writes  

\[
\boxed{\displaystyle 
\langle\Phi_{\rm T}^{I}\,|\,\hat H_{\rm SO}\,|\,\Phi_{\rm T}^{J}\rangle
= \sqrt{\sum_{m_s = 0,\pm1}\Big|
\langle\Phi_{\rm T}^{I,m_s}\,|\,\hat H_{\rm SO}\,|\,\Phi_{\rm T}^{J,m_s}\rangle\Big|^{2}}
}
\tag{2}
\]

The student wonders whether (2) should actually contain **two** independent sums over the spin‑projection quantum numbers of the two states, i.e.

\[
\sqrt{\displaystyle\sum_{m_{s,i}=0,\pm1}\;
\sum_{m_{s,j}=0,\pm1}
\Big|
\langle\Phi_{\rm T}^{I,m_{s,i}}|\hat H_{\rm SO}|
\Phi_{\rm T}^{J,m_{s,j}}\rangle\Big|^{2}} .
\tag{3}
\]

In other words: *Do the off‑diagonal spin‑blocks (the “\(a\)” elements in the 3 × 3 matrix shown by the student) contribute to the overall SOC, or are they forced to zero by the theory?*  

The solution below shows, step‑by‑step, why only the **diagonal** spin‑blocks survive, so the **single‑sum** expression (2) is the correct one.

---

## 2.  Detailed derivation  

### 2.1.  Spin‑orbit Hamiltonian

In non‑relativistic quantum chemistry the one‑electron spin‑orbit operator is usually written (in atomic units) as  

\[
\hat H_{\rm SO}= \sum_{p}\,\xi(\mathbf r_{p})\,
\hat{\mathbf L}_{p}\!\cdot\!\hat{\mathbf S}_{p},
\tag{4}
\]

where  

* \(\hat{\mathbf L}_{p}\) acts **only on the spatial** coordinates of electron *p*,  
* \(\hat{\mathbf S}_{p}\) acts **only on the spin** coordinate of the same electron, and  
* \(\xi(\mathbf r)\) is a (real) scalar function that depends on the distance of the electron from the nuclei (it is the so‑called spin‑orbit constant).

Because \(\hat{\mathbf L}\) does **not** change the spin part of a wavefunction, the only way the operator can connect two many‑electron spin functions is through the **spin scalar product** \(\hat{\mathbf L}\!\cdot\!\hat{\mathbf S}\).  

The one‑electron spin operators have the well‑known matrix elements in the basis of spin‑eigenfunctions \(\{| \alpha\rangle,| \beta\rangle\}\) (or, equivalently, in the coupled basis \(|S,m_{s}\rangle\) with \(S=1\) for a triplet):

\[
\begin{aligned}
\langle S,m_{s}|\hat{\mathbf L}\!\cdot\!\hat{\mathbf S}|S,m'_{s}\rangle
&= \langle S,m_{s}|L_{z}S_{z}+ \tfrac12(L_{+}S_{-}+L_{-}S_{+})|S,m'_{s}\rangle\\[2pt]
&= \langle S,m_{s}|L_{z}|S,m'_{s}\rangle\,m_{s}\,\delta_{m_{s},m'_{s}}
   \;+\; \text{terms that change }m_{s}\text{ by }\pm1 .
\end{aligned}
\tag{5}
\]

When the **total spin of the many‑electron state is a good quantum number** (as it is for the spin‑adapted CI states used in TD‑DFT), the operator \(\hat H_{\rm SO}\) **cannot mix different values of \(m_{s}\)** **unless** the spatial part supplies the necessary angular‑momentum change.  

In practice the *single‑electron* operators \(L_{\pm}\) act on the orbital of the same electron that carries the spin‑flip operator \(S_{\mp}\). For a *closed‑shell* or *restricted open‑shell* determinant the net effect is that **the matrix element between two overall triplet states is diagonal in the total spin‑projection quantum number**:

\[
\boxed{
\langle\Phi_{\rm T}^{I,m_{s,i}}|\hat H_{\rm SO}|
\Phi_{\rm T}^{J,m_{s,j}}\rangle
= \delta_{m_{s,i},\,m_{s,j}}\;X^{IJ}_{m_{s,i}}
}
\tag{6}
\]

where \(X^{IJ}_{m_{s,i}}\) is a (generally complex) number that depends on the spatial part of the two states and on the particular value of \(m_{s}\) (through the factor \(m_{s}\) that appears in Eq. (5)).  

**Key point:** the Kronecker delta \(\delta_{m_{s,i},m_{s,j}}\) tells us that *off‑diagonal* spin blocks (\(m_{s,i}\neq m_{s,j}\)) are **exactly zero**.  

### 2.2.  Consequence for the norm of the SOC matrix element  

The program defines an *effective* SOC matrix element between two **spin‑adapted** states as the **Euclidean norm** of the (3 × 3) block matrix in spin space:

\[
\big\|\mathbf H^{IJ}_{\rm SO}\big\|
= \sqrt{ \sum_{m_{s,i}=0,\pm1}\;
        \sum_{m_{s,j}=0,\pm1}
        \big|
        \langle\Phi_{\rm T}^{I,m_{s,i}}|
        \hat H_{\rm SO}
        |\Phi_{\rm T}^{J,m_{s,j}}\rangle
        \big|^{2} } .
\tag{7}
\]

Insert the diagonal form (6):

\[
\begin{aligned}
\big\|\mathbf H^{IJ}_{\rm SO}\big\|
&= \sqrt{ \sum_{m_{s,i}=0,\pm1}
          \sum_{m_{s,j}=0,\pm1}
          \big|\delta_{m_{s,i},m_{s,j}}\,X^{IJ}_{m_{s,i}}\big|^{2} }\\[4pt]
&= \sqrt{ \sum_{m_{s}=0,\pm1}
          \big|X^{IJ}_{m_{s}}\big|^{2} } .
\end{aligned}
\tag{8}
\]

Because the double sum collapses to a **single** sum over the three possible values of the *same* spin projection, we recover exactly the expression quoted in the Q‑Chem manual (Eq. 2).  

Thus the “\(a\)” elements that the student placed in the off‑diagonal positions of the 3 × 3 matrix are **forced to be zero** by the spin‑selection rule encoded in Eq. (6).  

### 2.3.  Explicit evaluation for a triplet–triplet pair  

Let us write the three spin‑adapted CI wavefunctions for a given electronic configuration (the superscript denotes the state index, the subscript the spin projection):

\[
\begin{aligned}
|\Phi_{\rm T}^{I,0}\rangle &= \frac{1}{\sqrt{2}}
\bigl(|\alpha\beta\rangle + |\beta\alpha\rangle\bigr) \otimes |\Psi^{I}_{\rm orb}\rangle ,\\
|\Phi_{\rm T}^{I,+1}\rangle &= |\alpha\alpha\rangle \otimes |\Psi^{I}_{\rm orb}\rangle ,\\
|\Phi_{\rm T}^{I,-1}\rangle &= |\beta\beta\rangle \otimes |\Psi^{I}_{\rm orb}\rangle .
\end{aligned}
\tag{9}
\]

Operating with \(\hat H_{\rm SO}\) on any of these states gives (using Eq. 5)

\[
\hat H_{\rm SO}\,|\Phi_{\rm T}^{I,m_{s}}\rangle
= m_{s}\; \Bigl[\,\sum_{p}\xi(\mathbf r_{p})\,\hat L_{z}^{(p)}\Bigr]\,
|\Phi_{\rm T}^{I,m_{s}}\rangle ,
\tag{10}
\]

i.e. the result is *proportional to the same spin function* with the same \(m_{s}\). Consequently  

\[
\langle\Phi_{\rm T}^{I,m_{s}}|\hat H_{\rm SO}|\Phi_{\rm T}^{J,m'_{s}}\rangle
= m_{s}\,\delta_{m_{s},m'_{s}}\;
\langle\Psi^{I}_{\rm orb}|\,\sum_{p}\xi(\mathbf r_{p})\,\hat L_{z}^{(p)}\,
|\Psi^{J}_{\rm orb}\rangle .
\tag{11}
\]

The spatial integral is the same for the three components; only the prefactor \(m_{s}=0,\pm1\) changes.  

Hence the **norm** becomes

\[
\big\|\mathbf H^{IJ}_{\rm SO}\big\|
= \sqrt{\,0^{2}+|X^{IJ}|^{2}+|{-X^{IJ}}|^{2}}
= \sqrt{2}\,|X^{IJ}|\;,
\tag{12}
\]

where \(X^{IJ}= \langle\Psi^{I}_{\rm orb}|\,\sum_{p}\xi(\mathbf r_{p})\,\hat L_{z}^{(p)}\,|\Psi^{J}_{\rm orb}\rangle\).  
Equation (12) is precisely the numerical value that the program reports when it evaluates the *single‑sum* formula (2).  

---

## 3.  Final answer  

The SOC matrix element between two **triplet** states is defined as the Euclidean norm of the (3 × 3) spin‑block matrix. Because the one‑electron spin‑orbit operator is **diagonal in the total spin‑projection quantum number** (the Kronecker delta \(\delta_{m_{s,i},m_{s,j}}\) appears in every matrix element), all off‑diagonal blocks vanish. Consequently the double sum in Eq. (3) collapses to a **single sum** over the three possible values of the *common* spin projection:

\[
\boxed{
\langle\Phi_{\rm T}^{I}|\hat H_{\rm SO}|\Phi_{\rm T}^{J}\rangle
= \sqrt{\displaystyle\sum_{m_{s}=0,\pm1}
\Big|\,
\langle\Phi_{\rm T}^{I,m_{s}}|\hat H_{\rm SO}|
\Phi_{\rm T}^{J,m_{s}}\rangle
\Big|^{2}}
}
\]

Therefore the expression given in the Q‑Chem manual (the “single‑sum” form) is **correct**; the off‑diagonal entries labelled “\(a\)” in the student's matrix are identically zero by symmetry.

---

## 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the spin‑orbit operator can change the total spin projection** (i.e., that \(\langle T^{m_s}| \hat H_{\rm SO} | T^{m'_s}\rangle\) is non‑zero for \(m_s\neq m'_s\)). | The operator contains \(\hat{\mathbf L}\cdot\hat{\mathbf S}\); the *spin* part can raise/lower \(m_s\) by at most one, but the *same* electron must also change its orbital angular momentum. For a *closed‑shell* reference (or for spin‑adapted CI) the net effect is that the overall **

*Original question: [Calculating Triplet-Triplet Spin-Orbit Coupling](https://chemistry.stackexchange.com/questions/90004/calculating-triplet-triplet-spin-orbit-coupling) on Chemistry Stack Exchange, licensed CC BY-SA.*
{% endraw %}
