---
layout: question
title: Are There Weaker Axioms to Extend Intuitionistic Propositional Logic, to Jankov
  Logic, to G&#246;del-Dummett Logic, to Smetanich Logic Stepwise?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Are There Weaker Axioms to Extend
  Intuitionistic Propositional Logic, to Jankov Logic, to G&#246;del-Dummett Logic,
  to S'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

### 1. Restatement of the Problem in Plain Language

We are studying **intermediate logics**—propositional logics that sit strictly between Intuitionistic Propositional Logic (IPL) and Classical Propositional Logic (CPL). Specifically, we are looking at a well-known chain of logics ordered by deductive strength:

$$\text{IPL} \subsetneq \text{JPL} \subsetneq \text{GPL} \subsetneq \text{SML} \subsetneq \text{CPL}$$

where:
*   **IPL** = Intuitionistic Logic
*   **JPL** = Jankov Logic (KC) = $\text{IPL} + (\neg A \lor \neg\neg A)$
*   **GPL** = Gödel-Dummett Logic (LC) = $\text{IPL} + ((A \to B) \lor (B \to A))$
*   **SML** = Smetanich Logic (Sm) = $\text{IPL} + ((\neg A \lor B) \lor (B \to A))$
*   **CPL** = Classical Logic = $\text{IPL} + (A \lor \neg A)$

Usually, each of these logics is defined by adding a single strong axiom directly to **IPL**. The student is asking a fine-grained structural question: **Can we find "weaker" intermediate axioms or rules to step incrementally between adjacent logics in the chain?** 

Specifically:
1. Is there an axiom or rule $R_1$ such that $\text{IPL} + R_1 \neq \text{JPL}$, but $\text{JPL} + R_1 = \text{GPL}$?
2. Is there an axiom or rule $R_2$ such that $\text{GPL} + R_2 \neq \text{SML}$, but $\text{JPL} (\text{or GPL}) + R_2 = \text{SML}$? (And similarly for the step from SML to CPL).

---

### 2. Step-by-Step Analysis

To answer whether we can decompose these extensions into smaller, intermediate steps, we must look at the algebraic semantics of intermediate logics (specifically, Heyting algebras and their corresponding subvarieties) and the lattice of intermediate logics.

#### Step A: Understanding the Lattice Structure of Intermediate Logics
The set of all intermediate logics forms a gigantic, uncountably infinite distributive lattice under inclusion, ordered by $\subseteq$. 
*   Jankov logic ($\text{JPL}$ or $\text{KC}$) corresponds to the variety of Heyting algebras satisfying $\neg x \lor \neg\neg x = 1$ (Weak Law of Excluded Middle).
*   Gödel-Dummett logic ($\text{GPL}$ or $\text{LC}$) corresponds to chains (Heyting algebras where the lattice of elements is linearly ordered).
*   Smetanich logic ($\text{SML}$) has a specific algebraic characterization.
*   $\text{CPL}$ corresponds to Boolean algebras.

Because the lattice of intermediate logics is dense and massive, **yes**, there are infinitely many intermediate logics between $\text{IPL}$ and $\text{JPL}$, between $\text{JPL}$ and $\text{GPL}$, between $\text{GPL}$ and $\text{SML}$, and between $\text{SML}$ and $\text{CPL}$. 

#### Step B: Addressing the Student's Attempt at Stepwise Axiomatization
The student tried to bridge $\text{JPL}$ to $\text{GPL}$ by finding a rule that, when added to $\text{JPL}$, yields $\text{GPL}$ without jumping straight to classical logic. 

The student evaluated the formula $\neg\neg A \to (B \to A)$ and correctly noticed that substituting $\neg\neg A$ for $B$ yields:
$$\neg\neg A \to (\neg\neg A \to A) \vdash \neg\neg A \to A$$
In intuitionistic logic, $\neg\neg A \to A$ is **Glivenko's theorem**-adjacent; specifically, adding $\neg\neg A \to A$ to IPL immediately collapses the logic to **Classical Logic ($\text{CPL}$)**. Thus, that specific formula overshoots $\text{GPL}$ and lands directly at $\text{CPL}$.

