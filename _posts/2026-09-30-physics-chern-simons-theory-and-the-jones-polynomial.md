---
layout: question
title: Chern-Simons theory and the Jones Polynomial
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Chern-Simons theory and the Jones Polynomial'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the student is really asking  

The student wants to understand three rather subtle points that appear in Witten’s 1989 paper *“Quantum Field Theory,  Chern‑Simons Theory, and the Jones Polynomial”* :

| # | Question (in plain language) |
|---|------------------------------|
| 1 | **Why do we have to frame Wilson lines?**  Even though the expectation value of an *unframed* Wilson line in Chern‑Simons theory is finite, it depends on the background metric. Does that make the observable “invalid” or simply “unphysical”? |
| 2 | **How does changing the framing give anyonic statistics?**  When we twist the framing of a Wilson line, the expectation value picks up a phase. Why can we interpret that phase as the statistical phase of the point‑like excitations that sit at the ends of the line? |
| 3 | **Does the canonical Gauss‑law constraint already contain the framing information?**  In the Hamiltonian picture we impose \((\rho - \frac{k}{2\pi}\epsilon^{ij}\partial_i A_j)\,|\psi\rangle =0\). Is any reference to framing hidden in this equation, or does it have to be added later? |

Below we answer each question systematically, spelling out the underlying physics and the mathematics that Witten used.  

---

## 2.  Answer to Question 1 – Why must we *frame* Wilson lines?

### 2.1  Wilson lines in Chern‑Simons theory  

In pure Chern‑Simons theory with gauge group \(G\) and level \(k\),

\[
S_{\text{CS}}[A]=\frac{k}{4\pi}\int_M \operatorname{Tr}\!\left(A\wedge dA+\tfrac{2}{3}A\wedge A\wedge A\right)
\]

the classical equations of motion are \(F=0\); the gauge field is flat.  
A Wilson line in representation \(R\) along a (oriented) curve \(\gamma\) is

\[
W_R(\gamma)=\operatorname{Tr}_R \,\mathcal{P}\exp\!\left(i\int_\gamma A\right) .
\]

In the *topological* quantum field theory (TQFT) we would like the vacuum expectation value (VEV)

\[
\langle W_R(\gamma)\rangle = \int \mathcal{D}A\,e^{iS_{\text{CS}}[A]}W_R(\gamma)
\]

to be a **topological invariant** of the embedded curve (or link, when several lines are present).

### 2.2  The framing anomaly  

When the path integral is regularised (e.g. using point‑splitting, Pauli–Villars, or lattice regularisation) a short‑distance cutoff must be introduced. Because Chern‑Simons theory is *first‑order* in derivatives, the regulator inevitably breaks the naïve diffeomorphism invariance: the regularised theory depends on a **choice of framing** – a continuous choice of a non‑vanishing normal vector field along each Wilson line.  

* What actually happens is that the self‑linking number (or **framing number**) of the curve appears in the perturbative expansion.  
* In perturbation theory the one‑loop diagram that contracts the Wilson line with itself yields a factor  

  \[
  \exp\!\Bigl(2\pi i\,\frac{C_2(R)}{k}\, \mathrm{fr}(\gamma)\Bigr),
  \]

  where \(\mathrm{fr}(\gamma)\) is the **self‑linking** (framing) number and \(C_2(R)\) is the quadratic Casimir of \(R\).  

If we ignore the framing (i.e. set \(\mathrm{fr}=0\) by hand) the result is **finite**, but it **depends on the metric** that was used to define the short‑distance cutoff. Changing the metric changes the way the Wilson line is regularised, and the VEV changes by precisely the above phase.

### 2.3  Why metric‑dependence makes the observable “invalid” as a TQFT observable  

