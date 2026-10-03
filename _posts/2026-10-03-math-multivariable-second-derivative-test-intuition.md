---
layout: question
title: Multivariable Second Derivative Test Intuition
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Multivariable Second Derivative Test
  Intuition'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1. What the problem is asking  

We are asked to **justify the classic second‑derivative (Hessian) test for a function of two variables**  

\[
f:\mathbb R^{2}\to\mathbb R ,\qquad (x,y)\mapsto f(x,y)
\]

and to explain why, when the first‑order partial derivatives vanish at a point \((a,b)\),

* the point is a **local minimum** if the quadratic form defined by the Hessian matrix is **positive‑definite**, i.e.  

  \[
  \mathbf u^{T}H_f(a,b)\,\mathbf u>0\quad\text{for every non‑zero direction }\mathbf u\in\mathbb R^{2},
  \]

* and that this condition is equivalent to the two scalar inequalities  

  \[
  f_{xx}(a,b)>0 ,\qquad 
  \det H_f(a,b)=f_{xx}(a,b)f_{yy}(a,b)-f_{xy}(a,b)^{2}>0 .
  \]

The same reasoning (with “\( <0\)” instead of “\( >0\)”) yields the criterion for a local maximum, and if the quadratic form is indefinite the point is a saddle.

---

## 2. Step‑by‑step justification  

### 2.1.  Critical points – why \(\nabla f(a,b)=\mathbf 0\)  

For a differentiable function \(f\) the **directional derivative** in direction \(\mathbf u\) (with \(\|\mathbf u\|=1\)) is  

\[
D_{\mathbf u}f(a,b)=\nabla f(a,b)\cdot\mathbf u .
\]

If \((a,b)\) is a local extremum (maximum or minimum) then the slope in **every** direction must be zero; otherwise we could move a tiny amount in a direction where the slope is non‑zero and obtain a larger (or smaller) value of \(f\).  

Hence at an extremum  

\[
D_{\mathbf u}f(a,b)=0\quad\text{for all }\mathbf u\Longrightarrow \nabla f(a,b)=\mathbf 0 .
\]

The equations \(\partial f/\partial x=0,\;\partial f/\partial y=0\) are called the **first‑order conditions**; their solutions are the **critical points**.

---

### 2.2.  The second‑order (Hessian) expansion  

Assume that \(f\) has continuous second partial derivatives near \((a,b)\).  
Taylor’s theorem with remainder (in vector form) gives, for a small displacement \(\mathbf h=(h_1,h_2)^{T}\),

\[
f(a+\mathbf h)=f(a,b)+\underbrace{\nabla f(a,b)^{T}\mathbf h}_{=0}
+\tfrac12\,\mathbf h^{T} H_f(a,b)\,\mathbf h
+o(\|\mathbf h\|^{2}),
\]

where  

\[
H_f(a,b)=
\begin{bmatrix}
f_{xx}(a,b) & f_{xy}(a,b)\\[2pt]
f_{yx}(a,b) & f_{yy}(a,b)
\end{bmatrix}
\quad\text{(the Hessian matrix).}
\]

Because the first‑order term vanishes at a critical point, the **quadratic term**  

\[
Q(\mathbf h)=\tfrac12\,\mathbf h^{T} H_f(a,b)\,\mathbf h
\]

dominates the behaviour of \(f\) near \((a,b)\).  
If \(Q(\mathbf h)>0\) for every non‑zero \(\mathbf h\), then for sufficiently small \(\|\mathbf h\|\) we have  

\[
f(a+\mathbf h)-f(a,b)=Q(\mathbf h)+o(\|\mathbf h\|^{2})>0,
\]

so the function is larger in every nearby direction → **local minimum**.  
Similarly, \(Q(\mathbf h)<0\) for all non‑zero \(\mathbf h\) gives a **local maximum**.  
If \(Q\) takes both positive and negative values, the point is a **saddle**.

Thus the problem reduces to deciding when the quadratic form  

\[
\mathbf h^{T} H_f(a,b)\,\mathbf h
\]

is **positive‑definite**, **negative‑definite**, or **indefinite**.

---

### 2.3.  Positive‑definiteness of a \(2\times 2\) symmetric matrix  

The Hessian is symmetric (\(f_{xy}=f_{yx}\)).  
For a symmetric \(2\times 2\) matrix  

\[
A=
\begin{bmatrix}
\alpha & \beta\\
\beta & \gamma
\end{bmatrix},
\]

the following are equivalent:

| Condition | Meaning |
|-----------|---------|
| (i) \(\displaystyle \mathbf v^{T}A\mathbf v>0\) for all non‑zero \(\mathbf v\in\mathbb R^{2}\) | \(A\) is **positive‑definite** |
| (ii) \(\alpha>0\) **and** \(\det A>0\) | Simple scalar test (Sylvester’s criterion) |
| (iii) Both eigenvalues of \(A\) are positive | Spectral view |

*Proof of the equivalence (ii) ⇔ (i):*  

