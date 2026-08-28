---
layout: question
title: Damped Oscillators types mathematical function
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Damped Oscillators types mathematical
  function'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the student is asking  

The student has three questions:

1. **Why does the textbook formula**  

   \[
   y(t)=y_0\,e^{-\delta t}\cos (\omega t)
   \]

   **only describe one kind of damping?**  

2. **What are the correct mathematical conditions for under‑, critical‑ and overdamping?** (The teacher said “critical damping when  δ = ω  and overdamping when δ > ω”, but the student’s simulations disagree.)  

3. **Why does a larger exponential decay constant δ sometimes make the motion slower (over‑damped case)?**  

Below we answer each point step‑by‑step, starting from the differential equation that governs a damped harmonic oscillator.

---

## 2.  Derivation from the equation of motion  

A mass‑spring system with a viscous damper obeys  

\[
m\ddot y + b\dot y + k y = 0,
\]

where  

* \(m\) = mass,  
* \(b\) = damping coefficient (units N·s m\(^{-1}\)),  
* \(k\) = spring constant.  

It is convenient to define two *angular frequencies*:

\[
\boxed{\omega_0 \equiv \sqrt{\frac{k}{m}}}\qquad\text{(undamped natural frequency)}
\]

\[
\boxed{\delta \equiv \frac{b}{2m}}\qquad\text{(damping constant, sometimes called “decay rate”)}.
\]

Dividing the whole equation by \(m\) gives the standard form  

\[
\ddot y + 2\delta \dot y + \omega_0^{\,2} y = 0. \tag{1}
\]

Equation (1) is a second‑order linear ODE with constant coefficients.  
Assume a solution of the form \(y(t)=e^{\lambda t}\). Substituting yields the **characteristic equation**

\[
\lambda^{2}+2\delta\lambda+\omega_0^{2}=0.
\]

Its roots are  

\[
\boxed{\lambda_{1,2}= -\delta \pm \sqrt{\delta^{2}-\omega_0^{2}} } .\tag{2}
\]

The nature of the square‑root term determines the type of damping.

---

## 3.  Three regimes and their explicit solutions  

| Regime | Condition on \(\delta\) and \(\omega_0\) | Roots \(\lambda_{1,2}\) | General solution \(y(t)\) | Behaviour |
|--------|------------------------------------------|------------------------|----------------------------|-----------|
| **Underdamped** | \(\displaystyle \delta < \omega_0\) | \(\lambda = -\delta \pm i\omega_D\) with \(\displaystyle\omega_D =\sqrt{\omega_0^{2}-\delta^{2}}\) (purely imaginary part) | \(\displaystyle y(t)=e^{-\delta t}\big(A\cos\omega_D t + B\sin\omega_D t\big)\)  <br>or \(y(t)=y_0 e^{-\delta t}\cos(\omega_D t+\phi)\) | Oscillatory with exponentially decreasing envelope. |
| **Critically damped** | \(\displaystyle \delta = \omega_0\) | \(\lambda = -\delta\) (double root) | \(\displaystyle y(t)=\big(A+Bt\big)\,e^{-\delta t}\) | Returns to equilibrium as fast as possible **without** oscillating. |
| **Overdamped** | \(\displaystyle \delta > \omega_0\) | \(\lambda_{1,2}= -\delta \pm \sqrt{\delta^{2}-\omega_0^{2}}\) – both are **real and negative** | \(\displaystyle y(t)=A\,e^{\lambda_1 t}+B\,e^{\lambda_2 t}\) with \(\lambda_1\neq\lambda_2\) | No oscillation; the motion is a sum of two decaying exponentials. The slower‑decaying term dominates at long times, giving a “gliding” approach to equilibrium. |

### Why the teacher wrote “δ = ω”?

Often textbooks **rename** the undamped natural frequency \(\omega_0\) simply as \(\omega\).  
If the teacher used that shorthand, the statement “critical damping when \(\delta = \omega\)” really means  

\[
\boxed{\delta = \omega_0}.
\]

The student’s confusion arises because the formula they were given,
\(y(t)=y_0 e^{-\delta t}\cos(\omega t)\), already **assumes** the under‑damped case and uses  

\[
\omega = \omega_D = \sqrt{\omega_0^{2}-\delta^{2}} .
\]

Thus the same symbols appear in two different contexts, which is why the simulation did not match the teacher’s rule.

---

## 4.  Visualising the three cases  

Below are the typical shapes (choose arbitrary \(y_0=1\), \(m=1\) for simplicity).

| Parameter set | Plot description |
|---------------|------------------|
| **Underdamped**: \(\omega_0 = 5\; \text{rad/s},\; \delta = 1\; \text{s}^{-1}\) | Oscillations with period \(2\pi/\omega_D \approx 1.3\) s, envelope \(e^{-t}\). |
| **Critical**: \(\omega_0 = \delta = 5\; \text{s}^{-1}\) | Curve rises (or falls) monotonic, reaches zero fastest among all non‑oscillatory curves. |
| **Overdamped**: \(\omega_0 = 5\; \text{rad/s},\; \delta = 8\; \text{s}^{-1}\) | Two exponentials: one decays quickly, the other slowly. The motion is slower than the critical case even though \(\delta\) is larger. |

If you plot the **envelope** \(e^{-\delta t}\) together with the actual overdamped solution, you will see that the solution never follows the envelope; instead the slower exponential (with rate \(|\lambda_{\text{slow}}| = \delta-\sqrt{\delta^{2}-\omega_0^{2}}\)) dictates the long‑time behavior. Because \(|\lambda_{\text{slow}}| < \delta\), a larger \(\delta\) can *reduce* the overall decay rate, giving the “less steep” appearance.

