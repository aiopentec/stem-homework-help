---
layout: question
title: Definition of degree map of complex line bundle in Lee&#39;s Introduction to
  Complex Manifolds
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Definition of degree map of complex
  line bundle in Lee&#39;s Introduction to Complex Manifolds'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We have a complex line bundle \(L\to M\) over a compact Riemann surface \(M\).

* **Definition A (sheaf‑theoretic).**  
  The first Chern class is defined as the element  

  \[
  c(L)= -\delta_\ast([L])\in H^{2}(M;\underline{\mathbb Z})
  \]

  obtained from the exponential exact sequence of sheaves.  
  Using the natural isomorphism  

  \[
  \Phi_{\mathbb Z}:H^{2}(M;\underline{\mathbb Z})\xrightarrow{\;\cong\;}H^{2}_{\text{sing}}(M;\mathbb Z)
  \]

  we view \(c(L)\) as a singular cohomology class and pair it with the fundamental class \([M]\in H_{2}(M;\mathbb Z)\):
  \[
  \deg(L)=\langle \Phi_{\mathbb Z}(c(L)),[M]\rangle .
  \]

* **Definition B (curvature).**  
  Choose a Hermitian metric on \(L\) and a compatible connection \(\nabla\).  
  Let \(F_{\nabla}\in\Omega^{2}(M;i\mathbb R)\) be its curvature 2‑form.  
  The “curvature definition” of the degree is  

  \[
  \deg(L)=\frac{1}{2\pi i}\int_{M}F_{\nabla}.
  \]

The problem asks: **Do these two numbers agree?** In other words, does the integer obtained by evaluating the sheaf‑theoretic Chern class on the fundamental class equal the integral of the curvature (up to the factor \(2\pi i\))?  

We will prove that they are indeed the same.

---

## 2.  Detailed proof that the two definitions coincide  

The proof is a short tour through three standard isomorphisms:

1. **Sheaf cohomology \(\leftrightarrow\) singular cohomology** (Theorem 6.18 of Lee).  
2. **Singular cohomology \(\leftrightarrow\) de Rham cohomology** (de Rham theorem).  
3. **Curvature form representing the Chern class** (Chern–Weil theory for line bundles).

We will keep track of the sign conventions used in Lee’s book.

---

### 2.1  From sheaf cohomology to singular cohomology  

The exponential short exact sequence of sheaves  

\[
0\longrightarrow\underline{\mathbb Z}\stackrel{i}{\longrightarrow}\mathscr E\stackrel{\exp}{\longrightarrow}\mathscr E^{\!*}\longrightarrow 0
\]

induces a connecting homomorphism  

\[
\delta_\ast:H^{1}(M;\mathscr E^{\!*})\longrightarrow H^{2}(M;\underline{\mathbb Z}).
\]

For the line bundle \(L\) we have its class \([L]\in H^{1}(M;\mathscr E^{\!*})\) (the Čech class of the transition functions).  
Lee defines  

\[
c(L)=-\,\delta_\ast([L])\in H^{2}(M;\underline{\mathbb Z}).
\tag{2.1}
\]

The natural isomorphism  

\[
\Phi_{\mathbb Z}:H^{2}(M;\underline{\mathbb Z})\xrightarrow{\;\cong\;}H^{2}_{\text{sing}}(M;\mathbb Z)
\]

sends \(c(L)\) to a singular cohomology class which we still denote by \(\Phi_{\mathbb Z}(c(L))\).

---

### 2.2  From singular cohomology to de Rham cohomology  

Let  

\[
\mathcal I : \Omega^{\bullet}(M)\longrightarrow C^{\bullet}_{\text{sing}}(M;\mathbb R)
\]

be the integration map: for a \(k\)-form \(\omega\) and a smooth singular \(k\)-simplex \(\sigma\),

\[
\mathcal I(\omega)(\sigma)=\int_{\sigma}\omega .
\]

\(\mathcal I\) is a cochain map and induces an isomorphism on cohomology (the de Rham isomorphism)

\[
\mathcal D:H^{k}_{\text{dR}}(M)\xrightarrow{\;\cong\;}H^{k}_{\text{sing}}(M;\mathbb R).
\tag{2.2}
\]

Because the image of \(\Phi_{\mathbb Z}(c(L))\) lies in the **integral** lattice of \(H^{2}_{\text{sing}}(M;\mathbb R)\), there exists a unique real cohomology class \(\alpha\in H^{2}_{\text{dR}}(M)\) such that  

\[
\mathcal D(\alpha)=\Phi_{\mathbb Z}(c(L))\in H^{2}_{\text{sing}}(M;\mathbb R).
\tag{2.3}
\]

We will identify \(\alpha\) explicitly using a connection on \(L\).

---

### 2.3  Chern–Weil description of the first Chern class  

Pick a Hermitian metric \(h\) on \(L\) and the unique metric‑compatible connection \(\nabla\).  
Its curvature is a 2‑form with values in \(i\mathbb R\),

\[
F_{\nabla}\in\Omega^{2}(M;i\mathbb R).
\]

For a complex line bundle the Chern–Weil theorem says

