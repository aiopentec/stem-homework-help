---
layout: question
title: ONIOM NMR Gaussian 16
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: ONIOM NMR Gaussian 16'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

### 1. Restate What’s Being Asked

The student is trying to run an ONIOM-based NMR shielding calculation in Gaussian 16 (e.g., `# nmr=giao oniom(...)`) and encounters an error stating that the NMR calculation has not completed. They want to know why this happens and if they need to explicitly restrict the NMR calculation to specific atoms (such as the high-layer atoms) to make it work.

---

### 2. Step-by-Step Solution

#### Step A: Understand Gaussian’s Limitations with ONIOM Property Calculations
In Gaussian, property calculations—specifically analytical frequencies, NMR shielding tensors, and certain electric-field-dependent properties—are not natively implemented for arbitrary multi-layer ONIOM models in a single combined step via the standard `# nmr` keyword. 

When you submit a job like `# nmr=giao oniom(...)`, Gaussian attempts to run an analytical or numerical derivative calculation on the total ONIOM energy. However, the energy expression in ONIOM depends on combinations of different model chemistries across layers (Real/Low, Model/Low, Model/High), and **Gaussian 16 does not support direct analytical NMR property calculations for standard two- or three-layer ONIOM energy expressions.** 

#### Step B: Address the Student's Question ("Do I need to specify to only calculate magnetic shieldings for the high-layer atoms?")
Specifying a subset of atoms for the NMR calculation does not bypass the fundamental limitation. The route card parser in Gaussian 16 will still reject the combination of the `NMR` keyword directly acting on an `ONIOM` energy job because the required coupled-perturbed Kohn-Sham (CPKS) equations for the mixed ONIOM layers are not coded into the standard property evaluation modules.

#### Step C: Determine the Correct Workaround
If you need NMR shieldings for a system partitioned via ONIOM, you cannot do it with a single Gaussian command line like `# nmr oniom(...)`. Instead, you must use one of two standard workarounds:

1. **Extract the High-Layer Geometry and Run a Standard NMR Job:**
   * Run your ONIOM geometry optimization to get the optimized geometry.
   * Extract the coordinates of the **high-layer atoms** (along with any necessary capping/link atoms if bonds cross the boundary).
   * Run a standard, non-ONIOM NMR calculation (`# b3lyp/6-31g(d) nmr=giao`) on just that isolated high-layer subsystem. This is the most common approach because high layers are typically chosen to be the region of primary chemical interest where you want accurate NMR shifts.

2. **Use Numerical Derivatives (Finite Field Method) / External Scripts:**
   * For advanced users, NMR shieldings can theoretically be obtained numerically by applying finite electric fields, though this is rarely practical for routine molecular systems compared to extracting the core region.

---

### 3. Final Answer

You **cannot** directly run an NMR calculation on an ONIOM job using a command like `# nmr=giao oniom(...)` in Gaussian 16 because **Gaussian does not support analytical NMR property calculations for ONIOM energy expressions**. Furthermore, restricting the calculation to high-layer atoms via input syntax will not resolve the underlying lack of coded CPKS derivatives for ONIOM.

**To solve this problem:**
1. Optimize your geometry using your ONIOM setup (`# opt oniom(...)`).
2. Extract the coordinates of the **high-layer atoms** (and any associated link atoms) from the resulting output.
3. Submit a separate, standard single-point NMR calculation on that extracted high-layer subsystem using the high-layer method (e.g., `# b3lyp/6-31g nmr=giao`).

---

### 4. Common Mistakes for This Problem Type

* **Mixing Property Keywords with ONIOM:** Assuming that because energy, gradients (geometry optimization), and frequencies work under ONIOM, *all* other Gaussian keywords (like `nmr`, `polar`, `druck`, etc.) will automatically work the same way.
* **Ignoring Link Atoms:** When extracting the high-layer subsystem to run a separate NMR calculation, failing to account for the hydrogen link atoms (or standard capping atoms) that Gaussian automatically inserts at ONIOM layer boundaries, which leads to dangling valencies and erroneous electronic structures.
* **Overcomplicating the Route Card:** Trying to use internal syntax modifiers or atom-selection options within the `NMR` keyword to force Gaussian to read the ONIOM layers, rather than recognizing that the calculation must be decoupled into a geometry step followed by a property step on the isolated region.

*Original question: [ONIOM NMR Gaussian 16](https://chemistry.stackexchange.com/questions/196132/oniom-nmr-gaussian-16) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
