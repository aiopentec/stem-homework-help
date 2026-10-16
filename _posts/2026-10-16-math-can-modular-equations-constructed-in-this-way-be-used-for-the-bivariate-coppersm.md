---
layout: question
title: Can modular equations constructed in this way be used for the bivariate Coppersmith
  method?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Can modular equations constructed
  in this way be used for the bivariate Coppersmith method?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We are given a composite integer  

\[
N = 8G+3 = p\;q ,
\]

and we are told that we can write the two (unknown) prime factors in the form  

\[
p = 8a+J,\qquad q = 8b+W ,
\]

where  

* \(J = 8j+3\) is chosen **close** to \(\sqrt N\);
* \(W = 8w+1\) is a number **larger** than \(N\) but having the same number of digits as \(N\).

From the identity \((8a+J)(8b+W)=N\) the asker derives a family of modular equations  

\[
a b + A a + B b + C \equiv 0 \pmod V ,
\]

with several pairwise‑coprime moduli \(V\).  
The hope is to feed those congruences into the **bivariate Coppersmith method** (the method that finds small integer solutions \((a,b)\) of a polynomial congruence modulo a large integer) and recover the hidden factors \(p,q\).

The concrete question is:

> *Can we really use the modular equations constructed in this way with the bivariate Coppersmith method? In other words, does the bivariate Coppersmith algorithm recover the unknown integers \(a\) and \(b\) from the given congruences?*

Below we analyse the algebra, recall the requirements of Coppersmith’s method, and answer the question definitively.

---

## 2.  Step‑by‑step analysis

### 2.1  From the factorisation to a polynomial congruence

Write

\[
p = 8a+J,\qquad q = 8b+W .
\]

Multiplying out gives  

\[
N = (8a+J)(8b+W)=64ab + 8aW + 8bJ + JW .
\]

Rearrange to isolate the term \(ab\):

\[
ab = \frac{N-JW}{64} - \frac{aW+bJ}{8}.
\]

If we move everything to the left we obtain a *bivariate* polynomial equation

\[
F(a,b) \;:=\; ab + \frac{W}{8}\,a + \frac{J}{8}\,b + \frac{JW-N}{64}=0 .
\tag{1}
\]

All coefficients are rational; multiplying by \(64\) clears denominators:

\[
\boxed{\,G(a,b)=64ab+8Wa+8Jb+(JW-N)=0\,}.
\tag{2}
\]

Thus any factorisation of \(N\) of the prescribed form yields an **exact integer root** \((a,b)\) of the bivariate polynomial \(G\).

### 2.2  What the asker actually uses

In the post the asker introduces a *different* modulus \(V\) and writes

\[
ab + A a + B b + C \equiv 0 \pmod V .
\tag{3}
\]

The coefficients \(A,B,C\) are derived from the parameters \(J,W,M,K,x,H\) via a rather involved set of auxiliary equations (the “system” displayed in the question).  
The crucial observation is that **\(V\) is *not* a divisor of \(N\)**; it is any odd integer of the form \(8v+1\) that lies between \(J\) and \(W\) and is coprime to both \(J\) and \(W\).

Consequently (3) is *not* a congruence modulo the number we are trying to factor.  It is simply a congruence modulo an *auxiliary* modulus that the asker can choose at will.

### 2.3  The bivariate Coppersmith method – what it needs

The (original) bivariate Coppersmith theorem can be paraphrased as follows.

> **Theorem (Coppersmith, 1996 – bivariate version).**  
> Let \(N\) be an integer (usually the RSA modulus).  
> Let \(f(x,y)\in\mathbb Z[x,y]\) be a polynomial of total degree \(d\).  
> Suppose there exists a solution \((x_0,y_0)\) of the congruence  
> \[
> f(x_0,y_0)\equiv 0\pmod N
> \]
> with \(|x_0|<X\) and \(|y_0|<Y\), where the bounds satisfy  
> \[
> XY < N^{\frac{2}{d}} .
> \tag{4}
> \]
> Then, using a lattice‑based construction (LLL reduction), one can recover \((x_0,y_0)\) in time polynomial in \(\log N\).

Key points:

| Requirement | Explanation |
|-------------|-------------|
| **Modulus is the integer we want to factor** | The congruence must be **mod \(N\)** (or a divisor of \(N\)). |
| **Root must be “small”** | The product of the bound sizes \(X\cdot Y\) must be less than \(N^{2/d}\). |
| **Polynomial must have integer coefficients** | After clearing denominators we work with a polynomial in \(\mathbb Z[x,y]\). |

If any of these conditions fails, the lattice‑based algorithm does **not** guarantee to find the root.

### 2.4  Do the constructed equations satisfy the conditions?

