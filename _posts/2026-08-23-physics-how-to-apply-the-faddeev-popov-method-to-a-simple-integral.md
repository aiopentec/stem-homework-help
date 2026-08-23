---
layout: post
title: "How to apply the Faddeev-Popov method to a simple integral"
author: StemFix Bot
category: physics
tags: [physics]
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [this textbook](https://www.amazon.com/YOUR-ASSOCIATE-TAG).

---

## 1.  What the question is asking (in plain language)

The student wants to see **how the Faddeev‑Popov (FP) trick works on a really simple integral** that has a continuous redundancy, i.e. a “gauge symmetry”.  
The integral  

\[
I=\iint_{-\infty}^{\infty} e^{-(x^{2}+y^{2})}\;dx\,dy
\]

is invariant under **rotations in the \(x\!-\!y\) plane**  

\[
\begin{pmatrix}x\\y\end{pmatrix}\;\longrightarrow\;
R(\theta)\begin{pmatrix}x\\y\end{pmatrix},
\qquad 
R(\theta)=\begin{pmatrix}\cos\theta & -\sin\theta\\[2pt]
\sin\theta & \phantom{-}\cos\theta\end{pmatrix},
\]

so each point on a circle of radius \(r=\sqrt{x^{2}+y^{2}}\) is counted many times.  
The FP method tells us how to **factor out the infinite volume of the rotation group** (the “gauge‑orbit”) in a mathematically clean way.

We will:

1. Write the identity that implements the gauge fixing (the FP trick).  
2. Compute the FP determinant \(\Delta\).  
3. Insert the identity into the integral and carry out the integrals step‑by‑step.  
4. Show that we obtain the same result as the ordinary change to polar coordinates.

---

## 2.  Step‑by‑step solution

### 2.1  Identify the “gauge symmetry”

The transformation  

\[
(x,y)\;\to\;(x',y') = R(\theta)\,(x,y)
\]

leaves both the measure \(dx\,dy\) and the exponent \(-(x^{2}+y^{2})\) unchanged.  
Thus the **orbit** of a point is the whole circle of fixed radius \(r\).

### 2.2  Choose a gauge‑fixing condition

A convenient gauge condition is to **pick the point on each orbit that lies on the positive \(x\)‑axis**, i.e.

\[
F(x,y)\equiv \phi(x,y)=\arctan\frac{y}{x}=0 .
\]

Equivalently, we could demand \(y=0\) together with \(x>0\); the angular variable \(\phi\) is the most transparent choice.

### 2.3  Write the FP identity

For a continuous group \(G\) (here \(G=SO(2)\) with parameter \(\theta\in[0,2\pi)\)) the FP trick inserts

\[
1\;=\;\int_{0}^{2\pi}\!d\theta\;
\Delta(x,y)\;
\delta\!\bigl(F\bigl(R(\theta)\!(x,y)\bigr)\bigr) .
\tag{1}
\]

The **FP determinant** \(\Delta\) is defined as

\[
\Delta(x,y)\;=\;\Bigl|\frac{\partial}{\partial\theta}
F\bigl(R(\theta)\!(x,y)\bigr)\Bigr|_{\theta=0}.
\tag{2}
\]

---

### 2.4  Compute the determinant \(\Delta\)

Under a rotation the polar angle simply **shifts**:

\[
\phi\bigl(R(\theta)(x,y)\bigr)=\phi(x,y)+\theta .
\]

Therefore  

\[
\frac{\partial}{\partial\theta}
F\bigl(R(\theta)(x,y)\bigr)=\frac{\partial}{\partial\theta}
\bigl[\phi(x,y)+\theta\bigr]=1 .
\]

Hence  

\[
\boxed{\;\Delta(x,y)=1\;}
\]

(Any constant factor would cancel later; we can set it to 1.)

---

### 2.5  Insert the identity into the integral

Start from the original integral

\[
I=\int_{-\infty}^{\infty}\!dx\int_{-\infty}^{\infty}\!dy\;
e^{-(x^{2}+y^{2})}.
\]

Insert (1) with \(\Delta=1\):

\[
\begin{aligned}
I &=
\int dx\,dy\; e^{-(x^{2}+y^{2})}
\int_{0}^{2\pi}\!d\theta\;
\delta\!\bigl(\phi(R(\theta)(x,y))\bigr) .
\end{aligned}
\tag{3}
\]

Now change variables from Cartesian \((x,y)\) to **polar coordinates** \((r,\phi)\):

\[
x=r\cos\phi,\qquad y=r\sin\phi,\qquad 
dx\,dy = r\,dr\,d\phi .
\]

The exponent becomes \(-r^{2}\) and the measure acquires the Jacobian \(r\).  
Equation (3) reads

\[
\begin{aligned}
I &=
\int_{0}^{\infty}\!dr\int_{0}^{2\pi}\!d\phi\;
r\,e^{-r^{2}}
\int_{0}^{2\pi}\!d\theta\;
\delta\!\bigl(\phi+\theta\bigr) .
\end{aligned}
\tag{4}
\]

---

### 2.6  Perform the \(\phi\)–integration using the delta function

Because the integration range for \(\phi\) is the whole interval \([0,2\pi)\),

\[
\int_{0}^{2\pi} d\phi\;
\delta(\phi+\theta)=1 ,
\qquad\text{for any fixed }\theta .
\]

(Geometrically, the delta function picks the unique \(\phi\) that makes \(\phi+\theta=0\) modulo \(2\pi\); the integral over \(\phi\) therefore yields 1.)

After performing this integral (the \(\delta\) disappears) we are left with

\[
I = \int_{0}^{2\pi}\!d\theta
\int_{0}^{\infty}\!dr\; r\,e^{-r^{2}} .
\tag{5}
\]

---

### 2.7  Carry out the remaining integrals

* **\(\theta\)‑integral**: the integrand does not depend on \(\theta\),

\[
\int_{0}^{2\pi} d\theta = 2\pi .
\]

* **Radial integral**:

\[
\int_{0}^{\infty} r\,e^{-r^{2}}\,dr
= \frac12\int_{0}^{\infty} e^{-u}\,du
\quad (u=r^{2}) 
= \frac12 .
\]

Putting the two results together,

\[
I = 2\pi \times \frac12 = \boxed{\;\pi\;}.
\]

This is exactly the value obtained by the ordinary change to polar coordinates, confirming that the FP procedure correctly “divides out’’ the volume \(2\pi\) of the rotation group.

---

## 3.  Final answer

\[
\boxed{\,I=\displaystyle\iint_{\mathbb{R}^{2}} e^{-(x^{2}+y^{2})}\,dx\,dy = \pi\, } .
\]

The FP method reproduces the standard result by:

1. Inserting the identity (1) with the gauge condition \(\phi=0\).  
2. Finding the FP determinant \(\Delta=1\).  
3. Using the delta function to eliminate the redundant angular integration, leaving only a factor equal to the volume of the gauge group (\(2\pi\)).  

---

## 4.  Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to fix it |
|--------|----------------|--------------|
| **Forgetting the Jacobian when switching to polar coordinates** | The measure \(dx\,dy\)

*Original question: [How to apply the Faddeev-Popov method to a simple integral](https://physics.stackexchange.com/questions/221848/how-to-apply-the-faddeev-popov-method-to-a-simple-integral) on Physics Stack Exchange, licensed CC BY-SA.*
