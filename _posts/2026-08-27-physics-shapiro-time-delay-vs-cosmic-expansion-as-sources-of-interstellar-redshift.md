---
layout: question
title: Shapiro time delay vs cosmic expansion as sources of interstellar redshift?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Shapiro time delay vs cosmic expansion
  as sources of interstellar redshift?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the student is really asking  

|Student’s wording|What it really means|
|---|---|
|“The radar pulses that passed the Sun took ~200 µs longer than expected.  Does this mean that **the speed of light itself changed** for the observers on Earth?”|If a signal takes longer to go from A to B, does that imply that the *local* speed of the photons was different from the invariant value **c**?|
|“If the speed can change, does Einstein’s 2nd postulate (c is the same in every inertial frame) have to be abandoned?”|Is the post‑postulate falsified by the Shapiro delay?|
|“Should we think of **c** as only a *defined* number, not a physical constant, because gravity and energy everywhere can tweak it?”|Is the constancy of c only a convention, not a law of nature?|
|“Does the Shapiro effect have any bearing on the interpretation of cosmological red‑shift (expansion of the Universe)?”|Can the extra travel time/red‑shift produced by a gravitational field be confused with the red‑shift we attribute to the expanding Universe?|

The answer requires a clear distinction between **(i) the locally measured speed of light**, which is always exactly *c*, and **(ii) the coordinate speed of light** that depends on the choice of space‑time coordinates (e.g., the Sun‑centered Schwarzschild coordinates used to describe the experiment).  

---

## 2. Step‑by‑step explanation  

### 2.1. What the Shapiro delay measures  

1. **Set‑up** – A radio pulse is sent from Earth, skims the Sun at a distance *r* ≈ solar radius, is reflected by a spacecraft (or a planet) and returns to Earth.  
2. **Naïve expectation** – If space were flat and empty, the round‑trip travel time would be  
   \[
   t_{\rm flat}= \frac{2\,L}{c},
   \]  
   where *L* is the (Euclidean) Earth–spacecraft distance.  
3. **Observed result** – The round‑trip time is **longer** by  
   \[
   \Delta t \simeq \frac{2GM_{\odot}}{c^{3}}\,
      \ln\!\Bigl(\frac{4r_{E}r_{S}}{b^{2}}\Bigr) ,
   \]  
   the **Shapiro (gravitational) time delay**, where  
   * *G* – Newton’s constant,  
   * *M\_{\odot}* – mass of the Sun,  
   * *r\_E, r\_S* – distances of Earth and spacecraft from the Sun,  
   * *b* – impact parameter (closest approach).  

   For the Venus experiment *Δt* ≈ 200 µs, for the Cassini‑Saturn experiment *Δt* ≈ 240 µs.  

4. **Physical origin** – In General Relativity (GR) the presence of mass curves space‑time.  Light follows a **null geodesic**, i.e. a path for which the space‑time interval *ds* = 0.  Because the coordinate *t* (the time measured by a distant observer) runs more slowly deeper in the gravitational potential, the coordinate *dt* required to traverse a given coordinate *dr* is larger.  This manifests as an extra travel time when the ray passes near the Sun.

### 2.2. Local vs. coordinate speed of light  

|Quantity|Definition|Value in the Shapiro experiment|
|---|---|---|
|**Locally measured speed**|What an observer *at the point where the photon passes* measures with a ruler and a clock that are both in the same gravitational potential.|Exactly **c** = 299 792 458 m s⁻¹ (by construction of the metric).|
|**Coordinate speed**|Rate *dr/dt* in a chosen set of coordinates (e.g., Schwarzschild coordinates where *t* is the time kept by a far‑away observer).|Slightly **less than c** near the Sun: \(v_{\rm coord}=c\,(1-2GM/rc^{2})\).|

*Why the difference matters*  

- The **postulate** “the speed of light in vacuum is the same in all inertial frames” is a *local* statement. It says that any *freely‑falling* observer (i.e. an observer in an infinitesimally small region where gravity can be ignored) will always measure the speed of a light pulse as *c*.
- The **Shapiro delay** does **not** involve a local measurement of *speed*; it involves the *integrated* coordinate time taken for the photon to travel a macroscopic curved path. The integration of the *slower* coordinate speed over the portion of the path near the Sun yields the extra delay.

Thus the delay **does not contradict** Einstein’s second postulate.

### 2.3. Does the experiment “slow down” the *photon*?  

No. In the local inertial frame of an observer comoving with the photon (or, more realistically, an observer at the same point with a small laboratory), the photon still moves at *c*.  The *elapsed* coordinate time measured by a distant Earth clock is larger because the clock ticks slower in the deeper potential.  The photon’s world‑line is the same null line; only the **coordinate mapping** stretches the time axis.

### 2.4. Is “c is only a defined constant” a valid reinterpretation?  

- In the International System of Units (SI) the meter is *defined* by the value of *c*: **1 m = (1 c s)**.  This definition makes *c* an *exact* number by convention; it is not *measured* each time.
- The *physical constancy* is that **any locally measured speed of light in vacuum equals this exact number**.  GR predicts that in any freely‑falling laboratory, even in the presence of strong gravitational fields, the measured speed will be *c*.  The experiment merely confirms the *gravitational time‑dilation* part of the metric, not a variation of the local speed.

Hence the experimental outcome **supports**, rather than undermines, the idea that *c* is a fundamental constant.

### 2.5. Relation (or lack thereof) to the cosmological red‑shift  

