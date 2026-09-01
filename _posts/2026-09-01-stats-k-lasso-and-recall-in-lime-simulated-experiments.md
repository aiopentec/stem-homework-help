---
layout: question
title: K-LASSO and Recall in LIME (simulated experiments)
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: K-LASSO and Recall in LIME (simulated
  experiments)'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the student is really asking  

The student wants to understand the **“K‑LASSO”** step that appears in the LIME algorithm (Algorithm 1 of the “Why Should I Trust You?” paper).  
Specifically they are asking:

1. **What does K‑LASSO do?** – Does it simply give a sparse model by setting some coefficients to zero and then keep the non‑zero features?  
2. **How does it fit into the overall LIME optimisation**  

   \[
   \xi(x)=\arg\min_{g\in G} \; L\bigl(f,g,\pi_x\bigr)+\Omega(g) \; ?
   \]

   In particular:  
   * Is the loss \(L\) the same loss that LASSO minimises?  
   * How does the weighting \(\pi_x(z)\) (the proximity kernel) interact with the LASSO step?  

The student also wants a concise, step‑by‑step “worked‑out” explanation that ties together the regularisation path, the selection of exactly \(K\) features, and the final ordinary‑least‑squares (OLS) fitting that the paper calls *K‑LASSO*.

---

## 2. Step‑by‑step explanation  

Below we break the whole procedure into **four logical pieces** and show how they connect.

### 2.1 The overall LIME optimisation

LIME explains the prediction of a black‑box classifier \(f\) at a particular instance \(x\) by fitting a *simple* (interpretable) model \(g\) to data that are **locally perturbed** around \(x\).

\[
\boxed{\xi(x)=\arg\min_{g\in G}\; L\bigl(f,g,\pi_x\bigr)+\Omega(g)}
\]

* **\(G\)** – the family of interpretable models (in the paper: linear models on a binary bag‑of‑words representation).  
* **\(L\bigl(f,g,\pi_x\bigr)\)** – a **locally weighted squared loss** that measures how well \(g\) mimics \(f\) on the perturbed samples.  
* **\(\pi_x(z)\)** – a kernel (typically an exponential kernel) that gives higher weight to samples \(z\) that are *closer* to the original instance \(x\).  
* **\(\Omega(g)\)** – a complexity penalty (e.g., the number of non‑zero coefficients) that forces the explanation to stay simple.

Because the family \(G\) is linear, we can write a perturbed sample as a binary vector \(\mathbf{z}\in\{0,1\}^p\) (presence/absence of each word). The linear explanation model is  

\[
g(\mathbf{z}) = \beta_0 + \sum_{j=1}^{p}\beta_j z_j .
\]

Plugging this into the loss gives a **weighted least‑squares problem**:

\[
\min_{\beta_0,\beta}\; \sum_{i=1}^{N}\pi_x(\mathbf{z}^{(i)})\Bigl(f(\mathbf{z}^{(i)})- \beta_0-\beta^{\top}\mathbf{z}^{(i)}\Bigr)^2 \;+\; \Omega(\beta).
\]

If we **ignore** \(\Omega(\beta)\) we simply have ordinary weighted least squares (WLS).  
If we **add** a sparsity‑inducing penalty (e.g., \(\lambda\|\beta\|_1\)) we obtain the classic **LASSO** objective, but now with **sample weights** \(\pi_x(\mathbf{z}^{(i)})\).

Thus **LASSO can absolutely be performed with the same loss** used by LIME – we just attach the kernel weights to each observation.

---

### 2.2 Why a *regularisation path*?

Standard LASSO solves

\[
\min_{\beta}\; \underbrace{\sum_{i}\pi_i\bigl(y_i-\beta^{\top}\mathbf{z}_i\bigr)^2}_{\text{weighted SSE}} \;+\; \lambda\|\beta\|_1 .
\]

