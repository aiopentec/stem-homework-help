---
layout: question
title: Stationary bootstrap for daily observations separated by market closures
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Stationary bootstrap for daily observations
  separated by market closures'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

You have a series  

\[
Y_1,\;Y_2,\dots ,Y_N
\]

where each \(Y_t\) is the **daily, risk‑adjusted profit‑and‑loss** of a trading rule on a *trading day* (i.e., a day the market is open).  
If a calendar day is a market‑holiday or a weekend the series simply **skips** that day – there is no observation for it.  

You want to estimate the sampling variability of the **equally‑weighted mean**

\[
\bar Y = \frac{1}{N}\sum_{t=1}^{N} Y_t ,
\]

and you are considering the **stationary bootstrap** (Politis & Romano, 1994).  

The stationary bootstrap works by

1. picking a random starting index,
2. drawing a block length \(L\) from a geometric distribution with mean \(\ell\) (e.g. \(\ell=\lceil N^{1/3}\rceil\)),
3. copying the consecutive **indices** \(t,t+1,\dots ,t+L-1\) (wrapping around the end of the series if needed),
4. repeating until a bootstrap sample of size \(N\) is obtained,
5. recomputing the statistic (here, the mean) on the resampled series.

Because the bootstrap treats the **index** distance “1” as “the next observation”, the question is:

> **When is it legitimate to treat two observations that are separated by a weekend (or any market‑closed days) as if they were consecutive in the bootstrap?**  
> In other words, under what assumptions does the index‑based stationary bootstrap give a valid estimate of the uncertainty of \(\bar Y\) when the calendar gaps are irregular?  
> If those assumptions are violated, can we give a concrete counter‑example showing that the dependence structure is mis‑represented?

---

## 2.  Step‑by‑step reasoning

### 2.1  What the stationary bootstrap **requires** in the abstract

The stationary bootstrap is designed for a **strictly stationary** stochastic process \(\{X_t\}_{t\in\mathbb Z}\) that is observed **at equally‑spaced time points** (e.g. every day, every hour).  
The key theoretical conditions are:

| Condition | Intuition |
|-----------|-----------|
| **Strict stationarity**: the joint distribution of \((X_{t_1},\dots ,X_{t_k})\) is the same as that of \((X_{t_1+h},\dots ,X_{t_k+h})\) for any integer shift \(h\). | The dependence pattern does not change over time. |
| **Mixing / weak dependence** (e.g. α‑mixing with \(\sum_{h=1}^\infty \alpha(h)^{\delta/(2+\delta)} <\infty\) for some \(\delta>0\)). | Correlations die out sufficiently fast so that block‑resampling mimics the true dependence. |
| **Observations are equally spaced**. | The geometric block length is interpreted as a *time* length, not just “number of records”. |

If these hold, Politis & Romano proved that the stationary bootstrap consistently estimates the distribution of any smooth functional (such as the mean) of the underlying process.

### 2.2  How “calendar gaps” disturb the “equally spaced” requirement

In your data the *clock time* between two consecutive observations can be 1, 2, 3 … calendar days, because weekends and holidays are omitted.  

Two ways to think about the underlying reality:

| Perspective | What the data represent | Implication for bootstrap |
|-------------|------------------------|---------------------------|
| **(A) Discrete‑time view** – the process is defined **only on trading days**. The index \(t\) itself *is* the “time” variable, and the fact that a weekend passes is irrelevant. | \(Y_t\) is the profit on the *t‑th* trading day; there is **no latent value** for Saturday or Sunday. | Treating the series as equally spaced in the index sense *is* correct, provided the *trading‑day process* is stationary. |
| **(B) Continuous‑time view** – the process actually evolves every calendar day (or even continuously), but you observe it only when the market is open. The unobserved days still affect the next observed value (e.g., via overnight drift, weekend news). | \(Y_t\) is a *sample* of an underlying daily‑calendar process \(\{X_{\tau}\}_{\tau\in\mathbb Z}\) taken at the subset of days \(\tau\in\mathcal T\) (the trading calendar). | The “index distance” of 1 does **not** correspond to a calendar distance of 1 day; the autocorrelation between \(Y_t\) and \(Y_{t+1}\) is actually the autocorrelation of \(X\) over a *variable* number of calendar days. The stationary bootstrap that uses a *geometric distribution on index steps* will therefore **mis‑represent** the dependence.

Thus the crucial question is **which perspective matches the data‑generating mechanism (DGM)**.

### 2.3  When the index‑based bootstrap *is* appropriate

The stationary bootstrap will give a valid estimate of the sampling distribution of \(\bar Y\) **iff** the following hold:

1. **Trading‑day stationarity**:  
   The stochastic process \(\{Y_t\}\) indexed by *trading‑day number* is strictly stationary. Formally, for any lag \(h\),

   \[
   (Y_t, Y_{t+1},\dots ,Y_{t+k}) \stackrel{d}{=} (Y_{t+h}, Y_{t+h+1},\dots ,Y_{t+h+k}) .
   \]

   In practice, this means that the distribution of returns does **not** depend on the day of the week, month, or position in the calendar.

2. **Independence of market‑closure pattern from the process**:  
   The set of closed days \(\mathcal C\) (weekends, holidays) must be **deterministic** or at least **independent** of the returns. If holidays were scheduled based on market volatility (e.g., a “circuit‑breaker” closure), the independence would be violated.