* In a **topological quantum field theory** the set of admissible observables must be *metric‑independent* after renormalisation. Otherwise the theory would not be purely topological; different choices of background geometry would give different numbers for the same knot.  
* The *finite* value you obtain for an unframed line is **not** a topological invariant; it is a **regularisation‑scheme dependent** number. In a rigorous mathematical definition of the Chern‑Simons TQFT (Reshetikhin–Turaev, Witten‑Reshetikhin–Turaev invariants) the path integral is defined only after a framing has been fixed. The resulting invariant is the **framed** Jones (or HOMFLY‑PT, etc.) polynomial.  
* One can of course *choose* a particular framing (e.g. the blackboard framing) and declare that to be the definition of the observable. But the **choice** must be recorded; otherwise the “observable” is ambiguous.  

Hence the answer: **Unframed Wilson lines are not part of the spectrum of the Chern‑Simons TQFT because they are not topological observables – they retain a hidden dependence on the metric introduced by the regularisation.** They are perfectly fine as operators in a *non‑topological* regularised gauge theory, but they do not define the knot invariants that Witten was after.

---

## 3.  Answer to Question 2 – Framing change ↔ anyonic statistics  

### 3.1  Wilson lines ending on particles  

In a (2+1)‑dimensional Chern‑Simons theory coupled to static point charges, the Wilson line can be thought of as the world‑line of a heavy particle that carries a representation \(R\) of the gauge group. The particle itself lives at the **endpoints** of the line (if the line is open) or, in a closed loop, there are no endpoints and the line just creates a “flux tube”.

The exchange of two such particles is represented by a braid of their world‑lines. Because the Chern‑Simons action is *first order* in time, the path‑integral weight of a braid is purely a phase: the theory is *abelian* (in the sense of “no local degrees of freedom”), but the phase can be *fractional* – this is the hallmark of anyons.

### 3.2  The framing twist  

Consider a single Wilson line \(\gamma\) together with a chosen framing \(\hat{n}(s)\) (a unit normal vector along the curve). A **twist** of the framing by \(+1\) means that as we travel once around the curve the normal vector rotates by \(2\pi\). Topologically this is equivalent to adding a **self‑linking** of \(+1\) (the curve linked with a copy displaced along \(\hat{n}\)).  

The perturbative result quoted above tells us that adding one unit of self‑linking multiplies the expectation value by

\[
\exp\!\Bigl(2\pi i\,\frac{C_2(R)}{k}\Bigr) .
\tag{1}
\]

For the simplest case \(G=SU(2)\) and \(R\) the spin‑\(j\) representation, \(C_2(R)=j(j+1)\). Thus a single twist gives the phase  

\[
\theta_R = \frac{2\pi\,j(j+1)}{k}\; .
\]

### 3.3  Interpreting the phase as a statistical angle  

When two identical particles are exchanged, the braid can be decomposed (up to isotopy) into a **half‑twist** of each particle’s framing plus a trivial motion. More concretely, the world‑line picture of the exchange shown in the question can be continuously deformed into a picture in which each particle’s world‑line acquires *half* of a full framing twist.  

Because the phase (1) is *linear* in the framing number, a half‑twist contributes **half** of the phase (1). Consequently the exchange of two identical particles of type \(R\) multiplies the total wave‑function by

\[
e^{i\theta_R/2}= \exp\!\Bigl(i\pi\,\frac{C_2(R)}{k}\Bigr) .
\tag{2}
\]

Equation (2) is precisely the **anyonic statistics** angle for the quasiparticles associated with representation \(R\). For \(SU(2)_k\) with \(j=1/2\) we get  

\[
\theta_{1/2}= \frac{\pi}{k},
\]

so for \(k=1\) the particles are **fermions** (\(e^{i\pi}=-1\)), for \(k=2\) they are **semions** (\(e^{i\pi/2}=i\)), etc.

### 3.4  Relation to the diagrammatic argument in the question  

The student's picture:

1. Create two particle‑antiparticle pairs.  
2. Braid (exchange) two of the particles.  
3. Annihilate the pairs.

