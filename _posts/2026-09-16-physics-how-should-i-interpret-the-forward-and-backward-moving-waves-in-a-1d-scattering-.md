---
layout: question
title: How should I interpret the forward- and backward-moving waves in a 1D scattering
  problem?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How should I interpret the forward- and
  backward-moving waves in a 1D scattering problem?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  Restating the question in plain language  

A student is studying the textbook treatment of a one‑dimensional step potential  

\[
V(x)=\begin{cases}
0,&x<0\\[2pt]
V_{0},&x>0\qquad (E>V_{0})
\end{cases}
\]

and sees the usual stationary‑state solutions  

\[
\psi_{I}(x)=Ae^{ik_{1}x}+Be^{-ik_{1}x},\qquad 
\psi_{II}(x)=Ce^{ik_{2}x}+De^{-ik_{2}x},
\]

with  

\[
k_{1}=\frac{\sqrt{2mE}}{\hbar},\qquad 
k_{2}=\frac{\sqrt{2m\,(E-V_{0})}}{\hbar}.
\]

Textbooks then **set \(D=0\)** and say that the particle is “incident from the left”, so that the term \(Ae^{ik_{1}x}\) is the incoming wave, \(Be^{-ik_{1}x}\) the reflected wave, and \(Ce^{ik_{2}x}\) the transmitted wave.

The student asks:

* Why is it legitimate to *assume* that the particle comes from the left?  
* Could we not also consider a particle coming from the right, or even particles coming from both sides?  
* What does it really mean that a reflected wave “appears” when the initial state was only a forward‑moving plane wave?  
* Is the scattering state a superposition that *already* contains reflected and transmitted pieces, or does the potential generate them during time evolution?

We need to give a complete, step‑by‑step answer that clarifies the physical meaning of the four exponential terms, the role of boundary conditions, and how to construct realistic scattering states from wave packets.

---

## 2.  Detailed answer  

### 2.1  Plane waves vs. wave packets  

A single exponential \(e^{ikx}\) (or \(e^{-ikx}\)) is **not** a normalisable quantum state; it extends over all space and carries a definite momentum \(p=\hbar k\). In scattering theory we use such *plane‑wave solutions* as a convenient basis because the Schrödinger equation is linear and translation invariant in each region.  

Physical particles, however, are described by **wave packets** – superpositions of many plane waves with a narrow distribution of momenta centred at some \(k_{0}\). A packet that is initially far on the left and moving to the right can be written as  

\[
\Psi(x,0)=\int\! dk\, a(k)\,e^{ikx},
\qquad a(k)\approx 0\;\text{unless }k\approx k_{0}>0 .
\]

Because the packet is localized, we can unambiguously say that it is *incoming from the left*.

When we let this packet evolve under the Hamiltonian with the step potential, each momentum component evolves according to the stationary solutions described above. The **linear superposition principle** then guarantees that the whole packet evolves into the superposition of the corresponding reflected and transmitted pieces. In the long‑time limit (after the packet has interacted with the step) the packet separates into two spatially distinct parts:

* a reflected packet moving to the left (built from the \(e^{-ik_{1}x}\) components),
* a transmitted packet moving to the right on the \(x>0\) side (built from the \(e^{+ik_{2}x}\) components).

Thus the reflected wave does **not** appear *out of nothing*; it is already present in the stationary solution as the coefficient \(B\) that multiplies the left‑moving basis function in region I. The *physical* reflected packet is obtained by integrating those coefficients over the momentum distribution of the incoming packet.

### 2.2  Stationary scattering states  

A **stationary scattering state** is a solution of the time‑independent Schrödinger equation that has a definite energy \(E\). It is written as a linear combination of the four exponential basis functions:

\[
\psi(x)=
\begin{cases}
Ae^{ik_{1}x}+Be^{-ik_{1}x}, & x<0,\\[4pt]
Ce^{ik_{2}x}+De^{-ik_{2}x}, & x>0 .
\end{cases}
\tag{1}
\]