The solution depends on the regularisation parameter \(\lambda\).  
- Large \(\lambda\) → most coefficients forced to zero (very sparse).  
- Small \(\lambda\) → many coefficients survive (dense).

A **regularisation path** (Efron et al., 2004 – “Least Angle Regression”) computes the whole set of solutions for **all possible values of \(\lambda\)** in a single, efficient pass.  

The path gives us a **ranking of features**: the first feature to enter the model is the one that reduces the loss the most, the second is the next best, and so on.  

Because we want **exactly \(K\) features** in the explanation (the paper’s “\(K\)-LASSO”), we simply walk **down the path** until we have \(K\) non‑zero coefficients. That choice of \(\lambda\) is *not* pre‑specified; it is *implicitly* chosen so that \(|\{j:\beta_j\neq0\}| = K\).

---

### 2.3 Algorithmic definition of **K‑LASSO** (Algorithm 1 in the paper)

| Step | What is done | Why it matters |
|------|--------------|----------------|
| **1. Sample** | Generate \(N\) perturbed binary vectors \(\mathbf{z}^{(i)}\) from the original instance \(x\). Compute the black‑box predictions \(y_i = f(\mathbf{z}^{(i)})\). | Provides the data on which the local surrogate will be fitted. |
| **2. Weight** | Compute kernel weights \(\pi_i = \pi_x(\mathbf{z}^{(i)})\) (larger for points close to \(x\)). | Enforces *locality*: far points influence the fit only weakly. |
| **3. Run LASSO path** | Run a weighted LASSO (weights \(\pi_i\)) on the design matrix \(\mathbf{Z}\) and response \(\mathbf{y}\). Record the order in which variables become non‑zero. | Gives a *global* ordering of features by importance under the weighted loss. |
| **4. Pick top‑\(K\)** | Stop the path when exactly \(K\) variables have entered the model. Keep only those columns of \(\mathbf{Z}\). | Guarantees the explanation has the prescribed complexity (exactly \(K\) words). |
| **5. Refine coefficients** | Fit an **unregularised weighted least‑squares** (OLS) using only the selected \(K\) columns, again with weights \(\pi_i\). | The LASSO penalty shrinks coefficients; refitting without the \(\ell_1\) term gives unbiased estimates for the chosen features. |
| **6. Return** | The final \(\beta\) (intercept + \(K\) non‑zero coefficients) constitute the local linear explanation \(g\). | This \(g\) is what LIME reports as the explanation for \(x\). |

Notice the **two‑stage nature**:

1. **Stage A (feature selection)** – weighted LASSO + path → *which* \(K\) words to keep.  
2. **Stage B (coefficient estimation)** – ordinary weighted LS on the reduced set → *how much* each kept word contributed.

That is exactly what the authors call **“K‑LASSO”**.

---

### 2.4 Answering the student’s specific questions  

| Question | Answer (with justification) |
|----------|------------------------------|
| **(a) “Is my overall idea correct?”** | Yes, *in principle* – K‑LASSO selects a **subset of features** (the non‑zero coefficients) and then fits a **sparse linear model** on those features. The nuance is that the selection is **driven by a weighted LASSO path**, not by a single LASSO run with a pre‑chosen \(\lambda\). |
| **(b) “Can LASSO be performed with the LIME loss \(\;L(f,g,\pi_x)\)?”** | Absolutely. The loss used by LIME is a **weighted sum of squared errors**. Adding an \(\ell_1\) penalty to that loss gives the exact optimisation solved by (weighted) LASSO. The kernel \(\pi_x(z)\) simply acts as observation‑wise weights. |
| **(c) “What about the two optimisations?”** | There is **one optimisation** (the weighted LASSO) that yields a **path** of solutions. The “second optimisation” in the algorithm is a **refit**: once we have fixed the set of \(K\) features, we drop the \(\ell_1\) penalty and solve ordinary weighted LS to obtain the final coefficients. This refit is **not** a new selection step; it just improves coefficient estimates. |
| **(d) “Why not just use the LASSO coefficients directly?”** | LASSO’s \(\ell_1\) penalty **shrinks** all coefficients toward zero, which can bias the magnitude of the explanation weights. By refitting with OLS on the selected features we obtain **unbiased** weights while keeping the sparsity enforced by the first stage. |

