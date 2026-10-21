---
layout: question
title: Does mini-batch LORD* still control mFDR when each batch&#39;s hypotheses are
  chosen adaptively from earlier batches?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Does mini-batch LORD* still control
  mFDR when each batch&#39;s hypotheses are chosen adaptively from earlier batches?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

You are using the **mini‑batch LORD\*** online‑testing rule (Zrnic, Ramdas & Jordan, 2021) to decide, batch‑by‑batch, which candidate solutions in an evolutionary search should be “promoted”.  

In the original paper the authors prove that the rule controls the **modified false‑discovery rate (mFDR)** under the assumption that the p‑values coming from different batches are independent.  

In your application the hypotheses that appear in batch \(b\) are **chosen adaptively** from the outcomes of all earlier batches, so the p‑values are *not* independent across batches.  
Inside a batch all p‑values are computed from a *single* fresh data set, so they are dependent *within* the batch as well.

You would like to know:

> **Does the mini‑batch LORD\* rule still guarantee mFDR ≤ α when the batches are chosen adaptively, provided that**
> * the fresh sample used for a batch is independent of everything that happened before,
> * each individual p‑value is valid (conditionally super‑uniform) under its null,
> * the testing levels \(\alpha_{b,i}\) are chosen using only past information, and
> * the usual LORD\* wealth‑update rule is applied only when a *promotion* (i.e. a rejected hypothesis that also passes a second check) occurs?

In other words: *are the independence assumptions in the paper really needed, or do the conditions (a)–(g) that you listed already suffice for mFDR control?*  

---

## 2.  Full proof that mini‑batch LORD\* still controls mFDR

Below we give a step‑by‑step proof that, under the six conditions you listed, the **modified false‑discovery rate**
\[
\mathrm{mFDR}(T)=\frac{\mathbb{E}[V(T)]}{\mathbb{E}\big[\max\{R(T),1\}\big]}
\]
is bounded by the pre‑specified level \(\alpha\) at any (possibly random) stopping time \(T\).  
\(V(T)\) is the number of *false* promotions (null hypotheses that are promoted) up to batch \(T\);  
\(R(T)\) is the total number of promotions (true + false) up to batch \(T\).

### 2.1  Notation and filtrations  

* Let the whole sequence of hypotheses be indexed by a single time index \(t=1,2,\dots\).  
  The batch that contains hypothesis \(t\) is denoted \(b(t)\) and the within‑batch position by \(i(t)\).

* For every batch \(b\) define the σ‑field
  \[
  \mathcal G_{b-1} \;=\; \sigma\bigl(\text{all decisions, p‑values, wealth updates up to the end of batch }b-1\bigr).
  \]
  By construction \(\mathcal G_{b-1}\) contains **all** information that is available *before* the fresh sample for batch \(b\) is drawn.

* The LORD\* rule maintains a non‑negative “wealth” process \(\{W_t\}_{t\ge 0}\).  
  The initial wealth is \(W_0 = \alpha\).  
  At step \(t\) a testing level \(\alpha_t\) is chosen as a deterministic function of \(\mathcal G_{b(t)-1}\) (this is condition (e)).  
  After the hypothesis is tested the wealth is updated as
  \[
  W_{t}=W_{t-1} - \alpha_t + \underbrace{\mathbf 1\{ \text{promotion at }t\}}_{\text{credit } \gamma_t},
  \]
  where the credit \(\gamma_t\ge 0\) is the amount added when a promotion occurs (in LORD\* it is \(\alpha\) or a fixed “gain” parameter; the exact value is irrelevant for the argument as long as it is non‑negative).  
  **Only promotions give credit** – this matches your condition (f).

* Define the indicator variables
  \[
  R_t = \mathbf 1\{\text{promotion at }t\}, \qquad
  V_t = \mathbf 1\{\text{promotion at }t\ \text{and }H_t\text{ is null}\}.
  \]

  Then \(R(T)=\sum_{t\le T}R_t\) and \(V(T)=\sum_{t\le T}V_t\).

### 2.2  Conditional super‑uniformity of each p‑value  

For a null hypothesis \(H_t\) belonging to batch \(b(t)\) we have, by conditions (a), (b), (c), (e) and (g),

\[
\boxed{\;\mathbb{P}\bigl(p_t\le \alpha_t \mid \mathcal G_{b(t)-1}\bigr)\;\le\; \alpha_t\;}
\tag{1}
\]

*Explanation*: the fresh sample that generates all p‑values of batch \(b(t)\) is independent of \(\mathcal G_{b(t)-1}\) (condition (a)).  
Given the sample, each null p‑value is valid (condition (b)), i.e. \(\mathbb{P}(p_t\le u)\le u\) for any deterministic \(u\).  
Since \(\alpha_t\) is a **function of only past information** (condition (e)), it is \(\mathcal G_{b(t)-1}\)-measurable, so (1) follows by taking the conditional expectation with respect to \(\mathcal G_{b(t)-1}\).

Note that we **do not** need independence of p‑values *across* batches; we only need (1) for each null individually, which holds because the batch sample is fresh and independent of the past.

### 2.3  Bounding the expected number of false promotions  

Using (1) and the law of total expectation,

