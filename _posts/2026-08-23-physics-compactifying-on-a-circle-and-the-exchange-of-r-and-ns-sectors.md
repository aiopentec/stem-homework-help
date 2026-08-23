---
layout: post
title: Compactifying on a circle and the exchange of R and NS sectors
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

When we compactify a ten‑dimensional superstring on a circle \(S^{1}\) we obtain a lower‑dimensional theory (for definiteness we will go to nine dimensions).  
The massless fields in ten dimensions come either from the **NS (Neveu–Schwarz)** sector or from the **R (Ramond)** sector of the world‑sheet theory.  

Empirically one finds the following pattern:

| 10‑d field | 9‑d field after compactification | Why? |
|------------|--------------------------------|------|
| NS field with **no index** along the circle → stays NS in 9‑d | a 9‑d field of the same type |
| NS field **with one index** along the circle → becomes an **R** field in 9‑d | the internal index “flips’’ the sector |
| The same pattern holds for fermions, but the spinor bundle behaves as a **tensor product** rather than a direct sum. |

The student wants a clear, step‑by‑step explanation of why the presence of an index along the compact direction changes the sector, and how the splitting of spinor bundles explains the fermionic case.

---

## 2.  Detailed solution  

Below we work in the RNS formulation of the superstring.  The same logic applies to any supersymmetric theory that is reduced on a circle.

### 2.1  Geometry of the compactification

Take the ten‑dimensional spacetime to be  

\[
\mathcal{M}_{10}= \mathcal{M}_{9}\times S^{1}_{R},
\qquad
y\sim y+2\pi R .
\]

The Lorentz group factorises as  

\[
SO(1,9)\;\longrightarrow\;SO(1,8)\times SO(1)
\]

and any tensor (or spinor) of \(SO(1,9)\) can be decomposed into representations of the 9‑d Lorentz group together with representations of the “internal’’ group \(SO(1)\) (the rotation group of a line).  For a line the only non‑trivial representation is the **sign** representation, i.e. a field can be **periodic** or **anti‑periodic** when we go once around the circle.

### 2.2  Bosonic fields (NS sector)

The NS sector of the world‑sheet contains the spacetime bosons:
the metric \(G_{MN}\), the Kalb‑Ramond 2‑form \(B_{MN}\) and the dilaton \(\Phi\).  
All of them are *periodic* on the world‑sheet, so in spacetime they are ordinary (periodic) fields on \(S^{1}\).  

When we expand a generic ten‑dimensional bosonic field \(\Phi(x^{\mu},y)\) in Kaluza–Klein (KK) modes we write  

\[
\Phi(x^{\mu},y)=\sum_{n\in\mathbb Z}
\phi_{n}(x^{\mu})\,e^{i n y/R}\; .
\tag{2.1}
\]

Because the field is periodic in \(y\) we only get **integer** Fourier modes \(n\in\mathbb Z\).  The zero mode \(n=0\) is a genuine nine‑dimensional field; the non‑zero modes are massive excitations with mass \(|n|/R\).

Now split the 10‑d index \(M\) as \((\mu,9)\) where \(\mu=0,\dots ,8\) runs over \(\mathcal{M}_{9}\) and \(9\) denotes the circle direction.  Two kinds of components appear:

| Component | 9‑d interpretation | KK expansion |
|-----------|--------------------|--------------|
| \(G_{\mu\nu}, B_{\mu\nu}\) (no 9‑index) | 9‑d tensors (graviton, 2‑form) | (2.1) with integer \(n\) – **NS** |
| \(G_{\mu 9}, B_{\mu 9}\) (one 9‑index) | 9‑d vectors | also (2.1) with integer \(n\).  **Why do they look like R?** |

The key point is that a vector component **along the circle** carries one unit of charge under the internal \(U(1)\) isometry (the momentum around the circle).  Under a shift \(y\to y+2\pi R\) the component picks up a factor  

\[
G_{\mu 9}(x,y+2\pi R)= G_{\mu 9}(x,y)\;,
\]

