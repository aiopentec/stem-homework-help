---
layout: post
title: How does Zeeman effect work for sodium spectrum?
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

### 1. Restate What's Being Asked in Plain Language

The student is asking about the polarization states of the spectral lines (specifically the $\pi$ and $\sigma$ components) observed during the **anomalous Zeeman effect** in a sodium atom. 

In the normal Zeeman effect (which occurs in singlet states where total spin $S = 0$), the spectral line splits into three components: one $\pi$ component and two $\sigma$ components, with well-defined polarizations relative to the external magnetic field direction (parallel for $\pi$, perpendicular for $\sigma$). 

The student is looking at the anomalous Zeeman effect for sodium (which involves doublet states where $S = 1/2$, resulting in a more complex splitting pattern) and wants to know: **Do the $\pi$ and $\sigma$ components in the anomalous Zeeman effect retain the exact same polarization meanings (electric field parallel vs. perpendicular to the magnetic field) as they do in the normal Zeeman effect?**

---

### 2. Step-by-Step Solution

To answer this question, we need to examine the quantum mechanics of atomic transitions in a magnetic field, focusing on the change in the magnetic quantum number ($\Delta m_j$) and how it dictates the polarization of emitted light, regardless of whether the splitting is "normal" or "anomalous."

#### Step 1: Understand the Origin of Polarization in Zeeman Splitting
When an atom is placed in a uniform external magnetic field $\vec{B}$ (chosen to lie along the $z$-axis), the spatial degeneracy of the energy levels is lifted. Transitions between these magnetic sublevels obey strict quantum mechanical selection rules for the total angular momentum component along the field axis, $m_j$.

#### Step 2: Review the Selection Rules for $\Delta m_j$
Regardless of whether the Zeeman effect is normal or anomalous, the allowed changes in the magnetic quantum number $m_j$ during a dipole-allowed radiative transition are universally governed by:
* $\Delta m_j = 0$
* $\Delta m_j = \pm 1$

These $\Delta m_j$ values correspond directly to the physical oscillation directions of the transition dipole moment (and therefore the electric field vector $\vec{E}$ of the emitted photon) relative to the quantization axis (the external magnetic field $\vec{B}$).

#### Step 3: Connect $\Delta m_j$ to $\pi$ and $\sigma$ Components
We classify the components based on $\Delta m_j$:
1. **$\Delta m_j = 0$ ($\pi$ components):**
   * These transitions correspond to an oscillating electric dipole parallel to the magnetic field ($\vec{E} \parallel \vec{B}$). 
   * An observer looking perpendicular to the magnetic field sees linearly polarized light whose electric vector oscillates parallel to the magnetic field.
2. **$\Delta m_j = \pm 1$ ($\sigma$ components):**
   * These transitions correspond to circular or elliptical motion in the plane perpendicular to the magnetic field, producing an electric field component perpendicular to the magnetic field ($\vec{E} \perp \vec{B}$).
   * An observer looking perpendicular to the magnetic field sees linearly polarized light whose electric vector oscillates perpendicular to the field.

#### Step 4: Apply to Sodium (Anomalous Zeeman Effect)
In sodium, the yellow D-lines arise from transitions between $2P_{3/2}, 2P_{1/2}$ and $2S_{1/2}$ states. Because electron spin is involved ($S = 1/2$), the Landé $g$-factor is not $1$ (it is $4/3$ for $2P_{3/2}$, $2/3$ for $2P_{1/2}$, and $2$ for $2S_{1/2}$). This causes a more complicated multi-line splitting pattern (anomalous Zeeman effect) rather than a simple triplet.

However, **the physical mechanism of light emission and the interaction of the atomic dipole with the magnetic field remain fundamentally identical.** Every single spectral line in the anomalous Zeeman pattern still originates from a transition obeying $\Delta m_j = 0$ or $\Delta m_j = \pm 1$. 

Therefore, the labels $\pi$ and $\sigma$ retain their exact standard definitions:
* **$\pi$ components** always arise from $\Delta m_j = 0$ and have their electric vector **parallel** ($\parallel$) to the magnetic field.
* **$\sigma$ components** always arise from $\Delta m_j = \pm 1$ and have their electric vector **perpendicular** ($\perp$) to the magnetic field.

---

### 3. Final Answer

**Yes, you can safely assume this.** 

The polarization meanings of the $\pi$ and $\sigma$ components are universal across both the normal and anomalous Zeeman effects. In the anomalous Zeeman effect for sodium (and all other atoms), **$\pi$ components** strictly correspond to transitions where $\Delta m_j = 0$ and the electric field is **parallel** ($\parallel$) to the applied magnetic field. **$\sigma$ components** strictly correspond to transitions where $\Delta m_j = \pm 1$ and the electric field is **perpendicular** ($\perp$) to the applied magnetic field. Only the *number* of components and their spacing change due to differing $g$-factors; the polarization geometry relative to the magnetic field axis does not change.

---

### 4. Common Mistakes

* **Assuming anomalous means different physics:** Students often think that because the splitting pattern is "anomalous" (more than 3 lines), the fundamental selection rules or polarization properties must also be anomalous or reversed. In reality, "anomalous" is just a historical term for a doublet/multiplet splitting where $S \neq 0$; the quantum mechanical origins of polarization remain identical.
* **Confusing view direction with polarization:** The labels $\pi$ ($\parallel$) and $\sigma$ ($\perp$) describe the direction of the electric field vector relative to the magnetic field vector, *regardless* of whether you are viewing the source longitudinally (along the field) or transversely (perpendicular to the field). 
* **Mixing up $\Delta m_j$ values:** Believing that $\Delta m_j = 0$ gives perpendicular polarization. Always remember: $\Delta m_j = 0$ is parallel ($\pi$), and $\Delta m_j = \pm 1$ is perpendicular ($\sigma$).

*Original question: [How does Zeeman effect work for sodium spectrum?](https://chemistry.stackexchange.com/questions/181267/how-does-zeeman-effect-work-for-sodium-spectrum) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
