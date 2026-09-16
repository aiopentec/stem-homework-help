---
layout: question
title: Choosing 5 of 13 Equally Spaced Points Guarantees an Isosceles Triangle
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Choosing 5 of 13 Equally Spaced Points
  Guarantees an Isosceles Triangle'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## Problem restated  

On a circle we mark the vertices of a regular 13‑gon (so the 13 points are equally spaced).  
Take **any** 5 of those vertices. Show that among the 5 chosen points there are three that are the
vertices of an isosceles triangle (i.e. two of the three sides have the same length).

---

## Full solution  

### 1.  Put the problem in a convenient language  

Number the 13 equally spaced points  

\[
0,1,2,\dots ,12 \pmod{13}
\]

clockwise around the circle.  
If we walk clockwise from a point \(i\) to a point \(j\) we pass a certain number of steps;
the chord length between \(i\) and \(j\) depends only on the *shorter* of the two arc lengths,
so it is the integer  

\[
\ell(i,j)=\min\{\,|j-i|,\;13-|j-i|\,\}\in\{1,2,\dots ,6\}.
\]

Thus two chords are equal **iff** the corresponding step numbers are equal.

--------------------------------------------------------------------

### 2.  Order the chosen points and look at the gaps  

Let the five chosen vertices be written in clockwise order  

\[
P_{1},P_{2},P_{3},P_{4},P_{5}.
\]

Define the *gaps* (numbers of steps between successive chosen points)  

\[
g_{1}=|P_{2}-P_{1}|,\;
g_{2}=|P_{3}-P_{2}|,\;
g_{3}=|P_{4}-P_{3}|,\;
g_{4}=|P_{5}-P_{4}|,\;
g_{5}=13-|P_{5}-P_{1}|.
\]

All \(g_{k}\) are positive integers and, because we have gone once all the way round the circle,

\[
\boxed{g_{1}+g_{2}+g_{3}+g_{4}+g_{5}=13}\tag{1}
\]

--------------------------------------------------------------------

### 3.  When do we obtain an isosceles triangle?  

Look at a vertex, say \(P_{2}\).  
The two sides that meet at \(P_{2}\) are the chords joining \(P_{2}\) with its neighbours
\(P_{

*Original question: [Choosing 5 of 13 Equally Spaced Points Guarantees an Isosceles Triangle](https://math.stackexchange.com/questions/5149506/choosing-5-of-13-equally-spaced-points-guarantees-an-isosceles-triangle) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
