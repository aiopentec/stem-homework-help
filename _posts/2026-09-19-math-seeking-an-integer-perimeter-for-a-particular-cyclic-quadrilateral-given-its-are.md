---
layout: question
title: Seeking an integer perimeter for a particular cyclic quadrilateral, given its
  area and the radius of its circumcircle .
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Seeking an integer perimeter for
  a particular cyclic quadrilateral, given its area and the radius of its circumcircle
  .'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We have a **convex cyclic quadrilateral** (its four vertices lie on a circle) that  

* has two opposite right angles,  
* has area \(2026\), and  
* is inscribed in a circle of radius \(R=40\).

Among all quadrilaterals that satisfy those three conditions we have to decide  

*whether any of them can have an **integer perimeter**.*

---

## 2.  Geometry of a quadrilateral with opposite right angles  

For a cyclic quadrilateral the opposite angles always add to \(180^{\circ}\).  
Hence if one angle is a right angle, the opposite one must also be a right angle – the situation described in the problem.

Let the two right‑angled vertices be \(B\) and \(D\).  
Because \(\angle B\) subtends the side \(AC\), the chord \(AC\) must be a **diameter** of the circum‑circle.  
Similarly \(\angle D\) subtends the side \(BD\), so \(BD\) is also a diameter.

Thus the quadrilateral consists of the four endpoints of **two diameters** of the same circle.  
The two diameters intersect at the centre \(O\) of the circle.

```
          B •
            \
             \      (diameter BD)
              \
               O •
              / \
   (diameter AC)   \
            /       \
          A •-------• C
                D •
```

Consequently both diagonals have the same length  

\[
|AC|=|BD|=2R=80 .
\]

Let the angle between the two diameters be \(\theta\;(0<\theta<\pi)\).  
Then the area of the quadrilateral is half the product of the diagonals multiplied by the sine of the angle between them:

\[
\boxed{\ \text{Area}= \frac12\,(|AC|)(|BD|)\sin\theta =2R^{2}\sin\theta\ }.
\]

---

## 3.  Determining \(\theta\) from the given area  

The area is \(2026\) and \(R=40\).  Hence  

\[
2026 = 2\cdot 40^{2}\sin\theta
      = 3200\sin\theta
      \quad\Longrightarrow\quad
\sin\theta = \frac{2026}{3200}= \frac{1013}{1600}.
\tag{1}
\]

So \(\sin\theta\) is a **rational** number (but not an integer).

---

## 4.  The side lengths in terms of \(\theta\)

Place the centre at the origin and the first diameter on the \(x\)-axis:

\[
A=(-R,0),\qquad C=(R,0).
\]

Let the second diameter make the angle \(\theta\) with the \(x\)-axis, i.e.

\[
B=(R\cos\theta,\;R\sin\theta),\qquad
D=(-R\cos\theta,\;-R\sin\theta).
\]

The four sides are then

\[
\begin{aligned}
AB &= \sqrt{(R\cos\theta+R)^2+(R\sin\theta)^2}
     = R\sqrt{2+2\cos\theta}=2R\cos\frac{\theta}{2},\\[2mm]
BC &= \sqrt{(R-R\cos\theta)^2+(R\sin\theta)^2}
     = R\

*Original question: [Seeking an integer perimeter for a particular cyclic quadrilateral, given its area and the radius of its circumcircle .](https://math.stackexchange.com/questions/5149820/seeking-an-integer-perimeter-for-a-particular-cyclic-quadrilateral-given-its-ar) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
