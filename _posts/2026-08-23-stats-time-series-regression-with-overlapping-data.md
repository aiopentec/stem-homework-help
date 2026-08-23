---
layout: post
title: Time series regression with overlapping data
author: StemFix Bot
category: stats
tags:
- stats
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student has built a **linear regression** that tries to explain the *year‑on‑year (YoY) return of the S&P 500* at month *t* with  

* the same YoY return 12 months earlier,  
* the current credit‑spread,  
* the **future** (lead) values of inflation and industrial production (2‑month ahead), and  
* a dummy that flags “high‑inflation” periods.

All variables are **computed from monthly data**, but the dependent variable is a *rolling* YoY return: for every month we compare the index level to the level twelve months earlier.  
Hence each observation shares 11 of the 12 monthly returns that appear in the adjacent observation – the data are **overlapping**.

The model is estimated by ordinary least squares (OLS) and then used for 1‑, 2‑ and 3‑month‑ahead forecasts. The future values of inflation and industrial production are supplied by separate ARIMA forecasts; the credit‑spread forecasts are “mental estimates”.

The student wants to know:

1. Does the OLS regression make sense when the observations overlap?  
2. Are the coefficient estimates unbiased / consistent?  
3. Are the usual OLS standard errors valid, or do we need a correction?  
4. Is the whole forecasting procedure statistically sound?

Below we answer each of these points **step‑by‑step**, showing the relevant mathematics, the intuition, and the practical recommendations.

---

## 2. Step‑by‑step analysis  

### 2.1. Set‑up and notation  

