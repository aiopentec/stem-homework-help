---
layout: question
title: 'Theoretical interpretation of CHSH correlation loss: Classical phase-space
  thermal noise vs. non-unitary decoherence'
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Theoretical interpretation of CHSH correlation
  loss: Classical phase-space thermal noise vs. non-unitary decoherence'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

A laboratory reports a CHSH Bell‑parameter  

\[
S = E_1+E_2+E_3-E_4 = 2.404 ,
\qquad 
\begin{aligned}
E_1 &=+0.556 ,\\
E_2 &=-0.672 ,\\
E_3 &=+0.592 ,\\
E_4 &=+0.584 .
\end{aligned}
\]

The value lies **between**  

* the **local‑realist bound** \(S\le 2\) and  
* the **Tsirelson bound** \(S\le 2\sqrt 2\approx 2.828\).

The student wants to know whether this *intermediate* value can be explained **only** by classical (thermal) noise acting on a deterministic phase‑space picture, **or** whether one must invoke *non‑unitary* open‑quantum‑system dynamics (e.g. dephasing, amplitude‑damping channels) to account for the loss of correlation.

In plain language:

> *Can a completely classical, deterministic model with thermal fluctuations produce a CHSH value of 2.404, or is some quantum‑mechanical decoherence inevitably required?*  

We shall answer this by examining what a classical hidden‑variable (HV) model can produce, how quantum noise reduces the Bell value, and why the reduction is fundamentally a quantum (non‑unitary) effect even if it can be expressed as “classical” random flips on the measurement outcomes.

---

## 2.  Step‑by‑step analysis  

### 2.1  Bell‑CHSH basics  

For two distant parties, Alice and Bob, each chooses one of two measurement settings  
\((a,a')\) for Alice and \((b,b')\) for Bob, obtaining outcomes \(\pm1\).  
The CHSH combination is  

\[
S = \langle A B\rangle + \langle A B'\rangle + \langle A' B\rangle - \langle A' B'\rangle .
\]

* **Local‑realist (LR) models** (any deterministic or stochastic HV theory respecting locality) obey  

\[
|S| \le 2 .
\]

* **Quantum mechanics** allows up to  

\[
|S| \le 2\sqrt 2 .
\]

* **No‑signalling** (the most general correlations consistent with relativity) permits  

\[
|S| \le 4 .
\]

Thus a value **larger than 2** *already* guarantees that the observed statistics cannot be reproduced by any **local deterministic phase‑space dynamics**—no amount of classical (thermal) noise can raise \(S\) above 2 if the underlying model is strictly local.

### 2.2  Classical phase‑space + thermal noise  

A deterministic phase‑space model (Liouville dynamics) assigns a definite hidden variable \(\lambda\) to every experimental run. The outcome functions are predetermined:

\[
A(a,\lambda)=\pm 1, \qquad B(b,\lambda)=\pm 1 .
\]

If we now add **thermal (or any) classical noise** *after* the deterministic outcome is produced, we can model it as a random bit‑flip with probability \(q\). For example,

\[
\tilde{A}= A\,\xi_A,\qquad \xi_A=\begin{cases}
+1 & \text{w.p. } 1-q\\
-1 & \text{w.p. } q
\end{cases}
\]

(and similarly for \(\tilde{B}\)).  
The observed correlator becomes

\[
\langle \tilde{A}\tilde{B}\rangle = (1-2q)^2 \langle A B\rangle .
\]

Hence the CHSH value scales as

\[
S_{\text{noisy}} = (1-2q)^2 S_{\text{ideal}} .
\]

Crucially, **\(S_{\text{ideal}}\) itself cannot exceed 2** for any LR model. Multiplying by any factor \((1-2q)^2\le 1\) never pushes the result above 2. Therefore a *purely classical* deterministic model, even with arbitrary thermal noise, can never reproduce \(S=2.404\).

> **Conclusion 1:**  A classical phase‑space picture (local hidden variables) can only give \(S\le 2\). Any observed value larger than 2 proves that the underlying correlations are **non‑local** (or that the model abandons locality).

### 2.3  Quantum source + noise (open‑system picture)  

Consider now a *quantum* source that would give the **maximal** violation if it were perfect: a singlet state \(|\psi^{-}\rangle\). With the optimal CHSH measurement settings, the ideal quantum value is  

\[
S_{\text{max}} = 2\sqrt2 .
\]

If the state (or the measurement) is affected by noise, the observed correlators are reduced. The most common noise models are:

| Noise model | Kraus operators | Effect on correlators |
|-------------|----------------|----------------------|
| **Depolarising channel** on each qubit: \(\rho\to p\rho+(1-p)\frac{\mathbb I}{2}\) | \(K_0=\sqrt{p}\,\mathbb I, \; K_{1..3}=\sqrt{\frac{1-p}{3}}\,\sigma_i\) | Correlators multiplied by \(p\) |
| **Phase‑damping (dephasing)** on each qubit: \(\rho\to p\rho+(1-p)Z\rho Z\) | \(K_0=\sqrt{p}\,\mathbb I,\; K_1=\sqrt{1-p}\,|0\rangle\langle0|,\;K_2=\sqrt{1-p}\,|1\rangle\langle1|\) | Correlators in the \(\sigma_x,\sigma_y\) plane multiplied by \(p\) |
| **Amplitude‑damping** (energy loss) | \(K_0=|0\rangle\langle0|+\sqrt{1-\gamma}\,|1\rangle\langle1|,\; K_1=\sqrt{\gamma}\,|0\rangle\langle1|\) | Asymmetric reduction of correlators; also changes local statistics |

