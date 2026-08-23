---
layout: post
title: Field theory based on square-well potential?
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

The student wants to know whether one can formulate a **relativistic scalar field theory** whose self‑interaction potential is a *square‑well* :

\[
V(\phi)=\begin{cases}
0 & \text{if }-1<\phi<1,\\[2pt]
\infty & \text{otherwise},
\end{cases}
\qquad\qquad (\;V(\phi)=\lim_{p\to\infty}\phi^{\,p}\;).
\]

In other words the field value at every space‑time point is **forced** to stay inside the interval \((-1,1)\).  
The student tried to write down a lattice Hamiltonian, guessed a product of one‑particle box‑wave‑functions for the ground‑state functional, and then asked:

* Is the theory well‑defined?  
* What does the exact ground‑state wave functional look like?  
* How do we construct excited states (e.g. a one‑particle state with momentum \(k\))?  

Below we answer these points step by step, showing every algebraic and conceptual step.

--------------------------------------------------------------------

## 2. Setting up the problem

### 2.1 Continuum Lagrangian

In \(d\) space‑time dimensions the action is

\[
S[\phi]=\int d^dx\;
\Bigl[\tfrac12(\partial_\mu\phi)(\partial^\mu\phi)-V(\phi)\Bigr],
\qquad
V(\phi)=\begin{cases}
0,&|\,\phi|<1,\\
\infty,&|\,\phi|\ge 1 .
\end{cases}
\tag{1}
\]

Because \(V\) is infinite outside the interval, the functional integral (or the canonical Hilbert space) contains **only those field configurations that satisfy**

\[
|\,\phi(x)|<1\quad\text{for every }x .
\tag{2}
\]

Thus the theory is nothing but a *free* scalar field **with a hard bound on its amplitude**.  
In the language of sigma‑models the target space is the **closed interval** \([-1,1]\) (or the open interval if we keep the walls strictly at \(\pm1\)).  

### 2.2 Lattice regularisation

Put the theory on a hypercubic lattice of spacing \(\varepsilon\) (for simplicity a 1‑dimensional chain, the generalisation being straightforward).  
At each site \(n\) we have a quantum‑mechanical coordinate \(\phi_n\).  
The canonical Hamiltonian reads

\[
H=\frac1N\sum_{n=1}^{N}
\Bigl[
-\frac12\frac{\partial^{2}}{\partial\phi_n^{2}}
+\frac12\frac{(\phi_n-\phi_{n-1})^{2}}{\varepsilon^{2}}
+V(\phi_n)
\Bigr],
\qquad
V(\phi_n)=\begin{cases}
0,&|\phi_n|<1,\\[2pt]
\infty,&\text{otherwise}.
\end{cases}
\tag{3}
\]

The factor \(1/N\) in front of the sum is just a convenient overall normalisation; it does **not** affect the eigenfunctions.

--------------------------------------------------------------------

## 3. Diagonalising the quadratic (kinetic) part

If we *ignore* the infinite walls for a moment, the Hamiltonian is a set of **coupled harmonic oscillators**.  
Introduce discrete Fourier modes (normal‑mode coordinates)

\[
\phi_n=\frac{1}{\sqrt N}\sum_{k}\;e^{ikn\varepsilon}\,q_k,
\qquad
k=\frac{2\pi}{N\varepsilon}m,\;m=0,\dots ,N-1 .
\tag{4}
\]

The gradient term becomes diagonal:

\[
\frac12\sum_{n}\frac{(\phi_n-\phi_{n-1})^{2}}{\varepsilon^{2}}
=
\frac12\sum_{k}\omega_k^{2}\,q_k^{2},
\qquad
\omega_k^{2}= \frac{4}{\varepsilon^{2}}\sin^{2}\!\Bigl(\frac{k\varepsilon}{2}\Bigr).
\tag{5}
\]

The kinetic term (the second derivative with respect to \(\phi_n\)) also diagonalises:

\[
-\frac12\sum_{n}\frac{\partial^{2}}{\partial\phi_n^{2}}
=-\frac12\sum_{k}\frac{\partial^{2}}{\partial q_k^{2}} .
\tag{6}
\]

Hence, *without* the wall, the Hamiltonian splits into a sum of independent one‑dimensional particles:

