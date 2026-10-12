---
layout: question
title: How can a wireless mouse dongle efficiently receive a signal with a much longer
  wavelength?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: How can a wireless mouse dongle efficiently
  receive a signal with a much longer wavelength?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is really asking  

A 2.4 GHz wireless mouse sends a tiny RF signal (≈ 10 mW or less).  
The receiver that sits in the USB dongle is only about **1 cm** long – far smaller than the 12.5 cm wavelength of a 2.4 GHz wave.  

> **Why does the dongle still pick up the signal “efficiently”, even though textbook antenna theory seems to say an antenna must be on the order of a quarter‑wavelength to work?**  

We have to explain, using the physics of antennas and RF circuits, how a **very small antenna** can still receive enough energy to decode the mouse’s data, and why the “quarter‑wave rule” is not a hard limit for modern wireless designs.

---

## 2. Step‑by‑step explanation  

### 2.1.  Antenna size vs. wavelength – the *electrically short* case  

* **Electrically short antenna**: an antenna whose physical length \(L\) is much smaller than the wavelength \(\lambda\) ( \(L \ll \lambda/4\) ).  
* For such an antenna the **radiation resistance** \(R_{\rm rad}\) is tiny (a few mΩ) while the **reactive (capacitive) impedance** is huge (tens to hundreds of ohms).  
* Because most of the input power is stored in the reactance instead of being radiated, the **radiation efficiency** \(\eta = R_{\rm rad}/(R_{\rm rad}+R_{\rm loss})\) can be low (a few percent).

> **Key point:** Low radiation efficiency does **not** mean the antenna cannot be used as a *receiver*. It merely means that, compared with a half‑wave dipole, a smaller antenna captures less power from the same incident field. If the incident field is strong enough, the captured power can still exceed the receiver’s sensitivity.

### 2.2.  How much power does the dongle actually need?  

The mouse uses a low‑power RF front‑end (typically **10 mW** EIRP or less).  
The dongle is usually only a few **centimetres** away – let us take a representative distance \(d = 5\;\text{cm}\).

The free‑space Friis transmission formula tells us the received power \(P_{\rm r}\):

\[
P_{\rm r}= P_{\rm t}\, G_{\rm t}\, G_{\rm r}\,\Bigl(\frac{\lambda}{4\pi d}\Bigr)^{\!2}
\]

where  

* \(P_{\rm t}\) – transmitted power (≈ 10 mW = 0.01 W)  
* \(G_{\rm t}\) – gain of the mouse’s antenna (≈ 1 dBi ⇒ 1.26)  
* \(G_{\rm r}\) – gain of the dongle’s antenna (≈ 1 dBi ⇒ 1.26) – even a very small antenna can achieve ~0 dBi with a ground plane.  
* \(\lambda = c/f = 0.125\;\text{m}\) (for 2.4 GHz)  

Plugging numbers:

\[
\begin{aligned}
\Bigl(\frac{\lambda}{4\pi d}\Bigr)^{2} &=
\Bigl(\frac{0.125}{4\pi \times 0.05}\Bigr)^{2}
= \Bigl(\frac{0.125}{0.628}\Bigr)^{2}
= (0.199)^{2}
\approx 0.040 \\
P_{\rm r} &\approx 0.01\;\text{W}\times 1.26 \times 1.26 \times 0.040 \\
&\approx 0.01\;\text{W}\times 0.064 \\
&\approx 6.4\times10^{-4}\;\text{W}=0.64\;\text{mW}
\end{aligned}
\]

Even **without any antenna gain** (i.e. \(G_{\rm t}=G_{\rm r}=1\)) we would still receive ≈ 0.4 mW.  

Typical low‑power RF receivers (e.g., the CC2500 used in many mice) have a **sensitivity** of about **‑90 dBm** (≈ 0.1 µW) for a 1 % bit‑error rate.  

\[
0.64\;\text{mW} = -1.9\;\text{dBm} \gg -90\;\text{dBm}
\]

Thus the received power is **hundreds of thousands of times larger** than the minimum needed for reliable demodulation. The system does **not** require a highly efficient antenna – it just needs enough power to stay above the noise floor, which the short distance easily guarantees.

### 2.3.  Making a *tiny* antenna resonant – matching networks  

A 1 cm trace on a PCB is far from a λ/4 radiator, but we can **electrically lengthen** it:

1. **Inverted‑F antenna (IFA) / Meander line** – a short conductor placed over a ground plane acts like a λ/4 monopole if we add a **capacitive loading** at its tip (a small metal pad or a “short” to the ground plane). This creates a resonance at the desired frequency despite the physical length being only a few percent of λ.

2. **Chip antenna** – a commercial component that contains a tiny radiating element together with an integrated **LC matching network** on the same substrate. Its electrical size may be ≈ λ/20, but the internal matching transforms the high reactance to a 50 Ω resistive input.

3. **External matching network** – a discrete inductor (or a printed spiral) placed in series with the antenna, together with the antenna’s own capacitance, forms a **series‑LC resonant circuit**. At resonance the impedance seen by the receiver front‑end is close to 50 Ω, so almost all the captured power is transferred to the low‑noise amplifier (LNA).

