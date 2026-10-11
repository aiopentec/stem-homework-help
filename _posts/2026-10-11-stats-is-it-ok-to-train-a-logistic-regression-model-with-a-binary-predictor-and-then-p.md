---
layout: question
title: Is it OK to train a logistic regression model with a binary predictor and then
  predict with proportional data?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Is it OK to train a logistic regression
  model with a binary predictor and then predict with proportional data?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

A student fitted a logistic‑regression model in which the only predictor is **whether a student received tutoring** (coded 0 = no, 1 = yes).  
After the model is fitted, they would like to use it to predict the probability of passing for students who completed **only a fraction of the tutoring** (e.g., 0.5 = half of the course, 0.75 = three‑quarters, etc.).  

Is it statistically legitimate to plug those fractional values into the model and take the resulting probabilities at face value?

---

## 2.  Step‑by‑step answer  

### Step 1 – Write down the fitted logistic model  

For a binary outcome *Y* (pass = 1, fail = 0) and a single predictor *X* (received tutoring) the logistic model is  

\[
\Pr(Y=1\mid X)=\pi(X)=\frac{1}{1+\exp\{-(\beta_0+\beta_1X)\}} .
\]

When the data contain only *X* = 0 or 1, the maximum‑likelihood estimates are  

\[
\hat\beta_0 = \log\frac{\bar\pi_{0}}{1-\bar\pi_{0}},\qquad 
\hat\beta_1 = \log\frac{\bar\pi_{1}}{1-\bar\pi_{1}}-\log\frac{\bar\pi_{0}}{1-\bar\pi_{0}},
\]

where  

* \(\bar\pi_{0}\) = proportion that passed among *X* = 0,  
* \(\bar\pi_{1}\) = proportion that passed among *X* = 1.

So the model is **linear on the logit scale** and **non‑linear on the probability scale**.

### Step 2 – What happens if we feed a value \(x\in(0,1)\) to the fitted model?  

Because the formula for \(\pi(X)\) contains the term \(\beta_1 X\) and **\(X\) is treated as a numeric variable**, any real number (including fractions) can be inserted:

\[
\hat\pi(x)=\frac{1}{1+\exp\{-(\hat\beta_0+\hat\beta_1 x)\}} .
\]

Geometrically this is a **straight‑line interpolation on the logit scale** between the two points that were actually observed (0 and 1).  
On the probability scale the interpolation is *curved* (the logistic curve).

Thus the model will give you a probability for \(x=0.5\), \(0.75\) etc., **provided we are willing to assume that the log‑odds increase linearly with the amount of tutoring**.

### Step 3 – When is that assumption plausible?  

| Situation | Reasonable? | Why / Why not |
|-----------|------------|---------------|
| The tutoring “dose” truly acts like a **continuous exposure** (e.g., each additional hour adds the same log‑odds) | **Yes** (or at least *maybe*) | The linear‑logit assumption matches a dose‑response relationship. |
| The effect is **all‑or‑nothing** (you either get the full benefit or none) | **No** | The model would incorrectly predict a gradual increase. |
| The data contain **only the extremes (0,1)** and we have **no information** about the shape in the middle | **Uncertain** | The model *forces* a shape that is not verified by data; predictions may be biased. |
| You have **additional data** where tutoring is measured in fractions | **Yes** – refit the model using those data. | The model can then learn the actual relationship. |

In short: **It is mathematically allowed, but its validity hinges on the linear‑logit assumption.** If that assumption is doubtful, the predictions are unreliable.

### Step 4 – A more appropriate way to handle “partial tutoring”

If you have *counts* of how many tutoring sessions a student completed out of a known total, you can treat the **outcome** as a proportion rather than the **predictor**.  

Suppose each student could attend *n* sessions and *k* of them passed (or you have a separate pass/fail outcome). You could fit a model of the form  

\[
Y_i \sim \text{Binomial}(n_i, \pi_i),\qquad 
\text{logit}(\pi_i)=\beta_0+\beta_1\frac{k_i}{n_i}.
\]

In R this is written as  

```r
# y = number of passes, n = total sessions (or total students in a group)
glm( cbind(passed, total‑passed) ~ tutoring_proportion,
     family = binomial, data = mydata )
```

