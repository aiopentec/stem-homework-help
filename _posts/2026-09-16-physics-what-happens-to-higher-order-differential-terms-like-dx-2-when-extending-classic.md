---
layout: question
title: What happens to higher-order differential terms like $(dx)^2$ when extending
  classical mechanics to a stochastic space-time trajectory?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: What happens to higher-order differential
  terms like $(dx)^2$ when extending classical mechanics to a stochastic space-time '
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking – in plain language  

* In ordinary (deterministic) calculus we write  

\[
dx = v\,dt ,\qquad (dx)^2 = v^{2}\,dt^{2}\;,
\]

and because \(dt\to 0\) the term \((dx)^2\) is *always* thrown away – it is “higher‑order”.

* If the trajectory of a particle is **not** a smooth curve but a wildly fluctuating one (the kind of path that appears in Brownian motion or in stochastic formulations of quantum mechanics), the increment \(dx\) behaves like the increment of a Wiener process \(dW\).  
  For a Wiener process  

\[
dW\sim\mathcal{N}(0,dt)\qquad\Longrightarrow\qquad dW=O(\sqrt{dt}),
\]

so that  

\[
(dW)^2 = O(dt)\neq 0 .
\]

* The student therefore asks:

  1. **Mathematically** – how does stochastic calculus (Itô calculus) treat the product \((dx)^2\) when the path is non‑smooth?  
  2. **Physically** – what does the presence of a non‑vanishing \((dx)^2\) imply for the notion of “velocity” of a quantum particle?

The answer will explain the Itô rule \((dW)^2 = dt\), show where it comes from, and interpret the result for quantum‑stochastic models (e.g., Nelson’s stochastic mechanics).

---

## 2.  Detailed solution  

### 2.1  Classical deterministic case (review)

If the trajectory \(x(t)\) is differentiable, we can write a Taylor expansion for a smooth function \(f(x,t)\):

\[
df = \frac{\partial f}{\partial t}\,dt+\frac{\partial f}{\partial x}\,dx
       +\frac12\frac{\partial^{2}f}{\partial x^{2}}\,(dx)^{2}+ \cdots .
\]

Because \(dx = \dot x\,dt\) and \(\dot x\) is finite, \((dx)^2 = \dot x^{\,2}dt^{2}\) is of order \(dt^{2}\) and vanishes faster than the linear term when we divide by \(dt\) and let \(dt\to0\). Hence we drop it and obtain the ordinary chain rule

\[
\frac{df}{dt}= \frac{\partial f}{\partial t}+ \frac{\partial f}{\partial x}\,\dot x .
\]

### 2.2  Brownian (Wiener) motion – why \((dx)^2\) is **not** negligible  

A *standard Wiener process* \(W(t)\) satisfies  

* \(W(0)=0\);  
* increments are independent;  
* \(W(t+dt)-W(t)\sim\mathcal N(0,dt)\).

Define the infinitesimal increment  

\[
dW \equiv W(t+dt)-W(t).
\]

From the Gaussian distribution we have  

\[
\mathbb{E}[dW]=0,\qquad \mathbb{E}[(dW)^{2}]=dt .
\]

Thus, *in the mean-square sense*  

\[
(dW)^{2}=dt\quad\text{(to leading order)}.
\]

This is the core of **Itô’s calculus**: the product of two infinitesimal Wiener increments is **first order** in \(dt\), not second order.  

The rigorous statement is  

\[
\boxed{(dW)^{2}=dt,\qquad dW\,dt=0,\qquad (dt)^{2}=0 } .
\]

The equalities are to be understood inside stochastic integrals; they are derived from the limit

\[
\sum_{k=0}^{n-1}(W_{t_{k+1}}-W_{t_{k}})^{2}
   \xrightarrow[n\to\infty]{} \int_{0}^{t} ds = t ,
\]

which is the **quadratic variation** of Brownian motion.

