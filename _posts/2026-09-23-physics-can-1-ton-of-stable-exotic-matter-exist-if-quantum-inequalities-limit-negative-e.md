---
layout: question
title: Can 1 ton of stable exotic matter exist if Quantum Inequalities limit negative
  energy?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Can 1 ton of stable exotic matter exist
  if Quantum Inequalities limit negative energy?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the student is really asking  

* **Goal:**  Understand whether it is possible, even in principle, to have a **macroscopic amount of stable “negative‑energy” (or exotic) matter** – e.g. **‑1000 kg** of mass‑equivalent – that could keep a 1 m traversable wormhole open for a second.  

* **Specific questions**  

  1. Does a block of exotic matter with a total negative energy of \(-1000\;{\rm kg}\,c^{2}\) existing for 1 s **violate the Ford‑Roman Quantum Inequality** (QI)?  
  2. Are there any “loopholes’’ (curved spacetime, metamaterials, Casimir plates, etc.) that could let such a large amount of negative energy be stable?  
  3. Is the Casimir‑energy estimate \(\sim10^{-27}\;{\rm kg}\) for 1‑µm‑spaced plates correct?

Below we answer each point step‑by‑step, keeping the math as elementary as possible.

---

## 2.  Basics you need to know  

| Symbol | Meaning | Typical value |
|--------|---------|---------------|
| \(c\) | Speed of light | \(c = 2.998\times10^{8}\;{\rm m\,s^{-1}}\) |
| \(\hbar\) | Reduced Planck constant | \(\hbar = 1.055\times10^{-34}\;{\rm J\,s}\) |
| \(E = mc^{2}\) | Energy equivalent of a mass \(m\) | 1 kg → \(9.0\times10^{16}\;{\rm J}\) |
| Quantum Inequality (schematic) | \(\displaystyle \int_{-\infty}^{\infty}\rho(t)f(t)dt \;\ge\; -\frac{K}{\tau^{4}}\) | \(K\) is a number of order 1 (in units where \(\hbar = c = 1\)).  \(\tau\) = sampling time. |
| Casimir energy (parallel plates) | \(\displaystyle E_{\rm Cas}= -\frac{\pi^{2}\hbar c}{720}\,\frac{A}{a^{3}}\) | \(A\) = plate area, \(a\) = separation |

*The Quantum Inequality* tells us that **the larger the magnitude of a negative energy density, the shorter the time it can persist**.  A useful back‑of‑the‑envelope version (obtained by assuming the negative energy is roughly constant over a time \(\tau\)) is  

\[
|E_{\rm neg}| \;\lesssim\; \frac{\hbar}{\tau}\, .
\tag{1}
\]

Equation (1) is not exact, but it gives the right order of magnitude for what the QI permits.

---

## 3.  How much negative energy would 1 ton of exotic matter carry?  

\[
\begin{aligned}
|E_{\rm ton}| &= (1000\;{\rm kg})\,c^{2} \\
              &= 1000 \times 9.0\times10^{16}\;{\rm J} \\
              &= 9.0\times10^{19}\;{\rm J}.
\end{aligned}
\]

That is the *negative* energy we would like to have for the wormhole.

---

## 4.  Quantum‑Inequality bound for a 1‑second “pulse’’  

Set the allowed duration \(\tau = 1\;{\rm s}\) in (1):

\[
|E|_{\max} \;\approx\; \frac{\hbar}{\tau}
                     = \frac{1.055\times10^{-34}\;{\rm J\,s}}{1\;{\rm s}}
                     = 1.1\times10^{-34}\;{\rm J}.
\]

Even if we ignore the factor of order‑unity that the full QI contains, the bound is **~\(10^{-34}\) J**, i.e. a mass‑equivalent of

\[
m_{\max} = \frac{|E|_{\max}}{c^{2}} \approx
\frac{1.1\times10^{-34}}{9.0\times10^{16}}
\approx 1.2\times10^{-51}\;{\rm kg}.
\]

*Conclusion:* The QI allows at most about \(10^{-51}\) kg of negative mass for a **continuous** 1‑second interval—**over 70 orders of magnitude** smaller than the \(-1000\) kg you ask for.  So a 1‑ton block of exotic matter persisting for a second would **grossly violate the quantum inequality**.

---

## 5.  Could curved spacetime or clever engineering relax the bound?  

