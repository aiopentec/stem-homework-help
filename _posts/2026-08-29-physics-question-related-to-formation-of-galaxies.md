---
layout: question
title: Question related to formation of galaxies
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Question related to formation of galaxies'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What is being asked?  

The student is asking:

> *“Is there any modern scientific theory that can confirm the explanation of galaxy formation given in *Science of Time and the Theory of Everything* (Bhausaheb Bhosle, based on the ancient text *Surya‑Siddhanta*)?  If we use the information supplied in that book, can we calculate the result and compare it with observations?”*  

In plain language the question is:

*“Do any accepted physical theories reproduce the galaxy‑formation story described in that book, and can we work out the numbers to see whether it matches what astronomers observe?”*  

---

## 2. Step‑by‑step analysis  

Below is a systematic way to address any claim about how galaxies form, whether it comes from a modern textbook, an ancient manuscript, or a popular‑science book.

### Step 1 – Identify the *explicit* physical ingredients that the claim uses  

| Typical ingredient in a galaxy‑formation model | What the claim must specify |
|-----------------------------------------------|------------------------------|
| Initial conditions (density fluctuations, temperature, composition) | amplitude of perturbations, matter‑radiation ratio, etc. |
| Governing equations (gravity, hydrodynamics, radiation) | Newton/Einstein gravity, Navier–Stokes, radiative transfer |
| Contents of the Universe (dark matter, dark energy, baryons, neutrinos) | fractions Ω<sub>dm</sub>, Ω<sub>b</sub>, Ω<sub>Λ</sub> |
| Timeline (age of the Universe, redshift of key events) | numerical values for when “first galaxies” appear |
| Physical processes (cooling, star formation, feedback, mergers) | cooling functions, star‑formation efficiency, supernova/AGN feedback |

**Action:** Write down every number, equation, or qualitative rule that the book supplies. If the book does **not** give any of the above, the claim cannot be turned into a calculable model.

### Step 2 – Translate those ingredients into the standard cosmological framework  

The current, widely‑tested framework is the **ΛCDM (Lambda‑Cold‑Dark‑Matter) model**. Its core equations are:

1. **Friedmann equation** (expansion of the Universe)  

   \[
   H^{2}(z)=H_{0}^{2}\big[\,\Omega_{\rm m}(1+z)^{3}
   +\Omega_{\rm r}(1+z)^{4}
   +\Omega_{\Lambda}\big],
   \]

   where \(H(z)\) is the Hubble parameter at redshift \(z\).

2. **Linear growth of density perturbations**  

   \[
   \ddot\delta +2H\dot\delta -4\pi G\bar\rho_{\rm m}\,\delta =0,
   \]

   whose solution gives the growth factor \(D(z)\).

3. **Press–Schechter (or modern Sheth–Tormen) halo mass function** – predicts the number density of dark‑matter haloes of mass \(M\) at a given redshift:

   \[
   \frac{{\rm d}n}{{\rm d}M}(M,z)=\sqrt{\frac{2}{\pi}}\,
   \frac{\bar\rho_{\rm m}}{M}\,
   \frac{\delta_{\rm c}}{\sigma(M,z)}\,
   \left|\frac{{\rm d}\ln\sigma}{{\rm d}\ln M}\right|
   \exp\!\Big[-\frac{\delta_{\rm c}^{2}}{2\sigma^{2}(M,z)}\Big].
   \]

   Here \(\sigma(M,z)\) is the rms fluctuation of the density field filtered on scale \(M\); \(\delta_{\rm c}\simeq1.686\).

4. **Baryonic physics** (cooling, star formation, feedback) are added through semi‑analytic recipes or full hydrodynamic simulations (e.g., Illustris, EAGLE, TNG).

**Action:** Map the book’s numbers onto these equations. For example, if the book says “the Universe began with a uniform sphere of radius \(R_0\) and density \(\rho_0\)”, compute \(\Omega_{\rm m}\) and the corresponding \(H_0\) using the Friedmann equation. If it gives a “critical mass for a galaxy” of \(10^{11}M_\odot\), see whether that mass appears with the right abundance in the Press–Schechter formula at the stated epoch.

### Step 3 – Perform a concrete calculation  

Below is a **template** calculation that can be filled in with any numerical values the book supplies.

| Quantity | Formula (ΛCDM) | What you need from the book | Example (using Planck 2018 values) |
|----------|----------------|-----------------------------|------------------------------------|
| Age of Universe today, \(t_0\) | \(\displaystyle t_0 = \int_{0}^{\infty}\frac{dz}{(1+z)H(z)}\) | \(H_0\) and \(\Omega\)s | \(t_0\approx13.8\) Gyr |
| Redshift of first galaxy formation, \(z_{\rm f}\) | – | Stated redshift or time | If \(z_{\rm f}=10\), \(t(z_{\rm f})\approx0.5\) Gyr |
| Typical halo mass at \(z_{\rm f}\) | Use Press–Schechter to get \(M_{\star}(z_{\rm f})\) where \(\sigma(M_{\star})=\delta_c/D(z_{\rm f})\) | Desired mass (e.g., \(10^{11}M_\odot\)) | At \(z=10\), \(M_{\star}\sim10^{9}M_\odot\) (much smaller) |
| Stellar mass‑to‑halo‑mass ratio | Empirical relation \(M_\star/M_{\rm halo}\approx0.01\) for \(M_{\rm halo}\sim10^{11}M_\odot\) | Any claimed ratio | Gives \(M_\star\approx10^{9}M_\odot\) |

