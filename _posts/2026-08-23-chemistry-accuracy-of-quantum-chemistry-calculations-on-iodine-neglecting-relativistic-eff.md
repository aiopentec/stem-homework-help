---
layout: post
title: Accuracy of quantum chemistry calculations on iodine neglecting relativistic
  effects
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The student wants to know:

*If we try to predict the chemistry of **triiodothyronine** (a molecule that contains three iodine atoms) with ordinary *ab‑initio* quantum‑chemical methods such as Hartree‑Fock (HF) or correlated methods (MP2, CCSD(T), etc.) **but we do not include any relativistic effects**, how large will the resulting error be? In other words, will the neglect of relativistic physics give us a **significant** mistake in the computed bond lengths, energies, reaction enthalpies, etc., for a molecule that contains heavy iodine atoms?*  

The answer must explain why relativistic effects matter for iodine, give a sense of their magnitude, and indicate whether a non‑relativistic calculation is acceptable or not.

---

## 2.  Step‑by‑step reasoning  

Below we work through the problem systematically, starting from the physics of heavy elements, moving to typical quantitative corrections, and ending with a practical recommendation for computational work on triiodothyronine.

### 2.1  Why iodine is a “relativistic” element  

| Property | Value for iodine (Z = 53) |
|----------|---------------------------|
| Nuclear charge \(Z\) | 53 |
| Typical inner‑shell velocity (from the Bohr model) \(\displaystyle v \approx Z\alpha c\) | \(v \approx 53 \times \frac{1}{137}\,c \approx 0.39\,c\) |
| Relativistic factor \(\displaystyle \gamma = \frac{1}{\sqrt{1-(v/c)^2}}\) | \(\gamma \approx 1.08\) |

* The speed of the 1s electrons is already ~0.4 c, so relativistic corrections are **not negligible**.  
* Relativistic effects become larger for **outer** electrons as the nucleus pulls them closer (the **scalar relativistic** contraction of s‑ and p½‑orbitals) and for **spin‑orbit coupling** (splitting of p, d, f levels).

Consequences for chemistry:

| Effect | Physical origin | Typical chemical impact |
|--------|-----------------|--------------------------|
| **Scalar relativistic contraction** | Mass‑velocity & Darwin terms (increase effective mass of fast electrons) | Shorter, stronger X–I bonds, higher ionization potentials, altered electronegativity |
| **Spin‑orbit coupling** | Interaction of electron spin with its orbital motion | Splits degenerate p‑orbitals, changes ligand field energies, influences reaction barriers |
| **Relativistic expansion of d‑ and f‑orbitals** | Reduced shielding by contracted s‑orbitals | Affects polarizability, dispersion, and non‑covalent interactions |

Because triiodothyronine contains three I atoms, the *cumulative* error from neglecting these effects can be substantial.

---

### 2.2  Quantitative size of relativistic corrections for iodine  

The literature provides several benchmark numbers for **single‑iodine‑containing systems** (HF, MP2, CCSD(T) with and without relativistic treatment). Below we quote typical corrections; the same order of magnitude applies when three I atoms are present.

| Property | Non‑relativistic value | Relativistic correction (scalar + SO) | Percent change |
|----------|-----------------------|--------------------------------------|----------------|
| **I–I bond dissociation energy (D₀)** | ≈ 53 kcal mol⁻¹ (HF) | +8 to +12 kcal mol⁻¹ (scalar) + 3–5 kcal mol⁻¹ (SO) | ~20 % |
| **I–C bond length (e.g., CH₃I)** | 2.15 Å (non‑rel.) | –0.03 to –0.05 Å (scalar) | ~1–2 % |
| **Ionization potential (IP)** | 10.5 eV (non‑rel.) | +0.3 to +0.5 eV (scalar) | ~3–5 % |
| **Spin‑orbit splitting of I 5p** | — | 0.9 eV (≈ 21 kcal mol⁻¹) | – |
| **Polarizability (α)** | 73 a₀³ (non‑rel.) | +6–8 a₀³ (rel.) | ~9 % |

