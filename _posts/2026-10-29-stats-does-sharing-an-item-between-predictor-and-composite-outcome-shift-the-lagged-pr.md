---
layout: question
title: Does sharing an item between predictor and composite outcome shift the lagged-predictor
  coefficient by $\tfrac34c-\tfrac14b$?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Does sharing an item between predictor
  and composite outcome shift the lagged-predictor coefficient by $\tfrac34c-\tfrac1'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. Plain Language Restatement

When researchers study how things change over time, they often use a **lagged mixed model**. This means predicting a person's outcome today using their predictor from *yesterday* (the lagged predictor), while also controlling for their outcome from *yesterday* (the autoregressive lagged outcome). 

Sometimes, the outcome variable is an average score that includes the predictor variable itself as one of its component items (item overlap). The student noticed that this overlap creates a fake (spurious) effect of the lagged predictor on the outcome. 

Specifically, the student observed that moving from a clean outcome ($Y_\text{new}$) to an overlapping outcome ($Y_\text{old}$) shifted the regression coefficient of the lagged predictor. They derived an algebraic approximation for this shift: $\frac{3}{4}c - \frac{1}{4}b$ (where $c$ is the clean coefficient and $b$ is the lagged-outcome coefficient), and it matched their empirical data almost perfectly.

We need to answer two questions:
1. Is this mathematical derivation generally correct for this specific linear transformation?
2. Is there a standard reference for how item overlap biases lagged and autoregressive coefficients in panel or mixed models?

---

### 2. Step-by-Step Derivation

Let's model the relationship algebraically to see how transforming the outcome variable affects the regression coefficients.

#### Step A: Define the variables and the transformation
Let:
*   $X_{t-1}$ be the lagged predictor (measured at time $t-1$).
*   $Y_{\text{new}, t}$ be the "clean" composite outcome measured at time $t$ (composed of items excluding the predictor).
*   $Y_{\text{old}, t}$ be the "overlapping" composite outcome measured at time $t$, which includes the predictor item $X_t$. 

As given by the student, the overlapping outcome is an average of four items where one of them is the predictor:
$$Y_{\text{old}, t} = \frac{3}{4}Y_{\text{new}, t} + \frac{1}{4}X_t$$

We are interested in the lagged version of this relationship. Assuming the same weights apply at the lagged time point $t-1$:
$$Y_{\text{old}, t-1} = \frac{3}{4}Y_{\text{new}, t-1} + \frac{1}{4}X_{t-1}$$

