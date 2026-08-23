---
layout: post
title: Where does the Berry phase of $\pi$ come from in a topological insulator?
author: StemFix Bot
category: physics
tags:
- physics
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What is being asked?  

A 3‑D time‑reversal‑invariant topological insulator (TI) is characterized by a **\(Z_{2}\) bulk invariant**  

\[
\nu=\frac{1}{2\pi}\Bigl[\;\underbrace{\oint_{\partial (A+B)}\!{\bf A}\cdot d{\bf k}}_{\text{line integral}}
      \;-\;\underbrace{\iint_{A+B}\!\! \bigl(\nabla_{\bf k}\times{\bf A}\bigr)\,d^{2}k}_{\text{Berry‑curvature flux}}\Bigr]\;\;{\rm mod}\;2 .
\tag{1}
\]

The student wonders why the **surface states** of a TI acquire a **Berry phase of \(\pi\)** when their momentum winds once around the Dirac point, and how this \(\pi\) shows up in the expression (1).  
In other words we must show that, for a non‑trivial TI (\(\nu=1\)),

\[
\boxed{\;\oint_{\cal C}{\bf A}\!\cdot d{\bf k}= \pi\;({\rm mod}\;2\pi)\;}
\tag{2}
\]

where \({\cal C}\) is any closed loop that encloses the surface Dirac point (or, equivalently, the boundary of the half‑Brillouin‑zone used in (1)).  

We shall do this **purely from the Berry connection/curvature** and the **time‑reversal symmetry** constraint, without invoking charge polarization or transport arguments.

---

## 2.  Detailed derivation  

### 2.1  Berry connection, curvature and the \(Z_{2}\) formula  

For a (single) occupied Bloch band \(n\)

\[
\boxed{{\bf A}_{n}({\bf k}) = i\langle u_{n}({\bf k})|\nabla_{\bf k}u_{n}({\bf k})\rangle},
\qquad
\boxed{\Omega_{n}({\bf k}) = \bigl(\nabla_{\bf k}\times{\bf A}_{n}({\bf k})\bigr)_z } .
\]

In a time‑reversal‑invariant (TRI) crystal the anti‑unitary operator \(\Theta\) satisfies  

\[
\Theta^{2}=-1\qquad (\text{spin‑}\tfrac12\;\text{electrons}) .
\]

Acting on a Bloch state we can write  

\[
|u_{n}(-{\bf k})\rangle = \sum_{m} w_{nm}({\bf k})\,\Theta |u_{m}({\bf k})\rangle ,\qquad 
w({\bf k})\in U(N_{\rm occ}) .
\tag{3}
\]

From (3) one obtains the **TR constraint on the Berry connection**

\[
{\bf A}(-{\bf k}) = -\,{\bf A}({\bf k}) + i\,w^{\dagger}({\bf k})\nabla_{\bf k} w({\bf k}) .
\tag{4}
\]

The second term is a pure gauge.  Consequently the **Berry curvature** is **odd**:

\[
\boxed{\Omega(-{\bf k}) = -\Omega({\bf k})}\ .
\tag{5}
\]

Hence the total Chern number of the whole Brillouin zone (BZ) vanishes,
\(\displaystyle \int_{\rm BZ}\Omega\,d^{2}k =0\).

### 2.2  Why we integrate only over *half* the BZ  

Because \(\Omega\) is odd, the integral over a *half* BZ, denoted \(A+B\) in Fig. 1 of Fu’s thesis, need **not** be zero.  The two halves are related by TR, but the **gauge choice on their common boundary** is constrained by (4).  This is precisely what makes the quantity (1) gauge‑invariant and integer‑valued (mod 2).

Define the **Wilson loop** (Berry phase) of the occupied subspace along the closed contour \(\partial(A+B)\),

\[
\gamma \equiv \oint_{\partial(A+B)} {\bf A}\!\cdot d{\bf k}\; .
\tag{6}
\]

Using Stokes’ theorem on a *simply‑connected* region would give \(\gamma = \int_{A+B}\Omega\).  However the region \(A+B\) is *not* a closed surface in the periodic BZ: its opposite edges are identified only after a **time‑reversal operation**.  Because of (4) the line integral on the two opposite edges does **not** cancel, and the difference  

