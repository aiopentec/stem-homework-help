---
layout: post
title: Classification of local Artin (commutative) rings which are finite over an
  algebraically closed field
author: StemFix Bot
category: math
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking  

Let  

\[
A\;\text{ be a commutative local Artin $k$‑algebra that is finite as a $k$‑vector space,}
\]

where \(k\) is an algebraically closed field.  
The student wants a **concrete description** of all such rings.  
In particular:

* When the maximal ideal \(\mathfrak m\) of \(A\) is principal one can write  
  \(A\cong k[t]/(t^{n})\).  
* If \(\mathfrak m\) needs more generators, can we still write \(A\) in a simple
  “\(k[t^{a_{1}},\dots ,t^{a_{r}}]/(\text{power of }t)\)” way?  
* If not, what is the general (non‑tautological) description of these algebras?

We will answer these points completely.

--------------------------------------------------------------------

## 2.  General facts about local Artin \(k\)-algebras  

### 2.1  Finite‑dimensional + local ⇒ residue field = \(k\)

Because \(k\) is algebraically closed, any finite‑dimensional local
\(k\)-algebra has residue field equal to \(k\).  
Indeed, the residue field is a finite field extension of \(k\), but an
algebraically closed field has no non‑trivial finite extensions.  
Thus  

\[
A/\mathfrak m \;\cong\; k .
\]

Consequently every such \(A\) is a *local* \(k\)-algebra with maximal ideal
\(\mathfrak m\) *nilpotent* (Artinian ⇒ \(\mathfrak m^{N}=0\) for some \(N\)).

### 2.2  Minimal generators of \(\mathfrak m\)

Let  

\[
e:=\dim_{k}\bigl(\mathfrak m/\mathfrak m^{2}\bigr)
\]

(the **embedding dimension** of \(A\)).  
Choose elements  

\[
x_{1},\dots ,x_{e}\in\mathfrak m
\]

whose classes form a \(k\)-basis of \(\mathfrak m/\mathfrak m^{2}\).  
Then \(\{x_{1},\dots ,x_{e}\}\) generates \(\mathfrak m\) and therefore
generates \(A\) as a \(k\)-algebra.

### 2.3  Presentation by a quotient of a polynomial ring  

Define a surjection of \(k\)-algebras  

\[
\pi : k[x_{1},\dots ,x_{e}] \longrightarrow A, \qquad 
x_{i}\mapsto x_{i}\;(\text{the chosen elements in }A).
\]

Because \(\mathfrak m^{N}=0\) for some \(N\), the kernel of \(\pi\) contains the
ideal \((x_{1},\dots ,x_{e})^{N}\).  Hence

\[
\boxed{ \;A\;\cong\;k[x_{1},\dots ,x_{e}]/I \;}
\]

where \(I\) is an ideal satisfying  

\[
(x_{1},\dots ,x_{e})^{N}\subseteq I
\quad\text{for some }N\gg 0 .
\]

Conversely, any quotient of a polynomial ring by an ideal containing a power
of the maximal ideal is a finite‑dimensional local \(k\)-algebra with residue
field \(k\).  

Thus **every** local Artin \(k\)-algebra finite over \(k\) is a *finite*
quotient of a polynomial ring in finitely many variables, and the number of
variables equals the embedding dimension \(e\).

### 2.4  Relation with the Cohen structure theorem  

The Cohen structure theorem says that a *complete* Noetherian local ring with
residue field \(k\) is a quotient of a formal power series ring

\[
k[[X_{1},\dots ,X_{e}]] \big/ (f_{1},\dots ,f_{r}).
\]

For an Artinian local algebra the ring is already complete (its maximal
ideal is nilpotent), so we may replace the formal power series by ordinary
polynomials; the description above is exactly the “polynomial version’’ of
Cohen’s theorem.

--------------------------------------------------------------------

## 3.  What does this description look like in practice?  

### 3.1  The monogenic case (\(e=1\))

If \(e=1\) then \(\mathfrak m\) is principal and we obtain

\[
A\cong k[t]/(t^{n})\qquad (n\ge 1).
\]

These are precisely the *local* Artin \(k\)-algebras of embedding dimension
\(1\).

### 3.2  Two generators (\(e=2\))

Take two generators \(x,y\) of \(\mathfrak m\).  A typical example is

\[
A\;=\;k[x,y]/(x^{2},xy,y^{2})\quad(\dim_{k}A=3).
\]

Another family is

\[
A_{m,n}=k[x,y]/(x^{m},y^{n},xy),\qquad m,n\ge 2 .
\]

Both have maximal ideal \((x,y)\) which is **not** principal.

### 3.3  Higher embedding dimension  

For any \(e\ge 1\) one may take