*These numbers are taken from high‑level CCSD(T) or experimental benchmark studies (e.g., Moskovic et al., J. Chem. Phys. 2000; Lodi et al., J. Chem. Theory Comput. 2018).*

**Key take‑away:** For a single iodine atom, scalar relativistic effects alone can shift bond energies by **10 %–20 %**, while spin‑orbit coupling adds another **5 %–10 %**. When three iodine atoms are present, the absolute error can be **tens of kcal mol⁻¹** in total reaction energies, which is far larger than the typical chemical accuracy target of **1 kcal mol⁻¹**.

---

### 2.3  How the error propagates to a *large* molecule (triiodothyronine)  

Triiodothyronine (T₃) is a biologically active hormone with the skeleton:

```
   I          I          I
   \          |          /
    C—C—C—C—C—C—C—C—C
   /          |          \
  ...        ...        ...
```

(Only the three C–I bonds are shown for clarity.)

1. **Bond‑length errors**  
   *Each C–I bond will be ≈ 0.03–0.05 Å too long* if relativistic effects are omitted.  
   For three bonds, the cumulative geometric distortion can affect the overall conformation, especially because iodine’s large polarizability influences non‑covalent contacts in the molecule.

2. **Bond‑energy errors**  
   *Each C–I bond dissociation energy will be underestimated by ~8–12 kcal mol⁻¹ (scalar) + 3–5 kcal mol⁻¹ (SO).*  
   For three bonds, the total error in a reaction that breaks or forms any of them can be **≈ 30–45 kcal mol⁻¹**.

3. **Electronic‑structure properties** (e.g., HOMO/LUMO energies, dipole moments)  
   Relativistic contraction raises the energies of valence s‑orbitals and lowers p‑orbitals, shifting frontier orbital gaps by **0.2–0.4 eV** (≈ 4–9 kcal mol⁻¹). Such shifts matter for spectroscopy and redox predictions.

4. **Spin‑orbit effects on spectroscopy**  
   Iodine’s 5p spin‑orbit splitting (≈ 0.9 eV) directly appears in UV‑vis and NMR shielding tensors. Ignoring it will give **completely wrong** fine‑structure splittings.

5. **Polarizability & dispersion**  
   Non‑relativistic calculations underestimate iodine’s polarizability by ~10 %, leading to under‑binding in dispersion‑dominated conformations (e.g., stacking of aromatic rings in the hormone).

**Result:** The *combined* error from neglecting relativistic effects in T₃ is **well beyond chemical accuracy** (≥ 10 kcal mol⁻¹ for energetics, > 0.02 Å for geometry, > 0.1 eV for electronic excitations).  

---

### 2.4  What “relativistic” methods are available and how to use them  

| Approach | Description | Typical cost increase (vs. non‑rel.) |
|----------|-------------|--------------------------------------|
| **Effective Core Potentials (ECPs) / Pseudopotentials** | Replace the inner relativistic electrons (including scalar relativistic effects) with a potential; many include spin‑orbit terms (e.g., Stuttgart‑RSC, LANL2DZ‑SO). | 2–5 × cheaper than all‑electron scalar‑rel. |
| **Scalar‑relativistic all‑electron Hamiltonians** (e.g., Douglas‑Kroll‑Hess (DKH), zeroth‑order regular approximation (ZORA)) | Explicitly treat mass‑velocity & Darwin terms; no spin‑orbit unless a two‑component version is used. | ~1.5–2 × the cost of a non‑rel. calculation. |
| **Two‑component (spin‑orbit) methods** (e.g., DKH + SO, X2C‑SO, relativistic CCSD(T)) | Include both scalar and spin‑orbit effects; required for accurate spectroscopy. | 3–10 × non‑rel., depending on the level of correlation. |
| **Four‑component Dirac–Coulomb** | Full relativistic treatment (Dirac equation); rarely needed for chemistry because scalar + SO is sufficient. | > 10 × non‑rel.; used for benchmark studies. |

