---
layout: question
title: '&quot;The object obtained by associating a space of any number of dimensions
  with an affine connection is called an affine space.&quot;?'
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: &quot;The object obtained by associating
  a space of any number of dimensions with an affine connection is called an affi'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is really asking  

The student has found two different “definitions’’ of the term **affine space** in the literature:

1.  In Veblen’s *Invariants of Differential Quadratic Forms* (and in many old differential‑geometric texts) the phrase  

    > “the object obtained by associating a space of any number of dimensions with an affine connection is called an affine space’’  

    is used.

2.  In most modern textbooks the phrase “affine space’’ means **a set on which a vector space acts freely and transitively** (a *torsor*).  

The student wants to know which of these two descriptions is the *correct* definition of an affine space.

---

## 2.  Step‑by‑step analysis  

### 2.1  The modern algebraic‑geometric definition  

Let \(V\) be a real (or complex) vector space.  
A **(real) affine space** modeled on \(V\) is a pair \((A,\tau)\) where  

* \(A\) is a non‑empty set,  
* \(\tau : V\times A \to A\) is an action \((v,a)\mapsto a+v\),

satisfying  

| Property | Meaning |
|----------|----------|
| **Free** | If \(a+v = a\) for some \(a\in A\) then \(v=0\). |
| **Transitive** | For any \(a,b\in A\) there is a unique \(v\in V\) with \(b = a+v\). |

In other words, the difference of two points of \(A\) is a *vector* in \(V\), and adding a vector to a point moves you to another point.  

Typical notation: if \(p,q\in A\) we write \(\overrightarrow{pq}\in V\) for the unique vector satisfying \(q = p+\overrightarrow{pq}\).  

This definition does **not** involve any notion of smoothness, connection, curvature, etc. It is the definition used in linear algebra, projective geometry, computer graphics, etc.

### 2.2  “Affine space’’ in the differential‑geometric literature  

In the early 20th‑century differential‑geometric tradition (Veblen, Weyl, Eisenhart, …) the word **affine** was used more loosely:

* An **affine connection** on a smooth manifold \(M\) is a rule \(\nabla\) that permits covariant differentiation of vector fields.  
* If a smooth manifold \(M\) is equipped with a (generally non‑flat) affine connection, some authors called the pair \((M,\nabla)\) an **affine space**.  
* If, in addition, the connection is *flat* (vanishing curvature) and *torsion‑free*, then locally there exist coordinates in which all Christoffel symbols are zero; the manifold looks like ordinary Euclidean space.  In that special case the same authors sometimes said the affine space is “flat’’ and could be regarded as Euclidean.

Thus Veblen’s sentence

> “The object obtained by associating a space of any number of dimensions with an affine connection is called an affine space”

means **“a smooth manifold together with a chosen affine connection’’**.  Modern terminology would call this an **affine manifold** (or an **affine connection space**) rather than an affine *space*.

### 2.3  Why the two meanings differ  

| Aspect | Modern “affine space’’ (torsor) | Veblen’s “affine space’’ (affine connection) |
|--------|--------------------------------|----------------------------------------------|
| Underlying set | Any set with a free, transitive \(V\)-action | A smooth manifold \(M\) |
| Extra structure | Only the action of a vector space | A connection \(\nabla\) (covariant derivative) |
| Curvature / torsion | Not defined | Defined via the connection; flat ↔ Euclidean |
| Typical notation | \(A\), \(\overrightarrow{pq}\) | \((M,\nabla)\) |
| Modern name (if you keep Veblen’s meaning) | – | **affine manifold** (or **manifold with affine connection**) |

Both uses are historically correct, but they refer to *different* mathematical objects.  In contemporary mathematics the word “affine space’’ is *almost always* reserved for the torsor definition.  When a manifold equipped with a connection is meant, authors say “affine manifold’’ or “manifold with an affine connection’’ to avoid ambiguity.

### 2.4  Which definition should you adopt?  

*If you are reading a modern algebra/geometry text* – use the torsor definition.  
*If you are reading an older differential‑geometric paper (Veblen, Eisenhart, etc.)* – interpret “affine space’’ as “a smooth manifold equipped with an affine connection’’ (often called an **affine manifold** today).

Consequently, **the “correct’’ definition depends on the context**.  In current standard terminology the first definition (torsor) is the accepted one; the second is an outdated usage that should be replaced by “affine manifold’’ when writing today.

---

## 3.  Final answer  

- **Standard modern definition**:  
  An **affine space** is a set \(A\) on which a vector space \(V\) acts freely and transitively (a torsor for \(V\)).  

- **Veblen’s definition**:  
  The phrase “affine space’’ is being used to mean a **smooth manifold equipped with an affine connection**; in modern language one would call this an **affine manifold** (or simply a manifold with an affine connection).  

Thus the “correct’’ definition is the torsor one; Veblen’s usage is an older, non‑standard terminology that should be interpreted as “affine manifold’’ in present‑day language.

---

## 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|-----------------|-----------------|
| **Confusing the two meanings** and assuming a torsor automatically has a connection. | A torsor has no smooth structure, no notion of parallel transport, curvature, etc. | Always check whether the source talks about a *manifold* and a *connection*; if yes, they are using the older “affine space’’ meaning. |
| **Calling any manifold with a connection an “affine space’’** without qualification. | Modern authors reserve “affine space’’ for the torsor; using the term loosely can lead to misunderstandings. | Use the term **affine manifold** or **manifold with an affine connection** for the differential‑geometric object. |
| **Assuming flatness = Euclidean** for a general affine connection. | Flatness (vanishing curvature) only guarantees locally Euclidean coordinates; globally the manifold may be a torus, a cylinder, etc. | Remember: flat ⇔ locally isomorphic to \(\mathbb{R}^n\); global topology can still be non‑trivial. |
| **Neglecting torsion** when the connection is not symmetric. | Veblen’s “affine connection’’ need not be torsion‑free; the presence of torsion changes the geometry. | State explicitly whether the connection is assumed symmetric (torsion‑free) or not. |

By keeping the two notions distinct and using the appropriate modern terminology, the confusion disappears.

*Original question: [&quot;The object obtained by associating a space of any number of dimensions with an affine connection is called an affine space.&quot;?](https://math.stackexchange.com/questions/5149502/the-object-obtained-by-associating-a-space-of-any-number-of-dimensions-with-an) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