### 2.3  Itô’s Lemma – the stochastic analogue of the chain rule  

Let \(X(t)\) satisfy an Itô stochastic differential equation (SDE)

\[
dX = a(X,t)\,dt + b(X,t)\,dW .
\]

For a twice‑differentiable scalar function \(f(x,t)\) define \(Y(t)=f\bigl(X(t),t\bigr)\).  
Itô’s Lemma (proved by applying the Taylor expansion and using the rules above) gives

\[
\boxed{
\begin{aligned}
dY &=\frac{\partial f}{\partial t}\,dt
    +\frac{\partial f}{\partial x}\,dX
    +\frac12\frac{\partial^{2}f}{\partial x^{2}}\, (dX)^{2} \\[4pt]
    &=\Bigl[\,\frac{\partial f}{\partial t}
           +a\,\frac{\partial f}{\partial x}
           +\frac12 b^{2}\,\frac{\partial^{2}f}{\partial x^{2}} \Bigr]dt
      +b\,\frac{\partial f}{\partial x}\,dW .
\end{aligned}}
\]

The term \(\frac12 b^{2}\partial^{2}_{x}f\,dt\) **originates solely from** the replacement \((dW)^{2}=dt\).  
If the trajectory were smooth (\(b\equiv0\)) this term would disappear and we would recover the ordinary chain rule.

### 2.4  What does this mean for the “velocity” of a quantum particle?  

1. **No ordinary derivative.**  
   For a Brownian‑type path the limit  

   \[
   \lim_{dt\to0}\frac{x(t+dt)-x(t)}{dt}
   \]

   does **not exist** (it diverges like \(1/\sqrt{dt}\)). Hence a classical velocity \(v(t)=\dot x(t)\) is undefined.

2. **Forward and backward drifts.**  
   In stochastic mechanics (Nelson, 1966) one introduces *mean forward* and *mean backward* derivatives:

   \[
   D_{+}x(t)=\lim_{dt\downarrow0}\mathbb{E}\!\left[\frac{x(t+dt)-x(t)}{dt}\,\bigg|\,\mathcal F_t\right],
   \qquad
   D_{-}x(t)=\lim_{dt\uparrow0}\mathbb{E}\!\left[\frac{x(t)-x(t-dt)}{dt}\,\bigg|\,\mathcal F_t\right].
   \]

   These are finite and play the role of “velocity fields” (called **current velocity** \(v\) and **osmotic velocity** \(u\)). They are not instantaneous microscopic speeds but *statistical* averages over the random fluctuations.

3. **Physical interpretation of \((dx)^{2}=dt\).**  
   The non‑vanishing quadratic variation is the mathematical expression of the fact that the particle’s path is *nowhere differentiable*. In quantum‑stochastic models the diffusion coefficient is fixed by Planck’s constant:

   \[
   b = \sqrt{\frac{\hbar}{m}} \quad\Longrightarrow\quad
   (dx)^{2}=b^{2}\,dt = \frac{\hbar}{m}\,dt .
   \]

   Thus the stochastic term carries the quantum of action \(\hbar\); it is the source of the *uncertainty* that replaces a sharp velocity.

4. **Consequences for the Schrödinger equation.**  
   Starting from the SDE  

   \[
   dX = v\,dt + \sqrt{\frac{\hbar}{m}}\,dW ,
   \]

   and applying Itô’s Lemma to the *wave‑function amplitude* \(\psi(X,t)\), one recovers the Schrödinger equation (Nelson’s derivation). The extra term \(\frac12 b^{2}\partial_{x}^{2}\psi\,dt\) coming from \((dW)^{2}=dt\) is precisely the kinetic term \(-(\hbar^{2}/2m)\partial_{x}^{2}\psi\).

### 2.5  Summary of the mathematical answer  

