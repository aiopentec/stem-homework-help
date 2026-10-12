---
layout: question
title: Checking a method for comparing vehicle encounters near arrivals and departures
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Checking a method for comparing vehicle
  encounters near arrivals and departures'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

You have a list of **encounters** with a particular type of vehicle, each with a timestamp, and for every journey you also know the **departure time** and the **arrival time**.  
You want to know whether these encounters tend to happen more often **close to the start or the end of a journey** (the first 5 min after departure and the last 5 min before arrival) than you would expect simply because you happen to be observing the road more (or less) during those periods.

In statistical language you are trying to compare two **rates**  

\[
\text{Encounter rate in “edge” windows}
\; \text{vs.}\;
\text{Encounter rate in the rest of the journey}
\]

while taking the amount of time you actually spent watching each part of the journey into account.  
You also wonder how to control for other factors that differ between journeys (different routes, traffic conditions, time‑of‑day, vehicles that travel in groups, etc.).

---

## 2.  Step‑by‑step solution  

Below is a complete, reproducible workflow that shows how to turn the raw timestamps into a valid statistical comparison.

### 2.1  Organise the data  

| Journey ID | Dep_time | Arr_time | Encounter_time(s) (vector) |
|------------|----------|----------|-----------------------------|
| 1          | 08:00    | 09:30    | 08:02, 08:12, …            |
| 2          | 10:15    | 11:45    | 10:20, 10:55, …            |
| …          | …        | …        | …                           |

For each journey create three **time intervals**  

| Interval | Start | End |
|----------|-------|-----|
| **Edge** (the part we care about) | max(Dep, Dep + 0 min) → min(Dep + 5 min, Arr − 5 min) | max(Arr − 5 min, Dep + 5 min) |
| **Start‑only** | Dep → Dep + 5 min (if it does **not** overlap the end) | — |
| **End‑only**   | Arr − 5 min → Arr (if it does **not** overlap the start) | — |
| **Middle** | All remaining time between the two edge windows | — |

Because a journey can be shorter than 10 min, the two 5‑min windows may overlap. In that case the **edge interval** is simply the whole journey (no “middle” part).  

*Implementation tip*: in R you can use `interval()` from the **lubridate** package or in Python `pandas.Interval`.

### 2.2  Count encounters and exposure time  

For every journey \(j\):

| Quantity | Symbol | How to obtain |
|----------|--------|----------------|
| Total observation time | \(T_j\) | \( \text{Arr}_j - \text{Dep}_j\) (in minutes) |
| Edge observation time | \(E_j\) | length of the edge interval (≤ 10 min) |
| Middle observation time | \(M_j = T_j - E_j\) | subtraction |
| Encounters in edge interval | \(C^{\text{edge}}_j\) | count of `Encounter_time` that fall inside the edge interval |
| Encounters in middle interval | \(C^{\text{mid}}_j\) | count of those that fall elsewhere |

Then sum across all journeys  

\[
\begin{aligned}
E &= \sum_j E_j &&\text{(total edge‑time)}\\
M &= \sum_j M_j &&\text{(total middle‑time)}\\[4pt]
C_E &= \sum_j C^{\text{edge}}_j &&\text{(total edge encounters)}\\
C_M &= \sum_j C^{\text{mid}}_j &&\text{(total middle encounters)}
\end{aligned}
\]

### 2.3  Compute the two encounter rates  

\[
\lambda_E = \frac{C_E}{E}\qquad
\lambda_M = \frac{C_M}{M}
\]

These are *encounters per minute* (or per hour, whichever unit you used for the times).  

Your original “share of encounters ÷ share of observation time” is exactly the **rate ratio**

\[
\text{RR} = \frac{C_E/E}{C_M/M}= \frac{\lambda_E}{\lambda_M}.
\]

If RR > 1, encounters are **more concentrated** near departures/arrivals than elsewhere, after accounting for the amount of time observed.

### 2.4  Get a confidence interval / hypothesis test  

Because counts of rare events observed over a known exposure time are well described by a **Poisson distribution**, we can treat \(C_E\) and \(C_M\) as independent Poisson variables with means \(\lambda_E E\) and \(\lambda_M M\).  

The standard (large‑sample) **log‑rate‑ratio** confidence interval is  

\[
\log(\widehat{\text{RR}}) \pm z_{1-\alpha/2}\,
\sqrt{\frac{1}{C_E}+\frac{1}{C_M}} .
\]

Exponentiating gives the CI for RR.

If the counts are small (e.g., any of the two counts < 10), use an **exact** method such as the conditional Poisson test (implemented as `poisson.test` in R) or the **mid‑P** interval.

#### Example (R‑style pseudo‑code)

```r
# totals from step 2
C_E <- 125   # edge encounters
E   <- 3000  # edge minutes
C_M <- 340   # middle encounters
M   <- 12000 # middle minutes

RR  <- (C_E / E) / (C_M / M)
logRR.se <- sqrt(1/C_E + 1/C_M)
ci.low   <- exp(log(RR) - qnorm(0.975) * logRR.se)
ci.high  <- exp(log(RR) + qnorm(0.975) * logRR.se)

RR
ci.low
ci.high
```

### 2.5  Adjusting for other factors  

The simple rate‑ratio treats every journey as interchangeable. If you suspect that **route**, **traffic conditions**, **time of day**, or **group travel** affect the baseline encounter intensity, you can extend the analysis in two common ways.

