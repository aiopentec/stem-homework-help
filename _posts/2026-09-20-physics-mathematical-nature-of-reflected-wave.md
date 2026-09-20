---
layout: question
title: Mathematical Nature of Reflected wave
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Mathematical Nature of Reflected wave'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

A thin string is made of two different materials that meet at a point (the *junction*).  
A travelling wave of the form  

\[
y_i(x,t)=A_i\cos (k_1x-\omega t)    \qquad (x<0)
\]

is sent from the left toward the junction.  
When the wave reaches the junction part of it is reflected back into the left‑hand string and part is transmitted into the right‑hand string.  

The student obtained the familiar expressions for the reflected and transmitted amplitudes **by assuming** that the reflected and transmitted waves are also sinusoids.  

The question is:

* Is it legitimate to assume that the reflected and transmitted waves are sinusoidal when the incident wave is sinusoidal?  
* If so, why?  
* Can we give a rigorous (mathematical/physical) proof of this fact?

---

## 2. Full derivation and justification  

### 2.1. Wave equation for a stretched string  

For a uniform string under tension \(T\) with linear mass density \(\mu\) the transverse displacement \(y(x,t)\) obeys  

\[
\frac{\partial^{2}y}{\partial t^{2}} = v^{2}\frac{\partial^{2}y}{\partial x^{2}},\qquad 
v=\sqrt{\frac{T}{\mu}} .
\]

The general solution is any *superposition* of forward‑ and backward‑traveling waves:

\[
y(x,t)=f(x-vt)+g(x+vt).
\]

Because the equation is **linear and homogeneous**, if \(f\) and \(g\) are solutions, any linear combination of them is also a solution.

---

### 2.2. Sinusoidal (harmonic) solutions  

A single‑frequency sinusoid  

\[
y(x,t)=A\cos (kx-\omega t) \quad\text{with}\quad \omega = v k
\]

is a particular solution of the wave equation.  
Because of linearity, any **linear combination** (including an integral) of such sinusoids is also a solution. This is the basis of Fourier analysis: an arbitrary waveform can be written as a sum (or integral) of sinusoidal components.

Consequences:

* If the *incident* wave is a single sinusoid, the **boundary conditions** at the junction are linear equations. Their solution will be a linear combination of the same sinusoid on each side of the junction.  
* If the incident wave were a more complicated shape, we could decompose it into sinusoids, treat each frequency separately, and then recombine the results.  

Thus, **for a single‑frequency incident wave, the reflected and transmitted waves must also be sinusoids of the same frequency**. The only quantities that can change are the amplitudes (and possibly a phase shift).

---

### 2.3. Boundary conditions at the junction  

Let the junction be at \(x=0\).  
String‑1 (left side, \(x<0\)) has linear density \(\mu_1\) → wave speed \(v_1=\sqrt{T/\mu_1}\) and mechanical impedance  

\[
Z_1 = \mu_1 v_1 = \sqrt{T\mu_1}.
\]

String‑2 (right side, \(x>0\)) has \(\mu_2,\;v_2,\;Z_2=\sqrt{T\mu_2}\).

Because the string is continuous and the tension is the same on both sides, the following **two** conditions must hold at all times:

1. **Continuity of displacement** (the string cannot break):  

   \[
   y_1(0,t)=y_2(0,t).
   \tag{1}
   \]

2. **Continuity of transverse force** (the net vertical force on the junction must be zero).  
   The vertical component of the tension is \(T\,\partial y/\partial x\). Hence  

   \[
   T\frac{\partial y_1}{\partial x}\Big|_{x=0}=T\frac{\partial y_2}{\partial x}\Big|_{x=0}
   \;\;\Longrightarrow\;\;
   \frac{\partial y_1}{\partial x}(0,t)=\frac{\partial y_2}{\partial x}(0,t).
   \tag{2}
   \]

---

### 2.4. Write the three waves  

Incident wave (travelling to the right, on the left string):

\[
y_i(x,t)=A_i\cos(k_1x-\omega t),\qquad k_1=\frac{\omega}{v_1}.
\]

Reflected wave (travelling to the left, also on the left string):

\[
y_r(x,t)=A_r\cos(k_1x+\omega t+\phi_r)
\]
or, more conveniently, using complex notation,  

\[
y_r(x,t)=\Re\{A_r e^{i(k_1x+\omega t)}\}.
\]

Transmitted wave (travelling to the right on the right string):

\[
y_t(x,t)=A_t\cos(k_2x-\omega t+\phi_t),\qquad k_2=\frac{\omega}{v_2}.
\]

Because the equations are linear, we can treat the complex amplitudes and drop the real‑part symbols until the end.  Define

\[
\begin{aligned}
y_1(x,t) &= A_i e^{i(k_1x-\omega t)} + A_r e^{i(-k_1x-\omega t)} ,\qquad (x<0)\\[4pt]
y_2(x,t) &= A_t e^{i(k_2x-\omega t)} ,\qquad\qquad\;\;(x>0).
\end{aligned}
\]

(Note: the reflected term uses \(-k_1x\) because it travels in the \(-x\) direction.)

---

### 2.5. Apply the boundary conditions  

#### 2.5.1. Displacement continuity (1)

At \(x=0\):

\[
A_i e^{-i\omega t}+A_r e^{-i\omega t}=A_t e^{-i\omega t}
\;\Longrightarrow\;
A_i + A_r = A_t .
\tag{3}
\]

#### 2.5.2. Slope (force) continuity (2)

First compute the spatial derivative of each region:

