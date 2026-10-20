---
layout: question
title: Is this characterization of Neuberg cubic a new one?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Is this characterization of Neuberg
  cubic a new one?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

For a given reference triangle \(ABC\) we do the following construction for an arbitrary point
\(M\) in the plane.

* Let \(I_{A},I_{B},I_{C}\) be the mid‑points of the segments \(MA,MB,MC\).
* Draw the **perpendicular bisector** of \(MA\); it meets the side \(BC\) at a point we call \(D\).  
  (Analogously we obtain \(E\in CA\) from the perpendicular bisector of \(MB\) and
  \(F\in AB\) from the perpendicular bisector of \(MC\).)

The claim to be proved is  

> **The triangle \(DEF\) is degenerate (the three points are collinear)  
>  if and only if the point \(M\) lies on the Neuberg cubic of \(\triangle ABC\).**

In other words, the locus of all points \(M\) for which the three
perpendicular‑bisector intersections are collinear is precisely the Neuberg
cubic.  

We have to give a complete proof of this equivalence and indicate that the
result is a known description of the Neuberg cubic.

--------------------------------------------------------------------

## 2.  Proof  

### 2.1  A useful algebraic identity  

Denote by \(\vec{XY}\) the vector \(\overrightarrow{XY}\).  
If \(I_{A}\) is the midpoint of \(MA\) then

\[
\boxed{\;2\;\vec{MA}\!\cdot\!\vec{BI_{A}} = AB^{2}-BM^{2}\;}\qquad(1a)
\]
\[
\boxed{\;2\;\vec{MA}\!\cdot\!\vec{CI_{A}} = AC^{2}-CM^{2}\;}\qquad(1b)
\]

*Proof.*  
Write \(\vec{BI_{A}}=\dfrac{\vec{BA}+\vec{BM}}{2}\) and \(\vec{CI_{A}}=
\dfrac{\vec{CA}+\vec{CM}}{2}\).  Then

\[
\begin{aligned}
2\vec{MA}\!\cdot\!\vec{BI_{A}}
   &=\vec{MA}\!\cdot\!(\vec{BA}+\vec{BM})   \\
   &=(\vec{MA}\!\cdot\!\vec{BA})+(\vec{MA}\!\cdot\!\vec{BM})\\
   &=(\vec{CA}-\vec{CM})\!\cdot\!(\vec{CA}+\vec{CM})
      \quad(\text{since }\vec{MA}=\vec{CA}-\vec{CM})\\
   &=CA^{2}-CM^{2}=AB^{2}-BM^{2},
\end{aligned}
\]

which is (1a).  The second identity is obtained in the same way. ∎  

These two relations will be used repeatedly.

--------------------------------------------------------------------

### 2.2  The point \(D\) in terms of \(M\)

Because \(D\) lies on the **perpendicular bisector** of \(MA\) we have

\[
\vec{DA}\!\cdot\!\vec{MA}=0\qquad\text{and}\qquad AD=MD .
\tag{2}
\]

The first condition can be written as  

\[
(\vec{DB}+\vec{BA})\!\cdot\!\vec{MA}=0,
\]

i.e.

\[
\vec{DB}\!\cdot\!\vec{MA}= -\vec{BA}\!\cdot\!\vec{MA}.
\tag{3}
\]

Write \(\vec{DB}=t\,( \vec{BC})\) where \(t=\dfrac{BD}{BC}\) (so \(0<t<1\) when
\(D\) is between \(B\) and \(C\)).  Using (3) we obtain  

\[
t\,\vec{BC}\!\cdot\!\vec{MA}= -\vec{BA}\!\cdot\!\vec{MA}.
\]

Now \(\vec{BC}= \vec{BI_{A}}-\vec{CI_{A}}\); substituting this and employing the
identities (1a)–(1b) gives  

\[
t\bigl[(AB^{2}-BM^{2})-(AC^{2}-CM^{2})\bigr]=AB^{2}-BM^{2}.
\]

Consequently

\[
\boxed{\displaystyle\frac{BD}{DC}= 
\frac{AB^{2}-BM^{2}}{AC^{2}-CM^{2}}}\qquad(4)
\]

(and the analogous formulas for the other two sides).

--------------------------------------------------------------------

### 2.3  Menelaus’ theorem for \(\triangle ABC\) and the transversal \(D\!-\!E\!-\!F\)

The three points \(D\in BC,\;E\in CA,\;F\in AB\) are collinear **iff**
the Menelaus product equals \(1\):

\[
\frac{BD}{DC}\cdot\frac{CE}{EA}\cdot\frac{AF}{FB}=1 .
\tag{5}
\]

Insert the three ratios obtained in (4) (and the two cyclic permutations)
into (5).  After a short cancellation we obtain

\[
\frac{AB^{2}-BM^{2}}{AB^{2}-AM^{2}}\;
\frac{BC^{2}-CM^{2}}{BC^{2}-BM^{2}}\;
\frac{CA^{2}-AM^{2}}{CA^{2}-CM^{2}}=1 .
\tag{6}
\]

Multiplying the numerators and denominators gives the equivalent condition

\[
\boxed{(AB^{2}-BM^{2})(BC^{2}-CM^{2})(CA^{2}-AM^{2})
      =(AB^{2}-AM^{2})(BC^{2}-BM^{2})(CA^{2}-CM^{2}) } .
\tag{7}
\]

Equation (7) is a **cubic equation** in the three numbers
\(MA^{2},\,MB^{2},\,MC^{2}\); it is the analytic equation of the Neuberg
cubic.

--------------------------------------------------------------------

### 2.4  Recognising the Neuberg cubic  

Let the barycentric coordinates of the variable point \(M\) with respect to
\(\triangle ABC\) be \((x:y:z)\) (\(x+y+z=1\)).  The well‑known formulae for the
squared distances from \(M\) to the vertices are  

\

*Original question: [Is this characterization of Neuberg cubic a new one?](https://math.stackexchange.com/questions/5152373/is-this-characterization-of-neuberg-cubic-a-new-one) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
