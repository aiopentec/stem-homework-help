---
layout: post
title: Density Functional Theory with Generalized Gradient Approxmations (GGA) - What
  Happens if the Electron Density Shows a &quot;Kink&quot; at the Ion Position?
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

For an atom (or any spherically‑symmetric closed‑shell system) we want the **exchange–correlation (XC) potential** that appears in the Kohn–Sham equations when the XC energy is written in a **generalized‑gradient approximation (GGA)**  

\[
E_{\text{xc}}[n]=\int d\mathbf r\; e_{\text{xc}}\!\bigl(n(\mathbf r),\nabla n(\mathbf r)\bigr) .
\]

The student tried to obtain the functional derivative  

\[
v_{\text{xc}}(\mathbf r)=\frac{\delta E_{\text{xc}}}{\delta n(\mathbf r)}
\]

by varying only the radial part of the density, integrating by parts, and worrying about the “kink’’ (actually a cusp) of the electronic density at the nuclear position.  

The answer must

* show the **correct derivation** of the GGA XC potential, keeping the full three‑dimensional functional derivative and only **afterwards** imposing spherical symmetry,
* discuss what happens at the nucleus where the density gradient diverges,
* point out where the original derivation went wrong, and
* give a compact final expression that can be used in practice.

---

## 2.  Full step‑by‑step derivation  

### 2.1  Functional derivative of a GGA functional  

Start from  

\[
E_{\text{xc}}[n]=\int d\mathbf r\; e_{\text{xc}}\!\bigl(n(\mathbf r),\nabla n(\mathbf r)\bigr) .
\]

A small variation of the density, \(n\to n+\delta n\), gives  

\[
\delta E_{\text{xc}}
  =\int d\mathbf r\Bigl[
       \frac{\partial e_{\text{xc}}}{\partial n}\,\delta n
     + \frac{\partial e_{\text{xc}}}{\partial(\nabla n)}\!\cdot\!\delta(\nabla n)
    \Bigr].
\]

Because \(\delta(\nabla n)=\nabla(\delta n)\),

\[
\delta E_{\text{xc}}
 =\int d\mathbf r\Bigl[
      \frac{\partial e_{\text{xc}}}{\partial n}\,\delta n
    + \frac{\partial e_{\text{xc}}}{\partial(\nabla n)}\!\cdot\!\nabla(\delta n)
   \Bigr].
\]

Now **integrate the second term by parts** (vector version of the product rule).  
Using the identity  

\[
\int d\mathbf r\; \mathbf A(\mathbf r)\!\cdot\!\nabla(\delta n)=
    -\int d\mathbf r\; \bigl[\nabla\!\cdot\!\mathbf A(\mathbf r)\bigr]\;\delta n
    +\underbrace{\oint_{\partial V}\! d\mathbf S\;\mathbf A\!\cdot\!\hat{\mathbf n}\,\delta n}_{\text{surface term}} ,
\]

and assuming that the variation vanishes on the boundary of the integration volume
(\(\delta n=0\) at \(r\to\infty\) and the surface at the origin gives no contribution because the area element is \(\propto r^{2}\)), we obtain  

\[
\delta E_{\text{xc}}
 =\int d\mathbf r\;
    \Bigl[
      \frac{\partial e_{\text{xc}}}{\partial n}
      -\nabla\!\cdot\!\frac{\partial e_{\text{xc}}}{\partial(\nabla n)}
    \Bigr]\;\delta n .
\]

Since the variation \(\delta n(\mathbf r)\) is arbitrary, the functional derivative is  

\[
\boxed{%
v_{\text{xc}}(\mathbf r)=\frac{\delta E_{\text{xc}}}{\delta n(\mathbf r)}
   =\frac{\partial e_{\text{xc}}}{\partial n}
    -\nabla\!\cdot\!\frac{\partial e_{\text{xc}}}{\partial(\nabla n)} } .
\tag{1}
\]

Equation (1) is the **general GGA XC potential**.  

---

### 2.2  Impose spherical symmetry  

For an atom we can write  

\[
n(\mathbf r)=n(r), \qquad
\nabla n = \frac{dn}{dr}\,\hat{\mathbf r}\equiv n'(r)\,\hat{\mathbf r},
\]