| Symbol | Meaning |
|--------|---------|
| \(R_t\) | YoY S&P 500 return for month \(t\): \(\displaystyle R_t=\frac{P_t-P_{t-12}}{P_{t-12}}\) (or log‑return equivalent). |
| \(R_{t-12}\) | Same return 12 months earlier (lagged predictor). |
| \(C_t\) | Credit‑spread observed at month \(t\). |
| \(I_{t+2}\) | Industrial‑production index 2 months *ahead* of \(t\). |
| \(F_{t+2}\) | Inflation rate 2 months ahead of \(t\). |
| \(D_{t+2}\) | Dummy = 1 if \(F_{t+2}>5\%\), else 0. |
| \(\mathbf{x}_t\) | Row vector of regressors: \([1,\;R_{t-12},\;C_t,\;I_{t+2},\;F_{t+2},\;D_{t+2}]\). |
| \(\beta\) | Column vector of true coefficients \((\beta_0,\beta_1,\dots,\beta_5)'\). |
| \(\varepsilon_t\) | Regression disturbance term. |
| \(T\) | Number of monthly observations available (e.g. 120 months). |

The regression that is actually estimated is  

\[
R_t = \mathbf{x}_t\beta + \varepsilon_t,\qquad t=13,\dots,T .
\]

(The first 12 months cannot be used because the lagged YoY return is undefined.)

### 2.2. Why overlapping creates autocorrelation  

Write the YoY return in terms of **monthly log‑returns** \(r_s = \ln P_s-\ln P_{s-1}\).  
Then  

\[
R_t = \sum_{k=0}^{11} r_{t-k} .
\]

Hence the regression error \(\varepsilon_t\) (which captures everything not explained by the regressors) is a **linear combination of the 12 monthly return shocks** that make up the YoY return.  

If the underlying monthly returns \(\{r_s\}\) are (approximately) serially uncorrelated, the **overlap** between consecutive \(R_t\) and \(R_{t-1}\) induces a **moving‑average** structure of order 11 in the regression residuals:

\[
\varepsilon_t = u_t + u_{t-1} + \dots + u_{t-11},
\]

where \(u_t\) are the “primitive” monthly disturbances.  
Therefore  

\[
\operatorname{Cov}(\varepsilon_t,\varepsilon_{t-h})\neq 0 \quad\text{for}\;h=1,\dots,11 .
\]

The residuals are **serially correlated** (positively, because the same monthly shocks appear in many adjacent YoY observations). This violates OLS assumption *A3* (no autocorrelation) and leads to **incorrect conventional standard errors**.

### 2.3. Consequences for OLS coefficient estimates  

* **Unbiasedness / consistency**  
  * The OLS estimator \(\hat\beta = (X'X)^{-1}X'R\) remains **unbiased** and **consistent** *provided the regressors are strictly exogenous*:  
    \[
    \mathbb{E}[\varepsilon_t \mid \mathbf{x}_t]=0 .
    \]  
  * In the present set‑up the regressors contain **future values** of inflation and industrial production (\(t+2\)). Those are *not* known at time \(t\); they are **predicted** later using separate ARIMA models. As long as the forecasts are treated as *known* numbers **when the regression is estimated**, the exogeneity condition is *violated* (the forecast error is part of \(\varepsilon_t\)). Consequently the OLS point estimates are **biased** unless you explicitly model the forecast error (see §2.6).

* **Efficiency**  
  * Even if exogeneity held, the presence of autocorrelated errors makes the OLS estimator **inefficient** (it does not attain the Gauss‑Markov minimum‑variance bound). A feasible generalized least‑squares (GLS) estimator that accounts for the MA(11) error structure would be more efficient.

* **Standard errors**  
  * The usual OLS formula \(\hat\sigma^2 (X'X)^{-1}\) assumes i.i.d. disturbances. With MA(11) errors it **under‑states** the true sampling variability. Confidence intervals and t‑statistics based on those SEs are unreliable.

### 2.4. How to obtain valid inference  

| Method | What it does | When to use |
|--------|--------------|-------------|
| **Newey‑West (HAC) estimator** | Estimates a heteroskedastic‑and‑autocorrelation‑consistent covariance matrix, allowing you to specify a lag truncation (e.g., 11 or a data‑driven choice). | Quick fix when you are happy with OLS point estimates and just need correct SEs. |
| **Feasible GLS (FGLS)** | First estimate the error autocorrelation (e.g., fit an MA(11) or ARMA model to residuals), then transform the data (pre‑whiten) and run OLS on the transformed variables. | Gives more efficient coefficient estimates *and* correct SEs, but requires a correctly specified error model. |
| **Dynamic regression / ARIMAX** | Model the dependent variable directly as an ARMA process *with* exogenous regressors (including leads). The error term is part of the ARMA structure, so autocorrelation is handled internally. | Preferred when the series is clearly autocorrelated and you need multi‑step forecasts. |
| **State‑space / Kalman filter** | Represent the whole system (ARIMA for each predictor, regression for the response) in a joint state‑space model. Allows optimal forecasting that propagates all sources of uncertainty. | Most rigorous, but more complex to implement. |

**Practical recommendation**:  
- Estimate the regression **by OLS** first.  
- Compute Newey‑West robust standard errors with a lag window of at least 11 (the overlap length).  
- Check the residuals for remaining serial correlation (e.g., Ljung‑Box test). If significant, move to an FGLS or ARIMAX specification.

### 2.5. Forecasting with leads (future regressors)

You intend to produce 1‑, 2‑, 3‑month‑ahead forecasts of \(R_{t+h}\) (h = 1,2,3). The regression uses **future** values of inflation and industrial production, i.e. \(F_{t+2}\) and \(I_{t+2}\). To obtain a forecast at time \(t\) you need forecasts of those leads **at the same horizon** (or longer).  

Key points:

| Issue | Explanation |
|-------|-------------|
| **Exogeneity of leads** | In the regression they are treated as *known* (fixed) at time \(t\). In reality they are *predicted* with error. Ignoring that error makes the forecast variance **too small** and can bias the coefficient estimates (see §2.3). |
| **Propagation of forecast error** | When you feed ARIMA forecasts of \(F_{t+2}\) and \(I_{t+2}\) into the regression, you must **add** their variance to the variance of the regression forecast. In a linear setting, the total forecast variance is  
\[
\operatorname{Var}(\hat R_{t+h}) = \mathbf{x}_{t+h}'\widehat{\operatorname{Var}}(\hat\beta)\mathbf{x}_{t+h} + \sum_{j}\bigl(\partial\hat R_{t+h}/\partial z_j\bigr)^2\operatorname{Var}(\hat z_j),
\]  
where \(z_j\) are the forecasted regressors. |
| **Dynamic vs static forecasts** | If you need a 3‑month‑ahead forecast you could (i) compute a *static* forecast by plugging the 3‑month‑ahead ARIMA forecasts directly into the regression, or (ii) generate a *dynamic* forecast by iterating the regression (use the 1‑month forecast of \(R_{t+1}\) as the lagged predictor for the 2‑month forecast, etc.). The dynamic approach respects the model’s own lag structure and usually yields more realistic prediction intervals. |

If you ignore the forecast‑error component, your confidence intervals will be **over‑optimistic** (too narrow) and may lead to erroneous investment decisions.

### 2.6. A more coherent modelling strategy  

A tidy way to avoid the “future‑regressor” problem is to **re‑specify the model** so that all regressors are **contemporaneous or lagged** (i.e., known at the time of the forecast). For example:

\[
R_t = \alpha + \beta_1 R_{t-12} + \beta_2 C_t + \beta_3 I_{t} + \beta_4 F_{t} + \beta_5 D_{t} + u_t .
\]

You can still capture the predictive power of future macro variables by **including them indirectly** through their own dynamics (e.g., by adding lagged inflation and production terms) or by using a **vector autoregression (VAR)** that jointly models all series.

If you truly believe that *future* macro conditions influence *current* stock‑return expectations (e.g., through forward‑looking investors), then treat the regression as a **conditional expectation model** and estimate it by **instrumental variables (IV)** or **maximum likelihood** that explicitly incorporates the forecast‑error distribution. This is a more advanced approach, rarely needed for practical forecasting.

---

## 3. Final answer – summary of the statistical assessment  

| Question | Answer |
|----------|--------|
| **Is the OLS regression “correct”?** | The *point* estimates are unbiased **only if** the regressors are truly exogenous (they are not, because they include future values that are forecast). Moreover, overlapping YoY returns induce an MA(11) error structure, violating the OLS i.i.d. assumption. |
| **Is it efficient?** | No. With serially correlated errors OLS is *inefficient*; a GLS or ARIMAX estimator would give smaller variance. |
| **Are the usual OLS standard errors valid?** | **No.** They underestimate the true sampling variability. Use Newey‑West (HAC) or feasible GLS to obtain correct inference. |
| **Is the forecasting procedure sound?** | Partially. The idea of feeding ARIMA forecasts of the leads into the regression is acceptable, but you must (i) account for the forecast‑error variance when constructing prediction intervals, and (ii) recognise that the regression coefficients may be biased because the leads are not truly known at forecast time. |
| **Practical recommendation** | 1. Estimate the regression by OLS with HAC (Newey‑West) SEs (lag ≥ 11).<br>2. Test

*Original question: [Time series regression with overlapping data](https://stats.stackexchange.com/questions/8373/time-series-regression-with-overlapping-data) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*