When the braid is “pinched” into a small loop, the loop can be removed at the price of a framing twist. The loop removal contributes exactly the factor \(\exp(2\pi i C_2(R)/k)\). Since the loop is *contractible* it does not affect the topology of the remaining world‑lines, but the **framing change** remains, giving the overall phase (2).  

Thus the argument is **correct in principle**, provided one keeps track of the fact that a *full* self‑linking (a closed loop) contributes the phase (1); a *half* linking (the exchange) contributes its square‑root, i.e. the anyonic statistical phase. The sign \(-1\) that the student obtained corresponds to the special case \(k=1\), \(R\) the fundamental of \(SU(2)\), where the anyons are ordinary fermions.

---

## 4.  Answer to Question 3 – Does the canonical Gauss law know about framing?  

### 4.1  The Gauss‑law constraint  

In the Hamiltonian formulation on a spatial surface \(\Sigma\) (say a plane or a torus) we write the Chern‑Simons action in temporal gauge \(A_0=0\):

\[
S_{\text{CS}}=\frac{k}{4\pi}\int dt\int_\Sigma \epsilon^{ij}\, \text{Tr}\!\bigl(A_i\dot A_j\bigr)\; .
\]

Varying with respect to \(A_0\) (which is a Lagrange multiplier) yields the **Gauss law**

\[
\boxed{ \; \frac{k}{2\pi}\,\epsilon^{ij}F_{ij}(x) = \rho(x) \; } ,
\tag{3}
\]

where \(\rho\) is the external charge density (e.g. Wilson line endpoints). In the quantum theory this becomes an operator condition on physical states:

\[
\bigl(\rho(x)-\frac{k}{2\pi}\epsilon^{ij}\partial_i A_j(x)\bigr)\,|\psi\rangle =0 .
\]

### 4.2  Where does framing appear?  

Equation (3) itself is **purely topological**; it contains no reference to any framing or metric. The Gauss law tells us that the magnetic flux through any small region equals the charge inside, i.e. the *holonomy* of the gauge field is fixed by the Wilson‑line insertions.  

The **framing dependence** enters **later**, when we evaluate the Wilson‑line expectation value **inside** the physical Hilbert space defined by (3). Concretely:

1. **Regularisation** – To define the product \(W_R(\gamma)\) as an operator, we must regularise the coincident point on the curve. The standard point‑splitting regularisation separates the curve from a copy displaced along a chosen normal vector field. That normal field is exactly the **framing**.  

2. **Operator ordering / path‑integral measure** – In canonical quantisation the equal‑time commutator  

   \[
   [A_i^a(x),A_j^b(y)] = \frac{2\pi i}{k}\,\epsilon_{ij}\,\delta^{ab}\,\delta^{(2)}(x-y)
   \]

   implies that a Wilson line operator is *ill‑defined* without a prescription for how to treat the self‑contraction of the line. The prescription is equivalent to a choice of framing.  

3. **Physical consequence** – When we compute the matrix element \(\langle\psi_f|W_R(\gamma)|\psi_i\rangle\) using the Gauss‑law‑constrained Hilbert space, the result acquires the framing factor (1). Thus the **Gauss law does not “know” about framing**, but **the representation of Wilson‑line operators on the constrained Hilbert space does**, because the latter requires a regularisation that breaks diffeomorphism invariance.

### 4.3  Summary  

* The **constraint** (3) is metric‑free and framing‑free.  
* The **observable** (the Wilson line) is only defined after we *choose* a framing in order to regulate its self‑linking.  
* Consequently, the **physical Hilbert space** together with a **choice of framing** yields a well‑defined representation of the braid group, and the anyonic phases appear precisely from the framing choice.

---

## 5.  Final Answers  

| # | Answer (concise

*Original question: [Chern-Simons theory and the Jones Polynomial](https://physics.stackexchange.com/questions/876502/chern-simons-theory-and-the-jones-polynomial) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
