---
layout: question
title: Which estimand better fits the matched pair design within units? ATT or ATE
  (Conditional or Local ATE?)
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Which estimand better fits the matched
  pair design within units? ATT or ATE (Conditional or Local ATE?)'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking – restated in plain language  

The student has an observational study in which **each site contains two plots**:  

* one plot that is “treated’’ (adjacent to land‑use type 1)  
* one plot that is “control’’ (adjacent to land‑use type 2).  

The sites were **chosen** because they have *both* land‑use types, not because they were *only* treated or only untreated.  

The student wants to know which causal estimand is appropriate for the analysis:

| Option | Rough meaning |
|--------|----------------|
| **ATT** (Average Treatment effect on the Treated) | Effect that would be observed **only for the units that actually received the treatment** (here, the treated plots). |
| **ATE** (Average Treatment Effect) | Effect averaged over **all units in a well‑defined population** (here, all plots that could possibly appear, treated or not). |
| **Conditional (or “local’’) ATE** | Effect averaged over the *sub‑population that has the same pre‑treatment covariates* as the observed sample (e.g., the set of sites that satisfy the geographic and climatic constraints used for sampling). |

Because the design pairs a treated and a control plot **within the same site**, the student wonders whether the estimand is automatically an ATT, a (sample) ATE, or a conditional ATE that only applies to sites with the same geoclimatic characteristics.

---

## 2. Step‑by‑step reasoning  

### Step 1 – Write down the potential‑outcome (Rubin) framework  

For each **plot** \(i\) we denote  

* \(Y_i(1)\) – outcome we would observe if the plot were treated (adjacent to land‑use 1)  
* \(Y_i(0)\) – outcome we would observe if the plot were control (adjacent to land‑use 2)  

The **observed** outcome is  

\[
Y_i = Z_i Y_i(1) + (1-Z_i) Y_i(0),
\]

where \(Z_i\in\{0,1\}\) indicates treatment (1 = treated).

Because plots are nested inside sites, let \(s(i)\) denote the site that contains plot \(i\).  
Within each site we have exactly one treated plot \((Z_i=1)\) and one control plot \((Z_i=0)\).  

### Step 2 – Define the three candidate estimands  

| Estimand | Formal definition (finite‑sample version) | Population it refers to |
|----------|--------------------------------------------|--------------------------|
| **ATT** | \(\displaystyle \tau_{\text{ATT}} = \frac{1}{N_T}\sum_{i:Z_i=1}\bigl\{Y_i(1)-Y_i(0)\bigr\}\) | The **treated** plots only (the “treated’’ side of each pair). |
| **ATE** | \(\displaystyle \tau_{\text{ATE}} = \frac{1}{N}\sum_{i=1}^{N}\bigl\{Y_i(1)-Y_i(0)\bigr\}\) | **All** plots that could belong to the target population (treated + control). |
| **Conditional (local) ATE** | \(\displaystyle \tau_{\text{CATE}}(x) = \mathbb{E}\!\big[\,Y(1)-Y(0)\mid X=x\,\big]\) where \(X\) are the pre‑treatment covariates used for sampling (geoclimatic, landscape, etc.). In a finite sample it is the average treatment effect **within the sub‑sample that shares the observed covariate pattern**. | The sub‑population that satisfies the same **site‑selection criteria** as the observed sample. |

### Step 3 – Examine how the sample was generated  

* **Selection rule**: Choose *sites* that contain *both* land‑use types.  
* Within each selected site, we observe **both** a treated and a control plot.  
* The selection rule does **not** depend on whether a site is “treated’’ or “control’’ (both exist in every selected site).  
* The rule *does* depend on **geoclimatic and landscape characteristics** (e.g., elevation, precipitation). Those characteristics are the same for the treated and control plot inside a site, and they are the only source of variation across sites.

Thus the sample is **conditional on** a set of covariates \(X\). The sample does **not** preferentially pick treated plots; it picks *pairs* of plots that satisfy the covariate constraints.

### Step 4 – Determine which estimand the data naturally identify  

Because every selected site contributes **one treated** and **one control** plot, the **pairwise difference**  

\[
D_s = Y_{s,T} - Y_{s,C}
\]

is an unbiased estimator of the **site‑specific treatment effect**  

\[
\tau_s = Y_{s,T}(1) - Y_{s,C}(0),
\]

provided the **stable unit treatment value assumption (SUTVA)** holds within a site (no interference between the two plots) and the **conditional ignorability** assumption holds **given the covariates that are constant within a site** (i.e., after conditioning on the site‑level covariates, treatment assignment is as‑if random).  

Taking the average of the pairwise differences over all sampled sites gives

\[
\widehat{\tau}_{\text{pair}} = \frac{1}{S}\sum_{s=1}^{S} D_s .
\]

What does \(\widehat{\tau}_{\text{pair}}\) estimate?

* It is **not** an ATT, because ATT would weight each *treated* plot equally and would ignore the control‑only plots. In our data every treated plot has a matched control, so the ATT is exactly the same numerical average *if* we average only over treated plots **and** use the *same* control outcomes that belong to the same sites. However, the ATT definition does **not** condition on the covariate restrictions that generated the sample; it implicitly averages over *all* treated plots in the broader population (including sites that do **not** satisfy the selection rule).  
* It **is** a **conditional (local) ATE**: the average effect over the *sub‑population of sites that meet the geoclimatic/landscape constraints*. Formally,  

