---
layout: question
title: Why is the difference of AIC between generalized least square (GLS) and phylogenetic
  generalized least square (PGLS) for several traits the same?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Why is the difference of AIC between
  generalized least square (GLS) and phylogenetic generalized least square (PGLS)
  for '
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

The student is fitting two kinds of linear models to the same set of trait data for 20 tips (10 lineages × 2 ploidy levels):

* **GLS** – a regular generalized least‑squares model that assumes the residuals are independent (i.e. the covariance matrix is σ² I).  
* **PGLS** – a phylogenetic GLS that replaces the identity matrix by a covariance matrix derived from a phylogeny (often multiplied by a parameter λ).

After fitting the two models they compute  

* the log‑likelihoods,  
* the likelihood‑ratio (LR) statistic, and  
* the AIC for each model.

For *every* trait they obtain exactly the same numbers:

```
ΔAIC  = 261.15
LR    = 261.15
```

They wonder why the AIC difference is identical to the LR statistic and why the value does not change from trait to trait.

---

## 2. Step‑by‑step explanation

### 2.1.  AIC and the LR statistic

For a model fitted by maximum likelihood

\[
\text{AIC}=2k-2\log L,
\]

where  

* \(k\) = number of estimated parameters (including σ² and any phylogenetic parameters such as λ),  
* \(\log L\) = maximised log‑likelihood.

Consider two nested models, **M0** (the “simpler” GLS) and **M1** (the “more complex” PGLS).  
Their AIC values are

\[
\begin{aligned}
\text{AIC}_0 &= 2k_0 - 2\log L_0,\\
\text{AIC}_1 &= 2k_1 - 2\log L_1 .
\end{aligned}
\]

The **difference in AIC** is therefore

\[
\Delta\text{AIC}= \text{AIC}_0-\text{AIC}_1
                = 2(k_0-k_1) - 2(\log L_0-\log L_1).
\tag{1}
\]

The **likelihood‑ratio (LR) statistic** is defined as

\[
\text{LR}= -2\bigl(\log L_0-\log L_1\bigr)
        = 2(\log L_1-\log L_0).
\tag{2}
\]

Comparing (1) and (2),

\[
\boxed{\Delta\text{AIC}= \text{LR}+2(k_0-k_1)}.
\]

Thus **if the two models have the same number of free parameters** (\(k_0=k_1\)), the second term disappears and

\[
\Delta\text{AIC}= \text{LR}.
\]

That is exactly what the student observed.

### 2.2.  Why GLS and PGLS often have the *same* number of parameters

| Model | Parameters that are estimated |
|-------|------------------------------|
| GLS  | intercept (β₀), slope(s) β, residual variance σ² |
| PGLS | intercept, slope(s) β, residual variance σ², **and possibly** λ (if λ is *estimated*) |

If λ is **fixed** (e.g. λ = 0 or λ = 1) the PGLS does **not** add a new free parameter – the only thing that changes is the *covariance matrix* used to evaluate the likelihood.  
Even when λ is *estimated*, most software treats λ as a **single** extra parameter, so the total number of parameters becomes \(k_1 = k_0+1\). In that case the AIC difference would be

\[
\Delta\text{AIC}= \text{LR} - 2,
\]

because the more complex model pays a penalty of 2 extra parameters.

In the student’s runs the AIC‑difference is **exactly** the LR, meaning the two models have the *same* \(k\). Hence λ must have been **fixed** (or the software treats the phylogenetic covariance as a known matrix rather than a parameter to be estimated).

### 2.3.  Why the same numerical value appears for every trait

The LR (and therefore ΔAIC) is a function of the **difference in log‑likelihoods** between the two fitted models:

\[
\text{LR}= -2(\log L_{\text{GLS}}-\log L_{\text{PGLS}}).
\]

If the data for each trait are completely unrelated to the phylogeny (i.e. the phylogenetic covariance matrix is essentially an identity matrix for that trait), then the two log‑likelihoods will be *identical* for every trait, giving an LR of **zero**.  

