---
layout: question
title: Why carbon monoxide has most HOMO towards the carbon rather than the oxygen?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Why carbon monoxide has most HOMO towards
  the carbon rather than the oxygen?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. Restate the Problem in Plain Language

Oxygen is much more electronegative than carbon, which means oxygen holds onto its electrons more tightly and has lower-energy atomic orbitals. Based on electronegativity alone, you would naturally expect the highest occupied molecular orbital (HOMO) of carbon monoxide (CO) to be pulled closer to the oxygen atom. 

However, experimental and computational data show the exact opposite: the HOMO of CO (specifically the $5\sigma$ orbital) is heavily localized on the **carbon** atom. This is why CO uses its carbon atom, rather than its oxygen atom, to donate electrons to metal centers in coordination chemistry. 

The goal is to explain *why* this happens using molecular orbital (MO) theory, going beyond simple electronegativity arguments.

---

## 2. Step-by-Step Solution

### Step 1: Count the Valence Electrons
To build the molecular orbital diagram for CO, we first need to determine the number of valence electrons:
* Carbon ($Z = 6$): $2s^2 2p^2$ (4 valence electrons)
* Oxygen ($Z = 8$): $2s^2 2p^4$ (6 valence electrons)
* **Total valence electrons = 10**

### Step 2: Compare Atomic Orbital Energies
Because oxygen is more electronegative than carbon, its atomic orbitals (both $2s$ and $2p$) are **lower in energy** than the corresponding atomic orbitals of carbon. 

### Step 3: Construct the Molecular Orbitals (Qualitative MO Theory)
When the atomic orbitals combine to form molecular orbitals, orbitals of similar energy interact most strongly (the mixing is more effective when the energy gap is smaller). 

For homonuclear diatomics (like $\text{N}_2$ or $\text{O}_2$), $s-p$ mixing is either ignored or straightforward. For heteronuclear diatomics like CO, $s-p$ mixing is actually quite significant because the carbon $2s$ and oxygen $2p_z$ orbitals happen to be relatively close in energy. 

Let's look at the resulting valence MOs in order of increasing energy:
1. **$1\pi$ orbital (bonding):** Formed primarily from the $p_x$ and $p_y$ atomic orbitals.
2. **$4\sigma$ orbital (bonding):** Primarily derived from oxygen $2s$ mixed with some carbon $2s/2p_z$.
3. **$5\sigma$ orbital (HOMO):** The highest occupied molecular orbital.
4. **$2\pi$ orbital (antibonding):** The LUMO (Lowest Unoccupied Molecular Orbital).

### Step 4: Analyze the Nature of the $5\sigma$ HOMO
Why is the $5\sigma$ orbital localized more on the carbon atom despite oxygen's higher electronegativity? 

1. **Orbital Symmetry and Directional Character:** The $5\sigma$ orbital is strongly influenced by the antibonding interaction between the carbon $2s/2p_z$ and oxygen $2s/2p_z$ manifolds. 
2. **The $s-p$ Zipping Effect:** In CO, the carbon $2s$ orbital and carbon $2p_z$ orbital mix extensively (hybridize) because of the strong polarization of the molecule. The carbon $2s$ orbital is relatively high in energy compared to oxygen's orbitals, which pushes electron density away from the oxygen $2s$ core and onto the carbon atom's outward-pointing lobe.
3. **The Non-bonding/Weakly Antibonding Nature:** The $5\sigma$ orbital is often described as a lone pair localized on carbon. Mathematically, when we solve the secular determinants for CO using wavefunctions, the coefficient of the carbon atomic orbital in the $5\sigma$ wavefunction is larger than the coefficient of the oxygen atomic orbital. 

Therefore, even though oxygen's atomic orbitals are lower in energy, the specific algebraic combination of the carbon $2s$ and $2p_z$ orbitals creates a spatial distribution (a large lobe) that sticks out much further on the **carbon** side.

---

## 3. Final Answer

Although oxygen is more electronegative than carbon, the HOMO of carbon monoxide (the $5\sigma$ orbital) has greater electron density on the **carbon** atom. 

This occurs because of **extensive $s-p$ orbital mixing** in the unsymmetrical potential field of the heteronuclear diatomic. The mathematical combination of the carbon and oxygen atomic orbitals results in a wave function coefficient that is larger on carbon, and the directional lobe of this orbital projects further away from the carbon nucleus, creating a carbon-localized "lone pair" that dictates its Lewis basicity and bonding behavior with transition metals.

---

## 4. Common Mistakes

* **Relying solely on electronegativity:** Assuming that the electron density of *every* occupied orbital must be highest on the more electronegative atom. Electronegativity dictates orbital energy levels, but molecular orbital coefficients (shape and electron density distribution) depend on overlap and mixing, not just energy matching.
* **Confusing HOMO with LUMO:** Forgetting that while the HOMO ($5\sigma$) is carbon-centered, the LUMO ($2\pi$*) is *also* heavily weighted toward the carbon atom, which is why CO is both a good $\sigma$-donor *and* a good $\pi$-acceptor at the carbon end.
* **Treating CO like a homonuclear diatomic:** Forgetting that heteronuclear molecules feature uneven atomic orbital contributions due to differences in both energy *and* effective nuclear charge.

*Original question: [Why carbon monoxide has most HOMO towards the carbon rather than the oxygen?](https://chemistry.stackexchange.com/questions/196097/why-carbon-monoxide-has-most-homo-towards-the-carbon-rather-than-the-oxygen) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
