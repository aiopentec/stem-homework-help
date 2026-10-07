---
layout: question
title: Dilemma of Dielectric
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Dilemma of Dielectric'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the student is really asking  

The student is trying to reconcile three statements that seem to contradict one another  

| Statement | What it says (in the student’s words) |
|-----------|----------------------------------------|
| **A “perfect dielectric”** | should have *infinite* resistivity (i.e. zero conductivity) but the bound electrons can still be displaced to produce polarization. |
| **A “perfect conductor”** | should have *infinite* dielectric constant (i.e. “high dielectric”) while the free electrons are completely un‑bound and move without resistance. |
| **General intuition** | If electrons are bound they should not be called “high‑resistivity”; if they are free they should not be called “high‑dielectric”.  

The question, therefore, is:

> **How can a material be a perfect dielectric (no conduction) yet still polarize, and why is a perfect conductor sometimes described as having an “infinite dielectric constant”?  What is the precise relationship between conductivity, resistivity, and dielectric constant?**

---

## 2.  Step‑by‑step answer  

Below we build the answer from the ground up, using the definitions that appear in Maxwell’s equations.  

### 2.1  Basic material parameters  

| Symbol | Quantity | Definition | Units |
|--------|----------|------------|-------|
| **σ** (sigma) | **Electrical conductivity** | Ratio of conduction current density **J** to electric field **E**:  \(\mathbf J = \sigma \mathbf E\) (Ohm’s law for a homogeneous medium). | S m\(^{-1}\) (siemens per metre) |
| **ρ** (rho) | **Resistivity** | Reciprocal of conductivity: \(\rho = 1/\sigma\). | Ω m |
| **ε** (epsilon) | **Permittivity** | Ratio of electric displacement **D** to field **E**: \(\mathbf D = \varepsilon \mathbf E\). | F m\(^{-1}\) |
| **ε₀** | Vacuum permittivity | \(\varepsilon_0 = 8.854\,187\,817\cdots\times10^{-12}\,\text{F m}^{-1}\). |
| **εᵣ** (epsilon‑r) | **Relative permittivity** or **dielectric constant** | \(\varepsilon_{\rm r}= \varepsilon/\varepsilon_0\). |
| **χₑ** | Electric susceptibility | \(\varepsilon = \varepsilon_0(1+\chi_e)\). |

> **Key point:** Conductivity (σ) tells us how **free charges** move in response to a field (a *real* current).  
> Permittivity (ε) tells us how **bound charges** shift in response to a field (a *displacement* current). They are independent material properties.

### 2.2  Maxwell’s equations in matter (macroscopic form)

The two relevant equations are  

\[
\boxed{\mathbf J_{\rm total}= \mathbf J_{\rm conduction} + \mathbf J_{\rm displacement}}
\]

\[
\mathbf J_{\rm conduction}= \sigma \mathbf E
\qquad\text{(Ohmic current)}
\]

\[
\mathbf J_{\rm displacement}= \frac{\partial \mathbf D}{\partial t}
        =\varepsilon\frac{\partial \mathbf E}{\partial t}
\qquad\text{(due to polarization of bound charges)}
\]

Thus the **total current density** that appears in Ampère‑Maxwell law is  

\[
\mathbf J_{\rm total}= \sigma\mathbf E+\varepsilon\frac{\partial \mathbf E}{\partial t}.
\]

If the field is **static** (\(\partial\mathbf E/\partial t=0\)), only the conduction term survives.  
If the field is **time‑varying**, both terms can be present.

### 2.3  Perfect dielectric  

A *perfect* dielectric is defined mathematically by  

\[
\sigma = 0\qquad\Longleftrightarrow\qquad \rho = \infty .
\]

*Consequences*

1. **No conduction current** can flow, no matter how large a static field you apply.  
2. **Polarization is still possible** because the bound electrons (or molecular dipoles) can be displaced. This displacement is captured entirely by the permittivity ε, which remains **finite** (typically \(\varepsilon_{\rm r}=2\)–\(10^3\) for real dielectrics).  
3. In a time‑varying field, the **displacement current** \(\varepsilon\partial\mathbf E/\partial t\) is the only current that can exist.

> **Physical picture:** The electrons are “bound” to nuclei by the atomic potential. When an external field is applied, each electron cloud is shifted a tiny amount relative to its nucleus, creating a microscopic dipole. The **net charge does not move from point to point**, so no macroscopic conduction current appears. Energy is stored in the electric field as \(\tfrac12\varepsilon E^{2}\).

### 2.4  Perfect conductor  

A *perfect* conductor is defined by  

\[
\sigma \rightarrow \infty \qquad\text{(or equivalently } \rho\rightarrow0\text{)}.
\]

*Consequences*

1. Any **static** electric field inside the material would immediately produce an *infinite* conduction current, which is impossible. The only self‑consistent static solution is  

   \[
   \boxed{\mathbf E_{\text{inside}} = 0}.
   \]

2. Surface charges rearrange themselves until the interior field vanishes. The **surface** may support a surface charge density that produces the required external field.

