---
layout: question
title: 'Post-hoc tests after Kruskal-Wallis: Multiple testing adjustments'
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Post-hoc tests after Kruskal-Wallis:
  Multiple testing adjustments'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. Plain Language Restatement

When you run a Kruskal-Wallis test to compare three or more groups and find a statistically significant difference, you usually want to follow up with **post-hoc pairwise tests** (like Dunn’s test or Conover-Imam) to see *which specific groups* differ from each other. 

The student is asking two fundamental questions about this process:
1. **The "Protected" Test Question:** Do we actually need to adjust our $p$-values for multiple comparisons if we only run these pairwise tests *after* getting a significant overall Kruskal-Wallis result? (Does the initial Kruskal-Wallis test "protect" us from false positives, making adjustments unnecessary?)
2. **The Adjustment Choice Question:** If we *do* need to adjust for multiple testing, which method (Holm, Šidák, Benjamini-Hochberg, etc.) is the best choice?

---

### 2. Step-by-Step Solution

#### Part 1: Is a multiple testing adjustment necessary?

**Step 1.1: Understand the "Protected Fisher" concept the student is referring to.**
In classical ANOVA, the "Protected Fisher's Least Significant Difference (LSD)" test allows you to run pairwise $t$-tests without multiple testing corrections *if and only if* the overall ANOVA $F$-test is significant. The logic is that the global test acts as a gatekeeper, controlling the Family-Wise Error Rate (FWER) at the nominal alpha level ($\alpha$).

**Step 1.2: Evaluate whether this applies to Kruskal-Wallis and nonparametric post-hocs.**
While older texts (such as Conover 1999) state that you only perform Conover-Imam or Dunn tests if the overall Kruskal-Wallis is significant, **modern statistical consensus strongly disagrees with skipping multiple testing adjustments.** 

Here is why:
* The Kruskal-Wallis test evaluates differences in mean ranks across *all* groups simultaneously. 
* Once you reject the global null hypothesis, you have multiple ways the groups could differ. If you conduct $k$ pairwise comparisons without a correction, the probability of making at least one Type I error (false positive) across those comparisons rapidly exceeds your significance level ($\alpha$).
* The Kruskal-Wallis test **does not** strictly protect individual pairwise comparisons in the same way a truly conservative closed testing procedure might. 

**Step 1.3: Answer the sub-question about the number of groups.**
Yes, the number of groups ($g$) directly dictates the number of pairwise comparisons ($m = \frac{g(g-1)}{2}$). As the number of groups increases, the number of pairwise tests grows quadratically, drastically inflating the Family-Wise Error Rate if no adjustment is made. Therefore, multiple testing corrections are **always recommended** for post-hoc pairwise tests, regardless of whether the global Kruskal-Wallis was significant.

---

#### Part 2: Which multiple testing adjustment should be used?

**Step 2.1: Identify the goals of different adjustment methods.**
When choosing an adjustment, you must decide what you want to control:
* **FWER (Family-Wise Error Rate):** The probability of making *one or more* false discoveries among all tests. (Conservative)
* **FDR (False Discovery Rate):** The expected proportion of false discoveries among all rejected tests. (Less conservative, higher power)

**Step 2.2: Evaluate the options mentioned by the student.**
1. **Holm-Bonferroni Method:** 
   * *Type:* Controls FWER in a step-down manner.
   * *Verdict:* **Highly recommended.** It is uniformly more powerful than the standard Bonferroni correction, makes no assumptions about the dependence of tests, and is standardly implemented in packages like `dunn.test` in R.
2. **Šidák Method:** 
   * *Type:* Controls FWER. 
   * *Verdict:* Slightly more powerful than Bonferroni under independence, but yields almost identical results in practice. It is rarely necessary over Holm because Holm is non-parametric/distribution-free regarding the $p$-values.
3. **Benjamini-Hochberg (BH) Method:** 
   * *Type:* Controls FDR.
   * *Verdict:* **Good alternative if exploratory.** If you are dealing with a large number of pairwise comparisons (e.g., microbiome or genomics data) and want to avoid missing true effects (Type II errors), controlling FDR via Benjamini-Hochberg is appropriate. However, for standard experimental designs with few groups, FWER control (Holm) remains the traditional standard.

---

### 3. Final Answer

1. **Are adjustments necessary?** **Yes.** Even if the overall Kruskal-Wallis test is significant, running multiple pairwise post-hoc tests (like Dunn's or Conover-Imam) inflates your risk of false positives. The global Kruskal-Wallis test does not provide sufficient protection for individual post-hoc pairwise comparisons. This issue scales up with the number of groups being compared.
2. **Which adjustment should you use?** 
   * Use **Holm (Holm-Bonferroni)** as your default choice. It is simple, strictly controls the Family-Wise Error Rate (FWER), and is more powerful than standard Bonferroni.
   * Use **Benjamini-Hochberg** only if you have a large number of comparisons and prefer to control the False Discovery Rate (FDR) to maximize statistical power in an exploratory setting.

---

### 4. Common Mistakes

* **The "Protected Test" Fallacy:** Assuming that a significant Kruskal-Wallis test gives you a "free pass" to run unadjusted Mann-Whitney U or Dunn tests on all pairs. 
* **Using Standard Bonferroni:** Using the raw Bonferroni correction instead of Holm's adjustment. Holm's method is strictly superior because it offers greater statistical power while maintaining the exact same error control.
* **Confusing FWER and FDR:** Applying a False Discovery Rate correction (like Benjamini-Hochberg) when a strict Family-Wise Error Rate correction (like Holm) is required by your field's publication standards, or vice versa. Always check your discipline's standard practices.

*Original question: [Post-hoc tests after Kruskal-Wallis: Multiple testing adjustments](https://stats.stackexchange.com/questions/677526/post-hoc-tests-after-kruskal-wallis-multiple-testing-adjustments) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