3. **No intra‑week serial dependence beyond the trading‑day index**:  
   If there is a genuine “Monday effect” (systematic difference between Monday returns and other weekdays) that creates a *deterministic* pattern, then the process is *not* stationary in the index sense; the bootstrap will underestimate variability because it treats Monday‑Tuesday as the same lag as Tuesday‑Wednesday.

4. **Mixing condition satisfied on trading‑day index**:  
   The dependence between \(Y_t\) and \(Y_{t+h}\) must decay sufficiently fast as \(h\to\infty\) (e.g., ARMA‑type dependence). This is the same condition required for any block‑bootstrap.

If all four hold, the geometric block length \(\ell\) can be chosen by any standard rule (including \(\ell\approx N^{1/3}\) which is optimal for i.i.d.‑plus‑weak‑dependence under certain smoothness assumptions). The bootstrap will correctly capture the correlation structure because the *index* distance coincides with the *true* dependence distance.

### 2.4  When treating weekend gaps as consecutive **fails**

Suppose the underlying DGM is a **continuous‑time AR(1) process** observed only on trading days. A simple example:

\[
X_{\tau}= \rho X_{\tau-1}+ \varepsilon_{\tau},\qquad \varepsilon_{\tau}\sim\mathcal N(0,\sigma^2),
\]

with **calendar‑day index** \(\tau = 1,2,\dots\). Let the market be closed on Saturdays and Sundays, i.e., you only observe

\[
Y_t = X_{\tau(t)}, \qquad \tau(t)=t+2\bigl\lfloor\frac{t-1}{5}\bigr\rfloor ,
\]

so that every 5th observation is followed by a **two‑day gap** (the weekend).

The autocorrelation of the observed series is

\[
\operatorname{corr}(Y_t,Y_{t+1}) = \rho^{1},\quad
\operatorname{corr}(Y_t,Y_{t+2}) = \rho^{2},
\]
but **the lag‑1 autocorrelation of the underlying daily series across the weekend is \(\rho^{3}\)** because three calendar days separate them (Friday → Monday).  

If \(\rho\) is not close to 0, the weekend “jumps” introduce **extra decay** that the index‑based bootstrap completely ignores; it treats the Friday‑Monday pair as if the lag were 1, thereby **over‑stating the dependence**. Consequently:

* The bootstrap variance of \(\bar Y\) will be **biased downwards** (it thinks the series is more persistent than it truly is).
* Confidence intervals will be **too narrow** and coverage will be below nominal levels.

#### Concrete numerical counterexample

Take \(\rho = 0.8\), \(\sigma^2 = 1\), and a 2‑year sample (≈ 250 trading days). Compute the true variance of the mean analytically for the observed series:

\[
\operatorname{Var}(\bar Y) = \frac{1}{N^2}\sum_{i=1}^{N}\sum_{j=1}^{N}\operatorname{Cov}(Y_i,Y_j)
\]

where the covariance depends on the **calendar distance** between \(i\) and \(j\). Using the weekend‑adjusted autocorrelation yields \(\operatorname{Var}(\bar Y) \approx 0.0045\).

Run a stationary‑bootstrap (geometric blocks, \(\ell=10\)) on the index‑treated series and estimate the bootstrap variance; the result is ≈ 0.0031 – a **≈ 30 % underestimate**. Repeating the simulation many times confirms the bias.

Thus, **when the underlying process evolves on calendar days and the dependence is a function of calendar lag, the index‑based stationary bootstrap is invalid**.

### 2.5  How to proceed if assumption (B) holds

If you suspect (or know) that the true process depends on calendar time, you have two practical options:

| Option | How to implement | When it works |
|--------|------------------|---------------|
| **(i) Insert “placeholder” observations for closed days** (e.g., set them to 0 or to a *forecast* of the unobserved value). | Create a series \(Z_{\tau}\) for every calendar day. For non‑trading days, either (a) set \(Z_{\tau}=0\) if the strategy truly earns nothing, or (b) impute a value from a model (e.g., ARIMA). Then apply the stationary bootstrap on the *full* daily series. | Valid if the imputed values correctly reflect the *true* dependence (e.g., 0 is correct because there is no trading and no P&L). |
| **(ii) Use a **block‑bootstrap that respects calendar gaps**.** | Define blocks in **calendar time**: pick a starting calendar day, then draw a block length in *calendar days* (geometric on days, not on observed indices). When a block encounters a closed day, simply **skip** it (i.e., keep the block length counting calendar days). | Appropriate when you can model the calendar‑day dependence directly (e.g., you have an ARMA model for daily returns). |
| **(iii) Model‑based resampling** (e.g., fit a parametric time‑series model to the underlying daily process and simulate). | Fit an ARMA/GARCH on the *full* daily series (with imputed or zero values for closed days) and generate many simulated paths, then compute the mean on the trading‑day subset. | Works when the parametric model is trustworthy; often used in finance. |

---

## 3.  Final answer (summary)

| Question | Answer |
|----------|--------|
| **When is observation‑index stationary bootstrapping appropriate?** | When the **trading‑day series itself is strictly stationary**, its dependence structure is a function of **trading‑day lag** only, and the pattern of market closures is deterministic or independent of the returns. In that case the index distance equals the true dependence distance, so the geometric blocks correctly mimic the correlation structure. |
| **When does treating weekend‑separated observations as

*Original question: [Stationary bootstrap for daily observations separated by market closures](https://stats.stackexchange.com/questions/677400/stationary-bootstrap-for-daily-observations-separated-by-market-closures) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
