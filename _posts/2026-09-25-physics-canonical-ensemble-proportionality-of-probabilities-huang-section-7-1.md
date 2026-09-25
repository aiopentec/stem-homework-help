---
layout: question
title: Canonical ensemble - Proportionality of probabilities - Huang Section 7.1
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Canonical ensemble - Proportionality
  of probabilities - Huang Section 7.1'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

We have a large isolated system that is the sum of two weakly‑coupled parts  

* subsystem 1 – the “small” system we are interested in, with Hamiltonian  
  \(\mathcal H_{1}(p_{1},q_{1})\) and energy \(E_{1}\);
* subsystem 2 – a huge heat bath, with Hamiltonian \(\mathcal H_{2}(p_{2},q_{2})\) and energy \(E_{2}\).

The whole composite system is described by the **micro‑canonical ensemble**: every point \((p_{1},q_{1},p_{2},q_{2})\) whose total energy lies in the narrow interval \([E,\;E+2\Delta]\) is *equally likely*.

The book states that the probability of finding subsystem 1 in a particular infinitesimal phase‑space cell \(dp_{1}\,dq_{1}\) is **proportional to** the phase‑space volume that subsystem 2 can occupy at the complementary energy  
\(E_{2}=E-E_{1}\):

\[
\boxed{ \;P(p_{1},q_{1})\;dp_{1}\,dq_{1}\;\propto\;\Gamma_{2}\!\bigl(E-E_{1}\bigr)\;dp_{1}\,dq_{1}\;}
\]

The student asks: *Why does this proportionality hold?*  

Below we give a step‑by‑step derivation, starting from the definition of the micro‑canonical ensemble and showing exactly how the factor \(\Gamma_{2}(E-E_{1})\) appears.

---

## 2.  Detailed derivation

### 2.1  Micro‑canonical probability density for the whole composite

For an isolated system with total Hamiltonian  

\[
\mathcal H(p_{1},q_{1},p_{2},q_{2})=
\mathcal H_{1}(p_{1},q_{1})+\mathcal H_{2}(p_{2},q_{2})
\equiv E_{1}+E_{2},
\]

the **micro‑canonical ensemble** is defined by the uniform density  

\[
\rho_{\text{mc}}(p_{1},q_{1},p_{2},q_{2})=
\frac{1}{\Omega(E)}\;
\delta\!\bigl(E-H(p_{1},q_{1},p_{2},q_{2})\bigr),
\tag{1}
\]

where  

\[
\Omega(E)=\int d\Gamma_{1}\,d\Gamma_{2}\;
\delta\!\bigl(E-H_{1}-H_{2}\bigr)
\]

is the total phase‑space “area’’ (more precisely, the *density of states*) of the composite system, and  

\[
d\Gamma_{i}\equiv dp_{i}\,dq_{i}
\quad(i=1,2)
\]

denotes the infinitesimal volume element of subsystem \(i\).

The delta‑function implements the restriction that the total energy be exactly \(E\); the thin shell of width \(2\Delta\) used in the textbook is handled by the same expression in the limit \(\Delta\to 0\).

### 2.2  Probability that subsystem 1 lies in a particular cell

We want the probability that subsystem 1’s coordinates fall inside a given infinitesimal cell \(d\Gamma_{1}=dp_{1}\,dq_{1}\) centred at \((p_{1},q_{1})\), irrespective of what subsystem 2 does. This is obtained by **integrating out** the degrees of freedom of subsystem 2:

\[
\begin{aligned}
P(p_{1},q_{1})\,d\Gamma_{1}
&= \int d\Gamma_{2}\;
\rho_{\text{mc}}(p_{1},q_{1},p_{2},q_{2})\\[4pt]
&= \frac{1}{\Omega(E)}
\int d\Gamma_{2}\;
\delta\!\bigl(E-\underbrace{H_{1}(p_{1},q_{1})}_{E_{1}}
-\underbrace{H_{2}(p_{2},q_{2})}_{E_{2}}\bigr) .
\end{aligned}
\tag{2}
\]

The only quantity that depends on \((p_{2},q_{2})\) inside the integral is the second term of the argument of the delta‑function, i.e. the **energy of subsystem 2**.

### 2.3  Introducing the phase‑space volume \(\Gamma_{2}(E_{2})\)

Define the *phase‑space volume* (often called the *integrated density of states*) of subsystem 2 at a given energy \(E_{2}\) as  

\[
\Gamma_{2}(E_{2}) \equiv \int d\Gamma_{2}\;
\Theta\!\bigl(E_{2}-H_{2}(p_{2},q_{2})\bigr),
\tag{3}
\]

where \(\Theta\) is the Heaviside step function.  
Differentiating (3) with respect to \(E_{2}\) gives the usual density of states  

\[
\frac{d\Gamma_{2}}{dE_{2}} = \int d\Gamma_{2}\;
\delta\!\bigl(E_{2}-H_{2}\bigr) .
\tag{4}
\]

Equation (2) contains precisely the integral on the right‑hand side of (4) with the identification  

\[
E_{2}=E-E_{1}.
\]

Hence

\[
\int d\Gamma_{2}\;
\delta\!\bigl(E-E_{1}-H_{2}\bigr)=
\frac{d\Gamma_{2}}{dE_{2}}\Bigg|_{E_{2}=E-E_{1}} .
\tag{5}
\]

Because we are interested only in the *relative* probability of different microstates of subsystem 1, the overall normalisation factor \(1/\Omega(E)\) can be dropped (it will be absorbed later when we normalise the distribution). Consequently

