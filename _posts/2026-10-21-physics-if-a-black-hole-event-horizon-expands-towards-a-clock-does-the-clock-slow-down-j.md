---
layout: question
title: If a black hole event horizon expands towards a clock, does the clock slow
  down just as it would if it was moving towards a hole with a fixed mass?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: If a black hole event horizon expands
  towards a clock, does the clock slow down just as it would if it was moving towards
  a '
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the problem is really asking  

A distant observer watches a **pendulum clock** that is *outside* a black hole.  
Two different situations are presented:

| Situation | What changes? |
|-----------|----------------|
| **(A)** The clock **moves** radially inward toward a black hole whose mass (and therefore its event‑horizon radius) stays constant. |
| **(B)** The clock **stays at the same radial coordinate**, while the black hole **gains mass**, so its Schwarzschild radius **grows** and eventually reaches the clock. |

In both cases the observer notices that the pendulum appears to tick more and more slowly, and finally seems to stop when the horizon reaches it.  

The question: **Is the slowing of the clock in (B) exactly the same as in (A)?** In other words, does an expanding horizon produce the same “gravitational time‑dilation” effect as a clock that is actually falling into a static hole?

---

## 2.  Detailed solution  

### 2.1  The Schwarzschild metric and gravitational red‑shift  

For a non‑rotating, spherically symmetric black hole the space‑time outside the horizon is described by the Schwarzschild line element  

\[
\boxed{ds^{2}= -\left(1-\frac{r_{\!s}}{r}\right)c^{2}dt^{2}
        +\left(1-\frac{r_{\!s}}{r}\right)^{-1}dr^{2}
        +r^{2}d\Omega^{2}},
\]

where  

* \(r\) = Schwarzschild radial coordinate (circumference / \(2\pi\)),  
* \(t\) = coordinate time measured by an observer **at infinity**,  
* \(r_{\!s}=2GM/c^{2}\) = Schwarzschild radius (the horizon),  
* \(d\Omega^{2}=d\theta^{2}+\sin^{2}\!\theta\,d\phi^{2}\).

A **static** clock (i.e. held at fixed \(r\) with \(dr=d\theta=d\phi=0\)) experiences a proper time interval  

\[
d\tau = \sqrt{1-\frac{r_{\!s}}{r}}\; dt .
\tag{1}
\]

Equation (1) tells us how many seconds the clock actually ticks (\(d\tau\)) compared with the seconds counted by the distant observer (\(dt\)). The factor  

\[
\gamma_{\rm grav}(r)=\frac{1}{\sqrt{1-r_{\!s}/r}}
\]

is the **gravitational time‑dilation factor**. As the clock gets closer to the horizon (\(r\rightarrow r_{\!s}^{+}\)), the square‑root tends to zero, so \(\gamma_{\rm grav}\) diverges and the distant observer sees the clock tick more and more slowly. In the limit \(r\to r_{\!s}\) the ticking rate goes to zero – the clock appears to “freeze”.

### 2.2  Situation (A): Clock **moving** toward a *fixed* horizon  

If the clock is falling radially with velocity \(v\) (as measured locally), its total dilation as seen from infinity is the product of the gravitational factor (1) and the special‑relativistic factor  

\[
\gamma_{\rm SR}= \frac{1}{\sqrt{1-v^{2}/c^{2}}}.
\]

Thus  

\[
\boxed{\frac{d\tau}{dt}= 
\sqrt{1-\frac{r_{\!s}}{r}}\;
\frac{1}{\gamma_{\rm SR}} } .
\tag{2}
\]

Near the horizon the gravitational term dominates: even if \(v\) is modest, \(\sqrt{1-r_{\!s}/r}\) becomes tiny, so the product in (2) goes to zero. The distant observer therefore sees the pendulum slow down and asymptotically stop as the clock approaches the horizon. The clock itself, however, experiences a finite proper time to reach the horizon.

### 2.3  Situation (B): **Horizon expands** toward a *static* clock  

Now keep the clock at a fixed coordinate radius \(r_{0}\) (e.g. it is hanging from a rope). The black hole’s mass grows with time, so the Schwarzschild radius becomes a function \(r_{\!s}(t)\). For an observer at infinity we can still use (1) **instantaneously**, because the metric at any moment is the Schwarzschild metric with the current value of \(M(t)\). Hence at each instant

\[
\frac{d\tau}{dt}= \sqrt{1-\frac{r_{\!s}(t)}{r_{0}}}\; .
\tag{3}
\]

As the black hole accretes mass, \(r_{\!s}(t)\) increases. When the horizon radius approaches the clock’s radius (\(r_{\!s}(t)\to r_{0}^{-}\)), the square‑root again tends to zero, and the distant observer sees the pendulum’s ticking rate tend to zero.  