Each term represents a plane wave of the *same* energy travelling either to the right (\(+\) exponent) or to the left (\(-\) exponent). The coefficients \(A,B,C,D\) are *not* independent; they are linked by the continuity conditions at the step:

\[
\psi_{I}(0)=\psi_{II}(0),\qquad 
\psi'_{I}(0)=\psi'_{II}(0).
\tag{2}
\]

These two equations reduce the four complex coefficients to **two independent parameters**. The remaining freedom is used to **choose the physical scattering situation** we want to study.

### 2.3  Choosing the incident direction  

Because the step potential is *asymmetric* (it changes at \(x=0\)), the physics of a particle coming from the left is **different** from that of a particle coming from the right. To describe a *specific* experiment we must specify:

1. **From which side the incoming particles originate?**  
2. **What is the flux (or amplitude) of the incoming beam?**  

Mathematically this is done by fixing **one of the coefficients** that multiplies an incoming wave.  

| Scenario | Incoming side | Coefficient that is fixed (convention) |
|----------|---------------|----------------------------------------|
| Particle incident from the left | \(x\to -\infty\) | Set \(A=1\) (or any non‑zero value) and require *no* incoming wave from the right, i.e. **\(D=0\)** |
| Particle incident from the right | \(x\to +\infty\) | Set \(D=1\) and require **\(B=0\)** |
| Particles incident from *both* sides | – | Both \(A\) and \(D\) may be non‑zero; then the solution contains two independent scattering channels. |

Why do we set \(D=0\) for a left‑incident beam?  
* In region II (\(x>0\)) the term \(De^{-ik_{2}x}\) describes a wave travelling **towards the left**, i.e. **originating at \(+\infty\)** and moving into the scattering region. If the experimental set‑up contains **no source** at \(+\infty\), this term must be absent. The same logic applies to the right‑incident case, where we set \(B=0\).

Thus the *assumption* “incident from the left” is not a mathematical necessity; it is a **boundary condition** that reflects the experimental configuration.

### 2.4  Solving for the coefficients  

Take the left‑incident case: \(A\) is chosen (conventionally \(A=1\)), \(D=0\). Apply (2):

\[
\begin{aligned}
\text{continuity of } \psi &: \; A + B = C,\\
\text{continuity of } \psi' &: \; ik_{1}(A - B)= ik_{2}C .
\end{aligned}
\]

Solve for \(B\) and \(C\):

\[
\boxed{
B = \frac{k_{1}-k_{2}}{k_{1}+k_{2}}\,A, \qquad
C = \frac{2k_{1}}{k_{1}+k_{2}}\,A } .
\]

The **reflection coefficient** (probability flux ratio) is  

\[
R = \Bigl|\frac{B}{A}\Bigr|^{2}= \Bigl(\frac{k_{1}-k_{2}}{k_{1}+k_{2}}\Bigr)^{2},
\]

and the **transmission coefficient**  

\[
T = \frac{k_{2}}{k_{1}}\Bigl|\frac{C}{A}\Bigr|^{2}= 
\frac{4k_{1}k_{2}}{(k_{1}+k_{2})^{2}},
\]

which satisfy \(R+T=1\) (conservation of probability current).

If instead we take a right‑incident beam (\(D\neq 0,\;B=0\)) we obtain the symmetric formulas with \(k_{1}\leftrightarrow k_{2}\).

### 2.5  Superposition of left‑ and right‑incident beams  

If the physical situation contains *incoming fluxes from both sides* (e.g. two sources at \(\pm\infty\) turned on simultaneously) the most general stationary solution is exactly (1) with **both** \(A\) and \(D\) non‑zero. The coefficients \(B\) and \(C\) are then linear functions of the two independent incoming amplitudes:

