---
layout: question
title: Elliptical orrery path
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Elliptical orrery path'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the student is trying to prove  

The student wants a **single rotating arm** that drives a planet on a *Keplerian ellipse* (focus 1 at the star).  
The arm is imagined to rotate with a **constant angular speed**  ω  about the *second* focus (the empty focus).  
If the linear speed of the planet that results from that arm is  

\[
V_{t}= \omega \frac{|\mathbf T\times \mathbf S|}{|\mathbf T|},
\]

the student claims that this speed can be made equal, for every point on the ellipse, to the true orbital speed  

\[
v_{p}= \sqrt{\mu\!\left(\frac{2}{|\mathbf r|}-\frac{1}{a}\right)},
\]

by a suitable choice of the constants \( \mu \) (gravitational parameter) and \( \omega \) (the arm’s angular speed).  

In other words: **Is there a point on an ellipse from which a uniform‑speed rotation produces exactly the Keplerian velocity everywhere on the ellipse?**  

The answer is *no* – a uniform rotation about the empty focus cannot reproduce the varying Keplerian speed.  
Below we work through the geometry, write the two speeds explicitly, and show that their ratio **does depend on the orbital position** (the true anomaly). The student’s conclusion that the ratio is independent of the anomaly comes from an algebraic slip.

---

## 2. Geometry of the ellipse  

Let  

* \(a\) – semi‑major axis,  
* \(b\) – semi‑minor axis,  
* \(e\) – eccentricity, \(e = \sqrt{1-b^{2}/a^{2}}\).  

The centre of the ellipse is at the origin, the major axis lies on the *x*‑axis and the two foci are at  

\[
\mathbf F_{1}= (+ea,0),\qquad \mathbf F_{2}= (-ea,0).
\]

The **eccentric anomaly** \(t\) (often called \(E\)) parametrises the ellipse in the usual way  

\[
\mathbf R(t)=\begin{pmatrix} a\cos t \\[2pt] b\sin t \\[2pt] 0 \end{pmatrix}.
\]

The *position vector from the *star* (focus 1) to the planet* is  

\[
\boxed{\;\mathbf r(t)=\mathbf R(t)-\mathbf F_{1}
      =\begin{pmatrix} a\cos t-ea \\[2pt] b\sin t \\[2pt] 0 \end{pmatrix}\;}
\tag{1}
\]

and the vector from the *empty* focus (focus 2) to the same point is  

\[
\boxed{\;\mathbf S(t)=\mathbf R(t)-\mathbf F_{2}
      =\begin{pmatrix} a\cos t+ea \\[2pt] b\sin t \\[2pt] 0 \end{pmatrix}\;}
\tag{2}
\]

The **tangent vector** to the ellipse (the derivative of \(\mathbf R\) with respect to \(t\)) is  

\[
\boxed{\;\mathbf T(t)=\frac{d\mathbf R}{dt}
      =\begin{pmatrix} -a\sin t \\[2pt] b\cos t \\[2pt] 0 \end{pmatrix}\;}
\tag{3}
\]

All three vectors lie in the *x‑y* plane, so we can treat the cross product as a scalar equal to the *z*‑component of \(\mathbf T\times\mathbf S\).

---

## 3. Speed that a constant‑ω arm would give  

The arm rotates about focus 2 with constant angular speed \( \omega\).  
At a given instant the linear speed of the point that follows the arm is the product of the angular speed and the *perpendicular* distance from the rotation centre to the instantaneous direction of motion.  

That perpendicular distance is  

\[
d(t)=\frac{|\mathbf T\times\mathbf S|}{|\mathbf T|},
\]

hence the **arm‑induced speed**

\[
\boxed{\;V_{t}(t)=\omega\,\frac{|\mathbf T\times\mathbf S|}{|\mathbf T|}\;}
\tag{4}
\]

Let us evaluate the two factors in (4).

### 3.1   Magnitude of the tangent  

\[
|\mathbf T| =\sqrt{(-a\sin t)^{2}+(b\cos t)^{2}}
           =\sqrt{a^{2}\sin^{2}t+b^{2}\cos^{2}t}.
\tag{5}
\]

### 3.2   Magnitude of the cross product  

Because the vectors are planar,  

\[
\mathbf T\times\mathbf S = 
\begin{vmatrix}
\mathbf i & \mathbf j & \mathbf k\\
-a\sin t & b\cos t & 0\\
a\cos t+ea & b\sin t & 0
\end{vmatrix}
= \bigl[\,(-a\sin t)(b\sin t)- (b\cos t)(a\cos t+ea)\,\bigr]\;\mathbf k .
\]

Thus  

\[
|\mathbf T\times\mathbf S|
 =\Bigl| -ab\sin t\sin t -ab\cos t\cos t - a e b\cos t \Bigr|
 =\bigl| -ab(\sin^{2}t+\cos^{2}t)-a e b\cos t \bigr|
 =ab\bigl|\,1+e\cos t\,\bigr|.
\tag{6}
\]

Since \(1+e\cos t\ge 0\) for an ellipse, we may drop the absolute value:

\[
|\mathbf T\times\mathbf S| =ab\,(1+e\cos t).
\]

### 3.3   Putting them together  

