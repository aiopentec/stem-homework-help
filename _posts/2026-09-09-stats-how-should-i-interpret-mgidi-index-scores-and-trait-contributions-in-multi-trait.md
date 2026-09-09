---
layout: question
title: How should I interpret MGIDI index scores and trait contributions in multi-trait
  selection?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: How should I interpret MGIDI index
  scores and trait contributions in multi-trait selection?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (plain‑language restatement)

The student is using the **Multi‑trait Genotype–Ideotype Distance Index (MGIDI)** to rank genotypes (e.g., plant varieties) on the basis of several traits that have different desired directions (some to be maximised, some to be minimised).  
They want to know:

| Question | In everyday words |
|----------|-------------------|
| **Q1** | Does a *smaller* MGIDI value always mean the genotype is “closer” to the ideal (the ideotype)? |
| **Q2** | How should we read the **contribution of each trait** to the total MGIDI value? |
| **Q3** | If a trait contributes a lot, does that mean the genotype is *bad* for that trait, or just that the trait has a large influence on the distance? |
| **Q4** | What do the **factor scores** and **loadings** that appear in the MGIDI formula really represent? |
| **Q5** | Should we rely only on the MGIDI ranking to pick genotypes, or also look at the individual trait values? |

Below is a step‑by‑step walk‑through that answers each of these points and shows how the pieces (standardisation, factor analysis, Euclidean distance) fit together.

---

## 2.  Full derivation & interpretation of MGIDI  

### 2.1  The basic idea: distance to an *ideotype*

1. **Ideotype definition** – For each trait \(j\) we specify a *target* value \(t_j\) that reflects the breeding goal (e.g., highest possible grain yield, lowest disease score).  
2. **Genotype vector** – For genotype \(i\) we have the observed raw measurements \(\mathbf{x}_{i}= (x_{i1},x_{i2},\dots ,x_{ip})^\top\) for the \(p\) traits.  

The MGIDI tries to summarise, in a **single scalar**, how far genotype \(i\) lies from the ideal point \(\mathbf{t}=(t_1,\dots ,t_p)^\top\) **in a multivariate sense**.

### 2.2  Step 0 – Pre‑processing of the data  

| Operation | Why we do it |
|-----------|--------------|
| **Direction standardisation** (multiply traits to be *minimised* by \(-1\)) | Guarantees that for **all** traits “large = good”. |
| **Centering & scaling** (usually Z‑score: \(\tilde{x}_{ij}= (x_{ij}-\bar{x}_j)/s_j\)) | Removes units, makes traits comparable, and puts them on the same metric. The same transformation is applied to the ideotype: \(\tilde{t}_j = (t_j-\bar{x}_j)/s_j\). |

After this step the data matrix \(\tilde{\mathbf X}\) and the ideotype vector \(\tilde{\mathbf t}\) are *dimensionless* and have mean 0, variance 1 (per trait).

### 2.3  Step 1 – Factor analysis (FA)  

1. **Why FA?**  
   * Many traits are correlated. Using them directly would give redundant weight to the same underlying biological factor (e.g., “plant vigor”).  
   * FA creates a smaller set of *latent variables* (factors) that capture most of the variance while being (approximately) orthogonal.  

2. **FA model**  

\[
\tilde{\mathbf X}= \mathbf{F}\mathbf{L}^{\top}+ \mathbf{E},
\]

where  

* \(\mathbf{F}\) is the \(n \times m\) matrix of **factor scores** ( \(m\) = number of retained factors, usually chosen by eigenvalues > 1 or a cumulative variance threshold).  
* \(\mathbf{L}\) is the \(p \times m\) matrix of **loadings** (correlations between original traits and each factor).  
* \(\mathbf{E}\) is the residual matrix.

3. **Interpretation of loadings**  

   * A loading close to **+1** (or **–1**) means that the trait strongly contributes to that factor, with the sign indicating the direction of the relationship.  
   * Loadings near **0** mean the trait is almost unrelated to the factor.  

   Thus, each factor can be thought of as a *synthetic trait* that is a weighted combination of the original ones.

