---
layout: question
title: How can I separate the incremental predictive value of a delayed data source
  from the effect of waiting?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: How can I separate the incremental
  predictive value of a delayed data source from the effect of waiting?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  Restating the question in plain language  

You have two streams of information about the same market event:

| Time | What you see |
|------|--------------|
| **t₁** (e.g., 10:03) | **Source A** – always arrives, can be used to make a prediction immediately. |
| **t₂** (e.g., 10:07) | **Source B** – arrives later, sometimes never arrives, and may contain new, duplicate, or derived information. |

You want to know **two separate things**:

1. **Incremental predictive value** – If you wait until *t₂* and add B to the already‑available A, does the *prediction* become statistically better *ignoring the fact that you waited*?
2. **Operational value of waiting** – If you actually *delay the decision* from *t₁* to *t₂* (so you lose time, possibly lose the chance to act, and B may be missing), is the overall outcome (including the time cost) better?

The difficulty is that B is **not always observed** and its arrival time is **correlated** with the underlying event. You need a method that (i) separates the pure information gain from B from the cost of waiting, and (ii) avoids bias caused by the selective appearance of B and the temporal dependence between the two observations.

---

## 2.  Step‑by‑step solution  

Below is a complete, reproducible analytical framework.  
The notation is generic; replace it with your concrete variables when you implement it.

### 2.1  Formal notation  

| Symbol | Meaning |
|--------|---------|
| \(i = 1,\dots,N\) | Observation index (one market event). |
| \(t_i^A\) | Time at which source A becomes available for event *i*. (Usually the same for all events, e.g., 10:03.) |
| \(t_i^B\) | Time at which source B becomes available for event *i* (may be missing). |
| \(X_i^A\) | Feature vector from source A (available at \(t_i^A\)). |
| \(X_i^B\) | Feature vector from source B (available at \(t_i^B\)). |
| \(Y_i\) | Future outcome you wish to predict (e.g., price move in the next 30 min). |
| \(D_i\) | Binary indicator \(D_i = 1\) if B arrives (i.e., \(t_i^B\) observed) and 0 otherwise. |
| \(W_i = t_i^B - t_i^A\) | Waiting time (non‑negative, possibly undefined when \(D_i = 0\)). |
| \(\pi_A(\cdot)\) | Predictive model that uses only \(X^A\). |
| \(\pi_{AB}(\cdot)\) | Predictive model that uses both \(X^A\) and \(X^B\). |
| \(a_i\) | Decision made at time \(t_i^A\) using \(\pi_A\). |
| \(b_i\) | Decision made at time \(t_i^B\) using \(\pi_{AB}\). |
| \(U(\cdot)\) | Utility (or loss) function that maps a decision and the realized outcome to a numeric score (e.g., profit, negative log‑loss, etc.). |

We assume a **prospective** data collection plan: for each event we observe the timestamps, the feature vectors, and the eventual outcome.

---

### 2.2  Part 1 – Incremental predictive value (pure information gain)  

**Goal:** Compare the *predictive quality* of \(\pi_A\) vs. \(\pi_{AB}\) **conditioned on the same information set** (i.e., the same time point).  

**Key idea:** Use only the events for which B *actually arrived* (so both predictions can be made) and evaluate the two predictions on the *same outcome* \(Y_i\) with a proper scoring rule. This eliminates any effect of waiting because both predictions are judged at the *same future horizon*.

#### 2.2.1  Build the two models  

1. **Model A** – Train \(\pi_A\) on the full training set using only \(X^A\).  
2. **Model AB** – Train \(\pi_{AB}\) **only on the subset** where B is observed (i.e., \(D=1\)). Use both \(X^A\) and \(X^B\) as predictors.

> **Why train AB on the subset?**  
> The model should learn the relationship between the *joint* feature space and the outcome. If you train on all events and simply impute missing B, you introduce model misspecification that confounds the incremental value you are trying to measure.

#### 2.2.2  Paired evaluation on the test set  

1. Create a **test set** that mirrors the prospective evaluation (e.g., a forward‑rolling window).  
2. Keep **only the test observations with \(D=1\)** (B arrived).  
3. For each such observation \(i\) compute:  

   * Prediction from A: \(\hat{y}^{A}_i = \pi_A(X_i^A)\)  
   * Prediction from AB: \(\hat{y}^{AB}_i = \pi_{AB}(X_i^A, X_i^B)\)

4. Choose a proper scoring rule \(S(\hat y, y)\) (e.g., log‑loss for probabilities, Brier score, or a profit‑based utility). Compute the **difference** for each observation:

   \[
   \Delta_i = S(\hat y^{AB}_i, Y_i) - S(\hat y^{A}_i, Y_i)
   \]

   *If the utility is to be *maximized* (e.g., profit), then \(\Delta_i\) will be positive when AB is better.*

5. Summarize \(\Delta_i\) across the paired set:

   * Mean difference \(\bar\Delta = \frac{1}{n_{D=1}} \sum_{i:D_i=1}\Delta_i\)  
   * Standard error \(\text{SE} = \frac{s_{\Delta}}{\sqrt{n_{D=1}}}\) where \(s_{\Delta}\) is the sample standard deviation of the \(\Delta_i\).  
   * 95 % confidence interval \(\bar\Delta \pm 1.96\text{SE}\).  

6. Perform a **paired hypothesis test** (e.g., a paired t‑test or Wilcoxon signed‑rank test) to assess whether the mean difference differs from 0.

**Interpretation:** A statistically significant positive \(\bar\Delta\) tells you that *if you could magically receive B without waiting*, the prediction would be better. This isolates the *information* contributed by B.

---

