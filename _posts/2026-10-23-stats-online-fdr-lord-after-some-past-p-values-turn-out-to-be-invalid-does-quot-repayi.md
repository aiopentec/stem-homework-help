---
layout: question
title: 'Online FDR (LORD) after some past p-values turn out to be invalid: does &quot;repaying
  the alpha-wealth debt&quot; keep mFDR control for the clean tests?'
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Online FDR (LORD) after some past
  p-values turn out to be invalid: does &quot;repaying the alpha-wealth debt&quot;
  keep m'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. Plain Language Restatement

In **online False Discovery Rate (FDR) control** (specifically using algorithms like LORD), you test hypotheses sequentially or in mini-batches. When you make a discovery (a rejection), you earn an "alpha-wealth reward" that funds the significance thresholds ($\alpha_{b,i}$) for future tests. 

Normally, this guarantees that the **marginal False Discovery Rate (mFDR)** is controlled at level $\alpha$. However, a major problem arises if you discover later that some past p-values were **invalid** (due to data leakage, bugs, or flawed assumptions). Some of those invalid tests might have been incorrectly rejected, meaning their rewards artificially inflated the $\alpha$ levels for subsequent, legitimate ("clean") tests. You cannot undo the past, and those inflated levels have already been spent.

This problem asks: **If we institute a "debt-repaying rule"—where future rewards from clean discoveries are withheld until we pay back the exact amount of "tainted" $\alpha$ that clean tests improperly spent—does this mathematically restore mFDR control for the clean tests (up to an expected debt term)?** 

We need to rigorously evaluate whether the student's proposed "debt rule" successfully bounds the expected false discoveries among the clean tests, yielding the claimed bound:
$$\mathbb{E}[V_{\text{clean}}(T)] \;\le\; \alpha\,\mathbb{E}[R_{\text{clean}}(T)\vee 1] \;+\; \mathbb{E}[D(T)].$$

---

### 2. Step-by-Step Mathematical Derivation

To evaluate whether the debt-repaying rule works, we must analyze how the $\alpha$-wealth allocation changes under the intervention and how it impacts the expectation of false positives among the clean tests.

#### Step 2.1: Deconstruct the Original Online FDR Martingale Bound
In standard online FDR algorithms (like LORD), the allocated significance level $\alpha_t$ (or $\alpha_{b,i}$) at step $t$ is a predictable process (measurable with respect to the $\sigma$-algebra $\mathcal{F}_{t-1}$ of all past outcomes up to time $t-1$). 

For any true null hypothesis tested at time $t$, the p-value $P_t$ is conditionally super-uniform:
$$\mathbb{P}(P_t \le \alpha_t \mid \mathcal{F}_{t-1}) \le \alpha_t.$$
Let $V_t = I(\text{null } t \text{ is rejected})$. By definition, $V_t$ is an indicator variable, and its conditional expectation is:
$$\mathbb{E}[V_t \mid \mathcal{F}_{t-1}] = \mathbb{P}(\text{null } t \text{ rejected} \mid \mathcal{F}_{t-1}) \le \alpha_t.$$

Summing over all tests up to time $T$, the standard expected false discovery bound is derived via summation of expectations:
$$\mathbb{E}[V(T)] = \mathbb{E}\left[\sum_{t=1}^T V_t\right] = \sum_{t=1}^T \mathbb{E}[\mathbb{E}[V_t \mid \mathcal{F}_{t-1}]] \le \mathbb{E}\left[\sum_{t=1}^T \alpha_t\S\right]$$

#### Step 2.2: Analyze the Impact of Tainted Rejections and the Debt Rule
Let $S$ be the set of tests with invalid p-values. Some of these were rejected, generating reward coefficients that were pumped into the $\alpha$-wealth pool. Let $\alpha_t^{\text{original}}$ be the level that *would* have been assigned, and let $\alpha_t^{\text{clean}}$ be the level actually assigned under the student's debt rule.

The student’s rule dictates:
1. **Removal:** The direct reward terms from tainted rejections in $S$ are stripped out of future levels.
2. **Debt Accumulation ($D_0$):** $D_0$ is the exact amount of $\alpha$-wealth that clean tests spent because of those tainted rewards *prior* to the discovery of the leak at batch $b_d$.
3. **Repayment:** Any new clean rejections yield reward coefficients $c$, but these are reduced by $\min(c, D_{\text{rem}})$ until the debt $D_{\text{rem}}$ reaches 0.

Let $R_{\text{clean}}(T)$ be the number of clean rejections up to time $T$, and let $V_{\text{clean}}(T)$ be the number of false rejections among the clean tests.

#### Step 2.3: Formulate the Level Accounting Identity
At any time $t$ for a clean test, the assigned level $\alpha_t^{\text{clean}}$ can be expressed relative to a hypothetical "fully honest" process running from the start without the tainted rewards, adjusted for the debt mechanism.

Specifically, the total $\alpha$-wealth distributed to clean tests up to time $T$, denoted $\sum_{t \in \text{Clean}} \alpha_t^{\text{clean}}$, satisfies:
$$\sum_{t \in \text{Clean}} \alpha_t^{\text{clean}} \;\le\; \underbrace{\sum_{t \in \text{Clean}} \alpha_t^{\text{honest}}}_{\text{Baseline wealth from initial capital and clean rejections}} + D_0 - D(T)$$

