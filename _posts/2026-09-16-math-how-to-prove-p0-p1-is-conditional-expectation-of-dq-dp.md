---
layout: question
title: how to prove p0/p1 is conditional expectation of dq/dp
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: how to prove p0/p1 is conditional
  expectation of dq/dp'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What has to be shown?  

We have two probability measures on the same filtered space  

* **\( \mathbb P\)** – the original law of the diffusion  
  \[
  \begin{cases}
  dX_t^1 = u(X_t^1,X_t^2)\,dt + dB_t ,\\[2mm]
  dX_t^2 = X_t^1\,dt ,\qquad X_0=(x^1,x^2)=x .
  \end{cases}
  \]

* **\( \mathbb Q\)** – the measure obtained from \(\mathbb P\) by the Girsanov density  

  \[
  M_t:=\exp\!\Bigl(-\int_0^t u(X_s)\,dB_s-\frac12\int_0^t|u(X_s)|^2ds\Bigr),
  \qquad 
  \frac{d\mathbb Q}{d\mathbb P}\Big|_{\mathcal F_t}=M_t .
  \]

Under \(\mathbb P\) the random vector \(X_t\) has a **density** \(p_1(t,x,z)\) w.r.t. Lebesgue measure \(dz\); under \(\mathbb Q\) it has the **Kolmogorov density** \(p_0(t,x,z)\).  

The problem asks to prove, **for \(p_1(t,x,\cdot)\,dz\)-almost every \(z\)**,

\[
\boxed{\;\; \mathbb E_{\mathbb P}\!\bigl[\,M_t\mid X_t = z \bigr]=\frac{p_0(t,x,z)}{p_1(t,x,z)} \; } .
\]

In words: the conditional expectation of the Girsanov density given the terminal state equals the ratio of the two transition densities.  
We also have to explain what the right‑hand side means when \(p_1(t,x,z)=0\).

--------------------------------------------------------------------

## 2.  A rigorous proof  

### 2.1  Conditional expectation of a Radon–Nikodym derivative  

Let  

\[
\mathcal G := \sigma(X_t) \subset \mathcal F_t .
\]

Because \(M_t=\frac{d\mathbb Q}{d\mathbb P}\big|_{\mathcal F_t}\), the restriction of \(M_t\) to \(\mathcal G\) is the Radon–Nikodym derivative of the **marginal** \(\mathbb Q\) on \(\mathcal G\) with respect to the marginal \(\mathbb P\) on \(\mathcal G\):  

\[
\boxed{\; \mathbb E_{\mathbb P}[M_t\mid\mathcal G]=\frac{d\mathbb Q|_{\mathcal G}}{d\mathbb P|_{\mathcal G}}\;}\qquad\text{(a.s.)}      \tag{2.1}
\]

*Why?*  By definition of conditional expectation, for every bounded \(\mathcal G\)-measurable random variable \(F\),

\[
\mathbb E_{\mathbb P}\!\bigl[M_t F\bigr]
   = \mathbb E_{\mathbb Q}[F]
   = \int F\,d\mathbb Q|_{\mathcal G}
   = \int F\;\frac{d\mathbb Q|_{\mathcal G}}{d\mathbb P|_{\mathcal G}}\,d\mathbb P|_{\mathcal G}
   = \mathbb E_{\mathbb P}\!\bigl[F\,\frac{d\mathbb Q|_{\mathcal G}}{d\mathbb P|_{\mathcal G}}\bigr].
\]

Hence the Radon–Nikodym derivative satisfies the defining property of the conditional expectation, giving (2.1).

Since \(\mathcal G = \sigma(X_t)\), any \(\mathcal G\)-measurable random variable can be written as a Borel function of \(X_t\); we may therefore identify the conditional expectation with a (a.e. unique) Borel function \(g\) on \(\mathbb R^2\) such that  

\[
\mathbb E_{\mathbb P}[M_t\mid X_t]=g(X_t),\qquad g(z)=\frac{d\mathbb Q|_{\sigma(X_t)}}{d\mathbb P|_{\sigma(X_t)}}(z).      \tag{2.2}
\]

Thus the problem reduces to **identifying** the Radon–Nikodym derivative of the marginal law of \(X_t\) under \(\mathbb Q\) with respect to its marginal law under \(\mathbb P\).

--------------------------------------------------------------------

### 2.2  The two marginal laws have densities  

By hypothesis

* under \(\mathbb P\) the law of \(X_t\) has density \(p_1(t,x,\cdot)\):

  \[
  \mathbb P\bigl(X_t\in A\bigr)=\int_A p_1(t,x,z)\,dz ,\qquad A\subset\mathbb R^2\ \text{Borel};
  \tag{2.3}
  \]

* under \(\mathbb Q\) the law of \(X_t\) has density \(p_0(t,x,\cdot)\):

  \[
  \mathbb Q\bigl(X_t\in A\bigr)=\int_A p_0(t,x,z)\,dz .
  \tag{2.4}
  \]

Both densities are non‑negative and integrable (they integrate to \(1\)).  

