---
layout: question
title: Analyzing Changes in Partisanship in Absentee Voting
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Analyzing Changes in Partisanship
  in Absentee Voting'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. What's Being Asked in Plain Language

The student is trying to test a statistical and logical hypothesis about the 2020 election: **Did the massive surge in Democratic absentee voting happen simply because Democrats chose to vote by mail at higher rates, while Republicans mostly voted in person?**

To test this, the student looked at county-level data in Virginia across multiple election years. Their logic was:
* If Democrats disproportionately shifted to absentee voting, then counties with higher Democratic populations (which the student proxied using non-White population percentages) should have seen the largest increases in the *percentage* of votes cast via absentee ballots.
* To check this, the student calculated the change in absentee ballot usage for each county between pairs of election years.
* They then measured the **Pearson correlation** between this change in county absentee usage and the county's demographic makeup (non-White population percentage). 

Essentially, the goal is to evaluate whether demographic baselines (used as a proxy for partisan lean) successfully predict the geographic variation in how much counties increased their reliance on absentee voting.

---

### 2. Step-by-Step Statistical Breakdown

To determine how the student might be misusing statistics or how to properly execute and evaluate this workflow, we must break down the statistical mechanics of what they did.

#### Step 1: Define the Variables
* **Independent/Predictor Variable ($X$):** The demographic makeup of a county, specifically the non-White population percentage ($X_i$ for county $i$).
* **Dependent/Response Variable ($Y$):** The change in absentee ballot usage in county $i$ between year $A$ and year $B$:
  $$\Delta \text{Absentee}_i = (\text{Absentee Usage \% in Year } B)_i - (\text{Absentee Usage \% in Year } A)_i$$

#### Step 2: Calculate the Pearson Correlation Coefficient ($r$)
The student calculated the Pearson correlation coefficient between $X$ and $Y$ across all counties $i$:
$$r = \frac{\sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum_{i=1}^{n} (X_i - \bar{X})^2} \sum_{i=1}^{n} (Y_i - \bar{Y})^2}$$

#### Step 3: Evaluate Potential Statistical Issues (Why the student felt they were "misusing statistics")
While the intuition is sound, running Pearson correlations across multiple pairwise combinations of years introduces several statistical pitfalls:

1. **Ecological Fallacy / Proxy Mismatch:** Using "non-White population percentage" as a proxy for "Democratic vote share" introduces noise. While correlated in Virginia, they are not identical. Direct measurement of past Democratic vote share (e.g., from a previous statewide race) would be a more precise $X$ variable.
2. **Multiple Comparisons Problem:** The student stated they calculated this "for every possible combination of election years." By calculating correlations across dozens of year-pairs (e.g., 2005 vs 2007, 2005 vs 2009... up to 2023), the probability of finding a statistically significant correlation purely by random chance increases (Type I error inflation).
3. **Non-Linearity and Boundary Effects:** Absentee usage percentages are bounded between $0\%$ and $100\%$. If a county already had high absentee usage in a baseline year, its room to "increase" is structurally capped compared to a county starting at $0\%$. This ceiling effect can violate the linearity assumption of Pearson correlation.
4. **Collinearity and Autocorrelation:** Comparing overlapping years (e.g., 2011 compared to 2019 versus 2013 compared to 2019) creates dependent observations, violating the assumption of independent and identically distributed (i.i.d.) data if these correlation coefficients are later compared or pooled together.

---

### 3. Final Answer

The student’s logic is **fundamentally sound from a deductive reasoning standpoint**, but their execution runs into common statistical traps. 

* **Is the logic correct?** Yes. If a specific demographic/partisan group shifts behavior (e.g., adopting mail-in voting en masse), geographic areas densely populated by that group should exhibit the largest shifts in that specific voting method.
* **Are they misusing statistics?** Partially. Running bivariate Pearson correlations across *every possible combination* of historical years creates a multiple-testing problem and ignores boundary constraints (percentages bounded at 0 and 100). 
* **The Corrected Approach:** Instead of correlating changes across every pairwise year combination, the student should use a **regression framework (such as Difference-in-Differences or a fixed-effects model)** using direct baseline partisan metrics rather than demographic proxies, while explicitly accounting for pre-existing trends in absentee voting prior to 2020.

---

### 4. Common Mistakes for This Problem Type

1. **Confusing Demographic Proxies with Direct Variables:** Using race as a proxy for party affiliation adds unnecessary variance. Always use the most direct measure available (e.g., historical partisan vote share) when testing partisan hypotheses.
2. **Ignoring the Bounded Nature of Percentages:** Using standard Pearson correlation on variables bounded between 0 and 1 (or 0% and 100%) can lead to distorted linear estimates due to floor and ceiling effects.
3. **The "Fishing Expedition" (Multiple Testing):** Calculating correlations across *every* possible combination of years guarantees you will find "significant" results somewhere by random chance. Hypothesis tests should be specified *a priori* (e.g., explicitly testing 2016 vs. 2020).
4. **Conflating Cross-Sectional Change with Causal Proof:** Finding a positive correlation between a county's demographic makeup and its increase in absentee voting shows an association, but it does not mathematically prove *why* individual voters changed behavior (as individual-level shifts cannot be definitively proven using only aggregate county-level data—known as the **Ecological Fallacy**).

*Original question: [Analyzing Changes in Partisanship in Absentee Voting](https://stats.stackexchange.com/questions/677493/analyzing-changes-in-partisanship-in-absentee-voting) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
