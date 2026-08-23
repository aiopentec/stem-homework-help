---
layout: post
title: "Systematic approach to deriving equations of collective field theory to any order"
author: StemFix Bot
category: physics
tags: [physics]
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (plain‑language restatement)

The asker wants to know **how to obtain the equations of a collective‑field theory (CFT) in a controlled expansion in powers of \(1/N\)**, where \(N\) is the number of microscopic degrees of freedom (e.g. the size of a matrix or the number of particles).  

* In the original Sakita–Jevicki papers the collective Hamiltonian was written down and then approximations (large‑\(N\) limit, quadratic fluctuations) were made “by hand”.  
* The question is whether a **systematic, algorithmic procedure** exists that produces **all terms** in the \(1/N\) expansion, order by order.  
* The asker also wonders whether **Yaffe’s coherent‑state large‑\(N\) formalism** can be employed to achieve the same systematic expansion.

In short: **Give a step‑by‑step method that starts from a microscopic Hamiltonian, rewrites it in terms of collective fields, and generates the full \(1/N\) series (or equivalently the loop expansion) in a transparent way. Explain how Yaffe’s coherent‑state approach fits into this picture.**  

Below is a complete worked solution that shows every stage of the construction, the bookkeeping of powers of \(N\), and the connection to coherent states.

---

## 2.  Systematic derivation of collective‑field equations to any order in \(1/N\)

We will present the method for a **one‑dimensional bosonic many‑body system**; the extension to higher dimensions, to fermions, or to matrix models follows the same steps with only notational changes.

### 2.1  Microscopic model

Consider \(N\) identical particles on a line with canonical variables \((x_i,p_i)\) and Hamiltonian  

\[
H = \sum_{i=1}^{N}\frac{p_i^{2}}{2m}
      +\sum_{i=1}^{N} V(x_i)
      +\frac{1}{2N}\sum_{i\neq j}U\!\bigl(x_i-x_j\bigr) .
\tag{2.1}
\]

The factor \(1/N\) in the two‑body term makes the total interaction energy \(\mathcal O(N)\) (the standard ’t Hooft scaling).  

Our goal is to rewrite this theory in terms of the **density field**

\[
\rho(x) \equiv \frac{1}{N}\sum_{i=1}^{N}\delta\bigl(x-x_i\bigr),
\qquad
\int\!dx\,\rho(x)=1,
\tag{2.2}
\]

and its canonically conjugate momentum \(\pi(x)\).

---

### 2.2  Change of variables in the phase‑space path integral  

The quantum dynamics is encoded in the phase‑space (Hamiltonian) path integral

\[
Z = \int\!\prod_{i=1}^{N}{\cal D}x_i {\cal D}p_i\;
   \exp\!\Bigl\{ i\!\int\!dt
     \Bigl[\sum_i p_i\dot x_i - H(x,p)\Bigr]\Bigr\}.
\tag{2.3}
\]

Insert a functional representation of the identity that enforces the definition (2.2):

\[
1 = \int\!{\cal D}\rho\;
    \delta\!\Bigl[\rho(x)-\tfrac1N\!\sum_i\!\delta(x-x_i)\Bigr]
    \det\!\Bigl[\frac{\delta}{\delta\rho}\Bigl(\rho-\tfrac1N\sum_i\delta\Bigr)\Bigr],
\tag{2.4}
\]

where the determinant is the **Jacobian** of the change of variables.  

Perform the Fourier representation of the delta functional,

\[
\delta[\ldots]=\int\!{\cal D}\pi\;
   \exp\!\Bigl\{iN\!\int\!dt\,dx\,\pi(x,t)
   \bigl[\rho(x,t)-\tfrac1N\!\sum_i\!\delta(x-x_i(t))\bigr]\Bigr\},
\tag{2.5}
\]

so that \(\pi(x,t)\) appears as the conjugate momentum to \(\rho\).  

Carrying out the Gaussian integral over the particle momenta \(p_i\) and over the coordinates \(x_i\) **subject to the constraint** produces the **collective‑field path integral**

