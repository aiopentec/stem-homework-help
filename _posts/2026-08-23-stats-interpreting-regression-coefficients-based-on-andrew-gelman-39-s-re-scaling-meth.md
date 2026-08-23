---
layout: post
title: Interpreting regression coefficients based on Andrew Gelman&#39;s re-scaling
  method
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

You have a **binary outcome** (logistic regression) and two **predictors**  

| predictor | original form | after Gelman‑style scaling |
|-----------|---------------|----------------------------|
| **XCONT** (continuous) | raw units | **XCONT / 1 SD** (so a one‑unit change = 1 SD increase) |
| **XBIN** (binary)      | 0 / 1        | recoded **–1 / +1** (so a one‑unit change = a change from –1 to +1, i.e. a jump of 2 raw units) |

The student wants to **compare the two coefficients** that appear in the same logistic model and to understand why, in a second scenario, each predictor is “significant” when run alone but not when they are together.

The answer must explain:

1. How to interpret the coefficients after this particular scaling.  
2. How to compare the size of the two effects.  
3. Why the significance pattern can change when the predictors are entered jointly.  

---

## 2.  Step‑by‑step interpretation  

### 2.1  The logistic model after scaling  

\[
\log\frac{p}{1-p}= \beta_0 + \beta_1\,\underbrace{\frac{X_{\text{CONT}}}{\sigma_X}}_{\text{scaled cont.}} 
                     + \beta_2\,\underbrace{X_{\text{BIN}}^{*}}_{\text{–1 / +1}}
\]

* \(p = \Pr(Y=1\mid X)\).  
* \(\beta_1\) = change in **log‑odds** for a **one‑SD increase** in the original continuous predictor.  
* \(\beta_2\) = change in **log‑odds** for a **change of 2 units** on the recoded binary scale (i.e. going from –1 to +1).  

If you want the effect of flipping the original 0/1 binary variable, you must **divide \(\beta_2\) by 2**, because the coding stretch doubled the distance between the two categories.

---

### 2.2  Scenario 1 – both predictors significant in the same model  

| coefficient | estimate | SE | z | p‑value | odds‑ratio (OR) | interpretation |
|-------------|----------|----|---|---------|----------------|----------------|
| \(\beta_0\) (intercept) | –1.8197 | 0.1761 | –10.33 | \< 2e‑16 | \(\exp(-1.8197)=0.162\) | When **XCONT = 0 (i.e. at its mean)** and **XBIN = –1** (the “reference” group), the odds of Y=1 are 0.162 (probability ≈ 14 %). |
| \(\beta_1\) (XCONT) | **0.3175** | 0.1190 | 2.667 | **0.0076** | \(\exp(0.3175)=1.37\) | **A one‑SD increase** in the original continuous predictor multiplies the odds of Y=1 by **1.37** (≈ 37 % higher). |
| \(\beta_2\) (XBIN) | **1.0845** | 0.3564 | 3.043 | **0.0023** | \(\exp(1.0845)=2.96\) | A change from **–1 to +1** (i.e. from the original 0 to 1) multiplies the odds by **2.96**.  If you prefer the effect of the original 0→1 change, halve the coefficient: \(\beta_2/2 = 0.5423\); the corresponding OR is \(\exp(0.5423)=1.72\). |

#### 2.2.1  Comparing the two effects  

* **Continuous predictor:** per SD increase → OR = 1.37.  
* **Binary predictor (original coding):** 0→1 change → OR = 1.72.  

Thus, after putting the predictors on a comparable scale, the binary predictor still has a larger effect on the odds of Y = 1, but the continuous predictor is not negligible—it raises the odds by about one‑third of an SD.

You can also report the **standardised log‑odds effects** (the β’s themselves) as a “size” measure because they are now on roughly the same metric (one SD vs. a two‑unit binary jump).  
* \(|\beta_1| = 0.317\)  
* \(|\beta_2| = 1.084\)  

Since \(|\beta_2| > |\beta_1|\), the binary predictor has roughly three times the *log‑odds* impact of a one‑SD change in the continuous predictor.

---

### 2.3  Scenario 2 – each predictor is significant alone but not jointly  

| Model | Predictor(s) | Coefficient (β) | SE | z | p |
|-------|--------------|-----------------|----|---|---|
| **Model A (XCONT only)** | XCONT | significant (e.g. β≈0.30) | … | … | < 0.05 |
| **Model B (XBIN only)** | XBIN  | significant (e.g. β≈1.10) | … | … | < 0.05 |
| **Model C (both)** | XCONT + XBIN | both p > 0.05 | … | … | non‑sig |

#### Why does this happen?  