\[
\begin{aligned}
\frac{\partial y_1}{\partial x} &= i k_1\bigl(A_i e^{i(k_1x-\omega t)} - A_r e^{i(-k_1x-\omega t)}\bigr),\\[4pt]
\frac{\partial y_2}{\partial x} &= i k_2 A_t e^{i(k_2x-\omega t)} .
\end{aligned}
\]

Set \(x=0\) :

\[
i k_1 (A_i - A_r)= i k_2 A_t .
\]

Cancel the common factor \(i\):

\[
k_1 (A_i - A_r)= k_2 A_t .
\tag{4}
\]

---

### 2.6. Solve for the unknown amplitudes  

From (3) we have \(A_t = A_i + A_r\). Insert this into (4):

\[
k_1 (A_i - A_r)= k_2 (A_i + A_r).
\]

Collect terms of \(A_i\) and \(A_r\):

\[
k_1 A_i - k_1 A_r = k_2 A_i + k_2 A_r
\;\Longrightarrow\;
(k_1 - k_2)A_i = (k_1 + k_2)A_r .
\]

Hence the **reflection coefficient** (ratio of reflected to incident amplitude) is  

\[
\boxed{\,\displaystyle
\frac{A_r}{A_i}= \frac{k_1 - k_2}{k_1 + k_2}\, } .
\tag{5}
\]

Similarly, using \(A_t = A_i + A_r\),

\[
\boxed{\,\displaystyle
\frac{A_t}{A_i}= \frac{2k_1}{k_1 + k_2}\, } .
\tag{6}
\]

It is often more convenient to express the result in terms of the **mechanical impedances**  

\[
Z_j = \mu_j v_j = \frac{T}{v_j}= \frac{T k_j}{\omega},
\]
so that \(k_j = \omega Z_j / T\). Substituting into (5)–(6) gives the classic forms

\[
\boxed{\,\displaystyle
\frac{A_r}{A_i}= \frac{Z_2-Z_1}{Z_2+Z_1}},\qquad
\boxed{\,\displaystyle
\frac{A_t}{A_i}= \frac{2 Z_2}{Z_2+Z_1}} .
\]

These coefficients are *pure numbers* (possibly negative, indicating a phase reversal) and they do **not** depend on the spatial coordinate or time—only on the properties of the two strings.

---

### 2.7. Why the reflected and transmitted waves are sinusoidal  

* **Linearity** – The wave equation and the boundary conditions are linear.  
* **Single‑frequency driving** – The incident wave contains only one angular frequency \(\omega\). The boundary conditions are linear algebraic equations in the complex amplitudes at that same \(\omega\). Consequently the solution for each region must also oscillate at \(\omega\); otherwise the equations could not be satisfied for all times.  

In other words, the system cannot generate new frequencies because there is nothing (e.g., a nonlinear term) that mixes different time scales. The only possible change is in amplitude and phase.

* **Fourier perspective** – Any arbitrary incident shape can be expanded as a superposition of sinusoids (Fourier integral). Because each sinusoidal component is reflected and transmitted independently with the coefficients (5)–(6), the total reflected (or transmitted) wave is the **same superposition** of sinusoids. Therefore the sinusoidal nature of each component is preserved.

Thus the assumption that the reflected and transmitted waves are sinusoidal is *exact* for a sinusoidal incident wave, and it follows directly from the linearity of the governing equations.

---

## 3. Final answer  

*For a single‑frequency incident wave on a junction of two strings, the reflected and transmitted waves are necessarily sinusoidal with the same frequency. Their amplitudes are given by*

\[
\boxed{\displaystyle 
\frac{A_r}{A_i}= \frac{k_1 - k_2}{k_1 + k_2}
      = \frac{Z_2 - Z_1}{Z_2 + Z_1}},
\qquad
\boxed{\displaystyle 
\frac{A_t}{A_i}= \frac{2k_1}{k_1 + k_2}
      = \frac{2 Z_2}{Z_2 + Z_1}} .
\]

*The justification rests on the linearity of the wave equation and the linear boundary conditions; a sinusoidal input cannot produce any other frequencies, only different amplitudes (and possibly a phase reversal).*  

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the reflected wave has a different frequency** | The boundary conditions contain no time‑derivatives that could change \(\omega\); a linear system cannot generate new frequencies. | Write the boundary equations explicitly and see that they must hold for *all* \(t\); this forces the same \(\omega\). |
| **Using the same wavenumber \(k\) on both sides** | The two strings have different wave speeds, so \(k_1=\omega/v_1\) and \(k_2=\omega/v_2\) are generally unequal. | Keep \(k_1\) and \(k_2\) distinct throughout the algebra; only after solving may you express the result in terms of impedances. |
| **Dropping the phase of the reflected wave** | A negative reflection coefficient means the reflected wave is **π** out of phase with the incident wave. Ignoring the sign loses this information. | Keep complex amplitudes (or explicitly write a phase factor) until the final step; then translate a negative amplitude into a phase shift of \(\pi\). |
| **Treating the tension \(T\) as different on the two strings** | The problem statement usually assumes the same tension (the strings are tied together). Changing \(T\) would also change the boundary condition for force. | State the assumption \(T\) constant; if tension differs, you must include it in the force‑continuity condition. |
| **Confusing impedance \(Z=\mu v\) with wave speed \(v\)** | Impedance depends on both mass density and tension; mixing them leads to algebra errors. | Write both definitions: \(v=\sqrt{T/\mu}\) and \(Z=\mu v\). Use whichever form simplifies the algebra. |

---

*Original question: [Mathematical Nature of Reflected wave](https://physics.stackexchange.com/questions/876194/mathematical-nature-of-reflected-wave) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
