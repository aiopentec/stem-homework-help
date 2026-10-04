---
layout: question
title: Computing the intersection of two splitting fields as $\mathbb Q$-vector spaces
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Computing the intersection of two
  splitting fields as $\mathbb Q$-vector spaces'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

# 1.  What the problem is asking (in plain language)

You are given two **separable** polynomials  

\[
f(x),\;g(x)\in\mathbb Q[x]
\]

and you look at their *splitting fields*  

\[
K_f=\operatorname{Spl}_{\mathbb Q}(f),\qquad 
K_g=\operatorname{Spl}_{\mathbb Q}(g).
\]

Both fields are finite Galois extensions of \(\mathbb Q\).  
The question is:

*Can we **effectively** produce a polynomial \(h(x)\in\mathbb Q[x]\) whose splitting
field is exactly the intersection*  

\[
L=K_f\cap K_g ?
\]

Ideally the method should avoid having to compute the full Galois groups of
\(f\) and \(g\); it would be nice if we could work only with linear algebra
inside the compositum  

\[
K=K_fK_g=\operatorname{Spl}_{\mathbb Q}(fg).
\]

---

# 2.  Overview of the solution

Yes – an algorithm exists.  The idea is to

1. **Build the compositum** \(K=K_fK_g\).  This is the splitting field of the product
   \(fg\); we can represent it as a simple extension \(\mathbb Q[\theta]\) for a
   primitive element \(\theta\).

2. **Identify the two subfields** \(K_f\) and \(K_g\) inside \(K\).  A root of
   \(f\) (resp. \(g\)) belonging to \(K\) will serve as a primitive element for
   the corresponding subfield.

3. **Compute the vector‑space intersection** \(L=K_f\cap K_g\) inside the
   \(\mathbb Q\)-vector space \(K\) by solving a linear system.

4. **Produce a primitive element** \(\beta\) of the intersection (a random
   \(\mathbb Q\)-linear combination of a basis of \(L\) works with probability
   1).

5. **Return the minimal polynomial** of \(\beta\) over \(\mathbb Q\).  Its
   splitting field is precisely \(L\).

All steps are constructive and can be carried out with the standard
algorithms for number fields (factorisation of polynomials over a number field,
computing primitive elements, solving linear equations, etc.).  No explicit
computation of Galois groups is required, although the method can be phrased
in group‑theoretic language if one wishes.

---

# 3.  Detailed step‑by‑step algorithm

We write the algorithm in a way that could be implemented in a computer algebra
system.

--------------------------------------------------------------------
### Input
Two separable polynomials  

\[
f(x),\;g(x)\in\mathbb Q[x].
\]

--------------------------------------------------------------------
### Output
A polynomial \(h(x)\in\mathbb Q[x]\) whose splitting field equals
\(K_f\cap K_g\).

--------------------------------------------------------------------
### Step 0 – Preparations
* Compute the degrees  

  \[
  n_f=\deg f,\qquad n_g=\deg g,
  \]
  and verify separability (e.g. \(\gcd(f,f')=1\) and \(\gcd(g,g')=1\)).
* Let  

  \[
  n=[K_fK_g:\mathbb Q]=\deg\bigl(\operatorname{Spl}_{\mathbb Q}(fg)\bigr).
  \]

--------------------------------------------------------------------
### Step 1 – Construct the compositum \(K=K_fK_g\)

1. **Factor \(f\) and \(g\) over \(\mathbb Q\).**  
   Let \(\alpha_1,\dots ,\alpha_{n_f}\) be the (pairwise distinct) roots of \(f\)
   in an algebraic closure \(\overline{\mathbb Q}\); similarly \(\beta_1,\dots ,
   \beta_{n_g}\) for \(g\).

2. **Pick a primitive element.**  
   By the primitive‑element theorem there exist rational numbers
   \(c_1,c_2\) such that  

   \[
   \theta = \alpha_1 + c_1\beta_1 + c_2
   \]

   generates the whole compositum \(K\).  
   In practice one can try a few random integer pairs \((c_1,c_2)\) until the
   minimal polynomial of \(\theta\) over \(\mathbb Q\) has degree \(n\).
   (The probability of success is \(>1/2\) for a random choice.)

