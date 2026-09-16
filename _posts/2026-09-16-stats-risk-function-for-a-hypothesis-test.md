---
layout: question
title: Risk Function for a hypothesis test?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Risk Function for a hypothesis test?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the problem is asking  

We have i.i.d. normal observations  

\[
X_1,\dots ,X_n \stackrel{\text{i.i.d.}}{\sim} N(\mu,\sigma^{2}),\qquad \sigma^{2}\ \text{known}.
\]

We want to test  

\[
H_{0}:\mu =0\qquad\text{vs.}\qquad H_{1}:\mu\neq 0
\]

with the (two‑sided) decision rule  

\[
\mathcal R=\{\;|\bar X|\ge k\;\}\qquad\text{(reject }H_{0}\text{)} .
\]

The loss (cost) associated with a wrong decision is  

* \(L(H_{0},\text{reject }H_{0}) = c_{10}\)  (type‑I error)  
* \(L(H_{1},\text{retain }H_{0}) = c_{01}\)  (type‑II error)  

All other outcomes have loss \(0\).

Under the alternative we **do not know** the true \(\mu\); instead we are told that  

\[
\mu\mid H_{1}\;\sim\;N(0,\tau^{2}) .
\]

The task is to compute the **risk function**, i.e. the expected loss,  

* when the true state is \(H_{0}\) (i.e. \(\mu =0\)), and  
* when the true state is \(H_{1}\) (i.e. \(\mu\neq 0\) with the prior above).

---

## 2. Distribution of the test statistic  

The sample mean is  

\[
\bar X = \frac{1}{n}\sum_{i=1}^{n}X_i .
\]

*Conditional on a fixed \(\mu\)*  

\[
\bar X \mid \mu \;\sim\; N\!\Bigl(\mu,\; \frac{\sigma^{2}}{n}\Bigr).
\]

*Marginalising over the prior \(\mu\sim N(0,\tau^{2})\) (only under \(H_{1}\))*  

Because a sum of independent normal variables is normal,  

\[
\bar X \mid H_{1}\;\sim\; N\!\Bigl(0,\; \frac{\sigma^{2}}{n}+\tau^{2}\Bigr).
\]

Both distributions will be needed.

---

## 3. Risk when the null hypothesis is true (\(\mu =0\))

When \(\mu=0\) the only way we incur loss is by **rejecting** \(H_{0}\).  
Hence  

\[
R_{0}= \operatorname{E}\bigl[ L\mid \mu=0 \bigr]
     = c_{10}\; P\bigl(|\bar X|\ge k \mid \mu=0 \bigr).
\]

Because \(\bar X\mid \mu=0\sim N\!\bigl(0,\sigma^{2}/n\bigr)\),

\[
\begin{aligned}
P\bigl(|\bar X|\ge k \mid \mu=0\bigr)
&= P\!\left(\bar X\ge k\right)+P\!\left(\bar X\le -k\right)   \\
&= 2\Bigl[1-\Phi\!\Bigl(\frac{k}{\sigma/\sqrt{n}}\Bigr)\Bigr]    \\
&= 2\Bigl[1-\Phi\!\Bigl(\frac{k\sqrt{n}}{\sigma}\Bigr)\Bigr],
\end{aligned}
\]

where \(\Phi(\cdot)\) is the standard normal cdf.  

Therefore  

\[
\boxed{ \displaystyle
R_{0}= c_{10}\; 2\Bigl[1-\Phi\!\Bigl(\frac{k\sqrt{n}}{\sigma}\Bigr)\Bigr] } .
\]

---

## 4. Risk when the alternative hypothesis is true  

### 4.1 Conditional risk for a **fixed** non‑zero \(\mu\)

If the true mean were some specific \(\mu\neq0\), we would incur loss only when we **retain** \(H_{0}\) (i.e. \(|\bar X|<k\)). Thus  

\[
R_{1}(\mu)=c_{01}\;P\bigl(|\bar X|<k\mid \mu\bigr).
\]

Using the conditional distribution \(\bar X\mid \mu\sim N(\mu,\sigma^{2}/n)\),

\[
\begin{aligned}
P\bigl(|\bar X|<k\mid \mu\bigr)
&=P\bigl(-k<\bar X<k\mid \mu\bigr)   \\
&= \Phi\!\Bigl(\frac{k-\mu}{\sigma/\sqrt n}\Bigr)
   -\Phi\!\Bigl(\frac{-k-\mu}{\sigma/\sqrt n}\Bigr).
\end{aligned}
\]

Hence  

\[
\boxed{\displaystyle
R_{1}(\mu)=c_{01}\Bigl[
\Phi\!\Bigl(\frac{k-\mu}{\sigma/\sqrt n}\Bigr)
-\Phi\!\Bigl(\frac{-k-\mu}{\sigma/\sqrt n}\Bigr)
\Bigr] } .
\]

