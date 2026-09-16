---
layout: question
title: Is Linear LIME&#39;s model only valid for reasonably close points on the prediction
  model?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Is Linear LIME&#39;s model only valid
  for reasonably close points on the prediction model?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. Restatement of the question (plain language)

The student is asking:

* In the original LIME paper a *local* linear model is fit to a black‑box predictor.  
* The linear model often uses binary “on/off’’ features (each \(x_i\in\{0,1\}\)).  
* Sometimes a value of **0** does not correspond to a real, interpretable state of the original variable (e.g., “salary = 0’’ may never occur).  

**What the student wants to know**

1. Does the linear model that LIME learns only make sense for points that are *close* to the instance we are trying to explain?  
2. If a binary feature is set to 0 merely because LIME turned the feature “off”, does that 0 have any meaning, or is the explanation meaningless?  

---

## 2. Step‑by‑step answer

Below we go through the whole LIME pipeline, point out where *closeness* enters, and explain how binary perturbations are interpreted.

### Step 1 – What LIME is trying to approximate

For a particular instance \(\mathbf{x}^{(0)}\) we want a simple model \(g\) (usually linear) that mimics the black‑box predictor \(f\) **in the neighbourhood of \(\mathbf{x}^{(0)}\)** :

\[
g(\mathbf{z}) \approx f(\mathbf{z})\qquad\text{for }\mathbf{z}\text{ near }\mathbf{x}^{(0)} .
\]

The word *local* is crucial: the approximation is **not** required to be good far away from \(\mathbf{x}^{(0)}\).

### Step 2 – Sampling perturbed points

LIME creates a set of synthetic points \(\{ \mathbf{z}^{(k)}\}_{k=1}^{K}\) by perturbing the original instance.  
Two common strategies are:

| Feature type | Perturbation method | Resulting binary variable |
|--------------|--------------------|---------------------------|
| Categorical / text | “turn the word on/off”, “replace a category by a dummy” | \(z_i=1\) if the original word/category is present, \(z_i=0\) otherwise |
| Numerical | Sample from a **univariate** distribution (e.g., normal) **and then discretise** (e.g., “< 10 → 0, ≥ 10 → 1”) | Same binary encoding |

Thus the binary value **does not need to be a natural state of the original variable**; it is merely a *perturbation flag* that tells us whether the feature was kept as in the original instance (1) or replaced by some *reference* value (0).

### Step 3 – Defining the reference value for “0”

When a feature is turned *off* (set to 0) LIME replaces it by a *baseline* that is **chosen by the user or by the perturbation scheme**:

* **Missing/Masked baseline** – for images a gray patch; for tabular data a column‑wise mean or median; for text an empty string.
* **Sampled baseline** – draw a value from the marginal distribution of that feature *independently* of the rest of the instance.

Because the baseline is part of the *sampling* process, the coefficient of a binary feature in the linear model measures **the change in the prediction when we replace the original value by that baseline**, *averaged over all other perturbed features*.  

If a baseline such as “salary = 0” is impossible in the real data, LIME will **not** use it unless the user explicitly tells it to. A typical choice is “salary = median(salary)”, or “salary is drawn from the empirical distribution while other features stay as in \(\mathbf{x}^{(0)}\)”.

### Step 4 – Weighting by distance (the kernel \(\pi_{\mathbf{x}^{(0)}}(\mathbf{z})\))

Each synthetic point receives a weight

\[
\pi_{\mathbf{x}^{(0)}}(\mathbf{z}) = \exp\!\Bigl(-\frac{D(\mathbf{x}^{(0)},\mathbf{z})^2}{\sigma^2}\Bigr),
\]

where \(D\) is a distance (often Euclidean on a normalized space) and \(\sigma\) controls the width of the neighbourhood.

* **Points that are far away have exponentially small weight** → they contribute almost nothing to the fitted linear model.
* Consequently, **the linear model is only trustworthy inside the region where \(\pi\) is non‑negligible**. This is the formal meaning of “reasonably close”.

### Step 5 – Fitting the linear model

We solve a weighted regression:

