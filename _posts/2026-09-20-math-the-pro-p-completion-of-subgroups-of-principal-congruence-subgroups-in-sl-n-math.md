---
layout: question
title: The pro-$p$ completion of subgroups of principal congruence subgroups in $SL_n(\mathbb
  Z)$
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: The pro-$p$ completion of subgroups
  of principal congruence subgroups in $SL_n(\mathbb Z)$'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

* Let  

\[
\Gamma(m)=\{A\in SL_{n}(\mathbf Z)\;:\;A\equiv I\pmod m\}
\]

be the principal congruence subgroup of level \(m\).

* Fix a prime \(p\) and a positive integer \(k\).  
  Let  

\[
H\le \Gamma(p^{k})
\]

be any (abstract) subgroup.

* The **pro‑\(p\) completion** of a group \(G\) is  

\[
\widehat G_{\,p}= \varprojlim_{N\triangleleft G,\;[G:N]\text{ a power of }p} G/N .
\]

The question is: *Is it enough to take the normal subgroups \(N\) of the special form  
\(N=H\cap\Gamma(p^{n})\) (for \(n\ge 1\))?*  

Equivalently, does the inverse limit  

\[
\varprojlim_{n\ge 1}\; H\big/\bigl(H\cap\Gamma(p^{n})\bigr)
\tag{1}
\]

coincide with the pro‑\(p\) completion of \(H\)?

---

## 2.  Detailed solution

We shall prove that the answer is **yes**.  
The proof consists of three parts:

1.  The filtration \(\{\Gamma(p^{n})\}_{n\ge 1}\) makes \(\Gamma(p)=\Gamma(p^{1})\) a pro‑\(p\) group.  
2.  In a pro‑\(p\) group, the open normal subgroups are exactly the subgroups of finite
    \(p\)‑power index; they form a neighbourhood basis at the identity.  
3.  For a subgroup \(H\le\Gamma(p^{k})\) the induced pro‑\(p\) topology on \(H\) is given by the
    subgroups \(H\cap\Gamma(p^{n})\). Consequently (1) is the pro‑\(p\) completion of \(H\).

--------------------------------------------------------------------
### 2.1  \(\Gamma(p)\) is a pro‑\(p\) group

For any \(m\ge 1\) the natural reduction map  

\[
\pi_m:\Gamma(p)\longrightarrow SL_{n}(\mathbf Z/p^{m}\mathbf Z)
\]

has kernel \(\Gamma(p^{m})\).  
Hence  

\[
\Gamma(p)/\Gamma(p^{m})\cong \operatorname{im}\pi_m\le SL_{n}(\mathbf Z/p^{m}\mathbf Z).
\]

The group \(SL_{n}(\mathbf Z/p^{m}\mathbf Z)\) is a finite \(p\)-group when we look at the
congruence filtration:

\[
\Gamma(p^{m})/\Gamma(p^{m+1})\cong\{\,I+p^{m}X\mid X\in M_{n}(\mathbf Z/p\mathbf Z),\; \operatorname{tr}X=0 \,\},
\]

which is an elementary abelian \(p\)-group (additive group of trace‑zero matrices over \(\mathbf F_{p}\)).
Consequently each quotient \(\Gamma(p)/\Gamma(p^{m})\) is a finite \(p\)-group.
Moreover  

\[
\bigcap_{m\ge 1}\Gamma(p^{m})=\{I\}
\]

because a matrix that is congruent to the identity modulo every power of \(p\) must be the identity.
Thus \(\Gamma(p)\) is a **pro‑\(p\) group**: it is the inverse limit of the finite \(p\)-groups
\(\Gamma(p)/\Gamma(p^{m})\).

--------------------------------------------------------------------
### 2.2  Open normal subgroups of a pro‑\(p\) group

Let \(G\) be a pro‑\(p\) group.  
A subgroup \(U\le G\) is **open** iff the index \([G:U]\) is finite.  
Because every finite quotient of \(G\) is a \(p\)-group, an open subgroup has
\(p\)-power index; conversely, any normal subgroup of \(p\)-power index is open.
Therefore

