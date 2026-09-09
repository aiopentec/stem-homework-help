---
layout: question
title: Derivation of Rindler coordinates for general motion
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Derivation of Rindler coordinates for
  general motion'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the problem is asking  

We are asked to **derive the line element**

\[
\boxed{ds^{2}= \Bigl(1+\frac{a_{x'}x'}{c^{2}}+\frac{a_{y'}y'}{c^{2}}+\frac{a_{z'}z'}{c^{2}}\Bigr)^{2}c^{2}\,dt'^{2}
        -(dx'^{2}+dy'^{2}+dz'^{2})}
\tag{1}
\]

that is claimed to describe the space‑time as seen by an observer whose **proper acceleration**
\(\mathbf a(t')=(a_{x'}(t'),a_{y'}(t'),a_{z'}(t'))\) is an *arbitrary* (i.e. not necessarily constant) function of the observer’s proper time \(t'\).
In other words, we must show how the flat Minkowski metric looks in the non‑inertial coordinates \((t',x',y',z')\) that are attached to a non‑rotating, arbitrarily accelerated reference frame.

The derivation uses the *Fermi‑normal (or Fermi‑Weyl) coordinates* built around the world‑line of the observer.  
Below every step is written out explicitly.

---

## 2.  Step‑by‑step derivation  

### 2.1  Set up the inertial background  

Start with ordinary inertial Cartesian coordinates \((t, x^{i})\;(i=1,2,3)\) in flat space‑time.  
The metric is the Minkowski one (signature \(+---\))

\[
ds^{2}=c^{2}dt^{2}-dx^{2}-dy^{2}-dz^{2}
      \equiv \eta_{\mu\nu}\,dX^{\mu}dX^{\nu},
\qquad 
\eta_{\mu\nu}= \mathrm{diag}(c^{2},-1,-1,-1).
\]

Greek indices \(\mu,\nu\) run over \(0,1,2,3\) with \(X^{0}=ct\).

### 2.2  The observer’s world‑line and its tetrad  

Let the observer move along a timelike world‑line  

\[
X^{\mu}=x^{\mu}(\tau),\qquad \tau\equiv t'
\]

where \(\tau\) is the **proper time** measured by the observer.  

Define the observer’s **four‑velocity** and **four‑acceleration**

\[
u^{\mu}\equiv \frac{dx^{\mu}}{d\tau},\qquad 
a^{\mu}\equiv \frac{du^{\mu}}{d\tau}.
\]

Because \(\tau\) is proper time,
\[
u^{\mu}u_{\mu}=c^{2},\qquad u^{\mu}a_{\mu}=0 .
\]

Introduce an orthonormal tetrad \(\{e_{(0)}^{\mu},e_{(i)}^{\mu}\}\) that is **momentarily comoving** with the observer:

* \(e_{(0)}^{\mu}=u^{\mu}/c\) (unit time‑like vector);
* \(e_{(i)}^{\mu}\;(i=1,2,3)\) are three space‑like unit vectors orthogonal to \(u^{\mu}\):
  \[
  e_{(i)}^{\mu}e_{(j)\,\mu}=-\delta_{ij},\qquad
  e_{(i)}^{\mu}u_{\mu}=0 .
  \]

We demand that the spatial basis does **not rotate** with respect to the local inertial frames; this is achieved by **Fermi–Walker transport**:

\[
\frac{De_{(i)}^{\mu}}{d\tau}\equiv
\frac{de_{(i)}^{\mu}}{d\tau}
+ \Gamma^{\mu}_{\;\alpha\beta}u^{\alpha}e_{(i)}^{\beta}
 = (a_{\nu}e_{(i)}^{\nu})\frac{u^{\mu}}{c^{2}} .
\tag{2}
\]

In flat space the connection \(\Gamma^{\mu}_{\;\alpha\beta}=0\), so (2) reduces to

\[
\boxed{\displaystyle \frac{de_{(i)}^{\mu}}{d\tau}
      =\frac{a_{\nu}e_{(i)}^{\nu}}{c^{2}}\,u^{\mu}} .
\tag{3}
\]

Define the **proper‑acceleration components measured in the comoving frame**

\[
a_{i}(\tau) \equiv -\,a_{\mu}e_{(i)}^{\mu}\quad\Longrightarrow\quad
a_{\mu} = -a_{i}e_{(i)\,\mu}.
\]

(The minus sign comes from the space‑like character of \(e_{(i)}\).)  
With this definition (3) becomes simply

\[
\frac{de_{(i)}^{\mu}}{d\tau}= \frac{a_{i}}{c^{2}}\,u^{\mu}.
\tag{4}
\]

### 2.3  Defining the accelerated coordinates  

Take a point \(P\) that is *near* the observer.  Its coordinates in the inertial frame are written as a Taylor expansion about the observer’s world‑line:

\[
X^{\mu}=x^{\mu}(\tau)+e_{(i)}^{\mu}(\tau)\,\xi^{i},
\tag{5}
\]

where \(\xi^{i}\) are the **spatial coordinates measured in the instantaneously comoving inertial frame**.  
We shall identify

\[
t' \equiv \tau ,\qquad
x' \equiv \xi^{1},\qquad
y' \equiv \xi^{2},\qquad
z' \equiv \xi^{3}.
\]

Equation (5) is the definition of *Fermi normal coordinates* (sometimes called “Rindler‑like coordinates for arbitrary acceleration”).

### 2.4  Compute the differential \(dX^{\mu}\)

Differentiate (5) while remembering that the basis vectors depend on \(\tau\):

\[
\begin{aligned}
dX^{\mu}
&= \frac{dx^{\mu}}{d\tau}\,d\tau
   + \frac{de_{(i)}^{\mu}}{d\tau}\,\xi^{i}\,d\tau
   + e_{(i)}^{\mu}\,d\xi^{i} \\[2mm]
&= u^{\mu}d\tau
   +\Bigl(\frac{a_{i}}{c^{2}}u^{\mu}\Bigr)\xi^{i}d\tau
   + e_{(i)}^{\mu}d\xi^{i} \qquad\text{[using (4)]}\\[2mm]
&= u^{\mu}\Bigl(1+\frac{a_{i}\xi^{i}}{c^{2}}\Bigr)d\tau
   + e_{(i)}^{\mu}d\xi^{i}.
\end{aligned}
\tag{6}
\]

### 2.5  Insert into the Minkowski line element  

Now evaluate  

\[
ds^{2}= \eta_{\mu\nu}\,dX^{\mu}dX^{\nu}.
\]

Using the orthonormality of the tetrad,

\[
\eta_{\mu\nu}u^{\mu}u^{\nu}=c^{2},\qquad
\eta_{\mu\nu}u^{\mu}e_{(i)}^{\nu}=0,\qquad
\eta_{\mu\nu}e_{(i)}^{\mu}e_{(j)}^{\nu}=-\delta_{ij},
\]

the cross‑terms in (6) vanish and we obtain

\[
\begin{aligned}
ds^{2}
&= c^{2}\Bigl(1+\frac{a_{i}\xi^{i}}{c^{2}}\Bigr)^{2} d\tau^{2}
   -\delta_{ij}\,d\xi^{i}d\xi^{j}\\[2mm]
&= \Bigl(1+\frac{a_{x'}x'}{c^{2}}+\frac{a_{y'}y'}{c^{2}}
          +\frac{a_{z'}z'}{c^{2}}\Bigr)^{2} c^{2} dt'^{2}
   -(dx'^{2}+dy'^{2}+dz'^{2}).
\end{aligned}
\tag{7}
\]

Equation (7) is exactly the metric quoted in the problem statement.

### 2.6  Remarks on the

*Original question: [Derivation of Rindler coordinates for general motion](https://physics.stackexchange.com/questions/875835/derivation-of-rindler-coordinates-for-general-motion) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
