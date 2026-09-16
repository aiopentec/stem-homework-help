---
layout: question
title: Which statistical method should I use to analyze DOE results from a nonlinear
  simulation?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Which statistical method should I
  use to analyze DOE results from a nonlinear simulation?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is really asking  

The student has run a **design‑of‑experiments (DOE)** simulation of a coupled combustion‑cycle process (10 controllable input variables, 5 output responses).  
He/she now needs a **statistical methodology** that will  

* tell which inputs have the biggest effect on each response,  
* reveal important interactions or nonlinear behaviours, and  
* do all of this **without** having to perform a full optimisation of the system.  

In short: *“Given the DOE data from a nonlinear simulation, how should I analyse it to identify the most influential factors and their (possibly nonlinear) relationships with the responses?”*  

---

## 2.  Step‑by‑step guide to a suitable analysis  

Below is a complete workflow that works for exactly this kind of problem.  
Each step is described in enough detail that you can implement it in any statistical package (R, Python / statsmodels, JMP, Minitab, Design‑Expert, …).

| Step | Goal | What you do | Why it works |
|------|------|-------------|--------------|
| **0️⃣ Prepare the data** | Clean, code, and centre/scale the inputs | • Put the 10 input variables (factors) in columns **X1 … X10**. <br>• Put each response in its own column **Y1 … Y5**. <br>• For each factor, compute a **coded value**:  \[x_i = (X_i – X_{i,mid}) / (X_{i,range}/2)\]  (centering at 0, scaling to ±1). | Coding makes the regression coefficients directly comparable and stabilises the numerical fitting of higher‑order terms. |
| **1️⃣ Choose a modelling framework** | Capture linear, quadratic, and interaction effects (i.e. non‑linearity) | **Second‑order (quadratic) response‑surface model** for each response:  \[Y = \beta_0 + \sum_{i=1}^{10}\beta_i x_i + \sum_{i=1}^{10}\beta_{ii} x_i^2 + \sum_{i<j}\beta_{ij} x_i x_j + \varepsilon\]  <br>Alternatively, if the data look highly non‑linear, consider a **Gaussian‑process (Kriging) surrogate** or **multivariate adaptive regression splines (MARS)**. | A quadratic model is the classic RSM approach; it is flexible enough to capture curvature and pairwise interactions while still being easy to interpret and to test with ANOVA. Non‑parametric surrogates are a safety‑net when curvature is extreme. |
| **2️⃣ Fit the model(s)** | Estimate the β‑coefficients | • Use **ordinary least squares (OLS)** for the quadratic model (most packages have a “quadratic” or “2‑FI + quadratic” option). <br>• For a GP, choose a kernel (e.g., squared‑exponential) and estimate hyper‑parameters by maximum likelihood. | OLS gives unbiased estimates if the errors are approximately normal and homoscedastic; GP gives a flexible fit and an inherent estimate of prediction uncertainty. |
| **3️⃣ Diagnose the fit** | Make sure the model is adequate | • **Residual plots** (residual vs. fitted, residual vs. each factor). <br>• **Normal‑probability plot** of residuals. <br>• **Lack‑of‑Fit test** (ANOVA partitioning of pure error vs. lack‑of‑fit). <br>• **Variance‑inflation factors (VIFs)** to check multicollinearity. | If residuals show patterns or the lack‑of‑fit test is significant, the quadratic model is insufficient → add higher‑order terms or switch to a non‑parametric surrogate. |
| **4️⃣ ANOVA on the fitted model** | Quantify which terms are statistically significant | • Run an **ANOVA table** for each response. <br>• The table decomposes the total sum of squares into: <br>  – Linear main effects (Σβ_i²), <br>  – Quadratic effects (Σβ_{ii}²), <br>  – Two‑factor interactions (Σβ_{ij}²), <br>  – Error. <br>• Obtain **p‑values** and **F‑statistics** for each effect. | Even though the underlying physics is nonlinear, the ANOVA is applied **to the fitted polynomial**; it tells you which linear/quad/interaction terms are needed to explain the variance. |
| **5️⃣ Rank factor importance** | Produce a clear “most influential variables” list | • **Standardised (β\*) coefficients**: divide each β by the standard deviation of its predictor. <br>• **Partial‑R²** for each term (or group of terms). <br>• **Main‑effect plots** (average response when a factor is varied, holding others at centre). | Standardised coefficients and partial‑R² are directly comparable across factors; main‑effect plots give a visual check of monotonic vs. curved behaviour. |
| **6️⃣ Visualise interactions & curvature** | Understand *how* factors act together | • **Interaction (contour) plots** for any pair whose β_{ij} is significant. <br>• **Response surface plots** (3‑D or level‑contour) for the most important two‑factor combinations. <br>• **Pareto chart of effects** (ordered by |β\*|). | Curved contour lines immediately reveal non‑linear coupling. A Pareto chart is the classic “quick‑look” tool in DOE analysis. |
| **7️⃣ Global sensitivity analysis (optional but powerful)** | Quantify the contribution of each factor (including higher‑order) to output variance *without* assuming a particular parametric form | • Build a surrogate (the quadratic model or GP). <br>• Compute **Sobol’ total‑order indices** or the **Morris elementary effects** using the surrogate. | Sobol indices give a *global* measure of influence that integrates over the whole input space, which is exactly what the student wants (“which variables have the greatest influence”). |
| **8️⃣ Multi‑response handling** | Summarise the five responses together, if desired | • **Separate models** for each Y (most straightforward). <br>• **Multivariate RSM** (e.g., fit a multivariate linear model or use canonical correlation). <br>• **Desirability function**: transform each response to a 0–1 scale, combine (geometric mean) to obtain a single “overall performance” metric for later ranking. | Separate models keep interpretation simple; the desirability approach is useful only when you later decide to *optimise* a weighted combination. |
| **9️⃣ Report the findings** | Communicate clearly to the advisor / thesis committee | • Table of **significant main effects** and **interactions** (including p‑values). <br>• Pareto chart of standardized effects. <br>• Representative contour plots for the strongest interactions. <br>• (If done) Sobol total‑order indices. <br>• Short narrative: “Factor X₃ (feed flow) explains ~35 % of the variance in outlet temperature; the X₃·X₇ interaction adds another 12 % …”. | A concise, visual, and statistical summary directly answers the original goal. |

