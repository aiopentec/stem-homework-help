---
layout: question
title: Derivation of Planck&#39;s radiation law, Planck&#39;s quantum theory
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Derivation of Planck&#39;s radiation
  law, Planck&#39;s quantum theory'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (plain language)

A student has seen the standard derivation of **Planck’s radiation law**:

1. The walls of a cavity are modelled as a collection of **harmonic oscillators** (the “atoms” of the wall).  
2. For a wall‑oscillator of frequency ν the **average energy** in thermal equilibrium at temperature T is  

\[
\langle E\rangle_{\text{wall}}(\nu)=\frac{h\nu}{\displaystyle e^{\,h\nu/(kT)}-1}.
\]

3. The number of **electromagnetic eigenmodes** of the cavity whose frequencies lie between ν and ν+dν is  

\[
g(\nu)\,d\nu = 8\pi\frac{V}{c^{3}}\nu^{2}\,d\nu .
\]

Textbooks obtain the spectral energy density of the radiation by multiplying the two quantities:

\[
u(\nu)\,d\nu = g(\nu)\,\langle E\rangle_{\text{wall}}(\nu)\,d\nu .
\]

The student is puzzled: why should we use the *average energy of a wall‑oscillator*? Shouldn’t we instead use the *average energy of a cavity mode*? In other words, **does a wall‑oscillator have the same average energy as a field mode, and if so, why?**  

We have to show, step by step, that in thermal equilibrium the two averages are indeed identical, and that the multiplication above is therefore justified.

---

## 2.  Detailed derivation

### 2.1  Electromagnetic modes of a cavity are harmonic oscillators  

Inside a perfectly conducting cavity the electric and magnetic fields satisfy Maxwell’s equations with the boundary condition that the tangential component of **E** vanishes at the walls.  

The solutions are standing waves (normal modes) characterized by a wave‑vector **k** and a frequency  

\[
\omega = 2\pi\nu = c|\mathbf{k}|.
\]

For each allowed **k** there are **two independent polarizations**.  

If we write the vector potential of a given mode as  

\[
\mathbf{A}_{\mathbf{k},\lambda}(t)=\mathbf{e}_{\mathbf{k},\lambda}\,q_{\mathbf{k},\lambda}(t),
\]

the Lagrangian of the electromagnetic field reduces to a sum of independent terms

\[
L = \frac{1}{2}\sum_{\mathbf{k},\lambda}
\Bigl(\dot q_{\mathbf{k},\lambda}^{\,2}-\omega^{2}q_{\mathbf{k},\lambda}^{\,2}\Bigr).
\]

Thus **each mode behaves exactly like a one‑dimensional harmonic oscillator of frequency ν** (the two polarizations just give a factor 2 later).

Consequently, when the cavity is in thermal equilibrium, each mode must have the same statistical properties as a quantum harmonic oscillator of the same frequency.

---

### 2.2  Quantisation of the mode energy  

In quantum theory the energy of a single mode (one polarization) is

\[
E_{n}= \bigl(n+\tfrac12\bigr)h\nu,\qquad n=0,1,2,\dots
\]

(we will drop the zero‑point term \( \frac12 h\nu\) because it does not affect the energy exchange with the walls; the Planck law concerns *excess* energy over the ground state).

The **canonical partition function** for a single mode is therefore

\[
Z_{\text{mode}}=\sum_{n=0}^{\infty}e^{-n h\nu/kT}
   =\frac{1}{1-e^{-h\nu/kT}} .
\]

The mean energy (excluding the zero‑point term) follows from

\[
\langle E\rangle_{\text{mode}}
   = -\frac{\partial}{\partial\beta}\ln Z_{\text{mode}}
   =\frac{h\nu}{e^{h\nu/kT}-1},
\qquad\beta\equiv\frac{1}{kT}.
\]

**Exactly the same expression** is obtained for a wall‑oscillator because we assumed that the wall atoms are also harmonic oscillators with the *same* frequency‑energy relation \(E_{n}=nh\nu\).  

Hence **the average energy of a wall oscillator and the average energy of a cavity mode of the same frequency are identical**:

\[
\boxed{\;\langle E\rangle_{\text{wall}}(\nu)=\langle E\rangle_{\text{mode}}(\nu)=\frac{h\nu}{e^{h\nu/kT}-1}\;}
\]

---

### 2.3  Why the equality must hold in equilibrium  

Even if one did not invoke the explicit quantum calculation above, the equality follows from the **principle of detailed balance**:

* The wall oscillators and the electromagnetic modes exchange energy through emission and absorption of photons.  
* In thermal equilibrium the net energy flow between any particular wall oscillator and any particular field mode must be zero.  
* If the average energy of the wall oscillator were different from that of the mode, the rates of absorption and stimulated emission would not balance, contradicting equilibrium.

