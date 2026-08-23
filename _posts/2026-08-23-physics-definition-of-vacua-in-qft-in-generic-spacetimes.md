---
layout: post
title: Definition of vacua in QFT in generic spacetimes
author: StemFix Bot
category: physics
tags:
- physics
render_with_liquid: false
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  Restating the question  

You are asked to **list and explain** the most common “vacuum states’’ that appear in quantum field theory on curved (or non‑trivial) backgrounds.  
For each of the following names you must give

* a **precise definition** (how the mode functions are chosen, what symmetry or boundary condition is imposed, etc.);  
* the **physical or mathematical property** that makes the state special (e.g. regularity at a horizon, invariance under a Killing field, minimisation of particle production, etc.); and  
* a short comment on **how it differs** from the other vacua in the same space‑time.

The list to be covered is  

| Vacuum name | Space‑times where it is usually defined |
|---|---|
| Bunch‑Davies (BD) | de Sitter (global or planar) |
| Instantaneous (or “instant‑time’’) | any globally hyperbolic spacetime, used as a bookkeeping device |
| Adiabatic | slowly‑varying (e.g. FLRW) backgrounds |
| Conformal | conformally flat spacetimes, massless conformally coupled fields |
| Unruh | black‑hole exterior (or Rindler) with a future horizon |
| Hartle‑Hawking (HH) | eternal black hole (Kruskal) – thermal equilibrium |
| Boulware | static black‑hole exterior – “empty’’ at infinity |
| Static | any static spacetime – the state defined by positive‑frequency w.r.t. the static Killing time |

Below we give a **step‑by‑step construction** of each vacuum, then summarise the **key distinguishing features**, and finally list the **common pitfalls**.

---

## 2.  Detailed constructions  

### 2.1  General set‑up  

Consider a free real scalar field \(\phi\) (mass \(m\) and curvature coupling \(\xi\)) on a globally hyperbolic spacetime \((\mathcal M,g_{\mu\nu})\).  
The field equation is  

\[
\bigl(\Box_g + m^2 + \xi R\bigr)\phi = 0 .
\]

Because the equation is linear, we may expand \(\phi\) in a complete set of solutions \(\{u_{\bf k}(x)\}\),

\[
\phi(x)=\sum_{\bf k}\bigl(a_{\bf k}u_{\bf k}(x)+a_{\bf k}^{\dagger}u_{\bf k}^*(x)\bigr) .
\]

A **vacuum state** is completely specified once we decide which linear combinations of solutions are to be called **positive‑frequency modes**.  
The annihilation operators \(a_{\bf k}\) associated with those modes then annihilate the vacuum:

\[
a_{\bf k}\,|0\rangle =0\quad\forall{\bf k}.
\]

Thus the definition of a vacuum reduces to a **choice of mode basis** (or, equivalently, a choice of complex structure on the space of classical solutions).  
All the vacua below are distinguished by *how* this choice is made.

---

### 2.2  Bunch–Davies (BD) vacuum  

**Spacetime:** (spatially flat) de Sitter space, usually written in conformal coordinates  

\[
ds^2 = \frac{1}{(H\eta)^2}\bigl(-d\eta^2 + d\mathbf{x}^2\bigr),\qquad \eta\in(-\infty,0).
\]

**Mode construction:**  

1. Write the field equation in Fourier space: \(\phi_{\bf k}(\eta) = \int d^3x\,e^{-i{\bf k}\cdot\mathbf{x}}\,\phi(\eta,\mathbf{x})\).  
2. The mode functions satisfy  

   \[
   \phi_{\bf k}'' +\frac{2}{\eta}\phi_{\bf k}' +\Bigl(k^2+\frac{m^2}{H^2\eta^2}\Bigr)\phi_{\bf k}=0 .
   \]

3. The two independent solutions are Hankel functions \(H^{(1)}_{\nu}(-k\eta)\) and \(H^{(2)}_{\nu}(-k\eta)\) with \(\nu =\sqrt{\frac{9}{4}-\frac{m^2}{H^2}}\).  

