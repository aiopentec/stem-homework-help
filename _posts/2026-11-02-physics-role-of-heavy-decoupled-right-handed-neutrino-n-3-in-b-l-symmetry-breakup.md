---
layout: question
title: Role of heavy decoupled right-handed neutrino $N_3$ in B-L symmetry breakup
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Role of heavy decoupled right-handed
  neutrino $N_3$ in B-L symmetry breakup'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

# Physics Tutor Solution: The Role of the Heavy Decoupled Right-Handed Neutrino $N_3$ in $B-L$ Asymmetry Generation

---

### 1. Restatement of the Problem in Plain Language

In the context of leptogenesis (specifically the Minimal Seesaw model where right-handed neutrinos $N_1$ and $N_3$ exist), you are asking how the heaviest right-handed neutrino, $N_3$, helps generate the matter-antimatter asymmetry of the universe ($B-L$ asymmetry). 

You correctly identified from the governing equations that the rate of $B-L$ asymmetry production is inversely proportional to the Hubble expansion rate $H(a)$. You want to know:
1. Did you correctly understand that $N_3$ aids $B-L$ generation purely by suppressing the expansion rate $H$ via its energy density domination?
2. What are the other mechanisms mentioned in the literature (such as entropy injection and lowering the charged lepton Yukawa equilibration temperature to lock inverse decays)? 
3. How do all these pieces fit together into a single, coherent causal chain without oversimplifying?

---

### 2. Step-by-Step Derivation and Explanation

To understand the exact role of $N_3$, we must trace its cosmological history from the radiation-dominated era through its domination, decay, and the subsequent dynamics of the lighter $N_1$ neutrinos.

#### Step A: The Baseline $B-L$ Asymmetry Production Equation
The evolution of the $B-L$ asymmetry $n_{B-L}$ as a function of the scale factor $a$ is driven by the out-of-equilibrium decays of the lightest right-handed neutrino, $N_1$. Mathematically, this is governed by the Boltzmann equation:

$$\frac{d n_{B-L}}{d t} + 3H n_{B-L} = \varepsilon_1 \Gamma_{N_1} \left( n_{N_1} - n_{N_1}^{\text{eq}} \right)$$

where:
* $\varepsilon_1$ is the CP-asymmetry parameter in $N_1$ decays.
* $\Gamma_{N_1}$ is the decay width of $N_1$.
* $n_{N_1}$ and $n_{N_1}^{\text{eq}}$ are the actual and equilibrium number densities of $N_1$.
* $H$ is the Hubble expansion rate.

Expressed in terms of entropy-normalized yields or integrated over the scale factor $a$ (using $dt = \frac{da}{a H(a)}$), the accumulated asymmetry is proportional to:

$$n_{B-L}(a) \propto \int \frac{\varepsilon_1 \left( \rho_{N_1}(a) - \rho_{N_1}^{\text{eq}}(a) \right)}{H(a)} \frac{da}{a}$$

Your intuition is partially right: **the denominator contains $H(a)$**. If $H(a)$ is smaller, the dilution from cosmic expansion is weaker, and for a given amount of $N_1$ out-of-equilibrium abundance, the resulting $B-L$ asymmetry has more "time" and less kinematic suppression to accumulate.

---

#### Step B: The Role of $N_3$ Energy Density Domination and $H(a)$ Suppression
In the minimal seesaw model with hierarchical masses ($M_1 \ll M_3$), $N_3$ is much heavier and typically decouples and becomes non-relativistic earlier than $N_1$. 

1. **Matter Domination Phase:** Because $N_3$ decays are suppressed (due to smaller Yukawa couplings or phase space constraints), $N_3$ can dominate the total energy density of the Universe before it decays. 
2. **Impact on Hubble $H$:** During a standard radiation-dominated era, $H \propto T^2 \propto 1/a^2$. However, when a massive particle species like $N_3$ dominates the energy density, the universe enters a temporary **matter-dominated epoch**. The expansion rate during matter domination is given by:
   $$H^2 = \frac{\rho_{\text{total}}}{3M_{\text{Pl}}^2} \approx \frac{\rho_{N_3}}{3M_{\text{Pl}}^2}$$
   While $\rho_{N_3}$ falls as $a^{-3}$, the radiation density falls as $a^{-4}$. Thus, $N_3$ domination alters the scaling of $H$ relative to temperature compared to pure radiation domination. More importantly, the absolute value of $H$ at the time of $N_1$ decay can be modulated by how long and how completely $N_3$ dominated.

---

#### Step C: Entropy Injection (Reheating)
When $N_3$ eventually decays, it dumps a massive amount of entropy into the standard model plasma (a process akin to a secondary reheating of the universe). 