All of these are **completely positive, trace‑preserving (CPTP)** maps—i.e. **non‑unitary** evolutions that arise from coupling the system to an environment (open‑system dynamics).  

For the simple case of *isotropic* depolarising noise on *both* qubits, the state becomes

\[
\rho_{\text{mix}} = p\,|\psi^{-}\rangle\!\langle\psi^{-}|+(1-p)\,\frac{\mathbb I}{4},
\qquad 0\le p\le1 .
\]

The CHSH value for this Werner‑type state is

\[
S = p\, 2\sqrt2 .
\]

Setting \(S=2.404\) gives the required visibility  

\[
p = \frac{S}{2\sqrt2}= \frac{2.404}{2.828}\approx 0.85 .
\]

Thus **85 % of a maximally entangled state plus 15 % white noise** reproduces the experimental number. The same number would be obtained if we first prepared the perfect singlet and then let each qubit undergo a phase‑damping channel with visibility \(p\approx0.85\).

### 2.4  Classical‑noise picture vs. quantum‑channel picture  

One can **re‑interpret** the effect of a quantum channel as *classical random flips* on the measurement outcomes *after* the ideal measurement has been performed. For the depolarising case:

* With probability \(p\) the outcomes are the ideal quantum ones (correlated as \(\pm1\)).
* With probability \(1-p\) the outcomes are completely random (uncorrelated).

Mathematically this is **exactly** the same statistical mixture we wrote in the previous table. Hence, from a *statistical‑mechanics* point of view, the loss of CHSH strength can be described by a **classical stochastic process** acting on the measurement results.

However, **the origin of that stochastic process is quantum**: it is the trace over environmental degrees of freedom (the “thermal bath”) that turns a pure unitary evolution of system + environment into a non‑unitary map on the system alone. In other words:

* **Pure deterministic phase‑space dynamics** → cannot generate \(S>2\).  
* **Quantum entanglement + coupling to a bath** → yields a *non‑unitary* CPTP map, which *can* reduce the Bell value to any number between 2 and \(2\sqrt2\).

Therefore, while the *final statistics* can be modelled by “classical thermal noise” applied to the measurement outcomes, **the existence of the Bell violation itself (the part above 2) fundamentally requires a quantum, non‑unitary open‑system description**.

### 2.5  Summary of the logical chain  

1. **Local deterministic HV + classical noise ⇒** \(S\le 2\).  
2. **Observed \(S=2.404>2\) ⇒** the data cannot be reproduced by any such classical model.  
3. **Quantum pure state (maximally entangled) ⇒** \(S=2\sqrt2\).  
4. **Introduce any CPTP noise channel (dephasing, depolarising, amplitude damping, etc.)** → the CHSH value is multiplied by a *visibility* factor \(V\le1\).  
5. For \(S=2.404\) we need \(V\approx0.85\). This is exactly the prediction of a standard open‑quantum‑system model (e.g., a depolarising channel with probability \(1-V=0.15\)).  
6. The same statistics could be mimicked by a *classical* random‑flip model **after** the quantum measurement, but that classical model is only an *effective* description; it cannot replace the underlying quantum dynamics that generated the violation in the first place.

---

## 3.  Final answer  

**No.** A deterministic classical phase‑space model, even when supplemented with thermal (Liouville/Langevin) noise, can never yield a CHSH value larger than the local bound of 2. The observed intermediate value \(S=2.404\) therefore *must* arise from genuine quantum correlations that have been partially degraded by **non‑unitary open‑system dynamics** (dephasing, depolarising, amplitude‑damping, etc.).  

Mathematically, the degradation can be expressed as a visibility factor \(V\) so that  

\[
S = V\; 2\sqrt2, \qquad V = \frac{2.404}{2\sqrt2}\approx0.85 .
\]

A quantum channel with visibility \(V\) (e.g. a depolarising channel with probability \(1-V\approx0.15\)) reproduces the data. The same statistical outcome could be re‑cast as classical random flips on the measurement results, but that is only an *effective* description; the essential source of the Bell violation—and its reduction—is quantum decoherence, not purely classical thermal noise.

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming any reduction of \(S\) can be explained by classical noise alone.** | Classical (local) models cannot produce \(S>2\) to begin with; they cannot “reduce” a quantum violation. |

*Original question: [Theoretical interpretation of CHSH correlation loss: Classical phase-space thermal noise vs. non-unitary decoherence](https://physics.stackexchange.com/questions/876464/theoretical-interpretation-of-chsh-correlation-loss-classical-phase-space-therm) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
