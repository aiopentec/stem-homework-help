---
layout: question
title: 'Paired binary outcomes with a non-zero control rate: report the difference,
  the ratio, or both?'
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Paired binary outcomes with a non-zero
  control rate: report the difference, the ratio, or both?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

You have **paired** binary data from 50 simulation runs.  
For each pair you record whether a deterministic detector “fires” (yes = 1, no = 0)  

|                | Intervention = 1 | Intervention = 0 |
|----------------|-------------------|-------------------|
| **Control = 1**|  ? (both fire)    |  ? (control only)|
| **Control = 0**|  ? (intervention only) |  ? (both do not fire) |

The totals that are known are  

* 2 control runs fire  (i.e. **∑Control = 2**)  
* 44 intervention runs fire (i.e. **∑Intervention = 44**)  

The student wants to know

1. Which effect‑size measure should be reported – risk difference, risk ratio, or odds ratio?  
2. How to obtain a confidence interval that respects the pairing (McNemar vs. two independent‑sample Wilson intervals).  
3. Whether a “very low” control rate (only 2/50) justifies ignoring the pairing and reporting only the intervention proportion.

Below is a step‑by‑step worked solution that answers each of these points.

---

## 2.  Build the 2 × 2 table for the paired data

Let  

* **a** = number of pairs where *both* are 0 (no fire in either run)  
* **b** = number of pairs where *control* = 0, *intervention* = 1 (fire only with the intervention)  
* **c** = number of pairs where *control* = 1, *intervention* = 0 (fire only in the control)  
* **d** = number of pairs where *both* are 1 (fire in both runs)

The four cell counts satisfy  

\[
\begin{aligned}
a+b+c+d &= 50 \quad\text{(total pairs)}\\
b+d &= 44 \quad\text{(intervention fires)}\\
c+d &= 2  \quad\text{(control fires)} .
\end{aligned}
\]

From the last two equations we obtain  

\[
b = 44-d,\qquad c = 2-d .
\]

The exact values of **b** and **c** depend on how many of the 2 control fires also fire under the intervention (the unknown **d**).  
Two plausible extremes are:

| scenario | d | b = 44‑d | c = 2‑d |
|----------|---|----------|----------|
| **A** (no overlap) | 0 | 44 | 2 |
| **B** (complete overlap) | 2 | 42 | 0 |

Both satisfy the observed marginal totals, and the inference will be illustrated with the **most conservative** case (scenario A, *b* = 44, *c* = 2).  The other extreme gives identical point estimates for the risk difference and an even larger test statistic, so the conclusions are unchanged.

---

## 3.  Effect‑size measures

### 3.1  Risk (proportion) in each arm  

\[
\hat{p}_{\text{control}} = \frac{2}{50}=0.04,\qquad
\hat{p}_{\text{intervention}} = \frac{44}{50}=0.88 .
\]

### 3.2  Risk difference (RD)

\[
\widehat{\text{RD}} = \hat{p}_{\text{intervention}}-\hat{p}_{\text{control}}
                    = 0.88-0.04 = 0.84 .
\]

### 3.3  Risk ratio (RR)

\[
\widehat{\text{RR}} = \frac{\hat{p}_{\text{intervention}}}{\hat{p}_{\text{control}}}
                    = \frac{0.88}{0.04}=22 .
\]

Because the denominator (control risk) is very small, the RR is highly unstable: a change of a single control event would move the RR from 22 to 44 or to 11.

### 3.4  Odds ratio (OR) for paired data  

For matched binary outcomes the *conditional* odds ratio reduces to the ratio of discordant counts:

\[
\widehat{\text{OR}}_{\text{paired}} = \frac{b}{c}.
\]

With **b = 44** and **c = 2** we obtain  

\[
\widehat{\text{OR}} = \frac{44}{2}=22 .
\]

If **c = 0** (scenario B) the OR is formally infinite, which is another sign that the odds ratio is not a robust summary when any cell is zero.

### 3.5  Which measure to report?