#### 2.5.1  Stratified (layered) analysis  

Split the data into homogeneous strata (e.g., “morning vs. evening”, “highway vs. city”, “solo vs. group”). Compute a separate RR in each stratum and then combine them with a **Mantel–Haenszel** weighted average. This gives a pooled estimate that controls for the stratifying variable.

#### 2.5.2  Regression modelling  

A **Poisson (or quasi‑Poisson) regression** with an *offset* for the log of exposure time lets you estimate the effect of the “edge” window while simultaneously adjusting for covariates.

Model:

\[
\log(\mathbb{E}[C_{ij}]) = \beta_0 + \beta_1\; \text{Edge}_{ij}
                           + \beta_2\; \text{Route}_{ij}
                           + \beta_3\; \text{TimeOfDay}_{ij}
                           + \dots
                           + \log(T_{ij}),
\]

where  

* \(C_{ij}\) = count of encounters for journey \(j\) in interval \(i\) (edge = 1, middle = 0)  
* \(T_{ij}\) = exposure time for that interval (the *offset*)  
* \(\beta_1\) is the log‑rate‑ratio of interest.

If journeys are not independent (e.g., the same driver or the same vehicle appears repeatedly), add a **random intercept** (a mixed‑effects Poisson model) to capture within‑driver correlation.

Software examples  

* **R**: `glm(C ~ Edge + Route + TimeOfDay + offset(log(Time)), family = poisson)`  
  or `glmer(C ~ Edge + Route + TimeOfDay + offset(log(Time)) + (1|Driver), family = poisson)` (package *lme4*).  
* **Python**: `statsmodels.GLM` with `family=Poisson()` and `offset=np.log(time)`; for mixed models use `statsmodels.MixedLM` or `pymer4`.

The exponentiated coefficient \(\exp(\hat\beta_1)\) is the **adjusted rate ratio**.

### 2.6  Summarising the result  

* **Unadjusted**: compute \( \widehat{\text{RR}} = \dfrac{C_E/E}{C_M/M}\) and its confidence interval.  
* **Adjusted (if needed)**: fit a Poisson regression with an offset, extract \(\exp(\hat\beta_1)\) and its CI.  

If the CI excludes 1 (or the p‑value < 0.05), you have statistically significant evidence that encounters are concentrated near departures/arrivals after controlling for the amount of observation time (and any covariates you included).

---

## 3.  Final answer  

| Quantity | Formula | Interpretation |
|----------|---------|----------------|
| **Edge encounter rate** | \(\lambda_E = \dfrac{C_E}{E}\) | encounters per minute (or hour) in the first 5 min after departure **or** the last 5 min before arrival |
| **Middle encounter rate** | \(\lambda_M = \dfrac{C_M}{M}\) | encounters per minute in the rest of the journey |
| **Unadjusted rate ratio** | \(\displaystyle \widehat{\text{RR}} = \frac{\lambda_E}{\lambda_M}= \frac{C_E/E}{C_M/M}\) | > 1 ⇒ clustering near edges; < 1 ⇒ fewer edges than expected |
| **95 % CI (large‑sample)** | \(\displaystyle \exp\!\Big[ \log(\widehat{\text{RR}}) \pm 1.96\sqrt{\frac{1}{C_E}+\frac{1}{C_M}} \Big]\) | If it does **not** contain 1, the clustering is statistically significant |
| **Adjusted RR** | \(\exp(\hat\beta_1)\) from a Poisson (or mixed‑effects Poisson) regression with log‑exposure offset | Gives the edge‑effect after accounting for route, time‑of‑day, group travel, etc. |

Thus the method you described is essentially correct **provided you treat the counts as Poisson events and compute a proper confidence interval**.  Adding a regression (or stratified) layer will let you control for the extra factors you mentioned.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using raw proportions without accounting for variance** (e.g., just reporting “0.12 / 0.04 = 3”) | The ratio looks large, but you have no idea whether it could be due to chance. | Compute a confidence interval or p‑value using the Poisson variance formula (or exact test). |
| **Ignoring the different lengths of the edge windows** (e.g., treating every journey as if the edge period were exactly 10 min) | Short trips give less exposure; the rate will be biased upward. | Explicitly calculate the actual edge exposure \(E_j\) for each journey; use the offset in the regression. |
| **Double‑counting an encounter that falls in both the start‑5‑min and the end‑5‑min windows** | Inflates the edge count, especially for short trips. | Define the edge interval as the *union* of the two windows (as shown above) and count each encounter only once. |
| **Assuming independence when the same driver or vehicle appears many times** | Correlated observations underestimate the true variance → overly narrow CIs. | Use a mixed‑effects Poisson model with a random intercept for driver/vehicle, or apply a robust “sandwich” variance estimator. |
| **Treating the Poisson distribution as exact when counts are large and over‑dispersed** | Variance > mean → standard Poisson SEs are too small. | Use a quasi‑Poisson or negative‑binomial model; the over‑dispersion parameter inflates the SEs appropriately. |
| **Failing to handle journeys shorter than 10 min** | The two windows overlap; the edge period is then the

*Original question: [Checking a method for comparing vehicle encounters near arrivals and departures](https://stats.stackexchange.com/questions/677406/checking-a-method-for-comparing-vehicle-encounters-near-arrivals-and-departures) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
