---
layout: question
title: Time course experiment - which statistical analysis fits best?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Time course experiment - which statistical
  analysis fits best?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is being asked to do (plain language)

The student has measured the amount of protein X on Western blots for **two** experimental factors  

| Factor | Levels | Replicates per level |
|--------|--------|----------------------|
| **Treatment** | Control, Drug | 3 wells each |
| **Incubation time** | 30 min, 1 h, 2 h, 3 h | 3 wells each (per treatment) |

All wells come from the same organ lysate, so the only source of variation is the *technical* variability between wells.

The student wants to know how to test three questions:

1. **Overall drug effect** – does the drug change protein X irrespective of time?
2. **Overall time effect** – does protein X change with incubation time irrespective of drug?
3. **Interaction** – does the drug effect depend on the incubation time (i.e., does the drug work differently at 30 min vs 3 h)?

The appropriate statistical tool for simultaneously answering these three questions is a **two‑way (factorial) ANOVA** (analysis of variance) with the factors *Treatment* and *Time* and their interaction.

---

## 2. Step‑by‑step solution  

Below each step we give the *what* (action) and the *why* (reason).

### Step 0 – Organise the data

Create a table (or a spreadsheet) with one row per well:

| Well | Treatment | Time (h) | Protein X (raw intensity) |
|------|-----------|----------|---------------------------|
| 1 | Control | 0.5 |  … |
| 2 | Control | 0.5 |  … |
| 3 | Control | 0.5 |  … |
| 4 | Drug    | 0.5 |  … |
| … | … | … | … |
| 24| Drug    | 3   |  … |

There are **24 observations** (4 × 2 × 3).

> **Tip** – If the Western‑blot intensities span several orders of magnitude, take a log‑transform (e.g. `log10(intensity)`) before analysis; this often improves normality and variance homogeneity.

### Step 1 – Check ANOVA assumptions  

ANOVA assumes that, **within each combination of factors**, the residuals are

| Assumption | How to check (in R) |
|------------|---------------------|
| **Normality** | `shapiro.test(residuals(lm))` or a Q‑Q plot (`qqnorm`, `qqline`) |
| **Equal variances (homoscedasticity)** | `plot(lm, which = 1)` (residuals vs fitted) or Levene’s test: `car::leveneTest(Y ~ Treatment*Time)` |
| **Independence** | Design ensures wells are independent (no repeated measures). |

If the assumptions are seriously violated (e.g., Shapiro p < 0.01 and strong skew), either:

* Transform the data (log, square‑root), or  
* Use a *non‑parametric* factorial method such as the **Aligned Rank Transform (ART)** ANOVA (`ARTool::art` in R).

For the remainder we assume the assumptions are reasonably met (or that a log‑transform fixed them).

### Step 2 – Fit the two‑way ANOVA model  

The linear model is  

\[
Y_{ijk}= \mu \;+\; \alpha_i \;+\; \beta_j \;+\; (\alpha\beta)_{ij} \;+\; \varepsilon_{ijk}
\]

* \(Y_{ijk}\) = protein level in well *k* of treatment *i* and time *j*  
* \(\mu\) = overall mean  
* \(\alpha_i\) = effect of treatment (i = Control, Drug)  
* \(\beta_j\) = effect of time (j = 0.5, 1, 2, 3 h)  
* \((\alpha\beta)_{ij}\) = interaction term (does drug effect depend on time?)  
* \(\varepsilon_{ijk}\) = random error (assumed \(N(0,\sigma^2)\))

In R:

```r
# assume the data frame is called df and the response column is called X
df$Treatment <- factor(df$Treatment)      # two levels
df$Time      <- factor(df$Time)           # four levels

# optional log‑transform
df$logX <- log10(df$X)

model <- aov(logX ~ Treatment * Time, data = df)   # or aov(X ~ ...) if no transform
summary(model)
```

The `summary` table gives three *F‑tests*:

| Source | df (numerator) | df (denominator) | F value | p‑value |
|--------|----------------|------------------|--------|---------|
| Treatment | 1 | 18 | … | … |
| Time      | 3 | 18 | … | … |
| Treatment:Time | 3 | 18 | … | … |
| Residual  | 16 | — | — | — |

*(df for residual = total n – number of parameters = 24 – (1 + 1 + 3 + 1) = 16)*

### Step 3 – Interpret the three tests  

| Question | Null hypothesis (H₀) | What a **significant** p‑value (typically < 0.05) means |
|----------|---------------------|----------------------------------------------------------|
| **Treatment main effect** | The average protein level is the same for Control and Drug **after averaging over all times**. | The drug changes protein X on average (regardless of time). |
| **Time main effect** | All four time points have the same mean (after averaging over treatment). | Protein X changes with incubation time (regardless of drug). |
| **Interaction** | The difference between Drug and Control is the **same** at every time point. | The drug effect **depends** on incubation time – e.g., it may be strong at 2 h but weak at 30 min. |

*If the interaction is **significant**, the main‑effect p‑values are less informative; you should explore the simple effects (drug vs control) **within each time**.*

### Step 4 – Post‑hoc / simple‑effects analysis (if needed)

**Scenario A – Interaction NOT significant**  
You can report the two main effects and stop there.