\[
P(p_{1},q_{1})\,d\Gamma_{1}\;\propto\;
\frac{d\Gamma_{2}}{dE_{2}}\Big|_{E_{2}=E-E_{1}}\;d\Gamma_{1}.
\tag{6}
\]

For a macroscopic subsystem (the heat bath) the function \(\Gamma_{2}(E_{2})\) is an *exponentially large* monotonic function of its argument. Over the tiny range of energies that subsystem 1 can exchange with the bath (\(\Delta E_{1}\sim\) a few \(k_{B}T\)), \(\Gamma_{2}\) varies only very slowly, so it is legitimate to replace the derivative by the function itself up to an irrelevant constant factor:

\[
\frac{d\Gamma_{2}}{dE_{2}} \propto \Gamma_{2}(E_{2}) .
\]

Thus we arrive at the textbook statement

\[
\boxed{
P(p_{1},q_{1})\;dp_{1}\,dq_{1}
\;\propto\;
\Gamma_{2}\!\bigl(E-E_{1}\bigr)\;dp_{1}\,dq_{1}
}
\tag{7}
\]

which says: *the likelihood of a particular microstate of the small system is proportional to the number of microstates that the big heat bath can still occupy once it has given up the energy \(E_{1}\) to the small system.*

### 2.4  From \(\Gamma_{2}\) to the Boltzmann factor

For a macroscopic bath the entropy is defined by  

\[
S_{2}(E_{2}) = k_{B}\,\ln \Gamma_{2}(E_{2}).
\]

Using a first‑order Taylor expansion of the entropy about the most probable energy \(\bar E_{2}\),

\[
S_{2}(E_{2}) = S_{2}(\bar E_{2}) + 
\left.\frac{\partial S_{2}}{\partial E_{2}}\right|_{\bar E_{2}}(E_{2}-\bar E_{2}) + \cdots,
\]

and noting that \(\displaystyle \frac{\partial S_{2}}{\partial E_{2}} = \frac{1}{T}\) (definition of temperature), we obtain

\[
\Gamma_{2}(E-E_{1}) = 
\exp\!\bigl[ S_{2}(E-E_{1})/k_{B} \bigr] 
\propto 
\exp\!\bigl[-E_{1}/(k_{B}T)\bigr] .
\]

Plugging this into (7) gives the familiar canonical‑ensemble probability density for subsystem 1:

\[
P(p_{1},q_{1}) \propto 
\exp\!\bigl[-\mathcal H_{1}(p_{1},q_{1})/(k_{B}T)\bigr] .
\]

The proportionality constant is fixed by normalising the distribution over the phase space of subsystem 1, producing the partition function \(Z\).

---

## 3.  Final answer

The proportionality  

\[
P(p_{1},q_{1})\,dp_{1}\,dq_{1} \propto \Gamma_{2}\!\bigl(E-E_{1}\bigr)\,dp_{1}\,dq_{1}
\]

follows directly from the definition of the micro‑canonical ensemble for the total isolated system.  

* The micro‑canonical ensemble assigns equal probability to every point in the total phase space whose total energy lies in \([E,E+2\Delta]\).  
* Integrating this uniform density over the degrees of freedom of subsystem 2 leaves, for a given \((p_{1},q_{1})\), the **density of states** of subsystem 2 at the complementary energy \(E_{2}=E-E_{1}\).  
* That density of states is precisely the phase‑space volume \(\Gamma_{2}(E_{2})\).  

Hence the probability of a particular microstate of subsystem 1 is proportional to the number of microstates available to the large bath when the bath’s energy is reduced by the amount \(E_{1}\).  

When the bath is macroscopic, \(\Gamma_{2}(E-E_{1})\) can be written as \(\exp[-E_{1}/(k_{B}T)]\), leading to the canonical (Boltzmann) distribution for subsystem 1.

---

## 4.  Common mistakes and how to avoid them

| Mistake | Why it’s wrong | How to correct it |
|---------|----------------|-------------------|
| **Confusing \(\Gamma_{2}(E_{2})\) with the density of states \(\omega_{2}(E_{2})\).** | \(\Gamma_{2}\) is the *integrated* phase‑space volume, while \(\omega_{2}=d\Gamma_{2}/dE_{2}\) is the *density*. The derivation uses the latter, but for a huge bath the two are proportional up to an irrelevant constant. | Keep the distinction clear: start from \(\omega_{2}=d\Gamma_{2}/dE_{2}\) (Eq. 4). Then note that for a macroscopic bath the factor of proportionality is the same for all relevant \(E_{1}\) and can be absorbed into the overall normalisation. |
| **Dropping the delta‑function too early.** | The micro‑canonical uniformity is encoded in the \(\delta(E-H)\). Ignoring it makes the argument lose the link between the total energy constraint and the appearance of \(\Gamma_{2}\). | Write the probability as an explicit integral over the delta function (Eq. 2) and only after performing the integral over subsystem 2 replace it by \(\omega_{2}(E-E_{1})\). |
| **Assuming the bath’s energy is exactly \(E\).** | The bath’s energy fluctuates because subsystem 1 can exchange energy; the correct expression uses \(E_{2}=E-E_{1}\). | Remember the energy‑conservation constraint

*Original question: [Canonical ensemble - Proportionality of probabilities - Huang Section 7.1](https://physics.stackexchange.com/questions/876372/canonical-ensemble-proportionality-of-probabilities-huang-section-7-1) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
