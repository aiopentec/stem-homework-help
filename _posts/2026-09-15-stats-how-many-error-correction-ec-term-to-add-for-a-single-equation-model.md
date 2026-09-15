---
layout: question
title: How many error correction (EC) term to add for a single equation model?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: How many error correction (EC) term
  to add for a single equation model?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

You have a *single‑equation* ARIMAX (or error‑correction) model  

\[
y_t = \beta_0+\beta_1x_{1,t}+\dots+\beta_5x_{5,t}+ \text{(error‑correction terms)} + u_t,
\]

where the dependent variable \(y_t\) and all five regressors \(x_{i,t}\) are integrated of order 1, \(I(1)\).

The student is told that some of the series move together in the long run (they share a **stochastic trend**).  
The questions are:

1. If  

   * \(y_t,\,x_{1,t},\,x_{2,t},\,x_{3,t}\) share **one** common stochastic trend, and  
   * \(y_t,\,x_{4,t},\,x_{5,t}\) share **another** common stochastic trend,  

   how many error‑correction (EC) terms should be put into the *single* equation for \(y_t\)?

2. If, in addition, \(x_{2,t}\) and \(x_{3,t}\) also share a *third* stochastic trend that is **different** from the two trends above, how many EC terms are now required?

In other words: **Given the long‑run relationships, what is the rank of the error‑correction (Π) matrix that is relevant for the equation of \(y_t\)?**



--------------------------------------------------------------------

## 2.  Step‑by‑step solution

### 2.1  Basic concepts

| Symbol | Meaning |
|--------|---------|
| \(k\) | Number of variables in the *system* (here \(k = 6\): \(y\) plus five \(x\)’s). |
| \(\Pi\) | Long‑run impact matrix in the vector error‑correction representation (VECM). |
| \(\text{rank}(\Pi)=r\) | Number of **linearly independent cointegrating vectors** (i.e. number of EC terms you could have in a *full* VECM). |
| Number of stochastic trends = \(k-r\). |
| In a **single‑equation** ECM for \(y\) we only need the cointegrating vectors that involve \(y\). Call this number \(r_y\). It is **not** necessarily equal to the full system rank \(r\). |

Thus we have to (i) infer the *total* number of stochastic trends, (ii) compute the system rank \(r = k - (\text{# trends})\), and finally (iii) count how many of the \(r\) cointegrating vectors contain \(y\).

---

### 2.2  Scenario 1  
> *\(y, x_1, x_2, x_3\) share one trend; \(y, x_4, x_5\) share another trend.*

1. **Identify distinct stochastic trends**  
   *Trend A* is common to \(\{y, x_1, x_2, x_3\}\).  
   *Trend B* is common to \(\{y, x_4, x_5\}\).  

   There is **no information** that these two trends are the same, so we treat them as **two independent** stochastic trends.

2. **How many trends in total?**  
   Since the two groups overlap only through \(y\), the two trends are distinct.  
   \[
   \#\text{trends}=2.
   \]

3. **System rank** (the number of independent cointegrating relations in the *full* 6‑variable system)  
   \[
   r = k - (\#\text{trends}) = 6 - 2 = 4.
   \]

   So a *full* VECM would contain 4 EC terms.

4. **How many of those 4 involve \(y\)?**  
   * From Trend A we can form a cointegrating vector that includes \(y, x_1, x_2, x_3\).  
   * From Trend B we can form a cointegrating vector that includes \(y, x_4, x_5\).  

   Any other linear combination of the four vectors that is independent of the two above will **not** involve \(y\) (they will be linear combinations of the regressors only). Hence the number of *distinct* cointegrating relations **containing \(y\)** is

   \[
   r_y = 2 .
   \]

5. **Answer for (1)**  

   **You need 2 error‑correction terms in the single‑equation model for \(y_t\).**  
   The full system rank is 4, but only two of those four EC terms are relevant for the equation of \(y\).

---

### 2.3  Scenario 2  
> *In addition to the relationships above, \(x_{2,t}\) and \(x_{3,t}\) share a **third** stochastic trend.*

1. **Add the new trend**  
   *Trend C* is common only to \(\{x_2, x_3\}\) and is independent of Trends A and B.

2. **Total number of distinct stochastic trends**  

   \[
   \#\text{trends}=3 .
   \]

3. **System rank**  

   \[
   r = k - (\#\text{trends}) = 6 - 3 = 3 .
   \]

   The full VECM would now have three cointegrating vectors.

4. **Which of those three involve \(y\)?**  

   *Vector 1* – from Trend A (contains \(y, x_1, x_2, x_3\)).  
   *Vector 2* – from Trend B (contains \(y, x_4, x_5\)).  
   *Vector 3* – from Trend C (contains only \(x_2, x_3\)).  

   Only the first two involve the dependent variable \(y\).

   Therefore  

   \[
   r_y = 2 .
   \]

5. **Answer for (2)**  

   **You still need 2 error‑correction terms in the equation for \(y_t\).**  
   The extra stochastic trend adds a third cointegrating relation, but it does not involve \(y\), so it does not enter the single‑equation ECM.

---

## 3.  Final answers

| Situation | Total stochastic trends | System rank \(r\) | Cointegrating vectors that contain \(y\) (\(r_y\)) | # EC terms to include in the *single‑equation* model |
|-----------|--------------------------|-------------------|----------------------------------------------|---------------------------------------------------|
| 1. Two overlapping groups (A & B) | 2 | \(6-2 = 4\) | 2 | **2** |
| 2. Add a third trend involving only \(x_2, x_3\) | 3 | \(6-3 = 3\) | 2 | **2** |

--------------------------------------------------------------------

## 4.  Common Mistakes

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing the system rank \(r\) with the number of EC terms needed for a single equation.** | The rank tells you how many *total* cointegrating relations exist in the whole vector of variables. Only those that contain the dependent variable matter for its ECM. | First determine the total rank, then count how many independent cointegrating vectors actually involve the dependent variable. |
| **Counting each variable that shares a trend as a separate EC term.** | If several variables share the *same* stochastic trend, they generate **one** cointegrating relation, not one per variable. | A group of variables that moves together on one trend contributes **one** EC term (the linear combination that eliminates the trend). |
| **Assuming overlapping groups automatically give more EC terms.** | Overlap (e.g., \(y\) appears in both groups) does not multiply the number of independent relations; it just indicates that \(y\) participates in more than one relation. | Identify the *distinct* stochastic trends; each distinct trend reduces the rank by one, regardless of overlap. |
| **Treating a trend that only involves regressors as relevant for the dependent‑variable equation.** | An EC term that contains only regressors cannot be entered into the equation for \(y\); it would be collinear with the regressors. | After you have the full set of cointegrating vectors, drop any that do not contain the dependent variable when writing the single‑equation ECM. |
| **Leaving out an EC term because it looks “redundant”.** | Two EC terms may look similar but can be linearly independent; dropping one can miss a genuine long‑run equilibrium relationship. | Verify linear independence (e.g., by checking the rank of the matrix of cointegrating vectors) before discarding any term. |

Keeping these

*Original question: [How many error correction (EC) term to add for a single equation model?](https://stats.stackexchange.com/questions/677182/how-many-error-correction-ec-term-to-add-for-a-single-equation-model) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
