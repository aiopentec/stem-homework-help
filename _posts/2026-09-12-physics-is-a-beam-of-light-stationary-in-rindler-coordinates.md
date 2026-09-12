---
layout: question
title: Is a beam of light stationary in Rindler coordinates?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Is a beam of light stationary in Rindler
  coordinates?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

A uniformly‑accelerated observer (constant proper acceleration \(a_{0}\)) can be described with **Rindler coordinates** \((\eta ,\xi )\).  
The observer’s own world‑line is \(\xi =0\); his proper time equals the Rindler time \(\eta\).

The claim we have to test is:

> *“A beam of light that is emitted from the origin (the point where the observer’s world‑line meets the Minkowski‑space origin) appears to be *still* in the accelerated observer’s frame; i.e. in Rindler coordinates the light’s spatial coordinate does not change while the time coordinate runs.”*

Our job is to write the light‑ray world‑line in inertial \((t,x)\) coordinates, transform it to \((\eta ,\xi )\), and see what the \(\xi\)‑coordinate does as \(\eta\) increases.

---

## 2. Step‑by‑step derivation

### 2.1  Minkowski description of the uniformly accelerated observer  

In an inertial frame \((ct,x)\) the world‑line of an observer with constant proper acceleration \(a_{0}>0\) is  

\[
\boxed{
\begin{aligned}
ct(\tau) &= \frac{c^{2}}{a_{0}}\;\sinh\!\left(\frac{a_{0}\tau}{c}\right),\\[2mm]
x(\tau)  &= \frac{c^{2}}{a_{0}}\;\cosh\!\left(\frac{a_{0}\tau}{c}\right),
\end{aligned}}
\tag{1}
\]

where \(\tau\) is the observer’s proper time.  
These equations describe the **right‑hand Rindler wedge** (\(x>|ct|\)).

---

### 2.2  Definition of Rindler coordinates  

Introduce coordinates \((\eta ,\xi )\) that cover the same wedge:

\[
\boxed{
\begin{aligned}
ct &= \frac{c^{2}}{a_{0}}\;e^{a_{0}\xi/c^{2}}\;\sinh\!\left(\frac{a_{0}\eta}{c}\right),\\[2mm]
x  &= \frac{c^{2}}{a_{0}}\;e^{a_{0}\xi/c^{2}}\;\cosh\!\left(\frac{a_{0}\eta}{c}\right).
\end{aligned}}
\tag{2}
\]

* The **Rindler time** \(\eta\) measures the proper time of the observer sitting at \(\xi =0\) (compare (1) with (2) and set \(\xi=0\) → \(\eta=\tau\)).  
* The **Rindler space coordinate** \(\xi\) is a logarithmic measure of the distance from the observer’s world‑line; surfaces of constant \(\xi\) are hyperbolae of constant proper acceleration.

The metric obtained from (2) is  

\[
ds^{2}= -\left( a_{0}\, \xi\right)^{2} d\eta^{2}+ d\xi^{2},
\qquad (\xi>0).
\tag{3}
\]

---

### 2.3  The light ray in the inertial frame  

A light signal that is emitted **from the Minkowski origin** \((t=0,x=0)\) and travels in the \(+x\) direction satisfies  

\[
x = c t .
\tag{4}
\]

(It is a null line, \(ds^{2}=0\).)

---

### 2.4  Transform the light ray to Rindler coordinates  

Insert the expressions (2) for \(ct\) and \(x\) into (4):

\[
\frac{c^{2}}{a_{0}}\;e^{a_{0}\xi/c^{2}}\;\cosh\!\left(\frac{a_{0}\eta}{c}\right)
=
\frac{c^{2}}{a_{0}}\;e^{a_{0}\xi/c^{2}}\;\sinh\!\left(\frac{a_{0}\eta}{c}\right).
\]

The overall factor \(\dfrac{c^{2}}{a_{0}}e^{a_{0}\xi/c^{2}}\) is non‑zero

*Original question: [Is a beam of light stationary in Rindler coordinates?](https://physics.stackexchange.com/questions/875929/is-a-beam-of-light-stationary-in-rindler-coordinates) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