Consequently the two probability measures \(\mathbb Q\circ X_t^{-1}\) and \(\mathbb P\circ X_t^{-1}\) are **absolutely continuous** with respect to each other. In particular  

\[
\mathbb Q\circ X_t^{-1}\ \ll\ \mathbb P\circ X_t^{-1}.
\]

The Radon–Nikodym derivative of \(\mathbb Q\circ X_t^{-1}\) with respect to \(\mathbb P\circ X_t^{-1}\) is therefore the ratio of the two densities:

\[
\frac{d\bigl(\mathbb Q\circ X_t^{-1}\bigr)}{d\bigl(\mathbb P\circ X_t^{-1}\bigr)}(z)
   =\begin{cases}
     \displaystyle\frac{p_0(t,x,z)}{p_1(t,x,z)}, & p_1(t,x,z)>0,\\[2mm]
     0, & p_1(t,x,z)=0 .
    \end{cases}           \tag{2.5}
\]

The definition on the set \(\{p_1=0\}\) is legitimate because absolute continuity guarantees that the numerator vanishes there as well (see the next subsection).

--------------------------------------------------------------------

### 2.3  Why does \(p_0\) vanish wherever \(p_1\) does?  

Since \(M_t\ge 0\) and \(\mathbb Q\) is defined by \(\frac{d\mathbb Q}{d\mathbb P}=M_t\), we have \(\mathbb Q\ll\mathbb P\). Hence for **any** measurable set \(A\),

\[
\mathbb P\bigl(X_t\in A\bigr)=0\quad\Longrightarrow\quad 
\mathbb Q\bigl(X_t\in A\bigr)=0 .
\tag{2.6}
\]

Take \(A=\{z\in\mathbb R^2:\;p_1(t,x,z)=0\}\). Because \(p_1\) is a density of \(\mathbb P\circ X_t^{-1}\), we have \(\mathbb P(X_t\in A)=0\). By (2.6) also \(\mathbb Q(X_t\in A)=0\). Using (2.4),

\[
0=\mathbb Q(X_t\in A)=\int_A p_0(t,x,z)\,dz .
\]

Thus \(p_0(t,x,z)=0\) for Lebesgue‑a.e. \(z\in A\). Consequently the ratio \(\frac{p_0}{p_1}\) can be set to **zero** on the set \(\{p_1=0\}\) without altering the equality that holds \(\mathbb P\)-a.s.

--------------------------------------------------------------------

### 2.4  Identification of the conditional expectation  

Let \(\varphi:\mathbb R^2\to\mathbb R\) be any bounded Borel function. Because \(\varphi(X_t)\) is \(\mathcal G\)-measurable, by the definition of conditional expectation and (2.2) we have  

\[
\mathbb E_{\mathbb P}\!\bigl[ M_t\varphi(X_t)\bigr]
   =\mathbb E_{\mathbb P}\!\bigl[ \, \mathbb E_{\mathbb P}[M_t\mid X_t]\,\varphi(X_t) \bigr]
   =\int_{\mathbb R^2} \varphi(z)\,
      \mathbb E_{\mathbb P}[M_t\mid X_t=z]\,
      p_1(t,x,z)\,dz .        \tag{2.7}
\]

On the other hand, by the very definition of \(\mathbb Q\),

\[
\mathbb E_{\mathbb P}\!\bigl[ M_t\varphi(X_t)\bigr]=\mathbb E_{\mathbb Q}\!\bigl[ \varphi(X_t)\bigr]
   =\int_{\mathbb R^2} \varphi(z)\,p_0(t,x,z)\,dz .        \tag{2.8}
\]

Equating the right–hand sides of (2.7) and (2.8) we obtain  

\[
\int_{\mathbb R^2} \varphi(z)\,
      \bigl(\mathbb E_{\mathbb P}[M_t\mid X_t=z]\,p_1(t,x,z)-p_0(t,x,z)\bigr)\,dz =0 .
\]

Since this holds for **every** bounded Borel \(\varphi\), the integrand must vanish for \(dz\)-almost every \(z\). Hence

\[
\mathbb E_{\mathbb P}[M_t\mid X_t=z]\,p_1(t,x,z)=p_0(t,x,z)
\qquad\text{for }dz\text{-a.e. }z .
\]

Dividing by \(p_1(t,x,z)\) wherever it is positive and using the convention \(0/0:=0\) on the set where \(p_1=0\) (which we have just justified), we obtain the desired identity

\[
\boxed{\;
\mathbb E_{\mathbb P}\bigl[ M_t\mid X_t=z\bigr]
      =\frac{p_0(t,x,z)}{p_1(t,x,z)}\quad
      \text{for }p_1(t,x,\cdot)dz\text{-a.e. }z .
\;}
\]

--------------------------------------------------------------------

## 3.  Final statement  



*Original question: [how to prove p0/p1 is conditional expectation of dq/dp](https://math.stackexchange.com/questions/5149474/how-to-prove-p0-p1-is-conditional-expectation-of-dq-dp) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
