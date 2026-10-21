---
layout: question
title: Transitivity in formal proofs and informal proofs
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Transitivity in formal proofs and
  informal proofs'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The student is wondering why, when we write a **formal** proof (a list of formulas each justified by an axiom or a rule of inference), we never see a line that says “*use transitivity*”.  
In an **informal** proof we often argue:

\[
P_{1}\!\implies\!P_{2},\;P_{2}\!\implies\!P_{3},\dots ,P_{k}\!\implies\!P_{n}\;\;\Longrightarrow\;\;P_{1}\!\implies\!P_{n},
\]

and we point to the *transitivity of implication* as the reason the chain collapses.  

The question is:  

*Is transitivity used in a formal proof at all?*  
*If it is, why do we never mention it explicitly?*  

We have to explain the relationship between the **meta‑theoretic** fact “⇒ is transitive” and the **object‑level** inference rules that make up a formal proof.

---

## 2.  Step‑by‑step answer  

### 2.1  Two different levels of “⇒”

| Level | Symbol | Meaning |
|------|--------|---------|
| **Object level** | \(A\to B\) (or \(A\Rightarrow B\)) | A *formula* of the language, an implication that can appear inside a proof. |
| **Meta level** | \(\Gamma\;\vdash\; \varphi\) | “There is a formal proof of \(\varphi\) from the set of premisses \(\Gamma\).” This is the **syntactic consequence** relation. |

*Transitivity of implication* that we use informally is a **meta‑statement** about the consequence relation:

\[
\text{If } \Gamma\vdash\psi \text{ and } \Gamma\cup\{\psi\}\vdash\chi,\text{ then }\Gamma\vdash\chi .
\tag{*}
\]

In many proof systems this meta‑property is called the **Cut rule** or **admissibility of cut**. It is *not* a primitive inference rule; it is a theorem about the proof system that can be *proved* inside the meta‑theory.

### 2.2  How transitivity is *built into* the usual inference rules  

Take a very common Hilbert‑style system for classical propositional logic. Its only rule of inference is **modus ponens**:

\[
\frac{A \qquad A\to B}{B}\;(\text{MP})
\]

and it has a few axiom schemata, e.g.

1. \(A\to (B\to A)\)  
2. \((A\to (B\to C))\to ((A\to B)\to (A\to C))\)   (the *distribution* axiom)  
3. \((\lnot A\to\lnot B)\to (B\to A)\)

Notice that axiom (2) **is exactly the formal statement of transitivity of implication**:

\[
(A\to B)\to\bigl((B\to C)\to (A\to C)\bigr).
\]

Thus, in a Hilbert proof the “transitivity step’’ is *already* present as a theorem that can be used with modus ponens.  

*Example.* Suppose we have already derived \(P_{1}\to P_{2}\) and \(P_{2}\to P_{n}\).  
1. \( (P_{1}\to P_{2})\to\bigl((P_{2}\to P_{n})\to (P_{1}\to P_{n})\bigr)\)   (axiom 2)  
2. \(P_{1}\to P_{2}\)                                       (derived)  
3. \((P_{2}\to P_{n})\to (P_{1}\to P_{n})\)                    (MP 1,2)  
4. \(P_{2}\to P_{n}\)                                      (derived)  
5. \(P_{1}\to P_{n}\)                                      (MP 3,4)

The five‑line derivation is the *formal* counterpart of the informal “\(P_{1}\to P_{2}\) and \(P_{2}\to P_{n}\) give \(P_{1}\to P_{n}\) by transitivity”. The rule *modus ponens* together with the axiom that encodes transitivity does all the work; we never have to write a separate “transitivity” step.

### 2.3  Natural‑deduction view  

In a natural‑deduction system the rule that corresponds to modus ponens is called **→‑elimination**:

\[
\frac{\displaystyle A \qquad \displaystyle A\to B}{B}\;(\to\!E)
\]

A chain of implications is handled by applying →‑elimination repeatedly:

\[
\begin{array}{l}
1.\; P_{1} \\
2.\; P_{1}\to P_{2} \\
3.\; P_{2} \quad (\to E\; 1,2)\\[2mm]
4.\; P_{2}\to P_{3}\\
5.\; P_{3} \quad (\to E\; 3,4)\\
\vdots\\
k+1.\; P_{n}\quad (\to E\; \dots )
\end{array}
\]

