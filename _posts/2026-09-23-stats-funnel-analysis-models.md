---
layout: question
title: Funnel analysis models
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Funnel analysis models'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

A business wants to understand how customers move through a **sales funnel** (e.g. inactive → view → add‑to‑cart → purchase) and how a new marketing treatment (e.g. a promotion, an email, a UI change) changes those movements.  

The student proposes:

* representing each stage with a binary variable that is 1 if the customer has reached that stage during a given time interval (week, month, …);
* conditioning on the customer’s previous stage(s) and on the treatment indicator;
* fitting a *multiclass* logistic regression to predict the next stage.

The question is:  

> **Which statistical‑modeling tools are appropriate for this type of “funnel analysis”, especially when we want to (a) respect the sequential/Markov‑type nature of the process and (b) make causal statements about the treatment?**  

We need to give a complete, step‑by‑step answer that shows how to set up the data, which models are available, how to estimate transition probabilities, and how to incorporate causal inference ideas (e.g., marginal‑structural models, inverse‑probability weighting).  

---

## 2.  Step‑by‑step solution  

Below is a **self‑contained workflow** that a practitioner can follow.  
All notation is defined as we go; nothing is assumed to be known beforehand.

### Step 1 – Define the states and the observation schedule  

| State label | Description                                   |
|-------------|-----------------------------------------------|
| 0           | Inactive (no activity in the interval)       |
| 1           | Viewed at least one item                     |
| 2           | Added at least one item to the cart          |
| 3           | Purchased at least one item                  |

We observe every customer *i* at discrete time points *t = 1, 2, …, T* (e.g., weeks).  
Let  

\[
S_{i,t}\in\{0,1,2,3\}
\]

be the **most advanced** state that customer *i* has reached by the end of interval *t*.  
(The “most advanced” rule guarantees a **mutually exclusive** coding: a customer who has purchased is automatically counted as having viewed and added‑to‑cart, but we keep only the highest level.)

The treatment variable is

\[
D_i\in\{0,1\}
\]

where 1 means the customer was exposed to the new marketing action (the exposure is assumed to be *time‑invariant* for simplicity; if it varies over time, replace \(D_i\) by \(D_{i,t}\) later).

### Step 2 – Build the transition‑probability matrix  

For a **first‑order Markov chain** the probability of moving from state *k* at time *t‑1* to state *ℓ* at time *t* is

\[
P_{k\ell}(t)=\Pr\bigl(S_{i,t}=ℓ \mid S_{i,t-1}=k,\; D_i\bigr),\qquad k,ℓ\in\{0,1,2,3\}.
\]

Because the treatment can alter these probabilities, we write them as functions of \(D_i\).

A convenient way to model each row of the transition matrix is a **multinomial logistic regression** (also called *conditional* or *baseline‑category* logit):

\[
\Pr\bigl(S_{i,t}=ℓ \mid S_{i,t-1}=k, D_i\bigr)
=
\frac{\exp\bigl(\alpha_{kℓ}+ \beta_{kℓ} D_i\bigr)}
     {\displaystyle\sum_{m\ge k} \exp\bigl(\alpha_{km}+ \beta_{km} D_i\bigr)},
\qquad ℓ\ge k,
\]

where the sum in the denominator runs over all *allowed* states (you cannot move “backwards”; e.g. from 2 to 1).  
If a customer is already in state 3 (purchase) they stay there, so the row for \(k=3\) contains a single probability equal to 1.

*Why multinomial logit?*  
It respects the **simplex constraint** (probabilities sum to 1) and lets us estimate a *treatment effect* \(\beta_{kℓ}\) for each possible forward jump (e.g., from “view” to “add‑to‑cart”).

### Step 3 – Estimate the parameters  

1. **Create the long‑format data set**  

| i | t | S_{i,t-1} | S_{i,t} | D_i |
|---|---|----------|--------|-----|
| 1 | 1 | 0        | 1      | 0   |
| 1 | 2 | 1        | 2      | 0   |
| … | … | …        | …      | …   |

2. **Fit a separate multinomial logit for each “origin” state** (or fit a single model with interaction terms).  
   In R, the `nnet::multinom()` function or `mlogit` package can be used; in Python, `statsmodels.MNLogit` works.

3. **Interpret \(\beta_{kℓ}\)**  

   * \(\exp(\beta_{kℓ})\) is the **odds ratio** for moving from *k* to *ℓ* when the treatment is present versus absent, holding the origin state fixed.  

   *If you prefer a causal risk‑ratio, you can convert the fitted probabilities to risk differences or ratios using the **g‑formula** (see Step 5).*

### Step 4 – Allow for longer memory (higher‑order Markov) if needed  

If you suspect that the previous *k* intervals matter (e.g., a user who viewed three weeks ago is more likely to purchase than one who viewed only last week), extend the conditioning set:

\[
\Pr\bigl(S_{i,t}=ℓ \mid S_{i,t-1}=k_1,\;S_{i,t-2}=k_2,\dots, D_i\bigr).
\]

Practically this is done by **augmenting the covariate vector** with lagged states (or lagged indicator variables) and fitting the same multinomial logit.  
To keep the model parsimonious, you can:

* Collapse lagged states into a single “history score” (e.g., number of weeks in each state);
* Use **regularisation** (LASSO, ridge) to shrink unnecessary lag coefficients to zero.

### Step 5 – Causal inference: marginal‑structural model (MSM)  

The multinomial logit above estimates **association** conditional on the observed history.  
If treatment assignment is *confounded* by prior behavior (e.g., more “active” users are more likely to be targeted), we need **inverse‑probability‑of‑treatment weighting (IPTW)**.

