---
layout: question
title: How can I generalize the multiplication rule of probability for more than two
  events?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: How can I generalize the multiplication
  rule of probability for more than two events?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking  

We know the **multiplication rule for two events**

\[
P(A\cap B)=P(A)\,P(B\mid A).
\]

The student wants to know how this rule extends when we have **many** events  
\(A_{1},A_{2},\dots ,A_{n}\).  
In other words, we must show (or *derive*) that

\[
\boxed{\;
P\Bigl(\bigcap_{i=1}^{n} A_{i}\Bigr)=
P(A_{1})\;
P(A_{2}\mid A_{1})\;
P(A_{3}\mid A_{1}\cap A_{2})\;
\cdots\;
P\bigl(A_{n}\mid A_{1}\cap\cdots\cap A_{n-1}\bigr)
\;}
\]

and we want an intuitive, step‑by‑step explanation, not just a terse “by induction” proof.

---

## 2.  Derivation from the definition of conditional probability  

### 2.1  The definition we start from  

For any two events \(X\) and \(Y\) with \(P(Y)>0\),

\[
P(X\mid Y)=\frac{P(X\cap Y)}{P(Y)}\qquad\Longleftrightarrow\qquad
P(X\cap Y)=P(Y)\,P(X\mid Y). \tag{1}
\]

Equation (1) is exactly the two‑event multiplication rule.

### 2.2  Three events  

Take three events \(A_{1},A_{2},A_{3}\) (assume each intersection we use has positive probability).  
Apply (1) to the pair  

\[
X = A_{3},\qquad Y = A_{1}\cap A_{2}.
\]

Then

\[
P(A_{3}\cap A_{1}\cap A_{2}) = P(A_{1}\cap A_{2})\;P\bigl(A_{3}\mid A_{1}\cap A_{2}\bigr). \tag{2}
\]

But we still have the factor \(P(A_{1}\cap A_{2})\).  
Apply (1) again, now with  

\[
X = A_{2},\qquad Y = A_{1}.
\]

\[
P(A_{1}\cap A_{2}) = P(A_{1})\;P(A_{2}\mid A_{1}). \tag{3}
\]

Insert (3) into (2):

\[
\begin{aligned}
P(A_{1}\cap A_{2}\cap A_{3})
&= \bigl[ P(A_{1})\,P(A_{2}\mid A_{1}) \bigr]\;
   P\bigl(A_{3}\mid A_{1}\cap A_{2}\bigr)\\[2mm]
&= P(A_{1})\;P(A_{2}\mid A_{1})\;P(A_{3}\mid A_{1}\cap A_{2}).
\end{aligned}
\]

Thus the rule holds for three events.

### 2.3  The pattern becomes clear  

When we added the third event we:

1. **Isolated the last event** using (1) with the whole previous intersection as the conditioning set.
2. **Repeated the same step** for the remaining intersection.

If we keep doing this, each new event is “peeled off” from the right‑hand side and appears as a conditional probability given everything that has already been peeled off.

### 2.4  Formal induction (optional but short)  

Define  

\[
Q_n = P\Bigl(\bigcap_{i=1}^{n} A_i\Bigr).
\]

**Base case** \(n=2\): by (1) we have  
\(Q_2 = P(A_1)P(A_2\mid A_1)\).  

**Inductive step**: Assume the formula holds for \(n-1\) events:

\[
Q_{\,n-1}=P(A_1)\,P(A_2\mid A_1)\cdots P\bigl(A_{n-1}\mid A_1\cap\cdots\cap A_{n-2}\bigr).
\]

Now apply (1) to the pair  

\[
X = A_n,\qquad Y = \bigcap_{i=1}^{n-1}A_i .
\]

\[
Q_n = P\Bigl(\bigcap_{i=1}^{n-1}A_i\Bigr)\;
       P\bigl(A_n \mid \bigcap_{i=1}^{n-1}A_i\bigr)
     = Q_{\,n-1}\;
       P\bigl(A_n \mid A_1\cap\cdots\cap A_{n-1}\bigr).
\]

Replace \(Q_{\,n-1}\) with the induction hypothesis and we obtain exactly the product with \(n\) factors. Hence the formula is true for all \(n\).

---

## 3.  Intuitive interpretation  

Imagine performing a sequence of **experiments**:

1. First we check whether \(A_{1}\) occurs. Its probability is \(P(A_{1})\).
2. **Given** that \(A_{1}\) has happened, we now ask whether \(A_{2}\) happens. The chance of this is \(P(A_{2}\mid A_{1})\).
3. **Given** that both \(A_{1}\) and \(A_{2}\) have happened, we ask about \(A_{3}\); its chance is \(P(A_{3}\mid A_{1}\cap A_{2})\).
4. Continue until the \(n\)‑th step.

The overall probability that *all* steps succeed (i.e., that the intersection of all events occurs) is the product of the step‑by‑step conditional probabilities. This is exactly the chain rule we derived.

---

## 4.  Final answer  

\[
\boxed{
P\Bigl(\bigcap_{i=1}^{n} A_{i}\Bigr)=
P(A_{1})\;
P(A_{2}\mid A_{1})\;
P(A_{3}\mid A_{1}\cap A_{2})\;
\cdots\;
P\bigl(A_{n}\mid A_{1}\cap\cdots\cap A_{n-1}\bigr)
}
\]

provided each conditioning event has positive probability (otherwise the corresponding conditional probability is undefined).

---

## 5.  Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the order as irrelevant** | The product depends on the *order* of the events; \(P(A_2|A_1)\) is generally not equal to \(P(A_1|A_2)\). | Write the product with a clear order and keep the conditioning set as the *previous* events. |
| **Multiplying unconditional probabilities** | Assuming independence when it isn’t given gives \(P(A_1\cap\cdots\cap A_n)=\prod_i P(A_i)\). | Only replace a conditional term by an unconditional one if you have proved the events are independent. |
| **Omitting a conditioning intersection** | Writing \(P(A_3|A_2)\) instead of \(P(A_3|A_1\cap A_2)\) forgets the information that \(A_1\) already occurred. | Remember the conditioning set always contains *all* earlier events. |
| **Dividing by zero** | Using the definition \(P(B|A)=P(A\cap B)/P(A)\) when \(P(A)=0\) is illegal. | The rule is valid only when each conditioning event (the intersection of earlier events) has positive probability. |
| **Assuming the formula “proves” independence** | The chain rule holds for any events, independent or not. | Independence is an *extra* property: if the events are independent, every conditional factor collapses to an unconditional probability. |

Keeping these points in mind will help you apply the multiplication (chain) rule correctly in any probability problem.

*Original question: [How can I generalize the multiplication rule of probability for more than two events?](https://math.stackexchange.com/questions/5148471/how-can-i-generalize-the-multiplication-rule-of-probability-for-more-than-two-ev) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