### 2.3  Part 2 – Operational value of waiting (cost of delay)  

Now we incorporate the fact that waiting may change the state of the world, cause missing B, or make the decision no longer actionable.

#### 2.3.1  Define a decision‑oriented utility  

Let the utility of a decision made at time \(t\) be \(U_t(a, Y)\). Typical examples:

* **Profit**: \(U_t = \text{(position size)} \times ( \text{price change after } t )\).  
* **Binary reward**: \(U_t = 1\) if the decision correctly predicts the event, else 0.  

Crucially, the utility must **penalize delay** (e.g., by using the price movement that occurs *after* the decision time).  

#### 2.3.2  Simulate two policies on the *full* prospective data  

| Policy | When it decides | What data it uses |
|--------|----------------|-------------------|
| **P₁ (Early)** | At \(t_i^A\) (no waiting) | \(\pi_A(X_i^A)\) |
| **P₂ (Wait)** | At \(\min(t_i^B,\, t_i^{\text{cutoff}})\) | If \(D_i=1\) use \(\pi_{AB}(X_i^A,X_i^B)\); otherwise fall back to \(\pi_A(X_i^A)\) (or abort the decision). |

*The cutoff* can be a business rule (e.g., never wait more than 5 min).  

For each event \(i\) compute the realized utility:

* \(U_i^{(1)} = U_{t_i^A}\bigl( \pi_A(X_i^A),\, Y_i \bigr)\)  
* \(U_i^{(2)} =\)  

  * If \(D_i=1\) **and** we wait the full \(W_i\):  
    \(U_{t_i^B}\bigl( \pi_{AB}(X_i^A,X_i^B),\, Y_i \bigr)\)  
  * If \(D_i=0\) (B never arrives) **or** we exceed a pre‑specified maximal wait: use the early decision (or a “no‑action” utility of 0).

#### 2.3.3  Handle the selection bias of B  

Because B arrives only for a subset, naïvely comparing the average utilities of P₁ and P₂ would be biased. Use **inverse‑probability‑weighting (IPW)** or **doubly‑robust** estimation:

1. **Model the propensity of B arriving**  
   Fit a logistic regression (or any appropriate classifier) \(p_i = \Pr(D_i = 1 \mid X_i^A, Z_i)\) where \(Z_i\) are any covariates that could influence B’s arrival (e.g., event size, time of day).  

2. **Compute weights**  

   \[
   w_i = \frac{1}{p_i} \quad\text{for events with } D_i=1, \qquad w_i = \frac{1}{1-p_i} \quad\text{for events with } D_i=0.
   \]

   These weights create a *pseudo‑population* in which B’s arrival is independent of the observed covariates.

3. **Weighted utility difference**  

   \[
   \Delta^{\text{op}} = \frac{1}{N}\sum_{i=1}^N w_i\Bigl[ U_i^{(2)} - U_i^{(1)} \Bigr].
   \]

   Compute a robust standard error (e.g., via the sandwich estimator) and a confidence interval.  

   *If you prefer a doubly‑robust estimator, additionally model the conditional expected utility given the covariates and combine the outcome regression with the propensity weights.*

#### 2.3.4  Alternative: Causal‑inference framing (dynamic treatment regime)  

Treat “waiting for B” as a **time‑varying treatment**:

* Treatment \(A_t = 0\) (decide now) vs. \(A_t = 1\) (wait).  
* The **potential outcome** under each regime is \(Y_i^{(0)}\) and \(Y_i^{(1)}\).  

Use **g‑formula** or **targeted maximum likelihood estimation (TMLE)** to estimate the average treatment effect (ATE):

\[
\text{ATE} = \mathbb{E}\bigl[ Y^{(1)} - Y^{(0)} \bigr].
\]

The required assumptions (sequential ignorability) are the same as those underlying the IPW approach above, but the TMLE implementation provides double robustness and often better finite‑sample performance.

---

### 2.4  Summary of the complete workflow  

| Step | What you do | Why |
|------|-------------|-----|
| **1. Data split** | Reserve a forward‑rolling test period; keep training data strictly earlier in time. | Avoid temporal leakage. |
| **2. Fit model A** | Use all training events, predictors \(X^A\) only. | Baseline predictor available for every event. |
| **3. Fit model AB** | Use only training events where B is observed; predictors \(X^A, X^B\). | Learns joint relationship without imputation bias. |
| **4. Incremental predictive value** | On test events with B, compute paired scores and a paired test. | Isolates pure information gain of B. |
| **5. Propensity model for B** | Estimate \(\Pr(D=1\mid X^A, Z)\). | Removes selection bias when B is missing. |
| **6. Simulate policies** | Apply P₁ (early) and P₂ (wait) to every test event, using the appropriate model and the actual waiting time. | Captures operational consequences of delay. |
| **7. Weighted utility comparison** | Use IPW or TMLE to estimate the mean utility difference \(\Delta^{\text{op}}\). | Gives unbiased estimate of the *value of waiting*. |
| **8. Decision** | If (i) incremental predictive value is significant **and** (ii) the weighted utility difference is positive, then B is worth waiting for; otherwise, act early. | Combines both aspects of the original question. |

---

## 3.  Final answer (concise)

*Yes*, the two‑part evaluation you proposed can be made statistically defensible **provided** you:

1. **Separate the two questions**:  
   * *Incremental information* – evaluate paired predictions on the *subset where B actually arrives* using a proper scoring rule and a paired statistical

*Original question: [How can I separate the incremental predictive value of a delayed data source from the effect of waiting?](https://stats.stackexchange.com/questions/677385/how-can-i-separate-the-incremental-predictive-value-of-a-delayed-data-source-fro) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
