---
layout: question
title: Explicit graph $H\subset\mathbb{R}^2$ with $\chi(H)\geq6$?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Explicit graph $H\subset\mathbb{R}^2$
  with $\chi(H)\geq6$?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The **Hadwiger–Nelson problem** asks how many colours are needed to colour every point of the Euclidean plane so that no two points at distance exactly 1 receive the same colour.  
The answer is the **chromatic number of the plane**, written \(\chi(\mathbb{R}^2)\).

A *finite* unit‑distance graph \(H\subset\mathbb{R}^2\) is a set of points together with the edges that join every pair of points whose Euclidean distance is exactly 1.  

If we can exhibit a concrete set of coordinates for such a graph whose chromatic number is **6**, then we would have a *concrete counter‑example* proving \(\chi(\mathbb{R}^2)\ge 6\).

The student’s question therefore is:

> **“Is there an explicit list of coordinates for a finite unit‑distance graph in the plane that needs at least six colours? If a recent proof that \(\chi(\mathbb{R}^2)\ge 6\) is correct, does it actually give us such a graph, perhaps one we could feed to a SAT‑solver to verify that four (or five) colours are impossible?”**

---

## 2.  Detailed answer – why no explicit 6‑chromatic unit‑distance graph is known yet

### 2.1.  Current state of knowledge

| Result | Year | Reference | What it tells us |
|--------|------|-----------|-------------------|
| \(\chi(\mathbb{R}^2)\ge 4\) | 1950s | de Bruijn & Erdős | Any proper 3‑colouring would give a 3‑colouring of some finite unit‑distance graph. |
| \(\chi(\mathbb{R}^2)\ge 5\) | 2018 | Aubrey de Grey | Constructed a 1581‑vertex unit‑distance graph that cannot be coloured with 4 colours. |
| \(\chi(\mathbb{R}^2)\le 7\) | 1950s | Isbell, later refinements | A 7‑colouring of the whole plane is known. |
| **\(\chi(\mathbb{R}^2)\ge 6\)** | *none (as of 2026)* | — | No published, peer‑reviewed proof. |

Thus **the best proven lower bound is 5**, and **the best proven upper bound is 7**.  A claim that \(\chi(\mathbb{R}^2)\ge 6\) would be a major breakthrough, but *no such claim has been verified* by the mathematical community up to the present date.

### 2.2.  What a “proof that \(\chi(\mathbb{R}^2)\ge 6\)” would have to contain

To prove \(\chi(\mathbb{R}^2)\ge 6\) one must **exhibit a finite unit‑distance graph** \(H\) with \(\chi(H)=6\).  By the de Bruijn–Erdős theorem, any lower‑bound proof for the whole plane necessarily yields a finite example.  Consequently the proof would have to supply:

1. **A finite set of points** \(\{p_1,\dots ,p_N\}\subset\mathbb{R}^2\).  
2. **The list of unit edges** \(\{(p_i,p_j):\|p_i-p_j\|=1\}\).  
3. **A proof that no 5‑colouring exists** (e.g. by reduction to SAT, by a combinatorial argument, or by exhaustive computer search).

If the proof were purely *probabilistic* (showing that a randomly chosen large enough set of points *almost surely* contains a 6‑chromatic subgraph), it would **not** automatically give concrete coordinates.  Probabilistic existence proofs are non‑constructive: they tell us that *some* graph exists, but they do not point to a specific one we can write down.

### 2.3.  Why we do not yet have an explicit 6‑chromatic unit‑distance graph

1. **No published construction** – All known papers that improve the lower bound stop at 5.  De Grey’s 2018 construction (1581 vertices) was found by a clever combination of smaller *Moser‑Spindle*‑type gadgets and massive computer search.  Extending that method to reach 6 has so far failed.

2. **Probabilistic methods give huge graphs** – A typical probabilistic argument (e.g. the Lovász local lemma applied to a random set of points on a large circle) shows that for a sufficiently large \(N\) (often astronomically big, e.g. \(N>10^{12}\)) a random unit‑distance graph will, with positive probability, have chromatic number 6.  Extracting an explicit subgraph from such a proof would require an exhaustive search through a combinatorial explosion that is far beyond current computing power.

