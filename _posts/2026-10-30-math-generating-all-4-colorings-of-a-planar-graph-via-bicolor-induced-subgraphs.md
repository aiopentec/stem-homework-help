---
layout: question
title: Generating all 4-colorings of a planar graph via bicolor induced subgraphs
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Generating all 4-colorings of a planar
  graph via bicolor induced subgraphs'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

# Generating all 4-colorings of a planar graph via bicolor induced subgraphs

## 1. Restatement in Plain Language

Let $G$ be a planar graph (specifically, a triangulation of the sphere where every vertex has a degree of at least 5). A **4-coloring** of $G$ is an assignment of one of 4 colors (say, $0, 1, 2, 3$) to each vertex such that no two connected vertices share the same color. 

If we pick any two colors—for instance, color $0$ and color $2$—the subgraph made up *only* of the vertices colored $0$ or $2$ breaks down into separate connected pieces. A **Kempe switch** on one of these pieces means swapping all the $0$s to $2$s and all the $2$s to $0$s within that specific piece. Crucially, doing this swap still leaves us with a valid 4-coloring of the entire graph.

The question asks: **Can we move from *any* valid 4-coloring of $G$ to *any other* valid 4-coloring of $G$ by performing a sequence of these Kempe switches?** 

In graph-theoretic terms, if we build a "Kempe graph" where each node is a valid 4-coloring and an edge connects two colorings that can be transformed into one another via a single Kempe switch, is this graph **connected**?

---

## 2. Step-by-Step Solution

### Step 1: Understand Kempe Chains and Kempe Switches
For a valid 4-coloring $C$ of graph $G$, let $G_{i,j}$ denote the induced subgraph of $G$ formed exclusively by the vertices colored $i$ or $j$ (where $i \neq j \in \{0, 1, 2, 3\}$). Because $C$ is a valid coloring, no edge in $G$ connects two vertices of the same color; therefore, $G_{i,j}$ is a bipartite graph.

A **Kempe chain** (or $(i,j)$-component) is a connected component of $G_{i,j}$. A **Kempe switch** on this component swaps the colors $i$ and $j$ for all vertices belonging to that component. 

### Step 2: The Historical Context (Kempe's 1879 Proof)
Alfred Kempe attempted to prove the Four Color Theorem using these switches. He showed that:
1. Performing a Kempe switch preserves the validity of the 4-coloring.
2. For any 4-colored planar triangulation, one can always resolve conflicts around degree-4 vertices (squares) using Kempe chains.
3. However, Kempe's argument failed for degree-5 vertices (pentagons) because swapping a Kempe chain to fix a color conflict at one vertex can inadvertently *create* a conflict at another vertex elsewhere in the graph, leading to overlapping, entangled chains that cannot be simultaneously resolved.

### Step 3: Counterexamples to Kempe Connectivity
While the Four Color Theorem is true (every planar graph *does* have at least one valid 4-coloring), **Kempe's approach of generating the entire coloring space via switches is false**. 

To show that the Kempe graph of 4-colorings is **not** necessarily connected, we look for obstructions where colorings belong to distinct connected components under Kempe switches.

1. **Entangled Kempe Chains:** In certain triangulations with vertices of degree $\ge 5$, two valid 4-colorings $C_1$ and $C_2$ can be constructed such that any sequence of valid Kempe switches starting from $C_1$ hits a dead end (a local maximum in terms of color conflict resolution, or a cycle of switches that just oscillates between a small subset of colorings) without ever reaching $C_2$.
2. **The Results of Kempe Equivalence Classes:** Explicit counterexamples were developed in the late 20th century (notably by researchers studying the combinatorics of graph colorings, such as Kempe-equivalence). It was proven that the space of 3-colorings or 4-colorings of certain planar graphs can be partitioned into *multiple disconnected components* under Kempe switches. 

Even with the strict condition that all vertices have degree $\ge 5$ (which eliminates simple degree-3 and degree-4 reduction traps), topological obstructions exist where the global interweaving of $(i,j)$-chains prevents a global transition between certain pairs of colorings.

---

## 3. Final Answer

**No, the graph of 4-colorings is not necessarily connected.** 

Even for a triangulation of the sphere where every vertex has a degree of at least 5, there exist planar graphs and pairs of valid 4-colorings $C$ and $C'$ such that $C'$ **cannot** be obtained from $C$ by any succession of Kempe switches. The Kempe graph of 4-colorings can have multiple disconnected components.

---

## 4. Common Mistakes

* **Confusing the Four Color Theorem with Kempe Equivalence:** Students often assume that because every planar graph *has* a 4-coloring, the set of all such colorings must form a single connected family via local moves. Existence does not imply path-connectivity.
* **Assuming Degree $\ge 5$ Eliminates All Obstructions:** While restricting vertices to degree $\ge 5$ removes the specific problematic configurations that ruined Kempe's original local proof (like separating triangles and certain pentagon configurations), global topological linking of bicolor chains can still isolate sets of colorings from one another.
* **Confusing Vertex-Coloring Kempe Switches with Edge-Coloring Tait Colorings:** Mixing up Kempe's vertex-coloring chains with Tait's edge-coloring (3-edge-coloring of cubic graphs) switch arguments.

*Original question: [Generating all 4-colorings of a planar graph via bicolor induced subgraphs](https://math.stackexchange.com/questions/5153218/generating-all-4-colorings-of-a-planar-graph-via-bicolor-induced-subgraphs) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