* **Curved spacetime** – The original Ford‑Roman derivations were done in flat Minkowski space, but later work (e.g. Fewster & Roman, 2005) shows that the same scaling \( |E| \propto \tau^{-1}\) holds *locally* in any globally hyperbolic spacetime, up to factors of order one.  Curvature can change the numerical coefficient, but **cannot remove the \(\tau^{-1}\) scaling**, so the bound remains astronomically small for \(\tau\sim 1\) s.

* **Metamaterials / engineered Casimir geometries** – By shaping conductors you can change the *distribution* of Casimir energy, but the total negative energy is still given by the same formula (it scales like \(\hbar c A/a^{3}\)).  You can increase the magnitude by:
  1. Making the gap \(a\) **smaller** (e.g. nanometre instead of micrometre);
  2. Using a **larger area** \(A\).  

  Even with optimistic numbers—say \(a = 10\;{\rm nm}\) and \(A = 10^{6}\;{\rm m^{2}}\) (a square kilometre)—the Casimir energy is

  \[
  E_{\rm Cas}\; \sim\; -\frac{\pi^{2}\hbar c}{720}\,
     \frac{10^{6}}{(10^{-8})^{3}}
     \; \approx\; -4\times10^{-2}\;{\rm J},
  \]

  i.e. a negative mass of \(\sim 4\times10^{-19}\) kg.  This is **still 70+ orders of magnitude** below the ton scale.

* **Squeezed‑vacuum or other quantum‑optical tricks** – They can produce larger *instantaneous* negative energy densities, but the QI still caps the *time‑averaged* amount.  The same \(|E| \lesssim \hbar/\tau\) bound applies.

**Bottom line:** No known configuration—whether Casimir plates, squeezed light, or exotic spacetime curvature—can circumvent the QI enough to accumulate a macroscopic, stable amount of negative energy such as \(-1000\) kg for a second.

---

## 6.  Verify the Casimir‑energy estimate in the question  

For two perfectly conducting plates of area \(A\) separated by \(a = 1\;\mu{\rm m}=10^{-6}\) m:

\[
\begin{aligned}
E_{\rm Cas}&= -\frac{\pi^{2}\hbar c}{720}\,\frac{A}{a^{3}} \\
           &= -\frac{9.87 \times (1.055\times10^{-34}\,{\rm J\,s})(2.998\times10^{8}\,{\rm m/s})}{720}\,
              \frac{A}{(10^{-6})^{3}} \\
           &= -\frac{3.12\times10^{-25}\;{\rm J\,m}}{720}\,
              \frac{A}{10^{-18}\,{\rm m^{3}}} \\
           &= -4.3\times10^{-10}\;{\rm J}\,\frac{A}{1\;{\rm m^{2}}}.
\end{aligned}
\]

Convert to mass units:

\[
m_{\rm Cas}= \frac{|E_{\rm Cas}|}{c^{2}}
            = \frac{4.3\times10^{-10}\;{\rm J}}{9.0\times10^{16}\;{\rm J/kg}}
            \approx 4.8\times10^{-27}\;{\rm kg}
\]

per **one square metre** of plate area.  
So the student’s figure of “\(10^{-27}\) kg” is correct (within a factor of two).  Even if you stacked a *million* such plates, you would still be many, many orders short of a gram, let alone a ton.

---

## 7.  Final answer – in plain language  

* A “ton of exotic matter” would carry a negative energy of about \(9\times10^{19}\) J.  
* The Ford‑Roman quantum inequality tells us that, for a pulse lasting one second, the most negative energy that any quantum field can sustain is roughly \(10^{-34}\) J – **70 + orders of magnitude smaller**.  
* Therefore a stable block of \(-1000\) kg of negative energy for one second would **directly violate the quantum inequality**; it is not allowed by known quantum‑field theory.  
* Casimir plates, squeezed light, or clever geometries can produce negative energy, but the amount scales as \(\hbar c A / a^{3}\) and is tiny; even the most optimistic laboratory set‑ups fall short by at least 20–30 orders of magnitude.  
* Curved spacetime does not remove the fundamental \(|E| \propto 1/\tau\) scaling, so

*Original question: [Can 1 ton of stable exotic matter exist if Quantum Inequalities limit negative energy?](https://physics.stackexchange.com/questions/876298/can-1-ton-of-stable-exotic-matter-exist-if-quantum-inequalities-limit-negative-e) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
