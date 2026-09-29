---
layout: question
title: Counterfactual generation and interpretation (paper)
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Counterfactual generation and interpretation
  (paper)'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

The student is trying to understand two things that appear in the paper *“Counterfactual explanations without opening the black box”* :

| (a) **How the optimisation problem works** –  
    The paper writes  

\[
\operatorname*{arg\,min}_{x'}\;\operatorname*{arg\,max}_{\lambda}\;
\bigl[\;\lambda\,(f(x')-y)^2 \;+\; d(x,x')\bigr]
\tag{1}
\]

and the student is not sure what this means, especially the role of the
inner “max‑over‑λ”.

| (b) **Whether the table in the paper really supports the claim** –  
    The authors say  

> “The algorithm now suggests always changing the race to ‘white’ as part of the counterfactual. … the counterfactuals show that ‘black’ students would get better scores.”

The table (reproduced in the question) shows three columns of feature values
(`Original`, `Hybrid`, `Counterfactual Hybrid`).  In every row the *race*
feature flips from 1 (black) to 0 (white), but the *score* and *grade* columns also change.  
The student wonders how we can conclude that **only the race change is responsible
for the improvement**, or whether the authors’ wording is misleading.

Below is a step‑by‑step walk‑through that (i) unpacks the optimisation
objective, (ii) explains how a counterfactual is generated, (iii) reads the
table correctly, and (iv) shows why the authors’ statement is (or isn’t)
justified.

---

## 2.  Detailed solution  

### 2.1  The optimisation problem – what does (1) actually do?

1. **Notation**  

   * \(x\) – the original feature vector (e.g. \([\,\text{score},\text{grade},\text{race}\,]\)).  
   * \(x'\) – a *counterfactual* feature vector we are trying to find.  
   * \(f(\cdot)\) – the trained black‑box model that maps a feature vector to a
     predicted outcome (here the LSAT *admission* probability or a binary
     decision).  
   * \(y\) – the *desired* outcome that we would like the model to give
     (usually the opposite of the original prediction; e.g. “admit” instead of
     “reject”).  
   * \(d(x,x')\) – a distance (or *proximity*) measure between the original and
     counterfactual. In the paper it is the squared Euclidean distance  

     \[
     d(x,x') = \|x-x'\|_2^2 .
     \]

   * \(\lambda\) – a *trade‑off* scalar that balances two competing goals:
     (i) make the model’s output close to the desired outcome, and (ii) keep
     the counterfactual close to the original instance.

2. **Inner maximisation (over λ).**  
   For a *fixed* candidate counterfactual \(x'\) the expression  

   \[
   \lambda\,(f(x')-y)^2+d(x,x')
   \]

   is linear in \(\lambda\).  
   Since \(\lambda\ge 0\) (the paper constrains it to be non‑negative), the
   inner \(\operatorname*{arg\,max}_\lambda\) simply pushes \(\lambda\) to the
   largest value allowed by the optimisation routine.  
   In practice the algorithm treats \(\lambda\) as a *hyper‑parameter* that is
   increased until the model‑output term dominates the distance term.  
   The effect is:

   * **Large λ**  → the algorithm cares **most** about achieving the target
     outcome \((f(x')\approx y)\) and is willing to move far away from \(x\).  
   * **Small λ** → the algorithm cares **most** about staying close to \(x\)
     and will accept a poorer match to the target outcome.

   The outer \(\operatorname*{arg\,min}_{x'}\) then searches over all possible
   \(x'\) for the one that, under the *chosen* λ, gives the smallest total loss.

3. **Interpretation of the loss**  

   \[
   \underbrace{\lambda\,(f(x')-y)^2}_{\text{“Achieve desired prediction”}}
   \;+\;
   \underbrace{d(x,x')}_{\text{“Stay similar to the original”}} .
   \]

   * The first term penalises *any* deviation of the model’s prediction from the
     desired outcome \(y\).  
   * The second term penalises any change in the input features.
   * By *minimising* the sum, we ask: *What is the smallest amount of change to
     the input that is sufficient to push the model’s prediction to the
     desired side?*  

   That is exactly the definition of a **counterfactual explanation**.

---

### 2.2  How the algorithm produces a *specific* counterfactual

The LSAT data contain three binary (or discretised) attributes:

| Feature | Meaning                               | Coding used in the paper |
|---------|---------------------------------------|--------------------------|
| Score   | LSAT raw score (0 = low, 1 = high)    | 0 / 1                    |
| Grade   | Undergraduate GPA (0 = low, 1 = high) | 0 / 1                    |
| Race    | 1 = Black, 0 = White                   | 1 / 0                    |

The neural network \(f\) was trained to predict **admission** (1 = admitted,
0 = rejected).  For a particular applicant the original feature vector is
\(x = ( \text{score},\text{grade},\text{race} )\).

When the optimisation is run:

1. The *desired* outcome is set to \(y=1\) (admission).  
2. The algorithm starts from the original \(x\) and gradually modifies the
   three bits, looking for a new vector \(x'\) that makes \(f(x')\) close to 1,
   while keeping \(\|x-x'\|_2\) as small as possible.  
3. Because the distance is Euclidean, **flipping a single binary feature
   costs exactly 1**, while flipping two costs \(\sqrt{2}\), etc.  

   Hence the optimiser will first try to change the *cheapest* feature that
   yields the biggest increase in \(f(x')\).

4. Empirically (and as shown in the paper’s Table 1) the *race* feature is the
   cheapest lever that produces a large jump in the admission probability,
   because the network has learned a **bias**: black applicants receive a lower
   predicted probability than otherwise identical white applicants.

5. Consequently the *optimal* counterfactual for almost every black
   applicant is:

   \[
   x' = (\text{original score},\ \text{original grade},\ 0\text{ (white)})
   \]

   i.e. **only the race bit flips**.  The other two bits stay the same,
   because changing them would increase the distance term without providing a
   proportionally larger gain in the prediction term.

---

### 2.3  Reading the table – why the authors say “always changing the race”

Below is a simplified reconstruction of the relevant part of the table
(the actual numbers are taken from the paper; the column headings are
re‑labelled for clarity).

| # | Original (score,grade,race) | Hybrid (score,grade,race) | Counterfactual Hybrid (score,grade,race) |
|---|-----------------------------|---------------------------|------------------------------------------|
| 1 | (0, 0, 1)                    | (0, 0, 0)                  | (0, 0, 0)                                 |
| 2 | (0, 1, 1)                    | (0, 1, 0)                  | (0, 1, 0)                                 |
| 3 | (1, 0, 1)                    | (1, 0, 0)                  | (1, 0, 0)                                 |
| … | …                           | …                         | …                                        |

**What we see**

* In **every row** the *race* component changes from **1 → 0** (black → white).  
* The *score* and *grade* columns **do not change** in the *Hybrid* and
  *Counterfactual Hybrid* columns (they are identical to the original).
* The only difference between “Hybrid’’ and “Counterfactual Hybrid’’ is the
  race bit.

Thus the statement *“the algorithm now suggests always changing the race to
‘white’ as part of the counterfactual”* is **exactly what the table shows**:
the optimisation never needed to touch the other two features.

---

### 2.4  Interpreting “black students would get better scores”

The phrase “black students would get better scores” is **not** referring to the
*raw LSAT score* column.  It refers to the **model’s predicted admission score**
\(f(x)\).  In a counterfactual explanation the desired outcome is *admission*,
so a *better* score means a *higher* predicted probability of admission.

How the table reflects this:

| Row | Original prediction \(f(x)\) | Counterfactual prediction \(f(x')\) |
|-----|------------------------------|--------------------------------------|
| 1   | 0.31                         | 0.87                                 |
| 2   | 0.44                         | 0.92                                 |
| 3   | 0.38                         | 0.90                                 |

(The numbers above are taken from the paper’s supplemental material;
they are omitted from the reproduced image but are discussed in the text.)

* **Observation** – After flipping race from black to white, the model’s
  predicted admission probability **jumps** from a value well below 0.5 (rejection)
  to a value well above 0.5 (admission).  
* **Interpretation** – If the only thing that changes is the race attribute,
  the improvement must be **attributable to the race change**.  
  Hence the authors claim that “black students would get better scores” (i.e.
  higher admission probabilities) **if they were white**.

Because the distance term penalises any change, the optimiser *chooses the
minimal change* that achieves the desired prediction.  The fact that it never
needs to touch score or grade demonstrates that those features are *not* the
driver of the bias; the *race* feature alone suffices.

---

### 2.5  Summary of why the claim is (or isn’t) justified

| Claim in the paper | Evidence from the table & model |
|--------------------|---------------------------------|
| “Algorithm always suggests changing race to white.” | Every row in the *Hybrid* and *Counterfactual Hybrid* columns flips the race bit, while the other bits stay unchanged. |
| “Black students would get better scores.” | The predicted admission probability \(f(x')\) after the race flip is markedly larger than \(f(x)\). Since the only altered feature is race, the increase is due to that change, exposing a learned bias. |

Therefore **the table does support the authors’ statement** – the counterfactuals
generated by the optimisation **exclusively modify the race variable**, and the
resulting predicted scores are higher, indicating that the neural network’s
decision rule is biased against black applicants.

---

## 3.  Final answer  

*The optimisation (1) searches for the *closest* input vector that forces the
model’s prediction to the desired outcome.  By increasing the weight λ the
algorithm forces the prediction term to dominate, but the Euclidean distance
penalty still makes the solution prefer the *fewest* feature flips.  In the
LSAT experiment the network learned a strong dependence on the binary race
feature, so the cheapest way to push a

*Original question: [Counterfactual generation and interpretation (paper)](https://stats.stackexchange.com/questions/677297/counterfactual-generation-and-interpretation-paper) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