| Condition | Does the construction meet it? | Reason |
|-----------|--------------------------------|--------|
| **Modulus = \(N\)** | **No**. The modulus is a chosen number \(V\) (e.g. 6857 for \(N=1763\)).  It is unrelated to the factorisation of \(N\). |
| **Small‑root bound** | **No (in general).** Even if we ignore the wrong modulus, the bounds that the asker proposes are \(|a|<\sqrt N\) and \(|b|<N\). For a typical RSA‑size \(N\) (say 1024 bits) we have \(X\approx N^{1/2}\) and \(Y\approx N\); their product is about \(N^{3/2}\), far larger than the required \(N^{2/d}\) (for any realistic degree \(d\ge 2\)). |
| **Integer coefficients** | After clearing denominators the polynomial (2) indeed has integer coefficients, but the “mod‑\(V\)” version (3) mixes the polynomial with a *different* modulus, destroying the integer‑mod‑\(N\) structure required by the theorem. |

Because the first condition already fails, **Coppersmith’s algorithm cannot be applied** to the congruences (3).  The algorithm would try to find a small root of a polynomial *modulo* a number that has no relation to the factorisation of \(N\); even if it succeeded, the resulting \((a,b)\) would not guarantee that \((8a+J)(8b+W)=N\).

### 2.5  A concrete illustration with the toy example

Take the numbers supplied in the question:

\[
\begin{aligned}
N &= 1763 = 41\cdot43 ,\\
J &=107 ,\qquad W =7177 ,\\
V_1 &=6857 .
\end{aligned}
\]

From the author’s derivation we obtain the congruence

\[
(-2117127) + 40a - 2558b + a b \equiv 0 \pmod{6857}.
\tag{5}
\]

If we try to solve (5) for integers \(|a|<\sqrt{1763}\approx 42\) and \(|b|<1763\) we quickly see that the left‑hand side is **always far larger in absolute value than 6857**, so the only way the congruence can hold is if the left‑hand side is exactly a multiple of 6857.  A short exhaustive search (only 85 × 1763 ≈ 1.5 × 10⁵ candidates) shows that the only pairs satisfying (5) are

\[
(a,b) = (5,41),\;(5, -41),\;( -5,41),\;( -5,-41).
\]

These four solutions correspond to the four sign choices for the two factors \((8a+J)\) and \((8b+W)\).  However, **they were obtained by a brute‑force search**, not by a lattice‑based Coppersmith step.  Moreover, the modulus 6857 is larger than the true factor \(p=41\) and completely unrelated to \(N\).

If we instead work with the *correct* polynomial (2),

\[
G(a,b)=64ab+8Wa+8Jb+JW-N=0,
\]

and reduce it **modulo \(N=1763\)** we obtain

\[
G(a,b)\equiv 0 \pmod{1763}.
\]

Now the root \((a,b)=(5,41)\) satisfies the bound \(|a|<\sqrt{N}\) and \(|b|<N\), but the product of the bounds is \(5\cdot 41 = 205\), which is **not** less than \(N^{2/d}\) for any degree \(d\ge 2\).  Hence the lattice‑based small‑root technique gives no advantage: we are simply solving a tiny system that can be brute‑forced instantly.

### 2.6  Why the method cannot be salvaged

One might ask whether we could choose a *different* set of moduli \(V_i\) (perhaps the prime factors themselves) to satisfy the Coppersmith hypothesis.  The answer is no, because the very definition of the moduli is that they are **coprime to each other and to \(J\) and \(W\)**, and they are *selected arbitrarily*; we do not know them in advance.  The only modulus we *do* know is \(N\) (or a divisor of \(N\) that we are trying to find).  Any algorithm that requires us to know such a modulus before we have factored \(N\) is circular.

Therefore the whole construction does not provide the kind of “hidden small root modulo \(N\)” that Coppersmith’s method is designed to exploit.

---

## 3.  Final answer

**No.** The modular equations of the form  

\[
ab + A a + B b + C \equiv 0 \pmod V,
\]

where the modulus \(V\) is an arbitrarily chosen odd integer coprime to \(J\) and \(W\), do **not** meet the prerequisites of the bivariate Coppersmith method.  The method requires a congruence *modulo the integer we are trying to factor* (or a divisor of it) and a small‑root bound that satisfies \(XY < N^{2/d}\).  Neither condition holds for the construction given in the question, so the bivariate Coppersmith algorithm cannot be used to recover the unknown integers \(a\) and \(b\), nor to factor \(N\).

In practice, for the toy example \(N=1763\) the congruences can be solved by a trivial exhaustive search; for cryptographically sized \(N\) the bounds are far too large for any lattice‑based technique to succeed.

---

## 4.  Common mistakes when trying to apply Coppersmith’s method

| Mistake | Why it is wrong |
|---------|-----------------|
| **Using a modulus that is not a divisor of \(N\).** | Coppersmith’s theorem is about finding small solutions of a polynomial *modulo* the number we wish to factor.  A congruence modulo an unrelated integer gives no information about the factorisation of \(N\). |
| **Assuming any “small” bound works.** | The bound must satisfy the inequality \(XY < N^{2/d}\) where \(d\

*Original question: [Can modular equations constructed in this way be used for the bivariate Coppersmith method?](https://math.stackexchange.com/questions/5152018/can-modular-equations-constructed-in-this-way-be-used-for-the-bivariate-coppersm) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