\[
\gamma - \int_{A+B}\Omega = 2\pi\,C_{A+B}
\tag{7}
\]

is an **even multiple of \(2\pi\)**.  Therefore the expression in (1) reduces to

\[
\nu = \frac{\gamma}{\pi}\;\;{\rm mod}\;2 .
\tag{8}
\]

Thus **the \(Z_{2}\) invariant is nothing but the Berry phase (6) measured in units of \(\pi\)**.  
If \(\nu=1\) (non‑trivial TI) we must have \(\gamma = \pi\;({\rm mod}\;2\pi)\); if \(\nu=0\) then \(\gamma =0\;({\rm mod}\;2\pi)\).

### 2.3  Explicit calculation for the surface Dirac cone  

The low‑energy surface Hamiltonian of a strong TI is the massless Dirac model

\[
H({\bf k}) = v\bigl(k_{x}\sigma_{y} - k_{y}\sigma_{x}\bigr) ,
\qquad {\bf k}=(k_{x},k_{y}) .
\tag{9}
\]

Its (conduction‑band) eigenstate can be written as  

\[
|u_{+}({\bf k})\rangle = \frac{1}{\sqrt{2}}
\begin{pmatrix}
1\\[2pt]
e^{i\theta_{\bf k}}
\end{pmatrix},
\qquad 
\theta_{\bf k}= \arg(k_{x}+ik_{y}) .
\tag{10}
\]

Compute the Berry connection:

\[
\begin{aligned}
{\bf A}({\bf k}) &= i\langle u_{+}|\nabla_{\bf k}u_{+}\rangle
                 = i\frac{1}{2}\bigl(0,\,e^{-i\theta}\partial_{\bf k}e^{i\theta}\bigr) \\
                 &= -\frac{1}{2}\nabla_{\bf k}\theta_{\bf k} .
\end{aligned}
\tag{11}
\]

Take a circular path \({\cal C}\) of radius \(R\) that encloses the Dirac point once, parametrized by \(\theta\in[0,2\pi]\).  The line integral is

\[
\begin{aligned}
\gamma &\equiv \oint_{\cal C}{\bf A}\!\cdot d{\bf k}
       = -\frac12\oint_{\cal C}\nabla_{\bf k}\theta_{\bf k}\cdot d{\bf k}
       = -\frac12\Delta\theta_{\bf k} \\
       &= -\frac12\bigl(\theta(2\pi)-\theta(0)\bigr) 
       = -\frac12(2\pi)= -\pi .
\end{aligned}
\tag{12}
\]

Modulo \(2\pi\) this is **\(\boxed{\gamma = \pi}\)**.  The same result follows for the valence band (the sign flips, but the phase is still \(\pi\) modulo \(2\pi\)).

Thus a **single surface Dirac cone carries a Berry phase of \(\pi\)**.  

### 2.4  Linking the surface Berry phase to the bulk \(Z_{2}\) invariant  

From (8) we have  

\[
\nu = \frac{\gamma}{\pi}\;{\rm mod}\;2 .
\tag{13}
\]

For a **strong TI** the bulk invariant is \(\nu=1\).  Consequently the surface Wilson loop must satisfy \(\gamma=\pi\) (mod \(2\pi\)), exactly what we have just obtained from the explicit Dirac Hamiltonian.  

Conversely, if the surface were topologically trivial (\(\nu=0\)), the Berry phase around any closed loop would be \(0\) (or an even multiple of \(\pi\)); a Dirac point could be gapped out without breaking time‑reversal symmetry.  

Hence the **\(\pi\) Berry phase of the surface state is a direct manifestation of the bulk \(Z_{2}\) invariant** encoded in the half‑BZ integral (1).

---

## 3.  Final answer  

*The Berry phase \(\pi\) of a topological‑insulator surface state follows from the bulk \(Z_{2}\) invariant. The invariant can be written as*  

\[
\nu=\frac{1}{2\pi}\Bigl[\oint_{\partial (A+B)}{\bf A}\cdot d

*Original question: [Where does the Berry phase of $\pi$ come from in a topological insulator?](https://physics.stackexchange.com/questions/70361/where-does-the-berry-phase-of-pi-come-from-in-a-topological-insulator) on Physics Stack Exchange, licensed CC BY-SA.*