The **quality factor** \(Q\) of this resonant circuit is modest (typically 5–15). A high \(Q\) would make the bandwidth too narrow; a modest \(Q\) gives enough bandwidth (≈ 2 % of 2.4 GHz ≈ 50 MHz) for the mouse’s data rate while still providing a good impedance match.

### 2.4.  The role of the low‑noise front‑end  

Even if only a tiny fraction (say 1 %) of the incident power is actually **radiated** (or captured) by the short antenna, the **receiver front‑end** amplifies it:

* **Low‑Noise Amplifier (LNA)** – provides 20–30 dB of gain with a noise figure of ~2 dB, raising the signal well above the thermal noise floor (\(-174\;\text{dBm/Hz}\)).  
* **Automatic Gain Control (AGC)** – adjusts gain so that the later demodulator always sees a suitable level.

Because the LNA is directly connected to the antenna via the matching network, the *effective* received power after the LNA can be many milliwatts, even though the *antenna efficiency* is low.

### 2.5.  Why “quarter‑wave is required” is a misconception  

| Statement | Reality |
|-----------|----------|
| An antenna must be ≈ λ/4 to receive any signal. | Any conductive piece will pick up an electric field; the *efficiency* simply drops as the size shrinks. |
| Below λ/4 the antenna “doesn’t work”. | It still works; you just get lower radiation resistance and need matching to extract the small voltage/current. |
| A small antenna cannot be used for communication. | Modern systems (Wi‑Fi, Bluetooth, ZigBee, RFID) routinely use antennas < λ/10 thanks to close proximity, high‑gain coding, and sensitive LNAs. |

Thus the “quarter‑wave rule” is a design guideline for **high‑efficiency radiators**, not a hard physical limit for *receivers*.

### 2.6.  Putting it all together  

1. **Short distance** → very little free‑space loss, so even a weakly efficient antenna receives enough power.  
2. **Compact antenna + matching network** → presents a 50 Ω resistive input to the receiver, maximizing power transfer.  
3. **Low‑noise, high‑gain front‑end** → boosts the tiny received voltage to a usable level.  
4. **Modulation & error‑correction** → tolerate the modest SNR that results from the small antenna.

Consequently the dongle can reliably decode the mouse’s data even though its physical dimensions are far smaller than the 12.5 cm wavelength.

---

## 3. Final answer  

A wireless‑mouse dongle works because:

* At the typical 5 cm separation the **received power** from a ≤ 10 mW transmitter is on the order of **hundreds of microwatts**, far above the receiver’s sensitivity.  
* The dongle uses a **tiny printed (or chip) antenna** that is made resonant at 2.4 GHz with a **matching network** (inverted‑F, meander line, or integrated LC). This converts the antenna’s large reactive impedance into a 50 Ω resistive load.  
* A **low‑noise amplifier** right after the antenna provides 20‑30 dB of gain, so the weak signal is amplified before demodulation.  
* Because the communication distance is very short, the system does not need a high‑efficiency (quarter‑wave) antenna; it only needs enough power to stay above the noise floor, which the above measures easily achieve.

Hence, the apparent size mismatch does **not** prevent efficient reception; the combination of proximity, impedance matching, and a sensitive front‑end makes the small dongle perfectly capable of handling a 2.4 GHz signal.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | Correct view |
|---------|----------------|--------------|
| **“An antenna must be at least λ/4 to work.”** | That rule is about *radiation efficiency*, not about the ability to pick up a field. | Any conductor can act as a receiving element; efficiency just falls with size. |
| **“Because the antenna is tiny, the received power is zero.”** | Power scales with the **effective aperture**, which for a modest‑gain small antenna is still non‑zero. | Use Friis’ equation: even a 1 cm antenna receives measurable power at a few‑centimetre range. |
| **“The mouse transmits only a few microwatts, so the dongle cannot see it.”** | Most mice transmit ≈ 10 mW EIRP, and the path loss over 5 cm is tiny. | Received power is ≈ 0.5 mW, orders of magnitude above typical receiver sensitivities (≈ ‑90 dBm). |
| **“Matching networks only work for large antennas.”** | Matching is purely an electrical technique; it works regardless of physical length. | A short PCB trace + a series inductor (or built‑in chip network) can present a 50 Ω resistive input at the desired frequency. |
| **“The dongle must have a directional antenna to capture the signal.”** | At very short distances the directionality is irrelevant; the field is essentially uniform over the small device. | Simple omnidirectional (monopole/IFA) antennas are sufficient. |

Avoid these misconceptions and remember that **proximity, impedance matching, and low‑noise amplification** are the real reasons a centimeter‑scale dongle can reliably receive a 2.4 GHz wireless mouse signal.

*Original question: [How can a wireless mouse dongle efficiently receive a signal with a much longer wavelength?](https://physics.stackexchange.com/questions/876829/how-can-a-wireless-mouse-dongle-efficiently-receive-a-signal-with-a-much-longer) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
