---
layout: question
title: Probability that two rare events follow a dated trigger closely by pure random
  happenstance
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Probability that two rare events follow
  a dated trigger closely by pure random happenstance'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

# Probability that two rare events follow a dated trigger closely by pure random happenstance

## 1. Restatement in Plain Language

Imagine a woman casually mentions to a coworker that she loves orchids. This is our "trigger" event ($T$), occurring on Day 0. Shortly after, two unusual things happen to her at work:
1. **Event A:** An anonymous box of orchids arrives on her desk after $t_1$ days.
2. **Event B:** An anonymous dinner invitation arrives on her desk after $t_2$ days.

Naturally, we want to know if these events are connected to her comment, or if they just happened by pure coincidence ($H_0$). 

To evaluate the coincidence hypothesis ($H_0$), we model the arrival of orchids and dinner invitations as rare, independent random events over time. The core question is: **What is the probability that *both* of these rare events would happen to land within $t_1$ and $t_2$ days of the trigger purely by chance?** Furthermore, how do we properly account for alternative hypotheses (like only one event being connected, or the two events being connected to each other rather than the trigger), and how do we avoid falling into common statistical traps when interpreting the result?

---

## 2. Step-by-Step Solution

### Step 1: Evaluating the Poisson Process Model for $H_0$
Under the null hypothesis $H_0$, neither event is connected to the trigger or to each other. We model the occurrence of each event as a homogeneous Poisson process. 

Let:
* $a$ = expected number of orchid deliveries per year for a given worker.
* $b$ = expected number of anonymous dinner invitations per year for a given worker.
* Time $t$ is measured in days. Since rates are given per year, we express daily rates as $\frac{a}{365}$ and $\frac{b}{365}$.

The waiting time $T_A$ until the first event $A$ occurs follows an Exponential distribution with rate $\lambda_A = \frac{a}{365}$. The probability that event $A$ happens *at or before* time $t_1$ is the cumulative distribution function (CDF) of the exponential distribution:
$$P(A \le t_1) = 1 - e^{-\frac{a}{365} t_1}$$

Similarly, for event $B$ by time $t_2$:
$$P(B \le t_2) = 1 - e^{-\frac{b}{365} t_2}$$

### Step 2: Joint Probability Under Independence ($H_0$)
Because $H_0$ assumes the events are completely independent of the trigger and of each other, the joint probability that event $A$ occurs within $t_1$ days **and** event $B$ occurs within $t_2$ days is the product of their individual probabilities:
$$P(A \le t_1,\ B \le t_2 \mid H_0) = \left(1 - e^{-\frac{a}{365} t_1}\right) \left(1 - e^{-\frac{b}{365} t_2}\right)$$

For small rates and short time intervals (where $\lambda t \ll 1$), we use the Taylor series approximation $1 - e^{-x} \approx x$:
$$P(A \le t_1,\ B \le t_2 \mid H_0) \approx \left(\frac{a \, t_1}{365}\right) \left(\frac{b \, t_2}{365}\right)$$

This confirms that the student's initial mathematical setup for evaluating the joint coincidence probability under $H_0$ is correct.

---

### Step 3: Addressing Question 1 — Is this the right way to quantify the timing?
**Yes, but with an important caveat.** 
Using the Poisson/Exponential framework is mathematically sound for modeling rare, memoryless events. However, calculating the probability of an event happening *within* a specific observed window ($t_1$ and $t_2$) after a fixed point is technically a **p-value-style calculation** (specifically, the probability of observing a wait time *at least this short* by chance). 

The limitation is that $t_1$ and $t_2$ were determined *after* seeing when the events actually arrived ("post-hoc window selection"). If the analyst looks at the data and says, "Look, it happened in 23 days!", and uses $t_1 = 23$, they are conditioning on the observed data. To be strictly rigorous, one must account for the Family-Wise Error Rate or use a Bayesian framework where $t_1$ and $t_2$ are treated as random variables integrated over the parameter space.

---

### Step 4: Addressing Question 2 — How to handle $H_2$ and $H_3$?

