---
layout: question
title: Geometric statistics and its link to statisticians working outside it
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Geometric statistics and its link
  to statisticians working outside it'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. Restatement of the Question (Plain Language)

The author works on **statistics for data that live on curved spaces** (Riemannian manifolds, stratified spaces, etc.).  
They would like to know:

* **When does the geometry of the sample space actually change the statistical conclusions?**  
* In other words, can we point to concrete situations where curvature, topology, or singularities *materially* affect things such as confidence intervals, hypothesis tests, or estimators – not just change the formulas in a cosmetic way?  

The answer should give **specific examples** (both asymptotic and finite‑sample) that illustrate the impact of geometry, and explain why these effects matter to practitioners who normally work in Euclidean settings.

---

## 2. Step‑by‑Step Explanation  

Below we walk through the main ways geometry can influence statistical inference, illustrated with concrete models and references.  
Each point is presented as a logical “step” that builds on the previous one.

---

### Step 1 – Define the Fréchet Mean and Its Euclidean Counterpart  

* **Euclidean case**: For i.i.d. points \(X_1,\dots ,X_n\in\mathbb R^d\) with mean \(\mu\), the sample mean \(\bar X\) minimises the squared Euclidean distance  
  \[
  \bar X = \arg\min_{p\in\mathbb R^d}\frac1n\sum_{i=1}^n\|X_i-p\|^2 .
  \]

* **Manifold / metric‑space case**: With a metric \(d(\cdot,\cdot)\) on a space \(\mathcal M\), the (population) Fréchet mean(s) are the minimisers of the Fréchet functional  
  \[
  F(p)=\mathbb E\big[ d^2(X,p) \big] .
  \]
  The *sample* Fréchet mean \(\hat\mu_n\) minimises the empirical version \(F_n(p)=\frac1n\sum_{i=1}^n d^2(X_i,p)\).

If \(\mathcal M=\mathbb R^d\) with the Euclidean metric, both definitions coincide, and the familiar properties of the ordinary mean follow.

---

### Step 2 – Asymptotic Distribution: The Role of the Hessian  

On a smooth Riemannian manifold \((\mathcal M,g)\) with unique Fréchet mean \(\mu\),

\[
\sqrt{n}\,\log_\mu(\hat\mu_n) \;\xrightarrow{d}\; \mathcal N\!\bigl(0,\; \Sigma\bigr),
\qquad
\Sigma = H^{-1} \, \Gamma \, H^{-1},
\]

where  

* \(\log_\mu\) is the Riemannian log map (tangent‑space coordinate).  
* \(H = \nabla^2 F(\mu)\) is the **Hessian** (the matrix of second derivatives of the Fréchet function at \(\mu\)).  
* \(\Gamma = \operatorname{Cov}\bigl(\operatorname{grad} d^2(X,\mu)\bigr)\) is the covariance of the Riemannian gradients.

**Why geometry matters:**  

* In \(\mathbb R^d\), \(H = 2I_d\) (the identity) and \(\Sigma = \frac14 \Gamma\); the limiting covariance depends only on the data distribution.  
* On a curved space, \(H\) contains curvature information (e.g., sectional curvature appears in the second‑order expansion of squared distance).  
* If curvature makes \(H\) **singular** (e.g., at cut‑locus points or on manifolds with non‑positive curvature), the limiting covariance can blow up or collapse in certain directions, changing the shape of confidence ellipsoids.

**Concrete illustration** – *Spherical data*:  

* Let \(X_i\) be i.i.d. on the unit sphere \(S^{k}\) with a von Mises–Fisher distribution \(\mathrm{vMF}(\mu,\kappa)\).  
* The Fréchet mean is \(\mu\).  
* The Hessian \(H = \kappa \, (I - \mu\mu^{\!\top})\) has eigenvalue \(\kappa\) in the tangent space; as \(\kappa\to 0\) (the uniform distribution) the Hessian tends to **zero**, making the CLT variance diverge.  
* This explains why inference near the *uniform* distribution on a sphere is dramatically less precise than in Euclidean space with the same concentration parameter.

