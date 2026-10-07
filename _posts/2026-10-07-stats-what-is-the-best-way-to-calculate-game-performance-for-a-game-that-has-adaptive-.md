---
layout: question
title: What is the best way to calculate game performance for a game that has adaptive
  difficulty over time?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: What is the best way to calculate
  game performance for a game that has adaptive difficulty over time?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (plain‑language restatement)

A player tries to hit a moving ball with a racket.  

* After **each successful hit** the racket becomes smaller → the next hit is **harder**.  
* After a **miss** the racket snaps back to its original size.  

A round lasts **30 min**.  
We have several rounds for each player and we also have a **control condition** in which the racket does **not move** (so hits can be produced just by chance).

The goal is to compress everything that happened in a round into **one number** that tells us “how well the player performed”:

* it must reward many *hard* hits and punish many *easy* misses,
* it must be comparable across rounds that contain different numbers of attempts,
* it must take into account the chance‑level hit probability that we have measured in the control condition.

In short – we need a **single, normalised performance metric** that explicitly accounts for the adaptive difficulty (the shrinking racket) and for the baseline chance level.

---

## 2.  Step‑by‑step construction of a suitable metric  

Below is a complete, reproducible recipe.  All symbols are defined in the **Notation** box.

### Notation  

| Symbol | Meaning |
|--------|---------|
| \(S_0\) | initial racket size (the size after a miss) |
| \(\alpha\) | shrink factor after a hit, \(0<\alpha<1\) (e.g. \(\alpha=0.9\) means the racket becomes 10 % smaller) |
| \(S_j\) | racket size **just before** attempt \(j\) |
| \(y_j\) | observed outcome of attempt \(j\): \(y_j=1\) for a hit, \(y_j=0\) for a miss |
| \(p(S)\) | probability of a hit when the racket has size \(S\) *in the control (stationary) condition* |
| \(n\) | total number of attempts made in the 30‑min round |
| \(L\) | log‑likelihood of the observed sequence under the model \(p(S_j)\) |
| \(\hat L_{\text{chance}}\) | log‑likelihood we would obtain if every attempt were drawn from the *overall* chance level (the mean of \(p(S)\) over all possible sizes) |
| \(Z\) | final normalised performance score (a z‑score) |

---

### 2.1  Estimate the *baseline* hit probability as a function of racket size  

1. **Collect control data** – play many trials with the racket stationary, but present the same range of sizes (e.g. \(S=S_0, \alpha S_0, \alpha^2 S_0,\dots\)).  
2. For each size \(S\) compute  

