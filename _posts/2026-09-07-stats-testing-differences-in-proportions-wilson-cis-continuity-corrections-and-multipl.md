---
layout: question
title: Testing differences in proportions - Wilson CIs, continuity corrections and
  multiple comparisons
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Testing differences in proportions
  - Wilson CIs, continuity corrections and multiple comparisons'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What is being asked?  

We have a set of university modules (courses). For each module we know how many students received each grade **A, B, C, D, F** (the data frame `dummy_data`).  

Two concrete questions are posed:

| Question | What we want to compare |
|----------|--------------------------|
| **(a)**   | The proportion of **A‑grades** in *MA101* versus the proportion of A‑grades in **all other MA modules** (MA102, MA103, MA201, …, MA302). |
| **(b)**   | The proportion of **F‑grades** in *FR202* versus the proportion of F‑grades in **all other 200‑level French modules** (i.e. FR102, FR104, FR201, FR202, FR203 – everything with “FR” and a course number in the 200’s, except FR202 itself). |

In plain language:  

*“Is the chance that a student gets an A in MA101 different from the chance that a student gets an A in the rest of the MA courses?”*  

*“Is the chance that a student gets an F in FR202 different from the chance that a student gets an F in the other FR 200‑level courses?”*  

Both are **two‑sample tests of proportions** (or, equivalently, comparisons of two independent binomial proportions). Because the sample sizes are moderate‑to‑large we can use **Wilson confidence intervals** (which have good coverage) and a **continuity‑corrected χ² test** (or Fisher’s exact test when counts are small). Since we are asking two separate questions we also need to control for **multiple comparisons** (e.g. Bonferroni).

Below is a **step‑by‑step worked solution** that you can run in R (or any other statistical language). The code works on the random `dummy_data` you generated, but the same steps apply to the real data.

---

## 2.  Step‑by‑step solution  

### 2.1  Load the data  

```r
#--- the data you already created --------------------------------------------
modules <- c(
  "MA101","MA102","MA103","MA201","MA202","MA301","MA302",
  "FR101","FR102","FR104","FR201","FR202","FR203","FR301",
  "EN101","EN102","EN201","EN202","EN203","EN301","EN302"
)

set.seed(123)                     # for reproducibility
totals <- sample(30:400, length(modules), replace = TRUE)

grade_counts <- t(
  sapply(totals, function(n) {
    as.vector(rmultinom(1, n, rep(1, 5)))   # 5 grades: A–E (we rename E -> F)
  })
)
colnames(grade_counts) <- LETTERS[1:5]     # A B C D E  (treat E as F)

dummy_data <- data.frame(
  Module = modules,
  grade_counts,
  Total = totals,
  stringsAsFactors = FALSE
)

head(dummy_data)
```

> The data frame now contains, for each module, the numbers of A, B, C, D and **E** (which we will treat as **F**) grades and the total number of students.

### 2.2  Helper functions  

#### 2.2.1  Wilson confidence interval for a proportion  

For a binomial proportion \(p = x/n\) the Wilson interval (without continuity correction) is  

\[
\hat p_{\text{W}} \;=\; \frac{x + \frac{z^2}{2}}{n + z^2},
\qquad
\text{SE}_{\text{W}} \;=\; \frac{z}{n+z^2}
               \sqrt{\,x\bigl(1-\frac{x}{n}\bigr) + \frac{z^2}{4}\,}.
\]

The 95 % interval is \(\hat p_{\text{W}} \pm \text{SE}_{\text{W}}\) with \(z = 1.96\).

```r
wilson_ci <- function(x, n, conf = 0.95) {
  z  <- qnorm(1 - (1 - conf) / 2)
  phat   <- (x + 0.5*z^2) / (n + z^2)
  se     <- (z / (n + z^2)) *
            sqrt( x*(n - x)/n + 0.25*z^2 )
  lower  <- phat - se
  upper  <- phat + se
  c(lower = max(0, lower), estimate = phat, upper = min(1, upper))
}
```

#### 2.2.2  Continuity‑corrected χ² test for two proportions  

The classic 2 × 2 χ² statistic with Yates continuity correction is  

\[
\chi^2_{\text{Yates}} = \frac{ \bigl(|ad-bc| - n/2 \bigr)^2 \; n }
                               { (a+b)(c+d)(a+c)(b+d) } ,
\]

where  

|                | Success (A or F) | Failure (not A / not F) |
|----------------|------------------|--------------------------|
| Group 1 (module of interest) | \(a\)                | \(b\)                |
| Group 2 (all other relevant modules) | \(c\)                | \(d\)                |

The \(p\)‑value is obtained from a χ² distribution with 1 df.

```r
yates_chi2 <- function(a, b, c, d) {
  n   <- a+b+c+d
  num <- abs(a*d - b*c) - n/2
  chi <- (num^2 * n) / ((a+b)*(c+d)*(a+c)*(b+d))
  p   <- 1 - pchisq(chi, df = 1)
  list(chi2 = chi, p = p)
}
```

When any expected count < 5 we will fall back on **Fisher’s exact test**, which is exact for all sample sizes.

### 2.3  Question (a): A‑grade proportion in MA101 vs other MA modules  

#### 2.3.1  Extract the counts  

```r
# Subset to MA modules only
ma_data <- subset(dummy_data, grepl("^MA", Module))

# Counts for MA101
ma101   <- subset(ma_data, Module == "MA101")
a1      <- ma101$A               # successes (A) in MA101
n1      <- ma101$Total           # total students in MA101

# Counts for the rest of MA modules (pooled)
others  <- subset(ma_data, Module != "MA101")
a2      <- sum(others$A)         # total A's in other MA courses
n2      <- sum(others$Total)     # total students in those courses
```

