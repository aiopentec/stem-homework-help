---
layout: question
title: Possible formalisations of an Orwellian problem
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Possible formalisations of an Orwellian
  problem'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

# Worked Solution  

## 1.  Restating the problem in plain language  

We have  

* a **population** of agents (people) and a **required set**  \(R\) of propositions that the organisation demands everyone to accept;  

* an **agent commits “thought‑crime”** when, on his own, he believes (or judges) a proposition that contradicts some member of \(R\).  

When an agent \(a\) is caught committing thought‑crime the organisation forces him through the following steps  

| step | informal description | formal requirement |
|------|----------------------|--------------------|
| **P1** | \(a\) must **accept** every proposition in the current required set \(R\). | After P1, \(Bel_a\supseteq R\). |
| **P2** | Later, when the organisation **requires** a new proposition \(p\) (or decides to drop some \(q\in R\)), \(a\) must be able to **replace** an already accepted proposition by an *incompatible* one. | There is a later time \(t\) with \(p\in R_t\) and \(Bel_a(t)\) contains a proposition \(q\) with \(q\vdash\neg p\). |
| **P3** | \(a\) may be **removed** from the population only after he has successfully gone through P1 and P2. | Removal \(\Rightarrow\) “P1 and P2 have been executed”. |
| **P4** | At any moment there must be **enough agents left** so that the above procedure can be applied to any future offender. | The set of “still‑alive’’ agents is never emptied. |

A distinguished **administrator** (call him \(A\)) can  

* detect thought‑crime,  
* decide whether the agent’s dissent is genuine or a pretence, and  
* force the agent through the two forced belief‑changes (P1 and P2).  

The questions are  

1. Which **formal framework** (transition systems, modal/temporal logic, belief‑revision theory, fixed‑point theory, …) is best suited to capture the situation?  
2. What **extra assumptions** are needed to make the description mathematically precise?  
3. Can the **rules generate an infinite regress** of agents that must judge each other’s thought‑crime? If a regress is possible, does it constitute a genuine logical obstruction?  
4. **Is it possible** (in a well‑defined formalisation) to satisfy P1–P4 **simultaneously**?

Below we answer each of these points step‑by‑step.

---

## 2.  Choosing a formal framework  

The problem mixes three ingredients  

* **Epistemic attitude** of many agents (what they *believe*).  
* **Dynamic manipulation** of those attitudes by an external authority (forced belief‑change).  
* **Temporal ordering** (P1 happens first, then later P2, then possibly removal).  

A single formalism that naturally incorporates all three is **Dynamic Epistemic Logic (DEL)** together with an **AGM‑style belief‑revision operator** for the individual agents.  

* **Epistemic part** – a Kripke structure \(\mathcal{M} = (W, \{R_i\}_{i\in \mathsf{Ag}}, V)\) where each \(R_i\) relates worlds that agent \(i\) cannot distinguish. The proposition set \(Prop\) is interpreted by \(V\). The “required set’’ \(R\subseteq Prop\) is a *global* datum (the Party line).  

* **Dynamic part** – DEL actions (also called *product updates*) model the forced operations:  

  * **Accept\(_a\)** : an action model that forces every world compatible with the current state to satisfy all \(p\in R\). In epistemic terms it **publicly announces** the conjunction \(\bigwedge_{p\in R}p\) *to* agent \(a\).  

  * **Replace\(_a(p,q)\)** : an action that publicly announces a *revision* of \(a\)’s belief set, replacing a formerly accepted proposition \(p\) by an incompatible one \(q\) (with \(p\vdash\neg q\)). This is exactly the AGM *revision* operator \(*\) with post‑condition \(Bel_a^{new}= (Bel_a\setminus\{p\})\cup\{q\}\).  

* **Temporal part** – we index the global state by a discrete time line \(\mathbb{N}\): the whole system evolves as a sequence \(\mathcal{M}_0,\mathcal{M}_1,\dots\). The administrator’s detection and the forced actions are *deterministic* functions of the current state.  

Thus a **state** of the whole system is a tuple  

\[
\Sigma_t = \bigl(\mathcal{M}_t,\; \text{Alive}_t\subseteq \mathsf{Ag}\bigr)
\]

where \(\text{Alive}_t\) are the agents that have not yet been removed.  
The **transition function** \(\tau\) maps a state and a chosen “offender’’ \(a\) to the next state obtained by  

1. applying **Accept\(_a\)** (P1),  
2. applying **Replace\(_a\)** for some required new proposition (P2),  
3. optionally removing \(a\) (P3).  

P4 is expressed as the invariant  

\[
\forall t\; \bigl|\text{Alive}_t\bigr| \ge 1 .
\]

---

### Why other frameworks are insufficient (or can be reduced to DEL)

