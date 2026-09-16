---
layout: question
title: Reconstructing Underlying state variable from One Observable Data
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Reconstructing Underlying state variable
  from One Observable Data'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## 1.  What is being asked?  

You have measured **only one scalar signal** from a deterministic chaotic system – for example the \(x\)-coordinate of the Lorenz attractor, \(x(t)\).  
From that single time‑series you would like to answer two questions  

1. **Do other state variables exist?** (i.e. is the system really three‑dimensional and not just a one‑dimensional “hidden” oscillator?)  
2. **If they exist, how can we uncover them or at least know how many there are?**

In other words: *given a scalar observable of an unknown dynamical system, how can we determine the minimal number of hidden variables that are required to describe the underlying dynamics?*  

---

## 2.  Step‑by‑step answer  

Below we give a full, self‑contained recipe that a researcher can follow with a measured series \(x(t)\).  
The method rests on **delay‑coordinate embedding** (Takens’ theorem) together with **practical dimension‑estimation tools** (false‑nearest‑neighbors, correlation dimension, Lyapunov exponents, etc.).  
If the minimal embedding dimension you discover is larger than 1, you have proved that **additional hidden state variables are needed**.

---

### Step 0 –  Preparations  

| What you need | Why it matters |
|---------------|----------------|
| A uniformly sampled scalar series \(x_k = x(t_k)\) (preferably long, \(\ge 10^4\) points). | Embedding methods assume a discrete‑time version of the continuous flow. |
| A rough estimate of the dominant time‑scale (e.g. the first zero of the autocorrelation or the first minimum of the mutual information). | This gives a good **delay** \(\tau\). |
| Software for basic nonlinear‑time‑series analysis (MATLAB, Python + NumPy/SciPy, R, TISEAN, …). | All the algorithms are standard and can be called from these packages. |

---

### Step 1 –  Build a delay‑coordinate (Hankel) matrix  

For a chosen delay \(\tau\) and an integer embedding dimension \(d\) form the vectors  

\[
\mathbf{v}_k^{(d)}=\bigl[x_k,\;x_{k+\tau},\;x_{k+2\tau},\dots ,x_{k+(d-1)\tau}\bigr]^T .
\]

Collecting all such vectors for \(k=1,\dots ,N-(d-1)\tau\) gives a **Hankel matrix**  

\[
\mathbf{H}^{(d)}=
\begin{bmatrix}
x_1 & x_{1+\tau} & \dots & x_{1+(d-1)\tau}\\[2pt]
x_2 & x_{2+\tau} & \dots & x_{2+(d-1)\tau}\\
\vdots & \vdots & \ddots & \vdots\\
x_{N-(d-1)\tau} & x_{N-(d-2)\tau} & \dots & x_N
\end{bmatrix}.
\]

Each row of \(\mathbf{H}^{(d)}\) is a point in the **reconstructed phase space** \(\mathbb{R}^{d}\).

> **Note** – The matrix is called “Hankel’’ because each anti‑diagonal contains the same value of the original series.  
> The construction is *non‑linear* in the sense that the *geometry* of the cloud of points can be highly curved even though the matrix itself is linear.

---

### Step 2 –  Choose a suitable delay \(\tau\)

Two popular, data‑driven rules:

1. **Autocorrelation method** – pick \(\tau\) at the first zero (or first crossing of \(1/e\)) of the autocorrelation function \(R(\tau)\).  
2. **Average mutual information (AMI)** – pick \(\tau\) at the first *minimum* of the AMI curve.  

Both aim at making the components of the delay vector as independent as possible while still staying on the same orbit.

---

### Step 3 –  Estimate the *minimum* embedding dimension  

The idea is simple: increase \(d\) until the reconstructed attractor **unfolds** – i.e. points that are close in \(\mathbb{R}^d\) are also close on the true manifold.  
Two widely used algorithms are described below.

#### 3.1 False‑Nearest‑Neighbors (FNN) method  

1. For each point \(\mathbf{v}_k^{(d)}\) find its nearest neighbour \(\mathbf{v}_{k'}^{(d)}\) (excluding temporally close points, e.g. \(|k-k'|<\tau\)).  
2. Compute the distance in the **next** dimension:

\[
R = \frac{\bigl|x_{k+d\tau} - x_{k'+d\tau}\bigr|}{\|\mathbf{v}_k^{(d)}-\mathbf{v}_{k'}^{(d)}\|}.
\]

3. If \(R\) exceeds a threshold (commonly \(R>10\) or \(R>2\)), the neighbour is *false* – the two points appear close only because of projection.  
4. The **percentage of false neighbours** is plotted versus \(d\).  
5. The smallest \(d\) where the percentage drops essentially to zero (or below a tiny tolerance, say \(<1\%\)) is taken as the **minimum embedding dimension** \(\hat d\).

> **Why this works** – In the true state space, two distinct points cannot be arbitrarily close unless the system is truly low‑dimensional. When you embed with too few coordinates, the attractor self‑intersects, creating artificial close pairs (false neighbours). Adding dimensions “unfolds’’ the attractor and removes them.

#### 3.2 Cao’s method (a refinement)

Cao’s algorithm avoids the arbitrary distance threshold of FNN. It computes two quantities  

