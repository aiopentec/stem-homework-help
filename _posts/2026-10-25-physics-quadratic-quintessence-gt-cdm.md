---
layout: question
title: Quadratic Quintessence --&gt; ΛCDM?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Quadratic Quintessence --&gt; ΛCDM?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

### 1. Plain Language Restatement

**Quintessence** is a model of dark energy where it is represented by a rolling scalar field, $\phi$, moving down a potential energy function, $V(\phi)$. **Quadratic quintessence** specifically uses a mass-like potential of the form $V(\phi) = \frac{1}{2}m^2\phi^2$. 

**$\Lambda$CDM** (Lambda Cold Dark Matter) is our standard model of cosmology, where dark energy is a true cosmological constant ($\Lambda$) with an equation of state parameter $w = -1$ that never changes in time, and its density perturbations are effectively zero.

The question asks: As we tweak the parameters of the quadratic quintessence model so that its properties today match those of a cosmological constant (holding its current energy density fixed), do the *fluctuations* (perturbations) in the dark energy field also smoothly approach zero (which is what $\Lambda$ predicts)? Or is there a sudden, jarring difference in how fluctuations behave, even when the background universe looks identical?

---

### 2. Step-by-Step Solution

#### Step 1: Define the Background Dynamics of Quadratic Quintessence
The action for a canonical scalar field $\phi$ in a Friedmann-Lemaître-Robertson-Walker (FLRW) universe is:
$$S = \int d^4x \sqrt{-g} \left[ -\frac{1}{2}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - V(\phi) \right]$$

For quadratic quintessence, the potential is:
$$V(\phi) = \frac{1}{2}m^2\phi^2$$

The background energy density $\bar{\rho}_\phi$ and pressure $\bar{p}_\phi$ are given by:
$$\bar{\rho}_\phi = \frac{1}{2}\dot{\bar{\phi}}^2 + V(\bar{\phi})$$
$$\bar{p}_\phi = \frac{1}{2}\dot{\bar{\phi}}^2 - V(\bar{\phi})$$

The equation of state parameter $w_\phi$ is:
$$w_\phi = \frac{\bar{p}_\phi}{\bar{\rho}_\phi} = \frac{\frac{1}{2}\dot{\bar{\phi}}^2 - V(\bar{\phi})}{\frac{1}{2}\dot{\bar{\phi}}^2 + V(\bar{\phi})}$$

To mimic a cosmological constant ($\Lambda$), we need $w_\phi \to -1$, which implies the kinetic energy must become much smaller than the potential energy: $\frac{1}{2}\dot{\bar{\phi}}^2 \ll V(\bar{\phi})$. This happens when the field is nearly stuck, meaning its mass $m$ is very small ($m \to 0$ relative to the Hubble expansion rate $H$).

#### Step 2: Formulate the Linear Perturbations
We work in Newtonian gauge, where the perturbed metric is:
$$ds^2 = -(1+2\Psi)dt^2 + a^2(t)(1-2\Psi)\delta_{ij}dx^i dx^j$$
(ignoring anisotropic stress for the scalar field).

Let $\delta\phi$ be the perturbation of the scalar field. The gauge-invariant density contrast $\delta_\phi \equiv \delta\rho_\phi / \bar{\rho}_\phi$ and velocity divergence $\theta_\phi$ are defined as:
$$\delta\rho_\phi = \dot{\bar{\phi}}\dot{\delta\phi} - \dot{\bar{\phi}}^2\Psi + V_{,\phi}\delta\phi$$
$$\bar{\rho}_\phi \theta_\phi = k^2 \left( \dot{\delta\phi} - \dot{\bar{\phi}}\Psi \right)$$

The linearized equation of motion for the field perturbation $\delta\phi$ in Fourier space is:
$$\ddot{delta\phi} + 3H\dot{\delta\phi} + \left( \frac{k^2}{a^2} + V_{,\phi\phi} \right)\delta\phi = 4\dot{\bar{\phi}}\dot{\Psi} - 2V_{,\phi}\Psi$$

For quadratic quintessence, $V_{,\phi} = m^2\phi$ and $V_{,\phi\phi} = m^2$.

#### Step 3: Analyze the Limit $m \to 0$ (The $\Lambda$CDM Limit)
To hold the present-day dark energy density $\bar{\rho}_{\phi,0}$ fixed while taking the $\Lambda$CDM limit, we look at how the parameters scale. The energy density today is approximately $\bar{\rho}_{\phi,0} \approx \frac{1}{2}m^2\phi_0^2$. 

