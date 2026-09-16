---
layout: question
title: How to show $\int_{0}^{\infty} x^{\sqrt{10}}e^{-x^{\frac{1}{100}}} dx &lt;
  \infty$?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: How to show $\int_{0}^{\infty} x^{\sqrt{10}}e^{-x^{\frac{1}{100}}}
  dx &lt; \infty$?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem asks  

We have the improper integral  

\[
I=\int_{0}^{\infty} x^{\sqrt{10}}\;e^{-\,x^{1/100}}\;dx
\]

and we must **prove that it is finite** (i.e. convergent).  
The only possible trouble points are  

* \(x\to0^{+}\) (the lower limit), and  
* \(x\to\infty\) (the upper limit).

We will treat the two ends separately.

--------------------------------------------------------------------

## 2.  Behaviour at the lower limit \(x=0\)

When \(x\) is very small, \(x^{1/100}\) is also small, so  

\[
e^{-x^{1/100}} = 1 - x^{1/100}+O\!\left(x^{2/100}\right) \longrightarrow 1 .
\]

Hence near \(0\)

\[
x^{\sqrt{10}}e^{-x^{1/100}} \sim x^{\sqrt{10}} .
\]

The integral \(\int_{0}^{1} x^{\sqrt{10}}dx\) converges because the exponent
\(\sqrt{10}>-1\).  Formally,

\[
\int_{0}^{1} x^{\sqrt{10}}e^{-x^{1/100}}dx\le
\int_{0}^{1} x^{\sqrt{10}}dx=\frac{1}{\sqrt{10}+1}<\infty .
\]

Thus the integral is **proper at the lower limit**.

--------------------------------------------------------------------

## 3.  Behaviour at the upper limit \(x\to\infty\)

The factor \(e^{-x^{1/100}}\) decays much faster than any power of \(x\).
A convenient way to see the finiteness is to make the substitution  

\[
t = x^{1/100}\qquad\Longrightarrow\qquad x = t^{100},
\quad dx = 100\,t^{99}\,dt .
\]

Then

\[
\begin{aligned}
I &=\int_{0}^{\infty} \bigl(t^{100}\bigr)^{\sqrt{10}}\,
      e^{-t}\; 100\,t^{99}\,dt  \\
  &= 100\int_{0}^{\infty} t^{100\sqrt{10}+99}\,e^{-t}\,dt .
\end{aligned}
\]

The integral on the right‑hand side is the **Gamma function**:

\[
\int_{0}^{\infty} t^{\alpha-1}e^{-t}\,dt = \Gamma(\alpha),\qquad 
\alpha>0 .
\]

Here  

\[
\alpha = 100\sqrt{10}+100 \; (>0),
\]

so  

\[
I = 100\,\Gamma\!\bigl(100\sqrt{10}+100\bigr) .
\]

Since the Gamma function is finite for every positive argument, \(I\) is finite.
Hence the integral converges at the upper limit.

--------------------------------------------------------------------

## 4.  A direct comparison (optional)

If one prefers a comparison test instead of the substitution, note that for any
\(a>0\) there exists \(M>0\) such that

\[
x^{a}\le e^{\frac12 x^{1/100}}\qquad\text{for all }x\ge M .
\]

Multiplying by \(e^{-x^{1/100}}\) gives

\[
x^{a}e^{-x^{1/100}}\le e^{-\frac12 x^{1/100}}\qquad(x\ge M).
\]

The right‑hand side is integrable on \([M,\infty)\) because  

\[
\int_{M}^{\infty} e^{-\frac12 x^{1/100}}dx
  = 100\int_{M^{1/100}}^{\infty} t^{99}e^{-\frac12 t}\,dt<\infty .
\]

Thus the original integrand is dominated by an integrable function, confirming
convergence.

--------------------------------------------------------------------

## 5.  Final answer  

\[
\boxed{\displaystyle 
\int_{0}^{\infty} x^{\sqrt{10}}e^{-x^{1/100}}dx
   = 100\,\Gamma\!\bigl(100\sqrt{10}+100\bigr) <\infty }
\]

The integral converges because it behaves like a power function at the origin
and, after the change of variables \(t=x^{1/100}\), becomes a Gamma integral,
which is known to be finite for positive parameters.

--------------------------------------------------------------------

## 6.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Ignoring the lower limit** and assuming convergence only depends on the behaviour at \(\infty\). | Near \(0\) the integrand behaves like \(x^{\sqrt{10}}\); if the exponent were \(\le -1\) the integral would diverge. | Check both endpoints separately. |
| **Applying the limit‑comparison test with the wrong comparison function**, e.g. comparing with \(1/x\). | \(x^{\sqrt{10}}e^{-x^{1/100}}\) decays much faster than any \(1/x^p\); the limit of their ratio may be \(0\) and give no information. | Use a comparison that dominates the integrand, such as \(e^{-c x^{1/100}}\) with \(c>0\). |
| **Forgetting the Jacobian when substituting** \(t = x^{1/100}\). | Omitting the factor \(dx = 100 t^{99} dt\) would give an incorrect power of \(t\). | Write the substitution step explicitly and keep track of the differential. |
| **Assuming the Gamma function diverges** because its argument looks large. | \(\Gamma(z)\) is finite for all \(z>0\); it only diverges at non‑positive integers. | Remember the definition \(\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}dt\) and that it is finite for positive \(z\). |

Keeping these points in mind will help avoid pitfalls when dealing with similar
improper integrals that mix polynomial growth and exponential decay.

*Original question: [How to show $\int_{0}^{\infty} x^{\sqrt{10}}e^{-x^{\frac{1}{100}}} dx &lt; \infty$?](https://math.stackexchange.com/questions/5149520/how-to-show-int-0-infty-x-sqrt10e-x-frac1100-dx-infty) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