To rigorously compare all hypotheses, we should frame this as a **Bayesian model selection problem** (calculating posterior probabilities using Bayes' Theorem) rather than just looking at $H_0$.

* **$H_0$ (Pure coincidence):** Both events occur randomly relative to $T$ and each other. The likelihood is the product of independent Poisson probabilities evaluated at $t_1$ and $t_2$.
* **$H_2$ (Only one connected to the trigger):** Suppose Event $A$ is caused by the trigger (so $t_1$ is tightly bound by a different, highly concentrated distribution, e.g., a Normal distribution centered near zero), while Event $B$ is completely random ($\sim \text{Poisson}(b)$). The joint likelihood becomes $P(A \text{ due to } T) \times P(B \le t_2 \mid H_0)$. We must sum over the two sub-cases: either $A$ is connected and $B$ is random, or $B$ is connected and $A$ is random.
* **$H_3$ (Connected to each other, but not $T$):** Here, $A$ and $B$ share a common hidden cause (e.g., a secret admirer workflow) that kicked off around the same time as the remark, but the remark itself ($T$) didn't cause them. Mathematically, this introduces a correlation between $A$ and $B$, meaning $P(A \le t_1, B \le t_2) \neq P(A \le t_1)P(B \le t_2)$. The joint waiting time would be modeled using a bivariate point process or a shared frailty model.

---

### Step 5: Addressing Question 3 — What assumptions would you challenge?
1. **Homogeneity of Rates ($a$ and $b$):** The model assumes baseline rates are constant across the year. In reality, workplace events may be seasonal (e.g., more gifts around holidays, office parties).
2. **Independence of Workers:** Does "a given worker" accurately reflect this specific office environment? Workplace dynamics often feature clustered social behaviors.
3. **The Definition of the Trigger ($T$):** Was the orchid remark truly isolated? People express likes and dislikes frequently; framing this specific remark as a strict "trigger" risks selection bias (the Texas Sharpshooter Fallacy—drawing a bullseye around bullet holes after they are fired).
4. **Independence of $A$ and $B$:** If a secret admirer is orchestrating both gifts, $A$ and $B$ are structurally dependent, violating $H_0$.

---

### Step 6: Addressing Question 4 — How should the result be stated?
The resulting probability (e.g., $0.00011$) is **not** "the probability that the events were unconnected." 

* **The Prosecutor's Fallacy / Inverse Probability Error:** $P(\text{Data} \mid H_0)$ is the probability of observing data *this extreme or more* **if** the null hypothesis is true. It is **not** $P(H_0 \mid \text{Data})$, which is the probability that the null hypothesis is true given the data.
* **Correct Statement:** *"Assuming that orchid deliveries and dinner invitations occur completely at random with baseline rates $a$ and $b$ (Null Hypothesis), the probability of observing both events manifest this quickly or quicker after the trigger is approximately $p$."* 
To find the actual probability that the events are unconnected, one must assign prior probabilities to $H_0, H_1, H_2,$ and $H_3$ and apply Bayes' theorem.

---

## 3. Final Answer

1. **Under $H_0$, the exact joint probability** that Event $A$ occurs within $t_1$ days and Event $B$ occurs within $t_2$ days is given by:
   $$P(A \le t_1,\ B \le t_2 \mid H_0) = \left(1 - e^{-\frac{a}{365} t_1}\right)\left(1 - e^{-\frac{b}{365} t_2}\right)$$
   For small values of $\frac{at_1}{365}$ and $\frac{bt_2}{365}$, this simplifies to the product of the individual linear approximations:
   $$\approx \frac{a\,t_1}{365} \cdot \frac{b\,t_2}{365}$$

2. **Hypotheses $H_2$ and $H_3$** require expanding the model beyond pure independence: $H_2$ mixes a deterministic/causal distribution for one event with a Poisson process for the other, while $H_3$ requires a bivariate dependent process (shared-cause model).

3. **Interpretation:** The resulting numerical output is a $p$-value ($P(\text{Data} \mid H_0)$), **not** the posterior probability that the events are unconnected.

---

## Common Mistakes

* **Confusing $P(\text{Data} \mid H_0)$ with $P(H_0 \mid \text{Data})$:** Assuming a small p-value means there is a $1 - p$ chance the events are genuinely connected. Without a Bayesian prior, you cannot state the probability that the null hypothesis is true.
* **Ignorance of Post-Hoc Selection:** Calculating the probability based *specifically* on the observed windows ($t_1, t_2$) without adjusting for the fact that you searched for patterns after the fact (multiple testing / Texas Sharpshooter Fallacy).
* **Treating Workplace Rates as Constant:** Forgetting that workplace social events (and gift-giving) are often non-homogeneous over time due to holidays, seasons, or office morale cycles.

*Original question: [Probability that two rare events follow a dated trigger closely by pure random happenstance](https://stats.stackexchange.com/questions/677561/probability-that-two-rare-events-follow-a-dated-trigger-closely-by-pure-random-h) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