1. **Fit a propensity model** for the treatment:

   \[
   e_i = \Pr(D_i=1 \mid \mathbf{X}_i),
   \]

   where \(\mathbf{X}_i\) includes baseline covariates and possibly summary measures of the early funnel (e.g., number of views in the first two weeks).

2. **Compute stabilized weights**  

   \[
   w_i = \frac{\Pr(D_i)}{e_i^{D_i}(1-e_i)^{1-D_i}}.
   \]

3. **Re‑fit the multinomial transition model** using these weights (most software accepts a `weights=` argument).  
   The resulting \(\beta_{kℓ}\) now has a **causal interpretation**: the *average treatment effect* on the odds of moving from state *k* to *ℓ* over the whole population.

If treatment can change over time (e.g., weekly email), you would construct **time‑varying** IPTW that also conditions on past treatment and past states (the classic *g‑formula* / *g‑estimation* set‑up).

### Step 6 – Alternative (and often complementary) modelling frameworks  

| Approach | When it shines | How it handles the funnel |
|----------|----------------|---------------------------|
| **Discrete‑time survival (hazard) models** | You care about *time to* a specific event (e.g., purchase) and censoring is present | Model hazard of *first* transition to each higher state using logistic (or complementary log‑log) link; can incorporate time‑varying covariates. |
| **Multi‑state (illness‑death) models** | You want *all* intermediate transitions, possibly allowing “backward” moves | Define a state‑transition intensity matrix; estimate with `mstate` (R) or `msm` packages; can incorporate covariates via proportional‑hazards form. |
| **Hidden Markov models (HMMs)** | The observed actions are noisy indicators of a latent “interest” level | Treat the true funnel stage as hidden; estimate via EM algorithm; useful when you suspect mis‑classification (e.g., view logged but not truly engaged). |
| **Bayesian hierarchical Markov models** | Small samples per segment, want to borrow strength across segments (e.g., regions, device types) | Put priors on transition probabilities; obtain posterior distributions for treatment effects; easy to propagate uncertainty to downstream metrics. |
| **Reinforcement‑learning / dynamic treatment regime** | You plan to *optimise* a sequence of interventions (e.g., send reminder only if still in “view” state) | Estimate Q‑functions or policy‑value using observed data (e.g., via doubly‑robust off‑policy evaluation). |

### Step 7 – Model checking and validation  

1. **Goodness‑of‑fit for each row** – Compare observed transition frequencies to those predicted by the fitted multinomial model (Pearson χ² or deviance).  

2. **Predictive performance** – Use **cross‑validation**: hold out a subset of customers, predict their next‑step distribution, compute log‑loss or Brier score.  

3. **Calibration** – For each origin state, plot observed vs. predicted probabilities across deciles of the fitted propensity.  

4. **Sensitivity to unmeasured confounding** – Apply **E‑value** calculations or conduct a Rosenbaum‑bounds analysis if you cannot measure all relevant covariates.

---

## 3.  Final answer – What modelling tools are appropriate?  

1. **Base model** – A **first‑order discrete‑time Markov chain** where each row of the transition matrix is estimated with a **multinomial logistic regression** (or equivalently a series of conditional logistic models). This respects the ordered, non‑backward nature of the funnel and gives state‑specific treatment effects.

2. **Causal extension** – Combine the above with **inverse‑probability‑of‑treatment weighting** (or a full **marginal‑structural model**) to obtain causal estimates of the treatment’s impact on each transition probability.

3. **If longer memory is believed to matter**, simply add lagged states as covariates; regularisation can keep the model tractable.

4. **Alternative frameworks** that may be preferable in specific settings:  
   * **Discrete‑time survival / hazard models** (focus on time to purchase);  
   * **Multi‑state (illness‑death) models** (allow arbitrary forward/backward moves);  
   * **Hidden Markov or Bayesian hierarchical Markov models** (mis‑classification or small‑sample borrowing).  

In practice, start with the simple multinomial‑logit Markov model, diagnose fit, then layer causal weighting or higher‑order history as needed.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the binary indicators \(v_{i,t},c_{i,t},b_{i,t}\) as independent outcomes** | They are **nested** (if you purchased you must have viewed and added to cart); modeling them separately violates the logical ordering and inflates error. | Collapse to a *single* ordered state variable \(S_{i,t}\) and model transitions. |
| **Using ordinary multinomial logistic regression *without* weighting when treatment is confounded** | The estimated \(\beta\)’s then reflect both treatment effect and the effect of the confounder (e.g., “high‑activity” users are more likely to be treated). | Estimate a propensity score and apply IPTW (or use a doubly‑robust estimator). |
| **Assuming a first‑order Markov property when the data really need longer memory** | Transition probabilities will be biased if past history (e.g., number of weeks already in “view”) influences the next step. | Test for higher‑order dependence (e.g., add lagged state as covariate, compare AIC/BIC) and retain useful lags. |
| **Forgetting that probabilities must sum to 1 within each origin state** | Fitting separate binary logistic regressions for each possible jump can produce impossible probability vectors (>1). | Use a **multinomial** (or conditional) logistic model that enforces the simplex constraint. |
| **Ignoring censoring / attrition** | Customers may drop out of the platform; treating them as “inactive” can bias transition estimates. | Treat dropout as an absorbing state or use survival‑analysis techniques that handle right‑censor

*Original question: [Funnel analysis models](https://stats.stackexchange.com/questions/677247/funnel-analysis-models) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
