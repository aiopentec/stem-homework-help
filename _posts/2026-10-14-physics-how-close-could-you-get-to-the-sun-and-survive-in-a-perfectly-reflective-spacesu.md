---
layout: question
title: How close could you get to the Sun and survive in a perfectly reflective spacesuit?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How close could you get to the Sun and
  survive in a perfectly reflective spacesuit?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the problem is really asking  

You have a **spacesuit that reflects every photon that hits it** (i.e. it absorbs *no* electromagnetic radiation).  
How close could a person wearing that suit get to the **visible surface of the Sun** and still stay alive for an hour?

In other words we must find the smallest distance from the Sun at which the *net heat* that reaches the astronaut is low enough that the body can survive (≈ 100 W of absorbed power for a resting adult).  
Because a perfectly reflecting surface would absorb zero power, the only limitation comes from the fact that *real* materials are never 100 % reflective – there is always a tiny absorptivity α. We will therefore:

1. Write the solar radiative flux as a function of distance from the Sun.  
2. Convert a tolerable absorbed power into a required **maximum flux** using the suit’s absorptivity and its effective area.  
3. Solve for the distance that gives that flux.  

If we truly had α = 0 the answer would be “arbitrarily close”, but we will keep a realistic tiny α to obtain a finite number and illustrate the physics.

---

## 2. Step‑by‑step solution  

### 2.1  Solar radiative flux at a distance *r*  

The Sun radiates as (approximately) a black‑body of temperature \(T_{\odot}=5778\ {\rm K}\).  
Its total power (luminosity) is  

\[
L_{\odot}=4\pi R_{\odot}^{2}\sigma T_{\odot}^{4}=3.846\times10^{26}\ {\rm W},
\]

where  

* \(R_{\odot}=6.96\times10^{8}\ {\rm m}\) – solar radius,  
* \(\sigma =5.670374419\times10^{-8}\ {\rm W\,m^{-2}\,K^{-4}}\) – Stefan‑Boltzmann constant.

At a distance \(r\) from the Sun’s centre the **irradiance** (power per unit area) is the inverse‑square law:

\[
\boxed{F(r)=\frac{L_{\odot}}{4\pi r^{2}} } \qquad\bigl[{\rm W\,m^{-2}}\bigr].
\]

For convenience we can also express it relative to the solar constant at Earth (\(F_{\oplus}=1361\ {\rm W\,m^{-2}}\)):

\[
F(r)=F_{\oplus}\left(\frac{1\ {\rm AU}}{r}\right)^{2},
\]
with \(1\ {\rm AU}=1.496\times10^{11}\ {\rm m}\).

---

### 2.2  How much absorbed power can a human tolerate?  

A resting adult produces about \(100\ {\rm W}\) of metabolic heat.  
To stay alive we must keep the **additional absorbed power** from the Sun at or below that value; otherwise the core temperature would rise too quickly.

So we set the tolerable absorbed power  

\[
P_{\text{tol}} = 100\ {\rm W}.
\]

---

### 2.3  Relating absorbed power to the suit’s properties  

Let  

* \(A\) = effective projected area of the astronaut+ suit that faces the Sun (≈ 2 m² for a standing person).  
* \(\alpha\) = **absorptivity** of the suit (fraction of incident radiation that is actually absorbed).  
  *Perfect reflection* would mean \(\alpha=0\).  
  In practice the best reflective coatings in the visible/IR have \(\alpha\) of order \(10^{-6}\) (reflectivity 99.9999 %).  

The absorbed power is

\[
P_{\text{abs}} = \alpha \, A \, F(r).
\]

Setting \(P_{\text{abs}} = P_{\text{tol}}\) gives the **maximum allowable flux**:

\[
F_{\max}= \frac{P_{\text{tol}}}{\alpha A}.
\tag{1}
\]

---

### 2.4  Choose a realistic absorptivity  

Even the most advanced multilayer dielectric mirrors (used on solar sails) have \(\alpha \sim 10^{-6}\)–\(10^{-7}\) over the whole solar spectrum.  
We will use the optimistic value

\[
\boxed{\alpha = 1\times10^{-6}} .
\]

With \(A = 2\ {\rm m^{2}}\) and \(P_{\text{tol}} = 100\ {\rm W}\),

\[
F_{\max}= \frac{100}{(1\times10^{-6})(2)} = 5.0\times10^{7}\ {\rm W\,m^{-2}}.
\tag{2}
\]

