---
layout: question
title: Understanding how gas flow condition inside a pipe influences the response
  of a flow sensor
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Understanding how gas flow condition
  inside a pipe influences the response of a flow sensor'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the problem is really asking  

A small MEMS mass‑flow sensor is glued on a PCB that sits in the centre of a 5 cm‑diameter, 40 cm‑long PVC pipe.  
Air is drawn through the pipe by a fan placed at end **A** (the “suction” side). The PCB is about 4 cm from the opposite end **B** (the “inlet” side).  

When the lower half of the pipe’s inlet (the region right at **B**) is **covered with tape**, the sensor works normally.  
When that tape is removed (the inlet is completely open), the sensor stops giving any output.

> **Why does covering half of the inlet change the sensor’s response?**  
> Is the effect only due to a change in the average air speed, or does something else (velocity profile, turbulence, pressure distribution, etc.) also play a role?

The answer must explain, step by step, the fluid‑dynamic reasons why the sensor sees a usable flow only when the lower half of the inlet is blocked.

---

## 2. Step‑by‑step analysis  

### 2.1. Geometry and basic numbers  

| Quantity | Symbol | Value (typical) |
|----------|--------|-----------------|
| Pipe inner diameter | \(D\) | 5 cm = 0.050 m |
| Pipe cross‑sectional area | \(A\) | \(\displaystyle A=\frac{\pi D^{2}}{4}=1.96\times10^{-3}\;{\rm m^{2}}\) |
| Length of pipe | \(L\) | 0.40 m |
| Distance of sensor from inlet B | \(x\) | 0.04 m (≈ 4 cm) |
| Air density (room temperature) | \(\rho\) | 1.2 kg m⁻³ |
| Dynamic viscosity of air | \(\mu\) | \(1.8\times10^{-5}\) Pa·s |
| Fan‑generated volume flow (order of magnitude) | \(Q\) | 1 L s⁻¹ = \(1.0\times10^{-3}\) m³ s⁻¹ (typical small brushless fan) |
| Corresponding average velocity (unblocked pipe) | \(v_{\text{avg}}\) | \(\displaystyle v_{\text{avg}}=\frac{Q}{A}\approx0.51\;{\rm m\,s^{-1}}\) |

> **Note:** The exact flow rate is not given, but a typical tabletop fan produces a few hundred cm³ s⁻¹ to a few litres s⁻¹, so the numbers above are a reasonable starting point.

---

### 2.2. Flow regime in the pipe  

The Reynolds number for pipe flow is  

\[
\mathrm{Re}= \frac{\rho v D}{\mu}
\]

Using the average velocity above:

\[
\mathrm{Re}\_{\text{unblocked}}\; \approx\; \frac{(1.2)(0.51)(0.05)}{1.8\times10^{-5}}
\; \approx\; 1.7\times10^{3}
\]

* This is **laminar** (Re < 2300).  

If the effective flow area is halved (see §2.4), the velocity roughly doubles, giving  

\[
\mathrm{Re}\_{\text{blocked}}\; \approx\; 3.4\times10^{3}
\]

* This pushes the flow into the **transitional / low‑turbulent** regime.

Thus the presence or absence of the tape changes not only the magnitude of the velocity but also the *type* of flow (laminar ↔ turbulent).

---

### 2.3. What the MEMS sensor actually measures  

The sensor works on a **thermal time‑of‑flight (TOF) principle**:

1. A short heating pulse is applied to the **upstream** platinum resistor.  
2. The heated air parcel is carried downstream by the bulk flow.  
3. The **downstream** resistor detects the arriving temperature rise.  
4. The delay \(\Delta t\) between heating and detection is converted to an average velocity  

\[
v_{\text{TOF}} = \frac{L_{\text{sensor}}}{\Delta t}
\]

where \(L_{\text{sensor}}\) is the spacing (≈ 0.5 mm–1 mm) between the two suspended structures.

**Key requirement:** the heated parcel must be *advected* downstream faster than it can spread by molecular diffusion. Otherwise the temperature rise is smeared out and the downstream resistor sees almost no distinct pulse.

The characteristic **convective‑to‑diffusive** ratio is the **Péclet number**

\[
\mathrm{Pe}= \frac{v L_{\text{sensor}}}{\alpha}
\]

with \(\alpha\) the thermal diffusivity of air (≈ 2.2 × 10⁻⁵ m² s⁻¹).  
For a detectable signal we typically need \(\mathrm{Pe}\gtrsim 5\).

Using the average velocity for the unblocked pipe:

\[
\mathrm{Pe}\_{\text{unblocked}} = \frac{0.51\;(1\times10^{-3})}{2.2\times10^{-5}} \approx 23
\]

That *looks* large enough, but two hidden factors reduce the effective velocity that reaches the downstream sensor:

* **Velocity profile** – near the centre of a laminar pipe the velocity is highest; close to the wall it goes to zero. If the sensor sits near the centre, it sees the centre velocity; if it is slightly off‑centre it can see a much smaller local speed.  
* **Recirculation / dead‑zone** – at low Re and in a short pipe the flow may not be fully developed; a large portion of the inlet cross‑section can form a **stagnation zone** that swirls back toward the inlet. In that zone the net axial velocity is near zero, so the thermal pulse never reaches the downstream resistor.

Consequently, even though the *average* \(\mathrm{Pe}\) is > 1, the **local** Péclet number at the sensor location can be far below the detection threshold when the inlet is completely open.

---

### 2.4. Effect of covering the lower half of the inlet  

#### 2.4.1. Simple continuity argument  

When the lower half of the inlet is taped, the **effective flow area** at the entrance becomes roughly

\[
A_{\text{eff}} \approx \frac{1}{2}A = 9.8\times10^{-4}\;{\rm m^{2}}
\]

Because the fan’s pressure head is essentially unchanged (the fan is a **constant‑pressure source** for a small pipe), the volumetric flow \(Q\) remains almost the same, so the **average velocity at the inlet** doubles:

\[
v_{\text{inlet}} \approx 2\,v_{\text{avg}} \;\approx\; 1.0\;{\rm m\,s^{-1}}
\]

The **Reynolds number** now rises to ~3 × 10³, i.e. the flow becomes transitional/turbulent. Turbulent flow mixes the core and wall regions, flattening the velocity profile and removing the low‑speed “dead‑zone” that existed in the laminar case.

#### 2.4.2. Formation of a *vena contracta*  

A sudden reduction in cross‑section (the half‑pipe blockage) creates a **vena contracta** just downstream of the blockage. The streamlines converge toward the centre of the open half, producing a **jet‑like** region with a velocity **higher than the simple continuity estimate** (often 1.2–1.5 × the average). The jet is directed upward (because the bottom half is blocked) and passes right over the PCB that is centred in the pipe.

*Result:* the sensor experiences a **locally higher velocity** (perhaps 1.5 m s⁻¹) and a **well‑defined direction** (upward). The Péclet number at the sensor jumps to

\[
\mathrm{Pe}\_{\text{blocked}} \approx \frac{1.5\;(1\times10^{-3})}{2.2\times10^{-5}} \approx 68
\]

comfortably above the detection limit, and the thermal pulse arrives at the downstream resistor as a clear, sharp peak → the sensor outputs a normal flow reading.

#### 2.4.3. Pressure‑gradient effect  

Blocking the lower half also **shifts the pressure distribution** across the pipe cross‑section. The suction side (fan) creates a nearly uniform pressure drop along the pipe; the blocked side, however, sees a higher static pressure because the flow cannot pass there. This pressure gradient pushes the bulk flow **toward the open side**, reinforcing the upward jet. The jet stays stable over the 4 cm distance between the inlet and the sensor.

---

### 2.5. Why the sensor fails when the inlet is fully open  

1. **Low local velocity** – In a fully open, smooth 5 cm pipe at the modest fan pressure, the centreline velocity may be only ~0.5 m s⁻¹, while the region where the sensor sits (a few mm off the centre due to PCB thickness) can be < 0.2 m s⁻¹. The local Péclet number falls below ~10, giving a very weak, broadened thermal pulse that the electronics cannot resolve.

2. **Laminar parabolic profile** – The velocity at the pipe wall is zero. The sensor’s suspended structures extend a few hundred microns into the flow; part of each structure sits in a region of near‑zero speed, diluting the effective advection speed.

3. **Developing flow and recirculation** – The pipe is short (L/D = 8). For laminar entry flow the **developing length** is roughly  

\[
L_{\text{dev}}\approx 0.05\,\mathrm{Re}\,D \approx 0.05\,(1700)\,(0.05) \approx 4.3\;{\rm m}
\]

Because the pipe is far shorter than this, the flow at the sensor location is **not fully developed**; a large portion of the inlet flow still forms a *plug* that slowly spreads to the walls. The resulting **large shear layer** near the walls can generate a weak reverse‑flow region that cancels the downstream temperature signal.

4. **Diffusion dominates** – With such low axial convection, the heated air parcel spreads radially by molecular diffusion before it can travel the ≈ 1 mm distance to the downstream resistor. The downstream resistor therefore measures only the ambient temperature rise (≈ 0 °C) and the TOF algorithm returns “zero flow”.

In short: the **sensor needs a minimum convective transport speed** and a **stable, uni‑directional flow** at its exact location. The unblocked pipe fails to provide either

*Original question: [Understanding how gas flow condition inside a pipe influences the response of a flow sensor](https://physics.stackexchange.com/questions/876759/understanding-how-gas-flow-condition-inside-a-pipe-influences-the-response-of-a) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