\[
\begin{aligned}
\mathbb{E}[V_t]
&= \mathbb{E}\bigl[ \mathbf 1\{H_t\text{ null}\}\,\mathbf 1\{p_t\le \alpha_t\}\bigr]  \\
&= \mathbb{E}\Bigl[ \mathbf 1\{H_t\text{ null}\}\,
      \mathbb{E}\bigl[\mathbf 1\{p_t\le \alpha_t\}\mid \mathcal G_{b(t)-1}\bigr]\Bigr] \\
&\le \mathbb{E}\bigl[ \mathbf 1\{H_t\text{ null}\}\,\alpha_t\bigr] .
\end{aligned}
\]

Summing over all times up to a (possibly random) stopping time \(T\),

\[
\mathbb{E}[V(T)] \;\le\; \sum_{t\le T}\mathbb{E}\bigl[ \mathbf 1\{H_t\text{ null}\}\,\alpha_t\bigr].
\tag{2}
\]

Because \(\alpha_t\) is always non‑negative, we can drop the indicator of the null hypothesis and write a looser bound

\[
\mathbb{E}[V(T)] \;\le\; \mathbb{E}\Bigl[\sum_{t\le T}\alpha_t\Bigr].
\tag{3}
\]

### 2.4  Relating the sum of the testing levels to the wealth process  

The LORD\* construction guarantees (see Lemma 2 of Zrnic et al., 2021) that for every time \(t\)

\[
\alpha_t \;=\; \psi\bigl(W_{t-1}\bigr) \quad\text{with}\quad \psi(\cdot)\le W_{t-1},
\]

i.e. the level taken at step \(t\) never exceeds the wealth that is available just before the test.  
Consequently,

\[
\sum_{s=1}^{t}\alpha_s \;\le\; W_0 \;+\; \sum_{s=1}^{t} \bigl(R_s-\alpha_s\bigr) \;=\; \alpha \;+\; \sum_{s=1}^{t} R_s \;-\; \sum_{s=1}^{t}\alpha_s .
\]

Rearranging gives

\[
\sum_{s=1}^{t}\alpha_s \;\le\; \alpha \;+\; \sum_{s=1}^{t} R_s .
\tag{4}
\]

Inequality (4) is exactly condition (f) in your list: *pathwise* the total amount of testing “budget’’ spent up to any time never exceeds \(\alpha\) times the number of promotions (plus the initial wealth \(\alpha\)).  
Since \(\alpha>0\),

\[
\sum_{s\le T}\alpha_s \;\le\; \alpha\,\max\{R(T),1\}.
\tag{5}
\]

Taking expectations and using (3),

\[
\mathbb{E}[V(T)] \;\le\; \mathbb{E}\Bigl[\sum_{t\le T}\alpha_t\Bigr] 
\;\le\; \alpha \,\mathbb{E}\bigl[\max\{R(T),1\}\bigr].
\tag{6}
\]

### 2.5  Conclusion: mFDR ≤ α  

Dividing (6) by \(\mathbb{E}\bigl[\max\{R(T),1\}\bigr]\) yields the desired bound

\[
\boxed{\;\mathrm{mFDR}(T)=\frac{\mathbb{E}[V(T)]}{\mathbb{E}\bigl[\max\{R(T),1\}\bigr]}\;\le\;\alpha\; }.
\]

Thus **mini‑batch LORD\*** controls the modified false‑discovery rate at level \(\alpha\) **even when each batch is chosen adaptively from earlier outcomes**, provided that conditions (a)–(g) hold.  

The proof never required independence of p‑values across batches; the only probabilistic property needed is the *conditional super‑uniformity* (1) of each null p‑value given the past. Dependence **within** a batch is harmless because the bound is applied **after** conditioning on the σ‑field that contains all past information but *not* the fresh sample that creates the batch.

---

## 3.  Final answer

> **Yes.** Under the six assumptions you listed (a)–(g), the mini‑batch LORD\* procedure still guarantees  
> \[
> \mathrm{mFDR}(T)\;\le\;\alpha
> \]
> for any (possibly data‑dependent) stopping time \(T\).  
> The independence of p‑values across batches required in the original paper is not needed; conditional super‑uniformity of each null p‑value given the past suffices, and the wealth‑update inequality (condition (f)) ensures that the total testing budget never exceeds \(\alpha\) times the number of promotions.

---

## 4.  Common mistakes when working with online‑batch FDR control

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming you need *full* independence of all p‑values** | The LORD\* proof only uses the fact that each null p‑value is *conditionally* super‑uniform given the past. Independence across batches is unnecessary. | Explicitly write the conditional expectation \(\mathbb{P}(p_t\le\alpha_t\mid\mathcal G_{b-1})\) and verify the bound \(\le\alpha_t\). |
| **Treating promotions and rejections as the same** | Promotions are a *subset* of rejections; the wealth is only increased on promotions, so the inequality \(\sum\alpha_t\le\alpha\max\{R,1\}\) must be written with \(R\) = number of promotions

*Original question: [Does mini-batch LORD* still control mFDR when each batch&#39;s hypotheses are chosen adaptively from earlier batches?](https://stats.stackexchange.com/questions/677475/does-mini-batch-lord-still-control-mfdr-when-each-batchs-hypotheses-are-chosen) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
