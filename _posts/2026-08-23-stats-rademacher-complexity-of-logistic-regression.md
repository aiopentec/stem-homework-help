---
layout: post
title: Rademacher complexity of logistic regression
author: StemFix Bot
category: stats
tags:
- stats
render_with_liquid: false
---

*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

You have logistic regression  

\[
\phi(u)=\log (1+e^{-u}) ,\qquad 
f_{w}(x)=w^{\top}x ,
\]

and you train the weight vector \(\hat w\) by **empirical risk minimisation (ERM)** on a sample  

\[
S=\{(x_{1},y_{1}),\dots ,(x_{N},y_{N})\},\qquad y_{i}\in\{-1,+1\}.
\]

You would like a *generalisation bound* for the learned predictor \(\hat f_{\hat w}\):
\[
\underbrace{\mathbb{E}_{(X,Y)}\big[\phi\big(Y\hat w^{\top}X\big)\big]}_{\text{true logistic risk}}
\;\;-\;\;
\underbrace{\frac1N\sum_{i=1}^{N}\phi\big(y_i\hat w^{\top}x_i\big)}_{\text{empirical logistic risk}} .
\]

The question is whether such a bound can be obtained **with Rademacher‑complexity arguments** (or with a VC bound) **without imposing any boundedness assumptions** on the data points \(x_i\) or on the weight vector \(w\).

---

## 2.  Full derivation  

### 2.1  Why a bound *must* involve some restriction  

The (empirical) Rademacher complexity of a class \(\mathcal{F}\) is  

\[
\widehat{\mathfrak R}_{N}(\mathcal{F})=
\frac{1}{N}\, \mathbb{E}_{\sigma}\Bigg[ \sup_{f\in\mathcal{F}}
\sum_{i=1}^{N}\sigma_i f(x_i) \Bigg] ,
\qquad \sigma_i\stackrel{i.i.d}{\sim}\{\pm1\}.
\]

If the class contains **unbounded linear functions**, i.e.  

\[
\mathcal{F}=\{x\mapsto w^{\top}x\;:\; w\in\mathbb R^{d}\},
\]

then for *any* sample that contains a non‑zero point we can choose a direction
\(w\) that makes the inner product arbitrarily large, so

\[
\sup_{w\in\mathbb R^{d}} \sum_{i=1}^{N}\sigma_i w^{\top}x_i
 = \infty .
\]

Consequently \(\widehat{\mathfrak R}_{N}(\mathcal{F})=+\infty\) and the standard
Rademacher‑complexity generalisation inequality

\[
\mathbb{E}\big[\phi(Yf(X))\big]\le
\frac1N\sum_{i=1}^{N}\phi(y_i f(x_i))+
2\,\widehat{\mathfrak R}_{N}(\phi\!\circ\!\mathcal{F}) +\text{confidence term}
\]

becomes vacuous.  
The same phenomenon appears in VC theory: the set of *all* half‑spaces has VC‑dimension
\(d+1\), which gives a bound of order \(\sqrt{d/N}\) **only for the 0/1 loss**.  
For the *logistic* (or any other *real‑valued*) loss you still need a uniform bound on the
range of the functions (or a moment condition) to apply concentration results.

Hence **some form of boundedness (or a tail‑condition) is unavoidable** if we want a *distribution‑free* bound that holds for *any* data set.

Below we present the *standard* way to obtain a useful bound: we **restrict the
norm of the weight vector** (or equivalently add an explicit regulariser) and we
**assume the inputs are bounded in Euclidean norm**.  
Both restrictions are mild in practice; they are exactly the assumptions that
appear in most statistical‑learning guarantees for linear models.

---

### 2.2  Setting the boundedness assumptions  

* **Input bound**: there exists a constant \(R>0\) such that  

  \[
  \|x_i\|_2 \le R \qquad\text{for every } i=1,\dots,N .
  \]

  (If the data are not a priori bounded, one can truncate them or work with a
  high‑probability bound assuming a sub‑Gaussian distribution; the resulting
  bound has the same order.)

* **Weight bound** (or regularisation): we consider the *restricted* class  

  \[
  \mathcal{F}_{B}= \Big\{x\mapsto w^{\top}x\;:\; \|w\|_2\le B\Big\},
  \]

  where \(B>0\) is either a hard constraint or the radius induced by an
  \(\ell_2\) regulariser \(\lambda\|w\|_2^2\) (the ERM solution then automatically
  satisfies \(\| \hat w\|_2\le \sqrt{2\lambda^{-1}\widehat L_N(\hat w)}\), see later).

With these two constants we can compute the Rademacher complexity of the *linear*
class.

---

### 2.3  Rademacher complexity of the linear class  

For any fixed sample \(\{x_i\}_{i=1}^{N}\),

\[
\begin{aligned}
\widehat{\mathfrak R}_{N}(\mathcal{F}_{B})
&= \frac{1}{N}\,
   \mathbb{E}_{\sigma}\Big[ \sup_{\|w\|\le B}
          \sum_{i=1}^{N}\sigma_i w^{\top}x_i\Big]   \\
&= \frac{1}{N}\,
   \mathbb{E}_{\sigma}\Big[ \sup_{\|w\|\le B}
          w^{\top}\Big(\sum_{i=1}^{N}\sigma_i x_i\Big)\Big]   \\
&= \frac{1}{N}\,
   \mathbb{E}_{\sigma}\Big[ B\,
          \Big\|\sum_{i=1}^{N}\sigma_i x_i\Big\|_2\Big] 
   \qquad\text{(Cauchy–Schwarz)}  \\
&\le \frac{B}{N}\,
   \mathbb{E}_{\sigma}\Big[ \sqrt{\sum_{i=1}^{N}\|x_i\|_2^{2}} \Big] 
   \qquad\text{(Khintchine inequality)}\\
&\le \frac{B}{N}\,
   \sqrt{\sum_{i=1}^{N}\|x_i\|_2^{2}} \\
&\le \frac{B R}{\sqrt N}.
\end{aligned}
\]

