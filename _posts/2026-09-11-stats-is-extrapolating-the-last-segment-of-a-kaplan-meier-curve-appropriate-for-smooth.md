---
layout: question
title: Is extrapolating the last segment of a Kaplan–Meier curve appropriate for smoothed
  survival calibration?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Is extrapolating the last segment
  of a Kaplan–Meier curve appropriate for smoothed survival calibration?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

You have fitted a 60‑month survival model with **rms::orm()** (logistic link) and you are trying to check how well the predicted probabilities match the observed data in a large subgroup (31 557 patients ≥ 65 y).  

You are using  

```r
val.surv(..., method = "smoothkm", eps = 30, msmooth = "raw")
```  

to compute *moving‑window* Kaplan–Meier (KM) estimates of the observed 60‑month survival, and you have discovered that, for a number of windows, the “observed” survival (`1‑incidence`) is either:

* **outside the interval \[0,1\]** (e.g., –0.02 or 1.13), or  
* **non‑finite** (NA or NaN).

You want to know:

1. **Why this happens.**  
2. **Whether the “extrapolation of the last KM segment” that the `smoothkm` method performs is appropriate, or if it should be avoided.**  
3. **What you can do to obtain sensible calibration results.**

---

## 2.  Step‑by‑step explanation  

Below each step is a short R‑style illustration (you can copy‑paste it into a clean R session) followed by the statistical reasoning.

### Step 1 – What `val.surv(..., method = "smoothkm")` does

| Sub‑step | What the code does | Why it matters |
|----------|-------------------|----------------|
| 1a | Sort the data by the **predicted probability** `p_sub`. | The moving windows are defined on the *prediction* axis, not on time. |
| 1b | For each centre `c` of a window (grid of length `eps` = 30 points), collect **all subjects whose predicted probability lies within ±eps/2** of `c`. | This defines the *window* of “similar‑risk” patients. |
| 1c | Within that window, compute a **Kaplan–Meier estimate of the survival function** up to the evaluation time `u = 60` months. | This is the “observed” survival you compare to the model‑predicted survival. |
| 1d | The raw KM curve is **linearly extrapolated** from the last observed event time to the evaluation time `u`. This extrapolation is performed by `smoothkm`. | If the window contains **no events after the last observed failure**, the extrapolated line can go below 0 or above 1. |

The object `v_raw$movstats` contains, for each window, the quantities needed to compute the observed survival at 60 months:

```r
incidence   # number of failures / (risk set at last observed time)
survival_at_60 = 1 - incidence
```

### Step 2 – When does the raw KM estimate become *invalid*?

A KM estimator is undefined (or degenerate) in three common situations:

| Situation | What the data look like | KM result | Effect on `survival_at_60` |
|-----------|------------------------|-----------|---------------------------|
| **A. No subjects in the window** | The predicted‑probability interval is empty (possible when `eps` is small relative to the distribution of `p_sub`). | `NA` (risk set = 0). | `survival_at_60 = NA` → *non‑finite* window. |
| **B. No *events* (deaths) observed in the window** | All subjects are censored before 60 mo, or the last observed failure occurs well before 60 mo. | KM stays at 1 until the last observed time, then the *extrapolation* line is forced to reach the value at time `u`. If the last observed failure is far from `u`, the line can **overshoot** > 1 or < 0. | `survival_at_60` may be > 1 or < 0 → *invalid probability* window. |
| **C. All subjects fail before the first observed time** (rare for survival data) | The KM estimator jumps immediately to 0, then the extrapolation stays at 0. | `survival_at_60 = 0` (valid) – no problem. |

In your output  

```
windows                        201
invalid_probability_windows     54
nonfinite_windows               …
```

roughly **27 % of the windows** fall into case **B** (or possibly **A**), which is why you see survival estimates outside the admissible range.

### Step 3 – Why the linear extrapolation creates values outside \[0,1\]

The `smoothkm` routine (see `?smoothkm`) does the following when the KM curve ends **before** the evaluation time `u`:

1. Compute the KM survival `S(t_last)` at the **last event time** `t_last`.  
2. Draw a straight line from `(t_last, S(t_last))` to `(u, Ŝ(u))`, where `Ŝ(u)` is obtained by **extending the slope** of the KM curve beyond `t_last`.  

If `S(t_last) = 1` (no failures) the slope is zero, so the extrapolated line stays at 1 → *valid*.  
If `S(t_last) < 1` but the **gap** `u – t_last` is large, the line can cross the horizontal axis (or go above 1) because the slope is estimated from a *single* step of the KM curve. The algorithm does **not** enforce the boundary constraints `0 ≤ Ŝ(u) ≤ 1`.

Consequently, the raw “incidence” computed as `1 – Ŝ(u)` can be negative or greater than 1, which is exactly what you observed.

### Step 4 – Is extrapolating the last KM segment appropriate for calibration?

**Short answer:** *No, not for a formal calibration plot.*  

*Reasons*