Take \(\mathbf v=(v_1,0)^{T}\). Then \(\mathbf v^{T}A\mathbf v=\alpha v_1^{2}>0\) for all \(v_1\neq0\) forces \(\alpha>0\).  

Now write the quadratic form in “completed‑square” form:

\[
\mathbf v^{T}A\mathbf v
= \alpha\Bigl(v_1+\frac{\beta}{\alpha}v_2\Bigr)^{2}
+\Bigl(\gamma-\frac{\beta^{2}}{\alpha}\Bigr)v_2^{2}
= \alpha\bigl(\cdots\bigr)^{2}
+\frac{\det A}{\alpha}v_2^{2}.
\]

If \(\alpha>0\) then the sign of the whole expression is governed by the second term.  
Thus the form is always positive **iff** \(\displaystyle\frac{\det A}{\alpha}>0\), i.e. \(\det A>0\).

Consequently, for the Hessian  

\[
H_f(a,b)=\begin{bmatrix}
f_{xx} & f_{xy}\\
f_{xy} & f_{yy}
\end{bmatrix},
\]

the condition  

\[
\mathbf h^{T}H_f(a,b)\,\mathbf h>0\quad\forall\ \mathbf h\neq\mathbf0
\]

is **exactly**  

\[
\boxed{\,f_{xx}(a,b)>0\quad\text{and}\quad 
f_{xx}(a,b)f_{yy}(a,b)-f_{xy}(a,b)^{2}>0\, } .
\]

These are the familiar **second‑derivative test** inequalities for a local minimum.  

The analogous condition for a local maximum is

\[
f_{xx}(a,b)<0\quad\text{and}\quad 
f_{xx}(a,b)f_{yy}(a,b)-f_{xy}(a,b)^{2}>0,
\]

i.e. the Hessian is **negative‑definite** (both eigenvalues negative).

If the determinant is negative, the quadratic form takes both signs and the critical point is a saddle.

---

### 2.4.  Summary of the full test  

1. **First‑order test** – solve  

   \[
   f_{x}(a,b)=0,\qquad f_{y}(a,b)=0 .
   \]

   Any solution \((a,b)\) is a *critical point*.

2. **Second‑order test** – compute the Hessian at the critical point and evaluate  

   \[
   D = f_{xx}(a,b)f_{yy}(a,b)-f_{xy}(a,b)^{2}.
   \]

   * If \(f_{xx}(a,b)>0\) **and** \(D>0\) → **local minimum**.  
   * If \(f_{xx}(a,b)<0\) **and** \(D>0\) → **local maximum**.  
   * If \(D<0\) → **saddle point** (neither max nor min).  
   * If \(D=0\) → the test is **inconclusive**; higher‑order analysis is needed.

---

## 3. Final Answer  

For a twice‑continuously differentiable function \(f(x,y)\) :

*A point \((a,b)\) with \(\nabla f(a,b)=\mathbf 0\) is a **local minimum** iff the Hessian matrix at that point is positive‑definite, which for a \(2\times2\) Hessian is equivalent to*

\[
\boxed{\;f_{xx}(a,b)>0\quad\text{and}\quad
f_{xx}(a,b)f_{yy}(a,b)-f_{xy}(a,b)^{2}>0\; } .
\]

The analogous inequalities with “\( <0\)” give a local maximum; a negative determinant signals a saddle point.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Forgetting the first‑order condition** and applying the Hessian test at a point where \(\nabla f\neq\mathbf0\). | The quadratic approximation assumes the linear term is zero; otherwise the sign of the linear term dominates. | Always verify \(\partial f/\partial x=\partial f/\partial y=0\) before using the second‑derivative test. |
| **Using only \(f_{xx}>0\) (or \(f_{yy}>0\)) as a test**. | Positivity of a single second partial does not guarantee the quadratic form is positive for all directions. | Check both \(f_{xx}>0\) *and* the determinant condition \(D>0\). |
| **Confusing “\(D>0\)” with “\(f_{xx}>0\)”**. | Either condition alone is insufficient; both are needed for definiteness. | Remember Sylvester’s criterion: *all leading principal minors* must be positive for positive‑definiteness. |
| **Assuming the test is decisive when \(D=0\)**. | When the determinant vanishes the quadratic form is degenerate; the point could be min, max, or saddle. | Treat \(D=0\) as “inconclusive” and examine higher‑order terms or use other methods (e.g., analyzing level curves). |
| **Mixing up the sign of \(f_{xx}\) for minima vs. maxima**. | The sign of \(f_{xx}\) determines whether the Hessian is positive or negative definite, not the determinant. | For minima: require \(f_{xx}>0\); for maxima: require \(f_{xx}<0\); in both cases the determinant must be positive. |

Keeping these points in mind will help you apply the multivariable second‑derivative test correctly and interpret its outcome with confidence.

*Original question: [Multivariable Second Derivative Test Intuition](https://math.stackexchange.com/questions/5150989/multivariable-second-derivative-test-intuition) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
