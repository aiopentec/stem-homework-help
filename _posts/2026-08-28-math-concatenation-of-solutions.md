---
layout: question
title: Concatenation of solutions
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Concatenation of solutions'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking (in plain language)

We have a first‑order autonomous‑in‑t ODE  

\[
u'(t)=\alpha(t)\,g\bigl(u(t)\bigr),\qquad t\in I\subset\mathbb R,
\]

where  

* \(\alpha : I_{1}\to\mathbb R\) and \(g : I_{2}\to\mathbb R\) are **continuous**,  
* \(I_{1},I_{2}\) are intervals, and  
* there is a special value \(u_{0}\in I_{2}\) with \(g(u_{0})=0\) (an equilibrium).

Two *partial* solutions are given:

* \(\varphi_{1}:(a,b_{1})\to I_{2}\) solves the ODE on \((a,b_{1})\) and approaches the equilibrium as \(t\to b_{1}^{-}\);
* \(\varphi_{2}:(b_{2},c)\to I_{2}\) solves the ODE on \((b_{2},c)\) and approaches the equilibrium as \(t\to b_{2}^{+}\).

The intervals may overlap at a single point (\(b_{1}=b_{2}\)) or be disjoint (\(b_{1}<b_{2}\)).  

We are asked to **glue** the two solutions together, staying at the equilibrium on the “gap’’ \([b_{1},b_{2}]\), and to prove that the resulting function

\[
\varphi(t)=
\begin{cases}
\displaystyle \varphi_{1}(t), & a<t<b_{1},\\[4pt]
u_{0},                           & b_{1}\le t\le b_{2},\\[4pt]
\displaystyle \varphi_{2}(t), & b_{2}<t<c,
\end{cases}
\]

is itself a (global) solution of the same ODE on the whole interval \((a,c)\).

In other words, we must show that \(\varphi\) is **continuous** on \((a,c)\) and **differentiable** at every point, with derivative satisfying  

\[
\varphi'(t)=\alpha(t)\,g\bigl(\varphi(t)\bigr)\qquad\text{for all }t\in(a,c).
\]

The only delicate points are the “junction’’ points \(b_{1}\) and \(b_{2}\); everywhere else \(\varphi\) coincides with a known solution, so the ODE is already satisfied there.

---

## 2.  Detailed proof

### 2.1  Extend the two given solutions to the endpoints

Define the *extended* functions  

\[
\tilde\varphi_{1}:[a,b_{1}]\to I_{2},\qquad 
\tilde\varphi_{2}:[b_{2},c]\to I_{2}
\]

by  

\[
\tilde\varphi_{1}(t)=
\begin{cases}
\varphi_{1}(t), & a<t<b_{1},\\
u_{0},          & t=b_{1},
\end{cases}
\qquad
\tilde\varphi_{2}(t)=
\begin{cases}
u_{0},          & t=b_{2},\\
\varphi_{2}(t), & b_{2}<t<c.
\end{cases}
\]

Because \(\displaystyle \lim_{t\to b_{1}^{-}}\varphi_{1}(t)=u_{0}\) and
\(\displaystyle \lim_{t\to b_{2}^{+}}\varphi_{2}(t)=u_{0}\), the extensions are **continuous** at the added endpoints.

### 2.2  Continuity of \(\varphi\) on \((a,c)\)

By construction \(\varphi\) equals \(\tilde\varphi_{1}\) on \((a,b_{1}]\), equals the constant \(u_{0}\) on \([b_{1},b_{2}]\), and equals \(\tilde\varphi_{2}\) on \([b_{2},c)\).  
All three pieces are continuous, and they match at the joining points:
\[
\tilde\varphi_{1}(b_{1})=u_{0}=\tilde\varphi_{2}(b_{2}).
\]
Hence \(\varphi\) is continuous on the whole interval \((a,c)\).

### 2.3  Differentiability away from the junction points

*If \(t\in (a,b_{1})\)*, then \(\varphi(t)=\varphi_{1}(t)\). Since \(\varphi_{1}\) solves the ODE,  

\[
\varphi'(t)=\varphi_{1}'(t)=\alpha(t)g\bigl(\varphi_{1}(t)\bigr)
          =\alpha(t)g\bigl(\varphi(t)\bigr).
\]

*If \(t\in (b_{2},c)\)*, the same argument with \(\varphi_{2}\) gives the identity.