\[
H_{\text{free}}=\sum_{k}\Bigl[
-\frac12\frac{\partial^{2}}{\partial q_k^{2}}
+\frac12\omega_k^{2}q_k^{2}
\Bigr].
\tag{7}
\]

The exact eigenfunctions are products of harmonic‑oscillator wavefunctions,
\(\displaystyle \Psi_{\{n_k\}}^{\text{free}}(q)=\prod_k\psi_{n_k}(q_k)\).

--------------------------------------------------------------------

## 4. Effect of the hard walls

The infinite potential (2) does **not** act on the normal‑mode variables separately; it is a *constraint* that couples *all* modes:

\[
|\,\phi_n|<1\;\;\Longleftrightarrow\;\;
\Bigl|\frac{1}{\sqrt N}\sum_{k}e^{ikn\varepsilon}q_k\Bigr|<1
\quad\forall n .
\tag{8}
\]

Thus the Hilbert space is the subspace of the free‑oscillator Hilbert space consisting of wavefunctions that **vanish** whenever any of the linear combinations (8) reaches \(\pm1\).

Consequences:

* The Hamiltonian **remains** the sum (7); the only change is the **domain** of the wavefunctions.
* The eigenfunctions are **not** products of the 1‑D box eigenfunctions \(\sin(\pi\phi_n/2)\) that the student guessed, because the coupling term mixes the sites.
* The problem is equivalent to a **free field with a compact target space**; it belongs to the class of *non‑linear sigma models* with target \([-1,1]\).

--------------------------------------------------------------------

## 5. Ground‑state wave functional

### 5.1 General form

For a free scalar field (no walls) the exact ground‑state functional is the Gaussian

\[
\boxed{
\Psi_{0}^{\text{free}}[\phi]=\mathcal N\;
\exp\!\Bigl[
-\frac12\!\int\!\! d^{d-1}x\,d^{d-1}y\;
\phi(\mathbf{x})\,K(\mathbf{x}-\mathbf{y})\,\phi(\mathbf{y})
\Bigr]
}
\tag{9}
\]

with kernel \(K\) equal to the square root of the Laplacian (in momentum space \(K(p)=|p|\)).  

### 5.2 Imposing the box constraint

Because the Hamiltonian does not change, the only effect of the walls is to **restrict** the support of the functional to the region

\[
\mathcal R=\bigl\{\phi(\mathbf{x})\;\big|\;|\phi(\mathbf{x})|<1\;\forall\mathbf{x}\bigr\}.
\]

Hence the exact ground state of the **square‑well theory** is

\[
\boxed{
\Psi_{0}[\phi]=
\begin{cases}
\displaystyle
\mathcal N\;
\exp\!\Bigl[
-\frac12\!\int\! d^{d-1}x\,d^{d-1}y\;
\phi(\mathbf{x})\,K(\mathbf{x}-\mathbf{y})\,\phi(\mathbf{y})
\Bigr],
& \phi\in\mathcal R,\\[12pt]
0, & \text{otherwise}.
\end{cases}
}
\tag{10}
\]

In words: **the same Gaussian as for the free field, but truncated to the hyper‑cube \(|\phi|<1\) at every point**.  

The normalisation constant \(\mathcal N\) is fixed by

\[
\int_{\mathcal R}\!{\cal D}\phi\;|\Psi_{0}[\phi]|^{2}=1 .
\]

Because the truncation removes only a *tiny* part of the infinite‑dimensional Gaussian measure (for a weakly fluctuating field), \(\mathcal N\) differs from the free‑field normalisation only by an exponentially small factor in the volume.

### 5.3 Why the product ansatz fails

The trial functional proposed in the question,

\[
\Psi_{\text{trial}}[\phi]=\prod_{n}\cos\!\Bigl(\tfrac{\pi}{2}\phi_n\Bigr),
\tag{11}
\]

has **no dependence** on the gradient term \((\phi_n-\phi_{n-1})^{2}\).  
Acting with the Hamiltonian (3) on (11) produces a non‑vanishing contribution from the gradient piece, because the derivative with respect to \(\phi_n\) brings down a factor \(\tan(\frac{\pi}{2}\phi_n)\) that is *not* cancelled by any term in the wavefunction.  
Consequently (11) is **not** an eigenstate

*Original question: [Field theory based on square-well potential?](https://physics.stackexchange.com/questions/823324/field-theory-based-on-square-well-potential) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
