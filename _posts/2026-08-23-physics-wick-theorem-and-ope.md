---
layout: post
title: Wick theorem and OPE
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A student has seen two different ways of writing the product of two fields  

* In ordinary (canonical) QFT the product is split into a **contraction** (the two‑point function) plus a **normal‑ordered** piece  

  \[
  X(z)Y(w)=\langle X(z)Y(w)\rangle+\;:\!X(z)Y(w)\!:
  \tag{1}
  \]

* In 2‑dimensional conformal field theory (CFT) the same product is written as a sum of a **singular part** (the terms that diverge when \(z\to w\)) and a **regular part** (the Taylor‑expanded non‑singular terms)

  \[
  X(z)Y(w)=\underbrace{\sum_{n=1}^{N}\frac{\{XY\}_n(w)}{(z-w)^n}}_{\text{contraction}}
  \;+\;
  \underbrace{\sum_{n=0}^{\infty}\frac{\{XY\}_{-n}(w)}{(z-w)^{-n}}}_{\text{regular (``normal‑ordered’’) terms}} .
  \tag{2}
  \]

The student wonders:

* How does Wick’s theorem look when we use the CFT definitions of **contraction** (the singular part of the OPE) and **normal ordering** (the regular part)?
* Can we simply replace “normal‑ordered product’’ in the textbook formula by “regular part’’ and keep the same combinatorial structure?
* If so, how do we actually obtain the **non‑singular** terms that appear in an OPE?

Below we give a step‑by‑step answer.

---

## 2.  Detailed solution

### 2.1  Review: contraction and normal ordering in a free (Gaussian) CFT  

In a *free* (or Gaussian) 2‑d CFT the fields satisfy Wick’s theorem exactly as in ordinary QFT.  
The basic objects are

* **Contraction** (or **propagator**)  

  \[
  \contraction{}{X}{(z)}{Y}
  X(z)Y(w)\equiv\langle X(z)Y(w)\rangle .
  \]

  By definition this is the **singular** part of the OPE; it contains every pole (or logarithm) that diverges when \(z\to w\).

* **Normal ordering** (radial‑ordered product)  

  \[
  :\!X(z)Y(w)\!:\;\equiv\;X(z)Y(w)-\langle X(z)Y(w)\rangle .
  \tag{3}
  \]

  In a CFT the notation \(\operatorname{Reg}\{X(z)Y(w)\}\) used in *di Francesco* is simply another way of writing the same object:
  \[
  \operatorname{Reg}\{X(z)Y(w)\}\equiv :\!X(z)Y(w)\!:
  \]

Thus the two formulae (1) and (2) are **identical**; they just use different terminology.

> **Key point:** In a free CFT the *regular part* of an OPE **is** the normal‑ordered product of the two fields.

---

### 2.2  Wick’s theorem in the CFT language  

Consider a collection of (free) fields \(\phi_i(z_i)\) with \(i=1,\dots,N\).  
The standard Wick theorem reads

\[
\phi_1(z_1)\phi_2(z_2)\cdots\phi_N(z_N)
   =\sum_{\text{all pairings }P}
      \Bigl(\prod_{(a,b)\in P}\langle\phi_a(z_a)\phi_b(z_b)\rangle\Bigr)\,
      :\!\!\prod_{k\notin P}\phi_k(z_k)\!\!:\; .
\tag{4}
\]

All possible ways of **pairing** the fields are summed over.  
Every pair contributes a contraction (the singular part of the OPE), and the remaining un‑contracted fields stay inside a normal‑ordered product.

If we now adopt the CFT notation of *di Francesco* we simply replace  

\[
:\!\!\prod_{k\notin P}\phi_k(z_k)\!\!:\;\;\longrightarrow\;\;
\operatorname{Reg}\Bigl\{\prod_{k\notin P}\phi_k(z_k)\Bigr\}.
\]

Hence the theorem becomes

\[
\boxed{
\phi_1(z_1)\cdots\phi_N(z_N)=
\sum_{P}
\Bigl(\prod_{(a,b)\in P}\underbrace{\contraction{}{\phi_a}{(z_a)}{\phi_b}
\phi_a(z_a)\phi_b(z_b)}_{\text{singular part}}\Bigr)\;
\operatorname{Reg}\Bigl\{\prod_{k\notin P}\phi_k(z_k)\Bigr\}
}
\tag{5}
\]

No extra terms appear; the combinatorial structure is unchanged.

---

### 2.3  Extracting the **regular (non‑singular) part** of an OPE  

Suppose we are interested in the OPE of two composite operators, e.g.  

\[
A(z)=:\!\phi_1(z)\phi_2(z)\!:\,,\qquad   
B(w)=:\!\phi_3(w)\phi_4(w)\!:\, .
\]

We want the expansion of \(A(z)B(w)\) around \(z=w\).  
Step‑by‑step:

1. **Write each composite operator as a product of elementary fields.**  
   \[
   A(z)B(w)=\phi_1(z)\phi_2(z)\,\phi_3(w)\phi_4(w) .
   \]

2. **Apply Wick’s theorem (5).**  
   Every contraction is the singular part of the corresponding two‑point function.  
   For a free boson \(X\) we have  

   \[
   \contraction{}{X}{(z)}{X}X(z)X(w)=\langle X(z)X(w)\rangle
   =-\alpha'\,\ln(z-w)\; .
   \]

   For fermions or other primaries the singular part is a simple pole or higher‑order pole.

3. **Collect the terms with a given number of contractions.**  
   *Zero contractions* give the regular part of the product:  

   \[
   \operatorname{Reg}\{\phi_1(z)\phi_2(z)\phi_3(w)\phi_4(w)\}
   =:\!\phi_1(z)\phi_2(z)\phi_3(w)\phi_4(w)\!:
   \tag{6}
   \]

   *One contraction* gives a term proportional to the two‑point function times a normal‑ordered product of the remaining three fields, etc.

4. **Expand the remaining normal‑ordered fields around \(w\).**  
   Because the normal‑ordered product is *regular* at \(z=w\), we may Taylor expand each field:

   \[
   :\!\phi_i(z)\!:=\sum_{n=0}^{\infty}\frac{(z-w)^n}{n!}\,\partial^n\phi_i(w) .
   \tag{7}
   \]

   Substituting (7) into the regular piece (6) yields a series of the form  

   \[
   \operatorname{Reg}\{A(z)B(w)\}
   =\sum_{n=0}^{\infty}\frac{(z-w)^n}{n!}\,C_n(w) ,
   \tag{8}
   \]

   where each coefficient \(C_n(w)\) is a **composite primary** built from normal‑ordered products of the elementary fields and their derivatives.  
   These \(C_n(w)\) are precisely the *non‑singular* terms that appear in the OPE.

5. **Combine singular and regular pieces.**  

   The full OPE reads

   \[
   A(z)B(w)=\underbrace{\sum_{\text{singular}} \frac{c_{k}(w)}{(z-w)^{k}}}_{\displaystyle\text{contractions}}
   \;+\;
   \underbrace{\sum_{n=0}^{\infty}\frac{(z-w)^n}{n!}\,C_n(w)}_{\displaystyle\text{regular (normal‑ordered) part}} .
   \tag{9}
   \]

   The coefficients \(c_k(w)\) are obtained from the various ways of contracting fields; the coefficients \(C_n(w)\) are obtained from the Taylor expansion of the regular product.

---

### 2.4  Example: free boson \(\partial X(z)\,\partial X(w)\)

The elementary field \(X(z)\) has the OPE  

\[
X(z)X(w)=-\alpha'\,\ln(z-w)+:X(z)X(w): .
\]

Differentiating gives  

\[
\partial X(z)\,\partial X(w)=\frac{-\alpha'}{(z-w)^2}+:\!\partial X(z)\partial X(w)\!:
\tag{10}
\]

Now expand the regular part:

\[
:\!\partial X(z)\partial X(w)\!:
   =:\!\partial X(w)\partial X(w)\!:+(z-w):\!\partial^2 X(w)\partial X(w)\!:+\cdots .
\tag{11}
\]

Thus the OPE is  

\[
\boxed{
\partial X(z)\,\partial X(w)=\frac{-\alpha'}{(z-w)^2}
+\sum_{n=0}^{\infty}\frac{(z-w)^n}{n!}\;:\!\partial^{n+1}X(w)\,\partial X(w)\!:
}
\tag{12}
\]

The first term is the *contraction* (singular part).  
All the terms in the infinite sum are the *regular* (normal‑ordered) contributions, obtained exactly by the Taylor expansion described above.

---

### 2.5  Summary of the answer to the original question  

* **Yes**, Wick’s theorem works in a CFT exactly as in ordinary QFT **provided the theory is free (Gaussian)**.  
* The **contraction** is the *singular part* of the OPE, i.e. the two‑point function.  
* The **regular part** of the OPE is *by definition* the **normal‑ordered product** of the fields that remain after the contractions have been removed.  
* Therefore the formula

  \[
  \text{product} = \text{sum over all contractions}\times\bigl(\text{regular part}\bigr)
  \]

  is completely legitimate; you may replace “normal‑ordered’’ by “regular’’ without changing anything.  
* The **non‑singular terms** in an OPE are obtained by (i) performing all possible contractions, (ii) writing the remaining fields inside a normal‑ordered product, and (iii) expanding that normal‑ordered product in a Taylor series around the point where the OPE is taken.

---

## 3.  Final answer (concise statement)

In a free (Gaussian)

*Original question: [Wick theorem and OPE](https://physics.stackexchange.com/questions/317395/wick-theorem-and-ope) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