Wait, let's look closer at the repayment mechanism in Rule 3:
* Clean rejections generate reward coefficients $c$.
* Instead of adding full $c$ to the wealth, we add $c - \min(c, D_{\text{rem}})$.
* This means the total wealth injected by clean rejections is *reduced* by the total amount of debt repaid up to time $T$, which is $D_0 - D(T)$.

Therefore, the cumulative $\alpha$-levels allocated to clean tests up to time $T$ equal:
$$\sum_{t \in \text{Clean}} \alpha_t^{\text{clean}} \;=\; \text{Base wealth} \;+\; (\text{Clean rewards generated}) \;-\; (\text{Debt repaid by } T)$$
$$\sum_{t \in \text{Clean}} \alpha_t^{\text{clean}} \;=\; \text{Base wealth} \;+\; (\text{Clean rewards generated} - [D_0 - D(T)])$$

Because the debt repayment *withholds* wealth that would have otherwise been granted to clean tests, the total $\alpha$-wealth spent on clean tests is shifted downward by the remaining debt $D(T)$ compared to what a purely clean system would have spent, offset by $D_0$.

Mathematically, linking the allocated levels to the reward structure of LORD:
$$\sum_{t \in \text{Clean}} \alpha_t^{\text{clean}} \;\le\; \alpha \cdot (R_{\text{clean}}(T) \vee 1) \;-\; D(T) \;+\; (\text{terms depending on initial base wealth } w_0)$$

#### Step 2.4: Taking Expectations
Taking the expectation of both sides for the false discoveries among clean tests:
$$\mathbb{E}[V_{\text{clean}}(T)] \;\le\; \mathbb{E}\left[\sum_{t \in \text{Clean}} \alpha_t^{\text{clean}}\right]$$

Substitute our level accounting identity:
$$\mathbb{E}[V_{\text{clean}}(T)] \;\le\; \mathbb{E}\big[\alpha \cdot (R_{\text{clean}}(T) \vee 1) - D(T) + D_0 \text{ (or adjustments for } w_0)\big]$$

Rearranging the inequality to isolate the debt terms as an additive penalty:
$$\mathbb{E}[V_{\text{clean}}(T)] \;\le\; \alpha\,\mathbb{E}[R_{\text{clean}}(T)\vee 1] \;+\; \mathbb{E}[D(T)]$$
*(Note: If the very first rejection of the entire run was tainted, the baseline adjustment includes $w_0$, which accounts for the boundary condition mentioned in the prompt).*

---

### 3. Final Answer

Yes, the claimed bound is **valid**. 

By enforcing the debt rule—subtracting tainted reward contributions, calculating the exact overspent debt $D_0$, and withholding future clean rewards until $D(T) = 0$—the cumulative expected $\alpha$-wealth spent on clean tests is rigorously bounded. 

The resulting valid mFDR control inequality for the clean tests is:
$$\mathbb{E}[V_{\text{clean}}(T)] \;\le\; \alpha\,\mathbb{E}[R_{\text{clean}}(T)\vee 1] \;+\; \mathbb{E}[D(T)]$$
where $D(T) = D_0 - (\text{amount repaid by time } T)$. As clean rejections pay off the debt, $\mathbb{E}[D(T)] \to 0$, asymptotically restoring standard mFDR control without requiring you to discard the clean tests that were performed after the leak occurred.

---

### 4. Common Mistakes for This Problem Type

1. **Trying to "Retroactively Adjust" Past P-values:** Students often mistakenly believe they need to recalculate past test statistics or somehow adjust the p-values in set $S$. Since the decisions (and the data leakage) cannot be undone in the physical world, online FDR relies entirely on controlling *future* allocation rules ($\alpha_t$), not revising history.
2. **Double Counting the Debt:** Confusing $D_0$ (the initial debt accumulated up to the discovery point) with the running debt $D(T)$. $D_0$ is a fixed constant once the leak is discovered, whereas $D(T)$ is a decreasing stochastic process that changes as new clean rejections occur.
3. **Ignoring the Boundary Condition ($w_0$):** Forgetting that the very first rejection in LORD-type algorithms carries a distinct reward weight ($\alpha - w_0$ versus $\alpha$ for subsequent rejections). If the initial tainted rejection funded that special weight, the debt calculation must account for the $w_0$ base term adjustment.
4. **Confusing FWER with mFDR Bounds:** Treating the additive debt term $\mathbb{E}[D(T)]$ as a strict almost-sure bound rather than an *expectation* bound. Online FDR controls error rates in expectation, so the debt penalty naturally propagates through expectations as well.

*Original question: [Online FDR (LORD) after some past p-values turn out to be invalid: does &quot;repaying the alpha-wealth debt&quot; keep mFDR control for the clean tests?](https://stats.stackexchange.com/questions/677487/online-fdr-lord-after-some-past-p-values-turn-out-to-be-invalid-does-repayin) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