### 2.4  Step 2 – Ideotype scores on the factor space  

Because the factor analysis is a **linear transformation**, the ideotype vector can also be projected onto the factor space:

\[
\mathbf{f}_t = \tilde{\mathbf t}\,\mathbf{L},
\]

giving the **ideotype factor scores** \(\mathbf{f}_t = (f_{t1},\dots ,f_{tm})\).

### 2.5  Step 3 – Euclidean distance in the factor space (the MGIDI)  

For genotype \(i\) we have its factor scores \(\mathbf{f}_i = (\tilde{x}_{i\cdot})\mathbf{L}\).  
The MGIDI is defined as the **Euclidean distance** between \(\mathbf{f}_i\) and the ideotype factor scores:

\[
\boxed{\text{MGIDI}_i = \bigl\| \mathbf{f}_i-\mathbf{f}_t \bigr\|
      = \sqrt{\sum_{k=1}^{m}\bigl(f_{ik}-f_{tk}\bigr)^2}}.
\]

Because Euclidean distance is always **non‑negative**, the *smallest* possible value is 0 (genotype = ideotype).  

### 2.6  Step 4 – Decomposing the distance into *trait contributions*  

Although the distance is computed in the **factor space**, we can trace back how each *original trait* influences it:

1. Compute the **squared** contribution of each factor:

\[
C_{ik}^{(\text{factor})}= (f_{ik}-f_{tk})^{2}.
\]

2. Express each factor as a linear combination of traits using the loadings. The contribution of trait \(j\) to factor \(k\) for genotype \(i\) is

\[
c_{ijk}= L_{jk}^{2}\, C_{ik}^{(\text{factor})},
\]

where \(L_{jk}\) is the loading of trait \(j\) on factor \(k\).  
(The squaring of the loading follows from the fact that distance is quadratic.)

3. Sum over factors to obtain the *overall* contribution of trait \(j\):

\[
\boxed{C_{ij}= \sum_{k=1}^{m} L_{jk}^{2}\,(f_{ik}-f_{tk})^{2}} .
\]

These \(C_{ij}\) values are **always positive** and add up to \(\text{MGIDI}_i^{2}\).  

To express them as percentages:

\[
\%C_{ij}= \frac{C_{ij}}{\text{MGIDI}_i^{2}}\times 100.
\]

---

## 3.  Answering the specific questions  

### Q1 – Does a lower MGIDI always mean a genotype is closer to the ideotype?  

**Yes.** By definition MGIDI is a Euclidean distance; the smaller the distance, the nearer the genotype’s factor scores are to the ideotype’s factor scores. A value of **0** would mean the genotype exactly matches the ideotype on every trait (after standardisation).  

*Note:* Because we work in a transformed (standardised + factor‑reduced) space, “closer” is measured on a **relative** scale, not on the raw trait units.

---

### Q2 – How to interpret the contribution of individual traits?  

* The **absolute contribution** \(C_{ij}\) tells how much trait \(j\) participates in the *squared* distance for genotype \(i\).  
* The **percentage contribution** \(\%C_{ij}\) tells the *proportion* of the total distance that is attributable to that trait.  

If a trait accounts for, say, **45 %** of the MGIDI of a genotype, it is the dominant source of the genotype’s deviation from the ideal.

---

### Q3 – Does a large contribution mean the genotype is “bad” for that trait?  

Not necessarily. A large contribution can arise from two sources:

| Source | What it means |
|--------|---------------|
| **Large residual** \((f_{ik}-f_{tk})\) for a factor that heavily loads on the trait | The genotype truly deviates from the desired direction for that trait (or a group of correlated traits). |
| **Large loading** \(L_{jk}\) (the trait is strongly tied to that factor) | Even a modest residual in that factor can translate into a large contribution because the trait is a major component of the factor. |

Hence, a high percentage contribution **flags** the trait as an important driver of distance, but you still need to look at the *direction* of the deviation (e.g., is the trait too low or too high?) to decide whether the genotype is “poor” for that trait.

