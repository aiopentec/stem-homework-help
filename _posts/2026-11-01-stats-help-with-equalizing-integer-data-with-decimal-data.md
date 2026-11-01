---
layout: question
title: Help with equalizing integer data with decimal data
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Help with equalizing integer data
  with decimal data'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. Restate What’s Being Asked in Plain Language

Historically, air rifle competitors were scored using whole numbers (integers) from 0 to 10 per shot, resulting in a maximum possible score of 300 for a 30-shot match. A plaque honors anyone who achieved an elite score of 280 or higher. 

The sport has now switched to a decimal scoring system, where each shot is worth anywhere from 0.0 to 10.9, raising the maximum possible score to 327. Because decimal scoring awards fractional points for shots landing between the rings, modern competitors naturally score higher totals than they would have under the old system. 

The goal is to find the mathematical equivalent of the old integer score of 280 under the new decimal scoring system so that the plaque remains equally exclusive and fair to both past and present competitors.

---

## 2. Show Every Step (No Steps Skipped)

To find the equivalent threshold, we need to understand the relationship between the old integer scoring scale and the new decimal scoring scale.

### Step 1: Analyze the Old Scoring System
* **Shots per match:** 30 shots (10 prone, 10 kneeling, 10 standing)
* **Minimum per shot:** 0
* **Maximum per shot:** 10
* **Maximum possible total score:** $30 \text{ shots} \times 10 \text{ points} = 300$
* **Target historical threshold:** 280

### Step 2: Determine the Historical Achievement Level (Percentage)
To see how "elite" a score of 280 was, we calculate what percentage of the maximum possible score it represents:
$$\text{Percentage} = \frac{280}{300}$$

$$\frac{280}{300} = 0.9333... \text{ or } 93.33\%$$

This means a historical competitor needed to earn **93.33%** of the maximum possible points to qualify for the plaque.

### Step 3: Analyze the New Decimal Scoring System
* **Shots per match:** 30 shots
* **Minimum per shot:** 0.0
* **Maximum per shot:** 10.9
* **Maximum possible total score:** $30 \text{ shots} \times 10.9 \text{ points} = 327$

### Step 4: Apply the Historical Percentage to the New System
Assuming the skill level required to earn a 93.33% remains constant, we apply that same percentage (0.9333...) to the new maximum possible score of 327:

$$\text{Equivalent Decimal Score} = 327 \times 0.9333...$$

To do this precisely using fractions:
$$\text{Equivalent Decimal Score} = 327 \times \left(\frac{280}{300}\right)$$

$$\text{Equivalent Decimal Score} = \frac{327 \times 280}{300}$$

$$\text{Equivalent Decimal Score} = \frac{91,560}{300}$$

$$\text{Equivalent Decimal Score} = 305.2$$

---

## 3. State the Final Answer Clearly

To maintain the exact same level of elite performance (93.33% of the maximum possible score), the equivalent threshold on the new decimal scoring system is **305.2**. 

Therefore, modern competitors should need a score of **305.2 or higher** to earn a spot on the plaque.

---

## 4. Common Mistakes for This Problem Type

* **Mistake 1: Adding a flat offset (additive approach).** 
  * *What people do:* Notice that decimal scoring adds up to 0.9 extra per shot, calculate $30 \text{ shots} \times 0.5 \text{ (average extra decimal)} = 15$, and add 15 to 280 to get 295.
  * *Why it’s wrong:* Scoring is proportional, not additive. A competitor shooting poorly won't gain the same decimal benefit as a competitor shooting near the center. Proportions must be maintained via percentages or ratios.
* **Mistake 2: Confusing the per-shot maximum with the total match maximum.**
  * *What people do:* Try to scale individual shots (e.g., converting a score of 9.3) instead of looking at the cumulative match total.
  * *Why it’s wrong:* The historical threshold of 280 is a *total match* aggregate, so the conversion must happen at the macro level using total maximums (300 vs. 327).
* **Mistake 3: Assuming scoring distributions are uniform.**
  * *What people do:* Assume that every integer score translates cleanly to a specific decimal (.0). 
  * *Why it’s wrong:* In reality, decimal scoring introduces a continuous distribution between integer rings. Using proportional scaling of the maximum possible score is the standard statistical baseline used to equate tests or scoring systems when micro-level shot data for every historical competitor is unavailable.

*Original question: [Help with equalizing integer data with decimal data](https://stats.stackexchange.com/questions/677596/help-with-equalizing-integer-data-with-decimal-data) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
