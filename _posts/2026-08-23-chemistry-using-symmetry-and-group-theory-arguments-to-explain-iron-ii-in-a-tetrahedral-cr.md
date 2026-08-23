---
layout: post
title: Using symmetry and group theory arguments to explain iron(II) in a tetrahedral
  crystal field
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

### 1. Restatement of the Problem in Plain Language

We want to understand the $1s \rightarrow 3d$ pre-edge features in the X-ray Absorption Spectroscopy (XAS) of an iron(II) ($\text{Fe}^{2+}$) ion situated in a tetrahedral ($T_\mathrm{d}$) crystal field. 

Specifically, we need to use group theory and symmetry arguments to determine which electronic transitions are allowed from the ground state to the final states. The $1s \rightarrow 3d$ transition is electric quadrupole-allowed. By looking at the symmetry of the ground state, the final states, and the quadrupole operator in $T_\mathrm{d}$ symmetry, we will determine which specific transitions can occur, accounting for spin and spatial symmetries.

---

### 2. Step-by-Step Worked Solution

#### Step 1: Establish the Initial State ($\text{Fe}^{2+}$, $d^6$ in $T_\mathrm{d}$ Symmetry)
* **Electron configuration:** $\text{Fe}^{2+}$ is a $d^6$ system. 
* **Free-ion ground term:** The lowest Russell–Saunders term for a free $d^6$ ion is $^5D$.
* **Crystal field splitting:** In a tetrahedral ($T_\mathrm{d}$) ligand field, the $d$-orbitals split into $e$ and $t_2$ sets (with the $e$ set lower in energy). The electron configuration for the lowest-energy state of a high-spin $d^6$ system is $(e^3 t_2^3)$.
* **Inversion center note:** Strictly speaking, a tetrahedron lacks an inversion center ($i$), so the $g$ (gerade) and $u$ (ungerade) subscripts do not rigorously apply to pure $T_\mathrm{d}$ point groups. However, XAS literature often correlates molecular orbitals or local site symmetries with $O_h$ parentage or explicitly includes ungerade/gerade labels when considering atomic core orbitals ($1s$ is $s$, which is inherently ungerade relative to a local center). Following the student's premise, the ground-state spatial symmetry transforms as the $^5E$ (or $^5E_u$) representation.

Thus, the initial state symmetry including spin multiplicity is:
$$\Gamma_{\text{initial}} = {}^5E$$

---

#### Step 2: Determine the Final State Configuration ($1s^1 3d^7$)
When a core $1s$ electron is excited into the $3d$ shell, the final core-hole configuration is $1s^1 3d^7$. 
* The $1s^1$ core hole has orbital angular momentum $l = 0$ (symmetry $^2S$).
* The $d^7$ configuration generates the free-ion terms: 
  $$\{{}^4F, {}^4P, {}^2H, {}^2G, {}^2F, {}^2P, {}^2D(2)\}$$
* Coupling the core hole ($^2S$) with the $d^7$ terms gives the final Russell–Saunders terms:
  $${}^2S \otimes \{{}^4F, {}^4P, \dots\} = {}^{5,3}F, {}^{5,3}P, \dots$$

#### Step 3: Apply Selection Rules
1. **Spin Selection Rule:** Electric quadrupole transitions are spin-allowed, meaning $\Delta S = 0$. 
   * The ground state is a quintet ($S = 2$, i.e., ${}^5D$). 
   * Therefore, only final states with $S = 2$ (quintets) can be reached. From our coupled terms, only the **${}^5F$** and **${}^5P$** terms satisfy this condition.
2. **Orbital/Symmetry Branching:** We now take the free-ion ${}^5F$ and ${}^5P$ terms and branch them into $T_\mathrm{d}$ symmetry:
   $$\begin{aligned}
   {}^5F &\rightarrow {}^5A_2 \oplus {}^5T_1 \oplus {}^5T_2 \\
   {}^5P &\rightarrow {}^5T_1 
   \end{aligned}$$
   Combining these gives the spatial-spin final state symmetries ($\Gamma_{\text{final}}$):
   $$\Gamma_{\text{final}} = {}^5A_2 \oplus {}^5T_1(F) \oplus {}^5T_2 \oplus {}^5T_1(P)$$