3. The displacement term can be written as  

   \[
   \mathbf J_{\rm displacement}= \varepsilon\frac{\partial\mathbf E}{\partial t}.
   \]

   Since \(\mathbf E\) inside a perfect conductor is zero (even for a time‑varying external field, the interior field remains zero at all times), the displacement current inside is also zero.  

   However, if we insist on keeping the **relationship** \(\mathbf D = \varepsilon\mathbf E\) while letting \(\mathbf E\to0\) but keeping \(\mathbf D\) finite (because surface charge may be finite), we can think of the **effective** permittivity as  

   \[
   \varepsilon_{\text{eff}} = \frac{D}{E}\;\; \xrightarrow[E\to0]{}\;\; \infty .
   \]

   Hence textbooks sometimes say a perfect conductor has an “infinite dielectric constant”. It is a **limit** rather than a literal material property: the *static* electric field is forced to zero, so the ratio \(D/E\) diverges.

4. In practice, real metals have a very large but finite σ (≈ 10⁷ S m\(^{-1}\)) and a finite ε that is dominated by the conduction term at low frequencies. At optical frequencies the conduction term becomes comparable to the displacement term, leading to a complex permittivity.

### 2.5  Why “high dielectric constant” ≠ “good conductor”  

| Property | High **εᵣ** (dielectric constant) | High **σ** (conductivity) |
|----------|-----------------------------------|---------------------------|
| Microscopic origin | Strong **polarizability** of bound charges (large χₑ) | Large density of **free carriers** (electrons or holes) |
| Energy storage | Large \(\tfrac12\varepsilon E^{2}\) → good capacitor material | Not relevant; energy dissipated as Joule heating |
| Loss (for AC) | Determined by **loss tangent** \(\tan\delta = \sigma/(\omega\varepsilon)\). A high εᵣ can still have tiny σ → low loss. | Large σ → large conduction loss (heat). |
| Example | Barium titanate (εᵣ≈ 5000, σ≈10⁻⁸ S m\(^{-1}\)) | Copper (σ≈ 5.8 × 10⁷ S m\(^{-1}\), εᵣ≈ 1) |

Thus a material can have a **very large dielectric constant** while still being an excellent insulator because its **conductivity** remains essentially zero.

### 2.6  Summarising the two “perfect” limits  

| Quantity | Perfect dielectric | Perfect conductor |
|----------|-------------------|--------------------|
| Conductivity σ | **0** (no free‑charge flow) | **∞** (free‑charge flow unlimited) |
| Resistivity ρ | **∞** | **0** |
| Permittivity ε (static) | Finite (material‑dependent) | **∞** (limit \(D/E\) as \(E\to0\)) |
| Electric field inside (static) | Can be non‑zero (field penetrates) | **0** |
| Polarization P | Finite (bound charges shift) | Not defined (bound charges negligible compared with free charges) |
| Energy storage | \(\tfrac12\varepsilon E^{2}\) (capacitor) | No static field → no stored electric energy (magnetic energy may dominate) |

The apparent “conflict” in the Wikipedia wording stems from mixing **two different limits**:  

* “High dielectric constant” refers to **large εᵣ** (strong bound‑charge response).  
* “Perfect conductor” refers to **σ→∞**, and the *mathematical* limit ε→∞ follows from the condition **E=0** inside.

---

## 3.  Final answer (concise)

* A **perfect dielectric** has **zero conductivity** (σ = 0, ρ = ∞) but a **finite permittivity** ε. The bound electrons can be displaced, producing polarization and storing electric energy, but no free charge moves; thus the material is an ideal insulator.

* A **perfect conductor** has **infinite conductivity** (σ → ∞, ρ → 0). In the static case the interior electric field must be zero; mathematically this forces the ratio **D/E** (the permittivity) to diverge, so one may say it has an “infinite dielectric constant”. The material’s response is dominated by free‑charge motion, not by bound‑charge polarization.

* “High dielectric constant” and “high conductivity” are **independent** properties. A material can possess a huge εᵣ while still having negligible σ, and vice‑versa.

---

## 4.  Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to correct it |
|---------|----------------|-------------------|
| **Confusing εᵣ with σ.** Thinking that a large dielectric constant automatically means the material conducts electricity. | εᵣ measures *how strongly bound charges polarize*; σ measures *how easily free charges move*. | Always ask: *Is the current due to free carriers (σ) or to dipole displacement (ε)?* |
| **Saying “electrons move in a dielectric”.** Interpreting polarization as a flow of charge through the bulk. | Polarization is a *local shift* of bound charge, not a net transport of charge from one side to the other. | Visualise each atom as a tiny dipole; the centre‑of‑charge of the whole sample does not move. |
| **Equating “infinite ε” with a real material property.** Believing a material can literally have infinite permittivity. | The “infinite ε” of a perfect conductor is a *limit* that results from forcing **E=0** inside; no real material has ε = ∞. | Remember that “∞” appears only in the *ideal* mathematical model, not in measured values. |
| **Thinking that a perfect dielectric can store unlimited charge.** | The charge that can be stored is limited by the breakdown field of the material; ε only tells how much energy per unit field is stored. | Distinguish **

*Original question: [Dilemma of Dielectric](https://physics.stackexchange.com/questions/876663/dilemma-of-dielectric) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
