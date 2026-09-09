---
layout: question
title: A question about why a atlas on a differentiable manifold consist of compatible
  charts
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: A question about why a atlas on a
  differentiable manifold consist of compatible charts'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

We have a differentiable manifold \(M\) equipped with an **atlas**
\(\mathcal A=\{(U,\varphi)\}\).  
Two charts \((U,\varphi)\) and \((V,\psi)\) are called **\(C^{m}\)-compatible** when the change‑of‑coordinates map  

\[
\varphi\circ\psi^{-1}:\psi\bigl(U\cap V\bigr)\longrightarrow 
\varphi\bigl(U\cap V\bigr)
\]

is a \(C^{m}\) function (i.e. has continuous partial derivatives up to order \(m\)).  

A **\(C^{m}\) function** on the manifold is defined as follows:

> \(f:M\to\mathbb R\) is of class \(C^{m}\) if for every point \(p\in M\) there exists a chart \((U,\varphi)\in\mathcal A\) with \(p\in U\) such that the Euclidean function  
> \[
> f\circ\varphi^{-1}:\varphi(U)\longrightarrow\mathbb R
> \]
> is of class \(C^{m}\).

The books say that this definition does **not** depend on which chart we pick, because the charts in the atlas are compatible.  

The student’s doubt is:

*When we write*
\[
f\circ\psi^{-1}= (f\circ\varphi^{-1})\;\circ\;(\varphi\circ\psi^{-1}),
\]
*the second factor \(\varphi\circ\psi^{-1}\) is only defined on the overlap
\(\psi(U\cap V)\), not on the whole set \(\psi(V)\). So we seem to obtain only
that \((f\circ\psi^{-1})\) restricted to the overlap is \(C^{m}\), not that
\(f\circ\psi^{-1}\) itself is \(C^{m}\). How do we get the full statement?*

In short: **Why does compatibility of charts guarantee that the notion of a \(C^{m}\) function is independent of the chosen chart?**  

---

## 2. Detailed solution (all steps shown)

### 2.1. What we actually have to prove

Let \((U,\varphi)\) and \((V,\psi)\) be two charts in a \(C^{m}\)-atlas \(\mathcal A\).
Assume that for a point \(p\in U\cap V\) the Euclidean representation
\(f\circ\varphi^{-1}\) is a \(C^{m}\) function on \(\varphi(U)\).
We must show that **the Euclidean representation using the other chart,
\(f\circ\psi^{-1}\), is also \(C^{m}\) (at least on a neighbourhood of \(p\)).**
Doing this for every point of \(V\) will give the desired global independence.

### 2.2. The domains that appear

- \(\varphi:U\to\varphi(U)\subset\mathbb R^{n}\) is a diffeomorphism onto its image.
- \(\psi:V\to\psi(V)\subset\mathbb R^{n}\) is a diffeomorphism onto its image.
- The **overlap** of the two coordinate neighbourhoods is \(U\cap V\).
  Its image in the \(\psi\)-coordinates is \(\psi(U\cap V)\subset\psi(V)\);  
  its image in the \(\varphi\)-coordinates is \(\varphi(U\cap V)\subset\varphi(U)\).

The change‑of‑coordinates map
\[
\Phi:=\varphi\circ\psi^{-1}:\psi(U\cap V)\longrightarrow\varphi(U\cap V)
\]
is defined **exactly** on the overlap \(\psi(U\cap V)\); it is not defined
outside that set.

### 2.3. The key observation

The definition of a \(C^{m}\) function on the manifold is **local**:
to say that \(f\) is \(C^{m}\) at a point \(p\) we only need one chart that
contains \(p\) and on which the Euclidean representation is \(C^{m}\) *on a
neighbourhood of the image of \(p\)*.

Therefore, to prove independence of the chart we do **not** have to
show that the whole map \(f\circ\psi^{-1}:\psi(V)\to\mathbb R\) is \(C^{m}\);
we only need to show that it is \(C^{m}\) on a neighbourhood of the point
\(\psi(p)\). That neighbourhood is precisely \(\psi(U\cap V)\).

Thus the apparent “domain problem’’ is actually what we need.

### 2.4. Proof that the representation in the second chart is \(C^{m}\)

Let \(p\in U\cap V\).  
Assume that \(f\circ\varphi^{-1}\) is \(C^{m}\) on an open set
\(W\subset\varphi(U)\) containing \(\varphi(p)\). (If it is \(C^{m}\) on the
whole \(\varphi(U)\), we can simply take \(W=\varphi(U)\).)

1. **Change of coordinates is \(C^{m}\).**  
   By the hypothesis that the atlas is a \(C^{m}\)-atlas, the map  
   \[
   \Phi=\varphi\circ\psi^{-1}:\psi(U\cap V)\longrightarrow\varphi(U\cap V)
   \]
   is a \(C^{m}\) diffeomorphism. In particular, its inverse
   \(\Phi^{-1}=\psi\circ\varphi^{-1}\) is also \(C^{m}\).