so the field itself is still periodic.  However, from the **world‑sheet point of view** the internal index behaves like a world‑sheet fermion with *different* moding, as we now explain.

### 2.3  World‑sheet fermions and the NS/R sectors

In the RNS formalism the ten spacetime coordinates are accompanied by ten world‑sheet fermions \(\psi^{M}(\sigma,\tau)\) (left‑moving) and \(\tilde\psi^{M}\) (right‑moving).  Their mode expansions depend on the spin structure on the world‑sheet circle \(\sigma\sim\sigma+2\pi\):

| Sector | Boundary condition on \(\psi^{M}\) | Mode expansion |
|--------|-----------------------------------|----------------|
| NS (Neveu–Schwarz) | **anti‑periodic** \(\psi^{M}(\sigma+2\pi)=-\psi^{M}(\sigma)\) | \(\displaystyle \psi^{M}(\sigma)=\sum_{r\in\mathbb Z+1/2}\psi^{M}_{r}e^{-ir\sigma}\) |
| R (Ramond) | **periodic** \(\psi^{M}(\sigma+2\pi)=+\psi^{M}(\sigma)\) | \(\displaystyle \psi^{M}(\sigma)=\sum_{n\in\mathbb Z}\psi^{M}_{n}e^{-in\sigma}\) |

Thus the **moding** (half‑integer vs. integer) is the distinguishing feature of the two sectors.

When we compactify one spacetime direction on a circle we also have to specify **how the world‑sheet fermions transform under translations in the internal direction**.  The ten‑dimensional fields are functions of \(y\).  A Fourier mode \(e^{i n y/R}\) carries momentum \(p_{9}=n/R\).  Because the world‑sheet fermion carries a *spin* index, parallel transport around the internal circle multiplies it by a factor \((-1)^{n}\).  Concretely,

\[
\psi^{9}(\sigma,\tau, y+2\pi R) = (-1)^{n}\,\psi^{9}(\sigma,\tau, y),
\qquad
n \;\text{the KK number of the mode}.
\tag{2.2}
\]

- **If \(n\) is even** (\(n\in 2\mathbb Z\)), the sign is \(+1\); the field is **periodic** on the world‑sheet and belongs to the **R** sector.  
- **If \(n\) is odd** (\(n\in 2\mathbb Z+1\)), the sign is \(-1\); the field is **anti‑periodic** and belongs to the **NS** sector.

For a *pure* NS field (no internal index) the Fourier modes are always integer, so (2.2) never flips the sign: all KK excitations stay in the NS sector.

For a field **with one index along the circle**, the factor \((-1)^{n}\) appears because the internal index transforms as a vector under the little group \(SO(1)\) of the circle.  Consequently the **overall boundary condition** for the world‑sheet fermion associated with that component becomes **periodic** (R) for *even* KK number and **anti‑periodic** (NS) for *odd* KK number.  In other words, the *sector* of the mode is shifted by **one unit of KK momentum**.

Since the lowest non‑zero KK momentum is \(n=\pm 1\), the *first* massive mode of a component with a circle index lands in the **R** sector, exactly what the empirical rule states.

### 2.4  Spinor bundle viewpoint (fermions)

The above story can be rephrased geometrically in terms of spin bundles.  
For a product manifold \(M^{9}\times S^{1}\) the spin bundle factorises as  

\[
S\bigl(M^{9}\times S^{1}\bigr)= S(M^{9})\;\otimes\; S(S^{1}) .
\tag{2.3}
\]

- \(S(M^{9})\) is the ordinary 9‑d spinor bundle.  
- \(S(S^{1})\) is a *two‑dimensional* bundle whose fibre consists of the two possible spin structures on the circle: **periodic** (Ramond) and **anti‑periodic** (Neveu–Schwarz).  

A ten‑dimensional Majorana–Weyl spinor \(\Psi(x,y)\) can therefore be

*Original question: [Compactifying on a circle and the exchange of R and NS sectors](https://physics.stackexchange.com/questions/57487/compactifying-on-a-circle-and-the-exchange-of-r-and-ns-sectors) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
