---
layout: question
title: Can anybody show with an example ( small data set) how to grade on a curve
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Can anybody show with an example (
  small data set) how to grade on a curve'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. Restating the problem in plain language  

A professor wants to “grade on a curve.”  
One simple way to do this is to compute a **weighted average** of the raw scores, where each student’s score is multiplied by a weight that reflects how much that score should count toward the final (curved) grade.  

The task is to:

1. Take a tiny data set (e.g., the raw scores of a few students).  
2. Choose reasonable weights (they could all be the same, or they could give extra credit to some items).  
3. Compute the weighted mean  

\[
\boxed{s=\frac{\displaystyle\sum_{i=1}^{n} a_i b_i}{\displaystyle\sum_{i=1}^{n} b_i}}
\]

4. Explain how that weighted mean can be used as the “curved” grade (e.g., by scaling all grades so that the class average becomes the weighted mean, or by setting the weighted mean equal to a target grade such as 75 %).  

We will walk through a concrete, small‑size example step‑by‑step.

---

## 2. Worked example (complete, no steps omitted)

### 2.1. The raw data

| Student | Raw score \(a_i\) (out of 100) |
|---------|------------------------------|
| 1       | 68 |
| 2       | 74 |
| 3       | 81 |
| 4       | 90 |
| 5       | 57 |

So we have \(n=5\) observations \(a_1,\dots ,a_5\).

### 2.2. Choosing the weights  

Suppose the instructor wants to **reward** the three highest scores a little more, because those students completed an optional project.  
A simple weight scheme:

| Student | Weight \(b_i\) |
|---------|----------------|
| 1       | 1 (no extra credit) |
| 2       | 1 |
| 3       | 2 (extra credit) |
| 4       | 2 (extra credit) |
| 5       | 1 |

All weights are positive integers; the total weight will be the denominator of the formula.

### 2.3. Compute the numerator \(\displaystyle\sum a_i b_i\)

\[
\begin{aligned}
a_1 b_1 &= 68 \times 1 = 68\\
a_2 b_2 &= 74 \times 1 = 74\\
a_3 b_3 &= 81 \times 2 = 162\\
a_4 b_4 &= 90 \times 2 = 180\\
a_5 b_5 &= 57 \times 1 = 57\\[4pt]
\text{Sum} &= 68+74+162+180+57 = 541
\end{aligned}
\]

### 2.4. Compute the denominator \(\displaystyle\sum b_i\)

\[
b_1+b_2+b_3+b_4+b_5 = 1+1+2+2+1 = 7
\]

### 2.5. Weighted mean (the “curved” class average)

\[
s = \frac{541}{7}= 77.2857\ldots \approx 77.3
\]

So the **weighted average of the class** is about **77.3 %**.

### 2.6. Using the weighted mean to produce a curve  

A common “curve” is to **shift all grades** so that the class average becomes a desired target, say 75 % (or 80 %).  
Here we already have a weighted average of 77.3 %, which is higher than 75 %.  
If the instructor wants the **new average** to be exactly 75 %, we compute an additive shift:

\[
\text{Shift} = \text{Target} - s = 75.0 - 77.3 = -2.3
\]

Every student’s raw score is reduced by 2.3 points:

| Student | Raw score | Curved score = Raw – 2.3 |
|---------|-----------|--------------------------|
| 1 | 68 | 65.7 |
| 2 | 74 | 71.7 |
| 3 | 81 | 78.7 |
| 4 | 90 | 87.7 |
| 5 | 57 | 54.7 |

Now the **simple (unweighted) average** of the curved scores is:

\[
\frac{65.7+71.7+78.7+87.7+54.7}{5}=75.5\approx 75.0
\]

(The tiny rounding difference is due to using only one decimal place.)

Alternatively, the instructor could **scale** the scores so that the weighted mean becomes a specific grade (e.g., 85 %).  
The scaling factor would be  

\[
\text{Factor} = \frac{\text{Target}}{s}= \frac{85}{77.3}=1.0995\approx 1.10
\]

Multiplying each raw score by 1.10 gives the curved grades (then optionally round to the nearest integer).  

Either additive shifting or multiplicative scaling is a legitimate way to “grade on a curve” once the weighted mean \(s\) has been computed.

---

## 3. Final answer  

For the small data set  

\[
\{(a_i,b_i)\}=\{(68,1),(74,1),(81,2),(90,2),(57,1)\},
\]

the weighted mean is  

\[
\boxed{s = \dfrac{68\cdot1 + 74\cdot1 + 81\cdot2 + 90\cdot2 + 57\cdot1}{1+1+2+2+1}= \dfrac{541}{7}\approx 77.3}.
\]

Using this value as the reference point, the instructor can shift all scores down by 2.3 points (or multiply by 1.10, etc.) to produce a curved grade distribution that meets a desired class‑average target.

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Adding the weights to the raw scores** (e.g., \(68+1\) instead of \(68\times1\)). | The formula requires **multiplication** of each score by its weight; adding inflates the numerator. | Always write the term as \(a_i b_i\) and compute the product first. |
| **Dividing by the number of students \(n\) instead of the sum of the weights**. | The denominator must be \(\sum b_i\); using \(n\) yields an ordinary mean, not a weighted one. | After summing the products, explicitly compute \(\sum b_i\) and use it as the divisor. |
| **Using negative or zero weights**. | Weights must be **positive** (or at least non‑negative) because a zero weight eliminates a data point and a negative weight would subtract it, which is not a standard grading practice. | Check that each \(b_i>0\) before plugging into the formula. |
| **Forgetting to round consistently** (e.g., rounding the numerator but not the denominator). | Rounding too early changes the exact value of the weighted mean. | Keep all intermediate calculations in full precision; round only for the final reported grade. |
| **Applying the additive shift before computing the weighted mean**. | The shift changes the mean; you need the original weighted mean to decide the appropriate shift. | Compute \(s\) first, then decide on the shift or scaling factor. |

By watching out for these pitfalls, the computation of a weighted mean—and the subsequent curve—will be accurate and transparent.

*Original question: [Can anybody show with an example ( small data set) how to grade on a curve](https://stats.stackexchange.com/questions/677485/can-anybody-show-with-an-example-small-data-set-how-to-grade-on-a-curve) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
