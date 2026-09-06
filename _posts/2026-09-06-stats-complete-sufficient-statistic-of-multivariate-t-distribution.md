---
layout: question
title: Complete sufficient statistic of multivariate t-distribution
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Complete sufficient statistic of multivariate
  t-distribution'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  What is being asked?

We have a random vector  

\[
X=(X_{1},\dots ,X_{n})\sim t_{n,\nu}\bigl(0,\sigma^{2}I_{n}\bigr),
\qquad \nu>4,
\]

i.e. a **multivariate Student‑\(t\)** distribution with  

* location vector \(0\),  
* scale matrix \(\sigma^{2}I_{n}\) (the only unknown parameter), and  
* \(\nu\) degrees of freedom (known).

From the factorisation theorem the statistic  

\[
T(X)=\sum_{i=1}^{n}X_{i}^{2}
\]

is sufficient for \(\sigma^{2}\).  
The question is: **Is \(T\) also *complete* for the one‑parameter family \(\{\sigma^{2}>0\}\)?**  

In other words, we must decide whether the following implication holds:

\[
\boxed{\;
E_{\sigma^{2}}\bigl[g(T)\bigr]=0\;\text{for every }\sigma^{2}>0\;
\Longrightarrow\;g(T)=0\;\text{a.s.}
\;}
\]

If it holds, \(T\) is a *complete sufficient statistic*; otherwise it is not.

---

## 2.  Full solution  

### 2.1  A useful representation of the multivariate \(t\)

Let  

* \(Z\sim N_{n}(0,I_{n})\) (standard normal vector),  
* \(W\sim \chi^{2}_{\nu}\) (chi‑square with \(\nu\) d.f.),  

independent of each other.  
Then

\[
X\;\stackrel{d}{=}\; \frac{\sigma}{\sqrt{W/\nu}}\; Z .
\]

Consequently  

\[
T=\sum_{i=1}^{n}X_{i}^{2}
      =\sigma^{2}\,\frac{\lVert Z\rVert ^2}{W/\nu}.
\]

Now \(\l

*Original question: [Complete sufficient statistic of multivariate t-distribution](https://stats.stackexchange.com/questions/677090/complete-sufficient-statistic-of-multivariate-t-distribution) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
