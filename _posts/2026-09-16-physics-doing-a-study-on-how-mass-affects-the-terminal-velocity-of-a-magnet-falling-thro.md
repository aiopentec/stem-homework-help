---
layout: question
title: Doing a study on how mass affects the terminal velocity of a magnet falling
  through a copper pipe (Magnetic Induction). Need some help!
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Doing a study on how mass affects the
  terminal velocity of a magnet falling through a copper pipe (Magnetic Induction).
  Need'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

A magnet is dropped through a **copper pipe**.  
Because the magnet’s field cuts the conducting pipe, eddy currents are induced.  
These currents create a magnetic drag that eventually balances the weight of the magnet, so the magnet falls at a **terminal velocity** \(v_{t}\).

The student has written the balance as  

\[
mg = k\,v_{t},
\]

and wants to understand why the constant \(k\) contains the **fourth power of the pipe radius** (or diameter).  
The goal is to **derive** the expression for the drag force, show explicitly where the \(R^{4}\) (or \(D^{4}\)) term comes from, and explain why the experiment should indeed be very sensitive to the pipe size.

---

## 2. Step‑by‑step derivation  

Below we follow the treatment that appears in the Donoso paper (Eq. 10) but we keep every algebraic step explicit.

### 2.1.  Geometry and notation  

| Symbol | Meaning |
|--------|---------|
| \(R\) | inner radius of the copper tube (m) |
| \(b\) | thickness of the tube wall (so outer radius is \(R+b\)) |
| \(\sigma\) | electrical conductivity of copper (S · m\(^{-1}\)) |
| \(\mu_{0}\) | permeability of free space (4π × 10⁻⁷ H · m⁻¹) |
| \(a\) | radius of the cylindrical magnet (assumed magnetized uniformly along its axis) |
| \(L\) | length of the magnet (m) |
| \(M\) | magnetic moment of the magnet (A·m²) – for a uniformly magnetized cylinder \(M = \pi a^{2} L\,M_{s}\) |
| \(v\) | instantaneous velocity of the magnet (positive downwards) |
| \(g\) | gravitational acceleration (9.81 m · s⁻²) |
| \(m\) | total mass of the falling object (magnet + non‑conductive load) |

The magnet’s axis stays coaxial with the pipe, and the pipe is long enough that end effects can be ignored while the magnet is inside.

### 2.2.  Magnetic field of the moving magnet

For a long cylindrical magnet whose magnetisation is along the axis, the axial component of the magnetic field at a radial distance \(r\) from the axis (outside the magnet) is well approximated by the field of a **magnetic dipole** when \(r\gg a\). Inside the pipe, however, the dominant field component that threads the conducting wall is the **axial flux** through a circular loop of radius \(r\).  

The flux through a loop of radius \(r\) at a distance \(z\) from the centre of the magnet is

\[
\Phi(r,z) = \mu_{0} M \frac{z}{2\pi\left(r^{2}+z^{2}\right)^{3/2}} .
\]

(Exact expressions exist, but the dipole form already captures the needed \(r^{-3}\) dependence.)

When the magnet moves with speed \(v\) the flux changes in time:

\[
\frac{d\Phi}{dt}= -v\,\frac{\partial\Phi}{\partial z}.
\]

### 2.3.  Induced emf and eddy‑current loop

Consider a thin cylindrical shell of the pipe at radius \(r\) (with \(R\le r\le R+b\)) and thickness \(\mathrm{d}r\).  
Because the wall is thin compared with \(R\) we treat the current as flowing in a **circular loop** of circumference \(2\pi r\).  

The emf around that loop is

\[
\mathcal{E}(r) = -\frac{d\Phi}{dt}= v\,\frac{\partial\Phi}{\partial z}.
\]

The resistance of the thin annular strip of width \(\mathrm{d}r\) and length \(2\pi r\) is

\[
\mathrm{d}R = \frac{1}{\sigma}\,\frac{\mathrm{d}\ell}{A}
          = \frac{1}{\sigma}\,\frac{2\pi r}{b\,\mathrm{d}r},
\]

where \(A = b\,\mathrm{d}r\) is the cross‑sectional area of the strip (wall thickness \(b\) times width \(\mathrm{d}r\)).

Thus the induced current in the strip is

\[
\mathrm{d}I = \frac{\mathcal{E}}{\mathrm{d}R}
            = \sigma\,\frac{b\,\mathrm{d}r}{2\pi r}\,\mathcal{E}(r).
\]

### 2.4.  Lorentz (drag) force on the strip

The current loop experiences a magnetic force density \(\mathbf{J}\times\mathbf{B}\).  Integrating around the loop gives a net axial force (opposite to the motion):

\[
\mathrm{d}F = I\, (2\pi r)\, B_{r}(r,z) ,
\]

where \(B_{r}\) is the radial component of the magnet’s field at the wall.  For a dipole, \(B_{r}\sim \dfrac{\mu_{0} M r}{4\pi (r^{2}+z^{2})^{5/2}}\).

Putting the expressions together and integrating over the whole wall thickness,

\[
\mathrm{d}F = \sigma b \,\frac{\mathcal{E}(r)}{r}\, B_{r}(r,z) \,\mathrm{d}r .
\]

Now substitute the explicit forms of \(\mathcal{E}\) and \(B_{r}\) (both proportional to \(M\) and to powers of \(r\) and \(z\)). After a bit of algebra the integrand behaves as