---

### 2.5  Solve for the distance *r* that yields this flux  

Set the solar flux (eq. 2) equal to the inverse‑square law:

\[
F_{\oplus}\left(\frac{1\ {\rm AU}}{r}\right)^{2}=5.0\times10^{7}\ {\rm W\,m^{-2}}.
\]

Insert numbers (\(F_{\oplus}=1361\ {\rm W\,m^{-2}}\)):

\[
\left(\frac{1\ {\rm AU}}{r}\right)^{2}= \frac{5.0\times10^{7}}{1361}
\;\;\Longrightarrow\;\;
\frac{1\ {\rm AU}}{r}= \sqrt{3.6748\times10^{4}} = 1.918\times10^{2}.
\]

Hence  

\[
r = \frac{1\ {\rm AU}}{1.918\times10^{2}}
   = \frac{1.496\times10^{11}\ {\rm m}}{191.8}
   \approx 7.8\times10^{8}\ {\rm m}.
\]

Recall that the solar radius is \(R_{\odot}=6.96\times10^{8}\ {\rm m}\).  
The **height above the photosphere** is therefore

\[
h = r - R_{\odot}
   \approx 7.8\times10^{8}\ {\rm m} - 6.96\times10^{8}\ {\rm m}
   \approx 8.4\times10^{7}\ {\rm m}
   = 8.4\times10^{4}\ {\rm km}.
\]

---

### 2.6  Interpretation  

* With an *ideal* perfectly reflective suit (\(\alpha=0\)) the absorbed power would be zero at any distance, so **theoretically you could get arbitrarily close to the Sun’s surface and still survive** (ignoring mechanical stresses, radiation pressure, etc.).  

* In a *realistic* ultra‑reflective suit with \(\alpha = 10^{-6}\) you could approach to within **≈ 8 × 10⁴ km above the photosphere**—roughly one‑tenth the Sun’s radius, or about one‑quarter the Earth–Moon distance—while keeping the extra heat load to ≤ 100 W.

* If the absorptivity were ten times larger (α = 10⁻⁵) the safe altitude would increase by √10, to about 2.6 × 10⁵ km. Conversely, improving α by a factor of ten pushes the safe altitude down by √10.

---

## 3. Final answer  

- **Perfectly reflective (α = 0)**: no radiative heating, so in principle you could get arbitrarily close to the Sun’s surface and still survive for an hour (subject to other non‑thermal hazards).

- **Practically achievable reflectivity (α ≈ 10⁻⁶)**: the maximum tolerable absorbed power (≈ 100 W) limits you to a distance of  

\[
\boxed{r \;\approx\; 7.8\times10^{8}\ {\rm m}\;( \;h\approx 8.4\times10^{4}\ {\rm km\ above\ the\ photosphere}\;)}.
\]

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the solar flux as constant** (using 1361 W m⁻² everywhere) | The Sun’s intensity follows an inverse‑square law; it grows dramatically near the Sun. | Write \(F(r)=F_{\oplus}(1\ {\rm AU}/r)^{2}\) before plugging numbers. |
| **Assuming a perfectly reflective surface absorbs *nothing* without mentioning absorptivity** | No real material has α = 0; even the best mirrors absorb a tiny fraction, which matters because the flux is huge. | Introduce an explicit absorptivity α and keep it in the equations. |
| **Neglecting the projected area** | Power absorbed is proportional to the area facing the Sun. Using the wrong area leads to an order‑of‑magnitude error. | Use a realistic estimate (≈ 2 m² for a person) and keep the factor in the calculation. |
| **Forgetting to compare absorbed power to a physiological limit** | The question is about “survive for an hour”; you need a sensible limit (≈ 100 W) rather than an arbitrary temperature. | State the tolerable power (or temperature rise) and set \(P_{\text{abs}}=P_{\text{tol}}\). |
| **Ignoring other hazards** (radiation pressure, solar wind, tidal forces) | These become significant extremely close to the Sun, but they are secondary to the radiative heating problem asked. | Mention them qualitatively, but keep the quantitative analysis focused on radiative heat balance. |

---

*Original question: [How close could you get to the Sun and survive in a perfectly reflective spacesuit?](https://physics.stackexchange.com/questions/876900/how-close-could-you-get-to-the-sun-and-survive-in-a-perfectly-reflective-spacesu) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
