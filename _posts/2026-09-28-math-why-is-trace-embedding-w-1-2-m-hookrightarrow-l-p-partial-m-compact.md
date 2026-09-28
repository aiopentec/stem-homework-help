---
layout: question
title: Why is trace embedding $W^{1,2}(M) \hookrightarrow L^p(\partial M)$ compact
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Why is trace embedding $W^{1,2}(M)
  \hookrightarrow L^p(\partial M)$ compact'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  Restatement in plain language  

Let  

* \(M\) be a compact \(n\)-dimensional Riemannian manifold with (non‑empty) smooth boundary \(\partial M\);
* \(W^{1,2}(M)=H^{1}(M)\) be the usual Sobolev space of functions whose first weak derivatives are square‑integrable;
* \(L^{p}(\partial M)\) be the Lebesgue space on the boundary equipped with the induced surface measure.

The **trace operator**  
\[
\operatorname{Tr}:W^{1,2}(M)\longrightarrow L^{p}(\partial M),\qquad
u\mapsto u|_{\partial M}
\]
is known to be **continuous** for every  
\[
1\le p\le p^{*}:=\frac{2(n-1)}{n-2}\qquad (n\ge 3),
\]
(and for all \(p<\infty\) when \(n=2\)).  

The question asks to prove that this trace map is **compact** when the exponent is *strictly sub‑critical*:

\[
\boxed{\; 1\le p<p^{*}\ \Longrightarrow\ \operatorname{Tr}:W^{1,2}(M)\hookrightarrow L^{p}(\partial M)\ \text{is compact.}\;}
\]

In addition we should comment on how much regularity of the boundary is really needed (Lipschitz, \(C^{1}\), …).

---

## 2.  Full proof  

The proof proceeds in three stages:

| Step | What we do | Reason |
|------|------------|--------|
| 1 | Reduce the problem to a local statement on a half‑space \(\mathbb{R}^{n}_{+}\) using charts and a partition of unity. | Manifolds are locally Euclidean; the trace operator is local. |
| 2 | Prove the compactness of the trace on a bounded Lipschitz domain \(\Omega\subset\mathbb{R}^{n}\) (in particular on a half‑ball). | This is the Euclidean Rellich–Kondrachov theorem together with continuity of the trace. |
| 3 | Patch the local results together to obtain compactness on the whole manifold. | A finite covering and a partition of unity preserve compactness. |

We now go through the details.

--------------------------------------------------------------------
### 2.1  Preliminaries  

* **Sobolev–trace theorem (continuous embedding).**  
  For a bounded Lipschitz domain \(\Omega\subset\mathbb{R}^{n}\) there is a bounded linear operator  
  \[
  T_{\Omega}:W^{1,2}(\Omega)\longrightarrow L^{p}(\partial\Omega),\qquad
  1\le p\le p^{*},
  \]
  with norm depending only on \(n\), the Lipschitz constant of \(\partial\Omega\) and \(|\Omega|\).  

* **Rellich–Kondrachov theorem (compact embedding).**  
  If \(\Omega\) is bounded with Lipschitz boundary, the inclusion  
  \[
  W^{1,2}(\Omega)\hookrightarrow L^{q}(\Omega)
  \]
  is compact for every \(1\le q<2^{*}:=\frac{2n}{n-2}\) (the critical Sobolev exponent).  

* **Relation between the two exponents.**  
  The critical trace exponent satisfies  
  \[
  p^{*}= \frac{2(n-1)}{n-2}= \frac{2(n-1)}{n-2}= \frac{2n}{n-2}\cdot\frac{n-1}{n}
        = 2^{*}\,\frac{n-1}{n},
  \]
  i.e. \(p^{*}<2^{*}\) for \(n\ge 3\). Consequently, if \(p<p^{*}\) we can find a number \(q\) with
  \[
  p<q<2^{*}
  \]
  and use the compact embedding into \(L^{q}(\Omega)\) together with the continuity of the trace.

--------------------------------------------------------------------
### 2.2  Local compactness on a Euclidean half‑space  