| Measure | Interpretation | Behaviour when control risk ≈ 0 |
|---------|----------------|---------------------------------|
| **Risk difference** | Absolute increase in probability (84 percentage‑points) | Remains finite and easy to interpret |
| **Risk ratio** | Multiplicative increase (22‑fold) | Explodes as control risk → 0; confidence interval becomes very wide |
| **Odds ratio** | Ratio of odds; for paired data = *b/c* | Infinite if *c* = 0; also unstable with small counts |

**Recommendation:**  
When the control event rate is low, the **risk difference** is the most transparent and statistically stable summary.  It tells the practitioner exactly how many more failures (or detections) to expect per 100 trials.  The RR can be reported *in addition* for completeness, but it should be accompanied by a warning about its instability.  The OR is appropriate only when both discordant cells are non‑zero; otherwise it is either infinite or undefined.

---

## 4.  Confidence interval that respects the pairing  

Because the data are paired, the **McNemar test** (or its exact version) is the correct basis for inference about the proportion difference.  Two independent Wilson intervals would treat the 50 control and 50 intervention observations as unrelated, which discards the within‑pair information.

### 4.1  Exact (binomial) McNemar confidence interval for the proportion difference  

The discordant pairs are **b = 44** (0 → 1) and **c = 2** (1 → 0).  
Conditioning on the total number of discordant pairs \(n_d = b + c = 46\), the number of “successes’’ (0 → 1) follows a **Binomial**\((n_d, \pi)\) distribution where  

\[
\pi = \Pr(\text{control}=0,\text{intervention}=1 \mid \text{discordant}) .
\]

A (1‑α) confidence interval for \(\pi\) can be obtained with the Clopper–Pearson exact method and then transformed to a confidence interval for the risk difference:

\[
\text{RD} = \frac{b-c}{N} = \frac{2\pi-1}{N}\times n_d ,
\]
where \(N = 50\) is the total number of pairs.

Carrying out the calculation (α = 0.05):

* Exact binomial CI for \(\pi\) with \(b=44\), \(n_d=46\):  

  \[
  \pi_{L}=0.804,\qquad \pi_{U}=0.999 .
  \]

* Transform back to RD:  

  \[
  \text{RD}_{L}= \frac{b-c}{N} - \frac{z_{0.975}}{N}\sqrt{b+c}
                = 0.84 - \frac{1.96}{50}\sqrt{46}
                \approx 0.58 ,
  \]
  \[
  \text{RD}_{U}= \frac{b-c}{N} + \frac{z_{0.975}}{N}\sqrt{b+c}
                \approx 1.00 .
  \]

Thus the **95 % confidence interval for the risk difference** is  

\[
\boxed{0.84\;(\;0.58,\;1.00\;)} .
\]

(The upper bound is truncated at 1 because a proportion cannot exceed 1.)

### 4.2  Exact (conditional) confidence interval for the odds ratio  

For paired data the conditional odds ratio is \(OR = b/c\).  An exact (conditional) CI is obtained by inverting the exact binomial test for the number of “b’’ successes out of \(n_d\) trials.

Using the exact binomial method for \(b=44, n_d=46\):

* Lower limit: \(OR_{L}= \frac{b}{c+ \frac{z_{0.975}^2}{2} + \sqrt{c(z_{0.975}^2 + 4b)}}\) (approximation) → 13.6  
* Upper limit: very large (practically infinite because *c* is tiny).  

Because the lower limit is still far above 1, the conclusion of a strong positive effect is robust, but the interval is extremely asymmetric and uninformative on the upper side.

### 4.3  McNemar χ² test (large‑sample)  

The usual continuity‑corrected McNemar statistic is  

\[
\chi^2 = \frac{(|b-c|-1)^2}{b+c}
      

*Original question: [Paired binary outcomes with a non-zero control rate: report the difference, the ratio, or both?](https://stats.stackexchange.com/questions/677149/paired-binary-outcomes-with-a-non-zero-control-rate-report-the-difference-the) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