| Reason | Explanation |
|--------|-------------|
| **Statistical validity** | A Kaplan–Meier estimate is only guaranteed to be a valid survival function **up to the last observed event**. Anything beyond that is an *extrapolation* that does not have the usual non‑parametric guarantees. |
| **Boundary violation** | As shown, linear extrapolation can produce probabilities outside \[0,1\], which makes the calibration curve misleading (the “observed” line may appear above the perfect‑fit line). |
| **Instability in sparse windows** | When a window contains few failures (or none), the KM estimate is driven by a single event, so the extrapolated value is extremely noisy. Calibration is meant to assess systematic bias, not random noise. |
| **Alternative methods exist** | `val.surv` offers other `method` options (`"binomial"` and `"cox"`). The binomial method directly computes the observed proportion of survivors in each window and therefore never exceeds the \[0,1\] limits. |

Hence, for a **reliable calibration plot** you should either:

* **Avoid extrapolation** by ensuring each window contains at least one observed event **before** the evaluation time, **or**
* Use a **different method** (`method = "binomial"` or `"cox"`), or
* Increase the window width `eps` so that each window is sufficiently populated.

### Step 5 – Practical ways to fix the problem  

Below are concrete R code snippets that you can insert after the call to `val.surv`.

#### 5a.  Check how many subjects (and how many events) are in each window

```r
# v_raw$movstats already contains n and nevent (if you ask for them)
w <- as.data.frame(v_raw$movstats)

# Number of subjects in the window
w$n_patients <- w$n

# Number of events that occurred before u = 60 months
w$n_events   <- w$nevent

# Flag windows that are too sparse
w$too_sparse <- w$n_patients < 5 | w$n_events < 1
summary(w$too_sparse)
```

If a sizable proportion are flagged, consider a larger `eps`:

```r
# Try a broader window, e.g., eps = 60 (covers more subjects)
v_raw2 <- rms::val.surv(
  S = S_sub, est.surv = p_sub, u = 60,
  fun = qlogis, method = "smoothkm",
  eps = 60, msmooth = "raw", tunits = "month"
)
```

#### 5b.  Use the *binomial* method (no extrapolation)

```r
v_bin <- rms::val.surv(
  S = S_sub, est.surv = p_sub, u = 60,
  fun = qlogis, method = "binomial",  # <-- change
  eps = 30, msmooth = "raw", tunits = "month"
)

# Now the observed proportion is always between 0 and 1
head(v_bin$movstats$incidence)   # proportion of failures
```

The binomial method computes `incidence = failures / n` directly; it never needs a KM curve, so the boundary problem disappears.

#### 5c.  Trim or merge the problematic windows after the fact

If you must stay with `smoothkm`, you can *post‑process* the raw results:

```r
w$survival_at_60 <- pmax(pmin(w$survival_at_60, 1), 0)   # truncate to [0,1]
# Optionally drop windows with NA
w_clean <- subset(w, is.finite(survival_at_60))
```

**Caution:** Truncation hides the underlying data problem; it is better to avoid the situation altogether.

### Step 6 – Summarize the answer to the original question  

| Question | Answer |
|----------|--------|
| *Is extrapolating the last segment of a Kaplan–Meier curve appropriate for smoothed survival calibration?* | **No** – the extrapolation can produce impossible probabilities and is unstable when windows contain few or no events. Use a method that does not extrapolate (e.g., `"binomial"`), or enlarge the window so that each window has enough observed events. |
| *Why do I get 54 windows with survival < 0 or > 1?* | Those windows contain **no observed failures** before the 60‑month cut‑off; `smoothkm` linearly extends the KM curve beyond the last event, which mathematically can cross the 0 / 1 boundaries. |
| *How can I fix it?* | Increase `eps`, switch `method` to `"binomial"` (or `"cox"`), or drop windows that are empty/too sparse. After fixing, the calibration plot will stay within the unit interval and will reflect genuine model bias rather than artefacts of extrapolation. |

---

## 3.  Final answer (concise)

*Extrapolating the tail of a Kaplan–Meier curve (the `smoothkm` option) is **not appropriate** for a calibration plot because it can generate observed survival estimates outside the admissible range \[0, 1\] when a moving window contains no failures before the evaluation time. The 54 invalid windows you observed are caused by this situation. To obtain a valid calibration you should either (i) increase the window width `eps` so that each window contains at least one event, (ii) switch to `method = "binomial"` (or `"cox"`), or (iii) discard/merge windows that are empty or contain no events. After doing so, the observed probabilities will always lie between 0 and 1 and the calibration curve will be trustworthy.*

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming `smoothkm` works for any window size** | Small `eps` often yields windows with zero events, leading to extrapolation artefacts. | Start with a relatively large `eps` (e.g., 50–100) and inspect the number of events per window. |
| **Ignoring the `n`/`nevent` columns in `movstats`** | You won’t know whether a window is empty or has no failures. | Always check `w$n` and `w$nevent` before plotting. |
| **Truncating probabilities after the fact and still reporting them

*Original question: [Is extrapolating the last segment of a Kaplan–Meier curve appropriate for smoothed survival calibration?](https://stats.stackexchange.com/questions/677143/is-extrapolating-the-last-segment-of-a-kaplan-meier-curve-appropriate-for-smooth) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