Let \(\Omega\subset\mathbb{R}^{n}\) be a bounded Lipschitz domain.  
Choose a smooth cutoff \(\chi\in C^{\infty}_{c}(\overline{\Omega})\) that equals \(1\) near a piece of the boundary where we shall work.  

Consider a bounded sequence \(\{u_{k}\}\subset W^{1,2}(\Omega)\).  
Because the trace operator is continuous,
\[
\{T_{\Omega}u_{k}\}\subset L^{p}(\partial\Omega)
\]
is bounded.

**Step 2.2.1 – Use Rellich inside the domain.**  
Pick any exponent \(q\) such that \(p<q<2^{*}\). By Rellich,
\[
\{u_{k}\}\ \text{is relatively compact in}\ L^{q}(\Omega).
\]
Hence (after passing to a subsequence) we have  
\[
u_{k}\longrightarrow u\quad\text{strongly in }L^{q}(\Omega).
\]

**Step 2.2.2 – Interpolation to the boundary.**  
The trace theorem gives a bounded linear map
\[
T_{\Omega}:L^{q}(\Omega)\longrightarrow L^{p}(\partial\Omega),
\]
because for \(q\ge 2\) the usual estimate
\[
\|T_{\Omega}v\|_{L^{p}(\partial\Omega)}
   \le C\|v\|_{W^{1,2}(\Omega)}^{\theta}
          \|v\|_{L^{q}(\Omega)}^{1-\theta}
\]
holds with suitable \(\theta\in(0,1)\). In particular, the restriction of \(T_{\Omega}\) to the compact set
\[
K:=\{v\in L^{q}(\Omega):\|v\|_{L^{q}(\Omega)}\le C\}
\]
is **compact** (the composition of a compact embedding \(L^{q}(\Omega)\hookrightarrow L^{p}(\partial\Omega)\) with the bounded inclusion \(W^{1,2}\hookrightarrow L^{q}\)).  

Consequently,
\[
T_{\Omega}u_{k}\longrightarrow T_{\Omega}u\quad\text{strongly in }L^{p}(\partial\Omega).
\]

Thus every bounded sequence in \(W^{1,2}(\Omega)\) has a subsequence whose traces converge in \(L^{p}(\partial\Omega)\). This proves:

> **Lemma.** Let \(\Omega\subset\mathbb{R}^{n}\) be a bounded Lipschitz domain. For any \(1\le p<p^{*}\) the trace operator
> \[
> T_{\Omega}:W^{1,2}(\Omega)\to L^{p}(\partial\Omega)
> \]
> is compact.

--------------------------------------------------------------------
### 2.3  Transfer to a compact manifold  

Now let \(M\) be a compact Riemannian manifold with (smooth) boundary \(\partial M\).  

1. **Cover the boundary by coordinate charts.**  
   Because \(\partial M\) is compact, we can choose finitely many boundary charts  
   \[
   \Phi_{j}:U_{j}\longrightarrow B^{+}_{r}\subset\mathbb{R}^{n}_{+},
   \qquad j=1,\dots,N,
   \]
   where each \(U_{j}\) is an open neighbourhood of a piece of \(\partial M\) and  
   \(B^{+}_{r}\) denotes a half‑ball in the Euclidean half‑space.  
   The maps \(\Phi_{j}\) are \(C^{\infty}\) diffeomorphisms with uniformly bounded Jacobians because the boundary is smooth (Lipschitz is enough).

2. **Partition of unity.**  
   Choose \(\{\psi_{j}\}_{j=0}^{N}\subset C^{\infty}(M)\) such that  
   \(\sum_{j=0}^{N}\psi_{j}\equiv 1\) on \(M\), each \(\psi_{j}\) has support in \(U_{j}\), and \(\psi_{0}\) is supported away from the boundary.  

3. **Localisation of a bounded sequence.**  
   Let \(\{u_{k}\}\subset W^{1,2}(M)\) be bounded. Then each product \(\psi_{j}u_{k}\) belongs to \(W^{1,2}(U_{j})\) and the norm
   \[
   \|\psi_{j}u_{k}\|_{W^{1,2}(U_{j})}\le C\|u_{k}\|_{W^{1,2}(M)}
   \]
   with a constant independent of \(k\) and \(j\).