---

#### Step 4: Identify the Symmetry of the Quadrupole Operator
* The electric quadrupole operator transforms as second-rank tensor components ($dxz, dyz, dxy, dx^2-y^2, dz^2$). 
* In a $T_\mathrm{d}$ point group, the components of the quadrupole operator span the **$E$** and **$T_2$** irreducible representations:
  $$\Gamma_{\text{quad}} = E \oplus T_2$$

---

#### Step 5: Test the Direct Product for Transition Integrals
For a transition to be allowed, the direct product of the initial state symmetry, the operator symmetry, and the final state symmetry must contain the totally symmetric irreducible representation ($A_1$ in $T_\mathrm{d}$):
$$\Gamma_{\text{initial}} \otimes \Gamma_{\text{op}} \otimes \Gamma_{\text{final}} \supset A_1$$
$$\text{or equivalently: } \quad \Gamma_{\text{final}} \in \Gamma_{\text{initial}} \otimes \Gamma_{\text{op}}$$

Let's evaluate the direct product of the initial state ($E$) and the quadrupole operator ($E \oplus T_2$):
1. **Using the $E$ component of the quadrupole operator:**
   $$E \otimes E = A_1 \oplus A_2 \oplus E$$
   This product contains $A_1$, $A_2$, and $E$. Matching this against our final states ($\Gamma_{\text{final}} = A_2 \oplus T_1 \oplus T_2$):
   * **${}^5A_2$** is **allowed** (since $A_2$ appears in $E \otimes E$).
   
2. **Using the $T_2$ component of the quadrupole operator:**
   $$E \otimes T_2 = T_1 \oplus T_2$$
   This product contains $T_1$ and $T_2$. Matching this against our final states:
   * **${}^5T_1$** (from both $F$ and $P$) is **allowed**.
   * **${}^5T_2$** is **allowed**.

---

### 3. Final Answer

By evaluating the direct products between the initial ground state ($^5E$), the electric quadrupole operator ($E \oplus T_2$), and the final state irreducible representations, we find that **all** generated quintet final states are symmetry-allowed for the $1s \rightarrow 3d$ quadrupole transition in $T_\mathrm{d}$ symmetry. 

Specifically, the allowed transitions connect the ${}^5E$ ground state to the following final states:
1. **${}^5A_2$** (originating from the ${}^5F$ term, accessed via the $E$ component of the quadrupole operator)
2. **${}^5T_2$** (originating from the ${}^5F$ term, accessed via the $T_2$ component of the quadrupole operator)
3. **${}^5T_1$** (originating from both the ${}^5F$ and ${}^5P$ terms, accessed via the $T_2$ component of the quadrupole operator)

---

### 4. Common Mistakes for This Problem Type

1. **Ignoring Spin Multiplicity:** Treating only the spatial symmetries ($E$, $T_2$, etc.) while forgetting that pre-edge transitions are strictly governed by spin selection rules ($\Delta S = 0$). Only states with matching spin multiplicity (here, $S = 2$ quintets) should be evaluated after initial term coupling.
2. **Incorrect Operator Symmetry:** Confusing electric dipole ($p$-type, transforming as $T_2$ in $T_\mathrm{d}$) and electric quadrupole ($d$-type, transforming as $E \oplus T_2$ in $T_\mathrm{d}$) selection rules. Using dipole instead of quadrupole ruins the symmetry matching.
3. **Misapplying Direct Products:** Forgetting that for a transition to be allowed, the direct product $\Gamma_{\text{initial}} \otimes \Gamma_{\text{op}}$ must *span* or *overlap with* the final state symmetry $\Gamma_{\text{final}}$ (i.e., $\Gamma_{\text{final}} \in \Gamma_{\text{initial}} \otimes \Gamma_{\text{op}}$).

*Original question: [Using symmetry and group theory arguments to explain iron(II) in a tetrahedral crystal field](https://chemistry.stackexchange.com/questions/151356/using-symmetry-and-group-theory-arguments-to-explain-ironii-in-a-tetrahedral-c) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
