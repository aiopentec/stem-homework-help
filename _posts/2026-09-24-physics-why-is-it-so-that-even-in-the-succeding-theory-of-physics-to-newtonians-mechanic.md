---
layout: question
title: Why is it so that even in the succeding theory of physics to Newtonians mechanics,
  the conceptual scaffolding of the theory still transfers?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Why is it so that even in the succeding
  theory of physics to Newtonians mechanics, the conceptual scaffolding of the theory '
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  Restating the Question in Plain Language  

A student is wondering why the **basic ideas** that we learn in *Newtonian mechanics* – things like **position, momentum, energy, force, mass, time, etc.** – keep showing up, often with the same names, when we move to more modern theories such as **quantum mechanics (QM)** and **general relativity (GR)**.  

The question can be broken down into three parts  

1. **Why do these concepts survive the transition to newer theories?**  
2. **What is the “core” of Newtonian mechanics that is still useful in the other theories?**  
3. **Why is it justified to treat that core as the underlying conceptual backbone of physics?**  

Below we will answer each part step‑by‑step, showing the logical chain that connects the old and the new theories.

---

## 2.  Detailed Explanation (Step‑by‑Step)

### Step 1 – Identify the “conceptual scaffolding’’ of Newtonian mechanics  

Newtonian mechanics rests on a small set of **primitive concepts** and **mathematical structures**:

| Primitive concept | Symbolic/Mathematical representation | Physical role |
|-------------------|--------------------------------------|---------------|
| **Space** (where things are) | \(\mathbf{x}\in\mathbb{R}^3\) (a point vector) | Provides a *stage* for the system |
| **Time** (when things happen) | \(t\in\mathbb{R}\) | Orders events, gives dynamics |
| **Mass** (inertia) | \(m\) (scalar, positive) | Relates force to acceleration |
| **Force** (cause of change) | \(\mathbf{F}\) | Determines how \(\mathbf{x}(t)\) changes |
| **Momentum** | \(\mathbf{p}=m\mathbf{v}\) | Conserved quantity for isolated systems |
| **Energy** | \(E = T+V = \frac12 m v^2 + V(\mathbf{x})\) | Conserved quantity (if system is time‑invariant) |
| **Newton’s second law** | \(\mathbf{F}=m\mathbf{a}\) | Equation of motion |

These concepts are tied together by **two mathematical ideas**:

1. **Differential calculus** (rates of change, acceleration).  
2. **Symmetry → conservation laws** (Noether’s theorem in later language).

### Step 2 – Recognise the *universal* aspects of those concepts  

Even though Newton’s specific **law** (\(\mathbf{F}=m\mathbf{a}\)) is replaced, the *structures* above are **universal**:

| Universal aspect | Reason it survives |
|------------------|--------------------|
| **Configuration space** (the set of all possible positions) | Any physical theory must describe *what* a system can be. In QM it becomes a Hilbert space; in GR it becomes a curved manifold. |
| **Time parameter** (ordering of events) | Dynamics needs a notion of “before” and “after”. In non‑relativistic QM we keep a global time; in GR the parameter is replaced by proper time along world‑lines, but the idea of a parameter that orders events stays. |
| **Momentum as generator of translations** | In QM, \(\hat{p}\) is the operator that generates spatial translations (via \(e^{-i\hat{p}x/\hbar}\)). In GR, the covariant momentum \(p_\mu\) is the generator of diffeomorphisms along a world‑line. |
| **Energy as generator of time translations** | In QM, \(\hat{H}\) generates time evolution (Schrödinger equation). In GR, the Hamiltonian constraint generates evolution in the chosen foliation of spacetime. |
| **Conservation laws from symmetries** | Noether’s theorem works in Lagrangian/Hamiltonian formulations that are common to all three theories. |
| **Mass as a label of representation** | In QM mass appears in the Schrödinger equation, in GR it appears in the stress‑energy tensor; both describe how a system responds to geometry or fields. |

Thus the *names* persist because the **same mathematical roles** persist, even though the *formulas* change.

### Step 3 – How each modern theory inherits the concepts  

#### 3.1 Quantum Mechanics (QM)

