---
layout: question
title: Post Lasso OLS Fit
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Post Lasso OLS Fit'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. Restating the Question in Plain Language  

You ran a LASSO regression on a data set that has **only 22 observations** but **22 potential predictor variables**.  
The LASSO kept **between 16 and 20** of those predictors (i.e., most of them are still in the model).  

Now you want to run a **“post‑LASSO” ordinary least‑squares (OLS) regression** on the variables that survived the LASSO step.  

**The dilemma:**  
- With so many predictors relative to the tiny sample size, OLS will be unstable and may over‑fit.  
- How many of the retained predictors should you actually include in the final OLS model?

---

## 2. Step‑by‑Step Solution  

Below is a systematic way to decide how many (and which) variables to keep for a post‑LASSO OLS fit.

### Step 1: Check the Basic Feasibility Condition  

For ordinary OLS to be uniquely estimable we need  

\[
p_{\text{OLS}} \;<\; n
\]

where  

* \(p_{\text{OLS}}\) = number of predictors you will finally include (including the intercept)  
* \(n\) = number of observations (22 in your case).

If you keep **all** 16–20 LASSO‑selected variables, you will have \(p_{\text{OLS}} \approx n\).  
That means:

* The design matrix \(\mathbf X\) will be **nearly singular** → inflated standard errors, unstable coefficient estimates, and unreliable inference.  

**Rule of thumb:** keep \(p_{\text{OLS}} \leq n/2\) (i.e., ≤ 11 for \(n=22\)) to obtain reasonably stable OLS estimates.  

---

### Step 2: Rank the LASSO‑Selected Predictors  

The LASSO gives you coefficient estimates \(\hat\beta^{\text{lasso}}_j\).  
Use the **absolute magnitude** of these coefficients as a proxy for each variable’s importance:

| Variable | \(|\hat\beta^{\text{lasso}}_j|\) |
|----------|-------------------|
| \(X_1\) | 2.34 |
| \(X_2\) | 0.87 |
| … | … |
| \(X_{20}\) | 0.02 |

*(Replace the dummy numbers with your actual output.)*

Order the variables from largest to smallest absolute coefficient.

---

### Step 3: Apply a Model‑Selection Criterion on the Ranked List  

Because we are in a **low‑\(n\), high‑\(p\)** setting, we need a criterion that penalises model complexity heavily.  
Two common choices are **BIC** (Bayesian Information Criterion) and **Adjusted \(R^2\)**.  
BIC is preferred for its stronger penalty and its tendency to favour more parsimonious models.

#### Procedure  

1. **Create a sequence of candidate OLS models**:  
   - Model 1: top 1 predictor (largest \(|\hat\beta^{\text{lasso}}|\))  
   - Model 2: top 2 predictors  
   - …  
   - Model \(k\): top \(k\) predictors  

2. **Fit OLS for each candidate model** (using the original data, not the LASSO‑shrunken coefficients).  
   For each fitted model compute  

\[
\text{BIC}_k = n\log(\widehat{\sigma}^2_k) + \log(n)\,p_k
\]

where  

* \(\widehat{\sigma}^2_k = \frac{1}{n-p_k}\sum_{i=1}^n (y_i-\hat y^{(k)}_i)^2\)  
* \(p_k\) = number of predictors in model \(k\) (including intercept).  

3. **Select the model with the smallest BIC**.  

Because BIC heavily penalises each additional variable (\(\log n \approx 3.09\) for \(n=22\)), you will typically end up with a model far smaller than the original 16‑20 set.

---

### Step 4: Verify that the Chosen Model Satisfies the “Rule‑of‑Thumb”  

Suppose the BIC procedure picks **\(p_{\text{OLS}} = 7\)** predictors.  

* Check: \(7 < 22\) ✅  
* Check: \(7 \leq n/2 = 11\) ✅  

If the BIC selected a model with, say, 15 predictors, you would **override** that result and apply an additional pruning step (e.g., keep only the 10 with the largest absolute LASSO coefficients) because the OLS estimates would be too noisy.

---

### Step 5: Fit the Final Post‑LASSO OLS Model  

Using the subset identified in Step 3 (or the trimmed version from Step 4), fit a standard OLS regression:

\[
y = \beta_0 + \sum_{j \in \mathcal S} \beta_j X_j + \varepsilon,
\]

where \(\mathcal S\) is the selected set of predictors (e.g., \(|\mathcal S| = 7\)).  

Report:

* Coefficient estimates \(\hat\beta_j\)  
* Standard errors, \(t\)-statistics, and \(p\)-values (now more reliable because the design matrix is well‑conditioned).  
* Model‑fit statistics (Adjusted \(R^2\), BIC, cross‑validated prediction error).  

---

### Step 6 (Optional): Double‑Selection / Post‑Selection Inference  

If your goal is **causal inference** (e.g., estimating the effect of a treatment variable), you may want to adopt the **double‑selection** method of Belloni, Chernozhukov, and Hansen (2014):

1. Run LASSO of \(y\) on all controls → keep selected set \(S_y\).  
2. Run LASSO of the treatment \(d\) on all controls → keep selected set \(S_d\).  
3. Take the **union** \(S = S_y \cup S_d\).  
4. Fit OLS of \(y\) on \(d\) and the variables in \(S\).  

Because the union typically contains fewer than the original 16–20 variables, this approach automatically guards against over‑fitting while delivering valid inference for the treatment coefficient.

---

## 3. Final Answer  

**You should not automatically keep all 16–20 LASSO‑selected predictors in a post‑LASSO OLS regression when you have only 22 observations.**  

1. **Rank** the retained variables by the absolute size of their LASSO coefficients.  
2. **Fit a series of OLS models** that add the variables one‑by‑one (starting with the largest).  
3. **Select the model that minimises a strong complexity‑penalising criterion** such as BIC (or, less aggressively, adjusted \(R^2\)).  
4. **Make sure the final model obeys \(p_{\text{OLS}} < n\) and preferably \(p_{\text{OLS}} \le n/2\)** to avoid unstable estimates.  
5. **Fit the chosen OLS model** and report the usual regression diagnostics.

In practice, with \(n=22\) you will almost always end up with **far fewer than 16 predictors**—often somewhere between **5 and 10** variables—depending on the BIC curve.  

---

## 4. Common Mistakes  

| Mistake | Why It’s Wrong | How to Avoid It |
|---------|----------------|-----------------|
| **Keeping every LASSO‑selected variable** in the OLS step. | With \(p\) close to \(n\), the OLS design matrix is ill‑conditioned → huge variance, over‑fitting, meaningless \(p\)‑values. | Use a model‑selection criterion (BIC, adjusted \(R^2\)) to trim the set. |
| **Choosing the number of predictors arbitrarily** (e.g., “keep 15 because LASSO gave 15”). | No statistical justification; the chosen model may have poor predictive performance. | Follow the systematic ranking‑and‑BIC procedure described above. |
| **Relying on the LASSO coefficient magnitudes alone** as if they were unbiased estimates. | LASSO shrinks coefficients; the magnitude is biased and does not reflect true effect size. | Use the magnitudes only for **ranking**; final coefficient estimates must come from OLS after selection. |
| **Ignoring the “p < n” rule** and fitting OLS with \(p \ge n\). | The OLS normal equations have no unique solution; the regression will fail or give infinite‑variance estimates. | Always verify that the final predictor count is strictly less than the number of observations. |
| **Failing to check multicollinearity** after selecting variables. | Even a small set can be highly collinear, inflating standard errors. | Examine variance inflation factors (VIF) after the OLS fit; drop or combine variables with VIF > 10. |
| **Thinking that post‑LASSO OLS automatically fixes the bias of LASSO**. | OLS eliminates shrinkage bias **but** re‑introduces variance; with few observations the net MSE may increase. | Compare predictive performance (e.g., via cross‑validation) of the LASSO model versus the post‑LASSO OLS model before deciding which to report. |

By following the step‑by‑step protocol above and steering clear of these pitfalls, you will obtain a post‑LASSO OLS model that is both **statistically sound** and **practically useful** despite the very small sample size.

*Original question: [Post Lasso OLS Fit](https://stats.stackexchange.com/questions/677258/post-lasso-ols-fit) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