and the scalar quantity \(e_{\text{xc}}\) depends only on the two arguments
\(n(r)\) and \(|\nabla n| = |n'|\).  Hence  

\[
\frac{\partial e_{\text{xc}}}{\partial(\nabla n)}
   =\frac{\partial e_{\text{xc}}}{\partial |n'|}\,
     \frac{\partial |n'|}{\partial(\nabla n)}
   =\frac{\partial e_{\text{xc}}}{\partial |n'|}\,
     \frac{\nabla n}{|\nabla n|}
   =\frac{\partial e_{\text{xc}}}{\partial |n'|}\,\hat{\mathbf r}.
\]

Because the derivative is purely radial, the divergence in (1) reduces to the
radial Laplacian of a radially‑directed vector field:

\[
\nabla\!\cdot\!\bigl[ f(r)\,\hat{\mathbf r}\bigr]
   =\frac{1}{r^{2}}\frac{d}{dr}\bigl[r^{2}f(r)\bigr].
\]

Identifying  

\[
f(r)=\frac{\partial e_{\text{xc}}}{\partial |n'|},
\]

we obtain the **spherically‑symmetrized XC potential**

\[
\boxed{%
v_{\text{xc}}(r)=
   \frac{\partial e_{\text{xc}}}{\partial n}(n(r),|n'|) 
   -\frac{1}{r^{2}}\frac{d}{dr}\Bigl[
        r^{2}\,\frac{\partial e_{\text{xc}}}{\partial |n'|}(n(r),|n'|)
      \Bigr] } .
\tag{2}
\]

If the functional is written directly in terms of the *signed* derivative
\(n'(r)\) (as many GGA codes do) one simply replaces \(|n'|\) by \(n'\) and
keeps the same formula; the derivative \(\partial e_{\text{xc}}/\partial n'\)
is understood as the derivative with respect to the scalar argument \(n'\).

---

### 2.3  Behaviour at the nucleus (the “kink’’)  

Near a nucleus of charge \(Z\) the **exact electronic density satisfies the Kato cusp condition**

\[
\left.\frac{dn}{dr}\right|_{r\to0}= -Z\,n(0) .
\tag{3}
\]

Thus \(n'(r)\) is *finite* at the origin, but the *gradient of the gradient*
\(\frac{d}{dr}n'(r)\) can be singular because the Coulomb potential produces a
\(1/r\) behaviour in the Kohn–Sham orbitals.  In practice:

* The factor \(r^{2}\) in the divergence term of (2) **cancels** the \(1/r\) divergence.
* Explicitly, using (3),

  \[
  \lim_{r\to0}\frac{1}{r^{2}}\frac{d}{dr}\!\bigl[r^{2} f(r)\bigr]
    =\lim_{r\to0}\Bigl[2\frac{f(r)}{r}+f'(r)\Bigr].
  \]

  For a well‑behaved GGA functional \(f(r)=\partial e_{\text{xc}}/\partial n'\)
  remains finite as \(r\to0\); the term \(2f(r)/r\) would diverge only if
  \(f(r)\) did not vanish proportionally to \(r\).  All standard GGAs (PBE,
  PW91, BLYP, …) are constructed so that \(\partial e_{\text{xc}}/\partial n'\to0\)
  linearly with \(r\) at the nucleus, guaranteeing a **finite** \(v_{\text{xc}}(0)\).

Consequently the XC potential does **not** inherit the cusp of the density;
the “kink’’ in \(n(r)\) is harmless for GGA functionals.

---

### 2.4  Where the original derivation went off the rails  

| Step in the student's attempt | Correct statement |
|-------------------------------|-------------------|
| “Restrict the variation to the radial direction only’’ | The functional derivative must be taken in full 3‑D.  One may *later* impose spherical symmetry on the result, but the variation itself is unrestricted. |
| Treating \(\partial e_{\text{xc}}/\partial n'\) as a scalar that can be taken outside the divergence | \(\partial e_{\text{xc}}/\partial(\nabla n)\) is a **vector**.  The integration‑by‑parts formula must contain the divergence operator, not a simple derivative of a scalar. |
| Dropping the surface term without justification | The surface term at \(r\to\infty\) vanishes because \(\delta n=0\) there, but the term at the origin is **not** automatically zero; it becomes zero only after using the factor \(r^{2}\) that appears in the spherical volume element. |
| Writing \(\partial_r\!\bigl(r^{2}\, e_{\text{xc}}/n'\bigr)\) instead of \(\partial_r\!\bigl(r^{2}\,\partial e_{\text{xc}}/\partial n'\bigr)\) | The derivative should act on \(\partial e_{\text{xc}}/\partial n'\), not on the ratio \(e_{\text{xc}}/n'\). |

---

## 3.  Final answer  

For a GGA XC energy functional  

\[
E_{\text{xc}}[n]=\int d\mathbf r\;
   e_{\text{xc}}\bigl(n(\mathbf r),\nabla n(\mathbf r)\bigr),
\]

the exchange–correlation potential that enters the Kohn–Sham equations is

\[
\boxed{%
v_{\text{xc}}(\mathbf r)=
   \frac{\partial e_{\text{xc}}}{\partial n}
   -\nabla\!\cdot\!\frac{\partial e_{\text{xc}}}{\partial(\nabla n)} } .
\]

For a spherically symmetric atom this reduces to  

\[
\boxed{%
v_{\text{xc}}(r)=
   \frac{\partial e_{\text{xc}}}{\partial n}(n(r),|n'|)
   -\frac{1}{r^{2}}\frac{d}{dr}\Bigl[
        r^{2}\,\frac{\partial e_{\text{xc}}}{\partial |n'|}(n(r),|n'|)
      \Bigr] } .
\]

At the nuclear position the density obeys the cusp condition (3); standard GGAs are built such that the term \(\partial e_{\text{xc}}/\partial |n'|\) goes to zero linearly with \(r\). Consequently the XC potential remains **finite** at \(r=0\); there is no pathological “kink’’ in the potential.

---

## 4.  Common mistakes for this type of problem  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|

*Original question: [Density Functional Theory with Generalized Gradient Approxmations (GGA) - What Happens if the Electron Density Shows a &quot;Kink&quot; at the Ion Position?](https://chemistry.stackexchange.com/questions/26865/density-functional-theory-with-generalized-gradient-approxmations-gga-what-h) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