#### Step C: Constructing the Exact Intermediate Steps (Can we step $X \to Y$?)
To show that we can step from $\text{JPL}$ to $\text{GPL}$ via weaker intermediate logics, we can look at finite-frame semantics (Kripke semantics). 
*   $\text{GPL}$ is characterized by the class of Kripke frames that are chains of clusters (linear orders of sets of worlds).
*   $\text{JPL}$ is characterized by frames where every point has a dense set of endpoints (or where $\neg x \lor \neg\neg x$ holds).

We can construct weaker axioms by considering Dummett's schema truncated or indexed by the depth of Kripke frames, or by using Hosoi's sequences of formulas. 
For instance, Hosoi defined a sequence of formulas $H_n$ such that:
*   $\text{IPL} \subset \text{IPL} + H_1 \subset \text{IPL} + H_2 \subset \dots \subset \text{GPL}$
Each $H_n$ acts as a "weaker" stepping stone toward Gödel-Dummett logic. Specifically, the axiom schemas:
$$LC_n = (A_0 \to A_1) \lor (A_1 \to A_2) \lor \dots \lor (A_n \to A_0)$$
generate an infinite ascending chain of logics between $\text{IPL}$ and $\text{GPL}$. Adding $LC_1$ is $(A \to B) \lor (B \to A)$, which gives $\text{GPL}$ directly, but sub-logics can be formed using broader disjunctions of implications, or structural restrictions on frames.

Similarly, between $\text{SML}$ and $\text{CPL}$, and $\text{JPL}$ and $\text{GPL}$, the intermediate logics form dense or highly branched sub-lattices. Therefore, weaker axioms (such as fragments of Jankov-De Jongh formulas) natively exist to bridge these gaps incrementally.

---

### 3. Final Answer

**Yes, there are weaker axioms and intermediate logics** that allow you to step incrementally from $\text{IPL}$ to $\text{JPL}$, from $\text{JPL}$ to $\text{GPL}$, from $\text{GPL}$ to $\text{SML}$, and from $\text{SML}$ to $\text{CPL}$. 

1. **Existence of Intermediate Logics:** The lattice of intermediate logics between any two distinct logics in the chain ($\text{L}_1 \subsetneq \text{L}_2$) is infinite. You do not have to jump from $\text{JPL}$ straight to $\text{GPL}$ in a single monolithic bound; there are infinitely many intermediate logics strictly between them.
2. **Axiomatizing the Steps:** Systems like Hosoi's formulas ($H_n$) and generalized Dummett schemas ($LC_n$) provide explicit, weaker axiomatic steps that gradually restrict Kripke frames from intuitionistic frames down to linear frames ($\text{GPL}$) and finally to trivial/Boolean frames ($\text{CPL}$).
3. **The Student's Caveat:** The student's intuition that certain candidate rules collapse the system too far (e.g., yielding $\text{CPL}$ via $\neg\neg A \to A$) is mathematically correct. Care must be taken not to validate Peirce's Law $((A \to B) \to A) \to A$ or Double Negation Elimination prematurely, which is avoided by using indexed chain axioms ($LC_n$) rather than unrestricted classical implicational mingling.

---

### 4. Common Mistakes for This Problem Type

*   **Assuming Finiteness of Options:** Assuming that because only a few famous intermediate logics ($\text{JPL}, \text{GPL}, \text{SML}$) are given standard names, there are no intermediate steps between them. In reality, the lattice of intermediate logics is uncountably infinite.
*   **Confusing Structural Rules with Admissible Rules:** Confusing structural rules (adding a Hilbert-style axiom schema to the logic) with structural rules of inference (like structural admissibility in Gentzen sequent calculi). Adding an axiom changes the set of theorems, whereas modifying structural rules changes the proof-theoretic environment.
*   **Accidental Collapse to Classical Logic (CPL):** Adding formulas containing nested implications or double negations that implicitly validate Peirce's law, Glivenko inversions, or the full Law of Excluded Middle ($A \lor \neg A$), thereby overshooting intermediate logics like $\text{JPL}$ or $\text{GPL}$ and landing straight on $\text{CPL}$.

*Original question: [Are There Weaker Axioms to Extend Intuitionistic Propositional Logic, to Jankov Logic, to G&#246;del-Dummett Logic, to Smetanich Logic Stepwise?](https://math.stackexchange.com/questions/5153615/are-there-weaker-axioms-to-extend-intuitionistic-propositional-logic-to-jankov) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