\[
c_{1}(L)=\Bigl[\frac{-1}{2\pi i}\,F_{\nabla}\Bigr]\in H^{2}_{\text{dR}}(M).
\tag{2.4}
\]

(Lee’s sign conventions: the Chern class defined in §6.2 is \(-\delta([L])\); the same sign appears in the Chern–Weil formula, so the factor \(-1/(2\pi i)\) is exactly the one that matches (2.1).)

Thus we may take  

\[
\alpha:=\Bigl[\frac{-1}{2\pi i}\,F_{\nabla}\Bigr]\in H^{2}_{\text{dR}}(M).
\]

Applying the de Rham isomorphism (2.2) we obtain  

\[
\mathcal D\!\left(\Bigl[\frac{-1}{2\pi i}\,F_{\nabla}\Bigr]\right)=\Phi_{\mathbb Z}(c(L)).
\tag{2.5}
\]

---

### 2.4  Pairing with the fundamental class  

Let \([M]\in H_{2}(M;\mathbb Z)\) be the fundamental class coming from a triangulation (or a smooth oriented manifold structure).  
The Kronecker pairing in singular (co)homology is compatible with the de Rham pairing:

\[
\langle \Phi_{\mathbb Z}(c(L)),[M]\rangle
\;=\;
\Bigl\langle \mathcal D\!\Bigl[\frac{-1}{2\pi i}F_{\nabla}\Bigr],[M]\Bigr\rangle
\;=\;
\int_{M}\frac{-1}{2\pi i}F_{\nabla}.
\tag{2.6}
\]

The middle equality follows from the definition of \(\mathcal D\): evaluating a de Rham class on the fundamental class is precisely integration of a representing form over \(M\).

Finally, note that the factor \(-1\) cancels the minus sign in Lee’s definition (2.1), so we obtain

\[
\boxed{\;
\deg(L)=\langle \Phi_{\mathbb Z}(c(L)),[M]\rangle
      =\frac{1}{2\pi i}\int_{M}F_{\nabla}
\;}
\]

which is exactly the curvature formula given in Lee’s Section 6.2.

Thus **the two definitions of the degree agree**.

---

## 3.  Final answer

Yes. For a complex line bundle \(L\to M\) over a compact Riemann surface the integer obtained by pairing the sheaf‑theoretic first Chern class with the fundamental class equals the integral of the curvature of any Hermitian connection divided by \(2\pi i\):

\[
\deg(L)=\langle \Phi_{\mathbb Z}\bigl(-\delta([L])\bigr),[M]\rangle
      =\frac{1}{2\pi i}\int_{M}F_{\nabla}.
\]

The equality follows from (i) the natural isomorphism between sheaf and singular cohomology, (ii) the de Rham isomorphism, and (iii) the Chern–Weil representation of the first Chern class by the curvature form.

---

## 4.  Common mistakes to avoid

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Forgetting the sign \(-\)** in the definition \(c(L)=-\delta([L])\). | The curvature formula already contains a minus sign; dropping one of them gives \(-\deg(L)\). | Write both definitions side‑by‑side and check the signs of each map (exponential sequence, Chern–Weil). |
| **Using \( \frac{1}{2\pi}\int F_{\nabla}\) instead of \(\frac{1}{2\pi i}\)**. | \(F_{\nabla}\) takes values in \(i\mathbb R\); omitting the \(i\) yields a purely imaginary number, not an integer. | Remember that \(F_{\nabla}=i\,\Omega\) with \(\Omega\) real, so \(\frac{1}{2\pi i}F_{\nabla}\) is real. |
| **Confusing de Rham cohomology with singular cohomology with integer coefficients**. | The de Rham isomorphism lands in \(H^{*}_{\text{sing}}(M;\mathbb R)\), not \(H^{*}_{\text{sing}}(M;\mathbb Z)\); the integer class lives in the lattice inside the real cohomology. | Emphasise the chain of maps: \(\underline{\mathbb Z}\to\underline{\mathbb R}\) (inclusion) → sheaf cohomology → singular cohomology → de Rham. |
| **Assuming the result holds for any connection** without checking metric compatibility. | The curvature of a non‑Hermitian connection need not represent the Chern class. | Use the unique metric‑compatible (Chern) connection; any two such connections differ by a \((1,0)+(0,1)\) form whose curvature contributes an exact term, leaving the cohomology class unchanged. |
| **Skipping the naturality of \(\Phi_{G}\)**. | The isomorphism \(\Phi_{\mathbb Z}\) must be compatible with the map \(\underline{\mathbb Z}\hookrightarrow\underline{\mathbb R}\); otherwise the diagram may not commute. | Cite Theorem 6.18: \(\Phi_{G}\) is natural with respect to sheaf morphisms, guaranteeing the diagram commutes. |

By watching out for these points the identification of the two degree formulas becomes routine.

*Original question: [Definition of degree map of complex line bundle in Lee&#39;s Introduction to Complex Manifolds](https://math.stackexchange.com/questions/5150695/definition-of-degree-map-of-complex-line-bundle-in-lees-introduction-to-complex) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
