---
layout: question
title: Do wreath products require a faithful action?
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Do wreath products require a faithful
  action?'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What is being asked?

The student is reading the definition of a **(permutational) wreath product**  

\[
D\wr Q = D^{\Omega}\rtimes Q,
\]

where  

* \(D\) and \(Q\) are groups,  
* \(\Omega\) is a (finite) \(Q\)-set,  
* \(D^{\Omega}= \displaystyle\prod_{\omega\in\Omega} D_{\omega}\) (each \(D_{\omega}\cong D\)), and  
* \(Q\) acts on the direct product by permuting the coordinates:
  \[
  q\big((d_{\omega})_{\omega\in\Omega}\big)= (d_{q^{-1}\omega})_{\omega\in\Omega}.
  \]

Rotman then lets a **\(D\)-set** \(\Lambda\) be given and defines an action of the wreath product on the product set \(\Lambda\times\Omega\):

\[
\begin{aligned}
d_{\omega}^{*}(\lambda,\omega')&=
\begin{cases}
(d\lambda,\ \omega') &\text{if }\omega'=\omega,\\[2pt]
(\lambda,\ \omega')   &\text{if }\omega'\neq\omega,
\end{cases} \\[4pt]
q^{*}(\lambda,\omega')&=(\lambda,\;q\omega').
\end{aligned}
\]

The book then says that  

* the set \(\{d_{\omega}^{*}\mid d\in D\}\) (denoted \(D_{\omega}^{*}\)) is **isomorphic** to \(D\), and  
* the set \(\{q^{*}\mid q\in Q\}\) (denoted \(Q^{*}\)) is **isomorphic** to \(Q\).

The student wonders:

1. Does this identification really need the actions of \(D\) on \(\Lambda\) and of \(Q\) on \(\Omega\) to be *faithful*?  
2. Does the definition of a wreath product implicitly assume that the action of \(Q\) on \(\Omega\) is faithful?  
3. Must the set \(\Omega\) be finite?

We will answer each question in turn, showing why the statements in the book are correct (or need a mild extra hypothesis) and what the general definition of a wreath product actually requires.

---

## 2.  The abstract (unrestricted) wreath product does **not** need any action to be faithful

### 2.1  The definition as a semidirect product

Let  

\[
K = D^{\Omega}= \{f:\Omega\to D\}\quad\text{(with pointwise multiplication)}.
\]

\(Q\) acts on \(K\) by *permuting the argument*:

\[
\bigl(q\cdot f\bigr)(\omega)=f\!\bigl(q^{-1}\omega\bigr),\qquad q\in Q,\;f\in K,\;\omega\in\Omega.
\]

The **(unrestricted) wreath product** is the semidirect product

\[
D\wr_{\Omega} Q:= K\rtimes Q.
\]

This construction makes sense for **any** groups \(D,Q\) and **any** (possibly infinite) \(Q\)-set \(\Omega\).  
No hypothesis about faithfulness appears at all.

### 2.2  The natural embeddings of \(D\) and \(Q\)

* **Embedding of \(D\).**  
  For a fixed \(\omega_{0}\in\Omega\) define  

  \[
  \iota_{\omega_{0}}: D\longrightarrow K,\qquad
  \iota_{\omega_{0}}(d)(\omega)=
  \begin{cases}
  d &\text{if }\omega=\omega_{0},\\
  1_{D} &\text{otherwise}.
  \end{cases}
  \]

  Since different \(d\)’s give different functions, \(\iota_{\omega_{0}}\) is injective.  
  Composing with the inclusion \(K\hookrightarrow K\rtimes Q\) we obtain an injective homomorphism  

  \[
  D\;\xrightarrow{\;\iota_{\omega_{0}}\;}\; D\wr_{\Omega} Q .
  \]

  This is exactly the subgroup denoted \(D^{*}_{\omega_{0}}\) in Rotman’s description.

* **Embedding of \(Q\).**  
  The map  

  \[
  \jmath: Q\longrightarrow D\wr_{\Omega} Q,\qquad
  \jmath(q)=(1_{K},q)
  \]

  is always injective, because the first component is the identity of \(K\).  
  Its image is the subgroup called \(Q^{*}\).

Thus the *abstract* wreath product always contains copies of \(D\) and \(Q\) (inside the semidirect product) **without any need for faithful actions**.

---

## 3.  The *permutational* wreath product on \(\Lambda\times\Omega\)

Rotman now equips the set \(\Lambda\times\Omega\) with a permutation action of the above group.  
The formulas

\[
d_{\omega}^{*}(\lambda,\omega')=
\begin{cases}
(d\lambda,\omega') & \omega'=\omega,\\
(\lambda,\omega')  & \omega'\neq\omega,
\end{cases}
\qquad
q^{*}(\lambda,\omega')=(\lambda,q\omega')
\]

are obtained by letting  

* the copy \(D_{\omega}^{*}\) act **only on the first coordinate** when the second coordinate equals \(\omega\), and  
* the copy \(Q^{*}\) act by permuting the second coordinate.

### 3.1  When is \(D_{\omega}^{*}\cong D\)?

Consider the homomorphism  

\[
\phi_{\omega}: D\longrightarrow \operatorname{Sym}(\Lambda\times\Omega),\qquad
\phi_{\omega}(d)=d_{\omega}^{*}.
\]

If \(d\in\ker\phi_{\omega}\) then for every \(\lambda\in\Lambda\)

\[
d_{\omega}^{*}(\lambda,\omega)=(d\lambda,\omega)=(\lambda,\omega),
\]

so \(d\lambda=\lambda\) for all \(\lambda\in\Lambda\).  
Hence  

\[
\ker\phi_{\omega}= \ker\bigl(D\curvearrowright\Lambda\bigr).
\]

Therefore  

\[
D_{\omega}^{*}\;\cong\; D / \ker(D\curvearrowright\Lambda).
\]

If the action of \(D\) on \(\Lambda\) is **faithful** (i.e. the kernel is \(\{1\}\)), then the quotient is just \(D\) and we obtain the claimed isomorphism \(D\cong D_{\omega}^{*}\).

If the action on \(\Lambda\) is not faithful, the statement in the book is still true **up to the natural quotient**: the subgroup \(D_{\omega}^{*}\) is isomorphic to the *image* of \(D\) in \(\operatorname{Sym}(\Lambda)\). Many authors simply assume from the outset that \(\Lambda\) is a faithful \(D\)-set, because the purpose of the construction is to view \(D\) as a permutation group.

### 3.2  When is \(Q^{*}\cong Q\)?

Analogously, the map  

\[
\psi : Q\longrightarrow \operatorname{Sym}(\Lambda\times\Omega),\qquad
\psi(q)=q^{*},
\]

has kernel  

\[
\ker\psi = \{\,q\in Q\mid q\omega=\omega\text{ for every }\omega\in\Omega\,\}
      = \bigcap_{\omega\in\Omega}\operatorname{Stab}_{Q}(\omega),
\]

i.e. the subgroup of \(Q\) that fixes **every** point of \(\Omega\).  
Thus  

\[
Q^{*}\;\cong\; Q / \bigcap_{\omega\in\Omega}\operatorname{Stab}_{Q}(\omega)
            \;=\; \text{image of }Q\text{ in }\operatorname{Sym}(\Omega).
\]

If the action of \(Q\) on \(\Omega\) is faithful (kernel \(=1\)), we obtain \(Q^{*}\cong Q\).  
Otherwise we obtain an isomorphic copy of the **permutation quotient** \(Q^{\text{perm}}:=Q/\ker(Q\curvearrowright\Omega)\).

So the book’s statement “\(Q\cong Q^{*}\)” is valid under the usual (implicit) hypothesis that \(\Omega\) is taken as a *faithful* \(Q\)-set. If the action is not faithful, one simply replaces \(Q\) by its image in \(\operatorname{Sym}(\Omega)\); the wreath product does not change, because the semidirect product \(D^{\Omega}\rtimes Q\) depends only on that image.

---

## 4.  Must \(\Omega\) be finite?

Two variants are common:

| Variant | Notation | Description of the base group |
|---------|----------|--------------------------------|
| **Restricted (regular) wreath product** | \(D\wr_{\Omega}^{\text{res}} Q\) | \(D^{(\Omega)} = \bigoplus_{\omega\in\Omega} D_{\omega}\) – the *direct sum* (functions with finite support). |
| **Unrestricted wreath product** | \(D\wr_{\Omega} Q\) | \(D^{\Omega}= \prod_{\omega\in\Omega} D_{\omega}\) – the *full direct product* (all functions). |

*If \(\Omega\) is **finite**, the direct sum and the direct product coincide, so there is only one construction.*  

If \(\Omega\) is **infinite**, one must decide whether to allow arbitrary functions \(\Omega\to D\) (unrestricted) or only those with finite support (restricted). Both are perfectly legitimate definitions; the choice depends on the intended applications.

Rotman works with a **finite** \(Q\)-set \(\Omega\

*Original question: [Do wreath products require a faithful action?](https://math.stackexchange.com/questions/5151790/do-wreath-products-require-a-faithful-action) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