| Situation | Increment size | Quadratic variation | Rule for \((dx)^{2}\) |
|-----------|----------------|---------------------|-----------------------|
| Smooth deterministic path \(x(t)\) | \(dx = v\,dt = O(dt)\) | \(\displaystyle\lim_{t\to0}\sum(dx)^{2}=0\) | \((dx)^{2}=0\) (higher‑order, discarded) |
| Wiener‑type stochastic path \(W(t)\) | \(dW = O(\sqrt{dt})\) | \(\displaystyle\lim_{n\to\infty}\sum_{k}(dW_{k})^{2}=t\) | \((dW)^{2}=dt\) (kept) |
| General Itô process \(dX = a\,dt + b\,dW\) | \(dX = O(dt) + O(\sqrt{dt})\) | \((dX)^{2}=b^{2}dt\) | \((dX)^{2}=b^{2}dt\) |

Thus, **in stochastic calculus \((dx)^{2}\) is *not* discarded; it is replaced by a term proportional to \(dt\)**, and that term is crucial for the dynamics.

---

## 3.  Final answer – concise statement  

* In ordinary calculus the square of an infinitesimal displacement is of order \(dt^{2}\) and is omitted.  
* For a trajectory that is a Wiener (Brownian) process, the increment scales as \(\sqrt{dt}\); consequently  

\[
(d x)^{2}= (b\,dW)^{2}=b^{2}\,dt ,
\]

where \(b\) is the diffusion coefficient (e.g., \(b=\sqrt{\hbar/m}\) in Nelson’s stochastic mechanics).  

* This rule, \((dW)^{2}=dt\), is the cornerstone of Itô calculus. It appears in Itô’s Lemma as an extra drift term \(\frac12 b^{2}\partial_{x}^{2}f\,dt\).  

* Physically, the non‑zero quadratic variation means the particle’s path is nowhere differentiable, so a classical instantaneous velocity does not exist. One can instead define **mean forward/backward drifts** (statistical velocities). The extra \((dx)^{2}\) term encodes the quantum diffusion that ultimately yields the Schrödinger equation.

---

## 4.  Common mistakes when tackling this type of problem  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating \(dx\) as a regular number** and writing \((dx)^{2}=0\) even for stochastic paths. | In Itô calculus \(dx\) denotes a random increment; its square is of order \(dt\), not \(dt^{2}\). | Remember the scaling: \(dW=O(\sqrt{dt})\) → \((dW)^{2}=O(dt)\). |
| **Confusing Itô and Stratonovich calculus** and using the wrong rule for \((dx)^{2}\). | Stratonovich integrals obey the ordinary chain rule, but the conversion adds a term \(\frac12 b^{2}\partial_{x}^{2}f\,dt\). | State clearly which interpretation you are using; for most quantum‑stochastic derivations Itô is standard. |
| **Assuming a well‑defined instantaneous velocity** for a Brownian path. | The limit \(\lim_{dt\to0}(x(t+dt)-x(t))/dt\) diverges; only mean drifts are finite. | Introduce forward/backward derivatives or the concept of *drift* instead of classical velocity. |
| **Dropping the \((dx)^{2}\) term in the Taylor expansion of a stochastic differential** because “it is higher order”. | The term is *first order* in \(dt\) for a stochastic increment, so it contributes to the dynamics. | Perform the expansion **including** the quadratic variation, then replace \((dW)^{2}\) by \(dt\). |
| **Neglecting the physical meaning of the diffusion coefficient** (e.g., setting \(b=1\) without justification). | In stochastic mechanics \(b\) is fixed by \(\hbar\) and the particle mass; arbitrary choice changes the physics. | Relate \(b\) to the quantum constants when interpreting the result. |

---

*Original question: [What happens to higher-order differential terms like $(dx)^2$ when extending classical mechanics to a stochastic space-time trajectory?](https://physics.stackexchange.com/questions/876046/what-happens-to-higher-order-differential-terms-like-dx2-when-extending-cla) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