| Newtonian concept | QM analogue | How it appears |
|-------------------|-------------|----------------|
| Position \(\mathbf{x}\) | Position operator \(\hat{\mathbf{x}}\) | Eigenstates \(|\mathbf{x}\rangle\) form a continuous basis of the Hilbert space. |
| Momentum \(\mathbf{p}\) | Momentum operator \(\hat{\mathbf{p}} = -i\hbar\nabla\) | Generates spatial translations via the unitary operator \(U(\mathbf{a}) = e^{-i\mathbf{a}\cdot\hat{\mathbf{p}}/\hbar}\). |
| Energy \(E\) | Hamiltonian \(\hat{H}\) | Generates time evolution: \(i\hbar\frac{d}{dt}|\psi(t)\rangle = \hat{H}|\psi(t)\rangle\). |
| Force \(\mathbf{F}\) | Potential term in \(\hat{H}\) (e.g., \(\hat{V}(\hat{\mathbf{x}})\)) | The gradient of the potential gives the expectation value of force via Ehrenfest’s theorem: \(\langle\dot{\mathbf{p}}\rangle = -\langle\nabla V\rangle\). |
| Mass \(m\) | Parameter in kinetic term \(\hat{T}= \hat{p}^2/2m\) | Determines dispersion relation and de Broglie wavelength. |
| Conservation laws | Commutators with \(\hat{H}\) | If \([\hat{O},\hat{H}]=0\) then \(\langle O\rangle\) is constant (Noether). |

*Key point*: The **operator algebra** \([\hat{x}_i,\hat{p}_j]=i\hbar\delta_{ij}\) is a *quantized* version of the classical Poisson bracket \(\{x_i,p_j\}= \delta_{ij}\). Thus the classical phase‑space structure survives in a *non‑commutative* form.

#### 3.2 General Relativity (GR)

| Newtonian concept | GR analogue | How it appears |
|-------------------|-------------|----------------|
| Space + Time (absolute) | 4‑dimensional spacetime manifold \(\mathcal{M}\) with metric \(g_{\mu\nu}\) | Geometry replaces the rigid background; still a *stage* for events. |
| Position \(\mathbf{x}(t)\) | World‑line \(x^\mu(\tau)\) (a curve in spacetime) | Parameterised by proper time \(\tau\). |
| Momentum \(\mathbf{p}=m\mathbf{v}\) | 4‑momentum \(p^\mu = m u^\mu\) with \(u^\mu = dx^\mu/d\tau\) | Tangent to the world‑line; conserved along geodesics in symmetric spacetimes. |
| Energy (kinetic + potential) | Conserved quantity associated with timelike Killing vector (if spacetime has time‑translation symmetry) | \(E = -p_\mu \xi^\mu\) where \(\xi^\mu\) is the Killing vector. |
| Force \(\mathbf{F}=m\mathbf{a}\) | No *force*; motion follows **geodesic equation** \(u^\nu\nabla_\nu u^\mu = 0\) | Acceleration is replaced by curvature of spacetime. |
| Mass \(m\) | Rest mass (invariant) appears in stress‑energy tensor \(T_{\mu\nu}\) | Sources curvature via Einstein equation \(G_{\mu\nu}=8\pi G T_{\mu\nu}\). |
| Conservation laws | Covariant divergence \(\nabla_\mu T^{\mu\nu}=0\) | Generalises energy‑momentum conservation. |

*Key point*: GR **re‑expresses** Newton’s ideas in a **geometrical language**. The same quantities (position, momentum, energy) become components of **four‑vectors** and **tensors**, but the underlying idea – *a quantity that tells you “where” and “how fast” a system is* – is unchanged.

### Step 4 – Why the Newtonian “core” is justified  

1. **Empirical continuity** – All three theories must reproduce the *same* experimental results in the domain where Newtonian mechanics is known to work (low speeds, weak gravity, macroscopic objects). This forces the newer theories to *reduce* to Newtonian formulas in the appropriate limit (the **correspondence principle**).

