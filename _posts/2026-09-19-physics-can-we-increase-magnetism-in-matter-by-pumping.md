---
layout: question
title: Can we increase magnetism in matter by pumping?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Can we increase magnetism in matter by
  pumping?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the problem is really asking  

A student proposes the following “pump‑up‑magnetism” scheme  

1. A three‑phase AC motor creates a **rotating magnetic field** (RMF) in the horizontal plane.  
2. A small permanent magnet (PM) is mounted on a friction‑free gimbal so that it can follow the RMF and therefore **spin up** like a compass needle in a rotating field.  
3. The RMF is switched off. A short vertical magnetic pulse is applied, forcing the PM’s magnetic axis to turn vertical.  
4. Because the magnet now has angular momentum from step 2, the sudden re‑orientation is supposed to **add spin** to the electrons that produce the PM’s own magnetisation, i.e. to increase the magnet’s intrinsic magnetic moment (or “magnetic forces”).  

The student asks  

* **Q1.** Is the premise physically sound?  
* **Q2.** If it is, how could the field geometry be altered to make a continuous “pumping’’ possible, avoiding the three difficulties they listed?  

Our job is to examine the idea from first principles, decide whether any net increase of magnetisation is possible, and explain why the suggested modifications cannot succeed.  

---

## 2.  Physics that governs the situation  

### 2.1  Torque on a magnetic dipole in a magnetic field  

A permanent magnet is, to an excellent approximation, a **magnetic dipole** with moment **μ**.  
If it sits in a magnetic field **B**, it experiences a torque  

\[
\boldsymbol{\tau}= \boldsymbol{\mu}\times\mathbf B .
\]

The torque changes the **mechanical** angular momentum **L** of the *rigid body* according to  

\[
\frac{d\mathbf L}{dt}= \boldsymbol{\tau}.
\]

If the field itself is rotating (RMF), the dipole will tend to follow it, and the body can be spun up. Nothing exotic is required – it is exactly how induction motors work.

### 2.2  Relation between magnetic moment and *intrinsic* angular momentum  

For the **electrons** that generate the permanent‑magnetisation, the magnetic moment is tied to their **spin angular momentum**  

\[
\boldsymbol{\mu}_\text{e}= -g\frac{e}{2m_e}\,\mathbf S
          \equiv \gamma_e \,\mathbf S ,
\]

where \(g\approx 2\) and \(\gamma_e\) is the gyromagnetic ratio of the electron.  
Thus **changing the magnetisation of the material means changing the sum of the electron spins**, not the mechanical rotation of the macroscopic piece.

### 2.3  The Barnett and Einstein–de Haas effects  

Two well‑known phenomena connect **macroscopic rotation** and **magnetisation**:

| Effect | What is changed? | Typical magnitude |
|--------|------------------|-------------------|
| **Barnett** (rotation → magnetisation) | A body spun at angular velocity \(\Omega\) acquires a tiny magnetisation \(\mathbf M_{\text{Barnett}} = \chi \frac{\rho}{\gamma_e}\,\boldsymbol{\Omega}\) | For steel, \(\Omega = 10^4\;{\rm rad\,s^{-1}}\) gives \(\mu\) of order \(10^{-9}\) A·m² (≈ 10⁻⁶ % of a usual PM) |
| **Einstein–de Haas** (magnetisation → rotation) | Magnetising a freely suspended ferromagnet makes it rotate in the opposite sense to conserve total angular momentum | The rotation speeds are similarly tiny (≈ 10⁻⁴ rad s⁻¹ for a 1 T magnetisation change) |

These are *real* but **extremely small** because the gyromagnetic ratio of the electron is huge compared with that of a macroscopic object.  

### 2.4  Energy and angular‑momentum bookkeeping  

The total angular momentum of the *combined* system (magnet + electromagnetic field) is conserved:

\[
\mathbf L_{\text{total}} = \mathbf L_{\text{mechanical}} + \mathbf L_{\text{field}} = \text{constant}.
\]

When the rotating field does work on the magnet, the **field loses exactly the same amount of angular momentum** that the magnet gains. Switching the field off simply returns that angular momentum to the external power source (the motor windings). No hidden reservoir of angular momentum is created.

### 2.5  Why a “vertical pulse’’ does **not** increase the intrinsic moment  

During step 3 the student applies a short vertical field pulse, forcing the dipole axis to flip. The pulse exerts a torque that changes the *direction* of **μ**, but the *magnitude* \(|\mu|\) stays the same because the internal electron spins are untouched. The only thing that can change \(|\mu|\) is to **re‑align more electron spins** (e.g. by heating above the Curie point and cooling in a field, or by applying a strong static field for a time comparable to the magnetic relaxation time). A brief pulse does not accomplish this.

---

## 3.  Step‑by‑step analysis of the proposed cycle  

| Step | What actually happens? | Consequence for magnetisation |
|------|------------------------|-------------------------------|
| **A. Rotating field** (four‑pole AC motor) | The dipole feels a torque and starts to spin. Mechanical kinetic energy is supplied by the motor, and the motor’s magnetic field **loses** an equal amount of angular momentum. | No change in \(|\mu|\). |
| **B. Turn field off** | The magnet continues to spin because of its inertia. The electromagnetic angular momentum that was stored in the RMF has already been returned to the power supply when the field was turned off. | Still no change in \(|\mu|\). |
| **C. Apply vertical pulse** | The dipole axis is forced to rotate vertically. The magnet’s body acquires a tiny extra rotation (Barnett effect) but the **electron‑spin** system does not gain net spin; the pulse simply redirects the existing magnetic moment. | \(|\mu|\) unchanged; the only added field is the minuscule Barnett magnetisation proportional to the achieved \(\Omega\). |
| **D. Switch pulse off** | The induced Barnett magnetisation disappears as the body slows down (dissipation). | Returns to original \(|\mu|\). |