\[
\{\,U\triangleleft G\mid [G:U]=p^{r}\text{ for some }r\,\}
\]

is precisely the set of open normal subgroups of \(G\), and these subgroups form a
neighbourhood basis of the identity.

A standard fact about the filtration \(\{ \Gamma(p^{n})\}\) inside \(\Gamma(p)\) is that it
is **cofinal** among all open normal subgroups:

> **Lemma.** For every open normal subgroup \(U\triangleleft\Gamma(p)\) there exists
> \(n\ge 1\) with \(\Gamma(p^{n})\subseteq U\).

*Proof.*  The quotients \(\Gamma(p)/\Gamma(p^{n})\) are the successive quotients of the
lower‑\(p\)-central series; they are powerful \(p\)-groups.  In a powerful pro‑\(p\) group the
\(p\)‑power map
\[
x\longmapsto x^{p}
\]
is surjective onto the next term of the filtration, i.e.
\((\Gamma(p^{n}))^{p}=\Gamma(p^{n+1})\).  
Since the family \(\{\Gamma(p^{n})\}\) is a descending chain of open normal subgroups,
any open normal \(U\) contains some term of the chain (otherwise the intersection
\(\bigcap_{n}\,U\Gamma(p^{n})\) would be a proper open subgroup containing all the
\(\Gamma(p^{n})\), contradicting \(\bigcap_{n}\Gamma(p^{n})=\{I\}\)). ∎

--------------------------------------------------------------------
### 2.3  The induced pro‑\(p\) topology on a subgroup \(H\)

Let \(H\le\Gamma(p^{k})\le\Gamma(p)\).  
Consider the family

\[
\mathcal{B}:=\{\,H\cap\Gamma(p^{n})\mid n\ge 1\,\}.
\]

* Each member of \(\mathcal{B}\) is a normal subgroup of \(H\) (intersection of two
  normal subgroups in the ambient group).
* Because \(\Gamma(p^{n})\) has index a power of \(p\) in \(\Gamma(p)\), the same holds
  for \(H\cap\Gamma(p^{n})\) inside \(H\).

Now let \(N\triangleleft H\) be any normal subgroup with \([H:N]=p^{t}\).
Consider its **closure** \(\overline N\) inside the pro‑\(p\) group \(\Gamma(p)\):
\(\overline N\) is an open normal subgroup of \(\Gamma(p)\) (open because the
quotient \(\Gamma(p)/\overline N\) is a finite \(p\)-group, namely a quotient of \(H/N\)).  
By the lemma of §2.2 there is an integer \(n\) such that \(\Gamma(p^{n})\subseteq\overline N\).
Intersecting with \(H\) gives  

\[
H\cap\Gamma(p^{n})\subseteq H\cap\overline N = N .
\]

Thus **every** normal subgroup of \(p\)-power index in \(H\) contains a member of
\(\mathcal{B}\). In other words, the collection \(\mathcal{B}\) is **cofinal** in the
directed set of all normal subgroups of \(p\)-power index in \(H\).

Consequences:

* The pro‑\(p\) topology on \(H\) (the topology whose neighbourhood basis at the identity
  is formed by all normal subgroups of \(p\)-power index) is the same as the topology
  generated by the subgroups \(H\cap\Gamma(p^{n})\).

* Therefore the pro‑\(p\) completion of \(H\) can be computed using only those
  subgroups:

\[
\widehat H_{\,p}\;=\;\varprojlim_{N\triangleleft H,\;[H:N]=p^{r}} H/N
\;=\;\varprojlim_{n\ge 1}\; H\big/\bigl(H\cap\Gamma(p^{n})\bigr).
\]

This is exactly the inverse limit asked about in the problem statement.

--------------------------------------------------------------------
### 2.4  Summary of the argument

| Step | Reason |


*Original question: [The pro-$p$ completion of subgroups of principal congruence subgroups in $SL_n(\mathbb Z)$](https://math.stackexchange.com/questions/5149906/the-pro-p-completion-of-subgroups-of-principal-congruence-subgroups-in-sl-n) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
