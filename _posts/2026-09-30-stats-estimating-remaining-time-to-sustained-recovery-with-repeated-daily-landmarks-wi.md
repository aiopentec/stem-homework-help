---
layout: question
title: Estimating remaining time to sustained recovery with repeated daily landmarks
  within stock drawdowns
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Estimating remaining time to sustained
  recovery with repeated daily landmarks within stock drawdowns'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking – plain‑language restatement  

You have daily closing prices for a few Egyptian stocks.  
During a **draw‑down** (the price is below the recent high) you would like, **at each trading day**, to predict the probability that the stock will “recover” within a short, medium, or long horizon:

| horizon | meaning in the problem |
|---------|------------------------|
| 5 sessions   | recovery within the next 5 trading days |
| 21 sessions  | recovery within the next 21 trading days |
| 126 sessions | recovery within the next 126 trading days |

A **recovery** is defined (for now) as:  

1. The first closing price that exceeds the maximum of the previous 10 closes, **and**  
2. The next 5 closes all stay above that breakout level.  

Those five “post‑breakout” closes are the **outcome**; they must never be used as predictors.

Because many days belong to the same draw‑down episode, the daily “landmark” observations are **not independent**.  
You want to know:

* How to build the **risk set** (i.e. which landmarks are eligible to be counted for each horizon) while respecting censoring (administrative end‑of‑study, unresolved prices, etc.)?  
* What **validation unit** (what should stay together when you split the data into training / test folds) is appropriate?  
* Whether a **discrete‑time landmark survival model** is suitable, and if so, **how to handle the episode‑level dependence** when you compare one predictor at a time (e.g. 3‑day return, volume‑to‑20‑day‑average, …).

The answer below walks through every step required to construct a proper dataset, fit a calibrated model, and evaluate it while accounting for the within‑episode correlation.

---

## 2.  Step‑by‑step solution  

### 2.1  Define the basic entities  

| Entity | Symbol | Description |
|--------|--------|-------------|
| Stock *s* |  | e.g. ABUK, FWRY |
| Draw‑down episode *e* (belonging to stock *s*) |  | a contiguous period that starts at the first day the price falls below the preceding 10‑day high and ends when a **consistent** recovery (the 5‑day post‑breakout rule) is observed or the episode is censored |
| Landmark day *l* (within episode *e*) |  | a trading day on which a prediction is made (i.e. every day while the episode is “open”) |
| Horizon *h* ∈ {5, 21, 126} |  | number of sessions ahead for which we want the recovery probability |
| Outcome *Y*<sub>l,h</sub> | 0/1 | 1 if a consistent recovery occurs **strictly within** the next *h* sessions after landmark *l*; 0 otherwise (including censored cases) |
| Censoring indicator *C*<sub>l</sub> | 0/1 | 1 if the observation is right‑censored before we can see the outcome for the longest horizon (e.g. episode ends, data series ends, unresolved price) |

### 2.2  Build the **episode table**  

1. **Detect draw‑down start**  
   * For each day *t* compute `max10_t = max(Close_{t‑9}, …, Close_t)`.  
   * A draw‑down starts on the first day after a day where `Close_t < max10_t`.  

2. **Detect a “consistent” recovery** (the label)  
   * Scan forward until a day *b* where `Close_b > max10_b`.  
   * Check that `Close_{b+1}, …, Close_{b+5}` are all ≥ `Close_b`.  
   * If yes, the episode **ends** on day *b+5* (the last of the five confirming closes).  

3. **Censoring**  
   * If the series ends before a consistent recovery is seen → right‑censor episode at the last observed day.  
   * If any of the 5 confirming closes are missing or marked *unresolved* → treat the episode as censored at the first missing day.  

4. Store for each episode *e*:  
   * `stock`, `episode_id`, `start_date`, `end_date` (or censoring flag), `max10_at_start`, etc.

### 2.3  Expand to **landmark‑level rows**  

For every episode *e* with start date *t₀* and (possibly censored) end date *t_end*:

```
for each day t = t₀, t₀+1, … , t_end:
        for each horizon h in {5,21,126}:
                if t + h ≤ t_end   (i.e. we can observe h days ahead)
                        Y_lh = 1 if a consistent recovery occurs on any day ≤ t+h
                        else Y_lh = 0
                else
                        C_l = 1   (right‑censored for horizon h)
```

Resulting **long data set** has one row per (episode, landmark day, horizon).  
Columns include:

* `stock`, `episode_id`, `landmark_date` (t)
* `horizon` (h)
* `outcome` (`Y`), `censor` (`C`)
* Predictor values **computed only from information available at t** (e.g. 3‑day return ending on t, volume/t‑20‑day‑mean ending on t, etc.)

### 2.4  Construct the **risk set** for each horizon  

In discrete‑time survival language the **risk set** at horizon *h* consists of all landmark rows where the observation is *not* censored for that horizon:

```
RiskSet_h = { (l, h) : C_lh = 0 }
```

Only those rows enter the likelihood for horizon *h*.  
Rows censored before horizon *h* contribute to the likelihood for shorter horizons (if they are uncensored there) but not for longer ones.

### 2.5  Choose the **validation unit**  

Because landmarks within the same episode share the same future price path, splitting the data at the **daily‑landmark** level would leak information (the training set could contain a landmark that is only a few days away from a landmark in the test set, and both share the same eventual recovery).  

