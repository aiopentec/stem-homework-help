---
layout: post
title: What is the largest volume of a polyhedron whose skeleton has total length
  1? Is it the regular triangular prism?
author: StemFix Bot
category: math
tags:
- math
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem asks (in plain language)

We are given a **polyhedron** – a solid bounded by flat polygonal faces.  
Let  

* \(L\) = the **total length of all its edges** (the “perimeter’’ of the polyhedron).  

The problem fixes this total edge‑length to be  

\[
L=1 .
\]

Among **all** possible polyhedra whose edge‑length sum is \(1\) we are asked to find the **largest possible volume** and to identify the shape that attains it.

--------------------------------------------------------------------

## 2.  Full solution  

### 2.1  Notation and elementary facts  

* For a polyhedron \(P\) denote  

  * \(V(P)\) – its volume,  
  * \(S(P)\) – its surface area,  
  * \(L(P)\) – the sum of the lengths of all its edges (the given “perimeter’’).  

* Every edge belongs to exactly two faces, therefore  

\[
\sum_{F\;{\rm face}} \operatorname{perimeter}(F)=2L . \tag{1}
\]

* **Planar isoperimetric inequality** – for any planar region with perimeter \(p\) the area \(A\) satisfies  

\[
A\le \frac{p^{2}}{4\pi},
\]

with equality only for a circle.  

* **Spatial isoperimetric inequality** – among all bodies with a given surface area \(S\), the sphere has the greatest volume. Hence for any body (in particular any polyhedron)

\[
V\le \frac{S^{3/2}}{6\sqrt{\pi}} . \tag{2}
\]

The constant \(1/(6\sqrt\pi)\) is exact for a sphere because a sphere of radius \(r\) has \(S=4\pi r^{2}\) and \(V=\tfrac{4}{3}\pi r^{3}= \frac{(4\pi r^{2})^{3/2}}{6\sqrt\pi}\).

--------------------------------------------------------------------

### 2.2  An upper bound for the surface area in terms of the total edge length  

Let the faces be \(F_{1},\dots ,F_{m}\) and let \(p_i\) be the perimeter of \(F_i\).
Applying the planar isoperimetric inequality to each face,

\[
\operatorname{area}(F_i)\le \frac{p_i^{2}}{4\pi}.
\]

Summing over all faces gives a bound for the total surface area:

\[
S(P)=\sum_{i=1}^{m}\operatorname{area}(F_i)
     \le \frac{1}{4\pi}\sum_{i=1}^{m}p_i^{2}. \tag{3}
\]

Now we use the fact that **every face has at least three edges**.  
Consequently each perimeter \(p_i\) is at least three times the length of the *shortest* edge of the polyhedron.  
Let \(e_{\min}\) denote this shortest edge length. Then  

\[
p_i\ge 3e_{\min}\qquad (i=1,\dots ,m). \tag{4}
\]

From (1) we have \(\sum p_i = 2L\).  With the restriction (4) the sum of the squares \(\sum p_i^{2}\) is maximised when **all perimeters are equal** (a standard consequence of the Cauchy–Schwarz inequality).  
Hence the maximal possible value of \(\sum p_i^{2}\) under the constraints
\[
\sum p_i = 2L,\qquad p_i\ge 3e_{\min}
\]
is attained when every face has the same perimeter  

\[
p_i = \frac{2L}{m}.
\]

In that case (3) becomes  

\[
S(P)\le \frac{1}{4\pi}\; m\Bigl(\frac{2L}{m}\Bigr)^{2}
      =\frac{L^{2}}{\pi\,m}. \tag{5}
\]

Because each face needs at least three edges, the number of faces satisfies \(m\ge 2\).  
The *largest* right‑hand side of (5) is therefore obtained for the **smallest possible** \(m\), namely \(m=2\).  
But a polyhedron cannot have only two faces – the smallest admissible number of faces is **four** (a tetrahedron).  
Putting \(m=4\) we obtain the universal bound  

\[
S(P)\le \frac{L^{2}}{4\pi}. \tag{6}
\]

A sharper bound is obtained by using the fact that **each vertex belongs to at least three edges**.  
A short combinatorial argument (Euler’s formula \(V-E+F=2\) together with the handshaking lemma) shows that the *average* number of edges per face is at most \(6\).  
Consequently  

\[
\frac{1}{m}\sum_{i=1}^{m}p_i^{2}\le
\frac{6}{m^{2}}\Bigl(\sum_{i=1}^{m}p_i\Bigr)^{2}
= \frac{6}{m^{2}}(2L)^{2}= \frac{24L^{2}}{m^{2}} .
\]

Insert this into (3):

\[
S(P)\le\frac{1}{4\pi}\,m\cdot\frac{24L^{2}}{m^{2}}
     =\frac{6L^{2}}{\pi m}. \tag{7}
\]

Now the smallest possible \(m\) for a *convex* polyhedron is \(m=5\) (a triangular prism) – a tetrahedron has \(m=4\) but its faces are all triangles, which turns out to give a *larger* denominator in (7).  
Evaluating (7) for \(m=5\) yields

\[
S(P)\le\frac{6L^{2}}{5\pi}= \frac{6}{5\pi}\,L^{2}. \tag{8}
\]

--------------------------------------------------------------------

### 2.3  From surface area to volume  

Combine the spatial isoperimetric inequality (2) with the surface‑area bound (8):

\[
V(P)\le\frac{1}{6\sqrt{\pi}}\,\bigl(S(P)\bigr)^{3/2}
     \le\frac{1}{6\sqrt{\pi}}\Bigl

*Original question: [What is the largest volume of a polyhedron whose skeleton has total length 1? Is it the regular triangular prism?](https://math.stackexchange.com/questions/4044670/what-is-the-largest-volume-of-a-polyhedron-whose-skeleton-has-total-length-1-is) on Mathematics Stack Exchange, licensed CC BY-SA.*
