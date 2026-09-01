---
layout: question
title: Maximum Norm of random vectors
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Maximum Norm of random vectors'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## Problem statement (re‑phrased)

Let  

\[
X_{1},\dots ,X_{N}\in\mathbb R^{n}
\]

be independent copies of a random vector \(X=(X_{1},\dots ,X_{n})\) whose coordinates  

* are independent,  
* have mean \(0\) and variance \(1\) (so \(X\) is **isotropic**), and  
* satisfy a sub‑gaussian bound  

\[
\|X_{ij}\|_{\psi_{2}}\le K\qquad (1\le i\le N,\;1\le j\le n)
\]

for some absolute constant \(K\ge 1\).

Show that the **expected largest Euclidean norm** among the \(N\) vectors is bounded by  

\[
\boxed{\;
\mathbb E\Bigl[\max_{1\le i\le N}\|X_i\|_{2}\Bigr]
   \;\le\; C K^{2}\Bigl(\sqrt n+\sqrt{\log N}\Bigr)
\;}
\]

where \(C>0\) is an absolute constant (independent of \(n,N,K\)).  
In particular, if the coordinates are standard sub‑gaussian (\(K=1\)),  

\[
\mathbb E\Bigl[\max_{i\le N}\|X_i\|_{2}\Bigr]\le C\bigl(\sqrt n+\sqrt{\log N}\bigr).
\]

---

## Full solution, step by step  

We proceed in three stages:

1. **Concentration of the Euclidean norm of a single vector.**  
2. **Sub‑gaussian control of the deviation \(\|X_i\|_{2}-\sqrt n\).**  
3. **Bounding the maximum over \(i=1,\dots ,N\).**

---

### 1. Concentration of \(\|X\|_{2}\) for an isotropic sub‑gaussian vector  

Because the coordinates are independent, centred, unit‑variance and sub‑gaussian, the vector \(X\) is isotropic:
\[
\mathbb E X X^{\top}=I_{n}.
\]

A standard result (Corollary 3.12 in Vershynin) states that for every \(t\ge 0\)

\[
\boxed{\;
\mathbb P\!\Bigl(\bigl|\|X\|_{2}-\sqrt n\bigr|\ge t\Bigr)
   \le 2\exp\!\Bigl(-c\,\frac{t^{2}}{K^{4}}\Bigr)
\;}
\tag{1}
\]

where \(c>0\) is an absolute constant.  
The proof uses the Hanson–Wright inequality applied to \(\|X\|_{2}^{2}=\sum_{j=1}^{n}X_{j}^{2}\).

---

### 2. Sub‑gaussian norm of the deviation  

Recall the definition of the sub‑gaussian (Orlicz) norm:

\[
\|Y\|_{\psi_{2}}:=\inf\{s>0:\;\mathbb E\exp(Y^{2}/s^{2})\le 2\}.
\]

A random variable \(Y\) satisfies a tail bound  

\[
\mathbb P(|Y|\ge t)\le 2\exp(-t^{2}/\sigma^{2})\quad\forall t\ge0
\]

iff \(\|Y\|_{\psi_{2}}\le C\sigma\) for some absolute constant \(C\).  
Comparing (1) with this form gives

\[
\boxed{\;
\bigl\|\; \|X\|_{2}-\sqrt n\;\bigr\|_{\psi_{2}}\le C_{1}K^{2}
\;}
\tag{2}
\]

for another absolute constant \(C_{1}\).

Thus each deviation \(Y_{i}:=\|X_{i}\|_{2}-\sqrt n\) is a centred sub‑gaussian random variable with
\(\|Y_{i}\|_{\psi_{2}}\le C_{1}K^{2}\).

---

### 3. From a single vector to the maximum of \(N\) vectors  

#### 3.1 A generic maximal‑sub‑gaussian inequality  

If \(Y_{1},\dots ,Y_{N}\) are (not necessarily independent) sub‑gaussian with the same \(\psi_{2}\)‑norm \(\sigma\), then (Lemma 2.2.2 in the book)

\[
\mathbb E\Bigl[\max_{1\le i\le N}|Y_{i}|\Bigr]\le C_{2}\,\sigma\sqrt{\log N},
\tag{3}
\]

where \(C_{2}>0\) is absolute.  
The proof integrates the tail bound (union bound + (1)).

#### 3.2 Apply (3) to the deviations  

