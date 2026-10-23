---
layout: question
title: Ray Transfer Matrix and Gaussian Beams
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Ray Transfer Matrix and Gaussian Beams'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

### 1. Restatement of the Problem in Plain Language

In ray optics, standard geometric rays are tracked using a vector $\begin{pmatrix} x \\ \theta \end{pmatrix}$, where $x$ is the ray's transverse position and $\theta$ is its angle relative to the optical axis. When studying Gaussian laser beams, however, optics textbooks use a complex beam parameter $q$ and a vector proportional to $\begin{pmatrix} q \\ 1 \end{pmatrix}$. 

The student attempts to bypass the $q$-parameter formalism by directly substituting geometric properties of a Gaussian beam—specifically, the spot size $w(z)$ for position $x$, and the divergence angle $w(z)/R(z)$ for angle $\theta$—into the standard ray transfer matrix (ABCD) equations. When the student propagates this vector through an optical system and tries to reconstruct the beam's properties, they find that an extra term appears (proportional to $\lambda^2$) which does not match the exact transformation predicted by the standard $q$-parameter ABCD law (the Kogelnik relation). 

The goal is to explain **where the logic breaks down** when treating $x = w(z)$ and $\theta = w(z)/R(z)$ as a standard ray vector subjected to linear ABCD matrix multiplication.

---

### 2. Step-by-Step Analysis

#### Step A: Review the Standard Gaussian Beam $q$-Parameter Transformation
For a rotationally symmetric Gaussian beam, the complex beam parameter $q(z)$ is defined by:
$$\frac{1}{q(z)} = \frac{1}{R(z)} - i \frac{\lambda}{\pi n w(z)^2}$$

When passing through an optical system represented by the ABCD matrix:
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix}$$
The transformation of the $q$-parameter obeys the **bilinear transformation** (often called the ABCD law for Gaussian beams):
$$q_2 = \frac{A q_1 + B}{C q_1 + D}$$

Taking the inverse of both sides yields the relation the student used:
$$\frac{1}{q_2} = \frac{C + D\left(\frac{1}{q_1}\right)}{A + B\left(\frac{1}{q_1}\right)}$$

#### Step B: Analyze the Student's Vector Hypothesis
The student proposed treating a Gaussian beam like a bundle of geometric rays by defining a vector:
$$\mathbf{v}(z) = \begin{pmatrix} w(z) \\ \frac{w(z)}{R(z)} \end{pmatrix}$$

Applying the standard matrix multiplication rule:
$$\begin{pmatrix} w_2 \\ \frac{w_2}{R_2} \end{pmatrix} = \begin{pmatrix} A & B \\ C & D \end{pmatrix} \begin{pmatrix} w_1 \\ \frac{w_1}{R_1} \end{pmatrix}$$

This matrix equation yields two scalar equations:
1. $w_2 = A w_1 + B \frac{w_1}{R_1}$
2. $\frac{w_2}{R_2} = C w_1 + D \frac{w_1}{R_1}$

#### Step C: Exposing the Flaw in Linearity
Geometrical ray optics is fundamentally **linear**. If a ray starts at position $x_1$ with angle $\theta_1$, its final position $x_2$ and angle $\theta_2$ are linearly proportional to $x_1$ and $\theta_1$. If you scale the input ray height and angle by a factor $k$, the output height and angle scale by $k$ as well.

Now, let's look at the student's "ray" components for a Gaussian beam:
* Position-like component: $x = w(z)$
* Angle-like component: $\theta = \frac{w(z)}{R(z)}$

If we consider free-space propagation over a distance $d$, the ABCD matrix is:
$$\begin{pmatrix} A & B \\ C & D \end{pmatrix} = \begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix}$$

Using the exact equations for Gaussian beam propagation in free space, the spot size $w(z)$ and radius of curvature $R(z)$ evolve non-linearly with $z$:
$$w_2^2 = w_1^2 \left[ \left(1 + \frac{d}{R_1}\right)^2 + \left(\frac{z_{R}}{R_1}\text{ terms}\dots\right) \right]$$
Notice that $w_2$ depends on $w_1$ *non-linearly* (through quadratic terms of $w_1$ embedded in the diffraction equations and Rayleigh range $z_R = \frac{\pi n w_1^2}{\lambda}$). 

Because $w(z)$ and $R(z)$ are coupled through complex wave optics (specifically diffraction, which introduces $\lambda$ into the equations), **Gaussian beam parameters do not undergo linear superposition in the manner of geometric rays**. 

When the student forced the vector $\begin{pmatrix} w \\ w/R \end{pmatrix}$ to obey linear matrix multiplication, they assumed that $w_2$ is a linear function of $w_1$ and $w_1/R_1$. In reality, wave optics dictates that the beam width $w(z)$ scales with the square root of quadratic sums involving $w_1$, meaning the underlying transformation is homographic (linear fractional), not strictly linear. This is precisely why the complex parameter $q$ (which contains both $w$ and $R$ in its inverse) is required: the linearity applies to $q$ via the *fractional linear transformation* $\frac{Aq+B}{Cq+D}$, not to $w$ and $w/R$ independently via matrix multiplication on a real vector.

---

### 3. Final Answer

The student's logic fails because **geometric ray vectors $\begin{pmatrix} x \\ \theta \end{pmatrix}$ undergo linear transformations, whereas Gaussian beam parameters evolve via non-linear wave-optics diffraction effects.** 

Specifically:
1. $w(z)$ and $R(z)$ are coupled through diffraction (via the wavelength $\lambda$ and Rayleigh range), making their propagation non-linear with respect to $w_1$ and $R_1$.
2. Matrix multiplication $\begin{pmatrix} A & B \\ C & D \end{pmatrix}\begin{pmatrix} w \\ w/R \end{pmatrix}$ forces a purely linear superposition of beam sizes, which violates the actual physics of diffraction.
3. The correct linearity applies to the inverse complex beam parameter $\frac{1}{q}$ through a **bilinear (fractional linear) transformation**, not through direct matrix multiplication of $w$ and $w/R$. The stray $\lambda^2$ term appearing in the student's derivation is the mathematical artifact of forcing a wave phenomenon (diffraction) into a purely geometric, linear matrix framework.

---

### 4. Common Mistakes for This Problem Type

* **Confusing Ray Optics with Wave Optics:** Assuming that any parameter describing a light beam can be treated as a "ray" vector $\begin{pmatrix} x \\ \theta \end{pmatrix}$ and propagated with standard ABCD matrices.
* **Ignoring Diffraction Effects:** Forgetting that Gaussian beam expansion depends explicitly on wavelength $\lambda$ and the waist size $w_0$, which introduces non-linear squaring operations into the beam radius evolution.
* **Misinterpreting the ABCD Law:** Applying the ABCD matrix directly to real-valued beam dimensions ($w$ and $R$) instead of applying the fractional linear transformation to the complex $q$-parameter (or $\frac{1}{q}$).

*Original question: [Ray Transfer Matrix and Gaussian Beams](https://physics.stackexchange.com/questions/877160/ray-transfer-matrix-and-gaussian-beams) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
