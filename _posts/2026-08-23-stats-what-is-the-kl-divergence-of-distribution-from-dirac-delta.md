---
layout: post
title: What is the KL divergence of distribution from Dirac delta?
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. What is being asked in plain language

We want to calculate the Kullback–Leibler (KL) divergence from a standard continuous probability distribution $P(x)$ to a Dirac delta distribution $Q(x) = \delta(x - x_0)$. 

The KL divergence measures how "different" one probability distribution is from another. In this case, $Q$ is a Dirac delta function, which represents a distribution where all of the probability mass is infinitely concentrated at a single point, $x_0$. 

The main mathematical challenge in this calculation is handling the term $\log[\delta(x - x_0)]$ inside the integral. Since the Dirac delta function is zero everywhere except at $x = x_0$ (where it is formally $\infty$), taking its logarithm leads to expressions like $\log(0)$ and $\log(\infty)$. This walkthrough demonstrates how to rigorously evaluate this expression.

---

### 2. Step-by-step solution

#### Step 1: Write down the definition of KL divergence
The KL divergence for two continuous probability distributions $P(x)$ and $Q(x)$ is given by:
$$D_{KL}(P \mid\mid Q) = \int_{-\infty}^{\infty} P(x) \log{\left[\frac{P(x)}{Q(x)}\right]} \, dx$$

#### Step 2: Expand the logarithm
Using the logarithmic property $\log(a/b) = \log(a) - \log(b)$, we can split the integral into two parts:
$$D_{KL}(P \mid\mid Q) = \int_{-\infty}^{\infty} P(x) \log[P(x)] \, dx - \int_{-\infty}^{\infty} P(x) \log[Q(x)] \, dx$$

#### Step 3: Substitute the Dirac delta function
Now, substitute $Q(x) = \delta(x - x_0)$ into the equation:
$$D_{KL}(P \mid\mid Q) = \int_{-\infty}^{\infty} P(x) \log[P(x)] \, dx - \int_{-\infty}^{\infty} P(x) \log[\delta(x - x_0)] \, dx$$

#### Step 4: Evaluate the second integral using the sifting property
The second integral contains the Dirac delta function multiplied by $P(x)\log[\delta(x - x_0)]$. 

Recall the fundamental **sifting property** (or sampling property) of the Dirac delta function, which states that for any continuous function $f(x)$:
$$\int_{-\infty}^{\infty} f(x) \delta(x - x_0) \, dx = f(x_0)$$

Here, our function $f(x)$ is $P(x) \log[\delta(x - x_0)]$. Applying the sifting property gives:
$$\int_{-\infty}^{\infty} P(x) \log[\delta(x - x_0)] \, dx = P(x_0) \log[\delta(0)]$$

#### Step 5: Address the evaluation at $x = x_0$
Mathematically, the value of the Dirac delta function at its center, $\delta(0)$, is strictly undefined (it diverges to infinity). Consequently, $\log[\delta(0)] = \log(\infty) = \infty$.

Assuming $P(x_0) > 0$, the second term evaluates to:
$$P(x_0) \log[\delta(0)] = \infty$$

Therefore, the KL divergence becomes:
$$D_{KL}(P \mid\mid Q) = \int_{-\infty}^{\infty} P(x) \log[P(x)] \, dx - \infty$$

Depending on whether the first term (negative differential entropy of $P$) is finite, subtracting infinity results in a divergence to negative infinity. 

---

### 3. Final Answer

The KL divergence of a continuous distribution $P(x)$ from a Dirac delta distribution $Q(x) = \delta(x - x_0)$ is **undefined** (or evaluates to **$-\infty$**):

$$D_{KL}(P \mid\mid Q) = -\infty \quad (\text{when } P(x_0) > 0)$$

*(Note: In information theory, KL divergence is technically undefined or infinite when the support of $P$ is not absolutely continuous with respect to the support of $Q$. Since $Q$ has support only at a single point $x_0$, the KL divergence $D_{KL}(P \mid\mid Q)$ is infinite/undefined for any non-degenerate continuous distribution $P$.)*

---

### 4. Common Mistakes

* **Treating the Dirac delta like a standard PDF:** Students often try to treat $\delta(x)$ as a regular function whose values can be manipulated algebraically (e.g., trying to write $\log(\delta(x)) = \log(0)$ for $x \neq x_0$ and integrating piece-by-piece). The Dirac delta is a generalized function (distribution) and must be integrated against a test function using its sifting property.
* **Confusing the direction of KL divergence:** This problem specifically asks for $D_{KL}(P \mid\mid Q)$ where $Q$ is the Dirac delta. Reversing the order to compute $D_{KL}(Q \mid\mid P)$ is a completely different calculation (and actually results in a finite value, representing the negative differential entropy of $P$ evaluated at $x_0$).
* **Ignoring support constraints:** KL divergence requires that $Q(x) > 0$ wherever $P(x) > 0$ (absolute continuity). Because a Dirac delta is zero everywhere except at $x_0$, it assigns zero probability to regions where $P(x)$ is positive, leading to a breakdown in the definition.

*Original question: [What is the KL divergence of distribution from Dirac delta?](https://stats.stackexchange.com/questions/292049/what-is-the-kl-divergence-of-distribution-from-dirac-delta) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