2. **Mathematical structure** – The **symplectic (phase‑space) structure** of classical mechanics underlies both QM (through canonical quantisation) and GR (through Hamiltonian formulations of gravity). The **Lie algebra of the Galilean group** (translations, rotations, boosts) is deformed into the **Poincaré algebra** (special relativity) and then further generalized to the **diffeomorphism group** (GR). The *generators* of these groups are still called momentum and energy.

3. **Physical intuition** – Humans experience the world in terms of *where* things are and *how* they move. The language of position, velocity, momentum, and energy is therefore an **effective description** that any successful theory must translate into its own formalism.

4. **Dimensional analysis and units** – The fundamental dimensions **[L] (length)**, **[M] (mass)**, **[T] (time)** remain the basis for building any physical quantity. Even in relativistic or quantum contexts, the *combinations* that give rise to momentum \([ML/T]\) or energy \([ML^2/T^2]\) are still meaningful.

5. **Noether’s theorem** – Conservation of momentum and energy follows from **spatial** and **temporal** symmetries. Those symmetries exist (though sometimes only locally) in QM and GR, so the associated conserved quantities retain the same names.

### Step 5 – Summarising the “core”  

The **core** that survives the transition can be expressed in a compact, theory‑independent way:

> **Core Statement**  
> *A physical system is described by a set of variables that specify its configuration (position‑like coordinates) and by conjugate variables that generate translations in those coordinates (momentum‑like quantities). If the dynamics is invariant under spatial translations, the conjugate quantities are conserved (momentum). If it is invariant under time translations, the generator of time evolution is conserved (energy). These statements hold regardless of whether the underlying geometry is Euclidean, Minkowskian, or curved, and regardless of whether the variables commute (classical) or obey quantum commutation relations.*

All three theories can be written in the **Hamiltonian formalism**:

- **Newtonian**: \( \dot{q}= \partial H/\partial p,\;\dot{p}= -\partial H/\partial q \) with Poisson brackets.  
- **Quantum**: \( i\hbar\dot{\hat{O}} = [\hat{O},\hat{H}] \) (Heisenberg picture).  
- **General Relativistic (canonical) gravity**: Hamiltonian constraint \( \mathcal{H}=0 \) and momentum constraints generate spacetime diffeomorphisms.

Thus the *same* algebraic skeleton (variables + Poisson/commutator brackets + Hamiltonian) underlies all three, and the familiar words are simply the historical labels that persist.

---

## 3.  Final Answer  

**Answer (in plain terms):**  

The reason concepts such as position, momentum, and energy keep appearing in quantum mechanics and general relativity is that they are **not specific to Newton’s force law**; they are the *structural pillars* of any dynamical theory.  

1. **Position** tells us the configuration of a system; in QM it becomes a *operator* on a Hilbert space, in GR it becomes a *point on a curved spacetime manifold*.  
2. **Momentum** is the generator of spatial translations; the same role is played by the quantum momentum operator \(-i\hbar\nabla\) and by the covariant four‑momentum in GR.  
3. **Energy** is the generator of time translations; it is the Hamiltonian in QM and the conserved quantity associated with a timelike Killing vector (or the Hamiltonian constraint) in GR.  

These concepts survive because:

* They are tied to **symmetries** (space‑ and time‑translation invariance) via Noether’s theorem, which holds in all three frameworks.  
* They appear naturally in the **Hamiltonian (or Lagrangian) formulation**, a mathematical language common to Newtonian mechanics, QM, and GR.  
* The **correspondence principle** forces any new theory to reproduce Newtonian results in the appropriate limit, so the same quantities must be recognizable.  

Thus the “core” of Newtonian mechanics that persists is **the identification of a configuration space, its conjugate momenta, and the generators of translations in space and time, together with the symmetry‑based conservation laws**. This core is justified because it is rooted in universal mathematical structures (symplectic geometry, Lie algebras, Noether’s theorem) and in the empirical requirement that newer theories agree with Newtonian predictions where the latter are known to be accurate.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking “momentum = mass × velocity” is fundamental** | In relativity the

*Original question: [Why is it so that even in the succeding theory of physics to Newtonians mechanics, the conceptual scaffolding of the theory still transfers?](https://physics.stackexchange.com/questions/876335/why-is-it-so-that-even-in-the-succeding-theory-of-physics-to-newtonians-mechanic) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