4. **Apply the Euclidean lemma.**  
   For \(j\ge 1\) (the charts intersecting the boundary) pull back by \(\Phi_{j}\):
   \[
   v_{k}^{(j)} := (\psi_{j}u_{k})\circ\Phi_{j}^{-1}\in W^{1,2}(B^{+}_{r}).
   \]
   The previous Lemma tells us that, after passing to a subsequence (still denoted \(k\)), the traces
   \[
   T_{j}v_{k}^{(j)}\ \longrightarrow\ w^{(j)}\quad\text{in }L^{p}\bigl(\partial B^{+}_{r}\bigr).
   \]
   Translating back to the manifold,
   \[
   (\psi_{j}u_{k})|_{\partial M}\ \longrightarrow\ (\psi_{j}w)\ \text{in }L^{p}(\partial M)
   \]
   for some limit function \(w^{(j)}\) defined on the corresponding piece of \(\partial M\).

5. **The interior part is irrelevant.**  
   The term \(\psi_{0}u_{k}\) vanishes on \(\partial M\); therefore it does not affect the trace.

6. **Reassemble the pieces.**  
   Because the covering is finite, we can extract a **single subsequence** that works simultaneously for all \(j=1,\dots,N\).  
   On the whole boundary,
   \[
   u_{k}|_{\partial M}= \sum_{j=1}^{N}\bigl(\psi_{j}u_{k}\bigr)|_{\partial M}
   \]
   converges in \(L^{p}(\partial M)\) to \(\sum_{j=1}^{N} w^{(j)}\).

Thus **every bounded sequence in \(W^{1,2}(M)\) has a subsequence whose traces converge in \(L^{p}(\partial M)\)**. This is precisely the definition of a compact operator. Hence the trace map is compact for all sub‑critical exponents.

--------------------------------------------------------------------
### 2.4  Remarks on the regularity of the boundary  

* The argument only uses the **Lipschitz** regularity of the boundary charts: we need the trace theorem and the Rellich–Kondrachov theorem on each chart, both of which are valid for bounded Lipschitz domains.  

* Consequently, the statement remains true if \(\partial M\) is merely **Lipschitz** (or piecewise \(C^{1}\) with uniformly bounded Lipschitz constants). Smoothness of the boundary is *not* required for compactness, although it guarantees the existence of smooth charts and simplifies the exposition.

--------------------------------------------------------------------
## 3.  Final answer  

*For a compact \(n\)-dimensional Riemannian manifold \(M\) with (Lipschitz) boundary \(\partial M\) and for every exponent*

\[
1\le p<p^{*}:=\frac{2(n-1)}{n-2}\qquad (n\ge 3)
\]

*the trace operator*

\[
\operatorname{Tr}:W^{1,2}(M)\longrightarrow L^{p}(\partial M),\qquad 
u\mapsto u|_{\partial M},
\]

*is a **compact** linear map. The same holds for all finite \(p\) when \(n=2\). The only regularity required on the boundary is Lipschitz (in particular \(C^{1}\) is more than enough).*

--------------------------------------------------------------------
## 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing continuity with compactness.** Believing that because the trace operator is bounded it must automatically be compact. | Compactness is a stronger property: bounded sets must be sent to relatively compact (pre‑compact) sets. | Explicitly use Rellich–Kondrachov to obtain strong convergence of a subsequence inside the domain, then pass to the boundary via the trace. |
| **Using the critical exponent \(p^{*}\) in the compactness claim.** The trace is *not* compact for \(p=p^{*}\). | At the critical exponent one can construct “bubbling” sequences that

*Original question: [Why is trace embedding $W^{1,2}(M) \hookrightarrow L^p(\partial M)$ compact](https://math.stackexchange.com/questions/5150607/why-is-trace-embedding-w1-2m-hookrightarrow-lp-partial-m-compact) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