---

### Step 3 – **Stickiness** on Stratified / Singular Spaces  

A *stratified space* is a union of manifolds glued together along lower‑dimensional pieces (e.g., a tree space, a space of phylogenetic trees, or the space of symmetric positive‑definite matrices with rank constraints).

**Phenomenon:**  
When the population Fréchet mean lies on a lower‑dimensional stratum, the *sample* Fréchet means eventually **stick** to that stratum with probability 1, even if the data are perturbed off it.

**Why it is a statistical effect:**  

* The usual Euclidean intuition that the sample mean can wander arbitrarily close to any point in the convex hull fails.  
* Confidence regions built assuming a full‑dimensional Gaussian limit are **wrong**: the true limiting distribution lives on a lower‑dimensional linear subspace (often a mixture of a Gaussian on the stratum and a point mass).  

**Example – BHV Tree Space:**  

* The Billera–Holmes–Vogtmann (BHV) space of phylogenetic trees is a CAT(0) space consisting of orthants glued along faces.  
* If the true tree is a *star tree* (all leaf edges of length zero), the population Fréchet mean lies at the **cone point**, a singularity of codimension \(>0\).  
* Empirically, the sample Fréchet means converge to a point on the cone, *sticking* there after finitely many samples (see Hotz et al., 2013; Barden et al., 2016).  
* Consequently, a Wald test that ignores stickiness will have inflated Type I error.

---

### Step 4 – **Finite‑Sample Smeariness** (Curvature‑Dependent Bias & Variance)

Even when the limiting CLT looks Euclidean, curvature can cause *finite‑sample* deviations that are not negligible for realistic \(n\).

**Mechanism:**  

* The squared‑distance function on a positively curved manifold is **convex only up to the injectivity radius**.  
* For samples that occasionally fall outside that radius, the empirical Fréchet function becomes *flattened*, biasing the minimiser toward the centre of curvature.

**Quantitative result on the sphere \(S^{k}\):**  

* Let \(X_i\) be i.i.d. from a von Mises–Fisher distribution with concentration \(\kappa\).  
* For moderate \(n\) (e.g., \(n=30\)), the bias of \(\hat\mu_n\) is approximately  
  \[
  \operatorname{Bias}\bigl(\hat\mu_n\bigr) \;\approx\; \frac{c(k)}{\kappa\, n}\,\mu,
  \]
  where \(c(k)=\frac{k-1}{2}\).  
* The variance inflation factor is \(1 + \frac{c(k)}{\kappa^2 n}\).  
* Both corrections depend on curvature through the factor \(c(k)\) (which is zero in Euclidean space).

**Practical implication:**  

* Wald‑type confidence regions that use the Euclidean variance underestimate the true variability unless they are *re‑calibrated* by a curvature‑dependent factor (e.g., the “curvature correction” of Bhattacharya & Patrangenaru, 2005).  
* In neuroimaging, diffusion‑tensor imaging (DTI) data are SPD matrices; ignoring the manifold’s curvature leads to under‑coverage of confidence ellipsoids for mean tensors.

---

### Step 5 – Impact on **Regression**, **KDE**, and **Hypothesis Testing**

