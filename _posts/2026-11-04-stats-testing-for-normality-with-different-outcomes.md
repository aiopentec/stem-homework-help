---
layout: question
title: Testing for normality with different outcomes
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Testing for normality with different
  outcomes'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. Restate What's Being Asked in Plain Language

A student has a dataset with a small sample size ($n = 20$) and is testing it for normality using multiple goodness-of-fit tests. They got a confusing result: the Lilliefors test says the data is *not* normally distributed (significant result), while other tests, such as the Shapiro-Wilk test, say it *is* normally distributed (non-significant result). 

The student knows that the Shapiro-Wilk test is generally very powerful for small sample sizes like $n = 20$, so they want to know:
1. What could cause this specific contradiction between the Lilliefors and Shapiro-Wilk tests?
2. What is the best test to use for checking normality when $n = 20$?

---

## 2. Step-by-Step Solution

### Step A: Clarify the relationship between the Kolmogorov-Smirnov and Lilliefors tests
The student notes that a discrepancy with the Kolmogorov-Smirnov (K-S) test "seems logical." It is important to clarify *why* this happens:
* **Standard K-S Test:** This test requires you to fully specify the parameters of the hypothesized distribution (mean $\mu$ and standard deviation $\sigma$) *before* looking at the data. If you estimate $\mu$ and $\sigma$ from the sample and then use the standard K-S test, the test becomes **extremely conservative**. This means it is very unlikely to reject the null hypothesis of normality, even if the data is non-normal.
* **Lilliefors Test:** This is simply a modification of the Kolmogorov-Smirnov test specifically designed for the case where the mean and variance are *estimated* from the sample data. Therefore, the Lilliefors test corrects for the conservatism of the standard K-S test and has appropriate critical values. If a student runs both, the Lilliefors test is the correct one to trust over the standard K-S test.

### Step B: Address the discrepancy between Lilliefors and Shapiro-Wilk ($n = 20$)
Now, why might the **Lilliefors test** be significant (rejecting normality) while the **Shapiro-Wilk test** is non-significant (failing to reject normality) for $n = 20$?

1. **Different Test Mechanics (Empirical CDF vs. Correlation of Ordered Values):**
   * The **Lilliefors/K-S test** focuses on the *maximum vertical distance* between the empirical cumulative distribution function (ECDF) and the cumulative distribution function (CDF) of the normal distribution. It is often most sensitive to discrepancies around the *center* of the distribution (the median/mean).
   * The **Shapiro-Wilk test** is based on the regression of the ordered sample values against the expected normal scores (essentially testing if the ordered points fall along a straight line in a Q-Q plot). It is notoriously sensitive to departures from normality in the **tails** (skewness and heavy/light tails).

2. **Power and Significance Level ($n = 20$):**
   * At $n = 20$, both tests have moderate power, but they behave differently. A "non-significant" Shapiro-Wilk test ($p > 0.05$) simply means there is *not enough evidence* to reject normality at the chosen significance level ($\alpha$). It does *not* prove the data is normal.
   * If the non-normality in the dataset stems from a sharp peak, a bimodal tendency near the center, or a specific step in the middle of the distribution—rather than extreme skewness in the tails—the Lilliefors test may detect it as a significant deviation of the maximum vertical gap, whereas Shapiro-Wilk might miss it.

### Step C: Determine the best approach/test for normality with $n = 20$
When $n = 20$, formal hypothesis tests for normality often struggle: they have low power to detect mild non-normality (Type II error), and sometimes high sensitivity to trivial quirks. 

1. **The Gold Standard for Small Samples ($n = 20$):**
   * Statisticians widely agree that the **Shapiro-Wilk test** is the most powerful and reliable formal test for normality when sample sizes are small ($n < 50$). 
   * However, *relying solely on a p-value* from any normality test is discouraged.

2. **Visual Inspection (The Essential Companion):**
   * With $n = 20$, formal tests can be misleading. The best approach combines the Shapiro-Wilk test with graphical diagnostics:
     * **Normal Q-Q Plot:** Look to see if the points closely follow the 45-degree reference line.
     * **Histogram or Boxplot:** Check for extreme skewness or severe outliers.

---

## 3. Final Answer

1. **Cause of the Discrepancy:** The conflict arises because tests for normality evaluate different aspects of the distribution. The Lilliefors test measures the maximum vertical distance between cumulative distributions (often sensitive to shifts near the center), while the Shapiro-Wilk test evaluates the correlation of ordered values (primarily sensitive to tail behavior like skewness). Furthermore, a "non-significant" Shapiro-Wilk result is not proof of normality; it simply means it failed to reach the threshold for rejection at $\alpha = 0.05$.
2. **Best Approach for $n = 20$:** The **Shapiro-Wilk test** is the best and most powerful formal statistical test for normality at this sample size. However, because formal tests have limitations with small samples, the definitive best approach is to combine the **Shapiro-Wilk test** with a **Normal Q-Q plot** to visually inspect the data.

---

## 4. Common Mistakes

* **Mistake 1: Treating a non-significant test as proof of normality.** Accepting the null hypothesis ($p > 0.05$) does not prove the data is normally distributed; it only means there is insufficient evidence to say it is *not* normal.
* **Mistake 2: Using the standard Kolmogorov-Smirnov test when parameters are estimated.** Running a standard K-S test after estimating the mean and standard deviation from the sample yields invalid, overly conservative p-values. You must use the Lilliefors correction (or Shapiro-Wilk) instead.
* **Mistake 3: Relying exclusively on p-values.** Ignoring visual diagnostics like Q-Q plots, especially with small sample sizes ($n = 20$), often leads to misinterpreting borderline test results.

*Original question: [Testing for normality with different outcomes](https://stats.stackexchange.com/questions/677658/testing-for-normality-with-different-outcomes) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