**Recommendation:**  
* **Unit of validation = whole episode** (i.e. all landmarks belonging to the same draw‑down).  
* When you create folds, **keep every landmark of an episode together** and never place two landmarks from the same episode into different folds.

#### 2.5.1  Chronological (time‑series) folds  

* Sort episodes by their start date.  
* Divide the ordered list into *K* contiguous blocks (e.g. K = 5).  
* For fold *k*: train on episodes in blocks 1,…,k‑1; test on block *k*.  
* This respects the “future‑cannot‑inform‑past” principle and mimics a realistic forecasting situation.

### 2.6  Model: **Discrete‑time landmark survival**  

For each horizon *h* you can fit a logistic (or complementary‑log‑log) model of the form  

\[
\Pr(Y_{lh}=1 \mid \mathbf X_{l}) = \text{logit}^{-1}\bigl(\beta_{0h} + \beta_{1h} X_{1l} + \dots + \beta_{ph} X_{pl}\bigr)
\]

where  

* \(\mathbf X_{l}\) are the predictors measured at landmark *l* (they are the same for all horizons, but you may allow horizon‑specific coefficients).  
* The likelihood uses only rows in `RiskSet_h`.  

**Why discrete‑time?**  
* Your horizons are measured in whole sessions, not in continuous calendar time.  
* The event (recovery) can only be observed at integer session boundaries.  
* The model directly yields calibrated probabilities for each horizon.

#### 2.6.1  Handling episode‑level dependence  

Two common ways:

| Method | How it works | When to use |
|--------|--------------|-------------|
| **Cluster‑robust (sandwich) SE** | Fit the logistic model ignoring dependence, then compute variance‑covariance matrix that is robust to arbitrary correlation within each `episode_id`. | If you only need inference (p‑values, CI) and the number of episodes is moderate‑large (>30). |
| **Mixed‑effects (random intercept) model** | Add a random intercept \(u_e \sim N(0,\sigma^2_u)\) for each episode *e*: \(\text{logit}(p_{leh}) = \beta_{0h}+u_e+\beta^{\top}\mathbf X_l\). Fit by Laplace approximation or adaptive Gaussian quadrature. | When you suspect that episodes have heterogeneous baseline hazards and you want the model to *borrow strength* across episodes. Also useful for out‑of‑sample prediction because the random effect can be set to its posterior mean (≈0) for a new episode. |
| **Frailty survival model** (continuous‑time analog) | Same idea as random intercept but expressed in a proportional‑hazards framework; not needed here because we are already in discrete time. | – |

For **predictor‑screening** (one predictor at a time) the simplest approach is to fit a *marginal* logistic model with **cluster‑robust SE**. When you later combine predictors, you may switch to the mixed‑effects version to improve calibration.

### 2.7  Model‑assessment metrics (calibration & discrimination)  

Because the goal is **calibrated probabilities**, use:

* **Brier score** (scaled) for each horizon, computed on the held‑out episodes of each fold.  
* **Calibration plot** (decile‑wise observed vs. predicted recovery rates).  
* **Time‑dependent AUC** (c‑index for discrete time) if you also care about ranking.

All metrics must be aggregated **episode‑wise** (i.e., average over all landmark rows in the test episodes) to avoid double‑counting the same future recovery.

### 2.8  Putting it all together – workflow  

1. **Pre‑process** raw price/volume data → clean dates, handle corporate actions.  
2. **Identify draw‑down episodes** → start, end, censoring flag.  
3. **Create landmark‑horizon rows** → compute predictors using only data up to the landmark date.  
4. **Assign risk‑set flags** (`C_lh`).  
5. **Split episodes into chronological folds** (e.g., 5‑fold).  
6. For each fold:  

   a. **Training set** = all rows from episodes in earlier folds.  

   b. **Fit** a discrete‑time logistic model for each horizon (or a pooled model with horizon indicator).  

   c. **Obtain predictions** on the test episodes (use fixed‑effects only; random intercept set to 0 if mixed model).  

   d. **Compute Brier score, calibration curves, AUC** for each horizon.  

7. **Aggregate** metric averages across folds → final estimate of out‑of‑sample performance.  

8. **Screen predictors**: repeat steps 6‑7 for each candidate predictor (or small sets). Compare Brier score improvements, use a paired‑fold test (e.g., DeLong for AUC, or bootstrap for Brier) that respects the episode‑level clustering.

### 2.9  Summary of the “what to use” answer  

| Question | Answer |
|----------|--------|
| **Risk‑set construction** | Use all landmark‑horizon rows that are **not censored** for that horizon (`C_lh = 0`). Rows censored before horizon *h* are excluded from the likelihood for *h* but may be kept for shorter horizons. |
| **Validation unit** | The **draw‑down episode** (all its daily landmarks) is the proper unit. Build chronological (time‑series) folds that keep whole episodes together. |
| **Is a discrete‑time landmark survival model appropriate?** | **Yes.** The problem is naturally cast as predicting a binary event within a fixed number of

*Original question: [Estimating remaining time to sustained recovery with repeated daily landmarks within stock drawdowns](https://stats.stackexchange.com/questions/677302/estimating-remaining-time-to-sustained-recovery-with-repeated-daily-landmarks-wi) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