\[
A_{e,N}=k[x_{1},\dots ,x_{e}]/(x_{1},\dots ,x_{e})^{N},
\qquad N\ge 2 .
\]

These are the “truncated polynomial algebras’’ of order \(N\).  Their
maximal ideal needs \(e\) generators.

### 3.4  “Adjoin powers of a single element’’ is not enough in general  

The presentation  

\[
k[t^{a_{1}},\dots ,t^{a_{r}}]/(t^{N})
\]

is a **subring** of a monogenic Artin algebra; it forces all generators to
lie in the *same* principal ideal \((t)\).  Consequently it can only produce
rings whose maximal ideal is *principal* (i.e. \(e=1\)).  
Any algebra with embedding dimension \(e\ge 2\) (for example the algebras
above) cannot be written in that form.  Hence the “adjoin powers of a single
\(t\)” description **does not cover the general case**.

--------------------------------------------------------------------

## 4.  How far can we go in classifying them?  

The description “\(k[x_{1},\dots ,x_{e}]/I\) with \((x_{1},\dots ,x_{e})^{N}
\subseteq I\)” is already *non‑tautological* and is the standard way experts
refer to these rings.  A finer classification (up to isomorphism) quickly
becomes impossible:

* For \(\dim_{k}A\le 6\) there are only finitely many isomorphism classes
  (this can be proved by a brute‑force enumeration of possible multiplication
  tables).  
* Starting at dimension \(7\) the problem is **wild**: classifying all such
  algebras is at least as hard as classifying finite‑dimensional modules
  over the free algebra \(k\langle u,v\rangle\), a problem known to be
  hopelessly intricate (see Drozd’s theorem on wildness).  

Thus there is **no simple list** of all local Artin \(k\)-algebras; the
polynomial‑quotient description is essentially the best one can hope for.

--------------------------------------------------------------------

## 5.  Final answer  

*Let \(k\) be an algebraically closed field.  
A commutative local Artin \(k\)-algebra that is finite over \(k\) is
exactly a quotient*

\[
\boxed{ \;A\;\cong\;k[x_{1},\dots ,x_{e}]/I \;}
\]

*where*

* \(e=\dim_{k}(\mathfrak m/\mathfrak m^{2})\) (the embedding dimension);
* the ideal \(I\) contains a power of the maximal ideal,
  \((x_{1},\dots ,x_{e})^{N}\) for some \(N\);
* the residue field of \(A\) is \(k\).

If \(e=1\) this reduces to the familiar rings \(k[t]/(t^{n})\).  
If \(e\ge 2\) the maximal ideal is not principal, and such algebras cannot be
written as “\(k[t^{a_{1}},\dots ,t^{a_{r}}]/(t^{N})\)”.  Examples are
\(k[x,y]/(x^{2},xy,y^{2})\) or \(k[x,y]/(x^{m},y^{n},xy)\).

Beyond the above presentation, a complete classification up to isomorphism
is known to be **wild** for dimensions \(\ge 7\); therefore the polynomial‑
quotient description is the natural and essentially optimal way to describe
all local Artin \(k\)-algebras finite over an algebraically closed field.

--------------------------------------------------------------------

## 6.  Common mistakes  

| Mistake | Why it is wrong | Correct viewpoint |
|---------|----------------|-------------------|
| **Assuming every such algebra is generated by one element** | The maximal ideal may need several generators; e.g. \(k[x,y]/(x^{2},xy,y^{2})\) has embedding dimension 2. | Use the embedding dimension \(e=\dim_{k}\mathfrak m/\mathfrak m^{2}\); the algebra is a quotient of a polynomial ring in \(e\) variables. |
| **Writing \(A=k[t^{a_{1}},\dots ,t^{a_{r}}]/(t^{N})\) for all cases** | This forces all generators to lie in the same principal ideal \((t)\) and thus forces \(\mathfrak m\) to be principal. | Only the case \(e=1\) admits such a description; for \(e\ge2\) one needs several independent variables. |
| **Thinking a finite list of “normal forms’’ exists** | Classification becomes wild already for dimension 7; there are families depending on continuous parameters. | The best general description is the presentation as a quotient of a polynomial ring containing a power of the maximal ideal. |
| **Confusing “Artinian’’ with “reduced’’** | Artinian local algebras are usually highly non‑reduced; their maximal ideal is nilpotent. | Remember that \(\mathfrak m^{N}=0\) for some \(N\); this is what guarantees the existence of the containing power \((x_{1},\dots ,x_{e})^{N}\). |

Keeping these points in mind will prevent the most frequent errors when
working with local Artin \(k\)-algebras.

*Original question: [Classification of local Artin (commutative) rings which are finite over an algebraically closed field](https://math.stackexchange.com/questions/384902/classification-of-local-artin-commutative-rings-which-are-finite-over-an-algeb) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