|Phenomenon|Origin|Mathematical form|Observed effect|
|---|---|---|---|
|**Gravitational (Shapiro) delay + red‑shift**|Static space‑time curvature around a mass (Schwarzschild metric).|Frequency shift: \(\displaystyle \frac{\nu_{\rm rec}}{\nu_{\rm em}} = \sqrt{\frac{1-2GM/rc^{2}}{1-2GM/r_{\infty}c^{2}}}\).|Photons climbing out of a potential lose energy → *gravitational red‑shift* (tiny, ≈10⁻⁶ for the Sun).|
|**Cosmological expansion red‑shift**|Dynamical Friedmann‑Lemaître‑Robertson‑Walker (FLRW) metric with a scale factor *a(t)*.|\(\displaystyle 1+z = \frac{a(t_{\rm now})}{a(t_{\rm em})}\).|Photons are stretched as the Universe expands → *Hubble law* (z ≈ H₀ d for nearby objects).|

Key points:

1. **Different metrics** – The Sun’s field is *static*; the Universe’s metric is *time‑dependent*.  The Shapiro effect can be expressed as a *coordinate* delay in a static geometry, while cosmological red‑shift is a *global* scaling of wavelengths over billions of years.  
2. **Magnitude** – Gravitational red‑shift from the Sun is of order 10⁻⁶, whereas typical extragalactic red‑shifts are *z ≈ 0.1–10* (10 % to many hundred percent).  The two are incomparable.  
3. **Observables** – The Cassini experiment measured *phase* changes in the radio carrier, which are interpreted as a *Shapiro‑induced* extra time, **not** as a change of the fundamental cosmic scale factor.

Consequently the Shapiro experiment does **not** provide an alternative explanation for the cosmological red‑shift.  The latter remains best described by the expansion of space (or, equivalently, by the FLRW metric).

---

## 3. Final answers to the three questions  

|Question|Answer (short)|
|---|---|
|**Q1.** Does the observed delay mean the speed of light changed, violating Einstein’s 2nd postulate?|**No.** The locally measured speed of light is always *c*.  The delay is caused by the *coordinate* time running slower in the Sun’s gravitational potential, not by a change in the intrinsic photon speed.|
|**Q2.** Must we abandon the axiom and treat *c* as merely a defined convention because gravity affects it?|**No.** The constancy of *c* is a *local* physical law that holds in all (locally inertial) frames, even in strong fields.  The definition of the meter via *c* reflects this constancy; the experiment confirms the GR prediction of gravitational time dilation, not a failure of the axiom.|
|**Q3.** Does the Shapiro delay/red‑shift undermine the interpretation of cosmic expansion?|**No.** The Shapiro effect is a small, static‑field phenomenon (Δt ∼ 10⁻⁴ s, red‑shift ∼ 10⁻⁶) distinct from the large, dynamic red‑shift caused by the expanding Universe (z ≳ 10⁻²).  The two have different physical origins and are treated with different metrics.|

---

## 4. Common Mistakes (and how to avoid them)

|Mistake|Why it’s wrong|How to avoid it|
|---|---|---|
|**Confusing *coordinate* speed with *local* speed.** Believing the photon “actually slowed down”.|Coordinate speed depends on the choice of time coordinate; it can be < c even though locally the speed is always *c*.|Remember the equivalence principle: in a sufficiently small freely‑falling lab, the metric is locally Minkowskian and the measured speed is exactly *c*.|
|**Claiming the Shapiro delay disproves the constancy of *c*.**|The constancy of *c* is a *local* postulate, not a claim about integrated travel times over curved space‑time.|Write out the null condition \(ds^{2}=0\) in the relevant metric; you will see that it forces the *local* speed to be *c* regardless of the metric components.|
|**Equating the tiny gravitational red‑shift near the Sun with the large cosmological red‑shift.**|They arise from different metrics (static Schwarzschild vs. dynamic FLRW) and differ by many orders of magnitude.|Compare the formulas: gravitational red‑shift ∝ GM/(rc²) ~10⁻⁶, while cosmological z ∝ H₀ d/c for distant galaxies, which can be ≳0.1.|
|**Thinking the experiment measured “c slowed to 299 792 458 m/s – 0.0002 %”.**|The experiment measured *Δt* relative to a Newtonian‑flat‑space prediction, not a change in the fundamental value of *c*.|Recall the SI definition of the metre: the *numerical* value of *c* is exact; the experiment merely tests the GR correction to the *coordinate* time of flight.|
|**Ignoring the role of the observer’s clock.**|Gravitational time dilation means the Earth clock runs at a different rate than a clock near the Sun; forgetting this leads to the impression that the photon took longer because it moved slower.|Write the proper time interval measured by the Earth observer: \(\Delta \tau_{\rm Earth}= (1+Φ/c^{2})\,\Delta t\). The factor (1+Φ/c²) is the source of the extra delay.|
|**Assuming that any “delay” automatically means the vacuum isn’t empty.**|The delay is caused by the curvature of space‑time, not by a medium with refractive index > 1.|Recall that in GR the “vacuum” can still have a curved geometry; the speed of light in that geometry remains *c* locally.|
|**Treating the Shapiro delay as a test of the speed of light rather than of the metric.**|The experiment is a *null‑geodesic* test of the Schwarzschild part of the metric (the \(g_{tt}\) component).|Identify what the measurable quantity is: the round‑trip *phase* of a radio carrier, which depends on the integrated metric coefficient, not on *c* itself.|

---

*Original question: [Shapiro time delay vs cosmic expansion as sources of interstellar redshift?](https://physics.stackexchange.com/questions/875415/shapiro-time-delay-vs-cosmic-expansion-as-sources-of-interstellar-redshift) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
