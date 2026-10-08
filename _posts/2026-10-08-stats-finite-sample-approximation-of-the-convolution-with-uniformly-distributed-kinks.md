---
layout: question
title: Finite sample approximation of the convolution with uniformly distributed kinks
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Finite sample approximation of the
  convolution with uniformly distributed kinks'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

We have a *random* family of piece‑wise smooth functions.  
Each realisation  

\[
f(x)=h(x-L)\qquad L\in\mathbb R
\]

has a **kink** (a jump in the first derivative) at a location \(L\).  
The kink location \(L\) is drawn from some probability distribution with density \(p_L(\ell)\).  
Different realisations are independent, so the locations of the kinks are almost surely different (the event “two kinks coincide’’ has probability 0).

From a sample of \(n\) such functions we form the **sample mean**

\[
\bar f_n(x)=\frac1n\sum_{i=1}^{n}f_i(x)
\]

and we notice that every individual jump in \(\bar f_n\) is **smaller** than the original jump of any single member of the sample – the jump is “attenuated’’ because the jumps are spread out over different \(L\)’s.

The question:  

*Does this attenuation of the derivative jumps amount to an approximation of a convolution?*  
*In other words, as the sample size \(n\) grows, does \(\bar f_n\) converge to the convolution of a “unit‑jump’’ kernel with the distribution of the kink locations?*

---

## 2.  Step‑by‑step solution  

### 2.1  Formal model  

1. **Base shape** – let  

   \[
   g(x)=
   \begin{cases}
   0, & x<0\\[4pt]
   J\,x, & x\ge 0,
   \end{cases}
   \qquad J>0
   \]

   i.e. a function that is linear with slope \(J\) for \(x\ge0\) and flat for \(x<0\).  
   Its first derivative is  

   \[
   g'(x)=J\mathbf 1_{\{x\ge0\}},
   \]

   which has a **jump of size \(J\)** at the origin.

2. **Random shift** – a random variable \(L\) with density \(p_L(\ell)\).  
   Define the random function  

   \[
   f(x)=g(x-L)=g\bigl((x-L)\bigr).
   \]

   Its derivative is  

   \[
   f'(x)=J\mathbf 1_{\{x\ge L\}},
   \]

   i.e. a jump of size \(J\) located at the random point \(L\).

3. **Independent sample** – draw \(L_1,\dots ,L_n\) i.i.d. from \(p_L\) and set  

   \[
   f_i(x)=g(x-L_i),\qquad i=1,\dots ,n .
   \]

### 2.2  What does the *population* mean look like?  

The expectation (population mean) of the random function at a fixed \(x\) is  

\[
\begin{aligned}
\mu(x)&:=\mathbb E[f(x)]\\[4pt]
     &=\int_{-\infty}^{\infty} g(x-\ell)\,p_L(\ell)\,d\ell .
\end{aligned}
\]

The integral is precisely the **convolution** of \(g\) with the density \(p_L\):

\[
\boxed{\;\mu = g * p_L\;}
\qquad\text{(definition of convolution)} .
\]

Because \(g\) has a single jump at 0, the convolution “smears’’ that jump according to the spread of the random locations \(L\). The result \(\mu(x)\) is a *smooth* function (if \(p_L\) is continuous) – the original sharp jump has been **attenuated**.

### 2.3  Sample mean as an estimator of the convolution  

The sample mean is  

\[
\bar f_n(x)=\frac1n\sum_{i=1}^{n}g(x-L_i).
\]

For each fixed \(x\) the random variables \(Y_i:=g(x-L_i)\) are i.i.d. with mean \(\mu(x)\) and finite variance (because \(g\) is bounded on any compact interval).  

By the **Weak Law of Large Numbers (WLLN)**  

\[
\bar f_n(x)\xrightarrow[]{\;P\;}\mu(x)\qquad(n\to\infty).
\]

If we assume, in addition, that  

* the density \(p_L\) is bounded, and  
* \(g\) is bounded on any compact set,  

then the **Uniform Strong Law of Large Numbers** guarantees

\[
\sup_{x\in K}\bigl|\bar f_n(x)-\mu(x)\bigr|\;\xrightarrow[]{\;a.s.\;}\;0
\]

for every compact interval \(K\). Thus the whole graph of the sample mean converges (almost surely) to the convolution \(g*p_L\).