Thus  

\[
\boxed{\;\widehat{\mathfrak R}_{N}(\mathcal{F}_{B})\;\le\; \dfrac{BR}{\sqrt N}\;}
\tag{1}
\]

holds for *any* sample satisfying the input bound.

---

### 2.4  Contraction through the logistic loss  

The logistic loss \(\phi(u)=\log(1+e^{-u})\) is **\(L_{\phi}=1\)‑Lipschitz** on the whole
real line because  

\[
\big|\phi'(u)\big| = \frac{e^{-u}}{1+e^{-u}} \le 1 .
\]

The Ledoux–Talagrand contraction lemma yields

\[
\widehat{\mathfrak R}_{N}\big(\phi\!\circ\!\mathcal{F}_{B}\big)
   \;\le\; L_{\phi}\,\widehat{\mathfrak R}_{N}(\mathcal{F}_{B})
   \;\le\; \frac{BR}{\sqrt N}. \tag{2}
\]

---

### 2.5  Generalisation bound for the empirical minimiser  

Let  

\[
\widehat L_N(f)=\frac1N\sum_{i=1}^{N}\phi\big(y_i f(x_i)\big),\qquad
L(f)=\mathbb{E}_{(X,Y)}\big[\phi\big(Y f(X)\big)\big].
\]

For any class of functions bounded in \([0,1]\) (the logistic loss satisfies this),
the standard Rademacher‑complexity inequality (see e.g. Mohri–Rostamizadeh–Talwalkar,
*Foundations of Machine Learning*, Thm. 3.1) states that with probability at least
\(1-\delta\) over the draw of the sample:

\[
\forall f\in\mathcal{F}_{B}:\qquad
L(f) \le \widehat L_N(f) + 2\,\widehat{\mathfrak R}_{N}\big(\phi\!\circ\!\mathcal{F}_{B}\big)
          + 3\sqrt{\frac{\ln(2/\delta)}{2N}} .
\tag{3}
\]

Insert (2) into (3) and specialise to the empirical minimiser  

\[
\hat f = f_{\hat w}\;,\qquad \hat w =\arg\min_{\|w\|\le B}\widehat L_N(f_w) .
\]

Because (3) holds uniformly for all \(f\in\mathcal{F}_{B}\), it holds in particular for \(\hat f\). Hence, **with probability \(\ge 1-\delta\)**,

\[
\boxed{
L(\hat f)\;\le\;
\widehat L_N(\hat f)
\;+\;
\frac{2BR}{\sqrt N}
\;+\;
3\sqrt{\frac{\ln(2/\delta)}{2N}} } .
\tag{4}
\]

Equation (4) is the desired generalisation bound for logistic regression **under the
norm constraints** \(\|x_i\|\le R\) and \(\|w\|\le B\).

---

### 2.6  Interpreting the bound for *unregularised* ERM  

If you run *unregularised* logistic regression (no explicit constraint on \(\|w\|\)),
the solution \(\hat w\) will **still satisfy a bound** because the empirical risk is
always finite (it is in \([0,1]\)). By the optimality condition for the regularised problem

\[
\hat w_{\lambda}
 = \arg\min_{w}\Big\{ \widehat L_N(f_w) + \lambda\|w\|_2^{2} \Big\},
\]

the minimiser fulfills \(\| \hat w_{\lambda}\|_2 \le \sqrt{ \widehat L_N(\hat w_{\lambda})/\lambda}\).
Plugging \(B = \sqrt{ \widehat L_N(\hat w_{\lambda})/\lambda}\) into (4) gives a data‑dependent bound

\[
L(\hat f_{\lambda})\le
\widehat L_N(\hat f_{\lambda})
+ \frac{2R}{\sqrt N}\sqrt{\frac{\widehat L_N(\hat f_{\lambda})}{\lambda}}
+ 3\sqrt{\frac{\ln(2/\delta)}{2N}} .
\]

Thus *even without an explicit hard constraint* we obtain a meaningful bound
provided a **regularisation parameter** \(\lambda>0\) is used (or, equivalently,
the algorithm is stopped early so that \(\| \hat w\|\) does not blow up).

---

### 2.7  What VC theory gives (for comparison)  

The set of half‑spaces \(\{ \operatorname{sign}(w^{\top}x) : w\in\mathbb R^{d}\}\) has VC‑dimension \(d+1\).
A standard VC‑bound for the 0/1 loss reads, with probability \(1-\delta\),

\[
\operatorname{err}_{0/1}(\hat g)\le
\widehat{\operatorname{err}}_{0/1}(\hat g)
+ O\!\Bigg(\sqrt{\frac{d+\ln(1/\delta)}{N}}\Bigg) .
\]

To turn this into a bound for the *logistic* loss one uses the fact that logistic loss
upper‑bounds the 0/1 loss: \(\mathbf 1\{y w^{\top}x\le 0\}\le \phi(y w^{\top}x)\).  
Consequently

*Original question: [Rademacher complexity of logistic regression](https://stats.stackexchange.com/questions/123026/rademacher-complexity-of-logistic-regression) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*