**Key point:** The *form* of the time‑dilation factor is **identical** to the static‑mass case; the only difference is that now the factor changes because the *parameter* \(r_{\!s}\) is varying rather than the coordinate \(r\).

### 2.4  How quickly does the dilation change?  

Suppose the black hole gains mass at a (slow) rate \(\dot M\). Then  

\[
\dot r_{\!s}= \frac{2G}{c^{2}}\dot M .
\]

If the clock sits at \(r_{0}\), the rate at which the observed ticking frequency \(\nu_{\infty}\) changes is  

\[
\frac{d\nu_{\infty}}{dt}= 
\frac{d}{dt}\Bigl[\nu_{0}\sqrt{1-\frac{r_{\!s}(t)}{r_{0}}}\Bigr]
= -\,\frac{\nu_{0}}{2\sqrt{1-r_{\!s}/r_{0}}}\,
\frac{\dot r_{\!s}}{r_{0}} .
\]

As \(r_{\!s}\) approaches \(r_{0}\), the denominator becomes very small, so even a modest \(\dot r_{\!s}\) produces a rapid decline of the observed frequency – the clock appears to “freeze” very quickly once the horizon is almost there.

### 2.5  What the clock **itself** experiences  

For the clock (its proper time) nothing singular happens at the instant the horizon reaches it. Equation (3) simply tells us that the *coordinate* time between successive ticks grows without bound, but the proper interval between ticks stays the same (the pendulum still swings with its own natural period). In other words, the clock does **not** physically slow down; the slowdown is a *red‑shift* of the signal as it climbs out of an ever‑deepening gravitational well.

### 2.6  Answer to the original question  

> **Yes.** Whether the horizon expands outward because the black hole’s mass grows, or the clock moves inward toward a fixed horizon, a distant observer sees the same gravitational time‑dilation effect: the pendulum’s ticking rate diminishes, approaching zero as the horizon reaches the clock. The mathematical description is the same; only the variable that changes (the radius \(r\) of the clock or the Schwarzschild radius \(r_{\!s}\) of the hole) is different.

---

## 3.  Final answer  

*For a clock that remains at a fixed radius while a black hole’s mass increases, the observed ticking rate is*

\[
\boxed{\displaystyle 
\frac{d\tau}{dt}= \sqrt{1-\frac{2G M(t)}{c^{2} r_{\!{\rm clock}}}} } ,
\]

*which tends to zero exactly as the Schwarzschild radius \(r_{\!s}=2GM/c^{2}\) approaches the clock’s radius. This is mathematically the same behaviour as a clock that moves inward toward a hole of constant mass. Therefore, from the viewpoint of a distant observer, the clock “slows down and freezes” in both scenarios.*  

---

## 4.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing proper time with the time seen at infinity.**  The pendulum’s own period never changes; only the red‑shifted signal does. | Proper time \(d\tau\) is what the clock measures locally. The distant observer measures \(dt\). | Always write down the relation \(d\tau = \sqrt{1-r_{\!s}/r}\,dt\) and keep the two quantities distinct. |
| **Thinking the horizon “pushes” the clock.** The horizon is not a material surface; it is a null surface defined by the metric. | No force is exerted on a static clock just because the horizon expands. | Emphasise that the horizon’s motion is a change in the space‑time geometry, not a physical object. |
| **Neglecting causality: assuming the mass increase instantly affects the clock’s location.** Changes in the gravitational field propagate at the speed of light. | If the black hole gains mass at some distant radius, the metric at the clock’s position only changes after a light‑travel time. | Mention the propagation delay and treat the problem as “quasi‑static” (mass changes slowly compared with light‑crossing time). |
| **Using only the special‑relativistic Doppler formula.** Near a horizon the dominant effect is gravitational red‑shift, not relative velocity. | The special‑relativistic factor \(\gamma_{\rm SR}\) alone cannot produce the infinite slowdown. | Combine both factors as in Eq. (2) when the clock is moving, but recognise that the \(\sqrt{1-r_{\!s}/r}\) term alone already gives the divergence. |
| **Assuming the clock will be seen to *cross* the horizon.** The signal from the crossing is infinitely red‑shifted. | No finite‑frequency photon can escape from exactly the horizon, so the distant observer never receives a crossing event. | State explicitly that the observer sees the clock asymptotically approach the horizon, never actually cross it. |

By keeping these points in mind, you can correctly analyze any scenario involving clocks near a black‑hole horizon—whether the horizon is static or growing.

*Original question: [If a black hole event horizon expands towards a clock, does the clock slow down just as it would if it was moving towards a hole with a fixed mass?](https://physics.stackexchange.com/questions/877104/if-a-black-hole-event-horizon-expands-towards-a-clock-does-the-clock-slow-down) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