**Procedure**  

1. **Insert the book’s numbers** into the left‑hand column.  
2. **Compute** the right‑hand side using a calculator or a simple script.  
3. **Compare** the result with the observational benchmarks (e.g., galaxy stellar mass functions at the quoted redshift, Hubble‑deep‑field counts).

If the book does **not** provide the necessary numerical inputs, the calculation cannot be completed; the claim remains *qualitative*.

### Step 4 – Compare with observations  

Key observational tests for any galaxy‑formation scenario are:

| Observation | What it measures | Typical ΛCDM prediction |
|-------------|------------------|--------------------------|
| Galaxy luminosity/stellar‑mass function (z≈0–10) | Number density vs. mass | Matches Schechter function with faint‑end slope ≈‑1.4 |
| Cosmic microwave background (CMB) anisotropies | Initial density perturbation spectrum (P(k)) | Nearly scale‑invariant (n≈0.965) |
| Large‑scale structure (BAO, clustering) | Spatial distribution of galaxies | Correlation function with BAO peak at ~150 Mpc |
| Rotation curves of spiral galaxies | Dark‑matter halo profiles | Flat curves ⇒ Navarro‑Frenk‑White (NFW) profile |

**Action:** After performing the calculation, ask: *Does the predicted number of galaxies of mass \(M\) at redshift \(z\) agree with the observed mass function?* If the answer is “no”, the theory is not supported by data.

### Step 5 – Decide whether the claim is confirmed  

- **If** the book’s quantitative predictions **exactly reproduce** the ΛCDM results *and* those results match observations → the claim is **consistent** (though it would be a coincidence that an ancient text anticipated modern cosmology).  
- **If** the predictions **differ** (e.g., galaxy formation at age < 10 Myr, or without dark matter) → the claim is **not supported** by current evidence.  

---

## 3. Final answer  

**There is currently no accepted scientific theory that confirms the galaxy‑formation description given in *Science of Time and the Theory of Everything* based on *Surya‑Siddhanta*.**  

The standard, observationally verified framework is the **ΛCDM cosmology** combined with hierarchical structure formation. Using the ΛCDM equations (Friedmann expansion, linear growth, Press–Schechter halo mass function, and baryonic cooling/feedback recipes) one can compute the expected timing, masses, and abundances of galaxies. All of these predictions have been **extensively tested** against observations (CMB, deep‑field galaxy surveys, large‑scale structure) and are **in agreement** to within a few percent.

Unless the book provides explicit, numerically testable statements that can be mapped onto the ΛCDM equations and shown to reproduce the observed galaxy population, its explanation remains **unverified** by modern physics. In practice, the information supplied in the cited work is qualitative and does not contain the necessary parameters (e.g., density fluctuation spectrum, matter/energy fractions, cooling rates) to perform a rigorous calculation. Consequently, no contemporary astrophysical theory confirms the book’s narrative.

---

## 4. Common mistakes when evaluating unconventional galaxy‑formation claims  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming “qualitative similarity” means “quantitative confirmation.”** | A story that *sounds* like “matter clumps together” does not give the precise numbers (mass function, redshift distribution) that observations demand. | Always demand explicit equations and numbers; then test them. |
| **Ignoring the role of dark matter.** | Modern observations (rotation curves, CMB, lensing) require a non‑baryonic matter component; any model that omits it cannot match data. | Check whether the claim includes a dark‑matter analogue; if not, it cannot reproduce the measured dynamics. |
| **Treating the age of the Universe as a free parameter.** | The age is tightly constrained by the CMB (≈13.8 Gyr). Claims of a much younger or older Universe clash with many independent measurements. | Compare the claimed age with the Friedmann integral using the supplied \(H_0\) and \(\Omega\) values. |
| **Using “order‑of‑magnitude” arguments without error analysis.** | Galaxy formation spans many orders of magnitude; a rough estimate can be off by factors of 10⁴–10⁶, which is fatal when comparing to observed number densities. | Propagate uncertainties and see whether the result lies within the observational error bars. |
| **Equating “scriptural description” with a scientific model.** | Religious or mythological language is not constrained by empirical testing and often lacks falsifiable predictions. | Translate any scriptural statement into testable physics; if it cannot be done, it remains outside the scientific domain. |

By following the systematic steps above and avoiding these pitfalls, one can objectively decide whether any proposed galaxy‑formation scenario—whether from a modern textbook or an ancient manuscript—holds up to the rigorous standards of contemporary astrophysics.

*Original question: [Question related to formation of galaxies](https://physics.stackexchange.com/questions/875480/question-related-to-formation-of-galaxies) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