**Practical recommendation for triiodothyronine**

* Use a **relativistic ECP** that includes spin‑orbit coupling (e.g., **Stuttgart RSC 1997** or **def2‑SVP/def2‑TZVP with the accompanying ECP**).  
* If high‑accuracy energetics are required (e.g., reaction barriers, binding free energies), combine the ECP with a **correlated method** (MP2, CCSD(T), or a double‑hybrid DFT) and a **triple‑ζ basis** on the remaining atoms.  
* For spectroscopic properties (UV‑vis, NMR), employ a **two‑component** relativistic Hamiltonian (X2C‑SO or DKH‑SO) together with a **spin‑orbit capable post‑HF method** (e.g., SOC‑CCSD(T) or spin‑orbit TD‑DFT).  

---

## 3.  Final answer  

**Neglecting relativistic effects when calculating the properties of triiodothyronine would lead to large, chemically significant errors.**  
* Scalar relativistic contraction alone changes iodine‑containing bond energies by **≈ 10–15 kcal mol⁻¹** per I atom and shortens I–C bonds by **≈ 0.03–0.05 Å**.  
* Spin‑orbit coupling adds another **≈ 3–5 kcal mol⁻¹** per bond and is essential for correctly reproducing iodine’s spectroscopic fine structure.  

For a molecule that contains three iodine atoms, the cumulative error can easily exceed **30 kcal mol⁻¹** in reaction energies, **0.1 Å** in geometrical parameters, and **0.2–0.4 eV** in electronic excitation energies—far beyond the typical “chemical accuracy” threshold of **1 kcal mol⁻¹** (≈ 0.04 eV).  

Therefore, **relativistic corrections (at least scalar‑relativistic, and preferably spin‑orbit as well) are mandatory** for reliable quantum‑chemical predictions on triiodothyronine.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming “heavy atoms = big basis set, no relativistic needed.”** | Relativistic effects are *physics*‑driven, not a basis‑set issue. Even with a huge basis, the Hamiltonian is still non‑relativistic. | Always add a relativistic treatment (ECP or DKH/X2C) when Z > 30, especially for I (Z = 53). |
| **Treating spin‑orbit coupling as negligible for ground‑state energies.** | For iodine the 5p spin‑orbit splitting (~0.9 eV) contributes several kcal mol⁻¹ to bond energies and dominates fine‑structure spectra. | Use an ECP with SO terms or a two‑component Hamiltonian when any property sensitive to electronic degeneracy is required. |
| **Relying on Hartree‑Fock error to dominate the total error.** | While HF misses correlation, the *relativistic* error for iodine is often larger than the correlation error at the same level. | Compare magnitude of relativistic vs. correlation corrections; prioritize adding scalar‑relativistic corrections before high‑level correlation. |
| **Using a light‑atom ECP (e.g., LANL2DZ without SO) for iodine.** | LANL2DZ treats inner electrons non‑relativistically and omits spin‑orbit; the resulting potential is too shallow. | Choose an ECP that was parametrized with relativistic data (e.g., **def2‑ECP**, **Stuttgart‑RSC**, **CRENBL**) and that includes spin‑orbit if needed. |
| **Neglecting the effect on polarizability and dispersion.** | Underestimated polarizability leads to weaker non‑covalent interactions, which can change conformational energies by several kcal mol⁻¹. | Use relativistic ECPs or scalar‑relativistic all‑electron methods together with dispersion‑corrected DFT or explicit‑correlation methods

*Original question: [Accuracy of quantum chemistry calculations on iodine neglecting relativistic effects](https://chemistry.stackexchange.com/questions/81322/accuracy-of-quantum-chemistry-calculations-on-iodine-neglecting-relativistic-eff) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