| Candidate | Reason it alone does not capture everything |
|-----------|--------------------------------------------|
| Pure **transition system** (states + arrows) | Can encode the dynamics, but gives no way to talk about *beliefs* of agents inside a state. |
| Plain **temporal logic** (LTL/CTL) | Allows ordering of events but again lacks epistemic operators (what agents consider true). |
| **Modal epistemic logic** without dynamics | Describes static beliefs but cannot express forced belief‑change. |
| **Fixed‑point theory** (e.g., Kripke–Fixpoint) | Useful for defining the set of offenders as the least fixed point of a detection operator, but still needs a base language for beliefs. |
| **AGM belief revision** alone | Gives the local operation “replace a belief”, but does not describe *who* performs the operation, when, or the global invariant P4. |

Therefore the **most natural single umbrella** is *Dynamic Epistemic Logic with AGM‑style revision*, which already contains a Kripke (modal) semantics, a temporal product‑update mechanism, and a well‑studied belief‑revision operator.

---

## 3.  Making the description mathematically precise  

We add the following **assumptions** (all of them are standard in DEL/AGM literature):

1. **Finite proposition set** – \(Prop\) is finite (or at least countable) so that the conjunction \(\bigwedge_{p\in R}\) is a well‑formed formula.  

2. **Non‑omniscient agents** – each agent’s belief set \(Bel_a(t)\) is *deductively closed* under a fixed logical consequence relation \(\vdash\) **only for the propositions they have already accepted**. In particular, after P1 the agent may still be *ignorant* of the incompatibility of the later‑required proposition; this permits P2 without immediate inconsistency.  

3. **Paraconsistent allowance** – we adopt a **paraconsistent** background logic (e.g., Priest’s LP) so that a belief set can temporarily contain both \(p\) and \(\neg p\) without exploding to triviality. This is crucial because P2 forces the agent to *replace* a required proposition by an incompatible one; in a classical setting the belief set would become inconsistent and the revision operator would be undefined.  

4. **Deterministic detection** – the administrator \(A\) has a primitive *detection* predicate \(Detect(a,t)\) that returns true iff \(a\) has, at time \(t\), a belief contradicting \(R\). We **axiomatise** this predicate as:  

   \[
   Detect(a,t)\;\Longleftrightarrow\; \exists p\in R\;.\; Bel_a(t)\vdash \neg p .
   \]

   No other agent is needed for the detection; hence no regress arises.  

5. **Sufficient population** – we assume a **lower bound** \(k\ge 1\) on the number of agents that must stay alive at all times. Formally  

   \[
   \forall t\; |\text{Alive}_t|\ge k .
   \]

   The value of \(k\) can be taken as 1 (the system can survive with a single “reformed’’ agent) or larger if the story demands it.

With these five assumptions the informal rules P1–P4 become **formal invariants** on the transition system \((\Sigma_t)_{t\in\mathbb N}\):

* **P1 (Accept)**  
  \[
  \forall t\;\bigl(Detect(a,t)\rightarrow Bel_a(t+1)\supseteq R\bigr)
  \]

* **P2 (Replace)** – there exists a later time \(t'>t\) such that a *new* required proposition \(p\in R_{t'}\setminus R_t\) is believed while some earlier required \(q\in R_t\) is *rejected*:

  \[
  \exists t'>t\; \bigl(p\in R_{t'}\setminus R_t\wedge Bel_a(t')\vdash p\wedge Bel_a(t')\vdash\neg q\bigr)
  \]

* **P3 (Removal)**  

  \[
  Remove(a,t) \;\Longleftrightarrow\; \bigl(Detect(a,t')\wedge P1\wedge P2\ \text{already executed for }a\bigr)
  \]

* **P4 (Survival)**  

  \[
  \forall t\; |\text{Alive}_t|\ge k .
  \]

All of these are *first‑order* statements over the underlying DEL structure, so the whole system is a **first‑order definable transition system**.

---

## 4.  Does the system generate an infinite regress of agents?  

### 4.1  Where a regress could appear  

The only place where an *extra* agent would be needed to judge thought‑crime is the clause “*determine whether agent \(a\) has committed thought‑crime*”. If we tried to model this judgment as **another agent’s belief** (“\(b\) believes that \(a\) has contradicted the Party line”), we would indeed obtain a chain:

\[
\text{Detect}(a) \text{ depends on } Bel_b,\; 
\text{Detect}(b) \text{ depends on } Bel_c,\; \dots
\]

If the detection predicate were defined *solely* in terms of other agents’ beliefs, we could get an **infinite hierarchy** with no base case.

### 4.2  How to block the regress  

In our formalisation we **axiomatised** the detection predicate as a primitive, **admin‑controlled** operation (Assumption 4). The administrator is a distinguished agent whose epistemic state is *outside* the system; we do **not** require any other agent to verify the detection.

*Original question: [Possible formalisations of an Orwellian problem](https://math.stackexchange.com/questions/5149507/possible-formalisations-of-an-orwellian-problem) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
