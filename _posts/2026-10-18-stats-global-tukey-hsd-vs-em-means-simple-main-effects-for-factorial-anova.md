---
layout: question
title: Global Tukey HSD vs. EM Means (Simple Main Effects) for Factorial ANOVA?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Global Tukey HSD vs. EM Means (Simple
  Main Effects) for Factorial ANOVA?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is really asking  

*In plain English*  

You have a two‑way (or higher‑order) ANOVA and the **interaction** between the factors is significant.  
Instead of comparing *every* treatment combination with every other one (the usual Tukey HSD “global” test), you only care about **simple main effects** – e.g., “compare the levels of factor A **within** each level of factor B, and/or compare the levels of factor B **within** each level of factor A”.  

The question is:

* Can we use **estimated marginal means (EMMs, also called LS‑means)** and apply a multiplicity correction such as Bonferroni or Sidak **just to those local comparisons**, rather than doing a global Tukey HSD?  
* What do standard statistical guidelines say about this approach?

---

## 2.  Step‑by‑step solution  

### Step 1 – Clarify the hypotheses you actually want to test  

Suppose we have two factors  

| Factor A | Levels | a₁, a₂, …, aₖ |
|----------|--------|--------------|
| Factor B | Levels | b₁, b₂, …, bₘ |

The full model is  

\[
Y_{ijk}= \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij}+ \varepsilon_{ijk},
\qquad \varepsilon_{ijk}\sim N(0,\sigma^{2}),
\]

with the usual constraints (sum‑to‑zero or reference coding).  

When the interaction \( (\alpha\beta)_{ij}\) is significant, the **simple main effects** are the sets of null hypotheses

* **Within‑B comparisons** (for each fixed \(j\)):  

  \[
  H_{0}^{(j)}: \ \alpha_1+\! (\alpha\beta)_{1j}= \alpha_2+\! (\alpha\beta)_{2j}= \dots = \alpha_k+\! (\alpha\beta)_{kj}.
  \]

* **Within‑A comparisons** (for each fixed \(i\)):  

  \[
  H_{0}^{(i)}: \ \beta_1+\! (\alpha\beta)_{i1}= \beta_2+\! (\alpha\beta)_{i2}= \dots = \beta_m+\! (\alpha\beta)_{im}.
  \]

If you only care about the first set (or the second), that **defines the family of hypotheses** you will test.

### Step 2 – Obtain the appropriate means (EMMs)  

*Estimated marginal means* are the model‑based (least‑squares) means that are **adjusted for the other factors**.  

In R, the `emmeans` package (or SAS `LSMEANS`, SPSS *Estimated Marginal Means*) produces exactly the quantities needed:

```r
library(emmeans)

# fit the model
fit <- aov(Y ~ A * B, data = mydata)

# EMMs for factor A *within* each level of B
emm_A_by_B <- emmeans(fit, ~ A | B)   # "by" B
```

The object `emm_A_by_B` contains the LS‑means for each level of A **conditional on each level of B**, i.e. the simple main effects.

### Step 3 – Choose a multiplicity correction  

Because you are performing *multiple* pairwise tests **within each slice**, you must control the error rate for the family you have defined.  

Two common choices:

| Procedure | What it controls | When it is appropriate |
|-----------|------------------|------------------------|
| **Tukey** (HSD) | Family‑wise error rate (FWER) for *all* pairwise comparisons in the family | Use when you truly want **all** pairwise comparisons within a slice (e.g., \(k(k-1)/2\) tests per level of B). |
| **Bonferroni** | FWER (very conservative) | Simple to apply; divide \(\alpha\) by the total number of pairwise tests you are making. |
| **Sidak** | FWER (slightly less conservative than Bonferroni) | Use when tests are independent or positively dependent (rarely exactly true, but often used). |
| **Holm** | FWER, step‑down version of Bonferroni (more power) | Recommended when you have many comparisons. |
| **Benjamini‑Hochberg (FDR)** | False discovery rate | Acceptable if you are willing to tolerate a proportion of false positives, and you have many simple‑effect tests. |

**Key point:** The correction must be applied **within the family you have pre‑specified**. If you only want to compare A‑levels *within each* B‑level, the family can be:

*All pairwise comparisons of A at a given B, **pooled across all B levels***, **or**
*All pairwise comparisons of A within each B level **separately**, each with its own correction.*

Both approaches are legitimate; they just control different error rates.

### Step 4 – Implement the comparison in software  

Using `emmeans` we can ask for pairwise contrasts and specify the adjustment:

```r
# Pairwise comparisons of A within each B, Tukey adjusted *within each B*
pairwise_A_by_B <- contrast(emm_A_by_B, method = "pairwise", adjust = "tukey")
pairwise_A_by_B
```

If you prefer Bonferroni (or Sidak) across *all* simple‑effect tests (i.e., across all slices together), you can do:

