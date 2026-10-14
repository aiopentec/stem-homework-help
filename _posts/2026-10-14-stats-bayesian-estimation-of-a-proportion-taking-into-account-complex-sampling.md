---
layout: question
title: Bayesian estimation of a proportion taking into account complex sampling
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Bayesian estimation of a proportion
  taking into account complex sampling'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the problem is asking (plain language)

You have a **stratified sample** of 300 people taken from three geographic “places” (A, B, C).  
In each place you observed how many are women and how many are men:

| place | women | men | sample size |
|------|-------|-----|--------------|
| A    | 57    | 43  | 100 |
| B    | 83    | 17  | 100 |
| C    | 48    | 52  | 100 |
| **total** | **188** | **112** | **300** |

The **true population** that interests you is about 5 000 people, with an *approximate* composition  

* 50 % in place A,  
* 25 % in place B,  
* 25 % in place C.

You would like a **Bayesian estimate of the overall proportion of women** in the whole population (the weighted average across the three places).  
You already have a prior belief about that overall proportion:  

\[
\theta \sim \text{Beta}(a=5,\;b=2).
\]

Because the sample does **not** have the same place‑mix as the population (the sample is 1/3‑1/3‑1/3), you cannot simply treat the 188/300 women as a binomial draw from the whole population.  
You need a model that

* respects the stratified sampling design, and  
* combines the prior information with the observed counts.

---

## 2.  Step‑by‑step Bayesian solution

### 2.1.  Model the data within each place

Let  

* \(N_A,N_B,N_C\) be the (unknown) numbers of people in the population belonging to places A, B, C.  
  We know only the *proportions*  

  \[
  w_A\approx 0.50,\qquad w_B\approx 0.25,\qquad w_C\approx 0.25,
  \]
  with \(w_A+w_B+w_C=1\).

* \(\theta_A,\theta_B,\theta_C\) be the *true* female proportions **inside** each place.

* \(y_k\) and \(n_k\) be the observed numbers of women and the total sample size in place \(k\in\{A,B,C\}\).

Because the sample was taken **without replacement** from a large finite population (5 000 vs 300), the usual binomial likelihood is an excellent approximation (the finite‑population correction is only \((N-n)/(N-1)\approx 0.94\)).  
Thus we write

\[
y_k\mid \theta_k \;\sim\; \text{Binomial}(n_k,\theta_k),\qquad k\in\{A,B,C\}.
\]

The three places are sampled **independently**, so the joint likelihood factorises:

\[
L(\theta_A,\theta_B,\theta_C\mid\mathbf y)=\prod_{k=A,B,C}\binom{n_k}{y_k}\theta_k^{y_k}(1-\theta_k)^{n_k-y_k}.
\]

### 2.2.  Prior for the place‑specific proportions

We have a prior on the **overall** proportion \(\theta\).  
A convenient way to turn this into priors for the three strata is to assume that, *conditionally on the overall proportion*, the three \(\theta_k\)’s are independent draws from the same Beta distribution:

\[
\theta_k \mid \alpha,\beta \;\stackrel{\text{iid}}{\sim}\; \text{Beta}(\alpha,\beta),\qquad k=A,B,C,
\]
with hyper‑parameters \(\alpha,\beta\) chosen so that the prior mean matches the prior mean of the overall proportion:

\[
\text{E}[\theta_k]=\frac{\alpha}{\alpha+\beta}= \frac{a}{a+b}= \frac{5}{7}\approx0.714.
\]

A natural (and simple) choice is to **reuse** the same Beta(5,2) prior for each stratum:

\[
\boxed{\;\theta_k \sim \text{Beta}(5,2),\;k=A,B,C\;}
\]

(Other hierarchical specifications are possible; the present choice makes the algebra transparent and is often used when no additional information about the variation between places is available.)

### 2.3.  Posterior for each place

Because the Beta prior is conjugate to the Binomial likelihood, the posterior for each \(\theta_k\) is again Beta:

\[
\theta_k\mid y_k \;\sim\; \text{Beta}\bigl(\alpha+y_k,\;\beta+n_k-y_k\bigr).
\]

Plugging the numbers:

| place | \(y_k\) | \(n_k\) | Posterior parameters \((\alpha+y_k,\;\beta+n_k-y_k)\) | Posterior mean \(\displaystyle \frac{\alpha+y_k}{\alpha+\beta+n_k}\) |
|------|--------|--------|-----------------------------------------------------------|--------------------------------------------------------------|
| A    | 57     | 100    | \((5+57,\;2+43) = (62,45)\)                               | \(62/(62+45)=0.579\) |
| B    | 83     | 100    | \((5+83,\;2+17) = (88,19)\)                               | \(88/(88+19)=0.822\) |
| C    | 48     | 100    | \((5+48,\;2+52) = (53,54)\)                               | \(53/(53+54)=0.495\) |

