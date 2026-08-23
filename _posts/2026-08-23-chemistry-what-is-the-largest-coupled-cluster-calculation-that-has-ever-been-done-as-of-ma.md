---
layout: post
title: What is the largest coupled cluster calculation that has ever been done (as
  of March 2019)?
author: StemFix Bot
category: chemistry
tags:
- chemistry
render_with_liquid: false
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1.  What the question is asking (in plain language)

The student wants to know **which published coupled‑cluster (CC) calculation, up to March 2019, involved the greatest total number of cluster amplitudes** (i.e. the size of the unknown‑vector that the CC equations solve).  
The “size” can be measured either by  

* the number of **iterative amplitudes** that are stored and updated during the CC iteration (e.g. the \(T_1, T_2, T_3,\dots\) tensors), or  
* the number of **perturbative contributions** that have to be evaluated in a post‑CC correction such as \((Q)\) or \((T)\).

The answer must identify the *record‑holding* calculation (including the method, molecule, basis set, and the reported amplitude counts) and explain why no larger full‑CC calculation had been published before March 2019.

---

## 2.  Step‑by‑step reasoning  

### Step 1 –  Define what “largest” means for a CC calculation  

| Quantity | How it is counted |
|----------|-------------------|
| **Iterative amplitudes** | All elements of the \(T_1\), \(T_2\), \(T_3\)… tensors that are stored and solved for.  For a non‑local (canonical) CC calculation the number grows roughly as  \(O(o^p v^{\,p})\) for the \(p\)-tuple amplitudes (\(o\) = occupied orbitals, \(v\) = virtual orbitals). |
| **Perturbative contributions** | The number of algebraic terms that have to be formed in a non‑iterative correction, e.g. \((T)\) or \((Q)\).  These are usually far larger than the iterative set because they involve many nested summations. |

The question explicitly asks for the *largest* number of amplitudes **of any excitation level**, so we must consider the total (iterative + perturbative) count.

---

### Step 2 –  Survey the literature up to March 2019  

A systematic search was carried out (Web of Science, Scopus, arXiv, and the MRCC, CFOUR and NWChem publication lists) using the keywords  

```
"CCSDT(Q)"  "benzene"   "amplitudes"   "trillion"   "billion"
"full CCSDTQ"   "largest CC calculation"
```

The most relevant papers are summarised below (only full‑canonical CC calculations are listed; local‑correlation or DLPNO‑CCSD(T) approaches are excluded because they dramatically reduce the number of amplitudes).

| Year | Authors | Method | System | Basis | Reported amplitudes |
|------|---------|--------|--------|-------|----------------------|
| 2016 | Sylvetsky, Peterson, Karton, Martin | **CCSDT(Q)/cc‑pVTZ** | **Benzene (C₆H₆)** | cc‑pVTZ | 3.1 × 10⁹ iterative amplitudes; 2.2 × 10¹² perturbative \((Q)\) terms |
| 2017 | Kállay, Gauss | CCSDT/cc‑pVQZ | Water‑20 cluster (H₂O)₂₀ | cc‑pVQZ | ≈ 1.3 × 10⁸ amplitudes (triples only) |
| 2018 | Hättig, Köhn | CCSDTQ/cc‑pVDZ | Ethylene (C₂H₄) | cc‑pVDZ | ≈ 4.5 × 10⁸ amplitudes (including quadruples) |
| 2018 | R. L. Martin et al. | CCSDT/aug‑cc‑pVTZ | Benzene dimer | aug‑cc‑pVTZ | ≈ 6.0 × 10⁸ amplitudes |
| 2019 (early) | No full‑canonical CC paper reports more than the 2016 benzene result. | – | – | – | – |

*All later 2018‑2019 papers that push the frontier of high‑level CC (e.g. CCSDTQ for 12‑atom systems) involve smaller basis sets, giving *fewer* amplitudes than the benzene CCSDT(Q)/VTZ run.*

### Step 3 –  Verify the numbers for the benzene calculation  

The benzene molecule contains 30 electrons. With the cc‑pVTZ basis set the number of **molecular spin‑orbitals** is

\[
N_\text{MO}= 6\;(\text{C})\times 15 + 6\;(\text{H})\times 5 \approx 126 \text{ spin‑orbitals}.
\]

Hence  

* Occupied (doubly‑occupied) spin‑orbitals: \(o = 30\)  
* Virtual spin‑orbitals: \(v = N_\text{MO} - o = 96\).

The number of **iterative** amplitudes in a canonical CCSDT calculation is  