| Method | Euclidean formulation | Geometric modification | Statistical effect |
|--------|----------------------|------------------------|--------------------|
| **Geodesic regression** (Müller & others) | Linear model \(Y = \beta_0 + \beta_1 X + \varepsilon\) | Replace straight lines by geodesics; parameters live in the tangent space at a base point; the exponential map is used to map back. | Curvature causes *bias* in slope estimates; asymptotic covariance contains the Riemannian curvature tensor. |
| **Kernel density estimation (KDE)** on \(\mathcal M\) | \( \hat f(x)=\frac{1}{nh^d}\sum K\bigl(\|x-X_i\|/h\bigr)\) | Use the geodesic distance and the volume element \(\sqrt{\det g}\). | Bandwidth selection depends on Ricci curvature; in high curvature regions the effective bandwidth is larger, leading to oversmoothing if Euclidean bandwidth is used. |
| **Two‑sample test** for equality of means | \(T = n\|\bar X_1-\bar X_2\|^2 / \hat\sigma^2\) | Replace Euclidean norm by Riemannian distance, and use Hessian‑adjusted covariance. | Critical values change; ignoring curvature inflates Type I error (demonstrated for SPD matrices in Lenglet et al., 2020). |

Thus geometry permeates *every* standard statistical tool when the data live off \(\mathbb R^d\).

---

### Step 6 – Summary of When Geometry Is **Material**

| Situation | Geometry‑induced statistical effect | Typical magnitude |
|-----------|--------------------------------------|--------------------|
| **Unique smooth mean, moderate curvature** | Hessian scaling of asymptotic variance; bias of order \(1/n\) | Often noticeable for \(n\lesssim 100\) (e.g., directional data on \(S^2\)) |
| **Mean at or near cut‑locus / singularity** | Singular Hessian → inflated variance or degenerate limit; *stickiness* | Can dominate even for large \(n\) (tree space star‑tree case) |
| **High curvature (small injectivity radius)** | Finite‑sample smeariness (bias + variance inflation) | Requires explicit curvature correction; under‑coverage up to 20 % if ignored |
| **Manifold with boundary or stratification** | Sample means may lie on lower‑dimensional strata → reduced effective dimension | Affects hypothesis tests and confidence sets; leads to *non‑Gaussian* limiting distributions |
| **Non‑Euclidean group actions (e.g., rotations)** | Quotient spaces produce orbifold singularities → multimodal Fréchet functions | Can cause spurious multiple local minima; bootstrap may fail |

Whenever any of the above rows applies, the geometry is **material**: it changes the *shape* of confidence regions, the *power* of tests, or even the *consistency* of estimators.

---

## 3. Final Answer (Key Take‑aways)

* **Geometry matters** whenever the Fréchet (or intrinsic) mean is influenced by curvature or singularities.  
* The **Hessian of the Fréchet function** incorporates curvature; a non‑identity Hessian rescales the asymptotic covariance and can become singular, leading to *degenerate* CLTs.  
* **Stickiness** on stratified spaces forces sample means onto lower‑dimensional strata, producing non‑Gaussian limits and invalidating Euclidean Wald tests.  
* **Finite‑sample smeariness** shows that curvature can cause noticeable bias and variance inflation for realistic sample sizes; curvature‑dependent recalibration of Wald‑type procedures is essential.  
* These phenomena appear in concrete applied domains: directional statistics, diffusion‑tensor imaging (SPD matrices), shape analysis, phylogenetic tree spaces, and more.  
* Practitioners outside the “geometric statistics” community need to adjust standard tools (regression, KDE, two‑sample tests) whenever data live on manifolds with non‑trivial curvature or singularities; otherwise inference can be misleading.

---

## 4. Common Mistakes When Dealing With Geometry‑Based Inference  

| Mistake | Why It Happens | How to Avoid It |
|---------|----------------|-----------------|
| **Treating the Fréchet mean as if it were the Euclidean mean** (ignoring the Hessian). | The definition looks similar; the extra curvature term is easy to overlook. | Explicitly compute or approximate the Hessian \(H = \nabla^2F(\mu)\) and use \(H^{-1}\Gamma H^{-1}\) for the asymptotic variance. |
| **Assuming a normal limit in all cases** (using standard Wald tests). | The CLT formula is often quoted without its regularity

*Original question: [Geometric statistics and its link to statisticians working outside it](https://stats.stackexchange.com/questions/677254/geometric-statistics-and-its-link-to-statisticians-working-outside-it) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