* **Dilution vs. Production:** Entropy injection dilutes *existing* particle abundances. If $B-L$ asymmetry was already present before $N_3$ decay, it would be washed out/diluted. 
* **The Delayed Decoupling Mechanism:** The key point of the article (*Delayed Charged Lepton Yukawa Equilibration*) is that $N_3$ decay sets the stage *before* $N_1$ dominates or decays. The entropy injection alters the thermal history, specifically lowering the ambient temperature of the plasma relative to what it would have been in standard cosmology.

---

#### Step D: Lowering the Charged Lepton Yukawa Equilibration Temperature
This is the most critical subtle point in the authors' argument:

1. **Yukawa Equilibration:** Standard thermal leptogenesis assumes that charged lepton Yukawa interactions (like those of tau and muon electrons) enter thermal equilibrium rapidly at high temperatures. When these interactions are in equilibrium, they distinguish lepton flavors and can wash out asymmetries through inverse decays and scattering.
2. **The $N_3$ Effect:** By dominating the energy density and subsequently decaying, $N_3$ injects entropy that **lowers the temperature** at which these charged lepton Yukawa interactions come into thermal equilibrium. 
3. **Locking Inverse Decays:** Because the Yukawa equilibration temperature is pushed down, the universe reaches temperatures where $N_1$ decays can occur *before* the wash-out processes (driven by rapid inverse decays and lepton-flavor mixing) become fully efficient. 
4. **The Result:** The asymmetry generated by $N_1$ decays is "locked in" (protected from being washed out) because the inverse processes that would normally erase the $B-L$ asymmetry are suppressed or delayed relative to the $N_1$ decay timeline.

---

#### Step E: Synthesizing the Complete Causal Chain

Putting it all together, the role of $N_3$ is **not** just a single-variable trick involving $H(a)$. It is a multi-step thermodynamic choreography:

1. **$N_3$ Domination:** $N_3$ takes over the universe's energy density, temporarily altering the expansion history ($H$).
2. **Entropy Injection & Temperature Drop:** When $N_3$ decays, it reheats the universe and shifts the thermal timeline, effectively lowering the temperature threshold at which charged-lepton Yukawa interactions equilibrate.
3. **Evading Washout:** Because Yukawa equilibrium is delayed, the inverse decays (which destroy $B-L$ asymmetry) are held off.
4. **Efficient $N_1$ Asymmetry Generation:** With washout processes suppressed and the expansion rate favorably tuned by the cosmological history, the lighter $N_1$ decays can inject a robust, un-minimized $\varepsilon_1$-weighted $B-L$ asymmetry into the plasma.

---

### 3. Final Answer

Your intuition that $N_3$ acts through the expansion rate $H(a)$ is **qualitatively on the right track, but incomplete**. 

* **Is $H$ the only factor?** No. While $N_3$ energy density domination modifies the Hubble expansion rate $H(a)$—which mathematically appears in the denominator of the $B-L$ accumulation integral—the dominant physical mechanism stressed by the authors is **entropy injection and its effect on Yukawa equilibration**.
* **The exact role of $N_3$:** $N_3$ dominates the energy density and decays, injecting entropy that **lowers the charged lepton Yukawa equilibration temperature**. This delay prevents rapid inverse decays from washing out the asymmetry, thereby "locking in" the $B-L$ asymmetry produced subsequently by the out-of-equilibrium decays of the lighter $N_1$ neutrinos.

---

### 4. Common Mistakes for This Problem Type

1. **Treating $H$ as a constant scalar:** Assuming $H$ is just a static number rather than a dynamically evolving quantity tied to the dominant energy component (radiation vs. $N_3$ matter domination) of the universe.
2. **Ignoring Washout Processes:** Assuming that generating asymmetry ($\varepsilon_1 \neq 0$) is sufficient. In leptogenesis, the *net* asymmetry is a fierce competition between production (decays) and destruction (inverse decays and scatterings). Failing to account for how $N_3$ delays Yukawa equilibrium misses the entire point of the cited paper.
3. **Confusing Entropy Dilution with Entropy Reheating:** Assuming entropy injection *only* dilutes things. While it dilutes pre-existing relics, it also resets the thermal clock of the universe, shifting the relative temperatures at which standard model gauge and Yukawa interactions enter equilibrium.

*Original question: [Role of heavy decoupled right-handed neutrino $N_3$ in B-L symmetry breakup](https://physics.stackexchange.com/questions/877413/role-of-heavy-decoupled-right-handed-neutrino-n-3-in-b-l-symmetry-breakup) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