2. **Compose the two \(C^{m}\) maps.**  
   Consider the composition
   \[
   (f\circ\psi^{-1})\big|_{\psi(U\cap V)} 
   \;=\;
   (f\circ\varphi^{-1})\;\circ\;\Phi .
   \]
   Here:
   - \(\Phi\) is \(C^{m}\) on the open set \(\psi(U\cap V)\);
   - \(f\circ\varphi^{-1}\) is \(C^{m}\) on the open set \(W\) that contains
     \(\Phi\bigl(\psi(U\cap V)\bigr)=\varphi(U\cap V)\).

   By the chain rule (or the standard theorem that the composition of two
   \(C^{m}\) maps is \(C^{m}\)), the composition
   \((f\circ\varphi^{-1})\circ\Phi\) is a \(C^{m}\) function on
   \(\psi(U\cap V)\).

3. **Conclusion for the point \(p\).**  
   Since \(\psi(p)\in\psi(U\cap V)\), we have shown that \(f\circ\psi^{-1}\)
   is \(C^{m}\) on a neighbourhood of \(\psi(p)\). Hence \(f\) is \(C^{m}\)
   at \(p\) when we use the chart \((V,\psi)\).

Because the argument works for *any* point \(p\in V\) (choose a chart
\((U,\varphi)\) that contains \(p\) and on which \(f\circ\varphi^{-1}\) is
\(C^{m}\); such a chart exists by the definition of a \(C^{m}\) function),
we obtain that **the property “\(f\) is \(C^{m}\) at \(p\)” does not depend on
the particular chart that contains \(p\)**.

### 2.5. Why we do not need the whole \(\psi(V)\)

The definition of a \(C^{m}\) function on a manifold never asks for a
single chart to work *everywhere* on \(M\). It only asks that **locally**
around each point there is *some* chart giving a \(C^{m}\) Euclidean
representation. Consequently, when we change from one chart to another we
only have to compare the representations on the *overlap* of the two
charts, which is exactly what the compatibility condition guarantees.

If we did want a statement of the form “\(f\circ\psi^{-1}\) is \(C^{m}\) on
all of \(\psi(V)\)”, it would be false in general: the function might not be
\(C^{m}\) on parts of \(V\) where we have not yet verified the condition.
What matters is that every point of \(V\) belongs to some overlap with a
chart where we already know \(C^{m}\), and then the above argument shows the
desired regularity at that point.

---

## 3. Final answer

The compatibility of charts in a \(C^{m}\)-atlas guarantees that the notion
of a \(C^{m}\) function on the manifold is **independent of the chosen chart**:

- If \(f\circ\varphi^{-1}\) is \(C^{m}\) on a chart \((U,\varphi)\) and
  \((V,\psi)\) is any other chart containing the same point, then on the
  overlap \(\psi(U\cap V)\) we have  

  \[
  f\circ\psi^{-1} = (f\circ\varphi^{-1})\;\circ\;(\varphi\circ\psi^{-1}),
  \]

  a composition of two \(C^{m}\) maps; therefore it is \(C^{m}\) on that
  overlap. Hence \(f\) is \(C^{m}\) at the point when expressed in the
  \(\psi\)-coordinates.

- Doing this for every point of \(V\) shows that the definition of a
  \(C^{m}\) function does not depend on which chart from the atlas we use.

Thus the requirement that the charts of an atlas be pairwise \(C^{m}\)‑compatible
is exactly what makes the definition of differentiability on a manifold
well‑posed.

---

## 4. Common mistakes

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking we must prove \(f\circ\psi^{-1}\) is \(C^{m}\) on the whole \(\psi(V)\).** | The definition of a \(C^{m}\) function is *local*; we only need \(C^{m}\) on a neighbourhood of each point. | Remember that the statement “\(f\) is \(C^{m}\) at \(p\)” requires a chart containing \(p\) with a \(C^{m}\) representation *near* \(p\). |
| **Ignoring the domain of the change‑of‑coordinates map.** | The map \(\varphi\circ\psi^{-1}\) is defined only on the overlap; trying to compose it with a function defined on a larger set leads to a meaningless expression. | Explicitly restrict all compositions to the overlap \(\psi(U\cap V)\). |
| **Assuming compatibility of two charts automatically gives a global \(C^{m}\) structure.** | Compatibility ensures smooth transition maps, but a single chart may not cover the whole manifold. | Use the atlas: cover the manifold with charts and apply the local argument at each point. |
| **Confusing “\(C^{m}\) on an open set” with “\(C^{m}\) on its closure”.** | Differentiability is defined on open sets; extending to the boundary can fail. | Work only with open neighbourhoods (e.g., \(\psi(U\cap V)\) is open in \(\psi(V)\)). |
| **Forgetting to use the chain rule for compositions of maps between Euclidean spaces.** | The regularity of the composition is not automatic without invoking the chain rule. | State explicitly: “Since both \(\Phi\) and \(f\circ\varphi^{-1}\) are \(C^{m}\), their composition is \(C^{m}\) by the chain rule.” |

By keeping these points in mind, the proof that chart compatibility makes the
definition of a \(C^{m}\) function well‑defined becomes clear and rigorous.

*Original question: [A question about why a atlas on a differentiable manifold consist of compatible charts](https://math.stackexchange.com/questions/5149009/a-question-about-why-a-atlas-on-a-differentiable-manifold-consist-of-compatible) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