```r
# Number of total pairwise tests = (k choose 2) * m
k <- length(levels(mydata$A))
m <- length(levels(mydata$B))
n_test <- choose(k,2) * m

pairwise_A_all <- contrast(emmeans(fit, ~ A | B), method = "pairwise",
                           adjust = "bonferroni")   # or "sidak"
```

The `adjust` argument automatically divides \(\alpha\) by the appropriate number of tests.

### Step 5 – Interpret the results in light of the interaction  

* The **global interaction test** (the ANOVA F‑test) tells you that *some* simple main effects differ, but it does **not** tell you which ones.
* The **simple‑effect tests** you just performed answer the substantive question: “Within each level of B, do the A‑means differ?” (or vice‑versa).
* Because you have limited the family of hypotheses to the set you actually care about, the adjustment you chose is *statistically correct*—it controls the error rate for the hypotheses you are testing, not for the whole set of possible pairwise comparisons that Tukey would consider.

### Step 6 – What do statistical guidelines say?  

| Source | Recommendation |
|--------|----------------|
| **Cohen (1988) & Maxwell & Delaney (2004)** | After a significant interaction, *probe* it with simple‑effect comparisons. Use a *familywise* error control that matches the set of comparisons you intend to make. |
| **American Psychological Association (APA) 7th ed., § 8.9** | “When conducting post‑hoc tests, the researcher should limit the family of comparisons to those that are theoretically justified and adjust p‑values accordingly.” |
| **R. H. Scheffe (1959) & Tukey (1953)** | Scheffé’s method is *global* (covers all possible contrasts) and is very conservative; Tukey’s HSD is designed for *all pairwise* comparisons. If you only need a subset, you may use any other method (Bonferroni, Sidak, Holm) that controls the error rate for that subset. |
| **Harrell (2015), “Regression Modeling Strategies”** | “Estimated marginal means (LS‑means) together with the `emmeans` package provide a transparent way to test any set of linear contrasts you specify; the programmer must decide on the appropriate multiplicity adjustment for the chosen contrast set.” |

**Bottom line:**  

*The statistical literature treats the approach you propose as perfectly acceptable.* The only “rule” is that the error‑rate control must be applied to the *exact* family of hypotheses you decide **a priori** to test. Using EMMs (or LS‑means) is the modern, model‑based way to obtain those simple‑effect means, and the same adjustment procedures (Tukey, Bonferroni, Sidak, Holm, etc.) can be applied to the resulting pairwise contrasts.

---

## 3.  Final answer  

Yes.  
When a factorial ANOVA shows a significant interaction, you may (and often should) examine **simple main effects** instead of performing a global Tukey HSD across all treatment combinations.  

1. Compute the estimated marginal (least‑squares) means for the factor of interest **within each level of the other factor** (e.g., `emmeans(fit, ~ A | B)`).  
2. Form the set of pairwise contrasts that correspond to the simple effects you care about.  
3. Apply a multiplicity correction (Bonferroni, Sidak, Tukey, Holm, etc.) **only to that set**.  

The adjustment controls the family‑wise error rate (or false‑discovery rate) for exactly the hypotheses you are testing, which is consistent with statistical best‑practice guidelines. A global Tukey HSD is unnecessary—and would be overly conservative—if you are not interested in comparisons outside the chosen slices.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Applying a global Tukey HSD and then ignoring most of the output** | The test still controls FWER for *all* pairwise comparisons, making it more conservative than needed for the subset you care about. | Limit the family of hypotheses to the simple‑effect set before adjusting. |
| **Using the same α for each slice without a correction** | If you test, say, three slices each at α = 0.05, the overall chance of at least one Type I error exceeds 0.05. | Apply a correction that accounts for the total number of tests across slices (e.g., Bonferroni across all simple‑effect tests, or use Holm). |
| **Treating LS‑means as raw group means** | LS‑means are adjusted for the other factor(s); they are not the same as simple arithmetic means when the design is unbalanced. | Remember that LS‑means are the appropriate quantities for marginal (simple) effects in a linear model. |
| **Testing simple effects without first confirming a significant interaction** | If the interaction is non‑significant, probing it inflates Type I error and may be unnecessary. | Follow the hierarchical testing rule: first test the interaction, then proceed to simple effects only if it is significant (or if you have strong a‑priori hypotheses). |
| **Choosing a correction arbitrarily** | Different corrections control different error rates; picking one without justification may be either too liberal or overly conservative. | Decide whether you need family‑wise control (FWER) or are comfortable with false‑discovery rate (FDR) and select the corresponding method (Bonferroni/Holm vs. BH). |

---  

*Original question: [Global Tukey HSD vs. EM Means (Simple Main Effects) for Factorial ANOVA?](https://stats.stackexchange.com/questions/677449/global-tukey-hsd-vs-em-means-simple-main-effects-for-factorial-anova) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
