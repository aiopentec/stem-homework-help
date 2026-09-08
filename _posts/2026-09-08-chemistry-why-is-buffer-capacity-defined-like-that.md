---
layout: question
title: Why is buffer capacity defined like that
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Why is buffer capacity defined like
  that'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the question is really asking  

A high‑school student has seen the textbook definition  

\[
\boxed{\beta \;=\;-\frac{d a}{d\mathrm{pH}}}\qquad\text{(with }a+s=\text{constant)}
\]

where  

* \(a\) = concentration of the **weak acid** (HA) in the buffer,  
* \(s\) = concentration of its **conjugate‑base salt** (A⁻, e.g. NaA),  

and is wondering

* **Why** is the buffer capacity expressed as \(-da/d\mathrm{pH}\) instead of something that looks more like “moles added per pH unit’’ (\(dn/d\mathrm{pH}\))?  
* **Why** do we keep the sum \(a+s\) constant while differentiating?  

The answer must use only the concepts that are usually covered in a 12‑th‑grade (dilute‑solution) chemistry class: the Henderson–Hasselbalch equation, simple algebra, and the idea that adding a strong acid or base converts one buffer component into the other.

---

## 2. Step‑by‑step derivation  

### 2.1  The buffer equilibrium and the Henderson–Hasselbalch equation  

For a weak acid HA dissociating in water  

\[
\mathrm{HA}\; \rightleftharpoons\; \mathrm{H^{+}}+\mathrm{A^{-}}
\]

the equilibrium constant is  

\[
K_a=\frac{[\mathrm{H^{+}}][\mathrm{A^{-}}]}{[\mathrm{HA}]}\; .
\]

In a **dilute** solution activities ≈ concentrations, so we can replace the brackets by concentrations.

Re‑arranging and taking base‑10 logarithms gives the Henderson–Hasselbalch equation:

\[
\boxed{\mathrm{pH}=pK_a+\log\frac{[\mathrm{A^{-}}]}{[\mathrm{HA}]}}
\]

In the notation of the problem  

\[
\mathrm{pH}=pK_a+\log\frac{s}{a}\qquad\text{(1)}
\]

where  

* \(a=[\mathrm{HA}]\) (mol L⁻¹)  
* \(s=[\mathrm{A^{-}}]\) (mol L⁻¹).

---

### 2.2  What happens when we add a strong base (or acid)?

*Adding a strong base* (e.g. NaOH) consumes HA and produces the same amount of A⁻:

\[
\mathrm{HA}+ \mathrm{OH^{-}}\;\longrightarrow\;\mathrm{A^{-}}+\mathrm{H_2O}
\]

If we add **\(n\) moles per litre** of NaOH, the concentrations change by  

\[
a \;\longrightarrow\; a-n,\qquad s \;\longrightarrow\; s+n .
\]

Notice that the **total concentration of buffer species does not change**:

\[
(a-n)+(s+n)=a+s=\text{constant}.
\]

That is the reason the textbook writes “keep \(a+s\) constant”.  
(If a strong **acid** were added the signs would be reversed, but the same idea holds.)

Thus the amount of base we have added is exactly the **decrease in the acid concentration**:

\[
n = -\Delta a .
\]

So, instead of writing the capacity as “moles of strong base added per pH unit”, we can equivalently write it as “the decrease of the weak‑acid concentration per pH unit”. That is why the definition uses \(-da/d\mathrm{pH}\).

---

### 2.3  Definition of buffer capacity  

Buffer capacity, \(\beta\), is defined as the **amount of strong acid or base that must be added to change the pH by one unit**. In differential form:

\[
\beta = \frac{dn}{d(\mathrm{pH})}.
\]

Using the relation \(n=-\Delta a\) (or \(dn=-da\)) we obtain

\[
\boxed{\beta = -\frac{da}{d(\mathrm{pH})}} \qquad\text{(2)}
\]

which is exactly the textbook expression.

---

### 2.4  Obtaining an explicit formula for \(\beta\)

Start from eq. (1):

\[
\mathrm{pH}=pK_a+\log\frac{s}{a}.
\]

Because \(a+s=C_{\text{tot}}\) (the total buffer concentration, a constant), we can write  

\[
s = C_{\text{tot}}-a .
\]

Insert this into (1):

\[
\mathrm{pH}=pK_a+\log\frac{C_{\text{tot}}-a}{a}.
\]

Now differentiate both sides with respect to \(a\). Remember that \(\displaystyle \frac{d}{dx}\log x = \frac{1}{\ln 10}\frac{1}{x}\) (the factor \(2.303\) appears because we use base‑10 logs).

\[
\frac{d(\mathrm{pH})}{da}= \frac{1}{\ln 10}\Bigl[\frac{-1}{C_{\text{tot}}-a}-\frac{1}{a}\Bigr]
          = -\frac{1}{2.303}\Bigl[\frac{1}{C_{\text{tot}}-a}+\frac{1}{a}\Bigr].
\]

