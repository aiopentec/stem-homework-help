---
layout: post
title: Penalized spline confidence intervals based on cluster-sandwich VCV
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the student is asking (in plain language)

The student fits a **penalised‑spline (P‑spline) model**

\[
\hat{\mathbf y}= \mathbf X\bigl(\mathbf X^{\!\top}\mathbf X+\lambda \mathbf D\bigr)^{-1}\mathbf X^{\!\top}\mathbf y
\]

where  

* **\(\mathbf X\)** contains the original covariates **and** the spline basis functions (the “knots”),  
* **\(\lambda\)** controls the amount of smoothing, and  
* **\(\mathbf D\)** is the penalty matrix (usually a difference operator on the spline coefficients).

The data are observed in **clusters** (e.g. individuals, schools, firms).  
* Within a cluster the errors may be autocorrelated and heteroskedastic,  
* Between clusters the errors are independent.

The student knows how to obtain a **cluster‑robust (sandwich) covariance matrix** for the *parameter vector*  

\[
\hat{\boldsymbol\beta}= (\mathbf X^{\!\top}\mathbf X+\lambda\mathbf D)^{-1}\mathbf X^{\!\top}\mathbf y ,
\]

but they also need **confidence bands for the fitted smooths** (the curves that are plotted).  

The question is therefore:

> *How can one construct pointwise (or simultaneous) confidence intervals for penalised‑spline fits when the error covariance is clustered and possibly heteroskedastic?*  

In addition, the student observed that the covariance matrix supplied by **mgcv** is sometimes singular, and wonders why.

Below is a **step‑by‑step worked solution** that (i) derives the appropriate sandwich variance for the smooth, (ii) shows how to turn it into confidence intervals, (iii) explains the singularity issue, and (iv) gives concrete R code that works with **mgcv** (or any other linear‑smoother).

---

## 2.  Theory – From the linear smoother to a sandwich variance

### 2.1  The penalised‑spline estimator is a **linear smoother**

Define the **smoother (hat) matrix**

\[
\boxed{\;\mathbf S \;=\; \mathbf X\bigl(\mathbf X^{\!\top}\mathbf X+\lambda\mathbf D\bigr)^{-1}\mathbf X^{\!\top}\;}
\]

so that  

\[
\hat{\mathbf y}= \mathbf S\mathbf y .
\]

Because the penalty is *quadratic* and the loss is *least squares*, the estimator is still *linear* in \(\mathbf y\).  

### 2.2  The usual (model‑based) covariance of \(\hat{\mathbf y}\)

If the errors were i.i.d. \(N(0,\sigma^{2})\),

\[
\operatorname{Var}(\hat{\mathbf y}) = \sigma^{2}\mathbf S\mathbf S^{\!\top}.
\]

In **mgcv** the reported covariance of the spline coefficients (or of the smooth) is derived from this expression plus the *prior* implied by the penalty (a Bayesian interpretation).  It **does not** account for clustering or heteroskedasticity.

### 2.3  Cluster‑robust (sandwich) variance

Assume we have \(G\) clusters.  
Let \(\mathbf y_{g}\) be the vector of observations in cluster \(g\) (\(g=1,\dots,G\)), and let \(\mathbf X_{g}\) be the corresponding rows of \(\mathbf X\).  
Define the **residuals**

\[
\hat{\boldsymbol\varepsilon}_{g}= \mathbf y_{g}-\mathbf X_{g}\hat{\boldsymbol\beta}
       =\mathbf y_{g}-\mathbf X_{g}(\mathbf X^{\!\top}\mathbf X+\lambda\mathbf D)^{-1}\mathbf X^{\!\top}\mathbf y .
\]

The **meat** of the sandwich is the sum over clusters of the outer product of the *score* for that cluster:

\[
\boxed{\;
\mathbf M \;=\; \sum_{g=1}^{G}
      \bigl(\mathbf X_{g}^{\!\top}\hat{\boldsymbol\varepsilon}_{g}\bigr)
      \bigl(\mathbf X_{g}^{\!\top}\hat{\boldsymbol\varepsilon}_{g}\bigr)^{\!\top}
   \;}
\]

(If the errors are autocorrelated within a cluster you can replace the outer product by  
\(\mathbf X_{g}^{\!\top}\hat{\boldsymbol\varepsilon}_{g}\hat{\boldsymbol\varepsilon}_{g}^{\!\top}\mathbf X_{g}\), which is the same when the autocorrelation is captured by the residuals themselves.)

The **bread** of the sandwich for penalised splines is the same matrix that appears in the estimator:

\[
\boxed{\;
\mathbf B \;=\; (\mathbf X^{\!\top}\mathbf X+\lambda\mathbf D)^{-1}.
\;}
\]

Putting them together, the **cluster‑robust covariance of the coefficient vector** is

\[
\boxed{\;
\widehat{\operatorname{Var}}(\hat{\boldsymbol\beta})
   \;=\; \mathbf B\; \mathbf M\; \mathbf B^{\!\top}.
\;}
\tag{1}
\]

Because the smoother matrix \(\mathbf S = \mathbf X\mathbf B\mathbf X^{\!\top}\),