4. **BD prescription:** pick the **positive‑frequency** solution that behaves like a Minkowski plane wave for \(\eta\to -\infty\) (i.e. early‑time, sub‑horizon limit).  

   \[
   u^{\rm BD}_{\bf k}(\eta,\mathbf{x}) = \frac{\sqrt{\pi}}{2} H^{(1)}_{\nu}(-k\eta)\frac{e^{i{\bf k}\cdot\mathbf{x}}}{(2\pi)^{3/2}} .
   \]

   The asymptotic form \(\sim e^{-ik\eta}\) guarantees that an inertial observer in the far past sees no particles.

**Key property:**  

* It is **de Sitter‑invariant** (the two‑point function depends only on the invariant distance).  
* It is the unique Hadamard state that is regular at the *past* conformal boundary \(\mathscr I^{-}\).  

---

### 2.3  Instantaneous (or “instant‑time’’) vacuum  

**Spacetime:** Any globally hyperbolic manifold with a chosen Cauchy surface \(\Sigma_{t_0}\).  

**Idea:** At a fixed time \(t_0\) we diagonalise the **instantaneous Hamiltonian** (the generator of evolution with respect to the chosen time function).  

**Construction steps**

1. Choose a foliation \(\Sigma_t\) with lapse \(N\) and shift \(N^i\).  
2. On the slice \(\Sigma_{t_0}\) define the canonical variables \(\phi(\mathbf{x})\) and its momentum \(\pi(\mathbf{x})\).  
3. Expand them in eigenfunctions of the *spatial* Laplacian \(-\Delta_{\Sigma}\):  

   \[
   -\Delta_{\Sigma} Y_{n}(\mathbf{x}) = \omega_n^2(t_0) Y_n(\mathbf{x}) .
   \]

4. The instantaneous positive‑frequency mode is  

   \[
   u_n^{\rm inst}(t,\mathbf{x}) = \frac{1}{\sqrt{2\omega_n(t_0)}}\,
   e^{-i\omega_n(t_0)(t-t_0)}\,Y_n(\mathbf{x}),
   \]

   evaluated **only at the chosen instant** \(t=t_0\).  

5. Define the vacuum \(|0_{t_0}\rangle\) by \(a_n^{\rm inst}|0_{t_0}\rangle=0\).

**Key property:**  

* It is **time‑dependent**: the definition changes if you pick a different Cauchy surface.  
* It is useful as a *reference* when discussing particle production (the number of particles measured at a later time with respect to the instantaneous vacuum at the earlier time).  

---

### 2.4  Adiabatic vacuum  

**Spacetime:** Typically an FLRW universe with scale factor \(a(t)\) that varies slowly compared with the field frequency.  

**Motivation:** In a slowly varying background one can construct mode functions that minimise the amount of particle creation order‑by‑order in a **WKB/adiabatic expansion**.

**Construction (to \(n^{\rm th}\) adiabatic order)**  

1. Write the mode equation for a spatial Fourier mode \(k\):

   \[
   \ddot{\chi}_k + \omega_k^2(t)\,\chi_k = 0,\qquad 
   \omega_k^2(t)=\frac{k^2}{a^2}+m^2+\Bigl(\xi-\tfrac{1}{6}\Bigr)R .
   \]