---

## 5.  Answering the three specific doubts  

### 5.1  Why the given formula only works for under‑damping  

The expression  

\[
y(t)=y_0 e^{-\delta t}\cos(\omega t)
\]

was derived **after** solving (1) under the condition \(\delta<\omega_0\). In that regime the square‑root in (2) is imaginary, leading to a sinusoidal factor with angular frequency  

\[
\omega = \omega_D = \sqrt{\omega_0^{2}-\delta^{2}} .
\]

If \(\delta\ge\omega_0\) the square‑root becomes real, the cosine term would become a hyperbolic cosine or a sum of exponentials, not a simple cosine. Hence the formula is not valid for critical or over‑damping.

### 5.2  Correct condition for each regime  

| Regime | Correct inequality (using the **undamped** frequency \(\omega_0\)) |
|--------|--------------------------------------------------------------------|
| Underdamped | \(\boxed{\delta < \omega_0}\) |
| Critical   | \(\boxed{\delta = \omega_0}\) |
| Overdamped | \(\boxed{\delta > \omega_0}\) |

If your textbook or teacher writes “δ = ω” they are implicitly meaning “δ equals the *undamped* ω”.

### 5.3  Why a larger δ can make the motion slower (over‑damped case)  

For overdamping the solution is  

\[
y(t)=A e^{\lambda_1 t}+B e^{\lambda_2 t},\qquad 
\lambda_{1,2}= -\delta \pm \sqrt{\delta^{2}-\omega_0^{2}} .
\]

Both \(\lambda_{1,2}\) are negative. The **slower** (less negative) root is  

\[
\lambda_{\text{slow}} = -\delta + \sqrt{\delta^{2}-\omega_0^{2}} .
\]

A quick algebraic check shows  

\[
|\lambda_{\text{slow}}| = \delta - \sqrt{\delta^{2}-\omega_0^{2}} \;<\; \delta .
\]

Thus the dominant exponential decays with a rate **smaller** than \(\delta\). As \(\delta\) grows much larger than \(\omega_0\),

\[
\lambda_{\text{slow}} \approx -\frac{\omega_0^{2}}{2\delta},
\]

so the decay actually becomes *slower* the larger the damping constant—exactly what you observed in the simulations.

---

## 6.  Final Summary  

* The damped harmonic oscillator obeys \(\ddot y + 2\delta\dot y + \omega_0^{2}y = 0\).  
* The three regimes are distinguished by the relation between the **damping constant** \(\delta\) and the **undamped natural frequency** \(\omega_0\):  

  * **Underdamped** \(\delta < \omega_0\) → oscillatory with envelope \(e^{-\delta t}\) and damped frequency \(\omega_D = \sqrt{\omega_0^{2}-\delta^{2}}\).  

  * **Critically damped** \(\delta = \omega_0\) → \(y(t)=(A+Bt)e^{-\delta t}\); fastest non‑oscillatory return.  

  * **Overdamped** \(\delta > \omega_0\) → \(y(t)=A e^{\lambda_1 t}+B e^{\lambda_2 t}\) (both terms decay, the slower one has rate \(|\lambda_{\text{slow}}|<\delta\)).  

* The formula \(y(t)=y_0 e^{-\delta t}\cos(\omega t)\) is **only** the under‑damped solution, where \(\omega\) is the *damped* angular frequency \(\omega_D\).  

* Increasing \(\delta\) beyond the critical value makes the dominant decay exponent smaller, so the motion appears “less steep” even though the physical damping coefficient is larger.

---

## 7.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using the same symbol \(\omega\) for both the undamped and the damped frequency.** | The under‑damped solution uses \(\omega_D=\sqrt{\omega_0^{2}-\delta^{2}}\). Confusing the two leads to the wrong condition for critical damping. | Keep the notation: \(\omega_0\) = natural (undamped) frequency; \(\omega_D\) = damped frequency. |
| **Applying the under‑damped formula \(e^{-\delta t}\cos(\omega t)\) to the overdamped case.** | For \(\delta\ge\omega_0\) the cosine becomes a hyperbolic cosine or a sum of exponentials; the formula no longer solves the ODE. | First check the inequality \(\delta\) vs. \(\omega_0\). Use the appropriate general solution from the roots (2). |
| **Thinking that a larger \(\delta\) always makes the system return faster.** | In the overdamped regime the dominant decay rate is \(|\lambda_{\text{slow}}| = \delta -\sqrt{\delta^{2}-\omega_0^{2}}\), which *decreases* as \(\delta\) increases beyond \(\omega_0\). | Remember that “critical damping” is the fastest non‑oscillatory return; any increase beyond that slows the approach. |
| **Ignoring the constant prefactors \(A\) and \(B\).** | The shape of the response (whether it crosses zero, how quickly it decays) depends on the initial conditions encoded in \(A\) and \(B\). | Write the full solution with two arbitrary constants, then apply the given initial displacement and velocity to determine them. |
| **Misreading “critical damping = δ = ω” as a universal rule.** | The teacher’s statement uses \(\omega\) to mean the *undamped* frequency \(\omega_0\). | When you see “δ = ω”, ask whether the instructor is referring to \(\omega_0\)

*Original question: [Damped Oscillators types mathematical function](https://physics.stackexchange.com/questions/875464/damped-oscillators-types-mathematical-function) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
