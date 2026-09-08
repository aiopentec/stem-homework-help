---
layout: question
title: Does a three-way decision built from equivalence and minimum-effect tests count
  as one hypothesis in a Holm correction?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Does a three-way decision built from
  equivalence and minimum-effect tests count as one hypothesis in a Holm correction?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is asking (in plain language)

The student has a **pre‑registered set of planned contrasts** (e.g., differences between groups).  
For some contrasts the plan is not a single two‑sided test but a **“three‑way decision”**:

| Decision | Test that leads to it |
|----------|----------------------|
| **Meaningful effect** | Minimum‑effect test: reject \(H_0:\;|\theta|\le \delta\) (i.e., evidence that the true effect is larger than a *smallest* effect of interest). |
| **No meaningful effect** | Equivalence test (TOST): reject \(H_0:\;|\theta|\ge \delta\) (i.e., evidence that the true effect is *smaller* than the same \(\delta\) in absolute value). |
| **Inconclusive** | Neither of the two null hypotheses is rejected. |

Because the two null hypotheses are **mutually exclusive** (they cannot both be true), the student treats the whole three‑way decision as **one “test”** when applying the Holm–Bonferroni step‑down procedure.  

They also have a **directional contrast** that yields a **four‑way decision** (meaningful increase, meaningful decrease, equivalence, inconclusive) – effectively three one‑sided procedures on the same data.

The questions are:

1. **Is it legitimate to count the three‑way decision as a single hypothesis for Holm?**  
2. **Does the same reasoning work for the four‑way (directional) decision?**  
3. **If not, what is the recommended way to handle such composite decisions when controlling the family‑wise error rate (FWER)?**  

They also wonder whether the positive dependence among some contrasts affects the conservativeness of Holm.

---

## 2. Background concepts

### 2.1. Holm–Bonferroni (step‑down) procedure  

* Suppose we have \(m\) *hypothesis tests* with raw \(p\)-values \(p_{(1)}\le p_{(2)}\le\cdots\le p_{(m)}\).  
* Choose a family‑wise error level \(\alpha\).  
* For \(k=1,\dots,m\) compare \(p_{(k)}\) with \(\alpha/(m-k+1)\).  
* Reject the first \(k\) hypotheses for which the inequality holds; stop at the first non‑rejection.

The guarantee: **If each individual test controls the type‑I error at level \(\alpha\) (i.e., \(P(\text{reject }H_0\mid H_0\text{ true})\le\alpha\)), then Holm controls the FWER at level \(\alpha\) regardless of the dependence structure among the tests.**  

The key point: *What counts as a “test”* is whatever hypothesis you are deciding to reject (or not) based on a single \(p\)-value or a set of \(p\)-values that together define a decision rule.

### 2.2. Minimum‑effect and equivalence (TOST) tests  

* **Minimum‑effect test** (sometimes called a “super‑null” test):  
  \[
  H_0^{\text{ME}}:\ |\theta|\le\delta \qquad\text{vs}\qquad H_1^{\text{ME}}:\ |\theta|>\delta .
  \]
  Usually performed by constructing a confidence interval for \(\theta\) and checking whether the interval lies **outside** \([-\,\delta,\delta]\).

* **Equivalence (TOST) test**:  
  \[
  H_0^{\text{EQ}}:\ |\theta|\ge\delta \qquad\text{vs}\qquad H_1^{\text{EQ}}:\ |\theta|<\delta .
  \]
  Implemented by two one‑sided tests (lower and upper bounds) and rejecting the overall null only if **both** one‑sided \(p\)-values are \(<\alpha\).  

Both procedures are **level‑\(\alpha\) tests**: under the respective null they reject with probability at most \(\alpha\).  

Importantly, the two null hypotheses are **disjoint** (they cannot both be true) but they are **not complements**: there is a “gap” region \(\{|\theta|=\delta\}\) of measure zero in continuous models, and the *inconclusive* region is the set of parameter values for which **neither** null is rejected.

