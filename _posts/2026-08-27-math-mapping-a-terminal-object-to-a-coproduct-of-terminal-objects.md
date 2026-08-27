---
layout: question
title: mapping a terminal object to a coproduct of terminal objects
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: mapping a terminal object to a coproduct
  of terminal objects'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We work in a category \(\mathcal C\) that  

* has a terminal object \(1\);
* has finite coproducts \(\;\coprod\).

For a fixed integer \(n\ge 1\) we form the coproduct of \(n\) copies of the terminal object  

\[
\underbrace{1\;\coprod\;1\;\coprod\;\cdots\;\coprod\;1}_{n\text{ times}}\;=\;\coprod^{\,n}1 .
\]

Every coproduct comes equipped with **injection maps**

\[
\iota_i : 1 \longrightarrow \coprod^{\,n}1 ,\qquad i=1,\dots ,n .
\]

The question is:  

> **When does the set of all arrows \(1\to\coprod^{\,n}1\) consist *exactly* of those \(n\) injections?**  

In other words, for which categories is the canonical function  

\[
\Phi_n \;:\; \{1,\dots ,n\}\;\longrightarrow\;\operatorname{Hom}_{\mathcal C}\!\bigl(1,\coprod^{\,n}1\bigr),\qquad
i\mapsto \iota_i\circ\!(!_1)
\]

a bijection for every \(n\ge 1\)?

The author calls this the **“one‑to‑\(n\) property”.**  
We have to relate it to known categorical notions and give a clean characterisation.



--------------------------------------------------------------------

## 2.  A systematic analysis  

### 2.1  The canonical map \(\Phi_n\)

Because \(1\) is terminal, there is a unique map \(!_{1}:1\to 1\).  
Hence each injection \(\iota_i\) gives a *global element* (arrow from the terminal object)  

\[
\iota_i\circ !_1 : 1\longrightarrow\coprod^{\,n}1 .
\]

Collecting them gives a function  

\[
\Phi_n : n \;=\;\coprod_{i=1}^{n}\operatorname{Hom}(1,1)
      \;\longrightarrow\;\operatorname{Hom}\bigl(1,\coprod^{\,n}1\bigr).
\tag{1}
\]

The domain has exactly \(n\) elements because \(\operatorname{Hom}(1,1)=\{!\_{1}\}\).

*Injectivity* of \(\Phi_n\) is automatic in any category: the injections \(\iota_i\) are distinct as morphisms of the coproduct, so the corresponding global elements are distinct.  
The *hard part* is **surjectivity**: we must show that **every** global element of \(\coprod^{\,n}1\) comes from one of the injections.

Thus the “one‑to‑\(n\) property’’ is exactly the statement

\[
\boxed{\text{For every }n,\; \Phi_n \text{ is a bijection}.}
\tag{2}
\]

### 2.2  Interpreting \(\Phi_n\) as preservation of coproducts  

Define the **global‑sections functor**

\[
\Gamma\;=\;\operatorname{Hom}_{\mathcal C}(1,-)\;:\;\mathcal C\longrightarrow \mathbf{Set}.
\]

For any two objects \(A,B\) we have a natural map  

\[
\Gamma A\;\amalg\;\Gamma B \;\longrightarrow\;\Gamma(A\amalg B)
\]

obtained by composing with the coproduct injections.  
When the source objects are both the terminal object we obtain precisely \(\Phi_n\) :

\[
\Gamma(1)\amalg\cdots\amalg\Gamma(1) \;\cong\; n
   \;\xrightarrow{\;\Phi_n\;}\; \Gamma\!\bigl(\coprod^{\,n}1\bigr).
\]

Consequently,

\[
\text{(2) holds for all }n \iff \Gamma \text{ preserves the coproduct }\coprod^{\,n}1.
\]

Because \(\Gamma\) already preserves the empty coproduct (it sends the initial object to the empty set), condition (2) is **equivalent** to

\[
\boxed{\Gamma\text{ preserves all finite coproducts}.}
\tag{3}
\]

Thus the “one‑to‑\(n\) property’’ is nothing other than the statement that **global sections turn a coproduct of copies of the terminal object into the ordinary set‑theoretic coproduct of the corresponding copies of a one‑point set.**



### 2.3  Relation to familiar categorical notions  

1. **Well‑pointedness (in topos theory).**  
   For an elementary topos \(\mathcal E\) the following are equivalent  

   * (i) \(\mathcal E\) is *well‑pointed*, i.e. the terminal object \(1\) is a **separator** (a generator) and the global‑sections functor \(\Gamma\) is **faithful**;  

   * (ii) \(\Gamma\) preserves finite coproducts.  

   In a well‑pointed topos the object \(\coprod^{\,n}1\) is the *discrete* object with exactly \(n\) points, so the one‑to‑\(n\) property holds.

2. **Generator + preservation of coproducts.**  
   In an arbitrary category (not necessarily a topos) condition (3) can be split:

   * \(1\) being a **generator** (or **separator**) guarantees that the map \(\Phi_n\) is **injective** (different injections give different arrows).  

   * Preservation of coproducts guarantees **surjectivity**.

   Hence the one‑to‑\(n\) property holds exactly when **\(1\) is a generator and \(\Gamma\) preserves finite coproducts**.

3. **Extensive categories.**  
   In an extensive category coproduct injections are *disjoint* and *universal*, but this does **not** force (3).  The total order with a top element is extensive (its coproducts are joins), yet \(\Gamma\) does **not** preserve them, and the property fails – exactly the example mentioned in the question.

4. **Free coproduct completion.**  
   The free coproduct completion \(\operatorname{Fam}(\mathcal C)\) of any category \(\mathcal C\) has the property, because objects are families \((X_i)_{i\in I}\) and a map \(1\to\coprod^{\,n}1\) is just the choice of an index \(i\); therefore \(\Gamma\) sends \(\coprod^{\,n}1\) to the set \(\{1,\dots ,n\}\).  This fits the general characterisation: \(\Gamma\) preserves coproducts in \(\operatorname{

*Original question: [mapping a terminal object to a coproduct of terminal objects](https://math.stackexchange.com/questions/5148037/mapping-a-terminal-object-to-a-coproduct-of-terminal-objects) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