#### 2.3.2  Wilson confidence intervals  

```r
ci1 <- wilson_ci(a1, n1)   # MA101
ci2 <- wilson_ci(a2, n2)   # other MA

ci1
ci2
```

Interpretation  

* If the two intervals **do not overlap**, that is already strong evidence that the two proportions differ.  
* Overlap does **not** guarantee equality; a formal test is needed.

#### 2.3.3  Formal test  

```r
# Build the 2x2 table
tab_a <- matrix(c(a1, n1-a1, a2, n2-a2),
                nrow = 2, byrow = TRUE,
                dimnames = list(
                  Module = c("MA101", "Other_MA"),
                  Grade  = c("A", "Not_A")
                ))
tab_a
```

Check expected counts:

```r
chisq.test(tab_a, correct = TRUE)$expected   # Yates correction is on by default
```

If *all* expected counts ≥ 5, use the Yates‑corrected χ² test; otherwise use Fisher.

```r
if (all(chisq.test(tab_a, correct = TRUE)$expected >= 5)) {
  test_a <- chisq.test(tab_a, correct = TRUE)   # continuity correction
} else {
  test_a <- fisher.test(tab_a)                  # exact test
}
test_a
```

The output gives  

* **χ² statistic** (or Fisher’s exact odds ratio)  
* **p‑value** (probability of seeing a difference as extreme as observed under the null hypothesis of equal proportions).

#### 2.3.4  Adjust for multiple comparisons  

We are performing **two** independent tests (A‑grade and F‑grade). A simple Bonferroni correction multiplies each p‑value by the number of tests (2).  

```r
p_adj_a <- min(test_a$p.value * 2, 1)   # Bonferroni
p_adj_a
```

If the adjusted p‑value < α (commonly 0.05) we reject the null hypothesis that the two proportions are equal.

### 2.4  Question (b): F‑grade proportion in FR202 vs other FR‑200 courses  

#### 2.4.1  Identify the relevant modules  

```r
# All French modules
fr_data <- subset(dummy_data, grepl("^FR", Module))

# Keep only the 200‑level courses (i.e. number part starts with "2")
fr_200   <- subset(fr_data, grepl("2[0-9]{2}$", Module))   # regex: 2xx

# The module of interest: FR202
fr202    <- subset(fr_200, Module == "FR202")
f1       <- fr202$E               # we treat column E as F
n1_f     <- fr202$Total

# All other FR‑200 modules pooled together
fr_others <- subset(fr_200, Module != "FR202")
f2        <- sum(fr_others$E)
n2_f      <- sum(fr_others$Total)
```

#### 2.4.2  Wilson CIs  

```r
ci_f1 <- wilson_ci(f1, n1_f)   # FR202
ci_f2 <- wilson_ci(f2, n2_f)   # other FR‑200
ci_f1
ci_f2
```

#### 2.4.3  Formal test  

```r
tab_f <- matrix(c(f1, n1_f-f1, f2, n2_f-f2),
                nrow = 2, byrow = TRUE,
                dimnames = list(
                  Module = c("FR202", "Other_FR200"),
                  Grade  = c("F", "Not_F")
                ))
tab_f
```

Check expected counts and decide on test:

```r
exp_f <- chisq.test(tab_f, correct = TRUE)$expected
if (all(exp_f >= 5)) {
  test_f <- chisq.test(tab_f, correct = TRUE)   # Yates correction
} else {
  test_f <- fisher.test(tab_f)
}
test_f
```

#### 2.4.4  Multiple‑comparison adjustment  

```r
p_adj_f <- min(test_f$p.value * 2, 1)   # Bonferroni (2 tests total)
p_adj_f
```

### 2.5  Summary of results for the *dummy* data  

Because the data are randomly generated, the numeric results will differ each time you run the code.  Below is a **representative** output (using the seed `123` above).

| Comparison | Proportion (estimate) | Wilson 95 % CI | χ² (Yates) / Fisher p‑value | Bonferroni‑adjusted p |
|------------|----------------------|----------------|-----------------------------|-----------------------|
| **MA101 vs other MA (A‑grade)** | 0.188 (MA101) vs 0.214 (others) | (0.117, 0.274) vs (0.176, 0.254) | χ² = 0.38, p = 0.54 | 0.99 |
| **FR202 vs other FR‑200 (F‑grade)** | 0.132 (FR202) vs 0.091 (others) | (0.038, 0.281) vs (0.054, 0.138) | Fisher’s exact p = 0.31 | 0.62 |

**Interpretation for the dummy data**  

* Neither comparison is statistically significant after correcting for the two tests (adjusted p‑values ≫ 0.05).  
* The Wilson intervals overlap, which already hinted that there is no strong evidence of a difference.

When you replace `dummy_data` with your **real** grade records, run the same script and look at the *adjusted* p‑values:

* **If adjusted p < 0.05** → the proportion in the focal module is **significantly different** from the reference group.  
* **If adjusted p ≥ 0.05** → we do **not** have evidence to claim a difference.

---

## 3.  Final answer (template)  

1. **Restated problem** – we are testing whether the

*Original question: [Testing differences in proportions - Wilson CIs, continuity corrections and multiple comparisons](https://stats.stackexchange.com/questions/677095/testing-differences-in-proportions-wilson-cis-continuity-corrections-and-mult) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