**Scenario B – Interaction significant**  

1. **Simple‑effect t‑tests** (or one‑way ANOVAs) for each time point:  

   ```r
   library(emmeans)
   em <- emmeans(model, ~ Treatment | Time)   # means per time
   pairs(em)                                   # drug vs control at each time
   ```

2. **Adjust for multiple testing** (e.g., Tukey’s HSD) because you are making four comparisons.  

   ```r
   contrast(em, method = "pairwise", adjust = "tukey")
   ```

3. Optionally plot the interaction:

   ```r
   library(ggplot2)
   ggplot(df, aes(x = Time, y = logX, colour = Treatment, group = Treatment)) +
     stat_summary(fun = mean, geom = "point", size = 3) +
     stat_summary(fun = mean, geom = "line") +
     stat_summary(fun.data = mean_se, geom = "errorbar", width = .2)
   ```

The plot visually shows whether the two lines are parallel (no interaction) or cross/diverge (interaction).

### Step 5 – Report the results  

A typical write‑up (using log‑transformed data) might look like:

> A two‑way ANOVA was performed on log₁₀‑transformed protein X levels with *Treatment* (Control vs Drug) and *Incubation time* (0.5, 1, 2, 3 h) as fixed factors. The interaction was significant, **F(3,16) = 5.42, p = 0.009**, indicating that the drug effect differed across time points. Simple‑effect comparisons (Tukey‑adjusted) showed that the drug significantly increased protein X at 2 h (p = 0.003) and 3 h (p = 0.021) but not at 30 min or 1 h (p > 0.10). The main effect of *Time* was also significant, **F(3,16) = 8.73, p = 0.001**, reflecting a general increase of protein X with longer incubation. The main effect of *Treatment* was not significant after accounting for the interaction (**F(1,16) = 2.01, p = 0.17**).

If the interaction were non‑significant, you would instead report the two main effects and their p‑values.

### Step 6 – Caveats about the experimental design  

* All wells originate from a **single organ**; therefore the data represent **technical replicates**, not biological replicates. The inference you can draw is limited to “the assay can detect a change under these laboratory conditions.”  
* If you later obtain lysates from *different* animals, you would treat **Animal** as a random factor and use a **mixed‑effects model** (e.g., `lmer(logX ~ Treatment*Time + (1|Animal))`).  
* With only **n = 3 per cell**, the ANOVA has low power; a non‑significant result does **not** prove there is no effect – it may simply be undetectable with this sample size.

---

## 3. Final answer (concise)

| Question | Recommended test | What the test tells you |
|----------|------------------|------------------------|
| Overall drug effect (ignoring time) | **Two‑way ANOVA** – main effect of *Treatment* | Whether the drug changes protein X on average. |
| Overall time effect (ignoring drug) | **Two‑way ANOVA** – main effect of *Time* | Whether protein X changes with incubation time. |
| Does drug effect vary with time? | **Two‑way ANOVA** – *Treatment × Time* interaction | Whether the drug’s impact is different at the various time points. |
| If the interaction is significant | **Post‑hoc simple‑effects** (pairwise comparisons of Drug vs Control at each time, Tukey‑adjusted) | Which specific times show a drug effect. |

The complete workflow:

1. Log‑transform the intensity (if needed).  
2. Verify normality and equal variances.  
3. Fit `aov(Y ~ Treatment * Time)`.  
4. Inspect the three F‑tests (Treatment, Time, Interaction).  
5. If Interaction = significant → run `emmeans`/Tukey post‑hoc for each time.  
6. Summarise results with F‑values, p‑values, and effect‑size estimates (e.g., η²).

---

## 4. Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | How to fix it |
|---------|----------------|---------------|
| **Treating the 24 wells as independent biological replicates** | All wells come from the *same* organ, so they only reflect assay variability, not animal‑to‑animal variation. | State clearly that the analysis is on technical replicates; plan a follow‑up with true biological replicates. |
| **Running three separate one‑way ANOVAs (Treatment, Time, Interaction)** | Inflates Type I error and ignores the factorial structure; you lose the ability to test interaction properly. | Use a single two‑way ANOVA that simultaneously evaluates both main effects and the interaction. |
| **Ignoring the interaction when it is significant** | The main‑effect p‑values become misleading; you might claim a “drug effect” that only exists at certain times. | When the interaction term is significant, focus on simple‑effects (drug vs control at each time) and report those. |
| **Not checking assumptions** | ANOVA’s p‑values are unreliable if residuals are highly non‑normal or variances are unequal. | Plot residuals, run Shapiro‑Wilk and Levene’s tests; transform data or use a non‑parametric ART‑ANOVA if assumptions fail. |
| **Using the raw Western‑blot intensities without normalization** | Loading differences or background can create systematic bias. | Normalize each lane to a loading control (e.g., β‑actin) and use the normalized values as the response variable. |
| **Reporting only “p < 0.05” without effect size** | Statistical significance does not convey biological relevance, especially with small n. | Report effect sizes (η² for

*Original question: [Time course experiment - which statistical analysis fits best?](https://stats.stackexchange.com/questions/677078/time-course-experiment-which-statistical-analysis-fits-best) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