\[
\widehat{\operatorname{Var}}(\hat{\mathbf y})
   \;=\; \mathbf X \widehat{\operatorname{Var}}(\hat{\boldsymbol\beta})\mathbf X^{\!\top}
   \;=\; \underbrace{\mathbf S}_{\text{bread}} \;
          \underbrace{\bigl(\sum_{g}\mathbf X_{g}^{\!\top}\hat{\boldsymbol\varepsilon}_{g}
                     \hat{\boldsymbol\varepsilon}_{g}^{\!\top}\mathbf X_{g}\bigr)}_{\text{meat}}
          \; \mathbf S^{\!\top}.
\tag{2}
\]

Equation (2) is the **sandwich variance of the fitted values**.  It is exactly the matrix the student wrote in the question (except that the residuals replace the unknown \(\varepsilon\)s).

### 2.4  Variance of a *single* smooth evaluated at a new point

A smooth \(f(x)\) is usually written as  

\[
f(x) = \mathbf b(x)^{\!\top}\boldsymbol\beta ,
\]

where \(\mathbf b(x)\) is the vector of spline basis functions evaluated at \(x\).  
For a set of evaluation points \(\{x_{1},\dots,x_{m}\}\) let \(\mathbf B_{\!*}\) be the \(m\times p\) matrix whose rows are \(\mathbf b(x_{i})^{\!\top}\).

The **robust variance of the smooth at those points** follows directly from (1):

\[
\boxed{\;
\widehat{\operatorname{Var}}\bigl(\hat f(x_{1}),\dots,\hat f(x_{m})\bigr)
   \;=\; \mathbf B_{\!*}\;
          \bigl(\mathbf B\mathbf M\mathbf B^{\!\top}\bigr)\;
          \mathbf B_{\!*}^{\!\top}.
\;}
\tag{3}
\]

The **pointwise standard error** at \(x_{i}\) is simply the square‑root of the \(i\)‑th diagonal element of the matrix in (3).

### 2.5  From standard errors to confidence intervals

Assuming large‑sample normality (the usual justification for sandwich SEs),

\[
\boxed{\;
\hat f(x_{i}) \;\pm\; z_{1-\alpha/2}\;\sqrt{\widehat{\operatorname{Var}}\bigl(\hat f(x_{i})\bigr)}.
\;}
\tag{4}
\]

Typical choices are \(z_{0.975}=1.96\) for a 95 % interval.  

If one wants **simultaneous (family‑wise) bands**, the multiplier can be replaced by a critical value from the **Bonferroni**, **Scheffé**, or **t‑distribution of the max‑t process** (e.g., using the `simul.confint` routine in `mgcv`).  The same robust covariance matrix (3) is used; only the multiplier changes.

---

## 3.  Step‑by‑step practical recipe (R)

Below is a **complete, reproducible workflow** that uses `mgcv` to fit the spline, then replaces the default covariance with a cluster‑robust sandwich and finally extracts confidence bands for a smooth.

```r
## ------------------------------------------------------------
## 1.  Simulate clustered data (for illustration)
## ------------------------------------------------------------
set.seed(123)

G  <- 30                     # number of clusters
n  <- 15                     # obs per cluster
N  <- G*n                    # total obs

## covariate
x  <- runif(N, 0, 1)

## true smooth (sin curve)
f.true <- function(x) sin(2*pi*x)

## cluster id
clust <- rep(1:G, each=n)

## generate autocorrelated, heteroskedastic errors
rho   <- 0.6                         # AR(1) within cluster
sigma <- rep(1, G) * runif(G, .5, 2) # cluster‑specific sd

eps   <- unlist(lapply(1:G, function(g){
          arima.sim(model=list(ar=rho), n=n)*sigma[g]
        }))

y <- f.true(x) + eps

## ------------------------------------------------------------
## 2.  Fit penalised‑spline with mgcv (default Gaussian, REML)
## ------------------------------------------------------------
library(mgcv)

mod <- gam(y ~ s(x, bs = "ps", k = 15), method = "REML")
summary(mod)               # shows smooth EDF, lambda, etc.

## ------------------------------------------------------------
## 3.  Compute the cluster‑robust sandwich for the spline coeffs
## ------------------------------------------------------------
# 3a. design matrix for the whole model (including intercept)
X   <- model.matrix(mod)                 # N x p
# 3b. penalty matrix (same ordering as X)
#     mgcv stores it as part of the fitted object
D   <- mod$sp[1] * mod$smooth[[1]]$S[[1]]  # λ*D

# 3c. "bread"
B   <- solve(t(X) %*% X + D)             # (X'X+λD)^{-1}

# 3d. residuals per observation
res <- residuals(mod)

# 3e. build the "meat" by summing over clusters
M   <- matrix(0, ncol = ncol(X), nrow = ncol(X))

for (g in unique(clust)) {
  idx   <- which(clust == g)                # rows belonging to cluster g
  Xg    <- X[idx, , drop = FALSE]           # design for cluster g
  eg    <- res[idx]                          # residuals for cluster g
  #   X'g * eg  is a p‑vector; outer product yields p×p matrix
  M     <- M + crossprod( t(Xg) %*% eg )     # = (Xg' eg)(Xg' eg)'
}
# (If you have within‑cluster autocorrelation you could use
#   Xg' %*% (eg %*% t(eg)) %*% Xg  instead.)

# 3f. robust covariance of the coefficient vector
Vbeta_robust <- B %*% M %*% t(B)    # (1)

## ------------------------------------------------------------
## 4.

*Original question: [Penalized spline confidence intervals based on cluster-sandwich VCV](https://stats.stackexchange.com/questions/44798/penalized-spline-confidence-intervals-based-on-cluster-sandwich-vcv) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