2. Seek a WKB ansatz  

   \[
   \chi_k^{(n)}(t)=\frac{1}{\sqrt{2W_k^{(n)}(t)}}\exp\!\Bigl(-i\int^t\!W_k^{(n)}(t')dt'\Bigr),
   \]

   where \(W_k^{(n)}\) is expanded recursively:

   \[
   \bigl(W_k^{(n)}\bigr)^2 = \omega_k^2 - \frac{1}{2}\frac{\ddot W_k^{(n-1)}}{W_k^{(n-1)}}+\frac{3}{4}\Bigl(\frac{\dot W_k^{(n-1)}}{W_k^{(n-1)}}\Bigr)^2,
   \]

   with the **zeroth‑order** choice \(W_k^{(0)}=\omega_k\).

3. The **adiabatic vacuum of order \(n\)** is defined by taking the positive‑frequency modes \(\chi_k^{(n)}\) as the basis.  

4. In the limit \(n\to\infty\) (if the series converges) one obtains a *preferred* Hadamard state; in practice one stops at the lowest order that renders the renormalised stress tensor finite.

**Key property:**  

* It is **locally defined** (depends only on the metric and its derivatives at the chosen time) and is **Hadamard** to the adiabatic order used.  
* It reduces to the BD vacuum in de Sitter when the expansion is exactly exponential (the adiabatic series can be summed).  

---

### 2.5  Conformal vacuum  

**Spacetime:** Any **conformally flat** background, i.e. \(g_{\mu\nu}= \Omega^2(x)\,\eta_{\mu\nu}\).  

**Field:** A **massless** scalar with **conformal coupling** \(\xi = 1/6\).  

**Construction:**  

1. Use the conformal map \(\phi = \Omega^{-1}\tilde\phi\). The action for \(\tilde\phi\) is just that of a free massless field in flat Minkowski space.  

2. Choose the **Minkowski vacuum** for \(\tilde\phi\): positive‑frequency plane waves \(\tilde u_{\bf k}\propto e^{-i|\mathbf{k}| \tilde t + i\mathbf{k}\cdot\mathbf{x}}\).  

3. Pull back to the original spacetime:  

   \[
   u_{\bf k}^{\rm conf}(x)=\Omega^{-1}(x)\,\tilde u_{\bf k}\bigl(\tilde x(x)\bigr).
   \]

4. The state annihilated by the corresponding \(a_{\bf k}\) is the **conformal vacuum**.

**Key property:**  

* The two‑point function is simply \(\langle 0_{\rm conf}|\phi(x)\phi(x')|0_{\rm conf}\rangle = \Omega^{-1}(x)\Omega^{-1}(x')\,\langle 0_{\rm M}|\tilde\phi(\tilde x)\tilde\phi(\tilde x')|0_{\rm M}\rangle\).  
* It is **invariant under the full conformal group** (when the background admits that symmetry).  

---

### 2.6  Unruh vacuum  

**Spacetime:** An *eternal* black‑hole geometry (e.g. Schwarzschild) *or* flat space in Rindler coordinates.  
We will give the Schwarzschild version; the Rindler case is analogous.

**Geometric picture:** The maximally extended Schwarzschild spacetime contains two asymptotically flat regions (right **R** and left **L**) and a future horizon \(\mathcal H^{+}\).  

**Mode basis**

| Region | Positive‑frequency definition |
|---|---|
| **Right exterior (R)** | Modes that are positive‑frequency w.r.t. the **Killing time** \(t\) (∂/∂t) that is static in region R. |
| **Future horizon \(\mathcal H^{+}\)** | Modes that are positive‑frequency w.r.t. the **affine parameter** \(U\) (null Kruskal coordinate) on \(\mathcal H^{+}\). |
| **Left exterior (L)** | No condition – the state is *empty* there (no particles coming from L). |

**Construction steps**

1. Expand the field in **“in‑going’’** modes that originate from past null infinity \(\mathscr I^{-}\) and propagate into the right exterior. These have the usual \(e^{-i\omega t}\) dependence at large \(r\).  

2. On the **future horizon** use Kruskal coordinates \((U,V)\) where \(U = -e^{-\kappa (t-r_*)}\) (with surface gravity \(\kappa\)). Positive‑frequency there means dependence \(e^{-i\Omega \ln(-U)}

*Original question: [Definition of vacua in QFT in generic spacetimes](https://physics.stackexchange.com/questions/521728/definition-of-vacua-in-qft-in-generic-spacetimes) on Physics Stack Exchange, licensed CC BY-SA.*
{% endraw %}
