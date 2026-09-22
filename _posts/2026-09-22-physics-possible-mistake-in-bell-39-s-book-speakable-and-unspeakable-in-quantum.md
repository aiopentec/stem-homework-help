---
layout: question
title: Possible Mistake in Bell&#39;s Book Speakable and Unspeakable in Quantum
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Possible Mistake in Bell&#39;s Book Speakable
  and Unspeakable in Quantum'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking – in plain language  

In Chapter 3 of J. S. Bell’s *Speakable and Unspeakable in Quantum Mechanics* Bell derives his famous inequality for a local hidden‑variable (LHV) theory.  
At one point he writes an expression that looks like  

\[
\Bigl|\,\int d\lambda\;\rho(\lambda)\,
\bigl[ A({\bf a},\lambda)B({\bf b},\lambda)-A({\bf a},\lambda)B({\bf b'} ,\lambda)\bigr] \Bigr|
\;\le\;
1+ \int d\lambda\;\rho(\lambda)\,
B({\bf b},\lambda)B({\bf b'},\lambda) .
\tag{★}
\]

The student wonders why the **absolute‑value sign is placed outside the integral** (i.e. outside the sum over the hidden variable λ) and not inside, as they would expect a term like  

\[
\int d\lambda\;\rho(\lambda)\,
\bigl|A({\bf a},\lambda)B({\bf b},\lambda)-A({\bf a},\lambda)B({\bf b'} ,\lambda)\bigr|
\]

instead. In short: **Is (★) a typo, or is the placement of the absolute value correct?**  

The answer is that the expression is **correct**. The absolute value belongs outside the integral because the inequality is obtained by applying the *triangle inequality* to the integrand **after** the factorisation that uses the fact that the hidden‑variable outcomes \(A,B\) are each ±1. Below we give a step‑by‑step derivation that makes the logic crystal clear.

---

## 2. Detailed derivation (every step shown)

### 2.1. Setting the stage  

* Hidden variable: a parameter λ that completely specifies the state of the pair of particles.  
* Distribution of hidden variables: a normalized probability density \(\rho(\lambda)\) with \(\rho(\lambda)\ge 0\) and \(\int d\lambda \,\rho(\lambda)=1\).  
* Measurement results: for any detector orientation **a**, the outcome of Alice’s measurement is a deterministic function  
  \[
  A({\bf a},\lambda)=\pm 1,
  \]
  and similarly for Bob,
  \[
  B({\bf b},\lambda)=\pm 1 .
  \]

The correlation predicted by any LHV theory for settings **a**, **b** is

\[
E({\bf a},{\bf b})\equiv
\int d\lambda\;\rho(\lambda)\;A({\bf a},\lambda)B({\bf b},\lambda) .
\tag{1}
\]

### 2.2. The quantity we want to bound  

Bell considers the difference of two correlations that share the same Alice setting **a** but have different Bob settings **b** and **b′**:

\[
\Delta\equiv E({\bf a},{\bf b})-E({\bf a},{\bf b'}).
\]

Using (1),

\[
\Delta
 =\int d\lambda\;\rho(\lambda)
   \Bigl[ A({\bf a},\lambda)B({\bf b},\lambda)
        -A({\bf a},\lambda)B({\bf b'},\lambda)\Bigr].
\tag{2}
\]

Factor out the common factor \(A({\bf a},\lambda)\):

\[
\Delta
 =\int d\lambda\;\rho(\lambda)\;
   A({\bf a},\lambda)\,\bigl[ B({\bf b},\lambda)-B({\bf b'},\lambda)\bigr].
\tag{3}
\]

### 2.3. Using the fact that \(A,B=\pm 1\)

Because \(A({\bf a},\lambda)^2 = 1\), we can multiply the integrand by the factor

\[
1 = \frac{1}{2}\Bigl[1+ B({\bf b},\lambda)B({\bf b'},\lambda)\Bigr]
      +\frac{1}{2}\Bigl[1- B({\bf b},\lambda)B({\bf b'},\lambda)\Bigr],
\]

but a simpler route—used by Bell—is to rewrite the bracket:

\[
B({\bf b},\lambda)-B({\bf b'},\lambda)
 = B({\bf b},\lambda)\bigl[1- B({\bf b},\lambda)B({\bf b'},\lambda)\bigr].
\tag{4}
\]

(Indeed, because \(B({\bf b},\lambda)^2=1\), multiplying the right‑hand side out gives the left‑hand side.)

Insert (4) into (3):

\[
\Delta
 =\int d\lambda\;\rho(\lambda)\;
   A({\bf a},\lambda)\,B({\bf b},\lambda)\,
   \bigl[1- B({\bf b},\lambda)B({\bf b'},\lambda)\bigr].
\tag{5}
\]

Now take the **absolute value** of \(\Delta\). Since the absolute value of an integral is bounded by the integral of the absolute value (the triangle inequality),

\[
|\Delta|
 \le \int d\lambda\;\rho(\lambda)\;
      \bigl| A({\bf a},\lambda)B({\bf b},\lambda)
            \bigl[1- B({\bf b},\lambda)B({\bf b'},\lambda)\bigr]\bigr|.
\tag{6}
\]

But \(|A({\bf a},\lambda)B({\bf b},\lambda)| = 1\) (product of two ±1 numbers), so the absolute value drops out of that factor:

\[
|\Delta|
 \le \int d\lambda\;\rho(\lambda)\;
      \bigl|1- B({\bf b},\lambda)B({\bf b'},\lambda)\bigr|.
\tag{7}
\]

Because the quantity inside the absolute value is either \(0\) or \(2\) (again a difference of two ±1 numbers), its absolute value equals the expression itself:

\[
|1- B({\bf b},\lambda)B({\bf b'},\lambda)|
   = 1- B({\bf b},\lambda)B({\bf b'},\lambda).
\tag{8}
\]

Thus

\[
|\Delta|
 \le \int d\lambda\;\rho(\lambda)\;
      \bigl[1- B({\bf b},\lambda)B({\bf b'},\lambda)\bigr].
\tag{9}
\]

Finally split the integral into two pieces:

\[
|\Delta|
 \le \underbrace{\int d\lambda\;\rho(\lambda)}_{=1}
     \;-\;
     \underbrace{\int d\lambda\;\rho(\lambda)\;
                B({\bf b},\lambda)B({\bf b'},\lambda)}_{=E({\bf b},{\bf b'})}.
\]

Re‑arranging gives the **Bell inequality** in the form that appears in the book:

\[
\boxed{ \;
|E({\bf a},{\bf b})-E({\bf a},{\bf b'})|
   \;\le\; 1 + E({\bf b},{\bf b'})
\; } .
\tag{10}
\]

Equation (10) is exactly the highlighted expression (★).  

**Key point:** the absolute value surrounds the *whole* left‑hand side, i.e. the difference of the two *integrated* correlation functions. It is **not** inside the integral. The inequality follows from the triangle inequality **after** the factorisation that uses \(A^2 = B^2 = 1\); moving the absolute value inside the integral would be a *different* (and generally weaker) bound and is **not** what Bell wrote.

---

## 3. Final answer  

The expression in Bell’s book is **correct**; the absolute‑value bars are meant to enclose the entire difference of the two correlation integrals, not the integrand itself. The derivation uses:

1. Factorisation of the difference of the two terms,
2. The fact that each hidden‑variable outcome is ±1,
3. The triangle inequality applied **after** the factorisation.

Hence no typo is present in the book.

---

## 4. Common mistakes when reproducing this derivation  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Placing the absolute value inside the integral** (i.e. writing \(\int \rho|\dots|\)). | The triangle inequality is applied to the *integral* of the product, not to each point‑wise term. Putting the absolute value inside would give a weaker (or sometimes meaningless) bound. | Keep the absolute value outside until after you have used the identity \(B({\bf b})-B({\bf b'}) = B({\bf b})[1-B({\bf b})B({\bf b'})]\). |
| **Forgetting that \(A\) and \(B\) are ±1** and therefore \(|A B| = 1\). | Without this you cannot drop the absolute value of the prefactor and you’ll end up with an extra (unnecessary) factor. | Explicitly note \(A({\bf a},\lambda)^2 = B({\bf b},\lambda)^2 = 1\) before applying the triangle inequality. |
| **Using \( |1-xy| = 1-xy\) without justification**. | This holds only because \(x,y = \pm1\) ⇒ \(xy = \pm1\) ⇒ the bracket is either 0 or 2, both non‑negative. | State the possible values of \(xy\) and verify the sign before dropping the absolute value. |
| **Mixing up the order of the settings** (e.g., writing \(E({\bf b},{\bf a})\) instead of \(E({\bf a},{\bf b})\)). | Correlation functions are symmetric for the singlet state, but the algebraic steps rely on a consistent labelling of the two parties. | Keep a clear table of which variable belongs to Alice and which to Bob throughout the derivation. |
| **Skipping the step where the integral of \(\rho(\lambda)\) is set to 1**. | The normalization \(\int\rho =1\) is essential to obtain the constant “1” on the right‑hand side of the inequality. | After expanding the integral, explicitly write \(\int d\lambda\,\rho(\lambda)=1\). |

By being careful about the placement of the absolute value, the ±1 property of the hidden‑variable outcomes, and the proper use of the triangle inequality, the derivation proceeds smoothly and the result matches Bell’s original formula.

*Original question: [Possible Mistake in Bell&#39;s Book Speakable and Unspeakable in Quantum](https://physics.stackexchange.com/questions/876267/possible-mistake-in-bells-book-speakable-and-unspeakable-in-quantum) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