\[
Z = \int\!{\cal D}\rho\,{\cal D}\pi\;
    J[\rho]\,
    \exp\!\Bigl\{ iN^{2}\!\int\!dt\,L_{\rm coll}[\rho,\pi]\Bigr\},
\tag{2.6}
\]

where  

* \(L_{\rm coll}= \int\!dx\;\bigl(\pi\dot\rho - {\cal H}_{\rm coll}\bigr)\),  
* \({\cal H}_{\rm coll}\) is the **collective Hamiltonian density**, and  
* \(J[\rho]=\exp\{N^{2}S_{\!J}[\rho]\}\) is the **Jacobian factor** (sometimes called the “Vandermonde term”).  

Because each particle contributes a factor \(N\) in the definition (2.2), the overall prefactor of the exponent is \(N^{2}\); this is the source of the \(1/N\) loop expansion (the saddle point is of order \(N^{2}\), each quantum fluctuation costs a factor \(1/N\)).  

---

### 2.3  Exact collective Hamiltonian

Carrying out the integrations in (2.6) (see Sakita–Jevicki, *Ann. Phys.* **140** (1982) 406) yields

\[
\boxed{
\begin{aligned}
{\cal H}_{\rm coll}[\rho,\pi] &=
\frac{1}{2m}\int\!dx\;\frac{\bigl[\partial_x\!\bigl(\rho\pi\bigr)\bigr]^{2}}{\rho}
\;+\;\int\!dx\,V(x)\,\rho(x) \\
&\qquad +\frac12\!\int\!dx\,dy\;U(x-y)\,\rho(x)\rho(y)
\;+\;{\cal H}_{\rm J}[\rho] .
\end{aligned}
}
\tag{2.7}
\]

The first term is the **kinetic energy** written entirely in terms of \(\rho\) and its conjugate \(\pi\).  

The **Jacobian contribution** (the only term that carries explicit \(\hbar\)–type quantum corrections) is

\[
{\cal H}_{\rm J}[\rho] = \frac{\hbar^{2}}{8m}\int\!dx\;
      \frac{\bigl[\partial_x\rho(x)\bigr]^{2}}{\rho(x)^{3}} .
\tag{2.8}
\]

For bosons the \(\hbar\) can be set to 1; for fermions the sign flips.  The crucial point is that **\({\cal H}_{\rm J}\) is already of order \(N^{0}\)**, whereas the other pieces scale as \(N^{2}\) (because \(\rho\sim\mathcal O(1)\) and the overall factor in the exponent of (2.6) is \(N^{2}\)).  This separation of scales makes the systematic \(1/N\) expansion transparent.

---

### 2.4  Large‑\(N\) saddle point (classical collective field)

Define the **classical background** \(\rho_{0}(x)\) by the stationary‑phase condition

\[
\frac{\delta}{\delta\rho(x)}\Bigl[ N^{2}{\cal S}_{\rm cl}[\rho]\Bigr]_{\,\rho=\rho_{0}}=0,
\qquad
{\cal S}_{\rm cl} = \int\!dt\!\int\!dx\;\Bigl[\pi\dot\rho-{\cal H}_{\rm coll}\Bigr] .
\tag{2.9}
\]

Since \(\pi\) appears linearly in the action, the variation w.r.t. \(\pi\) gives the **continuity equation**

\[
\dot\rho_{0}(x,t)+\partial_{x}\!\bigl[\,\rho_{0}(x,t) v_{0}(x,t)\bigr]=0,
\qquad
v_{0}\equiv\frac{1}{m}\partial_{x}\pi_{0},
\tag{2.10}
\]

and variation w.r.t. \(\rho\) yields the **Euler (force) equation**

\[
m\dot v_{0}+v_{0}\partial_{x}v_{0}
      = -\partial_{x}V(x)-\int\!dy\,U'(x-y)\,\rho_{0}(y)
      +\frac{\hbar^{2}}{2m

*Original question: [Systematic approach to deriving equations of collective field theory to any order](https://physics.stackexchange.com/questions/27016/systematic-approach-to-deriving-equations-of-collective-field-theory-to-any-orde) on Physics Stack Exchange, licensed CC BY-SA.*
