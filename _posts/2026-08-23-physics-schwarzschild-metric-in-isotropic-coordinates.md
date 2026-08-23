---
layout: post
title: Schwarzschild metric in Isotropic coordinates
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

### 1. What is being asked?

You are given the standard Schwarzschild metric (which describes the spacetime around a spherically symmetric, uncharged mass) in standard Schwarzschild coordinates. You are also shown the coordinate transformation used to rewrite this metric into **isotropic coordinates**, where the spatial part of the metric looks conformally flat (resembling spherical coordinates in flat Euclidean space multiplied by a conformal factor). 

The question is: **Where does the transformation equation for $r$ come from?** How do we actually derive or discover the relation between the standard radial coordinate $r$ and the isotropic radial coordinate $r'$?

---

### 2. Step-by-Step Derivation

To find where the transformation comes from, we need to start with the spatial part of the Schwarzschild metric and demand that it takes the isotropic form:
$$ds_{\text{spatial}}^2 = \left(1 - \frac{2GM}{r}\right)^{-1} dr^2 + r^2 (d\theta^2 + \sin^2\theta d\phi^2)$$
*(Note: In your prompt, $2m$ or $2GM$ represents the Schwarzschild radius, often set to $2M$ in geometric units where $G=1$).*

We want to find a new radial coordinate, let's call it $r'$, such that the spatial metric becomes **conformally flat**:
$$ds_{\text{spatial}}^2 = \Omega(r')^2 \left[ dr'^2 + r'^2 (d\theta^2 + \sin^2\theta d\phi^2) \right]$$
where $\Omega(r')$ is some conformal factor (a function of $r'$ only).

#### Step 1: Compare the angular parts
Look at the angular part ($d\theta^2 + \sin^2\theta d\phi^2$) in both metrics. 
In the standard metric, it is multiplied by $r^2$. 
In the isotropic metric, it is multiplied by $\Omega(r')^2 r'^2$. 

By equating these two terms, we immediately establish a relation between $r$, $r'$, and the conformal factor $\Omega(r')$:
$$r^2 = \Omega(r')^2 r'^2 \implies r = r' \Omega(r')$$

#### Step 2: Transform the radial differential $dr$
Now we need to relate the differentials $dr$ and $dr'$. Using our relation $r = r'\Omega(r')$, we take the derivative:
$$dr = \frac{d}{dr'} \big( r' \Omega(r') \big) dr' = \left( \Omega(r') + r' \frac{d\Omega}{dr'} \right) dr'$$

#### Step 3: Substitute into the radial part of the metric
The standard spatial metric component for $dr^2$ is:
$$g_{rr} dr^2 = \left(1 - \frac{2M}{r}\right)^{-1} dr^2$$

Substitute our expression for $dr$ into this term:
$$g_{rr} dr^2 = \left(1 - \frac{2M}{r}\right)^{-1} \left( \Omega + r'\frac{d\Omega}{dr'} \right)^2 dr'^2$$

#### Step 4: Demand the isotropic form
For the metric to be in isotropic coordinates, the coefficient of $dr'^2$ *must* equal the conformal factor $\Omega(r')^2$ (because the isotropic spatial metric is $\Omega^2(dr'^2 + r'^2d\Omega^2) = \Omega^2 dr'^2 + \Omega^2 r'^2(d\theta^2 + \sin^2\theta d\phi^2)$).

Therefore, we set:
$$\left(1 - \frac{2M}{r}\right)^{-1} \left( \Omega + r'\frac{d\Omega}{dr'} \right)^2 = \Omega^2$$

Take the square root of both sides:
$$\left(1 - \frac{2M}{r}\right)^{-1/2} \left( \Omega + r'\frac{d\Omega}{dr'} \right) = \Omega$$

#### Step 5: Solve the differential equation for $\Omega(r')$
Rearrange the equation to separate variables or integrate:
$$\left(1 - \frac{2M}{r}\right)^{-1/2} \left( 1 + \frac{r'}{\Omega}\frac{d\Omega}{dr'} \right) = 1$$

Recall from Step 1 that $r = r'\Omega$, which means $\frac{r}{r'} = \Omega$. Substitute this back in:
$$\left(1 - \frac{2M}{r}\right)^{-1/2} \left( 1 + \frac{r'}{\Omega}\frac{d\Omega}{dr'} \right) = 1$$

Actually, it is much easier to work directly with $r$ and $r'$. Let's rewrite $\left(1 - \frac{2M}{r}\right)^{-1/2}$ as $\frac{dr}{dr'\Omega}$:
From $\left(1 - \frac{2M}{r}\right)^{-1} dr^2 = \Omega^2 dr'^2$, we take the square root directly:
$$\frac{dr}{\sqrt{1 - \frac{2M}{r}}} = \Omega \, dr'$$

Since $\Omega = \frac{r}{r'}$, we substitute that in:
$$\frac{dr}{\sqrt{1 - \frac{2M}{r}}} = \frac{r}{r'} dr'$$

Rearrange terms to group $r$ on one side and $r'$ on the other:
$$\frac{dr}{r \sqrt{1 - \frac{2M}{r}}} = \frac{dr'}{r'}$$

#### Step 6: Integrate both sides
Now, integrate both sides of the equation:
$$\int \frac{dr}{r \sqrt{1 - \frac{2M}{r}}} = \int \frac{dr'}{r'}$$

* **Right side:** $\int \frac{dr'}{r'} = \ln(r') + C_1 = \ln\left(\frac{r'}{C}\right)$
* **Left side:** Use the substitution $u = \sqrt{1 - \frac{2M}{r}}$ (or standard integral tables) to find that:
  $$\int \frac{dr}{r \sqrt{1 - \frac{2M}{r}}} = \ln\left( \frac{\sqrt{1 - 2M/r} - 1}{\sqrt{1 - 2M/r} + 1} \right) + \text{constant}$$

Equating the integrals (and setting the integration constant such that $r \to r'$ at spatial infinity, where $C = M/4$):
$$\ln\left( \frac{\sqrt{1 - 2M/r} - 1}{\sqrt{1 - 2M/r} + 1} \right) = \ln\left( \frac{4r'}{M} \right)$$

Exponentiate both sides:
$$\frac{\sqrt{1 - 2M/r} - 1}{\sqrt{1 - 2M/r} + 1} = \frac{4r'}{M}$$

Solving this algebraic equation for $r$ in terms of $r'$ yields:
$$r = r'\left(1 + \frac{M}{2r'}\right)^2$$

This differential equation requirement is precisely where the coordinate transformation comes from.

---

### 3. Final Answer

The coordinate transformation $r = r'\left(1+\frac{M}{2r'}\right)^2$ is not chosen at random; it is **derived** by demanding that the spatial part of the Schwarzschild metric becomes **conformally flat** (i.e., isotropic), meaning the cross-terms vanish and the spatial metric takes the form $ds^2 = \Omega(r')^2 [dr'^2 + r'^2 d\Omega^2]$. Solving the differential equation $\frac{dr}{\sqrt{1 - 2M/r}} = \frac{r}{r'} dr'$ forces this exact relationship between $r$ and $r'$.

---

### 4. Common Mistakes

* **Assuming a linear relation:** Students often guess a simple scaling like $r = k r'$ or $r = r' + M$. Isotropic coordinates require a non-linear inverse-square relation to completely eliminate the off-diagonal metric components and flatten the spatial volume element.
* **Confusing $M$ and $2M$ definitions:** Different authors define the mass parameter differently ($m$, $GM$, $2M$, or $r_s$ for Schwarzschild radius). Be very careful tracking factors of 2 when integrating the differential equation.
* **Forgetting the conformal factor:** Trying to change coordinates by only substituting $r(r')$ into the $dr^2$ term while forgetting that the angular pre-factor ($r^2$) must also transform ($\Omega^2 r'^2$).

*Original question: [Schwarzschild metric in Isotropic coordinates](https://physics.stackexchange.com/questions/145342/schwarzschild-metric-in-isotropic-coordinates) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