\[
\mathrm{d}F \propto \sigma b \, v \, M^{2}\,
\frac{r^{3}}{(r^{2}+z^{2})^{4}} \,\mathrm{d}r .
\]

### 2.5.  Integrate over the pipe wall and over the magnet length

Because the pipe wall is thin we can replace \(r\) by the **mean radius** \(R\) (the error is of order \(b/R\)). The integral over \(r\) then simply yields a factor \(b\) and we obtain

\[
F_{\text{drag}} = C\,\sigma\,\frac{M^{2}}{R^{4}}\,v ,
\]

with  

\[
C = \frac{\mu_{0}^{2}}{8\pi}\int_{-\infty}^{\infty}\frac{z^{2}}{(R^{2}+z^{2})^{4}}\,\mathrm{d}z
   = \frac{\mu_{0}^{2}}{8\pi}\,\frac{\pi}{12R^{3}}
   = \frac{\mu_{0}^{2}}{96R^{3}} .
\]

Collecting constants we finally write the **linear drag law**

\[
\boxed{F_{\text{drag}} = k\,v},
\qquad 
k = \frac{\mu_{0}^{2}\,\sigma\,M^{2}}{96\,R^{4}} .
\]

All the approximations (thin wall, dipole field, long pipe) are the same ones used by Donoso; the factor \(96\) may be written differently depending on how the magnetic moment \(M\) is expressed.  In the paper the authors replace \(M\) by the product of the magnet’s **cross‑sectional area** \(\pi a^{2}\) and its **remanent flux density** \(B_{r}\), which yields the same \(R^{-4}\) dependence.

### 2.6.  Terminal velocity

At terminal velocity the gravitational force equals the magnetic drag:

\[
mg = k\,v_{t}
\quad\Longrightarrow\quad
\boxed{v_{t}= \frac{m g}{k}
      = \frac{96\, m g\, R^{4}}{\mu_{0}^{2}\,\sigma\,M^{2}} } .
\]

Because the drag coefficient \(k\) contains **\(R^{4}\)** (or, equivalently, **\(D^{4}\)**), a modest change in pipe radius produces a large change in terminal speed.

---

## 3. Final answer  

The constant that multiplies the velocity in the force balance is

\[
\boxed{ k = \dfrac{\mu_{0}^{2}\,\sigma\,M^{2}}{96\,R^{4}} }
\]

so that

\[
\boxed{ v_{t}= \dfrac{96\, m g\, R^{4}}{\mu_{0}^{2}\,\sigma\,M^{2}} } .
\]

The **fourth‑power dependence on the pipe radius** arises from:

* the **induced emf** being proportional to the rate of change of magnetic flux (\(\propto v/R^{3}\) for a dipole field);
* the **resistance** of the wall scaling as \(1/(bR)\);
* the **Lorentz force** on the eddy‑current loop bringing in another factor of \(1/R\).

Multiplying these three contributions gives the overall \(R^{-4}\) (or \(D^{-4}\)) factor.

Consequently, a pipe whose radius is larger by only a few millimetres can change the drag coefficient – and hence the terminal velocity – by roughly an order of magnitude, exactly as observed in the experiment.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating the pipe as a solid cylinder** and using its cross‑sectional area for resistance. | The current flows only in the thin wall; the resistance is inversely proportional to the wall thickness, not to the whole area. | Use the wall thickness \(b\) and the circumference \(2\pi R\) to compute the resistance of a thin annular strip. |
| **Using the magnetic field of a long solenoid** instead of the dipole field for a short magnet. | The field decays as \(1/r^{3}\); using a uniform field underestimates the radial dependence and removes the \(R^{-4}\) factor. | Approximate the magnet as a dipole (or use the exact analytical expression) when the pipe radius is several times larger than the magnet radius. |
| **Neglecting the factor of \(v\) in the emf** and writing the drag force as proportional to \(v^{2}\). | Faraday’s law gives \(\mathcal{E}\propto v\); the induced current (and thus the Lorentz force) is linear in \(v\) for the low‑speed regime where the magnetic diffusion time is short. | Keep the first‑order term in \(v\); the quadratic term only appears at very high speeds where skin‑effect becomes important. |
| **Assuming the magnet’s magnetic moment \(M\) does not appear in \(k\).** | \(M\) (or equivalently the product \(B_{r} a^{2}\)) enters squared because the induced emf and the Lorentz force each contain one factor of the field. | Write \(M = \pi a^{2}L\,M_{s}\) (or \(M = B_{r}\,a^{2}L/\mu_{0}\)) and keep it in the final expression. |
| **Forgetting the thin‑wall approximation** when the pipe wall is comparable to the radius. | The \(R^{-4}\) law strictly holds when \(b\ll R\); a thick wall reduces the effective resistance and changes the exponent slightly. | Verify \(b/R < 0.1\); otherwise keep the full integral over the wall thickness instead of pulling out a single \(R\). |

By paying attention to these points the derived expression will match both the literature (Donoso’s Eq. 10) and experimental data, and the strong sensitivity to pipe diameter will be fully understood.

*Original question: [Doing a study on how mass affects the terminal velocity of a magnet falling through a copper pipe (Magnetic Induction). Need some help!](https://physics.stackexchange.com/questions/876005/doing-a-study-on-how-mass-affects-the-terminal-velocity-of-a-magnet-falling-thro) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