---

### 2.5 Putting it all together – a concise mathematical description  

Given  

* perturbed binary matrix \(\mathbf{Z}\in\{0,1\}^{N\times p}\) (rows = samples, columns = words),  
* black‑box outputs \(\mathbf{y}\in\mathbb{R}^N\),  
* kernel weights \(\mathbf{w}\in\mathbb{R}^N_{+}\) where \(w_i = \pi_x(\mathbf{z}^{(i)})\),

**Stage A (K‑LASSO feature selection)**  

\[
\begin{aligned}
\text{Find } & \lambda^{*}\text{ such that } |\{j:\beta_j(\lambda^{*})\neq0\}| = K,\\
\text{where } &\beta(\lambda) = \arg\min_{\beta}\;
\underbrace{\sum_{i=1}^{N} w_i\bigl(y_i - \beta_0 - \beta^{\top}\mathbf{z}_i\bigr)^2}_{\text{weighted SSE}}
\;+\; \lambda\|\beta\|_1 .
\end{aligned}
\]

The solution \(\beta(\lambda^{*})\) tells us **which \(K\) columns** of \(\mathbf{Z}\) are retained.

**Stage B (Refit OLS on the chosen columns)**  

Let \(\mathbf{Z}_{(K)}\) be the sub‑matrix containing only the selected \(K\) columns. Solve  

\[
\hat{\beta}_{(K)} = \arg\min_{\beta_0,\beta_{(K)}}\; \sum_{i=1}^{N} w_i\bigl(y_i - \beta_0 - \beta_{(K)}^{\top}\mathbf{z}_{i,(K)}\bigr)^2 .
\]

The pair \((\beta_0,\hat{\beta}_{(K)})\) defines the **local linear explanation** \(g\) reported by LIME.

---

## 3. Final answer (concise)

* **K‑LASSO** is **not a new algorithm**; it is the **two‑step procedure** used by LIME to obtain a **\(K\)-feature sparse linear explanation**:

  1. **Weighted LASSO path** (loss = locally weighted squared error, penalty = \(\ell_1\)) is run on the perturbed data.  
  2. The path is stopped when exactly **\(K\)** coefficients are non‑zero – these are the **selected features**.  
  3. An **unregularised weighted least‑squares** fit on those \(K\) features provides the final, unbiased coefficient values.

* The loss \(L\) that appears in the LIME optimisation **is the same loss** used inside the LASSO; the kernel \(\pi_x(z)\) simply supplies observation‑wise weights.

* The “two optimisations” you see are (i) *selection* (weighted LASSO) and (ii) *refitting* (ordinary weighted LS). They are sequential, not competing.

* The resulting explanation model \(g\) therefore **recovers the same set of input words** that the original interpretable model would use (if the original model is truly linear), enabling the authors to compute a *recall* score that measures how often LIME’s top‑\(K\) words match the true important words.

---

## 4. Common mistakes when interpreting K‑LASSO / LIME  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing the LASSO penalty with the “complexity term” \(\Omega(g)\).** | \(\Omega(g)\) in the paper is a *hard* constraint (e.g., “use at most \(K\) features”), whereas LASSO’s \(\lambda\|\beta\|_1\) is a *soft* penalty. LIME implements the hard constraint by **stopping the LASSO path** at \(K\) non‑zeros, then discarding the penalty. | Remember: the

*Original question: [K-LASSO and Recall in LIME (simulated experiments)](https://stats.stackexchange.com/questions/677035/k-lasso-and-recall-in-lime-simulated-experiments) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