As $m \to 0$, to keep $\bar{\rho}_{\phi,0}$ constant, the initial field value $\phi_0$ must become very large. 

Now, let's examine the sound speed squared $c_s^2$ of the quintessence field, which dictates how perturbations propagate:
$$c_s^2 \equiv \frac{\dot{p}_\phi}{\dot{\rho}_\phi} = 1$$
Wait! Even when $w_\phi \to -1$ (because $\dot{\bar{\phi}} \to 0$), the sound speed of a canonical scalar field is *always* $c_s^2 = 1$. 

In contrast, a true cosmological constant ($\Lambda$) has an effective sound speed and perturbations that behave such that its effective equation of state for perturbations yields no clustering ($c_{s,\Lambda}^2 = \text{undefined/irrelevant}$, but crucially, $\delta\rho_\Lambda = 0$ in frames comoving with matter).

Let's look at the effective mass term in the perturbation equation: $V_{,\phi\phi} = m^2$. As $m \to 0$, $V_{,\phi\phi} \to 0$. 

However, look at the Jeans length or the Compton wavelength of the field perturbations. The scale is set by $m$. For sub-horizon modes ($k/a \gg H$), the perturbation equation for $\delta\phi$ becomes approximately:
$$\ddot{\delta\phi} + 3H\dot{\delta\phi} + \frac{k^2}{a^2}\delta\phi \approx 0$$

Because $c_s^2 = 1$, pressure gradients resist clustering on scales smaller than the Hubble radius if $k/a \gtrsim m$. More importantly, the gauge-invariant momentum density (velocity potential) of quintessence does not vanish as $m \to 0$, whereas in $\Lambda$CDM, dark energy perturbations are strictly zero ($\delta_\rho = 0, \theta = 0$).

#### Step 4: Check the Smoothness of the Limit
As $m \rightarrow 0$ (with $\bar{\rho}_{\phi,0}$ fixed):
1. **Background:** $w_\phi \rightarrow -1$ smoothly. The background expansion history $H(z)$ smoothly approaches that of $\Lambda$CDM.
2. **Perturbations:** The sound speed remains identically $c_s^2 = 1$ *everywhere* during this limit. A canonical scalar field always propagates waves at the speed of light ($c=1$). A true cosmological constant does not have propagating dynamical degrees of freedom; its perturbations vanish identically. 

Because a canonical scalar field retains a dynamical degree of freedom with $c_s^2 = 1$ no matter how small $m$ is made, the perturbations $\delta\phi$ (and hence $\delta_\rho$) do **not** vanish. They continue to support acoustic oscillations and spatial gradients, unlike $\Lambda$CDM where dark energy perturbations are identically zero. 

Therefore, at the level of linear perturbations, the limit is **discontinuous** (often referred to in the literature as the "$w = -1$ van Hove limit" or quintessence perturbation pathology at $w=-1$).

---

### 3. Final Answer

**No**, quadratic quintessence **does not** approach $\Lambda$CDM smoothly at the level of linear perturbations, even when its present-day energy density and background equation of state are tuned to match. 

While the background expansion history smoothly approaches $\Lambda$CDM as $m \to 0$, the linear perturbations do not. A canonical scalar field always maintains a sound speed of $c_s^2 = 1$ and a propagating dynamical degree of freedom, leading to non-zero dark energy fluctuations. In contrast, $\Lambda$CDM has identically zero dark energy perturbations. This structural difference creates a permanent, non-vanishing observational signature (e.g., in the Integrated Sachs-Wolfe effect) no matter how small $m$ is taken.

---

### 4. Common Mistakes

* **Confusing Background with Perturbations:** Students often think that if $w_\phi \to -1$ on the background level, the whole model mimics $\Lambda$CDM. They forget that perturbations have their own independent dynamical equations.
* **Assuming $c_s^2 \to 0$:** A common error is assuming that as the field slows down, it stops fluctuating. For a canonical scalar field, the sound speed is identically $c_s^2 = \dot{p}/\dot{\rho} = 1$ regardless of how small the potential slope or mass is.
* **Neglecting Initial Amplitude Scaling:** Forgetting that to hold $\bar{\rho}_{\phi,0}$ fixed while sending $m \to 0$, the field value $\phi$ must diverge, which changes the mathematical behavior of the perturbation source terms.

*Original question: [Quadratic Quintessence --&gt; ΛCDM?](https://physics.stackexchange.com/questions/877206/quadratic-quintessence-%ce%9bcdm) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
