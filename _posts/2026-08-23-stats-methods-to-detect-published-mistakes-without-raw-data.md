---
layout: post
title: Methods to detect published mistakes without raw data?
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. Restate What's Being Asked in Plain Language

The student is looking for statistical techniques, heuristics, or consistency-checking methods that can be applied to published academic papers to detect errors, anomalies, or potential fabrication—**specifically without having access to the original raw data**. 

They already mentioned:
*   **GRIM** (Granularity-Related Inconsistency of Means)
*   **Benford’s Law**

They want to know what *other* similar statistical tools or methods exist that allow researchers to audit published summary statistics (like means, standard deviations, test statistics, and $p$-values) simply by reading the paper.

---

### 2. Show Every Step: A Catalog of Methods to Detect Published Mistakes Without Raw Data

To detect reporting errors, statistical impossibilities, or anomalies using only published summary statistics, researchers use a toolkit of validation methods. Here is a step-by-step breakdown of the major techniques available in meta-science and data auditing:

#### Step A: Consistency Tests for Summary Statistics
These tests check whether the numbers reported in a paper mathematically fit together. If a paper reports a mean, sample size, and standard deviation, certain mathematical bounds must be respected.

1.  **GRIM (Granularity-Related Inconsistency of Means):**
    *   *What it checks:* Whether a reported mean is mathematically possible given the sample size and the scale of the variable (e.g., Likert scales with whole integers).
    *   *How it works:* If you have a sample size of $N = 10$ on a 1-to-5 scale, the sum of all scores must be an integer. Therefore, the mean multiplied by $N$ must equal a whole number. If a paper reports a mean of $2.43$ for $N=10$, $2.43 \times 10 = 24.3$, which is impossible because individual integer responses cannot sum to a decimal.

2.  **DEBIT (Data Error Detection in Bivalent Totals):**
    *   *What it checks:* Similar to GRIM, but specifically designed for percentages, proportions, and dichotomous data (e.g., yes/no, success/failure).
    *   *How it works:* It tests whether the reported percentages, sample sizes, and cell counts are mathematically compatible with a binomial distribution.

3.  **GRIMMER (Granularity-Related Inconsistency of Means, Standard Deviations, and Error Ranges):**
    *   *What it checks:* An extension of GRIM that tests whether the reported standard deviation (SD) is mathematically consistent with the sample size and mean.
    *   *How it works:* It evaluates whether the variance of a set of discrete values is capable of producing the exact reported standard deviation for a given $N$.

#### Step B: $p$-Value and Test Statistic Re-computation
These methods check the internal consistency of hypothesis tests (t-tests, ANOVAs, correlations, chi-square tests).

4.  **STATCHECK:**
    *   *What it checks:* Inconsistencies between reported test statistics (e.g., $t$-value, $F$-value) and their corresponding $p$-values.
    *   *How it works:* STATCHECK is an R package/algorithm that scans PDF texts for APA-formatted statistical results (e.g., *t*(45) = 2.31, *p* = .02). It re-calculates the exact $p$-value from the test statistic and degrees of freedom. If the reported $p$-value doesn't match the calculated one (especially if a non-significant result is misreported as significant), it flags an error.

5.  **$p$-Curve and $p$-Hacking Detection:**
    *   *What it checks:* The distribution of $p$-values just below .05 to detect selective reporting or data dredging.
    *   *How it works:* Under the null hypothesis, $p$-values are uniformly distributed. Under a true effect, there should be many low $p$-values ($.001$, $.002$). If a paper or body of literature has an implausibly high spike of $p$-values just under .05 (e.g., clustered heavily around .041 to .049), it suggests $p$-hacking or questionable research practices.

#### Step C: Distributional and Numerical Auditing
These methods analyze patterns across large sets of numbers, tables, or entire papers.

6.  **Benford’s Law (Already noted by student):**
    *   *What it checks:* The natural frequency of leading digits in naturally occurring numerical data.
    *   *How it works:* In many real-world datasets, the number 1 is the leading digit roughly 30.1% of the time, while 9 is the leading digit only 4.6% of the time. Applied to reported descriptive statistics, regression coefficients, or even chi-square values across a paper, significant deviations can indicate fabricated or manipulated numbers.

7.  **CIMT (Check for Internal Consistency and Mathematical Transitivity):**
    *   *What it checks:* Basic algebraic identities within tables and text.
    *   *How it works:* Ensuring that reported totals equal the sum of their parts, that correlation matrices are positive semi-definite, and that degrees of freedom align perfectly with the stated sample sizes and model parameters.

8.  **The "Too-Good-to-Be-True" Upper Bound Checks (e.g., impossibly high correlations):**
    *   *What it checks:* Perfect or near-perfect statistical outputs that defy real-world noise.
    *   *How it works:* In psychology and the social sciences, true correlations above .85 or .90 between distinct psychological constructs are exceedingly rare. Finding numerous correlation coefficients, effect sizes, or test statistics that are identical across multiple studies or subgroups can indicate copying/pasting errors or data fabrication.

---

### 3. Final Answer

To detect mistakes, errors, or potential fraud in published papers without raw data, researchers use a suite of validation techniques categorized into three main groups:

1.  **Granularity & Discrete Math Tests:** **GRIM**, **DEBIT**, and **GRIMMER**—which test whether means, standard deviations, and percentages are mathematically possible given the sample size and integer constraints of the scale.
2.  **Test Statistic Re-calculation:** **STATCHECK**—an automated tool that recalculates $p$-values from reported test statistics and degrees of freedom to catch typographical or reporting errors.
3.  **Distributional & Pattern Analysis:** **Benford’s Law** (for leading digits), **$p$-curve analysis** (to spot selective reporting clustering around $p = .05$), and checks for mathematically impossible correlation matrices or overly uniform/perfect summary statistics.

---

### 4. Common Mistakes

*   **Assuming every flagged error is fraud:** Tools like GRIM and STATCHECK frequently catch benign typographical errors (e.g., a typo where $p = .32$ is mistyped as $p = .23$, or a misplaced decimal point). An anomaly indicates a *reporting inconsistency*, not automatically intentional misconduct.
*   **Applying discrete tests to continuous data:** The GRIM test only works when the underlying data is discrete (e.g., whole numbers on a Likert scale or count data). Applying it to variables that are genuinely continuous averages of multiple items can lead to false positives if granular item-level constraints are misunderstood.
*   **Ignoring rounding conventions:** Authors often round means and standard deviations to two decimal places before reporting them. Good error-detection protocols must account for rounding bounds (e.g., testing whether a rounded mean *could* have originated from valid raw data prior to rounding).

*Original question: [Methods to detect published mistakes without raw data?](https://stats.stackexchange.com/questions/309495/methods-to-detect-published-mistakes-without-raw-data) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