**Result:** The cycle can *transfer* angular momentum between the motor, the magnet’s bulk rotation, and the electromagnetic field, but it **cannot increase the intrinsic magnetic moment** of the permanent magnet. At best you obtain an additional field of order \(10^{-9}\) T—far below any practical “increase of magnetic forces”.

---

## 4.  Answer to the two questions  

### 4.1  Is the premise valid?  

**No.**  
The premise confuses two distinct angular momenta:

1. **Mechanical angular momentum** of the whole magnet (the “spinning top” you can see).  
2. **Microscopic spin angular momentum** of the electrons that produce the permanent magnetisation.

The rotating field can only give the first kind. The second kind is quantised and tied to the electron gyromagnetic ratio; it can be altered only by *changing the orientation of the electron spins* (e.g. via domain wall motion, heating above Curie temperature, or by resonant spin‑flip processes). A short magnetic pulse that merely re‑orients the macroscopic dipole does **not** add spin to the electrons, and therefore does not increase the magnetic moment.

Even the Barnett effect, which does create a tiny extra magnetisation when a body is spun, is far too weak to be useful: to double the field of a typical NdFeB magnet (≈ 1 T) you would need an angular velocity of order \(10^{12}\) rad s⁻¹ (∼10¹⁰ rpm), a value that no macroscopic object can survive.

### 4.2  How could the field geometry be modified to “pump” continuously?  

Because the underlying physics forbids a net increase of \(|\mu|\) by the proposed mechanical route, **no modification of the field geometry can succeed**. The three practical obstacles listed by the student are symptoms of the same deeper limitation:

| Problem | Why it cannot be fixed by geometry | What *actually* works (if you truly want more magnetisation) |
|---------|-----------------------------------|------------------------------------------------------------|
| (1) The field does not allow continuous pumping | The RMF already supplies the maximum torque consistent with the supplied power; continuous “pumping” would require a source of *spin angular momentum* inside the material, which does not exist. | Use a **magnetisation process**: apply a strong static field while the material is above its Curie temperature, or use a high‑frequency alternating field to drive **magnetic hysteresis** into the saturated region. |
| (2) Currents in matter appear as paired “doublets” (no net field) | Bound currents are divergence‑free; you cannot create a net current loop without a closed path that exits the material. | If you truly need a net circulating current, you must supply **real conduction current** (e.g. a superconducting coil) – that is a different device, not a pumped permanent magnet. |
| (3) Vertical pulse is not isotropic | The anisotropy of a brief pulse is irrelevant; even a perfectly isotropic field cannot change the magnitude of the intrinsic dipole without re‑orienting electron spins. | Use a **uniform static bias field** of sufficient strength and duration to move domain walls into a fully aligned state (magnet‑hardening). |

In short, the only way to *increase* the magnetic field produced by a piece of matter is to **alter its internal magnetic order** (domain alignment, increase the number of aligned spins, or add an external current). The scheme described in the question does none of those.

---

## 5.  Final answer – concise statements  

* **Answer to Q1:** The proposed cycle cannot increase the magnetic moment of a permanent magnet. The rotating field can spin the magnet, but the intrinsic magnetisation (the source of the external field) remains unchanged. Any extra field generated by the Barnett effect is many orders of magnitude too small to be useful.  

* **Answer to Q2:** Because the limitation is not geometric but fundamental, no alteration of the horizontal AC field or the vertical pulse can create a continuous “magnetic pump”. To raise the magnet’s field you must either (a) supply a real current loop (e.g. a superconducting coil) or (b) change the material’s magnetic ordering by heating, applying a strong static field, or using high‑frequency hysteresis cycling. Changing the field geometry alone cannot overcome the three listed problems.

---

## 6.  Common Mistakes  

| Mistake | Why it’s wrong | Correct reasoning |
|--------|----------------|-------------------|
| **Confusing mechanical rotation with increased magnetic moment.** | A spinning magnet does not add electron spin; the dipole moment stays the same. | Only the *direction* of **μ** changes; its magnitude can change only by altering electron spin alignment. |
| **Assuming the electromagnetic field can “store” angular momentum indefinitely.** | When the motor field is turned off, its angular momentum returns to the power source; it is not a reservoir that can be tapped later. | Conservation of total (field + mechanical) angular momentum guarantees no net gain. |
| **Neglecting the tiny size of the Barnett effect.** | The Barnett magnetisation is proportional to \(\Omega\) and the electron gyromagnetic ratio; realistic \(\Omega\) gives a field ≪ 10⁻⁶ T. | Even rotating at 10⁴ rad s⁻¹ yields a magnetisation of ≈ 10⁻⁹ A m², far below typical PM moments (≈ 10⁻² A m²). |
| **Thinking that a short vertical pulse can “pump” spin into the material.** | A brief field only exerts torque; it does not

*Original question: [Can we increase magnetism in matter by pumping?](https://physics.stackexchange.com/questions/876170/can-we-increase-magnetism-in-matter-by-pumping) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
