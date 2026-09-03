---
layout: question
title: Feature and target alignment
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Feature and target alignment'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. Restating the Question in Plain Language  

You have a set of **graph embeddings** (vectors) that you intend to use as features for a supervised learning task (the *targets* are scalar or vector‑valued labels).  
You would like to know:

1. **Can a “nearest‑neighbour” (instance‑based) idea be used to decide whether a particular embedding is a “good” feature for the downstream task?**  
2. **Specifically**, for a held‑out (test) graph you find its 25 nearest training graphs in the embedding space, take a similarity‑weighted average of their **targets**, and compute the **cosine similarity** between this averaged target and the true target of the held‑out graph.  
   *If the cosine similarity is high, does that mean the embedding is “aligned” with the target?*  
   *If it is low, does that mean the embedding is poorly aligned?*  

In other words: *Is the described cosine‑similarity statistic an informative measure of feature‑target alignment, and does its usefulness depend on the learning task?*  

---

## 2. Step‑by‑Step Worked Solution  

Below we develop a rigorous statistical framework to answer the question.  
All symbols are defined in the **Notation** section; each subsequent step builds on the previous one.

### Notation  

| Symbol | Meaning |
|--------|----------|
| \( \mathbf{x}_i \in \mathbb{R}^d \) | Embedding (feature vector) of the *i‑th* graph |
| \( y_i \in \mathbb{R}^p \) | Target (label) of the *i‑th* graph (scalar if \(p=1\)) |
| \( \mathcal{T} = \{(\mathbf{x}_i,y_i)\}_{i=1}^N \) | Training set (size \(N\)) |
| \( (\mathbf{x}_\star, y_\star) \) | A held‑out (test) graph |
| \( \mathcal{N}_{25}(\mathbf{x}_\star) \) | Indices of the 25 nearest neighbours of \( \mathbf{x}_\star \) in the training set, measured by cosine similarity of the embeddings |
| \( w_{i\star} \) | Similarity‑based weight for neighbour \(i\) (non‑negative, sum to 1) |
| \( \bar y_\star = \sum_{i\in\mathcal{N}_{25}} w_{i\star}\, y_i \) | Weighted mean of the neighbours’ targets |
| \( \operatorname{cos}(\mathbf{a},\mathbf{b}) = \frac{\mathbf{a}^\top\mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|} \) | Cosine similarity between vectors \(\mathbf{a}\) and \(\mathbf{b}\) |
| \( s_\star = \operatorname{cos}(y_\star,\bar y_\star) \) | Statistic of interest for the held‑out graph |

### Step 1 – Clarify What “Alignment” Means  

*Alignment* is a vague term. In a statistical sense we can define it as **the degree to which similarity in the embedding space predicts similarity in the target space**.  
A concrete operational definition is:

> **Feature‑target alignment** ⇔ *Higher cosine similarity between a test target and the similarity‑weighted neighbour‑target average predicts better performance of a downstream model that uses the embeddings as features.*

Thus, the statistic \(s_\star\) is a **candidate proxy** for alignment. We must verify whether it is *informative* (i.e., carries signal about the true relationship) rather than just random noise.

### Step 2 – Compute the Statistic for Every Test Instance  

For each held‑out instance in a validation set (size \(M\)):

1. Compute cosine similarities between \(\mathbf{x}_\star\) and all training embeddings \(\mathbf{x}_i\).  
2. Select the 25 largest similarities → indices \(\mathcal{N}_{25}(\mathbf{x}_\star)\).  
3. Turn the raw similarities into weights, e.g.  
   \[
   w_{i\star}= \frac{\exp(\alpha\,\operatorname{cos}(\mathbf{x}_\star,\mathbf{x}_i))}{\sum_{j\in\mathcal{N}_{25}} \exp(\alpha\,\operatorname{cos}(\mathbf{x}_\star,\mathbf{x}_j))},
   \]
   where \(\alpha>0\) controls concentration (common choices: \(\alpha=1\) or \(\alpha=10\)).  
4. Compute the weighted mean target \(\bar y_\star\).  
5. Compute the cosine similarity \(s_\star = \operatorname{cos}(y_\star,\bar y_\star)\).

Collect the vector \(\mathbf{s} = (s_1,\dots,s_M)\).

### Step 3 – Decide What “Informative” Means  

Two natural ways to assess informativeness:

| Approach | What it measures | How to implement |
|----------|------------------|-------------------|
| **Correlation with prediction error** | If high \(s_\star\) corresponds to low error of a downstream model, the statistic is useful. | Train a model (e.g., linear regression, neural net) on the embeddings, obtain predictions \(\hat y_\star\) on the held‑out set, compute errors \(e_\star = \|y_\star-\hat y_\star\|_2\). Compute Pearson (or Spearman) correlation \(\rho = \operatorname{corr}(\mathbf{s}, -\mathbf{e})\). A large positive \(\rho\) indicates alignment. |
| **Permutation / null‑distribution test** | Checks whether the observed distribution of \(s_\star\) is different from what would be expected if embeddings and targets were unrelated. | Randomly permute the targets among the training points, recompute \(\mathbf{s}^{\text{perm}}\) many times (e.g., 1 000 permutations), obtain a null distribution of the mean (or median) of \(s\). If the true mean lies far in the tail (p < 0.05), the statistic is informative. |

Both approaches can be used together: the correlation tells you *how* the statistic relates to downstream performance; the permutation test tells you *whether* the statistic contains any signal at all.

### Step 4 – Perform the Correlation Analysis  

Assume we have trained a downstream model \(f(\mathbf{x})\) and obtained predictions \(\hat y_\star = f(\mathbf{x}_\star)\).  