Again, there is **no separate rule called “transitivity’’**; the repeated use of →‑elimination automatically yields the same effect. The meta‑theorem “if we have a derivation of \(P_{1}\to P_{2}\) and a derivation of \(P_{2}\to P_{3}\) then we can derive \(P_{1}\to P_{3}\)” is provable inside the system (it is a *derived rule*).

### 2.4  Sequent calculus and the explicit **cut** rule  

In the sequent calculus the transitivity of entailment appears **as an explicit rule** called **cut**:

\[
\frac{\Gamma\;\vdash\;A \qquad \Delta, A\;\vdash\;C}{\Gamma,\Delta\;\vdash\;C}\;(cut)
\]

Most textbook presentations show that *cut is admissible*: any proof that uses cut can be transformed into a cut‑free proof. When we work in a cut‑free system we never write a cut step, yet the meta‑theorem “if \(\Gamma\vdash A\) and \(A\vdash C\) then \(\Gamma\vdash C\)” remains true. Thus the sequent calculus makes the transitivity rule visible, but most natural‑deduction or Hilbert presentations hide it by building it into the primitive rules.

### 2.5  Why textbooks do not mention “transitivity” in formal proofs  

1. **It is not a primitive rule.** Formal systems are defined by a small set of primitive inference rules (modus ponens, →‑elimination, etc.). All other reasoning patterns, including transitivity, are *derived* from them.

2. **The meta‑property is proved once and for all.** After we have shown (in a meta‑theoretic proof) that the consequence relation is transitive, we can use that fact whenever we like, without having to write it down each time.

3. **Economy of notation.** In a formal proof we list the *individual* steps that are justified by the primitive rules. Adding a line that simply says “by transitivity of ⇒” would be a *meta‑step*; it would not be a correct object‑level inference in the chosen system.

Hence, in a *formal* proof transitivity is **present**, but it is either:
* encoded in an axiom schema (Hilbert),  
* hidden inside a primitive rule (natural deduction), or  
* an admissible derived rule (sequent calculus).

---

## 3.  Final answer  

*Transitivity of logical consequence is a meta‑theoretic property, not a primitive inference rule. In the usual formal systems the effect of transitivity is already captured by the basic rules (e.g., modus ponens together with an axiom that proves \((A\to B)\to((B\to C)\to(A\to C))\)). Therefore a formal proof never needs a separate “transitivity” line; the same result is obtained by applying the primitive rules repeatedly. In sequent calculus an explicit **cut** rule expresses transitivity, but even there the cut rule is provably admissible, so many presentations work cut‑free and never mention it. Consequently, formal proofs “use” transitivity implicitly, and it is omitted from the proof text because it is either built into the rules or already proved as a theorem about the system.*

---

## 4.  Common mistakes when dealing with this topic  

| Mistake | Why it is wrong | Correct approach |
|---------|----------------|------------------|
| **Confusing object‑level implication \(A\to B\) with meta‑level entailment \(\Gamma\vdash B\).** | Transitivity of \( \to \) is a theorem *inside* the language; transitivity of \( \vdash \) is a property *about* the proof system. | Keep the two levels separate; prove the meta‑property once, then use primitive rules for object‑level steps. |
| **Thinking a formal proof must contain a line “by transitivity”.** | Formal systems are defined by a fixed set of primitive inference rules; transitivity is not among them. | Derive the needed result by repeated applications of the primitive rule(s) (e.g., modus ponens). |
| **Assuming that because a proof uses many implication‑chains, the system must have a rule named “transitivity”.** | The chain is simply a series of →‑elimination steps; no special rule is required. | Write the chain as a sequence of →‑elimination (or MP) applications. |
| **Neglecting the deduction theorem.** | The informal “\(P_{1}\to P_{n}\)” often relies on the deduction theorem to turn a derivation with an extra assumption into an implication. | Show how the deduction theorem lets us move from a derivation of \(P_{n}\) from \(P_{1}\) to a derivation of \(P_{1}\to P_{n}\). |
| **Believing that “cut” is always part of every formal proof.** | Cut is optional; many proof systems (natural deduction, cut‑free sequent calculus) do not use it.

*Original question: [Transitivity in formal proofs and informal proofs](https://math.stackexchange.com/questions/5152463/transitivity-in-formal-proofs-and-informal-proofs) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
