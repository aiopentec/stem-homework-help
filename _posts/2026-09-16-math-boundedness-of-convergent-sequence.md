---
layout: question
title: Boundedness of convergent sequence.
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Boundedness of convergent sequence.'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1. What is being asked?

We have a **convergent sequence** \((a_n)_{n\in\mathbb N}\) of real numbers.  
We must show that **every convergent sequence is bounded**; i.e. there is a real number \(M>0\) such that  

\[
|a_n|\le M\qquad\text{for every }n\in\mathbb N .
\]

The student wonders whether we can simply take  

\[
M=\max\{|a_1|,|a_2|,\dots\}
\]

(the “maximum of all the absolute values”) and, if a maximum does not exist, take a number larger than that “supposed” maximum.  
We have to explain why this idea does **not** work as a proof and give a correct proof.

---

## 2. Detailed proof that a convergent sequence is bounded  

Let \((a_n)\) be a sequence of real numbers that converges to a limit \(L\in\mathbb R\).  
By definition of convergence:

> For every \(\varepsilon>0\) there exists an integer \(N\) such that  
> \[
> n\ge N \;\Longrightarrow\; |a_n-L|<\varepsilon .
> \]

We will use \(\varepsilon=1\).  

### Step 1 – control the “tail’’ of the sequence  

Choose \(\varepsilon=1\).  
Then there is an integer \(N\) with  

\[
n\ge N \;\Longrightarrow\; |a_n-L|<1 .
\]

For those indices we can bound \(|a_n|\) as follows:

\[
|a_n| = |a_n-L+L| \le |a_n-L|+|L|
            < 1+|L| .
\]

Thus every term **after** the \(N\)-th one satisfies  

\[
|a_n|\le 1+|L|\qquad (n\ge N).
\]

### Step 2 – bound the finitely many “initial’’ terms  

The set \(\{\,|a_1|,|a_2|,\dots,|a_{N-1}|\,\}\) contains only finitely many numbers, so it has a **maximum** (the real numbers are totally ordered and every finite non‑empty set has a maximum).  

Define  

\[
M_0:=\max\{|a_1|,|a_2|,\dots,|a_{N-1}|\}.
\]

If \(N=1\) this set is empty; in that case we may set \(M_0:=0\).

### Step 3 – combine the two bounds  

Let  

\[
M:=\max\bigl\{M_0,\;1+|L|\bigr\}.
\]

Both \(M_0\) and \(1+|L|\) are real numbers, so their maximum exists.  
Now we check the two possible cases for an arbitrary index \(n\).

*If \(n\ge N\):*  
\(|a_n|\le 1+|L|\le M\) by the definition of \(M\).

*If \(n<N\):*  
\(|a_n|\le M_0\le M\) again by the definition of \(M\).

Hence **for every \(n\in\mathbb N\) we have \(|a_n|\le M\)**.  
Therefore the sequence \((a_n)\) is bounded.

---

## 3. Why the “maximum of all terms’’ idea does not work

| Idea | Why it is not a valid proof |
|------|----------------------------|
| “Take \(M=\max\{|a_n|:n\in\mathbb N\}\). If a maximum does not exist, take a number larger than that supposed maximum.” | *Circular reasoning*: To speak of the **maximum of all the absolute values** we must already know that such a maximum exists. The existence of that maximum is exactly what we are trying to prove. Without a prior bound we cannot guarantee the set \(\{|a_n|:n\in\mathbb N\}\) has a supremum that is finite, nor that a maximum exists. |
| “If there is no maximum, pick any number larger than the (non‑existent) maximum.” | The phrase “larger than the non‑existent maximum’’ is meaningless: a number larger than something that does not exist cannot be defined. Moreover, we cannot simply *choose* a number larger than every term unless we have already shown that the collection of terms is bounded above. |
| “Because the sequence converges, its terms must stay close to the limit, so the set of absolute values must have a maximum.” | Convergence guarantees that the terms eventually lie inside any prescribed neighbourhood of the limit, **but only after some index \(N\)**. The finitely many terms before \(N\) might be arbitrarily large; we need a separate argument (the finiteness argument above) to bound those. The existence of a global maximum is not automatic. |

In short, the “maximum of all terms’’ approach **assumes** the very property (boundedness) we are trying to establish, making the argument circular and invalid.

---

## 4. Final answer  

A convergent sequence \((a_n)\) of real numbers is always bounded.  
A correct proof proceeds by:

1. Using the definition of convergence with \(\varepsilon=1\) to bound all terms from some index \(N\) onward by \(1+|L|\);
2. Bounding the finitely many preceding terms by taking their maximum;
3. Taking the larger of the two numbers as a global bound \(M\).

Thus there exists a real number \(M\) such that \(|a_n|\le M\) for every \(n\).

---

## 5. Common Mistakes  

| Mistake | Explanation |
|---------|-------------|
| **Assuming a maximum exists before proving boundedness** | The set \(\{|a_n|:n\in\mathbb N\}\) may have no maximum (e.g., \(a_n=n\)). Boundedness must be shown first. |
| **Using “take a number larger than the maximum’’ when the maximum does not exist** | “Larger than the non‑existent maximum’’ is undefined; you need a concrete finite upper bound, which comes from the convergence argument. |
| **Ignoring the finitely many early terms** | Convergence only controls the tail of the sequence. Early terms can be arbitrarily large unless handled separately. |
| **Choosing \(\varepsilon\) that depends on the sequence** | The proof works for any fixed \(\varepsilon>0\); \(\varepsilon=1\) is a convenient choice. Using a value that itself depends on the unknown bound leads to circularity. |
| **Working with “supremum’’ without justification** | The supremum exists for any non‑empty set of real numbers, but it may be \(+\infty\). One must first prove the supremum is finite; otherwise it does not give a bound. |

Avoid these pitfalls by following the three‑step argument shown above.

*Original question: [Boundedness of convergent sequence.](https://math.stackexchange.com/questions/5149460/boundedness-of-convergent-sequence) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