\[
\hat{\mathbf{w}} = \arg\min_{\mathbf{w}} \sum_{k=1}^{K}\pi_{\mathbf{x}^{(0)}}(\mathbf{z}^{(k)})\,
\bigl[f(\mathbf{z}^{(k)}) - \mathbf{w}^{\top}\mathbf{z}^{(k)}\bigr]^2 + \Omega(\mathbf{w}),
\]

where \(\Omega\) is a sparsity penalty (e.g., L1).  
Only those \(\mathbf{z}^{(k)}\) that are *close* (large \(\pi\)) affect \(\hat{\mathbf{w}}\).

### Step 6 – Interpreting the coefficients

* The coefficient \( \hat{w}_j\) tells us **how much the prediction changes on average when we toggle feature \(j\) from its baseline (0) to the original value (1), while all other features are allowed to vary in the neighbourhood**.
* It **does not claim** that the same coefficient would explain the model far away from \(\mathbf{x}^{(0)}\).

### Step 7 – Answering the two sub‑questions

| Question | Answer |
|----------|--------|
| **Is the linear LIME model only valid for “reasonably close” points?** | **Yes.** The kernel weighting explicitly restricts the fit to a local neighbourhood. Points far from the instance receive (practically) zero weight and do not influence the coefficients. |
| **What does a binary “0” mean when the original feature has no natural zero?** | The “0” is **not an intrinsic property of the original variable**; it is the *perturbation flag* that says “the feature has been replaced by the baseline used during sampling”. The meaning of the coefficient is therefore “the effect of swapping the original value for that baseline, averaged locally”. If the chosen baseline is unrealistic, the explanation may be hard to interpret, but the method itself remains mathematically sound. One can change the baseline to a more sensible reference (e.g., mean, median, or a sampled value) to obtain a more meaningful interpretation. |

---

## 3. Final answer (concise statement)

- **Locality:** Linear LIME’s surrogate model is *by definition* a local approximation; it is trustworthy only for points that lie within the neighbourhood determined by the kernel \(\pi_{\mathbf{x}}(\cdot)\). Far‑away points have negligible influence and the linear model should not be used to extrapolate there.

- **Interpretation of binary “0”:** In LIME the binary encoding is a *perturbation device*. A value of 0 means “the feature has been replaced by the baseline chosen for the sampling procedure”, not that the original variable actually takes the value 0. The coefficient of a binary feature therefore quantifies the change in the black‑box prediction when we switch the feature from that baseline to its original value, **conditioned on the other features staying close to the instance we are explaining**.

---

## 4. Common mistakes when using LIME

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the linear explanation holds globally.** | The surrogate is fitted with a locality kernel; far‑away points are essentially ignored. | Remember that the explanation is only valid “near” the instance. Report the kernel width \(\sigma\) or the effective neighbourhood. |
| **Interpreting a coefficient as “the effect of setting the feature to 0”.** | The 0 value is a *reference* (baseline) that may not correspond to any real state. | Clarify in the explanation what baseline was used (mean, median, sampled value, etc.). |
| **Choosing a meaningless baseline (e.g., salary = 0) and then trusting the numbers.** | The model may predict wildly for impossible inputs; the coefficient will reflect that artefact. | Pick a baseline that is plausible for the domain, or let LIME sample the baseline from the empirical marginal distribution. |
| **Using a very large kernel width so that “local” becomes “global”.** | The surrogate may become a poor fit to the highly non‑linear black box, and coefficients become unstable. | Tune the kernel width (or the number of samples) and verify the fidelity metric (e.g., R²) reported by LIME. |
| **Ignoring the sparsity regularisation (\(\Omega\)).** | Without it, all features get a coefficient, making the explanation noisy and hard to read. | Use the default L1 regulariser or set the desired number of features to display (`num_features` argument). |

---

*Original question: [Is Linear LIME&#39;s model only valid for reasonably close points on the prediction model?](https://stats.stackexchange.com/questions/677184/is-linear-limes-model-only-valid-for-reasonably-close-points-on-the-prediction) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