Therefore the only possible stationary distribution is the one that gives the same mean energy to every degree of freedom that shares the same frequency — which is exactly the Planck distribution derived for a quantum harmonic oscillator.

---

### 2.4  Counting the modes  

The number of *independent* standing‑wave modes with frequencies in \([\nu,\nu+d\nu]\) in a volume \(V\) is obtained by counting the integer lattice points in **k‑space**:

\[
\text{Number of wave‑vectors} = \frac{V}{(2\pi)^3} 4\pi k^{2} dk,
\qquad k = \frac{2\pi\nu}{c},\; dk = \frac{2\pi}{c}\,d\nu .
\]

Multiplying by the two possible polarizations gives

\[
g(\nu)\,d\nu 
   = 2 \times \frac{V}{(2\pi)^3} 4\pi \Bigl(\frac{2\pi\nu}{c}\Bigr)^{2}
      \frac{2\pi}{c}\,d\nu
   = 8\pi\frac{V}{c^{3}}\nu^{2}\,d\nu .
\]

Thus \(g(\nu)d\nu\) is the **total number of independent electromagnetic degrees of freedom** (modes) in the interval \([\nu,\nu+d\nu]\).

---

### 2.5  Energy density of the radiation field  

Since each mode carries on average \(\langle E\rangle_{\text{mode}}(\nu)\) of energy, the total energy contained in all modes between \(\nu\) and \(\nu+d\nu\) is simply

\[
U(\nu)\,d\nu = g(\nu)\,\langle E\rangle_{\text{mode}}(\nu)\,d\nu .
\]

Dividing by the cavity volume \(V\) yields the **spectral energy density** (energy per unit volume per unit frequency):

\[
\boxed{
u(\nu)=\frac{U(\nu)}{V}
      =\frac{8\pi\nu^{2}}{c^{3}}\,
        \frac{h\nu}{e^{h\nu/kT}-1}
      } .
\]

This is the *Planck radiation law* in its familiar form.

---

## 3.  Final answer

*In thermal equilibrium the wall atoms (modelled as harmonic oscillators) and the electromagnetic cavity modes are **identical statistical systems**: each is a quantum harmonic oscillator of the same frequency \(\nu\). Consequently they have the same mean energy,*

\[
\langle E\rangle(\nu)=\frac{h\nu}{e^{h\nu/kT}-1}.
\]

*Multiplying this average energy by the number of independent modes \(g(\nu)\,d\nu = 8\pi V\nu^{2}c^{-3}\,d\nu\) gives the total energy stored in the radiation field in the frequency interval \([\nu,\nu+d\nu]\). Dividing by the volume produces the Planck spectral energy density*

\[
u(\nu)=\frac{8\pi\nu^{2}}{c^{3}}\,
        \frac{h\nu}{e^{h\nu/kT}-1}.
\]

Thus the step of using the wall‑oscillator average energy is justified because **the average energy of a wall oscillator equals the average energy of a cavity mode at the same frequency**.

---

## 4.  Common mistakes

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing “mode energy” with “photon energy”** and writing \( \langle E\rangle = h\nu \). | The average energy is *not* the energy of a single photon; it is the statistical mean over many possible occupation numbers (0, 1, 2, …). | Remember the Planck factor \(1/(e^{h\nu/kT}-1)\) comes from the Bose‑Einstein distribution for a harmonic oscillator. |
| **Multiplying \(g(\nu)\) by \(kT\) (classical equipartition) instead of \(\langle E\rangle\).** | Classical equipartition fails at high frequencies (\(h\nu \gtrsim kT\)) and leads to the ultraviolet catastrophe. | Use the quantum expression for \(\langle E\rangle\); it reduces to \(kT\) only when \(h\nu\ll kT\). |
| **Neglecting the factor of 2 for the two polarizations** when deriving \(g(\nu)\). | Forgetting this gives a spectral density that is too low by a factor of two. | Explicitly count both transverse polarizations when counting modes in k‑space. |
| **Assuming the walls do not affect the field** and therefore using a different temperature for the oscillators. | In equilibrium the walls and the field must share the same temperature; otherwise detailed balance is violated. | State clearly that the whole cavity (walls + field) is at a uniform temperature T. |
| **Dropping the zero‑point term \( \frac12 h\nu \) without justification.** | The zero‑point energy does not exchange with the walls, but it must be mentioned to avoid confusion. | Explain that it cancels out when computing energy *differences* or when only the *excess* energy is relevant. |

Keeping these points in mind will prevent the most frequent conceptual and algebraic errors when deriving Planck’s law.

*Original question: [Derivation of Planck&#39;s radiation law, Planck&#39;s quantum theory](https://physics.stackexchange.com/questions/876741/derivation-of-plancks-radiation-law-plancks-quantum-theory) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
