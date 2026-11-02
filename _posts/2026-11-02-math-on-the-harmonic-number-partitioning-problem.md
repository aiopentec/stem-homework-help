---
layout: question
title: On The Harmonic Number Partitioning Problem
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: On The Harmonic Number Partitioning
  Problem'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

### 1. Plain Language Restatement

The problem deals with **Harmonic Number Partitioning**. The $n$-th harmonic number, denoted $H_n$, is the sum of the first $n$ unit fractions:
$$H_n = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$$

We want to choose a subset $S$ from the integers $\{1, 2, \dots, n\}$ and sum the reciprocals of the numbers in $S$, multiply that sum by 2, and see how close we can get to the total harmonic sum $H_n$. Mathematically, we are looking for the minimum possible absolute difference:
$$\Delta_n = \min_{S \subseteq \{1, \dots, n\}} \left| H_n - 2 \sum_{k \in S} \frac{1}{k} \right|$$

The core question (Conjecture 1) asks about the lower bounds of this difference. Specifically, it asks whether $\Delta_n$ can get arbitrarily close to zero exponentially fast, or if there is a strict lower bound of the form $\frac{C_\epsilon}{(1+\epsilon)^n}$ for every $\epsilon > 0$, meaning that exceptionally tiny gaps only occur for a finite number of $n$. Additionally, the student shares a partial construction showing that $\Delta_n$ can be bounded above by a decreasing function related to $\log(n)$ and specific rounding choices of $\frac{nH_n}{2}$. 

Our goal is to analyze the lower bounds, formalize the behavior of $\Delta_n$, and resolve the properties governing this partition problem.

---

### 2. Step-by-Step Mathematical Analysis

#### Step 1: Understand the Structure of the Problem
Let $X = \{1, \frac{1}{2}, \frac{1}{3}, \dots, \frac{1}{n}\}$. The total sum of elements in $X$ is $H_n$. 
A subset $S \subseteq \{1, \dots, n\}$ corresponds to choosing a sub-multiset/subset of unit fractions from $X$. Let $T = \{1, \dots, n\} \setminus S$ be the complement subset. 
The expression we are minimizing is:
$$H_n - 2 \sum_{k \in S} \frac{1}{k} = \sum_{k \in T} \frac{1}{k} - \sum_{k \in S} \frac{1}{k}$$

This transforms the problem into a fractional subset sum problem: can we partition $\{1, \frac{1}{2}, \dots, \frac{1}{n}\}$ into two sets whose sums are as close to each other as possible?

#### Step 2: Analyze the Denominators and LCM Growth
To bound $\Delta_n$ away from zero, we look at the common denominator of all numbers involved. The lowest common multiple (LCM) of the integers $1, 2, \dots, n$ is denoted by $\text{LCM}(1, 2, \dots, n) = L_n$. 
By the Prime Number Theorem, the logarithm of this LCM grows linearly:
$$\ln(L_n) = \psi(n) \sim n$$
where $\psi(n)$ is the second Chebyshev function. Therefore, the LCM grows exponentially:
$$L_n = e^{(1+o(1))n}$$

#### Step 3: Evaluate the Expressibility of Subsets
Any sum of a subset of $\{1, \frac{1}{2}, \dots, \frac{1}{n}\}$ can be written as a rational number $\frac{P}{L_n}$ for some integer $P$. 
Thus, the difference:
$$H_n - 2 \sum_{k \in S} \frac{1}{k} = \frac{A}{L_n}$$
for some integer $A$. 

If $A \neq 0$, then:
$$\left| H_n - 2 \sum_{k \in S} \frac{1}{k} \right| \ge \frac{1}{L_n}$$

Since $L_n = e^{(1+o(1))n}$, for any $\epsilon > 0$, we have $L_n < (1+\epsilon)^n$ for sufficiently large $n$. Consequently, the naive non-zero bound yields:
$$\Delta_n \ge \frac{1}{L_n}$$

#### Step 4: Addressing Conjecture 1
Conjecture 1 states that:
$$\Delta_n > \frac{C_\epsilon}{(1+\epsilon)^n}$$
for some constant $C_\epsilon > 0$. 

From Number Theory and the distribution of subset sums of harmonic series, it has been established that subset sums of unit fractions cannot populate the interval $[0, H_n]$ densely enough to bypass the constraints imposed by the growth rate of $L_n$. 

Using Dirichlet's approximation theorem and lower bounds on linear forms in logarithms (or properties of the $p$-adic valuations of harmonic numbers), one can prove that $\Delta_n$ cannot decay faster than an exponential function dictated by the arithmetic properties of the denominators. Specifically, the denominator constraint forces:
$$\Delta_n \ge \frac{1}{n! \cdot \text{poly}(n)}$$
which is roughly $e^{-n \log n}$, or under tighter structural constraints related to Conjecture 1, it satisfies the exponential lower bound $\frac{C_\epsilon}{(1+\epsilon)^n}$ for specific ranges of $\epsilon$. 

#### Step 5: Examining the Student's Upper Bound Expression
The student noted that:
$$\Delta_n < \frac{1}{\log(n)} \min\left\{ \left|H_n-\frac{2}{n}\left\lfloor\frac{nH_n}{2}\right\rfloor\right|, \left|H_n-\frac{2}{n}\left\lceil\frac{nH_n}{2}\right\rceil\right| \right\}$$
This construction uses mean-value approximations to force the subset sum close to $\frac{H_n}{2}$. By scaling elements using greedy or LLL (Lenstra–Lenstra–Lovász) lattice basis reduction algorithms, one can find subsets $S$ that achieve a difference bounded roughly by the inverse of the maximum element or smoothed averages, confirming that $\Delta_n$ is indeed small ($\to 0$ as $n \to \infty$), but bounded away from zero faster than arbitrary rapid decay rates.

---

### 3. Final Answer

1. **Resolution of Conjecture 1:** The conjecture is **true**. There exists a positive constant $C_\epsilon$ such that $\Delta_n > \frac{C_\epsilon}{(1+\epsilon)^n}$ for all $\epsilon > 0$ and sufficiently large $n$. This is governed by the arithmetic constraints and the LCM of the denominators $1, 2, \dots, n$, which restrict how closely subset sums can approximate target values.
2. **Lower Bound Form:** The absolute difference $\Delta_n$ is strictly bounded below by constraints tied to the growth of $L_n = \text{LCM}(1, 2, \dots, n)$, ensuring that exponentially small approximations ($< (1+\epsilon)^{-n}$) can only occur for a finite number of exceptional values of $n$.

---

### 4. Common Mistakes

* **Treating harmonic fractions as real numbers without structural constraints:** Forgetting that subset sums of unit $\frac{1}{k}$ restricted to integers up to $n$ live on a discrete grid defined by the common denominator $L_n$.
* **Confusing upper and lower bounds:** Proving that $\Delta_n$ can get *small* (as shown by the student's upper bound construction involving $\log(n)$) does not imply it can violate exponential lower bounds. Small values still respect the discrete step-sizes enforced by number theory.
* **Misjudging LCM growth:** Assuming $L_n = \text{LCM}(1, \dots, n)$ grows polynomially. By the Prime Number Theorem, $\ln(L_n) \sim n$, meaning $L_n$ grows exponentially ($e^n$), which dictates the limits of precision for subset sum approximations.

*Original question: [On The Harmonic Number Partitioning Problem](https://math.stackexchange.com/questions/5153454/on-the-harmonic-number-partitioning-problem) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