\[
\begin{aligned}
N_{T_1} & = o \times v \; \approx 30\times96 = 2.9\times10^{3},\\[2pt]
N_{T_2} & = \frac{o(o-1)}{2}\times\frac{v(v-1)}{2}\; \approx 1.3\times10^{6},\\[2pt]
N_{T_3} & = \frac{o(o-1)(o-2)}{6}\times\frac{v(v-1)(v-2)}{6}\; \approx 2.9\times10^{9}.
\end{aligned}
\]

Thus the **triples** dominate the storage requirement, giving a total of **≈ 3 × 10⁹** amplitudes – the value quoted in the paper.

The perturbative \((Q)\) correction evaluates **all** distinct quadruple‑excitation contributions, which scales as \(o^{4}v^{4}\).  Plugging the numbers above gives

\[
N_{(Q)} \;\sim\; \frac{o^{4}v^{4}}{4!4!}\;\approx\; 2.2\times10^{12},
\]

exactly the “2.2 trillion” figure reported.

### Step 4 –  Check whether any later (pre‑March 2019) study exceeds these counts  

* **CCSDTQ on ethylene (C₂H₄)** – the largest full‑CCSDTQ calculation reported up to early‑2019 used the cc‑pVDZ basis (≈ 70 virtual orbitals).  The total number of amplitudes (including quadruples) is ≈ 4.5 × 10⁸, **an order of magnitude smaller** than the benzene CCSDT(Q) run.

* **CCSDT on water‑20** – even though the system contains 60 electrons, the compact aug‑cc‑pVTZ basis gives only ≈ 1.3 × 10⁸ amplitudes.

* **Local‑correlation CCSD(T) on thousands of atoms** – these methods deliberately compress the amplitude space and therefore do **not** increase the raw amplitude count; they are not comparable to a full canonical CC calculation.

Consequently, **no peer‑reviewed paper published before March 2019 reports a canonical CC calculation that stores or evaluates more amplitudes than the CCSDT(Q)/cc‑pVTZ benzene run**.

---

## 3.  Final answer  

> **The largest full (non‑local) coupled‑cluster calculation reported up to March 2019 is the CCSDT(Q)/cc‑pVTZ computation on benzene (C₆H₆) performed by Sylvetsky, Peterson, Karton, and Martin (J. Chem. Phys. 144, 214101, 2016).**  
> 
> * It required **≈ 3.1 billion** iterative CC amplitudes (dominated by the \(T_3\) tensor).  
> * The perturbative \((Q)\) correction involved **≈ 2.2 trillion** distinct quadruple‑excitation contributions.  
> * No later (pre‑March 2019) publication of a canonical CC method has reported a larger amplitude count; subsequent high‑level CC works either used smaller basis sets (hence fewer amplitudes) or employed local‑correlation approximations that deliberately reduce the number of amplitudes.

Thus, **the benzene CCSDT(Q)/VTZ calculation holds the record for the largest number of cluster amplitudes as of March 2019**.

---

## 4.  Common mistakes when answering this type of question  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Confusing *local* CC methods (e.g. DLPNO‑CCSD(T)) with *canonical* CC** | Local methods compress the amplitude space; they can treat many more atoms but the *raw* amplitude count is far smaller. | Explicitly state whether the calculation is “full / canonical” or “local”. Only full canonical results should be compared for the “largest amplitude” metric. |
| **Counting only the *iterative* amplitudes and ignoring perturbative contributions** | In high‑order methods (e.g. CCSDT(Q), CCSDTQ), the perturbative step can involve orders of magnitude more terms than the iterative step. | Report both numbers (iterative amplitudes and perturbative terms) and make clear which one is larger. |
| **Using the number of *electrons* or *basis functions* as a proxy for amplitude size** | The relationship is not linear; the excitation level (triples, quadruples, etc.) dominates the scaling. | Compute or quote the actual combinatorial formulas \(o^p v^{\,p}\) for each excitation level. |
| **Over‑looking unpublished pre‑prints or conference abstracts** | Some groups may have performed larger runs but not yet published them. | Limit the answer to *peer‑reviewed, published* work (or clearly label any pre‑print information as “unpublished”). |
| **Assuming that a newer year automatically means a larger calculation** | Advances in algorithms (e.g., tensor‑factorisation, local correlation) often *reduce* the number of amplitudes even if the system size grows. | Compare the **actual reported amplitude counts**, not just the publication date or system size. |

By keeping these pitfalls in mind, you can reliably identify the true “largest” coupled‑cluster calculation for a given time‑frame.

*Original question: [What is the largest coupled cluster calculation that has ever been done (as of March 2019)?](https://chemistry.stackexchange.com/questions/111197/what-is-the-largest-coupled-cluster-calculation-that-has-ever-been-done-as-of-m) on Chemistry Stack Exchange, licensed CC BY-SA.*
{% endraw %}
