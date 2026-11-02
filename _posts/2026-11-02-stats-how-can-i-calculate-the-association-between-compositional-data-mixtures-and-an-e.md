---
layout: question
title: How can I calculate the association between compositional data (mixtures) and
  an external variable?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: How can I calculate the association
  between compositional data (mixtures) and an external variable?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. Restatement of the Problem in Plain Language

You have a dataset where every individual is described by a set of proportions (e.g., Archetype A = 70%, B = 20%, C = 10%) that **always sum to 1** (or 100%). This type of data is known as **compositional data**. 

You want to know how these mixtures relate to an **external variable** (such as hours of sleep per week). 

Standard statistical approaches—like running three separate correlation tests for A, B, and C against sleep duration—fail for two main reasons:
1. **The Closure Problem:** Because the proportions must sum to 1, they are not independent. If Archetype A goes up, B or C *must* go down. This creates spurious correlations.
2. **The Aggregation Problem:** An external variable might relate to a conceptual trait that spans *multiple* archetypes (e.g., "high coffee consumption" is represented by both Archetype A and Archetype C). Analyzing archetypes strictly one-by-one can mask these underlying relationships.

The goal is to properly model the relationship between a multi-part compositional mixture and an external continuous variable while accounting for the geometry of simplex (compositional) data.

---

### 2. Step-by-Step Solution

To solve this correctly, we will use **Log-Ratio Analysis (specifically, Isometric Log-Ratio or Additive Log-Ratio transformations)** combined with **multivariate regression**, which transforms constrained data into unconstrained real space where standard statistical tools apply.

#### Step 1: Understand the Geometry of Compositional Data (The Simplex)
Data that sums to a constant lives on a constrained space called the **Simplex**. Let $\mathbf{x} = (x_1, x_2, x_3)$ be an individual's proportions such that:
$$x_1 + x_2 + x_3 = 1 \quad \text{and} \quad x_i > 0$$
Standard statistical techniques (like Pearson correlation or ordinary least squares regression) assume data can range from $-\infty$ to $+\infty$. Applying them directly to the raw proportions violates these assumptions due to the constant-sum constraint.

#### Step 2: Apply a Log-Ratio Transformation (Aitchison Geometry)
To remove the constraint, we map the compositions from the simplex to standard Euclidean space using log-ratios. 

While the **Additive Log-Ratio (ALR)** uses one archetype as a denominator, the **Isometric Log-Ratio (ILR)** transformation creates an orthogonal coordinate system. For $D$ parts (here, $D = 3$ archetypes), we can define $D-1$ orthonormal log-contrast coordinates, denoted as $z_1$ and $z_2$.

Using the ALR approach for simplicity, we choose one archetype (say, Archetype C) as the reference denominator and take natural logarithms of the ratios:
$$y_1 = \ln\left(\frac{A}{C}\right) = \ln(A) - \ln(C)$$
$$y_2 = \ln\left(\frac{B}{C}\right) = \ln(B) - \ln(C)$$

*(Note: If your PCHA output yields exact zeros, you must apply a small imputation method for zeros before taking logarithms, though PCHA vertices usually yield strictly positive interior points for mixtures).*

Now, $y_1$ and $y_2$ are unconstrained real numbers ($\in (-\infty, +\infty)$). 

#### Step 3: Run a Multivariate or Multiple Regression Model
Let $Y$ be your external variable (e.g., hours of sleep per week). Because $y_1$ and $y_2$ capture the *entire* relative composition of the individual, you can now safely use standard **Multiple Linear Regression**:

$$Y = \beta_0 + \beta_1 y_1 + \beta_2 y_2 + \epsilon$$

Where:
* $\beta_0$ is the intercept.
* $\beta_1$ and $\beta_2$ are the regression coefficients for the log-ratios.
* $\epsilon$ is the error term.

By fitting this model, you test whether the *entire composition* (relative to Archetype C) is significantly associated with sleep duration using an overall $F$-test on the regression model.

#### Step 4: Address the Aggregation Problem (Combining Archetypes)
You noted that sleep duration might relate to "high coffee consumption," which is split across Archetypes A and C. 

Because log-ratio transformations preserve the relative geometry, you can easily redefine your basis if needed, or inspect the coefficients. However, a more direct way to test specific hypotheses (like $A + C$ vs. $B$) is to use **manual pairwise combinations** or **Principal Balances** within the ILR framework:
* **Balance 1 ($z_1$):** Contrasts the "high consumption" group $(A + C)$ against the "low consumption" group $(B)$:
  $$z_1 = \sqrt{\frac{2}{3}} \ln\left(\frac{\sqrt{A \cdot C}}{B}\right)$$
* **Balance 2 ($z_2$):** Contrasts good quality $(A)$ against poor quality $(C)$ *within* the high-consumption group:
  $$z_2 = \frac{1}{\sqrt{2}} \ln\left(\frac{A}{C}\right)$$

When you put these custom balances into your regression model:
$$Y = \gamma_0 + \gamma_1 z_1 + \gamma_2 z_2 + \epsilon$$
* $\gamma_1$ directly tests your hypothesis: **Does total consumption ($(A+C)$ vs. $B$) associate with sleep?**
* $\gamma_2$ tests: **Does the quality of that consumption ($A$ vs. $C$) associate with sleep?**

---

### 3. Final Answer

To rigorously calculate the association between compositional archetype mixtures and an external variable:

1. **Do not use raw proportions** with Pearson/Spearman correlations or standard regressions, as the sum-to-one constraint causes severe statistical bias.
2. **Transform the proportions** using log-ratios (specifically Isometric Log-Ratios or custom balances) to map the constrained simplex data into unconstrained real space.
3. **Use Multiple Linear Regression** using these log-ratio coordinates as predictors for your external variable.
4. **Design custom balances** (orthogonal log-ratios) if you want to explicitly test aggregated hypotheses, such as grouping Archetypes A and C together to test a broader behavioral trait against Archetype B.

---

### 4. Common Mistakes

* **Treating proportions as independent variables:** Running three separate simple linear regressions (Sleep vs. A, Sleep vs. B, Sleep vs. C) ignores the constraint that $A+B+C=1$, often resulting in false positives or completely distorted coefficient signs.
* **Forgetting zeros:** If any individual has a true 0% proportion for an archetype, taking $\ln(0)$ yields $-\infty$. Failing to handle boundary zeros via proper compositional replacement methods will break the model.
* **Ignoring the choice of denominator:** In standard log-ratios, the choice of denominator matters. Ensure interpretation is framed *relative* to the chosen baseline archetype, unless you are using orthonormal balances (ILR) that average out reference-frame bias.
* **Forcing linear models on untransformed data:** Assuming that a 10% increase in Archetype A has the same absolute meaning whether an individual started at 5% or 80% (ignoring the multiplicative, relative nature of mixtures).

*Original question: [How can I calculate the association between compositional data (mixtures) and an external variable?](https://stats.stackexchange.com/questions/677623/how-can-i-calculate-the-association-between-compositional-data-mixtures-and-an) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