### Quick checklist for implementation (R example)

```r
# 0. Load packages
library(rsm)          # quadratic RSM fitting
library(car)          # VIF, residual plots
library(ggplot2)
library(sensitivity) # Sobol indices

# 1. Code the factors (assuming df is your raw data)
code_factor <- function(col, low, high){
  (df[[col]] - (low+high)/2) / ((high-low)/2)
}
df$cX1 <- code_factor("X1", low1, high1)
# repeat for X2 … X10

# 2. Fit quadratic model for response Y1
fitY1 <- rsm(Y1 ~ SO(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10), data = df)

# 3. Diagnostics
par(mfrow=c(2,2))
plot(fitY1)                # residuals, qq-plot, etc.
vif(lm(Y1 ~ ., data = df[,c(paste0("cX",1:10))]))  # multicollinearity

# 4. ANOVA table
anova(fitY1)

# 5. Standardised coefficients
std_coefs <- summary(fitY1)$coefficients[, "Estimate"] *
             sd(df[, paste0("cX",1:10)])   # adjust per predictor
```

(Replace `SO` with `FO` + `TWI` + `PQ` if you prefer to specify linear, interaction, quadratic parts explicitly.)

---

## 3.  Final answer (concise)

**Use a second‑order response‑surface model (RSM) for each response, fit it by ordinary least squares, and then apply ANOVA to the fitted model to test the significance of linear, quadratic, and interaction terms.**  

* The quadratic model captures the curvature inherent in combustion simulations.  
* ANOVA on the fitted model tells you which factors and which interactions truly affect each output.  
* Complement the ANOVA with **standardised effect sizes**, **main‑effect / interaction plots**, and, if you want a truly global picture, compute **Sobol (or Morris) sensitivity indices** on the fitted surrogate.  

If residual diagnostics show that the quadratic model is inadequate, replace it with a **Gaussian‑process (Kriging) surrogate** and repeat the sensitivity‑analysis step.  

Thus, the workflow provides **both statistical significance** and **practical ranking of the most influential variables**, fulfilling the student’s goal without the need to run a full optimisation.

---

## 4.  Common mistakes & how to avoid them  

| Mistake | Why it’s a problem | Remedy |
|---------|-------------------|--------|
| **Treating ANOVA as “only for linear models”.** | ANOVA can be performed on *any* fitted regression model, including quadratic or higher‑order terms. | Fit a polynomial model first, then run ANOVA on that model. |
| **Ignoring interaction terms** because they look “complicated". | Interactions often dominate in combustion (e.g., temperature × pressure). Dropping them can hide the real physics. | Use a design that can estimate interactions (full‑factorial, CCD, Box‑Behnken) and keep any interaction with p < 0.1 (or based on effect size). |
| **Running too few experimental runs** (e.g., only a 2‑level factorial). | A 2‑level design cannot estimate curvature; you’ll falsely conclude linearity. | For 10 factors, a **central‑composite design** (≈ 2·k + 2·k + 1 = 41 runs) is the minimum to fit a full quadratic model. |
| **Not coding/centering the factors**. | Raw units can cause severe scaling problems; quadratic terms become huge and cause numerical instability. | Always transform to coded variables (−1, 0, +1) before fitting. |
| **Relying only on p‑values without looking at effect size**. | With many runs, tiny effects can be “significant” but practically irrelevant. | Report both **p‑values** and **standardised coefficients / partial‑R²**. |
| **Fitting separate models for each response and then “optimising” a combined desirability** when optimisation is *not* required. | Adds unnecessary complexity and can mask the individual physics of each response. | Keep responses separate for the influence study; only combine if you later need a trade‑off analysis. |
| **Skipping residual diagnostics**. | Violations of normality or heteroscedasticity invalidate the ANOVA F‑tests. | Plot residuals, conduct lack‑of‑fit test, transform response (log, Box‑Cox) if needed. |
| **Using the same model for all responses without checking adequacy**. | One response may be well described by a quadratic surface, another may need a more flexible surrogate.

*Original question: [Which statistical method should I use to analyze DOE results from a nonlinear simulation?](https://stats.stackexchange.com/questions/677082/which-statistical-method-should-i-use-to-analyze-doe-results-from-a-nonlinear-si) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