\[
\tau_{\text{CATE}} = \mathbb{E}\!\big[\,Y(1)-Y(0)\mid X\in\mathcal{X}_\text{sample}\,\big],
\]

where \(\mathcal{X}_\text{sample}\) denotes the region of covariate space used for sampling.  
* It can also be described as the **sample ATE** (the finite‑sample average treatment effect) **within that restricted sample**. In finite‑sample notation:  

\[
\tau_{\text{sample}} = \frac{1}{2S}\sum_{s=1}^{S}\bigl\{Y_{s,T}(1)-Y_{s,T}(0) + Y_{s,C}(1)-Y_{s,C}(0)\bigr\}
                 = \frac{1}{S}\sum_{s=1}^{S} D_s,
\]

because the control plot’s potential outcome under treatment, \(Y_{s,C}(1)\), is never observed but cancels out under the pairing design.

Hence the **identifiable estimand** is the *average treatment effect conditional on the covariates used for site selection*.

### Step 5 – When can we reinterpret it as an ATT or a broader ATE?  

* **If** the investigator is willing to assume that the **conditional effect** does **not vary** with the covariates (i.e., homogeneous treatment effect), then  

\[
\tau_{\text{CATE}} = \tau_{\text{ATE}} = \tau_{\text{ATT}} .
\]

In that special case the distinction is moot, but the assumption is strong and must be justified.

* **If** external data are available that describe the distribution of the covariates in the *full* target population (all sites, not only those with both land‑use types), one could **re‑weight** the conditional ATE to obtain an estimate of the population ATE (or ATT). The re‑weighting formula is the standard IPW or g‑formula:

\[
\tau_{\text{ATE}} = \frac{\displaystyle\sum_{s} w_s D_s}{\displaystyle\sum_{s} w_s},
\qquad 
w_s = \frac{P_{\text{pop}}(X_s)}{P_{\text{sample}}(X_s)} .
\]

Absent such re‑weighting, the most honest description is *conditional ATE*.

### Step 6 – Summarise the answer to the original question  

| Question | Answer |
|----------|--------|
| **Is the estimand an ATT?** | **No**, because the sample was not drawn by selecting *treated* sites only; it was drawn by selecting sites that satisfy certain covariate constraints and contain both a treated and a control plot. |
| **Is it a (sample) ATE?** | **Yes**, but only **within the restricted covariate space** used for sampling. This is often called the *conditional* or *local* ATE. |
| **Does it generalise to other sites with the same geoclimatic/landscape characteristics?** | Yes, under the assumption that the treatment effect is **exchangeable** for all sites sharing those covariates. The estimand is the average effect **among sites that fall in the same covariate region** as the observed sample. |
| **Can it be interpreted as the usual population ATE or ATT?** | Only with additional assumptions (effect homogeneity) or with re‑weighting using external information about the full population’s covariate distribution. |

---

## 3. Final answer  

The paired‑plot design yields an estimator that is **the average treatment effect conditional on the site‑level covariates used to select the sample** (the “conditional ATE’’ or “local ATE’’). It is not an ATT because the sampling scheme does not preferentially select treated sites; it is also not the unrestricted population ATE unless one imposes a homogeneity assumption or applies external re‑weighting. Consequently, the causal claim that can be made is:

> *“Among sites that satisfy the same geoclimatic and landscape constraints as those in the study, the average effect of changing the adjacent land‑use from type 2 to type 1 is \(\widehat{\tau}_{\text{pair}}\).”*

---

## 4. Common mistakes for this type of problem  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Calling the estimand ATT because the data contain treated plots.** | ATT refers to *all* treated units in the target population, not just the treated units that happen to appear in a sample selected on other criteria. | Verify the sampling frame: if units are selected *independently* of treatment status, ATT is not the natural estimand. |
| **Equating “sample ATE’’ with the population ATE without justification.** | The sample may be a non‑random slice of the population (e.g., restricted to a narrow climatic zone). | Explicitly state the conditioning set \(\mathcal{X}_\text{sample}\) and discuss whether you can assume transportability. |
| **Ignoring the matching/pairing structure and averaging treated and control outcomes separately.** | The paired design creates a *difference estimator* that directly targets the average effect *within each pair*. Averaging separately can re‑introduce bias if the pairwise balance is not respected. | Use the within‑pair difference (or a matched‑pair regression) as the primary estimator. |
| **Assuming SUTVA automatically holds because plots are in the same site.** | There can be spill‑over (e.g., water flow, species movement) from the treated to the control plot. | Examine the scientific context; if interference is plausible, consider hierarchical or spatial models that relax SUTVA. |
| **Treating covariates that are constant within a site as “plot‑level’’ variables.** | Such covariates cannot explain within‑site variation and therefore do not help with ignorability at the plot level. | Recognise they are **site‑level** covariates and include them in the conditioning set for the conditional ATE. |
| **Believing that matching guarantees unbiasedness without checking the ignorability assumption.** | Matching balances observed covariates but cannot address unobserved confounding. | State the **conditional ignorability** assumption explicitly and, if possible, conduct sensitivity analysis. |

By keeping these points in mind, you can correctly specify the estimand for a matched‑pair design that is sampled conditional on site‑level characteristics.

*Original question: [Which estimand better fits the matched pair design within units? ATT or ATE (Conditional or Local ATE?)](https://stats.stackexchange.com/questions/677180/which-estimand-better-fits-the-matched-pair-design-within-units-att-or-ate-con) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