1. Compute error vector \(\mathbf{e}\).  
2. Compute Pearson correlation:  

   \[
   \rho = \frac{\sum_{\star=1}^{M}(s_\star - \bar s)(e_\star - \bar e)}{\sqrt{\sum_{\star}(s_\star-\bar s)^2}\sqrt{\sum_{\star}(e_\star-\bar e)^2}} .
   \]

3. Test significance (t‑test):  

   \[
   t = \rho\sqrt{\frac{M-2}{1-\rho^2}},\quad p = 2\,\bigl[1 - T_{M-2}(|t|)\bigr],
   \]
   where \(T_{M-2}\) is the CDF of a Student‑t distribution with \(M-2\) df.

**Interpretation**

| Result | Interpretation |
|--------|----------------|
| \(\rho > 0\) and statistically significant (e.g., \(p < 0.05\)) | Higher cosine similarity → lower prediction error → embeddings are aligned with targets. |
| \(\rho \approx 0\) (non‑significant) | No linear relationship; the statistic does not convey useful alignment information. |
| \(\rho < 0\) (significant) | Counter‑intuitive; perhaps the weighting scheme is flawed or the task requires a different similarity metric. |

### Step 5 – Perform the Permutation Test  

1. **Create the null distribution**  
   - For \(b = 1,\dots,B\) (e.g., \(B=1000\)):  
     - Randomly permute the training targets \(\{y_i\}\) → \(\{y_i^{(b)}\}\).  
     - Re‑compute the weighted neighbour means \(\bar y_\star^{(b)}\) and cosine similarities \(s_\star^{(b)}\).  
     - Store the statistic of interest, e.g., the mean similarity \(\mu^{(b)} = \frac{1}{M}\sum_{\star} s_\star^{(b)}\).  

2. **Compute the observed statistic** \(\mu^{\text{obs}} = \frac{1}{M}\sum_{\star} s_\star\).

3. **p‑value**  

   \[
   p = \frac{1+\#\{b : \mu^{(b)} \ge \mu^{\text{obs}}\}}{1+B}.
   \]

4. **Decision**  
   - If \(p < \alpha\) (commonly \(\alpha = 0.05\)), reject the null hypothesis of no alignment.  

### Step 6 – Does the Result Depend on the Task?  

| Task Type | Expected behaviour of the statistic |
|-----------|--------------------------------------|
| **Regression with smooth target function** (e.g., predicting a molecular property) | If the embedding respects the geometry of the underlying property, neighbours in embedding space will have similar targets → high \(s_\star\) ⇒ good alignment. |
| **Classification** (binary or multiclass) | Cosine similarity of *continuous* target vectors is less natural. One can encode class labels as one‑hot vectors; then the statistic essentially measures *label homogeneity* among neighbours. Alignment is useful only when classes are well‑separated in the embedding space. |
| **Highly non‑linear / chaotic relationships** | Even exact neighbours may have wildly different targets, so \(s_\star\) will be near zero and not informative. |
| **Tasks where the embedding was trained *specifically* to capture the target** (e.g., supervised graph‑embedding) | Expect strong alignment; the statistic should be highly informative. |
| **Purely unsupervised embeddings** (e.g., node2vec on graph structure) | Alignment may be weak or absent; the statistic may not be informative unless the unsupervised geometry accidentally matches the target geometry. |

Thus, **the usefulness of the cosine‑similarity proxy indeed depends on the nature of the downstream task** and on how well the embedding space reflects the target structure.

### Step 7 – Summary of the Decision Procedure  

| What you want to know? | Recommended analysis |
|------------------------|----------------------|
| *Does a high cosine similarity indicate that the embedding is a good feature for my model?* | Compute \(s_\star\) for a held‑out set, train a downstream model, and check the correlation between \(s_\star\) and prediction error. |
| *Is the observed pattern statistically significant?* | Run a permutation test on the target labels and compare the observed mean (or median) similarity to the null distribution. |
| *Is the approach appropriate for my problem?* | Verify that (i) targets are numeric (or encoded as vectors) so cosine similarity makes sense, and (ii) the task is one where local similarity in feature space is expected to translate into local similarity in label space. |

---

## 3. Final Answer  

**Yes –** the cosine similarity between a test target and the similarity‑weighted mean of its 25 nearest training targets **can be an informative measure of feature‑target alignment**, **provided** that:

1. The embedding space is expected to preserve target similarity (e.g., the embedding was trained with supervision or the task is smooth).  
2. The downstream task is such that “nearby” instances in embedding space should have “nearby” targets (most regression problems and well‑separated classification problems).  

To decide whether the statistic is actually informative for a given dataset:

1. Compute the statistic \(s_\star\) for a held‑out validation set.  
2. Train a model on the embeddings and obtain prediction errors.  
3. Correlate \(s_\star\) with the negative errors; a significant positive correlation indicates that higher similarity ⇒ better predictive performance (i.e., alignment).  
4. Complement the correlation with a permutation test to ensure the observed similarity is larger than expected by chance.

If both the correlation is significant and the permutation test yields a small p‑value (e.g., < 0.05), you can conclude that **higher cosine similarity corresponds to better alignment**, and the statistic is useful for feature selection or for diagnosing the quality of your embeddings.

If either test fails, the cosine‑similarity proxy is not providing useful information for that particular task, and you should either (a) try a different similarity metric, (b) increase the number of neighbours, or (c) reconsider the embedding method.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using raw cosine similarity as weights without normalising** | Weights may not sum to 1, leading to biased \(\bar y_\star

*Original question: [Feature and target alignment](https://stats.stackexchange.com/questions/677061/feature-and-target-alignment) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
