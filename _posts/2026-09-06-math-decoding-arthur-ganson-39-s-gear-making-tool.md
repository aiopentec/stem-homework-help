---
layout: question
title: Decoding Arthur Ganson&#39;s gear-making tool
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Decoding Arthur Ganson&#39;s gear-making
  tool'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

Arthur Ganson’s “wire‑gear” jig (the picture in **Image 1**) lets a maker set three things that completely describe a regular star‑shaped gear:

| What we want to set | What the jig does |
|---------------------|-------------------|
| **J** – the angle at the *base* of each point (the “inner” angle) | The two fixed stops **F₁** and **F₂** keep a sliding arm at a fixed angle. |
| **K** – the angle at the *tip* of each point (the “outer” angle) | The same two stops also define the tip angle because the arm is a straight ruler. |
| **L** – the length of each arm (distance from the centre of the gear to the tip) | A movable stop that can be placed in one of the holes **B₁ … B₅** (in the picture they are labelled B1‑B5) fixes the distance of the arm from the centre. |
| **n** – the number of points (or “arms”) on the star | Determined by the angular spacing **K**; the jig does not have a separate “n‑dial”, the number of points follows automatically once **K** is chosen. |

The question is:

*How are the three geometric quantities **J, K, L** related to each other, and how does the jig actually produce a star with a chosen number of points?*  

In addition we have to explain what the three groups of holes **C**, **D**, **E** are for.

---

## 2.  Geometry of a regular star gear

### 2.1  Basic picture

Consider a regular star with **n** identical points (the same shape repeats all the way around).  
Pick one point and draw the two straight “arms” that form the point.  
Let

* **O** be the centre of the gear,
* **T** the tip of the point,
* **B₁**, **B₂** the two base points where the arm meets the inner circle.

```
               T
            /     \
          /         \
        B₁-----------B₂
           \       /
                O
```

The important angles are

* **K** – the *tip* angle ∠B₁TB₂,
* **J** – the *base* angle ∠OB₁T = ∠OB₂T (the two are equal by symmetry).

The arm length (the distance from the centre to the tip) is **L** = |OT|.

### 2.2  Relationship between the angles

Because the triangle **OB₁T** is isosceles (|OB₁| = |OB₂| = radius of the inner circle), the two base angles are equal:

\[
J = \frac{\pi - K}{2}\qquad\text{(radians)}
\]

or, in degrees,

\[
\boxed{J = \frac{180^{\circ} - K}{2}} .
\]

Thus **J** and **K** are *not* independent – fixing one automatically fixes the other.

### 2.3  Number of points \(n\)

When the star repeats, the tip angles of consecutive points fill the whole circle:

\[
n\,K = 2\pi\quad\Longrightarrow\quad
\boxed{n = \frac{2\pi}{K}} .
\]

Equivalently, in degrees,

\[
n = \frac{360^{\circ}}{K}.
\]

So the *number of points* is determined entirely by the tip angle **K** (or, by the previous formula, by the base angle **J**).

### 2.4  Length \(L\)

The jig’s sliding arm is a straight ruler that pivots about the centre **O**.  
When the arm is locked in a hole **Bₖ** (the five holes in the picture) its end lies at a distance **L** from the centre.  
Thus the chosen hole simply *sets* the length:

\[
\boxed{L = \text{distance from O to the chosen B‑hole}} .
\]

No trigonometry is needed for the length – it is a pure radial measurement.

---

## 3.  How the jig implements the geometry

| Part of the jig | What it does | How it creates the required geometry |
|-----------------|--------------|--------------------------------------|
| **F₁, F₂** (fixed stops) | Keep the sliding arm at a fixed *opening* | The two stops are spaced at the exact distance that forces the arm to make the tip angle **K**. Because the arm is a rigid straight line, the angle between the two lines drawn from the centre to the stops is exactly **K**. |
| **H₁** (the “follower” that slides in hole **A**) | Forces the wire to follow the arm while it pivots | As the arm rotates, the tip of the wire is forced to stay on the arm, guaranteeing that the wire’s tip angle is exactly the same as the arm’s opening **K**. |
| **H₂** (the bending pin) | Gives the wire its curvature at the base | While the arm is held, H₂ pushes the wire against the inner circle, producing the base angle **J** (which, as shown, is forced automatically once **K** is fixed). |
| **B₁…B₅** (holes on the radial bar) | Choose the arm length | Placing the movable stop in a particular hole fixes the radial distance **L**. Different holes give different arm lengths, producing longer or shorter points. |
| **C, D, E** (sets of three equally‑spaced holes) | Allow the whole assembly to be *re‑scaled* while preserving the angle | By moving the entire arm to a different set of holes (C, D or E) you change the *lever arm* that the fixed stops act on. The ratio of the distance between F₁/F₂ to the distance from O to the wire tip stays the same, so the **angles** stay unchanged while the whole star is enlarged or reduced. In practice the artist uses the three sets to make very small, medium, or large gears without having to change the stops. |
| **(optional) extra pins on the rim** | Fine‑tune the inner radius | Some versions of the tool have extra pins that can be inserted in the rim to change the radius of the inner circle, again without changing **J** or **K**. |