### 2.4  Interpretation of “attenuation’’  

The derivative of the sample mean is  

\[
\bar f_n'(x)=\frac1n\sum_{i=1}^{n}J\mathbf 1_{\{x\ge L_i\}}
          =J\;\frac{N_n(x)}{n},
\]

where \(N_n(x)=\#\{i: L_i\le x\}\) is the empirical count of kinks to the left of \(x\).  

As \(n\) grows,  

\[
\frac{N_n(x)}{n}\;\xrightarrow[]{\;P\;}\;F_L(x)=\int_{-\infty}^{x}p_L(\ell)\,d\ell,
\]

the cumulative distribution function of the kink locations. Hence  

\[
\bar f_n'(x)\;\xrightarrow[]{\;P\;}\;J\,F_L(x)=\bigl(g'*p_L\bigr)(x),
\]

which is exactly the derivative of the convolution \(\mu(x)\).  

Thus the *jump amplitude* that appears in any single realisation (size \(J\)) is **spread out** over the whole domain according to the distribution of the kink locations; the observed attenuation is nothing else than the smoothing produced by convolution.

### 2.5  Summary of the logical chain  

| Step | What we have | What it gives |
|------|--------------|---------------|
| 1.   | Random kink location \(L\) with density \(p_L\) | A random shift operator |
| 2.   | Function \(f(x)=g(x-L)\) with a jump of size \(J\) at \(L\) | Individual functions are nonsmooth |
| 3.   | Sample mean \(\bar f_n(x)=\frac1n\sum g(x-L_i)\) | Empirical average of shifted jumps |
| 4.   | \(\mathbb E[f(x)]=g*p_L\) | The *population* mean is a convolution |
| 5.   | LLN (pointwise or uniform) | \(\bar f_n \to g*p_L\) as \(n\to\infty\) |
| 6.   | Derivative of \(\bar f_n\) converges to \(J\,F_L\) | The jump is “attenuated’’ exactly as the convolution predicts |

Therefore, **the attenuation of the derivative jumps in the sample mean does constitute an approximation to the convolution of the unit‑jump kernel with the distribution of kink locations, and the approximation becomes exact in the limit of an infinite sample** (under the usual independence and finite‑variance assumptions).

---

## 3.  Final answer  

Yes.  
If the kink locations are drawn independently from a distribution with density \(p_L\), the expected (population) mean of the random functions is the convolution  

\[
\mu(x)=\bigl(g * p_L\bigr)(x),
\]

where \(g\) is the deterministic shape that carries a unit derivative jump.  
By the law of large numbers the empirical mean of \(n\) sampled functions converges (pointwise, and uniformly on compact sets under mild regularity) to \(\mu\).  
Consequently, the observed attenuation of each derivative jump is precisely the smoothing effect produced by that convolution, and the approximation improves without bound as the sample size increases.

---

## 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing the sample *mean* with the *median* of the functions.** | The median does **not** have the linearity property required for a convolution representation. | Remember that convolution arises from *linear* averaging (expectation), not from order statistics. |
| **Assuming a single realisation already equals the convolution.** | A single function still has a sharp jump; only after averaging over many random locations does the jump get smoothed. | Emphasise the role of the *law of large numbers*—convergence only occurs as \(n\to\infty\). |
| **Ignoring the independence of the kink locations.** | Dependence can create systematic alignment of jumps, preventing the smoothing effect. | State the independence (or at least exchangeability) assumption explicitly. |
| **Neglecting integrability/finite‑variance conditions.** | If \(g\) or the distribution of \(L\) have infinite variance, the usual LLN may fail. | Verify that \(g\) is bounded on compacts and that \(p_L\) is a proper density (finite moments). |
| **Thinking “attenuation’’ means the jump height shrinks to zero.** | The *height* of each individual jump stays \(J\); attenuation refers to the *average* jump per unit \(x\) after spreading the jumps over many locations. | Distinguish between the amplitude of a single jump and the *average* derivative observed in the mean function. |

By keeping these points in mind you can correctly recognise when a sample‑average of nonsmooth functions approximates a convolution and when it does **not**.

*Original question: [Finite sample approximation of the convolution with uniformly distributed kinks](https://stats.stackexchange.com/questions/677368/finite-sample-approximation-of-the-convolution-with-uniformly-distributed-kinks) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