Take \(Y_{i}= \|X_{i}\|_{2}-\sqrt n\).  
From (2) we have \(\sigma = C_{1}K^{2}\). Plugging into (3),

\[
\mathbb E\Bigl[\max_{i\le N}\bigl|\|X_{i}\|_{2}-\sqrt n\bigr|\Bigr]
    \le C_{2}\,C_{1}K^{2}\sqrt{\log N}
    = C_{3}K^{2}\sqrt{\log N}.
\tag{4}
\]

#### 3.3 Add back the deterministic part \(\sqrt n\)

For any numbers \(a_{i}\),

\[
\max_{i}a_{i}\le \sqrt n + \max_{i}|a_{i}-\sqrt n|.
\]

Apply expectation and (4):

\[
\begin{aligned}
\mathbb E\Bigl[\max_{i\le N}\|X_{i}\|_{2}\Bigr]
&\le \sqrt n + 
   \mathbb E\Bigl[\max_{i\le N}\bigl|\|X_{i}\|_{2}-\sqrt n\bigr|\Bigr]   \\
&\le \sqrt n + C_{3}K^{2}\sqrt{\log N}.
\end{aligned}
\]

Finally absorb the constant in front of \(\sqrt n\) (the term \(\sqrt n\) itself is deterministic, so we may multiply it by a harmless absolute constant) and write

\[
\boxed{\;
\mathbb E\Bigl[\max_{i\le N}\|X_{i}\|_{2}\Bigr]
   \;\le\; C K^{2}\bigl(\sqrt n+\sqrt{\log N}\bigr)
\;}
\]

with a universal constant \(C>0\).  
When \(K=1\) (standard sub‑gaussian entries) the bound simplifies to  

\[
\mathbb E\max_{i\le N}\|X_{i}\|_{2}\le C\bigl(\sqrt n+\sqrt{\log N}\bigr).
\]

---

## Final answer  

\[
\boxed{\displaystyle 
\mathbb{E}\Bigl[\max_{1\le i\le N}\|X_i\|_{2}\Bigr]
\le C K^{2}\bigl(\sqrt{n}+\sqrt{\log N}\bigr)
}
\]

where \(K=\max_{i,j}\|X_{ij}\|_{\psi_{2}}\) and \(C>0\) is an absolute constant.

---

## Common mistakes to avoid  

| Mistake | Why it is wrong | How to fix it |
|---------|----------------|---------------|
| **Forgetting the isotropic assumption.** | Without \(\mathbb E XX^{\top}=I_{n}\) the mean of \(\|X\|_{2}\) is not \(\sqrt n\); the concentration inequality (1) no longer holds. | Verify that the coordinates have variance 1, which guarantees isotropy. |
| **Bounding \(\|X_i\|_{2}\) directly instead of its deviation.** | \(\|X_i\|_{2}\) is not sub‑gaussian (its tail is only sub‑exponential). The sub‑gaussian property holds for the *centered* quantity \(\|X_i\|_{2}-\sqrt n\). | First prove (1) for the deviation, then apply the maximal inequality to \(|\|X_i\|_{2}-\sqrt n|\). |
| **Using the \(\psi_{2}\)–norm of the coordinates instead of that of the deviation.** | The bound \(\|X_{ij}\|_{\psi_{2}}\le K\) does **not** directly give \(\|\|X_i\|_{2}\|_{\psi_{2}}\le K\). | Use Corollary 3.12 (or Hanson–Wright) to translate coordinate sub‑gaussianity into (2). The resulting \(\psi_{2}\)–norm scales like \(K^{2}\). |
| **Dropping the constant \(K^{2}\).** | The concentration (1) has a denominator \(K^{4}\), so the \(\psi_{2}\) norm of the deviation is proportional to \(K^{2}\). Ignoring it yields a bound that is false for large \(K\). | Keep the factor \(K^{2}\) throughout; it appears in the final constant. |
| **Applying the union bound after taking expectations.** | The bound \(\mathbb E\max_i Y_i\le \max_i \mathbb E Y_i\) is false; expectation does **not** commute with max. | Use the tail‑integration method (Lemma 2.2.2) that gives (3) directly from the sub‑gaussian tail.

*Original question: [Maximum Norm of random vectors](https://math.stackexchange.com/questions/5148382/maximum-norm-of-random-vectors) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