*If \(t\in (b_{1},b_{2})\)*, \(\varphi(t)\equiv u_{0}\) is constant, so \(\varphi'(t)=0\). Because \(g(u_{0})=0\),

\[
\alpha(t)g\bigl(\varphi(t)\bigr)=\alpha(t)g(u_{0})=0=\varphi'(t).
\]

Thus the ODE holds everywhere except possibly at \(b_{1}\) and \(b_{2}\).

### 2.4  Differentiability at \(b_{1}\)

We compute the derivative from the definition.  
Recall that \(\varphi(b_{1})=u_{0}\).

#### Left‑hand limit (\(h<0\))

\[
\frac{\varphi(b_{1}+h)-\varphi(b_{1})}{h}
    =\frac{\varphi_{1}(b_{1}+h)-u_{0}}{h},\qquad h\in(-\varepsilon,0).
\]

Because \(\varphi_{1}\) is differentiable on \((a,b_{1})\), the **Mean Value Theorem** provides a point \(\xi_{h}\in(b_{1}+h,b_{1})\) such that

\[
\frac{\varphi_{1}(b_{1}+h)-u_{0}}{h}= \varphi_{1}'(\xi_{h}).
\]

Since \(h\to0^{-}\) forces \(\xi_{h}\to b_{1}\) and \(\varphi_{1}'\) has a finite limit at \(b_{1}\) (see below), we obtain

\[
\lim_{h\to0^{-}}\frac{\varphi(b_{1}+h)-\varphi(b_{1})}{h}
   =\lim_{h\to0^{-}}\varphi_{1}'(\xi_{h})
   =\lim_{t\to b_{1}^{-}}\varphi_{1}'(t).
\]

Now \(\varphi_{1}\) satisfies the ODE on \((a,b_{1})\); thus for every \(t\in(a,b_{1})\),

\[
\varphi_{1}'(t)=\alpha(t)g\bigl(\varphi_{1}(t)\bigr).
\]

Take the limit as \(t\to b_{1}^{-}\). By continuity of \(\alpha\) and \(g\) and because \(\varphi_{1}(t)\to u_{0}\),

\[
\lim_{t\to b_{1}^{-}}\varphi_{1}'(t)
   =\alpha(b_{1})\,g(u_{0})=0.
\]

Hence the left‑hand derivative at \(b_{1}\) exists and equals \(0\).

#### Right‑hand limit (\(h>0\))

Two cases.

*If \(b_{1}<b_{2}\)*, then for every sufficiently small \(h>0\) we have
\(b_{1}+h\in[b_{1},b_{2}]\), and \(\varphi(b_{1}+h)=u_{0}\). Consequently

\[
\frac{\varphi(b_{1}+h)-\varphi(b_{1})}{h}=0,
\]
so the right‑hand derivative is \(0\).

*If \(b_{1}=b_{2}\)*, then for \(h>0\) small we are in the interval \((b_{2},c)\) and
\(\varphi(b_{1}+h)=\varphi_{2}(b_{2}+h)\). By the same mean‑value argument as above,

\[
\frac{\varphi(b_{1}+h)-\varphi(b_{1})}{h}
   =\varphi_{2}'(\eta_{h}),\qquad \eta_{h}\in(b_{2},b_{2}+h).
\]

Letting \(h\to0^{+}\) gives \(\eta_{h}\to b_{2}\) and, using the ODE for \(\varphi_{2}\),

\[
\lim_{h\to0^{+}}\varphi_{2}'(\eta_{h})
   =\alpha(b_{2})\,g(u_{0})=0.
\]

Thus the right‑hand derivative is also \(0\).

Since the left and right limits coincide, \(\varphi\) is differentiable at \(b_{1}\) with

\[
\boxed{\;\varphi'(b_{1})=0=\alpha(b_{1})g\bigl(\varphi(b_{1})\bigr)\; }.
\]

### 2.5  Differentiability at \(b_{2}\)

The argument is completely symmetric.  
If \(b_{1}<b_{2}\) the left side uses the constant part \(u_{0}\), giving derivative \(0\).  
If \(b_{1}=b_{2}\) we apply the mean‑value theorem to \(\varphi_{1}\) on the left. In all cases we obtain

\[
\boxed{\;\varphi'(b_{2})=0=\alpha(b_{2})g\bigl(\varphi(b_{2})\bigr)\; }.
\]

### 2.6  Conclusion

We have shown that

* \(\varphi\) is continuous on \((a,c)\);
* \(\varphi\) is differentiable at every point of \((a,c)\);
* the derivative satisfies the differential equation everywhere:

\[
\varphi'(t)=\alpha(t)g\bigl(\varphi(t)\bigr),\qquad \forall\,t\in(a,c).
\]

Hence **\(\varphi\) is a solution of the ODE on the whole interval \((a,c)\)**, i.e. the two partial solutions can indeed be concatenated through the equilibrium value \(u_{0}\).

---

## 3.  Final answer

The piecewise‑defined function  

\[
\varphi(t)=
\begin{cases}
\varphi_{1}(t), & a<t<b_{1},\\[2mm]
u_{0},          & b_{1}\le t\le b_{2},\\[2mm]
\varphi_{2}(t), & b_{2}<t<c,
\end{cases}
\]

is a **global solution** of the differential equation  

\[
u'(t)=\alpha(t)g\bigl(u(t)\bigr)
\]

on the interval \((a,c)\). The crucial points \(b_{1}\) and \(b_{2}\) are differentiable with derivative \(0\) because the right‑hand side of the ODE vanishes at the equilibrium \(u_{0}\) (\(g(u_{0})=0\)).

---

## 4.  Common mistakes to avoid

| Mistake | Why it’s wrong | How to fix it |
|---|---|---|
| **Assuming differentiability at \(b_{1},b_{2}\) without proof.** | The function changes definition there; one must check the limit of the difference quotient. | Use the definition of derivative, or the Mean Value Theorem, as done above. |
| **Using \(\varphi_{1}'(b_{1})\) or \(\varphi_{2}'(b_{2})\) directly.** | The original solutions are not defined *at* the endpoints, so those derivatives are not given a priori. | Take limits of \(\varphi_{1}'(t)\) as \(t\to b_{1}^{-}\) (and similarly for \(\varphi_{2}\)). |
| **Ignoring the continuity of \(\alpha\) and \(g\).** | Without continuity we cannot pass limits through \(\alpha(t)g(\varphi(t))\). | Explicitly invoke continuity when computing \(\displaystyle\lim_{t\to b_{1}^{-}}\alpha(t)g(\varphi_{1}(t))\). |
| **Confusing the “gap’’ \([

*Original question: [Concatenation of solutions](https://math.stackexchange.com/questions/5148125/concatenation-of-solutions) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
