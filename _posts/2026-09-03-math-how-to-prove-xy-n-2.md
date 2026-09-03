---
layout: question
title: How to prove $xy=n^2$?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: How to prove $xy=n^2$?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## Problem Restatement  

We are given two **integers** \(x\) and \(y\).  

* Their (arithmetic) mean is \(n\):
\[
\frac{x+y}{2}=n .
\]

* The mean of their reciprocals \(\dfrac{1}{x}\) and \(\dfrac{1}{y}\) is \(\dfrac{1}{n}\):
\[
\frac{\dfrac{1}{x}+\dfrac{1}{y}}{2}= \frac{1}{n}.
\]

We have to **prove** that the product of the two integers equals the square of the mean, i.e.

\[
\boxed{\,xy = n^{2}\,}.
\]

---

## Detailed Solution  

### 1. Write the two given equations

\[
\begin{aligned}
\text{(i)}\qquad &\frac{x+y}{2}=n,\\[4pt]
\text{(ii)}\qquad &\frac{\dfrac{1}{x}+\dfrac{1}{y}}{2}= \frac{1}{n}.
\end{aligned}
\]

Both equations are valid for the (unknown) integers \(x,y\) and the (unknown) integer \(n\).

---

### 2. Isolate the sums in each equation  

From (i) multiply both sides by \(2\):

\[
x+y = 2n. \tag{1}
\]

From (ii) multiply both sides by \(2\) and combine the fractions on the left:

\[
\frac{1}{x}+\frac{1}{y}= \frac{2}{n}.
\]

Put the two fractions over a common denominator \(xy\):

\[
\frac{y+x}{xy}= \frac{2}{n}. \tag{2}
\]

---

### 3. Replace the numerator \(x+y\) using (1)

Equation (2) contains the same numerator \(x+y\) that we already know from (1).  
Substitute \(x+y = 2n\) into (2):

\[
\frac{2n}{xy}= \frac{2}{n}.
\]

---

### 4. Solve for \(xy\)

Both sides have a factor \(2\); cancel it (or divide the whole equation by \(2\)):

\[
\frac{n}{xy}= \frac{1}{n}.
\]

Now cross‑multiply (multiply each side by \(xy\) and by \(n\)):

\[
n\cdot n = xy.
\]

Thus

\[
\boxed{xy = n^{2}}.
\]

The required relationship follows directly from the two mean conditions.

---

## Final Answer  

The product of the two integers equals the square of their mean:

\[
\displaystyle xy = n^{2}.
\]

---

## Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Cancelling the denominator incorrectly** (e.g., turning \(\frac{y+x}{xy}= \frac{2}{n}\) into \(y+x = 2\) by “cancelling” \(xy\) and \(n\)). | You can only cancel a factor that appears **both** in the numerator *and* denominator of the *same* fraction. | Keep the fractions intact until you substitute the known expression for the numerator, then cross‑multiply. |
| **Forgetting to use the first equation** after writing the second one. | The second equation still contains \(x+y\); without replacing it you cannot isolate \(xy\). | After obtaining \(\frac{x+y}{xy}= \frac{2}{n}\), immediately replace \(x+y\) with \(2n\) from the first equation. |
| **Multiplying by the wrong term** (e.g., multiplying (ii) by \(n\) instead of by \(2\)). | The original equation has a factor \(2\) on the left; dropping it changes the equality. | Follow each algebraic step carefully: first clear the outer denominator (multiply by 2), then combine the inner fractions. |
| **Assuming \(x\) or \(y\) could be zero**. | The reciprocal \(\frac{1}{x}\) (or \(\frac{1}{y}\)) would be undefined if \(x=0\) or \(y=0\). | Remember that the problem implicitly requires \(x\neq0\) and \(y\neq0\); the algebra works only under that condition. |

Keeping these points in mind will help you solve similar “mean of numbers and mean of reciprocals” problems without errors.

*Original question: [How to prove $xy=n^2$?](https://math.stackexchange.com/questions/5148543/how-to-prove-xy-n2) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