### 4.2 **Bayes risk** – averaging over the prior \(\mu\sim N(0,\tau^{2})\)

The problem statement says “under \(H_{1}\) we also assume that \(\mu\sim N(0,\tau^{2})\)”.  
Therefore the *overall* risk when the true state is \(H_{1}\) is the prior‑average of the conditional risk:

\[
\begin{aligned}
R_{1}
&= \operatorname{E}_{\mu}\bigl[ R_{1}(\mu)\bigr] \\
&= c_{01}\; \operatorname{E}_{\mu}\bigl[ P(|\bar X|<k\mid\mu) \bigr] .
\end{aligned}
\]

Because the inner probability is just the marginal probability that the statistic falls in the acceptance region, we can replace the two‑step expectation by a single probability computed with the **marginal** distribution of \(\bar X\) under \(H_{1}\):

\[
\bar X\mid H_{1}\;\sim\; N\!\Bigl(0,\; \frac{\sigma^{2}}{n}+\tau^{2}\Bigr).
\]

Thus  

\[
\begin{aligned}
R_{1}
&= c_{01}\; P\bigl(|\bar X|<k\mid H_{1}\bigr)\\[4pt]
&= c_{01}\Bigl[
\Phi\!\Bigl(\frac{k}{\sqrt{\sigma^{2}/n+\tau^{2}}}\Bigr)
-\Phi\!\Bigl(\frac{-k}{\sqrt{\sigma^{2}/n+\tau^{2}}}\Bigr)
\Bigr] \\[4pt]
&= c_{01}\Bigl[\,2\Phi\!\Bigl(\frac{k}{\sqrt{\sigma^{2}/n+\tau^{2}}}\Bigr)-1\Bigr].
\end{aligned}
\]

So the **Bayes risk** for the alternative is  

\[
\boxed{\displaystyle
R_{1}=c_{01}\Bigl[\,2\Phi\!\Bigl(\frac{k}{\sqrt{\sigma^{2}/n+\tau^{2}}}\Bigr)-1\Bigr] } .
\]

---

## 5. Summary of the risk function  

| True state | Risk (expected loss) |
|------------|----------------------|
| \(H_{0}\) (\(\mu =0\)) | \(\displaystyle R_{0}=c_{10}\;2\bigl[1-\Phi\!\bigl(\tfrac{k\sqrt n}{\sigma}\bigr)\bigr]\) |
| \(H_{1}\) (\(\mu\neq0\), with prior \(\mu\sim N(0,\tau^{2})\)) | \(\displaystyle R_{1}=c_{01}\Bigl[\,2\Phi\!\bigl(\tfrac{k}{\sqrt{\sigma^{2}/n+\tau^{2}}}\bigr)-1\Bigr]\) |

If one wishes the risk **conditional on a specific** non‑zero \(\mu\), replace the second line by  

\[
R_{1}(\mu)=c_{01}\Bigl[
\Phi\!\Bigl(\frac{k-\mu}{\sigma/\sqrt n}\Bigr)
-\Phi\!\Bigl(\frac{-k-\mu}{\sigma/\sqrt n}\Bigr)
\Bigr].
\]

---

## 6. Common Mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using the marginal variance \(\sigma^{2}/n+\tau^{2}\) for the null case** | Under \(H_{0}\) the prior on \(\mu\) is *not* invoked; \(\mu\) is fixed at 0, so the variance is only \(\sigma^{2}/n\). | Remember the prior only applies under \(H_{1}\). |
| **Omitting the “\(-1\)” term in the type‑II risk** | The probability of *not* rejecting is \(P(|\bar X|<k)=2\Phi(\cdot)-1\), not just \(2\Phi(\cdot)\). | Write the acceptance probability as \(\Phi(a)-\Phi(-a)=2\Phi(a)-1\). |
| **Treating \(\bar X\) as \(N(0,\sigma^{2}/n+\tau^{2})\) for every \(\mu\neq0\)** | That distribution is the *mixture* (marginal) under the prior, not the conditional distribution given a particular \(\mu\). | Distinguish clearly: conditional on a fixed \(\mu\) → variance \(\sigma^{2}/n\); marginal (averaged over prior) → extra \(\tau^{2}\). |
| **Confusing type‑I and type‑II losses** | The loss \(c_{10}\) is paid only when we reject a true \(H_{0}\); \(c_{01}\) is paid only when we fail to reject a true \(H_{1}\). | Write the loss table explicitly before forming the risk. |
| **Using a one‑sided critical region** | The test is two‑sided, so the rejection region is \(|\bar X|\ge k\). | Ensure the probability calculations include both tails (multiply by 2 or use symmetry). |

With the correct distributions and the proper handling of the prior, the risk expressions above follow directly.

*Original question: [Risk Function for a hypothesis test?](https://stats.stackexchange.com/questions/677148/risk-function-for-a-hypothesis-test) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