\[
\begin{pmatrix} B \\ C \end{pmatrix}
=
\mathbf{M}
\begin{pmatrix} A \\ D \end{pmatrix},
\qquad
\mathbf{M}=
\frac{1}{k_{1}+k_{2}}
\begin{pmatrix}
k_{1}-k_{2} & 2k_{2}\\[4pt]
2k_{1} & k_{2}-k_{1}
\end{pmatrix}.
\]

Each incoming component generates its own reflected and transmitted parts; the total wavefunction is simply the **linear superposition** of the two scattering channels.

### 2.6  Time‑dependent picture – “appearance” of the reflected wave  

Consider an initial wave packet \(\Psi(x,0)\) that is localized far to the left and moving right. Expand it in the stationary basis:

\[
\Psi(x,0)=\int\! dk\, a(k) \bigl[ e^{ikx}+R(k) e^{-ikx}\bigr] \quad (x<0) ,
\]

where \(R(k)=\frac{k_{1}(k)-k_{2}(k)}{k_{1}(k)+k_{2}(k)}\) is the reflection amplitude for each Fourier component.  

During the time evolution each component acquires a phase \(e^{-i\omega t}\). After the packet has interacted with the step, the part proportional to \(e^{-ikx}\) has moved **backwards**, forming the reflected packet. Hence the reflected wave *exists* at all times in the stationary solution, but it only becomes spatially separated from the incident packet after the scattering event.

In other words, the stationary solution already encodes the *outcome* of the scattering; the time‑dependent wave packet shows how the incident packet *splits* into the two outcomes as a result of the potential.

### 2.7  Summary of the physical picture  

| Concept | Mathematical representation | Physical meaning |
|---------|----------------------------|-------------------|
| **Incoming wave** (from left) | \(A e^{ik_{1}x}\) (region I) | Flux supplied by a source at \(x\to -\infty\). |
| **Reflected wave** | \(B e^{-ik_{1}x}\) (region I) | Flux that returns to the left after interacting with the step. |
| **Transmitted wave** | \(C e^{ik_{2}x}\) (region II) | Flux that continues to the right on the far side of the step. |
| **Incoming wave from right** | \(D e^{-ik_{2}x}\) (region II) | Flux supplied by a source at \(x\to +\infty\). |
| **Boundary condition** | Set the coefficient of the *unphysical* incoming wave on the side where no source exists to zero (e.g. \(D=0\) for left‑incident). | Implements the experimental configuration. |
| **Stationary scattering state** | Linear combination (1) with coefficients related by (2). | Describes a particle of definite energy *after* the scattering region has been reached, containing both incident and outgoing components. |
| **Realistic scattering experiment** | Superposition of many such stationary states weighted by a momentum distribution (wave packet). | Shows the dynamical splitting into reflected and transmitted packets. |

---

## 3.  Final answer  

1. **Why can we assume “incident from the left”?**  
   Because a scattering experiment is defined by where the particle source is placed. The potential itself does not create particles; we must impose a boundary condition that there is **no incoming flux from the side where no source exists**. Mathematically this is done by setting the coefficient of the left‑moving plane wave in region II (\(D\)) to zero.

2. **Can we have right‑incident or both‑sided incidence?**  
   Yes. For a right‑incident beam we set \(B=0\) and keep \(D\neq0\); for simultaneous beams from both sides both \(A\) and \(D\) are kept non‑zero and the solution is a superposition of the two scattering channels.

3. **What does “reflected wave appears” mean?**  
   The stationary solution already contains a term proportional to \(e^{-ik_{1}x}\); when a wave packet with only right‑moving components reaches the step, the potential mixes the plane‑wave components so that the packet’s time evolution acquires a left‑moving part. The reflected wave is therefore *generated* by the interaction, but it is already encoded in the stationary eigenfunction.

4. **Is the scattering state a pre‑existing superposition?**  
   Yes

*Original question: [How should I interpret the forward- and backward-moving waves in a 1D scattering problem?](https://physics.stackexchange.com/questions/876023/how-should-i-interpret-the-forward-and-backward-moving-waves-in-a-1d-scattering) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