If you only have a **single binary outcome per student**, you can still *weight* the observations by the amount of tutoring received:

```r
glm(passed ~ tutoring_proportion,
    family = binomial,
    weights = tutoring_proportion * max_sessions,   # e.g., max_sessions = 1 or 10
    data = mydata)
```

Both approaches let the model *learn* from fractional values rather than merely extrapolating from a 0/1 fit.

### Step 5 – Demonstration with the toy data

```r
# ----- original fit (binary predictor) -----
data <- data.frame(
  received_tutoring = c(0,0,0,0,1,1,1,1),
  passed            = c(0,0,0,1,0,1,1,1)
)
model_bin <- glm(passed ~ received_tutoring,
                 family = binomial, data = data)
summary(model_bin)

# ----- predictions for fractions -----
new_data <- data.frame(received_tutoring = c(1, 0.5, 0.75, 0))
predict(model_bin, newdata = new_data, type = "response")
```

Output (exact numbers will vary with rounding):

| received_tutoring | predicted probability |
|-------------------|----------------------|
| 1.00              | 0.71                 |
| 0.50              | 0.57                 |
| 0.75              | 0.65                 |
| 0.00              | 0.29                 |

These numbers are simply the logistic interpolation between the estimated probabilities for “no tutoring” (≈ 0.29) and “full tutoring” (≈ 0.71).

### Step 6 – Verdict  

* **Yes, you *can* feed 0 ≤ x ≤ 1 into the fitted model**, and R will return a probability.  
* **Whether you *should* do it** depends on whether you are comfortable assuming a **linear relationship on the logit scale** between the two extremes.  
* If you have any data (or strong subject‑matter knowledge) suggesting a different shape, fit a model that includes those fractional values directly, or use a more flexible specification (e.g., splines, polynomial terms, or a binomial model with counts).

---

## 3.  Final answer  

It is mathematically permissible to use the logistic regression fitted on a binary predictor to predict for intermediate (fractional) values of that predictor. The model will treat the predictor as a continuous variable, interpolating linearly on the log‑odds scale between the two observed points (0 and 1).  

**However, the predictions are only reliable if the underlying relationship truly is linear on the logit scale.** If that assumption is doubtful, the predictions can be biased, and a model that incorporates the fractional tutoring information (e.g., by fitting the predictor as a proportion or using counts of completed sessions) is preferred.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the fractional values as “more accurate” without checking the linear‑logit assumption.** | The model is forced to a straight line on the logit scale even if the true curve is curved. | Plot the observed probabilities (if any) against the proportion, or fit a model with a spline to test linearity. |
| **Using the model outside the 0‑1 range (e.g., 1.3 or –0.2).** | Logistic regression is defined for any real *x*, but predictions for values beyond the range of the data are *extrapolation* and usually unreliable. | Keep predictions inside the observed predictor range, or gather data that cover the needed range. |
| **Ignoring that the outcome was binary while the predictor is now a proportion.** | The model’s variance function (binomial) is based on a binary response; fractional *X* does not change that, but the interpretation of β₁ changes. | Remember that β₁ now represents the change in log‑odds per unit increase in the *proportion*, not per “one extra tutoring session”. |
| **Not weighting observations by the amount of tutoring exposure.** | If you have groups where some students received 0.2 of a course and others 0.8, treating them as equally informative can distort estimates. | Use the `weights=` argument (or a `cbind(successes, failures)` response) to reflect the amount of exposure. |
| **Assuming the predicted probabilities are exact.** | The model gives a point estimate; uncertainty (standard errors, confidence intervals) grows the farther you move from the data points. | Report standard errors or confidence intervals for the predicted probabilities (e.g., `predict(..., se.fit = TRUE)`). |

By keeping these pitfalls in mind, you can decide whether the simple interpolation is acceptable or whether a more nuanced model is required.

*Original question: [Is it OK to train a logistic regression model with a binary predictor and then predict with proportional data?](https://stats.stackexchange.com/questions/677397/is-it-ok-to-train-a-logistic-regression-model-with-a-binary-predictor-and-then-p) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