3. **Algebraic constraints** – Unit‑distance edges impose equations of the form \((x_i-x_j)^2+(y_i-y_j)^2=1\).  Solving a large system of such equations exactly (to obtain rational or algebraic coordinates) is notoriously difficult.  Even if a 6‑chromatic graph is known to exist, turning the abstract graph into a concrete embedding in the plane is a separate hard problem.

4. **Verification with SAT solvers** – SAT‑based verification has been successfully used for the 5‑chromatic graphs (e.g. the 1581‑vertex graph).  The same technology *could* be applied once a concrete 6‑chromatic graph is written down, but it cannot create the graph for us.  The solver only checks a given instance.

### 2.4.  Summary answer to the student’s question

- **No explicit set of coordinates is known** that yields a unit‑distance graph requiring six colours.  
- The *only* rigorous lower bound at present is **5**, and the best explicit 5‑chromatic example is de Grey’s 1581‑vertex graph (coordinates are publicly available).  
- If a proof that \(\chi(\mathbb{R}^2)\ge 6\) ever appears, it will necessarily contain a concrete finite graph, and then a SAT‑solver could be used to verify that the graph is not 5‑colourable.  Until such a proof is published and vetted, we cannot produce the desired coordinates.

---

## 3.  Final answer

> **There is currently **no known explicit finite unit‑distance graph in the plane whose chromatic number is 6.** All published results give the lower bound \(\chi(\mathbb{R}^2)\ge 5\). A proof that \(\chi(\mathbb{R}^2)\ge 6\) would have to exhibit such a graph; a purely probabilistic existence proof would not yield concrete coordinates. Consequently we cannot at present write down a list of points and feed it to a SAT‑verifier to demonstrate that four (or five) colours are insufficient.**  

If and when a correct proof of \(\chi(\mathbb{R}^2)\ge 6\) appears, it will automatically provide the required explicit graph, and then the verification step becomes routine.

---

## 4.  Common mistakes when tackling this type of problem

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming a probabilistic existence proof automatically gives a small explicit example.** | Probabilistic arguments only guarantee *some* object exists, often of astronomically large size, without constructing it. | Remember the difference between “existence” and “constructive”. If you need an explicit graph, a non‑constructive proof is insufficient. |
| **Confusing the lower bound for the whole plane with a specific finite graph.** | The bound \(\chi(\mathbb{R}^2)\ge k\) is equivalent to “there exists a finite unit‑distance graph with chromatic number \(k\)”, but the proof must actually exhibit that graph. | Look for the concrete finite graph in the paper; if none is given, the claim is not yet a proof of the bound. |
| **Thinking a SAT‑solver can *discover* a 6‑chromatic graph from scratch.** | SAT solvers can only decide the colourability of a **given** graph. They do not generate graphs with a prescribed chromatic number. | Use SAT to verify a candidate graph, not to create one. |
| **Believing that any set of points with many unit distances must need many colours.** | High edge density does not automatically raise the chromatic number; specific structural constraints matter. | Study known constructions (Moser spindle, de Grey’s graph) to see which patterns force extra colours. |
| **Ignoring the algebraic nature of unit‑distance constraints.** | Coordinates must satisfy exact equations \((x_i-x_j)^2+(y_i-y_j)^2=1\); rounding errors can destroy the unit‑distance property. | When presenting an example, give exact algebraic numbers (or rational approximations together with a proof that distances are exactly 1). |

By keeping these pitfalls in mind, you’ll be better prepared to understand the current limits of the Hadwiger–Nelson problem and what would be required to push the lower bound from 5 to 6.

*Original question: [Explicit graph $H\subset\mathbb{R}^2$ with $\chi(H)\geq6$?](https://math.stackexchange.com/questions/5151609/explicit-graph-h-subset-mathbbr2-with-chih-geq6) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
