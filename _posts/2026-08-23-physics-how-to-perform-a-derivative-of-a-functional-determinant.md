---
layout: post
title: How to perform a derivative of a functional determinant?
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We have a scalar field that lives on a curved space‑time with metric \(g_{\mu\nu}(x)\).
The quadratic part of its (Euclidean) action can be written with the differential
operator  

\[
\boxed{ \;G^{-1}(x,y;g)=\delta^{(4)}(x-y)\,\sqrt{-g(y)}\,
\bigl(g^{\mu\nu}(y)\nabla_\mu^{(y)}\nabla_\nu^{(y)}+m^{2}\bigr) \;}
\]

which is the inverse propagator (the “kernel’’ of the kinetic operator).
The one‑loop effective action contains the functional determinant of this operator,
\(\log\det G^{-1}\).

The problem is to **differentiate** that determinant with respect to the metric,
i.e. to compute  

\[
\frac{\delta}{\delta g^{\mu\nu}(x)}\,
\log\det G^{-1}\; .
\]

In flat space a similar derivative with respect to a scalar background field \(\varphi\)
gives the familiar result  

\[
\frac{\delta}{\delta\varphi(x)}\log\det G^{-1}=
V'''(\varphi(x))\,G(x,x)\; .
\]

Here we have to do the same thing, but the operator depends on the metric in a
non‑trivial way (through the factor \(\sqrt{-g}\), the inverse metric
\(g^{\mu\nu}\) and the covariant derivatives).  
The goal is to obtain an expression that is **exact** (no steps skipped) and to
explain why it looks divergent and how the divergence is usually handled.

--------------------------------------------------------------------

## 2.  Full derivation, step by step  

Below we work in Euclidean signature (the Wick‑rotated version of the
original Lorentzian theory).  All functional traces are taken over the space of
square‑integrable functions on the manifold.

### 2.1  Basic functional‑determinant identity  

For any (formally) invertible operator \(\mathcal{O}\)

\[
\boxed{\;\frac{\delta}{\delta\lambda}\,\log\det \mathcal{O}
      =\operatorname{Tr}\!\bigl(\mathcal{O}^{-1}\,\delta_{\lambda}\mathcal{O}\bigr)
      =\operatorname{Tr}\!\bigl(G\,\delta_{\lambda}\mathcal{O}\bigr)\;}
\tag{2}
\]

where \(G\equiv\mathcal{O}^{-1}\) is the Green function (the propagator) defined by  

\[
\mathcal{O}_x\,G(x,y)=\frac{\delta^{(4)}(x-y)}{\sqrt{-g(x)}} .
\]

Equation (2) is the curved‑space analogue of the flat‑space identity used in the
question.

### 2.2  Write the operator in a convenient form  

Define the covariant Laplacian (the d’Alembertian)

\[
\Box\equiv g^{\mu\nu}\nabla_{\mu}\nabla_{\nu}\;,
\qquad\text{so that}\qquad 
\mathcal{O}\equiv G^{-1}= \sqrt{-g}\,(\,-\Box+m^{2}\,).
\]

(With the metric signature \((+,-,-,-)\) the kinetic operator is
\(-\Box+m^{2}\); the overall sign is irrelevant for the functional derivative.)

### 2.3  Variation of the operator  

The metric appears in three places:

1. the overall factor \(\sqrt{-g}\);
2. the inverse metric inside \(\Box\);
3. the connection hidden inside the covariant derivatives.

We vary each piece.

*Variation of the determinant factor*  

\[
\delta\sqrt{-g}= -\frac12\sqrt{-g}\;g_{\alpha\beta}\,\delta g^{\alpha\beta}.
\tag{3}
\]

*Variation of the Laplacian*  

\[
\delta\Box
    =\delta(g^{\mu\nu}\nabla_{\mu}\nabla_{\nu})
    =\underbrace{\delta g^{\mu\nu}\,\nabla_{\mu}\nabla_{\nu}}_{\text{explicit metric}}
     \;-\;g^{\mu\nu}\,\delta\Gamma^{\lambda}_{\mu\nu}\,\nabla_{\lambda},
\tag{4}
\]

where the variation of the Christoffel symbols is  

\[
\boxed{\;
\delta\Gamma^{\lambda}_{\mu\nu}
   =\frac12 g^{\lambda\rho}
     \bigl(\nabla_{\mu}\delta g_{\rho\nu}
          +\nabla_{\nu}\delta g_{\rho\mu}
          -\nabla_{\rho}\delta g_{\mu\nu}\bigr)
\;}
\tag{5}
\]

and \(\delta g_{\mu\nu}= -g_{\mu\alpha}g_{\nu\beta}\,\delta g^{\alpha\beta}\).

Putting (3)–(5) together we obtain  

\[
\boxed{
\delta\mathcal{O}
   =\sqrt{-g}\Bigl[
          -\frac12 g_{\alpha\beta}\,\delta g^{\alpha\beta}\;(\!-\Box+m^{2}\!)
          +\delta g^{\mu\nu}\nabla_{\mu}\nabla_{\nu}
          -g^{\mu\nu}\,\delta\Gamma^{\lambda}_{\mu\nu}\nabla_{\lambda}
          \Bigr].
}
\tag{6}
\]

### 2.4  Insert the variation into the trace formula  

Using (2) we write  

\[
\delta\log\det G^{-1}
   =\operatorname{Tr}\!\bigl(G\,\delta\mathcal{O}\bigr)
   =\int\!d^{4}x\sqrt{-g(x)}\,
      \bigl\langle x\big|\,G\,\delta\mathcal{O}\,\big|x\bigr\rangle .
\tag{7}
\]

Because \(G\) is the inverse of \(\mathcal{O}\), the operator product
\(G\,\delta\mathcal{O}\) can be evaluated by acting the derivatives on the
coincident Green function \(G(x,y)\) and then setting \(y\to x\).  Denoting  

\[
G(x,x)\equiv \lim_{y\to x}G(x,y),
\qquad
\bigl(\nabla_{\mu

*Original question: [How to perform a derivative of a functional determinant?](https://physics.stackexchange.com/questions/618560/how-to-perform-a-derivative-of-a-functional-determinant) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