---

### Q4 – How to understand the factor scores & loadings?  

| Item | Interpretation |
|------|----------------|
| **Loadings (\(L_{jk}\))** | Correlation (or weight) of original trait \(j\) with latent factor \(k\). A loading of +0.8 means trait \(j\) moves **in the same direction** as factor \(k\); –0.8 means it moves oppositely. |
| **Factor scores (\(f_{ik}\))** | The coordinate of genotype \(i\) on factor \(k\). It is a *synthetic* trait that aggregates the information of all original traits that load on that factor. |
| **Ideotype factor scores (\(f_{tk}\))** | The coordinate of the ideal genotype on factor \(k\). Because the ideotype is defined on the original trait scale, we project it onto the factor space using the same loadings. |

In practice, you can inspect the loading matrix to give each factor a **biological label** (e.g., “yield‑related”, “stress tolerance”) and then interpret a genotype’s distance in terms of those synthetic dimensions.

---

### Q5 – Should selection be based solely on MGIDI ranking?  

**MGIDI is a powerful *summary* index, but it should not be the only decision tool.** Recommended workflow:

1. **Rank by MGIDI** – eliminates genotypes that are far from the ideotype on the *overall* multivariate scale.  
2. **Inspect the trait‑percentage contributions** – identify which traits are responsible for the remaining distance.  
3. **Check raw (or standardized) trait values** for the top‑ranked genotypes, especially for traits that are of *critical* importance (e.g., disease resistance may be non‑negotiable even if its contribution to MGIDI is modest).  
4. **Apply any hard constraints** (e.g., a genotype must have grain yield ≥ X). These constraints can be enforced before or after the MGIDI calculation.  

Thus, MGIDI is best used **in conjunction** with trait‑level diagnostics, not as a black‑box selector.

---

## 4.  Worked numeric illustration (optional but clarifies the math)

| Trait (after direction standardisation) | Mean | SD | Desired (ideotype) |
|----------------------------------------|------|----|--------------------|
| Yield (kg) (higher‑better)            | 5000 | 400| 6000 |
| Plant height (cm) (lower‑better)      | 150  | 10 | 130 |
| Disease score (scale 1–9, lower‑better)| 4   | 1  | 1   |

1. **Standardise**  

\[
\tilde{x}_{ij}= \frac{x_{ij}-\bar{x}_j}{s_j},
\qquad
\tilde{t}_j = \frac{t_j-\bar{x}_j}{s_j}
\]

Suppose for genotype A we have raw values (6000, 140, 2). After standardisation:

\[
\tilde{\mathbf{x}}_A = (2.5,\; -1.0,\; -2.0), \qquad
\tilde{\mathbf{t}} = (2.5,\; -2.0,\; -3.0).
\]

2. **Factor analysis** (say we keep 2 factors). The loading matrix (rounded) is

\[
\mathbf{L}= 
\begin{bmatrix}
0.80 & 0.10\\
0.30 & -0.90\\
0.50 & 0.20
\end{bmatrix}.
\]

3. **Factor scores**  

\[
\mathbf{f}_A = \tilde{\mathbf{x}}_A\mathbf{L} = (2.5\cdot0.80+(-1.0)\cdot0.30+(-2.0)\cdot0.50,\;
2.5\cdot0.10+(-1.0)(-0.90)+(-2.0)\cdot0.20) = (0.65,\; 0.55).
\]

\[
\mathbf{f}_t = \tilde{\mathbf{t}}\mathbf{L} = (2.5\cdot0.80+(-2.0)\cdot0.30+(-3.0)\cdot0.50,\;
2.5\cdot0.10+(-2.0)(-0.90)+(-3.0)\cdot0.20) = (-0.85

*Original question: [How should I interpret MGIDI index scores and trait contributions in multi-trait selection?](https://stats.stackexchange.com/questions/677115/how-should-i-interpret-mgidi-index-scores-and-trait-contributions-in-multi-trait) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