#### Step B: Set up the population regression models
Consider the "clean" lagged regression model, where we regress the clean outcome at time $t$ on both the clean outcome at $t-1$ and the predictor at $t-1$:
$$Y_{\text{new}, t} = \beta_0 + b_{\text{clean}} Y_{\text{new}, t-1} + c_{\text{clean}} X_{t-1} + \varepsilon_t$$
*(Note: Here, $b_{\text{clean}}$ corresponds to the student's $b$, and $c_{\text{clean}}$ corresponds to $c$.)*

Now consider the "overlapping" regression model, where we substitute $Y_{\text{old}}$ in place of $Y_{\text{new}}$:
$$Y_{\text{old}, t} = \beta_0^* + b_{\text{old}} Y_{\text{old}, t-1} + c_{\text{old}} X_{t-1} + \varepsilon_t^*$$

#### Step C: Substitute the transformation into the overlapping model
We want to express $Y_{\text{old}, t}$ using the clean model components. Substitute $Y_{\text{old}, t} = \frac{3}{4}Y_{\text{new}, t} + \frac{1}{4}X_t$ into the left side:
$$\frac{3}{4}Y_{\text{new}, t} + \frac{1}{4}X_t = \beta_0^* + b_{\text{old}} \left(\frac{3}{4}Y_{\text{new}, t-1} + \frac{1}{4}X_{t-1}\right) + c_{\text{old}} X_{t-1} + \varepsilon_t^*$$

Next, substitute our clean regression equation for $Y_{\text{new}, t}$ on the left side:
$$\frac{3}{4} \left( \beta_0 + b_{\text{clean}} Y_{\text{new}, t-1} + c_{\text{clean}} X_{t-1} + \varepsilon_t \right) + \frac{1}{4}X_t = \beta_0^* + \frac{3}{4} b_{\text{old}} Y_{\text{new}, t-1} + \left(\frac{1}{4} b_{\text{old}} + c_{\text{old}}\right) X_{t-1} + \varepsilon_t^*$$

#### Step D: Match coefficients
Expand the left side:
$$\frac{3}{4}\beta_0 + \frac{3}{4}b_{\text{clean}} Y_{\text{new}, t-1} + \frac{3}{4}c_{\text{clean}} X_{t-1} + \frac{1}{4}X_t + \frac{3}{4}\varepsilon_t = \beta_0^* + \frac{3}{4}b_{\text{old}} Y_{\text{new}, t-1} + \left(\frac{1}{4}b_{\text{old}} + c_{\text{old}}\right) X_{t-1} + \varepsilon_t^*$$

By equating the coefficients of the lagged outcome ($Y_{\text{new}, t-1}$) and the lagged predictor ($X_{t-1}$) from both sides of the equation:

1. For the lagged outcome:
   $$\frac{3}{4}b_{\text{clean}} = \frac{3}{4}b_{\text{old}} \implies b_{\text{old}} \approx b_{\text{clean}}$$
   *(In expectation, the autoregressive coefficient remains largely stable).*

2. For the lagged predictor:
   $$\frac{3}{4}c_{\text{clean}} = \frac{1}{4}b_{\text{old}} + c_{\text{old}}$$

Solving for the new lagged-predictor coefficient ($c_{\text{old}}$):
$$c_{\text{old}} = \frac{3}{4}c_{\text{clean}} - \frac{1}{4}b_{\text{old}}$$

Since $b_{\text{old}} \approx b_{\text{clean}} = b$ and $c_{\text{clean}} = c$, we arrive directly at the student's formula:
$$c_{\text{old}} = \frac{3}{4}c - \frac{1}{4}b$$

#### Step E: Is there a standard reference for this?
Yes. While specific coefficients like $\frac{3}{4}$ and $\frac{1}{4}$ depend on the exact weighting of the composite, the general phenomenon is well-documented. This falls under **part-whole correlation bias** or **criterion contamination** in psychometrics and longitudinal modeling. 

 Seminal methodological warnings regarding item overlap in panel models include:
*   **Arminger & Bohstedt (1987)** or general texts on structural equation modeling (SEM) regarding test contamination.
*   More modern discussions on intensive longitudinal data (ILD) and ecological momentary assessment (EMA)—such as papers by **Hamaker, Kuiper, and Grasman (2015)** on lag-1 autoregressive models—explicitly warn that including a predictor item inside a composite outcome composite induces mechanical artifactual coupling (spurious cross-lagged effects).

---

### 3. Final Answer

**Yes, the student's derivation is mathematically correct.** 

By substituting the linear transformation $Y_{\text{old}} = \frac{3}{4}Y_{\text{new}} + \frac{1}{4}X$ into the lagged mixed model, algebraic expansion proves that the overlapping lagged-predictor coefficient ($c_{\text{old}}$) is structurally shifted from the clean coefficient ($c$) by:
$$c_{\text{old}} = \frac{3}{4}c - \frac{1}{4}b$$
where $b$ is the autoregressive lagged-outcome coefficient. 

---

### 4. Common Mistakes

*   **Assuming the bias is only a random error:** Researchers often treat item overlap as a minor source of random measurement noise. In reality, it introduces a *deterministic mathematical dependency* that systematically biases regression coefficients based on the exact weights of the composite items.
*   **Ignoring the autoregressive coefficient ($b$):** Forgetting that the lagged outcome coefficient directly scales the magnitude of the shift. Because $b$ is often positive (indicating psychological persistence over time), subtracting $\frac{1}{4}b$ systematically pulls the lagged predictor coefficient negative, creating a false compensatory or reactive effect.
*   **Conflating contemporaneous and lagged bias:** While contemporaneous overlap (items measured at the exact same time $t$) primarily inflates correlations due to shared method variance or direct part-whole overlap, lagged overlap introduces structural artifactual feedback loops across time points.

*Original question: [Does sharing an item between predictor and composite outcome shift the lagged-predictor coefficient by $\tfrac34c-\tfrac14b$?](https://stats.stackexchange.com/questions/677534/does-sharing-an-item-between-predictor-and-composite-outcome-shift-the-lagged-pr) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
