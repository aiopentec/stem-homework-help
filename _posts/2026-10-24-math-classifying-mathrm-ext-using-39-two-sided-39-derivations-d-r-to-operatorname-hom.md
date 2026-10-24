---
layout: question
title: Classifying $\mathrm{Ext}$ using &#39;two-sided&#39; derivations $D:R\to\operatorname{Hom}(N,M)$
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Classifying $\mathrm{Ext}$ using
  &#39;two-sided&#39; derivations $D:R\to\operatorname{Hom}(N,M)$'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

### 1. Restatement in Plain Language

The student is investigating a concrete way to describe elements of the extension group $\mathrm{Ext}_R^1(N, M)$ for a commutative $k$-algebra $R$ and $R$-modules $M$ and $N$. 

Instead of using abstract homological algebra (like projective resolutions or derived functors), they choose a vector space splitting $K \cong M \oplus N$ of the middle module of an extension. By forcing the scalar multiplication by elements of $R$ to be compatible with this splitting, the failure of $K$ to be a direct sum of $R$-modules is captured by a collection of maps $\psi(f): N \to M$ indexed by $f \in R$. 

The student observes that these maps satisfy a Leibniz-type rule:
$$\psi(fg) = f \cdot \psi(g) + \psi(f) \cdot g$$
which looks precisely like the definition of a $k$-linear derivation from $R$ into the bimodule $\operatorname{Hom}_k(N, M)$. 

The goal is to analyze the map $(\ast)$ from the set of such derivations to $\mathrm{Ext}_R^1(N, M)$, determine its properties (such as surjectivity and whether it is a group homomorphism), and connect this explicit construction to standard homological algebra.

---

### 2. Step-by-Step Solution

#### Step 1: Formalizing the Extension and the Splitting
Let $0 \to M \xrightarrow{i} K \xrightarrow{\pi} N \to 0$ be a short exact sequence of $R$-modules. Since $k$ is a field and $M$ is a $k$-vector space, the subspace $i(M) \subseteq K$ has a $k$-linear complement $X \subseteq K$. Thus, as $k$-vector spaces, we have a direct sum decomposition:
$$K = i(M) \oplus X$$
Moreover, the restriction of the quotient map $\pi|_X: X \to N$ is a $k$-vector space isomorphism. Let $c: N \to X$ be the inverse isomorphism ($c = (\pi|_X)^{-1}$). This allows us to identify $K$ as a $k$-vector space with $M \oplus N$ via the isomorphism $\text{id}_M \oplus c^{-1}: K \to M \oplus N$.

#### Step 2: The Action of $R$ on $K$
Because $K$ is an $R$-module, every element $f \in R$ induces an $R$-linear endomorphism $f^K_\ast: K \to K$, which satisfies:
1. $f^K_\ast(i(m)) = i(f \cdot m)$ for all $m \in M$ (since $i$ is $R$-linear).
2. $\pi(f^K_\ast(x)) = f \cdot \pi(x)$ for all $x \in X$ (since $\pi$ is $R$-linear).

In terms of the matrix representation with respect to the decomposition $K = M \oplus X$, an arbitrary $k$-linear endomorphism of $M \oplus X$ has the block form:
$$\begin{pmatrix} A & \xi \\ \beta & D \end{pmatrix}: M \oplus X \to M \oplus X$$
- Condition 1 implies $A = f^M_\ast$ and $\beta = 0$.
- Condition 2 implies $D = c^{-1} \circ f^N_\ast \circ c$.

Thus, the action of $f \in R$ on $K$ must look like:
$$f^K_\ast = \begin{pmatrix} f^M_\ast & \xi(f) \\ 0 & c^{-1} f^N_\ast c \end{pmatrix}$$
where $\xi(f): X \to M$ is a $k$-linear map. Defining $\psi(f) = \xi(f) \circ c^{-1}: N \to M$, the action of $f$ on $M \oplus N$ takes the form:
$$f^K_\ast = \begin{pmatrix} f^M_\ast & \psi(f) \\ 0 & f^N_\ast \end{pmatrix}$$

#### Step 3: Deriving the Cocycle Condition
Multiplication in $R$ must be respected, meaning $(fg)^K_\ast = f^K_\ast \circ g^K_\ast$ for all $f, g \in R$, and $1^K_\ast = \text{id}_K$. 

Using matrix multiplication:
$$\begin{pmatrix} f^M_\ast & \psi(f) \\ 0 & f^N_\ast \end{pmatrix} \begin{pmatrix} g^M_\ast & \psi(g) \\ 0 & g^N_\ast \end{pmatrix} = \begin{pmatrix} f^M_\ast g^M_\ast & f^M_\ast \psi(g) + \psi(f) g^N_\ast \\ 0 & f^N_\ast g^N_\ast \end{pmatrix}$$

