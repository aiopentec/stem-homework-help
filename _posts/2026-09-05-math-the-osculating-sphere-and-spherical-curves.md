---
layout: question
title: The osculating sphere and spherical curves.
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: The osculating sphere and spherical
  curves.'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem asks  

We have a regular space curve  

\[
c:\;I\to\mathbb R^{3},\qquad s\mapsto c(s)
\]

parameterised by its **arc length** \(s\) (so \(\|c'(s)\|=1\)).  
Let  

\[
e_{1}=T,\qquad e_{2}=N,\qquad e_{3}=B
\]

be the Frenet frame, with curvature \(\kappa(s)>0\) and torsion
\(\tau(s)\neq0\).

* **(i)** Show that the sphere whose centre  

\[
m(s_{0})=c(s_{0})+\frac{1}{\kappa(s_{0})}\,e_{2}(s_{0})
           -\frac{\kappa'(s_{0})}{\tau(s_{0})\kappa^{2}(s_{0})}\,e_{3}(s_{0})
\tag{1}
\]

passes through the point \(c(s_{0})\) and meets the curve at \(s_{0}\) with
contact of order three (third‑order contact).  
The sphere is called the **osculating sphere**.

* **(ii)** Assume the curve is of class \(C^{4}\) and \(\tau\neq0\) everywhere.  
Prove that the curve lies on a (fixed) sphere **iff**

\[
\boxed{\displaystyle 
\frac{\tau}{\kappa}= \Bigl(\frac{\kappa'}{\tau\kappa^{2}}\Bigr)'}
\tag{2}
\]

---

## 2.  Preliminaries – Frenet formulas  

Because the curve is parametrised by arc length we have  

\[
\begin{aligned}
T' &= \kappa N ,\\[2pt]
N' &=-\kappa T + \tau B ,\\[2pt]
B' &=-\tau N .
\end{aligned}
\tag{3}
\]

We shall also use  

\[
c'(s)=T(s),\qquad 
c''(s)=\kappa N ,\qquad 
c'''(s)= -\kappa^{2}T +\kappa' N +\kappa\tau B .
\tag{4}
\]

---

## 3.  Part (i) – The osculating sphere  

### 3.1  Setting up the centre  

Write the (as yet unknown) centre of the sphere as  

\[
m=m(s_{0})=c_{0}+ \alpha\,e_{1}(s_{0})+\beta\,e_{2}(s_{0})+\gamma\,e_{3}(s_{0}),
\qquad c_{0}=c(s_{0}).
\tag{5}
\]

Define the squared distance from a point of the curve to the centre  

\[
f(s)=\bigl\langle c(s)-m,\;c(s)-m\bigr\rangle .
\tag{6}
\]

The sphere through \(c_{0}\) has radius  

\[
R^{2}=f(s_{0}) .
\]

If the curve has **third‑order contact** with the sphere at \(s_{0}\) then,
apart from the obvious equality \(f(s_{0})=R^{2}\), the first three
derivatives of \(f\) must vanish at \(s_{0}\):

\[
f'(s_{0})=f''(s_{0})=f'''(s_{0})=0 .
\tag{7}
\]

These three equations will determine \(\alpha,\beta,\gamma\).

---

### 3.2  Computing the derivatives  

Because the centre \(m\) is constant, differentiation of (6) gives  

\[
\begin{aligned}
f'(s) &= 2\langle c'(s),\,c(s)-m\rangle,\\[2pt]
f''(s) &= 2\langle c''(s),\,c(s)-m\rangle + 2\langle c'(s),c'(s)\rangle ,\\[2pt]
f'''(s) &= 2\langle c'''(s),\,c(s)-m\rangle
          +6\langle c''(s),c'(s)\rangle .
\end{aligned}
\tag{8}
\]

Now evaluate at \(s=s_{0}\) and insert the Frenet expressions (4).

* **First derivative**

\[
f'(s_{0}) = 2\langle T_{0},\,c_{0}-m\rangle
          = 2\langle T_{0},-\alpha T_{0}-\beta N_{0}-\gamma B_{0}\rangle
          = -2\alpha .
\]

Thus \(f'(s_{0})=0\) gives  

\[
\boxed{\alpha =0}.
\tag{9}
\]

* **Second derivative**

\[
\begin{aligned}
f''(s_{0}) &= 2\langle \kappa N_{0},\;c_{0}-m\rangle + 2\langle T_{0},T_{0}\rangle\\
           &= 2\bigl(\kappa\langle N_{0}, -\beta N_{0}-\gamma B_{0}\rangle\bigr)+2\\
           &= 2(-\kappa\beta)+2 .
\end{aligned}
\]

Setting \(f''(s_{0})=0\) yields  

\[
\boxed{\beta = \frac{1}{\kappa(s_{0})}} .
\tag{10}
\]

* **Third derivative**

Because \(\langle c'' ,c'\rangle = \langle \kappa N_{0},T_{0}\rangle =0\), the
last term in (8) vanishes. Using (4),

\[
\begin{aligned}
f'''(s_{0}) &= 2\bigl\langle -\kappa^{2}T_{0}+ \kappa' N_{0}+ \kappa\tau B_{0},
                  \;c_{0}-m\bigr\rangle\\
           &= 2\Bigl\langle -\kappa^{2}T_{0}+ \kappa' N_{0}+ \kappa\tau B

*Original question: [The osculating sphere and spherical curves.](https://math.stackexchange.com/questions/5148700/the-osculating-sphere-and-spherical-curves) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