\[
\hat p(S)=\frac{\text{# hits at size }S}{\text{# attempts at size }S}.
\]

   If you have few observations per size, fit a smooth monotone curve (e.g. logistic regression) to obtain a continuous function \(\hat p(S)\).  
   This curve gives the **chance‑level probability** of a hit **solely because of the size**, i.e. what a player would achieve without any skill.

---

### 2.2  Re‑create the *size trajectory* for a 30‑min round  

Starting with the initial size \(S_0\):

```
S ← S0
for j = 1 … n
        record Sj = S
        observe yj (hit =1, miss =0)
        if yj == 1          # hit
                S ← α·S      # shrink
        else                # miss
                S ← S0       # reset
```

At the end you have a list \(\{S_1,S_2,\dots,S_n\}\) that tells you how difficult each attempt was.

---

### 22.3  Compute the *expected* hit probability for each attempt  

For every attempt \(j\),

\[
\pi_j \;=\; \hat p(S_j).
\]

\(\pi_j\) is the probability that a **random (chance) player** would succeed on that exact difficulty level.

---

### 2.4  Compare the observed outcomes with the chance expectations  

A natural way to do this is a **standardised sum of residuals**, i.e. a *z‑score* that tells us how many standard deviations the player’s performance deviates from chance.

1. **Mean of the chance model** for this round  

\[
\mu = \sum_{j=1}^{n}\pi_j .
\]

2. **Variance of the chance model** (Bernoulli trials are independent conditional on the size)

\[
\sigma^2 = \sum_{j=1}^{n}\pi_j(1-\pi_j).
\]

3. **Observed total hits**

\[
H = \sum_{j=1}^{n} y_j .
\]

4. **Standardised performance score**

\[
\boxed{ \; Z \;=\; \frac{H-\mu}{\sqrt{\sigma^{2}}}\;}
\]

Interpretation  

* \(Z\approx 0\): the player performed about as well as chance given the sequence of difficulties.  
* \(Z>0\): better than chance (the larger, the better).  
* \(Z<0\): worse than chance.

Because \(\mu\) and \(\sigma^{2}\) are *weighted* by the size‑specific chance probabilities, a hit when the racket is tiny (small \(\pi_j\)) contributes **much more** to the numerator than a hit when the racket is large.  Likewise, a miss on a tiny racket is penalised more because it reduces \(\sigma^{2}\) less than a miss on an easy size.

---

### 2.5  Optional: convert the z‑score to a bounded “percentage‑score”

If you prefer a metric that lies between 0 % and 100 % you can map the z‑score through the normal CDF:

\[
\text{Score}_{\%}= 100 \times \Phi(Z),
\]

where \(\Phi\) is the standard normal cumulative distribution function.  
A perfect player (hits on every trial) would have a very large positive \(Z\) and a score close to 100 %; a player who never hits would have a score close to 0 %.

---

### 2.6  Summary of the algorithm (pseudocode)

```python
# INPUT:  S0, alpha, control data (sizes, hits), list of attempts (hit/miss)
# OUTPUT: Z (normalised performance)

# 1. Fit p_hat(S) from control data
p_hat = fit_prob_function(control_sizes, control_hits)   # e.g. logistic regression

# 2. Reconstruct size sequence for the round
S = S0
sizes = []
for outcome in attempts:          # attempts is a list of 0/1
    sizes.append(S)
    if outcome == 1:             # hit
        S = alpha * S
    else:                        # miss
        S = S0

# 3. Compute chance probabilities for each attempt
pi = [p_hat(s) for s in sizes]

# 4. Compute μ, σ² and H
mu   = sum(pi)
sigma2 = sum(p*(1-p) for p in pi)
H = sum(attempts)

# 5. Z‑score
Z = (H - mu) / (sigma2**0.5)
```

The same code can be run for every 30‑min round; the resulting \(Z\) values are directly comparable across rounds and across participants.

---

## 3.  Final answer  

The **recommended single normalised performance metric** is the **z‑score**

\[
\boxed{ Z \;=\; \dfrac{\displaystyle\sum_{j=1}^{n} y_j \;-\; \displaystyle\sum_{j=1}^{n}\hat p(S_j)}
               {\sqrt{\displaystyle\sum_{j=1}^{n}\hat p(S_j)\bigl[1-\hat p(S_j)\bigr]}} }
\]

where  

* \(\hat p(S_j)\) is the hit probability obtained from the stationary‑racket (control) condition for the racket size that existed just before attempt \(j\),  
* the sequence \(\{S_j\}\) is generated by shrinking the racket after each hit (multiply by \(\alpha\)) and resetting it after each miss,  
* the numerator is the **excess number of hits** over what chance would predict for that exact difficulty sequence, and  
* the denominator is the **standard deviation** of the chance‑level prediction, turning the excess into a **standardised score** that can be compared across rounds of different length and difficulty.

If a bounded 0‑100 % value is preferred, transform the z‑score with the normal CDF:  

\[
\text{Performance}_{\%}=100\;\Phi(Z).
\]

---

## 4.  Common mistakes (and how to avoid them)

| Mistake | Why it’s wrong | Correct approach |
|---------|----------------|------------------|
| **Treat every hit as equally valuable** (e.g., `hits / attempts`). | Ignores that a hit while the racket is tiny is far harder than a hit with a large racket. | Weight each trial by the *chance* probability of success at that size (the \(\pi_j\) terms) before aggregating. |
| **Use a single overall chance probability** (e.g., overall hit rate in the control condition) for all trials. | The difficulty changes within a round; a single average chance level does not reflect that a tiny racket is much harder. | Estimate \(\hat p(S)\) as a function of size and evaluate it **for each individual attempt**. |
| **Subtract the expected number of hits but forget the variance**. | Gives a raw difference that is not comparable across rounds with different numbers of attempts or different difficulty distributions. | Standardise the difference by the square‑root of the variance (the denominator in the z‑score). |
| **Ignore the reset rule after a miss** and assume the racket shrinks continuously. | Over‑estimates difficulty after a miss, leading to biased scores. | Re‑create the exact size trajectory using the reset rule before computing \(\pi_j\). |
| **Use the observed hit rate from the control condition as the “chance level”.** | That observed rate already mixes skill and chance; it is not a pure baseline. | Derive \(\hat p(S)\) from the control condition **where the player has no skill advantage** (e.g., the racket is stationary and the player cannot aim). |
| **Report only the raw z‑score** without checking its magnitude. | Very large positive or negative values may indicate that the normal‑approximation (used to compute the denominator) is poor (e.g., when \(n\) is tiny). | Verify that the number of attempts \(n\) is large enough (rule of thumb: each \(\pi_j\) not too close to 0 or 1) or use an exact binomial‑likelihood ratio instead of the normal approximation. |

Avoiding these pitfalls ensures the final metric truly reflects **skillful performance under an ever‑increasing difficulty** and is comparable across sessions and participants.

*Original question: [What is the best way to calculate game performance for a game that has adaptive difficulty over time?](https://stats.stackexchange.com/questions/677361/what-is-the-best-way-to-calculate-game-performance-for-a-game-that-has-adaptive) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