However, the student reports a **large, constant** LR of 261.15. This can happen only when the *same* numerical difference in log‑likelihoods is obtained for all traits. In the reproducible example they built, the design matrix (intercept‑only, or the same set of predictors) is identical for every trait, and the covariance matrix supplied to the PGLS is the *same* for all traits. Consequently, the maximised log‑likelihood for each trait differs from the GLS log‑likelihood by exactly the same amount (the contribution of the phylogenetic covariance). The result is a constant LR across traits.

In short: the **pattern** (ΔAIC = LR) is a mathematical consequence of equal numbers of parameters; the **numerical constancy** (same 261.15 for every trait) is a consequence of using the *same* phylogenetic covariance matrix and the *same* set of predictors for each trait.

### 2.4.  What this tells you about model comparison

* When \(k_0=k_1\) (no extra free parameters), the LR test and the ΔAIC carry exactly the same information.  
* Because the LR test assumes the simpler model is a *nested* special case of the complex one, you can use it **only** if the complex model truly adds parameters (e.g., estimating λ). If λ is fixed, the two models are not nested in the usual sense, and a formal LR test is not appropriate.  
* In practice, when comparing a GLS (independent residuals) to a PGLS **with a freely estimated λ**, you should expect a ΔAIC that is **LR – 2** (penalising the extra λ parameter). If you still see ΔAIC = LR, check that λ is indeed being estimated.  

---

## 3. Final answer (concise)

*The difference in AIC between the GLS and the PGLS is identical to the likelihood‑ratio statistic because both models have the **same number of estimated parameters**. When \(k_{\text{GLS}} = k_{\text{PGLS}}\),

\[
\Delta\text{AIC}=2k_{\text{GLS}}-2\log L_{\text{GLS}}-
                \bigl(2k_{\text{PGLS}}-2\log L_{\text{PGLS}}\bigr)
               =-2(\log L_{\text{GLS}}-\log L_{\text{PGLS}})
               =\text{LR}.
\]

Thus the AIC difference must equal the LR value (261.15 in the example).  

The fact that the **same numerical value** (261.15) appears for all six traits occurs because the same phylogenetic covariance matrix and the same set of predictors are used for every trait, giving the same log‑likelihood gap for each trait.*

---

## 4. Common mistakes and how to avoid them

| Mistake | Why it’s wrong | How to fix / check |
|---------|----------------|--------------------|
| **Assuming AIC automatically incorporates phylogeny** | AIC only penalises *parameter count*, not the structure of the covariance matrix. | Verify whether the phylogenetic model adds a free parameter (e.g., λ). If λ is fixed, the AIC penalty is unchanged. |
| **Using a likelihood‑ratio test when the two models have the same number of parameters** | The LR test is meant to compare nested models that differ by at least one free parameter; otherwise the test statistic has no chi‑square distribution. | Either (a) estimate λ (adds one parameter) and then use LR with 1 df, or (b) compare models with AIC or a bootstrap‑based test. |
| **Thinking that different traits must give different AIC differences** | AIC depends on the *difference* in log‑likelihoods; if the same covariance matrix and predictor set are used, the difference can be identical across traits. | Look at the raw log‑likelihoods for each trait to confirm they differ by the same amount; if you want trait‑specific phylogenetic effects, let λ be estimated separately for each trait. |
| **Forgetting that λ=0 corresponds to ordinary GLS** | If λ is estimated but the optimiser returns exactly 0, the PGLS collapses to GLS, making the models identical. | Inspect the estimated λ value and its confidence interval; if it hits the boundary (0 or 1), treat the model as effectively GLS. |
| **Using the same tree for all traits without checking branch length scaling** | Branch lengths affect the covariance matrix; if they are not appropriate for a given trait, the model may be misspecified. | Rescale the tree (e.g., `chronos`, `ape::rescale`) or use a trait‑specific λ to allow the data to determine the appropriate phylogenetic signal. |

---

*Original question: [Why is the difference of AIC between generalized least square (GLS) and phylogenetic generalized least square (PGLS) for several traits the same?](https://stats.stackexchange.com/questions/677457/why-is-the-difference-of-aic-between-generalized-least-square-gls-and-phylogen) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
