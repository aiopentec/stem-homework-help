---
layout: question
title: Why is topology via opens still being taught?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Why is topology via opens still being
  taught?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1. Restatement of the Question (in plain language)

> **What is being asked?**  
> The student wonders why introductory courses in general topology still begin by defining a *topology* as a collection of **open sets**, even though many mathematicians find the language of **nets** or **filters** more convenient for proving theorems. In other words: *Why do textbooks and lectures continue to teach topology “through open sets” instead of “through nets/filters”?*  

We need to give a thorough, step‑by‑step explanation that addresses historical, pedagogical, and mathematical reasons for this choice.

---

## 2. Detailed Answer – Step‑by‑Step Reasoning  

Below each numbered point explains a separate “step” in the logical chain that justifies why the **open‑set** approach remains the standard entry point.

| Step | Reason / Argument | Explanation |
|------|-------------------|-------------|
| **1** | **Historical Origin** | The notion of *open* subsets was already present in the study of Euclidean space (open intervals, balls, etc.). When Hausdorff, Kuratowski, and others axiomatized “spaces” in the early 20th century, they chose the **open‑set** axioms because they directly captured the intuitive idea of “no boundary points.” |
| **2** | **Minimal Prerequisites** | Defining a topology via open sets only requires the elementary language of **sets** and **unions/intersections**. Nets and filters need the notion of a **directed set** (or a filter base) and, for filters, the axiom of **choice** to guarantee maximal filters. Those concepts are usually *not* part of the background of a first‑year analysis or algebra student. |
| **3** | **Concrete Visualisation** | In metric spaces the open balls are tangible geometric objects. Students can *draw* them, see how they overlap, and develop intuition about continuity, convergence, and connectedness. Open sets give a picture that is immediately accessible; nets/filters are more abstract. |
| **4** | **Foundational Simplicity** | The three axioms for a topology  

   1. ∅ and X are open,  
   2. arbitrary unions of opens are open,  
   3. finite intersections of opens are open  

   are short, easy to memorize, and can be checked directly in examples.  By contrast, the definition of a net (a function from a directed set) or a filter (a non‑empty family closed under supersets and finite intersections) is longer and requires more notation. |
| **5** | **Direct Link to Classical Concepts** | Many classical theorems (e.g., *Urysohn’s Lemma*, *Tietze Extension*, *Baire Category*, *Heine–Borel*) are most naturally expressed in terms of open sets (or closed sets, which are complements). Working with opens keeps the statements of these results close to their historical formulations. |
| **6** | **Equivalence to Nets/Filters** | Once the open‑set definition is in place, one can *prove* that the notions of convergence via nets or filters are **equivalent** to the open‑set notion of continuity, compactness, etc. Thus the open‑set framework is **foundational**; nets/filters become *derived tools* that can be introduced later as convenient machinery. |
| **7** | **Pedagogical Sequence** | A typical curriculum proceeds:  

   1. Define open sets → define a topology.  
   2. Use opens to define continuity, interior, closure, boundary.  
   3. Prove basic theorems (e.g., continuity ↔ pre‑image of opens is open).  
   4. Introduce bases, subbases, product topologies.  

   Only after students are comfortable with these concrete ideas do we bring in nets/filters to streamline proofs of, say, compactness (every net has a convergent subnet) or to discuss convergence in spaces without countable bases. |
| **8** | **Avoiding Set‑Theoretic Pitfalls Early On** | Nets and filters often require the **Axiom of Choice** (or at least a weak form) to guarantee the existence of maximal filters or cofinal maps. Teaching topology first with opens lets instructors postpone any discussion of choice‑related subtleties to a later, more advanced course. |
| **9** | **Compatibility with Other Areas** | In algebraic topology, differential geometry, and functional analysis, the open‑set language meshes well with **local charts**, **sheaves**, **manifolds**, and **Banach spaces**. Many constructions (e.g., atlases) are phrased in terms of open neighborhoods. |
| **10** | **Historical Pedagogical Tradition** | Textbooks and curricula have long been built around the open‑set approach; changing the foundation would require rewriting a huge amount of material. The inertia of tradition therefore reinforces the continued use of opens in introductory courses. |
| **11** | **Net/Filter Theory is Not “Simpler” for Everyone** | While nets/filters can make certain proofs shorter, they can also be *more confusing* for beginners because they introduce two new families of objects (directed sets and filter bases). What is “simpler” depends on the student’s background; many find the open‑set viewpoint the least abstract. |
| **12** | **Summarising the Rationale** | Putting the previous points together:  

   *Open sets give a direct, visual, historically grounded, and logically minimal entry point to topology. Nets and filters are powerful *auxiliary* tools that are introduced **after** the open‑set foundation is secure.* |

---

## 3. Final Answer (concise statement)

> **Answer:**  
> General‑topology courses start with open sets because they provide the simplest, most intuitive, and historically rooted definition of a topology. The open‑set axioms require only elementary set theory, give a clear geometric picture, and connect directly to classical results. Nets and filters, although very useful for many proofs, are more abstract, need extra concepts (directed sets, filters, often the axiom of choice), and are therefore taught later as convenient *derived* language rather than as the primary definition.

---

## 4. Common Mistakes When Addressing This Question  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing “easier to use in proofs” with “easier to learn.”** | Nets/filters may shorten certain arguments, but they are conceptually more demanding for beginners. | Emphasise the difference between *technical convenience* and *pedagogical accessibility*. |
| **Assuming the open‑set definition is obsolete.** | It is still the *foundational* definition; all other approaches are proven equivalent to it. | State clearly that nets/filters are **derived** notions, not replacements. |
| **Neglecting the role of the axiom of choice.** | Nets/filters often rely on choice to guarantee existence of maximal filters or cofinal directed sets, which is a subtle set‑theoretic issue not needed for opens. | Mention the choice‑dependence when discussing why nets/filters are introduced later. |
| **Claiming that every theorem is shorter with nets/filters.** | Some results (e.g., Urysohn’s Lemma, construction of bases) are naturally expressed with opens. | Give examples where the open‑set language is genuinely more natural. |
| **Over‑generalising from a single textbook.** | Different curricula may vary; some courses do start with nets/filters, but they are the exception. | Acknowledge the existence of alternative curricula but explain why the majority still prefer opens. |

---

*Original question: [Why is topology via opens still being taught?](https://math.stackexchange.com/questions/5151307/why-is-topology-via-opens-still-being-taught) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
