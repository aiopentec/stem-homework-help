---
layout: question
title: Unable to derive exact Coleman-de Luccia instanton differential equation 3.2
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Unable to derive exact Coleman-de
  Luccia instanton differential equation 3.2'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem asks  

We are given the “master” equation (2.10) of the paper (with the spacetime dimension set to \(d=4\))

\[
\kappa\Bigl(\frac{d\phi}{dz}\Bigr)^{2}
= \frac{2}{a^{2}}\Bigl(\frac{da}{dz}\Bigr)^{2}
-\frac{1}{a}\,\frac{d^{2}a}{dz^{2}}-1 .\tag{2.10\;(d=4)}
\]

The scale factor is taken to be  

\[
a(z)=\ell\,\frac{f(\lambda)}{\cosh z},
\qquad 
\lambda\equiv\tanh z .
\]

The goal is to **rewrite (2.10) only in terms of the new variable \(\lambda\) and the function \(f(\lambda)\)** and to show that it reduces to  

\[
\boxed{\;
\frac{\kappa^{2}}{4}\Bigl(\frac{d\phi}{d\lambda}\Bigr)^{2}
=
\Bigl(\frac{1}{f}\frac{df}{d\lambda}\Bigr)^{2}
-\frac{1}{2f}\frac{d^{2}f}{d\lambda^{2}}
\;}\tag{3.2}
\]

All we need is ordinary calculus (chain rule, product rule) – no cosmology.

---

## 2.  Step‑by‑step derivation  

### 2.1  Useful identities for the change of variable  

\[
\lambda=\tanh z \quad\Longrightarrow\quad 
\frac{d\lambda}{dz}= \operatorname{sech}^{2}z = 1-\lambda^{2}.
\tag{1}
\]

Because  

\[
\operatorname{sech}z=\frac{1}{\cosh z}= \sqrt{1-\tanh^{2}z}
               =\sqrt{1-\lambda^{2}},
\]

we can write  

\[
\frac{1}{\cosh z}= \sqrt{1-\lambda^{2}} .
\tag{2}
\]

Thus the scale factor becomes a **pure function of \(\lambda\)**:

\[
a(z)=\ell\,\frac{f(\lambda)}{\cosh z}
    =\ell\,f(\lambda)\sqrt{1-\lambda^{2}}
    \equiv \ell\,\mathcal{A}(\lambda),\qquad 
\mathcal{A}(\lambda)=f(\lambda)\sqrt{1-\lambda^{2}} .
\tag{3}
\]

All derivatives with respect to \(z\) are obtained from derivatives with respect to \(\lambda\) by the chain rule (1).

---

### 2.2  First derivative \(da/dz\)

\[
\frac{da}{dz}= \frac{da}{d\lambda}\frac{d\lambda}{dz}
            = (1-\lambda^{2})\,\frac{da}{d\lambda}.
\tag{4}
\]

From (3),

\[
\frac{da}{d\lambda}= \ell\Bigl[ f'(\lambda)\sqrt{1-\lambda^{2}}
                     + f(\lambda)\,\frac{1}{2}(1-\lambda^{2})^{-1/2}(-2\lambda) \Bigr]
                  = \ell\Bigl( \sqrt{1-\lambda^{2}}\,f' - 
                               \frac{\lambda f}{\sqrt{1-\lambda^{2}}}\Bigr).
\tag{5}
\]

Insert (5) into (4) :

\[
\boxed{
\frac{da}{dz}= \ell(1-\lambda^{2})
               \Bigl( \sqrt{1-\lambda^{2}}\,f' - 
                      \frac{\lambda f}{\sqrt{1-\lambda^{2}}}\Bigr)
           = \ell\Bigl[(1-\lambda^{2})^{3/2}f' -\lambda(1-\lambda^{2})^{1/2}f\Bigr].
}
\tag{6}
\]

---

### 2.3  Second derivative \(d^{2}a/dz^{2}\)

Differentiate (4) once more:

\[
\frac{d^{2}a}{dz^{2}}
 = \frac{d}{dz}\!\Bigl[(1-\lambda^{2})\,\frac{da}{d\lambda}\Bigr]
 = \frac{d}{d\lambda}\!\Bigl[(1-\lambda^{2})\frac{da}{d\lambda}\Bigr]
   \frac{d\lambda}{dz}.
\]

Using \(\frac{d\lambda}{dz}=1-\lambda^{2}\) again,

\[
\frac{d^{2}a}{dz^{2}}
 =(1-\lambda^{2})\Bigl[-2\lambda\frac{da}{d\lambda}
      +(1-\lambda^{2})\frac{d^{2}a}{d\lambda^{2}}\Bigr].
\tag{7}
\]

Now we need \(d^{2}a/d\lambda^{2}\).  
From (5),

\[
\frac{d^{2}a}{d\lambda^{2}}
 =\ell\Bigl[
        -\frac{\lambda}{\sqrt{1-\lambda^{2}}}f'
        +\sqrt{1-\lambda^{2}}\,f''
        -\frac{f}{\sqrt{1-\lambda^{2}}}
        +\frac{\lambda^{2}f}{(1-\lambda^{2})^{3/2}}
       \Bigr].
\tag{8}
\]

Insert (5) and (8) into (7) and simplify (all factors of \(\ell\) will cancel later).  
A straightforward but lengthy algebraic manipulation gives

\[
\frac{d^{2}a}{dz^{2}}
 =\ell\Bigl[
          (1-\lambda^{2})^{2}f'' 
         -2\lambda(1-\lambda^{2})f'
         -(1-\lambda^{2})f
        \Bigr].
\tag{9}
\]

---

### 2.4  The combinations that appear in (2.10)

Recall that  

\[
a(z)=\ell f\sqrt{1-\lambda^{2}},\qquad 
a^{2}= \ell^{2}f^{2}(1-\lambda^{2}).
\tag{10}
\]

1. **First term**  

\[
\frac{2}{a^{2}}\Bigl(\frac{da}{dz}\Bigr)^{2}
 =\frac{2}{\ell^{2}f^{2}(1-\lambda^{2})}
   \bigl[\ell^{2}\bigl((1-\lambda^{2})^{3/2}f' 
                      -\lambda(1-\lambda^{2})^{1/2}f\bigr)^{2}\bigr]
\]

\[
\boxed{
= \frac{2(1-\lambda^{2})}{f^{2}}
   \Bigl[(1-\lambda^{2})f' -\lambda f\Bigr]^{2}} .
\tag{11}
\]

2. **Second term**  

\[
\frac{1}{a}\,\frac{d^{2}a}{dz^{2}}
 =\frac{1}{\ell f\sqrt{1-\lambda^{2}}}
   \,\ell\Bigl[(1-\lambda^{2})^{2}f'' 
          -2\lambda(1-\lambda^{2})f'-(1-\lambda^{2})f\Bigr]
\]

\[
\boxed{
= \frac{(1-\lambda^{2})^{3/2}}{f}
   \Bigl[f'' -\frac{2\lambda}{1-\lambda^{2}}f' -\frac{f}{1-\lambda^{2}}\Bigr]} .
\tag{12}
\]

---

### 2.5  Insert everything into the master equation  

Equation (2.10) with \(d=4\) reads

\[
\kappa\Bigl(\frac{d\phi}{dz}\Bigr)^{2}
= \frac{2}{a^{2}}\Bigl(\frac{da}{dz}\B

*Original question: [Unable to derive exact Coleman-de Luccia instanton differential equation 3.2](https://math.stackexchange.com/questions/5152539/unable-to-derive-exact-coleman-de-luccia-instanton-differential-equation-3-2) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