Equating this to the matrix for $(fg)^K_\ast$, we obtain the functional equation:
$$\psi(fg) = f^M_\ast \circ \psi(g) + \psi(f) \circ g^N_\ast \quad \text{for all } f, g \in R$$
Additionally, if $f = \lambda \in k$ (scalar multiplication), then $\lambda^M_\ast = \lambda \cdot \text{id}_M$ and $\lambda^N_\ast = \lambda \cdot \text{id}_N$. The equation becomes $\psi(\lambda g) = \lambda \psi(g)$, which implies $\psi(\lambda) = 0$ for all $\lambda \in k$ (assuming a normalized derivation, or more precisely, $\psi(1) = 0$ forces $\psi(\lambda) = 0$ for constant scalars).

#### Step 4: Connecting to Derivations and $\mathrm{Ext}_R^1$
The space $\operatorname{Hom}_k(N, M)$ has a natural $R$-bimodule structure given by:
$$(f \cdot \phi \cdot g)(n) = f \cdot \phi(g \cdot n)$$
The relation derived in Step 3:
$$\psi(fg) = f \cdot \psi(g) + \psi(f) \cdot g$$
is precisely the definition of a $k$-linear derivation $D: R \to \operatorname{Hom}_k(N, M)$. 

Let $\mathcal{Der}_k(R, \operatorname{Hom}_k(N, M))$ denote the space of such derivations. 
- **Surjectivity:** Every extension $0 \to M \to K \to N \to 0$ gives rise to a splitting and thus a derivation $\psi$. This proves the map $(\ast)$ is **surjective**.
- **Is it an isomorphism?** Not quite. The choice of the $k$-linear splitting $X \subset K$ is **not unique**. If we choose a different splitting, the resulting derivation changes by a "principal" derivation (an inner derivation of the form $f \mapsto f \cdot \theta - \theta \cdot f$ for some $k$-linear map $\theta: N \to M$). 
- Specifically, the quotient of $\mathcal{Der}_k(R, \operatorname{Hom}_k(N, M))$ by the subspace of trivial/inner derivations yields precisely $\operatorname{Ext}_R^1(N, M)$ (often computed via Hochschild cohomology or general derived functor isomorphisms like $\operatorname{Ext}_R^1(N,M) \cong H^1(\mathbb{L}_{R/k}, \operatorname{Hom}(N,M))$).

---

### 3. Final Answer

The map $(\ast)$ 
$$\mathcal{Der}_k(R, \operatorname{Hom}_k(N, M)) \longrightarrow \mathrm{Ext}_R^1(N, M)$$ 
is a **surjective set-map**. 

To make it precise:
1. The left-hand side consists of $k$-linear derivations from $R$ into the $R$-bimodule $\operatorname{Hom}_k(N, M)$.
2. The map is constructed by choosing a $k$-linear splitting of the extension, which explicitly extracts the failure of $R$-linearity into a derivation satisfying $\psi(fg) = f\psi(g) + \psi(f)g$ and $\psi(\lambda) = 0$ for $\lambda \in k$.
3. The fibers of this map correspond to different choices of $k$-linear splittings. Factoring out by the equivalence relation corresponding to changing the splitting (inner derivations) upgrades this to an isomorphism with $\operatorname{Ext}_R^1(N,M)$.

---

### 4. Common Mistakes

* **Confusing $R$-linearity with $k$-linearity:** Assuming the splitting $X \subset K$ is an $R$-module splitting. If it were an $R$-module splitting, the extension would be split trivial, $\psi$ would be identically zero, and the sequence would split. The entire point of $\psi$ is that the splitting is *only* $k$-linear.
* **Incorrect Bimodule Action:** Forgetting how $R$ acts on $\operatorname{Hom}_k(N, M)$ on both the left and the right. The term $f^M_\ast \circ \psi(g)$ acts on the left of the codomain $M$, while $\psi(f) \circ g^N_\ast$ acts on the right via the domain $N$.
* **Assuming Injectivity:** Treating $(\ast)$ as a bijection without quotienting. Because the vector space complement $X \subset K$ is non-canonical, different choices of $X$ produce different derivations that represent the *same* isomorphism class in $\mathrm{Ext}_R^1(N, M)$.

*Original question: [Classifying $\mathrm{Ext}$ using &#39;two-sided&#39; derivations $D:R\to\operatorname{Hom}(N,M)$](https://math.stackexchange.com/questions/5152746/classifying-mathrmext-using-two-sided-derivations-dr-to-operatornameho) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