### 3.1  Summary of the workflow

1. **Choose the number of points** \(n\).  
   Compute the required tip angle \(K = 360^{\circ}/n\).  
   Adjust the fixed stops **F₁,F₂** (or pick the jig that already has that spacing) so that the arm opening equals \(K\).

2. **Pick the point length** \(L\).  
   Insert the radial stop into the appropriate hole **Bₖ** (or into a different set C/D/E for a larger scale). The distance from the centre to that hole is exactly the desired \(L\).

3. **Bend the wire**.  
   The sliding follower **H₁** runs along the arm, the bending pin **H₂** pushes the wire against the inner circle, and the wire automatically acquires the base angle  

   \[
   J = \frac{180^{\circ}-K}{2}.
   \]

4. **Result** – a perfectly regular star gear with the chosen number of points, point length, and sharpness.

---

## 4.  Final formulas (the “answers”)

| Quantity | Formula (degrees) | Formula (radians) |
|----------|-------------------|-------------------|
| Tip angle **K** (given \(n\)) | \(K = \dfrac{360^{\circ}}{n}\) | \(K = \dfrac{2\pi}{n}\) |
| Base angle **J** (from **K**) | \(J = \dfrac{180^{\circ}-K}{2}\) | \(J = \dfrac{\pi-K}{2}\) |
| Number of points **n** (from **K**) | \(n = \dfrac{360^{\circ}}{K}\) | \(n = \dfrac{2\pi}{K}\) |
| Arm length **L** | Chosen by the radial stop (distance O–B‑hole) | – |
| Scaling sets **C, D, E** | Multiply all linear dimensions by the ratio of the chosen set to the original set; angles stay the same | – |

---

## 5.  Common mistakes when solving this kind of problem

| Mistake | Why it happens | How to avoid it |
|---------|----------------|-----------------|
| **Treating \(J\) and \(K\) as independent** | Forgetting that the two angles belong to the same isosceles triangle. | Write down the triangle **OB₁T** and use the angle‑sum rule \(2J + K = 180^{\circ}\) (or \(\pi\) radians) first. |
| **Using the interior angle of a regular polygon instead of the tip angle** | The star’s points are not the interior angles of an \(n\)-gon; they are the *exterior* angles at the tips. | Remember that the whole circle (360°) is divided into the *tip* angles, not the interior angles of the polygon formed by the base points. |
| **Confusing the radius of the inner circle with the arm length \(L\)** | Both are radial distances, but only one (the distance to the chosen B‑hole) matters for the point length. | Keep a clear diagram: label the inner‑circle radius \(r\) and the arm length \(L\); they are unrelated for the geometry of the point shape. |
| **Ignoring the scaling sets C, D, E** | Assuming the jig only works for one size. | Recognise that moving the whole arm to a different set multiplies every linear dimension by a constant factor, leaving the angles unchanged. |
| **Mixing degrees and radians** | Plugging a degree value into a radian‑based formula (or vice‑versa). | Decide at the start which unit you will use and stay consistent. Convert with \(180^{\circ}= \pi\) rad if needed. |

--- 

**Bottom line:**  
The jig fixes the *angular* shape of a star gear by forcing the tip angle **K** (hence the base angle **J**) with the two stops **F₁,F₂**; the *size* of the gear is set by the radial stop in the B‑holes (and optionally by moving to the C/D/E sets). The number of points follows directly from \(n = 360^{\circ}/K\). With these simple relationships the artist can produce any regular wire‑gear he desires.

*Original question: [Decoding Arthur Ganson&#39;s gear-making tool](https://math.stackexchange.com/questions/5148773/decoding-arthur-gansons-gear-making-tool) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