### 2.3. What constitutes a *single* hypothesis in multiple‑testing language?

A hypothesis is a *set* of parameter values. If you decide **once** whether to reject that set, you have **one hypothesis test**.  
If you decide **twice** (e.g., first test \(H_0^{\text{ME}}\), then test \(H_0^{\text{EQ}}\)), you are effectively performing **two** hypothesis tests, even if you later combine the outcomes into a three‑way decision.

Therefore, the crucial question is: **Does the three‑way decision arise from a single test statistic with a single \(p\)-value, or from two separate tests each with its own \(p\)-value?**  

In the usual implementation, the minimum‑effect test uses a *single* two‑sided \(p\)-value (or equivalently a CI), while the equivalence test uses **two one‑sided \(p\)-values** that must both be below \(\alpha\).  The overall three‑way rule can be written as:

*Compute the (1–α) confidence interval for \(\theta\).*  

| CI location | Decision |
|-------------|----------|
| Entirely outside \([-\,\delta,\delta]\) | “meaningful effect” (reject ME) |
| Entirely inside \([-\,\delta,\delta]\) | “no meaningful effect” (reject EQ) |
| Overlaps a boundary | “inconclusive” |

Because the CI (or the underlying test statistic) is **the same** for both decisions, we can view the three‑way rule as a **single** test of a *composite null* that is the **union** of the two disjoint null sets:
\[
H_0^{\text{union}}:\ |\theta|\le\delta\ \text{or}\ |\theta|\ge\delta .
\]
Rejecting this *union* means we have evidence that \(\theta\) lies **outside** the union, i.e. in the interval \((-\,\delta,\delta)^c\) **and** inside \((-\,\delta,\delta)\) simultaneously – which is impossible.  In practice the rule *rejects* one of the two component nulls, never both.  

Hence the three‑way decision **can be treated as a single hypothesis test** *provided* we use a **single \(p\)-value** (or a single confidence interval) to drive the whole rule.  The resulting procedure still has type‑I error \(\le\alpha\).

---

## 3. Answer to the three questions

### Q1.  *Is it correct to treat the three‑way decision as one hypothesis for Holm?*  

**Yes, if the three‑way decision is derived from a *single* test statistic (or a single confidence interval) that yields a *single* \(p\)-value controlling the type‑I error at level \(\alpha\).**  

*Reasoning*  

1. Let \(C_{1-\alpha}\) be the \((1-\alpha)\) confidence interval for \(\theta\).  
2. The rule “declare a meaningful effect if \(C_{1-\alpha}\) lies entirely outside \([-\,\delta,\delta]\)” is equivalent to **rejecting** the null \(H_0^{\text{ME}}:|\theta|\le\delta\) at level \(\alpha\).  
3. The rule “declare no meaningful effect if \(C_{1-\alpha}\) lies entirely inside \([-\,\delta,\delta]\)” is equivalent to **rejecting** the null \(H_0^{\text{EQ}}:|\theta|\ge\delta\) at level \(\alpha\).  
4. Because the same confidence interval is used for both, the probability (under any true value of \(\theta\)) that **either** of the two rejections occurs is **exactly the same** as the probability that the interval falls completely in either the “outside” region or the “inside” region.  
5. Under the global null \(H_0^{\text{union}} =\{|\theta|\le\delta\}\cup\{|\theta|\ge\delta\}\) (i.e., any \(\theta\) not strictly between \(-\delta\) and \(\delta\)), the probability that the interval falls entirely outside **or** entirely inside is bounded by \(\alpha\).  This is a direct consequence of the confidence‑interval coverage property: \(P\bigl(\theta\in C_{1-\alpha}\bigr)\ge 1-\alpha\). Hence,
   \[
   P\bigl(\text{reject ME or reject EQ}\mid H_0^{\text{union}}\bigr)\le\alpha .
   \]

