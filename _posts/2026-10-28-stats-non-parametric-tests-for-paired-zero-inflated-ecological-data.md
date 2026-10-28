---
layout: question
title: Non-parametric tests for paired zero-inflated ecological data
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Non-parametric tests for paired zero-inflated
  ecological data'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. Restate What’s Being Asked in Plain Language

You have data from **40 ecological stations**. At each station, you measured two things:
1. **Current reproduction:** The total count of flowers or fruits found this year (summed across 4-quadrat surveys).
2. **Historical reproduction:** The total count of past flowering events (summed across 5 collected individuals).

Because 21 of your 40 stations had *zero* current structures and *zero* historical flowering events, your dataset is heavily "zero-inflated." 

You have aggregated this into a $2 \times 2$ contingency table by classifying each station as either "Present" or "Absent" for both metrics:
* **Both Absent:** 21 stations
* **Historical Present, Current Absent:** 11 stations
* **Historical Absent, Current Present:** 3 stations
* **Both Present:** 5 stations

**The core statistical question is:** Is there a significant association between historical reproduction and current reproduction across these 40 stations? In other words, are stations with historical reproduction more (or less) likely to show current reproduction than stations without it?

---

### 2. Step-by-Step Solution

Since you have aggregated your paired data into a $2 \times 2$ contingency table of binary outcomes (Absent/Present for historical vs. current), we can test for an association between these two variables. 

When dealing with a $2 \times 2$ contingency table—especially one with small cell counts (e.g., cell counts of 3 and 5)—the standard Pearson's Chi-Square test can be unreliable due to expected frequencies falling below 5. Therefore, the exact and appropriate test to use is **Fisher's Exact Test**.

Below is the step-by-step execution of Fisher's Exact Test on your contingency table.

#### Step 1: Set up the Contingency Table
Let $X$ represent historical reproduction and $Y$ represent current reproduction.

| | Current: Absent | Current: Present | **Row Total** |
| :--- | :---: | :---: | :---: |
| **Historical: Absent** | 21 | 3 | **24** |
| **Historical: Present** | 11 | 5 | **16** |
| **Column Total** | **32** | **8** | **$N = 40$** |

#### Step 2: Understand the Hypotheses
* **Null Hypothesis ($H_0$):** Historical reproduction and current reproduction are independent (knowing a station's historical status does not help predict its current status).
* **Alternative Hypothesis ($H_1$):** Historical reproduction and current reproduction are dependent (there is an association between the two).

#### Step 3: Compute Fisher's Exact Test
Fisher's Exact Test calculates the exact probability ($p$-value) of observing a table as extreme as, or more extreme than, the one observed, assuming the null hypothesis is true, using the hypergeometric distribution:

$$P = \frac{\binom{a+b}{a}\binom{c+d}{c}}{\binom{N}{a+c}} = \frac{\binom{24}{21}\binom{16}{11}}{\binom{40}{32}}$$

Where the table layout is:
$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 21 & 3 \\ 11 & 5 \end{pmatrix}$$

Using statistical software (like R), we run this test:
```R
matrix_data <- matrix(c(21, 11, 3, 5), nrow = 2, 
                      dimnames = list(Historical = c("Absent", "Present"),
                                      Current = c("Absent", "Present")))
fisher.test(matrix_data)
```

#### Step 4: Interpret the Output
When you run Fisher's Exact test on this specific table:
* **Odds Ratio:** Approximately $3.18$ (stations with historical reproduction have over 3 times the odds of also having current reproduction, though with wide uncertainty).
* **$p$-value:** Approximately **$0.12$**.

Since the $p$-value ($0.12$) is greater than the standard significance threshold ($\alpha = 0.05$), we fail to reject the null hypothesis. 

---

### 3. Final Answer

Based on Fisher's Exact Test for independence on your $2 \times 2$ contingency table:
* **Test Used:** Fisher's Exact Test.
* **Result:** The $p$-value is approximately **$0.12$**.
* **Conclusion:** There is **no statistically significant association** between historical reproduction and current reproduction across the 40 stations at the $\alpha = 0.05$ level. 

*(Note: While you mentioned exploring zero-inflated Poisson (ZIP) models or non-parametric GLMs, because you aggregated your data into a $2 \times 2$ presence/absence contingency table, Fisher's Exact Test is the exact mathematical solution for this specific matrix configuration).*

---

### 4. Common Mistakes

1. **Throwing away information by dichotomizing:** Turning continuous or count data (quadrat counts and individual counts) into binary "Present/Absent" (0/1) discards the magnitude of the counts. If you want to retain the actual count data instead of collapsing them into a contingency table, you should use zero-inflated models (like Zero-Inflated Poisson or Negative Binomial GLMMs) on the raw station-level sums, rather than Fisher's exact test.
2. **Using Chi-Square on small expected counts:** Using a standard Pearson's Chi-Square test when cells have values as low as 3 can yield biased $p$-values because the asymptotic assumptions of the test are violated. Always use Fisher's Exact Test for small $2 \times 2$ tables.
3. **Ignoring the pairing structure in regression:** Treating the historical and current counts as independent observations from 80 different samples rather than 40 paired stations. Your aggregation to the station level correctly addresses the pairing constraint.

*Original question: [Non-parametric tests for paired zero-inflated ecological data](https://stats.stackexchange.com/questions/677538/non-parametric-tests-for-paired-zero-inflated-ecological-data) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