Insert (5) and (6) into (4):

\[
\boxed{\;V_{t}(t)=\omega\,\frac{ab\,(1+e\cos t)}
                         {\sqrt{a^{2}\sin^{2}t+b^{2}\cos^{2}t}}\;}
\tag{7}
\]

---

## 4. True Keplerian speed on the ellipse  

For a body moving under the inverse‑square law the **vis‑viva equation** gives

\[
v_{p}(t)=\sqrt{\mu\Bigl(\frac{2}{r(t)}-\frac{1}{a}\Bigr)}.
\tag{8}
\]

The distance from focus 1 to the planet is the length of \(\mathbf r(t)\):

\[
r(t)=|\mathbf r| =\sqrt{(a\cos t-ea)^{2}+(b\sin t)^{2}}
               =\sqrt{a^{2}+e^{2}a^{2}-2ea^{2}\cos t - (a^{2}-b^{2})\sin^{2}t } .
\]

A simpler expression is obtained from the standard polar form of an ellipse,

\[
r(t)=\frac{a(1-e^{2})}{1+e\cos\theta},
\]

where \(\theta\) is the **true anomaly** (the angle measured from focus 1).  
The relationship between the eccentric anomaly \(t\) and the true anomaly \(\theta\) is  

\[
\boxed{\;\cos\theta=\frac{\cos t-e}{1-e\cos t}},\qquad
\boxed{\;1+e\cos\theta = \frac{1-e^{2}}{1-e\cos t}}.
\tag{9}
\]

Using (9),

\[
r(t)=\frac{a(1-e^{2})}{1+e\cos\theta}
    = a\frac{1-e^{2}}{1+e\cos\theta}
    = a\frac{1-e^{2}}{\,\frac{1-e^{2}}{1-e\cos t}\,}
    = a(1-e\cos t).
\tag{10}
\]

Thus the vis‑viva speed becomes

\[
\begin{aligned}
v_{p}(t)&=\sqrt{\mu\Bigl(\frac{2}{a(1-e\cos t)}-\frac{1}{a}\Bigr)}\\[4pt]
        &=\sqrt{\frac{\mu}{a}\,
               \Bigl(\frac{2}{1-e\cos t}-1\Bigr)}\\[4pt]
        &=\sqrt{\frac{\mu}{a}\,
               \frac{1+e\cos t}{1-e\cos t}} .
\end{aligned}
\tag{11}
\]

---

## 5. Ratio of the two speeds  

Now form the ratio

\[
\frac{V_{t}(t)}{v_{p}(t)}=
\frac{\displaystyle \omega\,
      \frac{ab\,(1+e\cos t)}{\sqrt{a^{2}\sin^{2}t+b^{2}\cos^{2}t}}}
     {\displaystyle \sqrt{\frac{\mu}{a}\,
                \frac{1+e\cos t}{1-e\cos t}} } .
\]

Cancel the common factor \(\sqrt{1+e\cos t}\) and simplify:

\[
\boxed{\;
\frac{V_{t}}{v_{p}}=
\omega\,\sqrt{a}\,
\frac{b\sqrt{1+e\cos t}}
     {\sqrt{a^{2}\sin^{2}t+b^{2}\cos^{2}t}}\;
\sqrt{\frac{1-e\cos t}{\mu}}\; } .
\tag{12}
\]

The crucial observation is that **the right‑hand side still contains the anomaly \(t\)** (through \(\sin t,\cos t\)).  
Only if the factor

\[
\frac{b\sqrt{1+e\cos t}}{\sqrt{a^{2}\sin^{2}t+b^{2}\cos^{2}t}}\,
\sqrt{1-e\cos t}
\]

were a constant could we choose \(\omega\) and \(\mu\) to make the whole ratio a constant.  
But this factor **does vary** as the planet moves from periapsis (\(t=0\)) to apoapsis (\(t=\pi\)).  

### 5.1   Explicit dependence  

A convenient way to see the variation is to rewrite the denominator using the identity  

\[
a^{2}\sin^{2}t+b^{2}\cos^{2}t = a^{2}\bigl(1-e^{2}\cos^{2}t\bigr),
\]

which follows from \(b^{2}=a^{2}(1-e^{2})\). Then

\[
\frac{V_{t}}{v_{p}}=
\omega\sqrt{\frac{a}{\mu}}\;
\frac{b}{a}\;
\frac{\sqrt{(1+e\cos t)(1-e\cos t)}}
     {\sqrt{1-e^{2}\cos^{2}t}}
=
\omega\sqrt{\frac{a}{\mu}}\;
\frac{b}{a}\;
\frac{\sqrt{1-e^{2}\cos^{2}t}}
     {\sqrt{1-e^{2}\cos^{2}t}}
=
\omega\sqrt{\frac{a}{\mu}}\;\frac{b}{a}.
\]

**Whoa!** The algebra looks as if the \(t\)-dependence has cancelled.  
The cancellation *is* correct **only** when we have used the *true* relationship  

\[
b^{2}=a^{2}(1-e^{2}) .
\]

But notice that in the numerator we have \(\

*Original question: [Elliptical orrery path](https://physics.stackexchange.com/questions/875961/elliptical-orrery-path) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