Invert the derivative (because we need \(-da/d\mathrm{pH}\)):

\[
-\frac{da}{d(\mathrm{pH})}= \frac{2.303}{\displaystyle\frac{1}{C_{\text{tot}}-a}+\frac{1}{a}}
                         = 2.303\; \frac{a\,(C_{\text{tot}}-a)}{C_{\text{tot}}}.
\]

Replace \(a\) by \([\mathrm{HA}]\) and \(C_{\text{tot}}-a = [\mathrm{A^{-}}]\).  Using the original equilibrium expression  

\[
\frac{[\mathrm{A^{-}}]}{[\mathrm{HA}]} = 10^{\mathrm{pH}-pK_a}
\]

one can rewrite the result in the more familiar symmetric form

\[
\boxed{\displaystyle \beta
      = 2.303\,C_{\text{tot}}\,
        \frac{K_a\,[\mathrm{H^{+}}]}{(K_a+[\mathrm{H^{+}}])^{2}}}
\tag{3}
\]

where \(C_{\text{tot}} = a+s\).  
Equation (3) shows that the capacity is highest when \([\mathrm{H^{+}}]=K_a\) (i.e. when pH ≈ pKₐ) and drops off on either side – exactly what we observe experimentally.

---

## 3. Final answer – what the definition means  

* **Why \(-da/d\mathrm{pH}\)?**  
  Adding a strong acid or base converts one buffer component into the other. The number of moles of strong base added equals the *decrease* of the weak‑acid concentration, so \(dn = -da\). Expressing capacity as \(-da/d\mathrm{pH}\) is mathematically identical to the more intuitive \(dn/d\mathrm{pH}\).

* **Why keep \(a+s\) constant?**  
  In the simple model we assume the volume does not change and that the added strong acid/base only interconverts HA ⇌ A⁻. Hence the total concentration of buffer species, \(a+s\), remains the same during the infinitesimal addition that the derivative describes.

* **Resulting expression** (for a dilute solution, activities ≈ concentrations)

\[
\boxed{\beta = -\frac{da}{d\mathrm{pH}}
        = 2.303\,C_{\text{tot}}\,
          \frac{K_a\,[\mathrm{H^{+}}]}{(K_a+[\mathrm{H^{+}}])^{2}}}
\]

The capacity is maximal when the pH equals the pKₐ of the weak acid and decreases as the pH moves away from that point.

---

## 4. Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Writing \(\beta = \dfrac{da}{d\mathrm{pH}}\) (missing the minus sign)** | Adding base *lowers* \(a\); the derivative is therefore negative. The minus sign makes \(\beta\) a **positive** number, which is how capacity is defined. | Remember that the amount of base added equals the *decrease* in acid concentration: \(dn = -da\). |
| **Treating \(a+s\) as variable** | The derivation assumes the only change is HA ⇌ A⁻. If \(a+s\) were allowed to change, you would be mixing in dilution or precipitation effects, which are not part of the basic buffer‑capacity definition. | Explicitly write \(s = C_{\text{tot}}-a\) and keep \(C_{\text{tot}}\) fixed throughout the differentiation. |
| **Using activities instead of concentrations** (e.g., writing \(K_a = \frac{a_{\mathrm{H^{+}}}a_{\mathrm{A^{-}}}}{a_{\mathrm{HA}}}\)) | For the high‑school level, activity coefficients are unnecessary and obscure the simple algebra. In dilute solutions activities ≈ concentrations. | Replace every activity symbol \(a_i\) by the concentration \([i]\) and omit activity coefficients. |
| **Assuming the volume changes when a small amount of acid/base is added** | Buffer capacity is defined for an **infinitesimal** addition, so volume change is negligible. | Keep the volume constant; treat the addition as a concentration change, not a bulk‑solution change. |
| **Confusing the sign when a strong acid (instead of base) is added** | Adding acid *increases* \(a\) and *decreases* \(s\); the formula \(-da/d\mathrm{pH}\) still works because \(da\) is now positive while pH falls, giving a positive \(\beta\). | Remember that \(\beta\) is always a positive magnitude; the sign of \(da\) simply follows the direction of the added strong acid or base. |

--- 

*With the steps above you can see that the textbook definition \(\displaystyle\beta = -\frac{da}{d\mathrm{pH}}\) is just a compact way of expressing “how many moles of strong acid or base are needed to change the pH by one unit”, using the fact that adding the strong titrant converts HA into A⁻ while keeping the total buffer concentration fixed.*

*Original question: [Why is buffer capacity defined like that](https://chemistry.stackexchange.com/questions/195952/why-is-buffer-capacity-defined-like-that) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