1. **Collinearity (shared variance)**  
   * If the two predictors are **correlated**, each explains part of the same variation in the outcome. When you fit them *separately* the entire shared variation is credited to the single predictor, giving a “significant” coefficient.  
   * When you fit them *together*, the model tries to apportion the shared variation between them. Because the information is split, the **standard errors inflate** and the individual *partial* effects may no longer reach significance.

2. **Statistical illustration**  

   *Compute the correlation (or, for a binary–continuous pair, the point‑biserial correlation).*
   ```r
   cor(mat0$XCONT, mat0$XBIN)   # e.g. 0.45
   ```
   A correlation around 0.4–0.5 is enough to cause the described pattern.

   *Check variance inflation factors (VIF):*  

   ```r
   library(car)
   vif(glm(YBIN ~ XCONT + XBIN, family = binomial, data = mat0))
   ```
   VIF values > 2–3 suggest moderate collinearity; values > 5 are a red flag.

3. **What the scaling does (or does not) do**  
   Gelman’s scaling makes the **units comparable**, but it does **not** remove collinearity. If the two predictors are truly measuring related concepts (e.g., “age” and “has chronic disease”), the joint model will naturally show larger standard errors.

4. **What to report / how to proceed**  

   * **Report both models** (separate and joint) and comment on the correlation.  
   * If the scientific question is “does either predictor matter?” you can keep the joint model and note that **neither predictor is uniquely predictive after adjusting for the other**.  
   * If you need to *compare* their relative importance, consider **regularised models** (ridge, lasso) or **dominance analysis**, but be clear that the apparent “significance” when run alone is **inflated** by omitted‑variable bias.

---

## 3.  Final take‑away answers  

### 3.1  Interpretation of the coefficients (Scenario 1)

* **Continuous predictor (scaled by 1 SD)**  
  *β₁ = 0.3175* → a **one‑SD increase** in the original variable multiplies the odds of Y = 1 by **exp(0.3175) ≈ 1.37** (≈ 37 % higher).  

* **Binary predictor (re‑coded –1 / +1)**  
  *β₂ = 1.0845* → moving from –1 to +1 (i.e. from the original 0 to 1) multiplies the odds by **exp(1.0845) ≈ 2.96**.  
  *If you want the effect of the original 0→1 change, divide the coefficient by 2:*  
  \[
  \beta_{2,\;0\to1}= \frac{1.0845}{2}=0.5423,\qquad \text{OR}=e^{0.5423}=1.72.
  \]

Thus the binary predictor has a larger impact on the odds than a one‑SD change in the continuous predictor, but both are statistically significant and contribute independently.

### 3.2  Why the “both non‑significant together” pattern (Scenario 2) occurs  

* The two predictors are **correlated** (shared variance).  
* When each is entered **alone**, the full shared effect is attributed to that predictor → significant coefficient.  
* When entered **together**, the model estimates each *partial* effect; the standard errors increase, and the p‑values can rise above the conventional 0.05 threshold.  

The scaling does not eliminate this issue; it only makes the magnitude of the coefficients easier to compare.

---

## 4.  Common Mistakes  

| Mistake | Why it’s wrong | Correct approach |
|---------|----------------|------------------|
| **Treating the binary coefficient as the effect of a 0→1 change** | After recoding to –1/+1 the coefficient refers to a **2‑unit** change. | Divide the binary coefficient by 2 (or multiply the OR by \(\sqrt{}\) accordingly) before interpreting a 0→1 shift. |
| **Comparing raw β’s without remembering the scaling** | A β for a continuous predictor (per SD) is not on the same scale as a β for a binary predictor (per 2‑unit change). | Remember the “per‑SD” vs. “per‑2‑units” meaning; optionally rescale the binary β to a per‑unit (0→1) effect. |
| **Assuming that significance in separate models proves importance in the joint model** | Omitted‑variable bias inflates the apparent effect when the other predictor is left out. | Check the correlation between predictors, compute VIFs, and interpret joint‑model coefficients as *partial* effects. |
| **Reporting only the odds‑ratio without the reference change** | Readers may think the OR refers to a 0→1 change for the binary predictor when it actually refers to a –1→+1 change. | Clearly state the coding scheme and, if useful, present both the “full” OR (for –1→+1) and the “original‑scale” OR (for 0→1). |
| **Thinking that Gelman’s scaling “standardizes” the model** | It makes the **units** comparable but does **not** give a true *standardised* coefficient (which would also adjust for the residual variance). | Use Gelman scaling for rough comparison; for a fully standardised logistic coefficient you would need additional transformations (e.g., divide by the residual SD of the latent variable). |

--- 

**Bottom line:** After Gelman‑style scaling, a logistic coefficient for a continuous

*Original question: [Interpreting regression coefficients based on Andrew Gelman&#39;s re-scaling method](https://stats.stackexchange.com/questions/345002/interpreting-regression-coefficients-based-on-andrew-gelmans-re-scaling-method) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
