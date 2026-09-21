---
layout: question
title: What percentage of NaCl in water will freeze at -10 C?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: What percentage of NaCl in water will
  freeze at -10 C?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the problem is really asking  

We are asked: **How much sodium‑chloride must be dissolved in water so that the solution begins to freeze at –10 °C?**  

In other words, we need the composition (mass % NaCl) of a water‑salt solution whose **freezing point** is –10 °C.  
(The “percentage” can be expressed either as  

* mass of salt ÷ mass of water (g NaCl / g H₂O)  

or  

* mass of salt ÷ total mass of solution (g NaCl / (g NaCl + g H₂O)).  

Both are given, because they differ by a factor of \(\frac{1}{1+\text{mass % of water}}\).)

---

## 2. Step‑by‑step solution  

### 2.1. Use the freezing‑point‑depression relation  

For dilute electrolyte solutions the freezing point depression is well described by  

\[
\Delta T_f = i\,K_f\,m
\]

where  

* \(\Delta T_f\) = depression of the freezing point (°C)  
* \(i\) = van’t Hoff factor (number of particles the solute produces). For NaCl, \(i \approx 2\) because it dissociates into Na⁺ and Cl⁻.  
* \(K_f\) = cryoscopic constant of water = **1.86 °C·kg mol⁻¹**  
* \(m\) = **molality** of the solution (mol solute · kg⁻¹ solvent)

We want the solution to start freezing at \(-10\;^{\circ}\text{C}\). Pure water freezes at \(0\;^{\circ}\text{C}\), so  

\[
\Delta T_f = 0 - (-10) = 10\;^{\circ}\text{C}
\]

Insert the numbers and solve for the required molality:

\[
\begin{aligned}
10 &= (2)(1.86)\,m \\
m &= \frac{10}{2 \times 1.86}
   = \frac{10}{3.72}
   = 2.688\;\text{mol kg}^{-1}
\end{aligned}
\]

Thus **2.688 mol of NaCl per kilogram of water** will depress the freezing point to –10 °C.

---

### 2.2. Convert molality to mass of NaCl  

Molar mass of NaCl  

\[
M_{\text{NaCl}} = 22.99 + 35.45 = 58.44\;\text{g mol}^{-1}
\]

Mass of NaCl needed per kilogram (1000 g) of water:

\[
\begin{aligned}
m_{\text{NaCl}} &= m \times M_{\text{NaCl}} \\
                &= 2.688\;\frac{\text{mol}}{\text{kg}}\times 58.44\;\frac{\text{g}}{\text{mol}}\\
                &= 157.2\;\text{g}
\end{aligned}
\]

So **≈ 157 g of NaCl per 1000 g of water** gives a freezing point of –10 °C.

---

### 2.3. Express the result as a percentage  

| Definition | Calculation | Result |
|------------|-------------|--------|
| **% ( NaCl / water )** (mass of salt ÷ mass of water) | \(\displaystyle \frac{157.2\;\text{g}}{1000\;\text{g}}\times100\) | **15.7 % (w/w of water)** |
| **% ( NaCl / solution )** (mass of salt ÷ total mass) | \(\displaystyle \frac{157.2}{1000+157.2}\times100\) | **13.6 % (w/w of solution)** |

Both numbers are correct; they just use different reference bases.  
The value that is most often quoted in tables and handbooks is the **solution‑mass percentage**: **≈ 13–14 % NaCl by mass**.

---

### 2.4. Why the simple equation works here  

The linear freezing‑point‑depression equation is exact only for *ideal* dilute solutions.  
For NaCl‑water, deviations become noticeable above ~20 % w/w. At ~14 % the error is < 1 °C, so the result above (≈ 13.5 % w/w) is accurate enough for practical purposes.  

A more precise value can be read from an experimental phase diagram (e.g., the one you found). The diagram shows that a liquid of about **14 % NaCl (solution mass)** has a liquidus line intersecting the temperature –10 °C, confirming our calculation.

---

## 3. Final answer  

- **Mass of NaCl needed:** ≈ 157 g per 1 kg (1000 g) of water.  
- **Expressed as a percentage:**  

  * **15.7 % NaCl / water** (salt mass divided by water mass)  

  * **13.6 % NaCl / solution** (salt mass divided by total mass)  

Thus, a solution that is **about 14 % NaCl by total mass** (or **≈ 16 % relative to the water mass**) will start to freeze at –10 °C.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|--------|----------------|-----------------|
| **Using the simple formula and forgetting the van’t Hoff factor** (i = 2 for NaCl) | Leads to a molality half the required value, giving a too‑low salt concentration. | Always include \(i\) for electrolytes; for NaCl, \(i≈2\). |
| **Confusing “% w/w” with “% v/v”** | Volume percentages are not appropriate for freezing‑point calculations, which depend on mass (or moles). | Use mass‑based percentages (mass of solute per mass of solvent or per total mass). |
| **Reading the phase diagram incorrectly** (e.g., taking the temperature axis as Celsius when it’s actually Fahrenheit) | Gives a completely wrong concentration. | Verify axis units; most scientific phase diagrams use °C. |
| **Assuming the linear depression equation works at any concentration** | At high concentrations the solution is non‑ideal; the linear relation under‑estimates the required salt. | For concentrations > 20 % w/w, consult experimental data or use activity‑coefficient models. |
| **Reporting the percentage without specifying the reference (water vs. solution)** | The answer can appear contradictory (13 % vs. 16 %). | State clearly whether the percentage is “% NaCl / water” or “% NaCl / solution”. |

Keeping these points in mind will give a reliable estimate of the salt concentration needed for a desired freezing temperature.

*Original question: [What percentage of NaCl in water will freeze at -10 C?](https://chemistry.stackexchange.com/questions/195991/what-percentage-of-nacl-in-water-will-freeze-at-10-c) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