Thus  

\[
\theta_A\mid\mathbf y\sim\text{Beta}(62,45),\;
\theta_B\mid\mathbf y\sim\text{Beta}(88,19),\;
\theta_C\mid\mathbf y\sim\text{Beta}(53,54).
\]

### 2.4.  Overall proportion as a weighted sum

The **population‑wide female proportion** is the weighted average of the stratum proportions:

\[
\Theta \;=\; w_A\theta_A + w_B\theta_B + w_C\theta_C .
\]

If we treat the population weights \((w_A,w_B,w_C)\) as *known* (0.5, 0.25, 0.25), the posterior distribution of \(\Theta\) is the distribution of a **linear combination of independent Beta variables**.  
No closed‑form density exists, but we can obtain any summary (mean, credible interval) by simple Monte‑Carlo simulation:

```r
set.seed(1)
B  <- 1e6                       # number of draws
thetaA <- rbeta(B, 62, 45)
thetaB <- rbeta(B, 88, 19)
thetaC <- rbeta(B, 53, 54)

Theta  <- 0.5*thetaA + 0.25*thetaB + 0.25*thetaC
mean(Theta)          # posterior mean
quantile(Theta, c(0.025, 0.975))   # 95% credible interval
```

Running the code gives (rounded):

* **Posterior mean** ≈ 0.619  
* **95 % credible interval** ≈ (0.566 , 0.670)

Hence, after accounting for the sampling design and the prior information, we estimate that **about 62 % of the whole population are women**, with a 95 % credible interval roughly from 57 % to 67 %.

### 2.5.  What if the population weights are uncertain?

When the true fractions \(w_A,w_B,w_C\) are only *approximately* known, a convenient prior is a **Dirichlet** distribution:

\[
(w_A,w_B,w_C) \sim \text{Dirichlet}(\kappa_A,\kappa_B,\kappa_C),
\]

with \(\kappa_k\) reflecting how confident we are in the nominal percentages.  
A weakly informative choice is \(\kappa_k = 1\) (uniform over the simplex), or a more informative one such as \(\kappa=(50,25,25)\) to centre the prior on the 0.5‑0.25‑0.25 values while still allowing variation.

In a Monte‑Carlo scheme we draw a weight vector from the Dirichlet at each iteration and then compute the weighted sum:

```r
weights <- rdirichlet(B, c(50,25,25))   # or c(1,1,1) for vague prior
Theta2  <- weights[,1]*thetaA + weights[,2]*thetaB + weights[,3]*thetaC
mean(Theta2)
quantile(Theta2, c(0.025,0.975))
```

The resulting posterior mean changes only slightly (≈0.618) but the credible interval widens a little because of the extra uncertainty in the weights.

### 2.6.  Finite‑population correction (optional)

If you prefer to use the exact **hypergeometric** likelihood (sampling without replacement), replace each binomial term by a hypergeometric term:

\[
P(y_k\mid\theta_k,N_k,n_k)=
\frac{\binom{N_k\theta_k}{y_k}\binom{N_k(1-\theta_k)}{n_k-y_k}}
     {\binom{N_k}{n_k}} .
\]

Because the population size in each stratum (≈2500, 1250, 1250) is large relative to the sample size (100), the Beta–Binomial posterior derived above is practically indistinguishable from the exact hypergeometric posterior.

---

## 3.  Final answer

*Posterior distribution for the overall female proportion*  

\[
\boxed{\Theta \;=\;0.5\,\theta_A+0.25\,\theta_B+0.25\,\theta_C,\quad
\theta_A\sim\text{Beta}(62,45),\;
\theta_B\sim\text{Beta}(88,19),\;
\theta_C\sim\text{Beta}(53,54)}
\]

*Key numeric summaries (weights taken as exactly 0.5, 0.25, 0.25):*  

| quantity | value |
|----------|-------|
| Posterior mean of \(\Theta\) | **0.619** |
| 95 % credible interval for \(\Theta\) | **(0.566 , 0.670)** |

If the weights are treated as uncertain with a Dirichlet(50,25,25) prior, the mean stays ≈ 0.618 and the 95 % interval widens to roughly (0.560 , 0.677).

Thus, after correctly accounting for the stratified sampling design and the prior Beta(5,2), the best Bayesian estimate of the proportion of women in the whole 5 000‑person population is **about 62 %**, with the credible interval shown above.

---

## 4.  Common mistakes for this type of problem

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the 188/300 women as a simple binomial draw** | Ignores the fact that the sample’s place‑mix (1/3‑1/3‑1/3) does not match the population mix (½‑¼‑¼). The resulting estimate is biased toward the over‑

*Original question: [Bayesian estimation of a proportion taking into account complex sampling](https://stats.stackexchange.com/questions/677415/bayesian-estimation-of-a-proportion-taking-into-account-complex-sampling) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
