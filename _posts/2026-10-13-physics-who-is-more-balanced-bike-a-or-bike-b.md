---
layout: question
title: Who is more balanced Bike A or Bike B?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Who is more balanced Bike A or Bike B?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the problem is really asking  

We have two identical‑looking bicycles that move at the same speed on the same road.  
The only difference is **the total mass of the bike** (including the frame, wheels, etc.) – bike **A** is heavier than bike **B**.  

The question is:

*Which bike will feel “more balanced’’ (i.e., be harder to tip or wobble) when a small disturbance – a gust of wind, a bump, a brief push – tries to un‑balance it?*  

Equivalently, on which bike is the **probability of an accident caused by loss of balance** larger?

---

## 2.  Detailed solution  

### 2.1  Modelling a bicycle as an inverted pendulum  

When a bike leans slightly to one side its motion can be approximated by an **inverted pendulum** rotating about a horizontal axis through the contact patch of the tyre.  
For small angles ( θ ≲ 10° ) we can linearise the equations.

| Symbol | Meaning |
|--------|---------|
| *m*    | total mass of bike (frame + wheels + rider, if the rider is the same on both bikes we can ignore it) |
| *g*    | acceleration of gravity (9.81 m s⁻²) |
| *h*    | height of the centre of mass (CM) above the ground |
| *I*    | moment of inertia of the whole system about the roll axis (through the tyre‑road contact) |
| *τ*    | external torque that tries to tip the bike (wind, bump, push) |
| *θ*    | lean angle (θ = 0 when the bike is upright) |
| *α*    | angular acceleration =  d²θ/dt² |

#### Equation of rotational motion  

\[
I\,\alpha = \tau - m g h \,\sin\theta \;\;\xrightarrow{\;\theta\;\text{small}\;}\;\; I\,\ddot\theta = \tau - m g h \,\theta .
\]

The term \(mgh\,\theta\) is the **restoring torque** produced by gravity; the heavier the bike, the larger this torque.

### 2.2  How mass influences the response to a disturbance  

#### 2.2.1  External torque from a disturbance  

Assume a short impulse (a gust of wind) delivers a torque \(\tau\) that is **independent of the bike’s mass** – the wind pushes on the same frontal area, the bump raises the same wheel, etc.

From the equation above the **initial angular acceleration** caused by the impulse is  

\[
\alpha = \frac{\tau}{I}.
\]

A larger moment of inertia \(I\) gives a smaller \(\alpha\).  
For objects with the same shape, the moment of inertia scales linearly with mass:

\[
I \;=\; k\, m, \qquad k\;(\text{geometry factor}) = \text{constant for the two bikes}.
\]

Therefore  

\[
\alpha = \frac{\tau}{k\,m}\;\propto\;\frac{1}{m}.
\]

*The heavier bike (larger *m*) accelerates angularly more slowly, i.e. it “leans’’ less for the same disturbance.*

#### 2.2.2  Restoring torque  

The gravitational restoring torque also grows with mass:

\[
\tau_{\text{restore}} = m g h \,\theta .
\]

A larger mass therefore produces a **stronger pull back toward the upright position**.  

If we write the linearised equation in the standard form of a simple harmonic oscillator:

\[
\ddot\theta + \underbrace{\frac{m g h}{I}}_{\displaystyle \omega^{2}} \theta = \frac{\tau}{I},
\]

the natural (small‑angle) frequency is  

\[
\omega = \sqrt{\frac{m g h}{I}} = \sqrt{\frac{g h}{k}} ,
\]

which is **independent of the total mass** because both the numerator and denominator contain *m*.  
What matters for *stability* is not the frequency but the **size of the response** to a given torque, which, as shown above, scales as \(1/m\).

### 2.3  Translational (linear) stability  

The same external forces (air drag, rolling friction) act on both bikes because they have identical shape, speed and tyre radius.  
From Newton’s second law  

\[
F = m a,
\]

the **linear acceleration** produced by a given force is also smaller for the heavier bike.  
Thus a gust that would slow bike B noticeably will change the speed of bike A only a little, giving the rider of A more time to react.

### 2.4  Putting it together  

| Effect | Depends on mass? | Consequence for heavier bike (A) |
|--------|------------------|----------------------------------|
| Angular acceleration from a tip‑inducing torque | **Inverse** (\(\alpha \propto 1/m\)) | **Smaller** lean rate → harder to tip |
| Restoring gravitational torque | **Direct** (\(\propto m\)) | **Stronger** pull back to upright |
| Linear acceleration from drag / friction | **Inverse** (\(a = F/m\)) | **Smaller** speed change → more time to correct |
| Moment of inertia (geometry same) | **Direct** (\(I \propto m\)) | Larger resistance to rotation |

Hence **bike A (the heavier one) is more “balanced’’**: a given disturbance makes it lean more slowly and the gravitational torque pulls it back more strongly.  

Because the probability of an accident caused by loss of balance is roughly proportional to the size of the lean response, **the chance of an accident is larger for bike B** (the lighter bike).

---

## 3.  Final answer  

- **Bike A (the heavier bike) is more balanced** – it resists being tipped or wobbling more effectively than bike B.  
- Consequently, **the probability of a balance‑related accident is higher for bike B** (the lighter bike).

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking “heavier = more momentum → more likely to crash.”** | Momentum matters for *collision* severity, not for *stability* against small torques. Stability depends on *rotational* inertia, not linear momentum. | Separate the concepts: use \(I\) for rotational response, \(m\) for linear response. |
| **Assuming friction or air drag increase with mass.** | The aerodynamic drag and rolling resistance are functions of shape, speed, and tyre radius – they are the same for both bikes. | Remember the forces are identical; only the acceleration they cause differs ( \(a = F/m\) ). |
| **Neglecting the restoring torque of gravity.** | The restoring torque also scales with mass, reinforcing stability of the heavier bike. | Include both the disturbance torque and the restoring torque in the equation of motion. |
| **Using the natural frequency \(\omega = \sqrt{gh/I}\) to claim the heavier bike is *more* stable.** | For identical geometry \(\omega\) is independent of mass; stability is judged by the *amplitude* of the response, not the frequency. | Focus on the factor \(\tau/I\) (angular acceleration) when comparing the two bikes. |
| **Ignoring rider mass (assuming it’s the same on both bikes).** | If the rider’s mass dominates, the difference in bike mass becomes negligible. | State the assumption clearly: either rider mass is the same and small compared with the bike mass, or we are comparing total system mass. |

By keeping these points in mind, you can correctly assess balance and stability for objects that differ only in mass.

*Original question: [Who is more balanced Bike A or Bike B?](https://physics.stackexchange.com/questions/876876/who-is-more-balanced-bike-a-or-bike-b) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