\[
E_1(d)=\frac{1}{N-d\tau}\sum_{k=1}^{N-d\tau}\frac{\|\mathbf{v}_{k}^{(d+1)}-\mathbf{v}_{k'}^{(d+1)}\|}{\|\mathbf{v}_{k}^{(d)}-\mathbf{v}_{k'}^{(d)}\|},
\qquad
E_2(d)=\frac{1}{N-d\tau}\sum_{k=1}^{N-d\tau}\bigl|x_{k+d\tau}-x_{k'+d\tau}\bigr|.
\]

When \(d\) reaches the true dimension, \(E_1(d)\) stabilises (its ratio \(E_1(d+1)/E_1(d)\to1\)), while \(E_2(d)\) continues to change for stochastic signals. The first \(d\) where \(E_1\) stops changing is taken as \(\hat d\).

---

### Step 4 –  Infer the number of hidden variables  

* If \(\hat d = 1\) → the scalar series alone suffices; you *cannot* conclude that additional state variables exist.  
* If \(\hat d > 1\) → the underlying dynamical system **must** have at least \(\hat d\) independent directions, i.e. at least \(\hat d-1\) hidden variables (because you already observe one, \(x\)).  

For the Lorenz system the attractor has a **fractal (Kaplan‑Yorke) dimension** \(D_{KY}\approx 2.06\).  
Typical FNN or Cao analyses on a clean Lorenz \(x(t)\) give a minimal embedding dimension  

\[
\hat d = 3\quad\text{(sometimes 4 if the measurement is not generic)}.
\]

Hence the *number of hidden variables* is  

\[
\boxed{\text{Hidden variables } = \hat d-1 = 2},
\]

which coincides with the known variables \(y(t),z(t)\).

---

### Step 5 –  Optional: Reconstruct the missing coordinates  

Once you know that a 3‑D embedding is sufficient, you can *explicitly* build the missing coordinates as the delayed copies:

\[
\begin{aligned}
\tilde x(t) &= x(t),\\
\tilde y(t) &= x(t-\tau),\\
\tilde z(t) &= x(t-2\tau).
\end{aligned}
\]

These are not the original \(y,z\) of the Lorenz equations, but a **smooth diffeomorphic image** of the true state. Any smooth function of \((\tilde x,\tilde y,\tilde z)\) can be used to model the vector field (e.g. by local linear regression, radial basis functions, or neural nets).  

If you need an explicit *equation* for the hidden variables, you can fit a model to the reconstructed trajectory:

1. Assemble a training set \(\{(\mathbf{v}_k^{(3)},\, \mathbf{v}_{k+1}^{(3)})\}\).  
2. Fit a map \(\mathbf{F}:\mathbb{R}^3\to\mathbb{R}^3\) (e.g. \(\mathbf{v}_{k+1}^{(3)} = \mathbf{F}(\mathbf{v}_k^{(3)})\)).  
3. The components of \(\mathbf{F}\) give you a discrete‑time surrogate for the continuous vector field; by numerical differentiation you can obtain a continuous‑time model \(\dot{\mathbf{v}} = \mathbf{G}(\mathbf{v})\).

---

### Step 6 –  Cross‑check with other invariants  

To be sure the embedding captured the correct dimension, compute **independent invariants**:

| Invariant | How to compute | Expected value for Lorenz |
|-----------|----------------|---------------------------|
| Correlation dimension \(D_2\) (Grassberger‑Procaccia) | Count pairs \(\| \mathbf{v}_i-\mathbf{v}_j\|<\epsilon\) for many \(\epsilon\) and fit slope of \(\log C(\epsilon)\) vs \(\log \epsilon\) | \(D_2\approx 2.05\) |
| Largest Lyapunov exponent \(\lambda_1\) | Track divergence of nearby trajectories in the embedding | \(\lambda_1\approx 0.9\) (in Lorenz units) |
| Kaplan‑Yorke dimension \(D_{KY}=j+\frac{\sum_{i=1}^{j}\lambda_i}{|\lambda_{j+1}|}\) | Use the whole Lyapunov spectrum (from step above) | Same as \(D_2\) ≈ 2.06 |

If these numbers are consistent with a **non‑integer dimension around 2**, they reinforce the conclusion that the underlying system is *not* 1‑D and that at least two hidden dimensions are required.

---

## 3.  Final answer  

*From a single scalar measurement \(x(t)\) you can determine whether other hidden state variables are present by constructing a delay‑coordinate embedding and estimating the minimal embedding dimension.*  

*If the minimal embedding dimension \(\hat d\) is larger than 1 (for the Lorenz attractor it is \(\hat d=3\)), then the system must possess \(\hat d-1\) additional independent variables. In the Lorenz case the analysis shows two hidden variables – exactly the missing \(y(t)\) and \(z(t)\).*  

Thus **the presence of hidden variables is inferred from the fact that the scalar time series alone cannot be embedded without self‑intersections; the number of extra dimensions required to unfold the attractor tells you how many hidden state variables there are.**  

---

## 4.  Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|-----------------|-----------------|
| **Choosing \(\tau\) arbitrarily (e.g. \(\tau=1\) sample).** | Too small \(\tau\)

*Original question: [Reconstructing Underlying state variable from One Observable Data](https://math.stackexchange.com/questions/5149504/reconstructing-underlying-state-variable-from-one-observable-data) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
