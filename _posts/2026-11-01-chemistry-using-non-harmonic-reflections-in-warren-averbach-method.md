---
layout: question
title: Using Non-Harmonic reflections in warren averbach method
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Using Non-Harmonic reflections in warren
  averbach method'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

### 1. Restate the Problem in Plain Language
You are analyzing X-ray diffraction (XRD) data for Hydroxyapatite (HAp) using the Warren-Averbach method to determine crystallite size and microstrain. You want to know two main things:
1. Can you include non-harmonic reflection peaks (peaks that do not belong to the same family of lattice planes, such as mixing $(hkl)$ reflections with different orders like $(100)$ and $(200)$ versus unrelated planes like $(100)$ and $(002)$), or must you stick strictly to harmonic reflections?
2. What are the exact criteria for selecting reflection peaks when setting up a Warren-Averbach analysis?

---

### 2. Step-by-Step Solution

#### Step 1: Understand the Theoretical Basis of the Warren-Averbach Method
The Warren-Averbach (WA) method is a Fourier-based line profile analysis used to separate size broadening from strain broadening. It relies on the Fourier coefficients $A(L)$ of a diffraction peak, which are a product of the size coefficients $A^S(L)$ and the strain coefficients $A^D(L, g)$:

$$A(L) = A^S(L) \cdot A^D(L, g)$$

Where:
* $L$ is the column length normal to the reflecting planes.
* $g$ is the diffraction vector magnitude ($g = 2\sin\theta / \lambda$).

To separate size from strain, the method requires data from **multiple orders of reflection** from the **same crystallographic plane family** (i.e., harmonic reflections).

---

#### Step 2: Answer Part 1 — Can You Use Non-Harmonic Reflections?
**No, you cannot use non-harmonic reflections for the core Warren-Averbach separation.** 

* **Why?** Microstrain broadening is anisotropic (it depends heavily on the crystallographic direction $hkl$) and scales with the diffraction order ($g$). To separate size and strain mathematically, the size contribution $A^S(L)$ must remain constant while the strain contribution $A^D(L, g)$ varies with $g$. 
* If you compare reflections from completely different plane families (non-harmonic, e.g., comparing $\{100\}$ and $\{002\}$), the local elastic constants, dislocation densities, and strain fields are entirely different. Therefore, the assumption that only the $g$-vector magnitude changes while the defect structure remains identical breaks down entirely.

---

#### Step 3: Answer Part 2 — How to Properly Choose Peaks for Warren-Averbach
To execute a successful Warren-Averbach analysis on Hydroxyapatite (or any material), follow these strict selection rules:

1. **Select Harmonic Orders (Orders of the Same Peak):**
   You need at least **two (preferably three or more)** orders of reflection from the same $(hkl)$ family. 
   * *Example for HAp (Hexagonal, $P6_3/m$):* You can use the $(002)$ and $(004)$ peaks, or the $(300)$ and $(600)$ peaks. 

2. **Check for Peak Overlap:**
   Hydroxyapatite has a relatively low crystal symmetry (hexagonal), meaning many peaks overlap closely (e.g., the complex triplet around $2\theta = 30^\circ - 35^\circ$ consisting of $(211), (112), (300)$, etc.). 
   * **Rule:** Do *not* use overlapping peaks unless you perform a rigorous Whole Powder Pattern Fitting (WPPF) or profile deconvolution first to isolate the individual peak shapes.

3. **Account for Instrumental Broadening (Standard):**
   You must measure a strain-free reference standard (like well-annealed $\text{LaB}_6$ or $\text{Si}$) under identical instrumental conditions to subtract instrumental broadening using Stokes Fourier deconvolution before applying the WA method.

4. **Address Anisotropy (If Using Multiple Families):**
   If you want to evaluate microstrain along *different* crystallographic directions (e.g., parallel vs. perpendicular to the $c$-axis in HAp), you must perform *separate* Warren-Averbach analyses on different harmonic sets (e.g., one analysis on $\{002\}-\{004\}$ and a separate analysis on $\{300\}-\{600\}$), and then combine them using anisotropic elasticity models (like the Voigt or Warren-Averbach-Krivoglad approach).

---

### 3. Final Answer
1. **Non-harmonic reflections cannot be mixed** in a single Warren-Averbach calculation because microstrain is crystallographically anisotropic and varies between different plane families.
2. **Peak selection criteria:** You must select **harmonic reflections** (multiple orders of the same $(hkl)$ family, such as $\{002\}$ and $\{004\}$), ensure the peaks are **free from overlap** (or properly deconvoluted), and use an **instrumental standard** to remove optics-related broadening prior to the Fourier analysis.

---

### 4. Common Mistakes
* **Mixing different $hkl$ indices in one plot:** Plotting Fourier coefficients of $(100)$ against $(002)$ assuming they are just different $g$-values. This yields physically meaningless strain values because strain behavior differs drastically along the $a$-axis versus the $c$-axis in anisotropic materials like Hydroxyapatite.
* **Ignoring peak overlap:** Using a peak that has a shoulder or hidden reflection nearby without performing profile fitting, which corrupts the Fourier coefficients.
* **Forgetting instrumental correction:** Applying the Warren-Averbach method directly to raw, as-measured peaks without deconvoluting the instrumental broadening profile, leading to a severe underestimation of crystallite size and overestimation of strain.

*Original question: [Using Non-Harmonic reflections in warren averbach method](https://chemistry.stackexchange.com/questions/196130/using-non-harmonic-reflections-in-warren-averbach-method) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