Therefore the three‑way rule behaves like a **single level‑\(\alpha\) test** of the union null, and counting it as *one* element in the Holm family is valid.  The FWER of the whole set of comparisons (including any other independent or dependent tests) will be controlled at \(\alpha\).

> **Caveat** – the reasoning hinges on *using the same confidence interval (or the same test statistic) for both decisions.* If you were to compute two *independent* \(p\)-values (e.g., a two‑sided test for the minimum effect **and** a separate two‑one‑sided TOST) and then combine them, you would actually be performing **two** tests, and the Holm count would need to be increased to two.

---

### Q2.  *What about a directional contrast that yields a four‑way decision (meaningful increase, meaningful decrease, equivalence, inconclusive)?*  

A four‑way rule can be expressed as **three** one‑sided tests:

| Decision | Null hypothesis tested (one‑sided) |
|----------|-----------------------------------|
| Meaningful increase | \(H_0^{\text{inc}}:\ \theta \le \delta\) (reject if lower CI bound \(> \delta\)) |
| Meaningful decrease | \(H_0^{\text{dec}}:\ \theta \ge -\delta\) (reject if upper CI bound \(< -\delta\)) |
| Equivalence | \(H_0^{\text{EQ}}:\ |\theta| \ge \delta\) (reject if CI entirely inside \([-\,\delta,\delta]\)) |

These three one‑sided nulls are **mutually exclusive** (they cannot all be true simultaneously). The decision rule is:

* If the confidence interval lies completely **to the right** of \(\delta\) → “increase”.  
* If it lies completely **to the left** of \(-\delta\) → “decrease”.  
* If it lies completely **inside** \([-\,\delta,\delta]\) → “equivalence”.  
* Otherwise → “inconclusive”.

Again, the rule can be seen as a **single test of the union null**
\[
H_0^{\text{union}} = \{\theta\le\delta\}\ \cup\ \{\theta\ge -\delta\}\ \cup\ \{|\theta|\ge\delta\}.
\]
But note that the first two sets overlap with the third; the union simplifies to the whole real line **except** the open interval \((-\delta,\delta)\) *and* the two tails beyond \(\pm\delta\). In fact the union is just the complement of the open interval \((-\delta,\delta)\); the three component nulls together are equivalent to “\(|\theta|\ge\delta\) **or** \(\theta\le\delta\) **or** \(\theta\ge -\delta\)”, which is *always true*.  

Therefore we must be more precise: the **directional** rule is *not* a test of a single null; it distinguishes **two distinct alternatives** (increase vs decrease) as well as equivalence. The proper way to view it is as **three separate hypotheses** that are *tested simultaneously* using the **same confidence interval**.  

Because the confidence interval can fall in at most **one** of the three mutually exclusive regions, the probability of **any** false rejection (i.e., rejecting a false directional or equivalence null) is still bounded by \(\alpha\). Formally:

* Under any true \(\theta\) that lies in the “increase” region (\(\theta>\delta\)), the only possible erroneous rejection is the equivalence or decrease nulls. The interval will be entirely to the right of \(\delta\) with probability at least \(1-\alpha\); consequently the probability of mistakenly rejecting the wrong null is \(\le\alpha\).

* The same argument works for the “decrease” and “equivalence” regions.

Thus, **the three one‑sided tests can be treated as a single composite test** (a *partition* of the sample space) provided we **use the same confidence interval** for all three decisions. In the Holm procedure we therefore **count this contrast as a single element**, not as three.  

*If you were to compute three *independent* \(p\)-values (e.g., two one‑sided tests for increase/decrease plus a separate TOST), you would need to count three hypotheses. But the standard practice is to base all three decisions on the same interval, which

*Original question: [Does a three-way decision built from equivalence and minimum-effect tests count as one hypothesis in a Holm correction?](https://stats.stackexchange.com/questions/677103/does-a-three-way-decision-built-from-equivalence-and-minimum-effect-tests-count) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