3. **Compute the minimal polynomial of \(\theta\).**  
   Use the standard “resultant’’ or “modular’’ algorithms to obtain  

   \[
   m_\theta (x)=\operatorname{MinPoly}_\mathbb{Q}(\theta)\in\mathbb Q[x].
   \]

   The field \(K\) is now represented as  

   \[
   K\;=\;\mathbb Q[\theta]\;\cong\;\mathbb Q[x]/(m_\theta (x)).
   \]

   All arithmetic in \(K\) will be performed with respect to the basis  

   \[
   \mathcal B_K=\{1,\theta,\theta^2,\dots ,\theta^{n-1}\}.
   \]

--------------------------------------------------------------------
### Step 2 – Embed the two splitting fields inside \(K\)

*Factor the original polynomials in the ring \(\mathbb Q[\theta]\).*

1. **Factor \(f\) over \(K\).**  
   Use the factorisation algorithm for polynomials over a number field to
   write  

   \[
   f(x)=\prod_{i=1}^{n_f}(x-\alpha_i)\quad\text{in }K[x].
   \]

   Pick any root, say \(\alpha:=\alpha_1\in K\).

2. **Set**  

   \[
   K_f = \mathbb Q[\alpha]\subseteq K.
   \]

   Since \(f\) is separable, \(\alpha\) generates the whole splitting field
   \(K_f\).  Its degree \(d_f=[K_f:\mathbb Q]\) is the degree of the minimal
   polynomial of \(\alpha\) over \(\mathbb Q\) (computed by a resultant).

3. **Do the same for \(g\).**  
   Factor \(g\) in \(K[x]\), pick a root \(\beta\in K\) and set  

   \[
   K_g = \mathbb Q[\beta]\subseteq K,
   \qquad d_g=[K_g:\mathbb Q].
   \]

Thus we have concrete \(\mathbb Q\)-bases

\[
\mathcal B_f=\{1,\alpha,\alpha^2,\dots ,\alpha^{d_f-1}\},\qquad
\mathcal B_g=\{1,\beta ,\beta^2,\dots ,\beta^{d_g-1}\}
\]

expressed as \(\mathbb Q\)-linear combinations of the basis \(\mathcal B_K\) of
\(K\).

--------------------------------------------------------------------
### Step 3 – Compute the intersection \(L = K_f\cap K_g\) as a vector space

Write an arbitrary element of \(K_f\) as  

\[
x=\sum_{i=0}^{d_f-1}u_i\alpha^i,\qquad u_i\in\mathbb Q .
\]

Express each power \(\alpha^i\) in the basis \(\mathcal B_K\); this gives a
matrix  

\[
A_f\in\mathbb Q^{n\times d_f}
\]

whose columns are the coordinates of \(1,\alpha,\dots ,\alpha^{d_f-1}\) in
\(\mathcal B_K\).

Do the same for \(K_g\) and obtain \(A_g\in\mathbb Q^{n\times d_g}\).

An element \(x\) belongs to the intersection iff its coordinate vector
\(v=A_f\mathbf u\) (with \(\mathbf u\in\mathbb Q^{d_f}\)) also lies in the column
space of \(A_g\).  Therefore we must solve

\[
A_f\mathbf u = A_g\mathbf w \quad\text{for }(\mathbf u,\mathbf w)\in
\mathbb Q^{d_f}\times\mathbb Q^{d_g}.
\]

This is a linear system over \(\mathbb Q\).  Compute a basis of its solution
space, then project the solutions onto the first \(d_f\) coordinates to obtain a
basis \(\{\gamma_1,\dots ,\gamma_m\}\) of the intersection as a \(\mathbb Q\)‑vector
space.  (Equivalently, compute a basis of \(\operatorname{im}A_f\cap\operatorname{im}
A_g\) inside \(\mathbb Q^n\).)

The dimension \(m\) equals \([L:\mathbb Q

*Original question: [Computing the intersection of two splitting fields as $\mathbb Q$-vector spaces](https://math.stackexchange.com/questions/5151056/computing-the-intersection-of-two-splitting-fields-as-mathbb-q-vector-spaces) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
