---
layout: question
title: Chemical (engineering) thermodynamics — how do we define the component fugacity?
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: Chemical (engineering) thermodynamics
  — how do we define the component fugacity?'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the question is really asking  

The student is trying to understand **how the fugacity of a component in a mixture is defined** and why the textbook definition  

\[
RT\,d\ln \hat f_i=(d\mu_i)_T\tag{1}
\]

does not seem to give a unique value (any factor that depends only on temperature could be multiplied onto \(\hat f_i\) and still satisfy the differential relation).  
The student also sees another definition that ties fugacity to the chemical potential of a **real pure gas** by  

\[
\mu_i^{\text{real}}=\mu_i^{\ominus}+RT\ln\frac{f_i}{P^{\ominus}}\tag{2}
\]

and wonders how these two ideas are related, what the role of the *reference (standard) state* is, and how the *fugacity coefficient* \(\phi_i\) enters.  

In short:  

* What is the precise definition of the component fugacity \(f_i\) (or \(\hat f_i\)) in a mixture?  
* Why does Eq. (1) not lead to an arbitrary constant?  
* How does the “pressure that an ideal gas would need to have to give the same μ” definition fit in?  

---

## 2. Full derivation – from the differential definition to an explicit expression  

### 2.1. Starting point: the differential relation  

For any component \(i\) in a multicomponent system the **chemical potential** \(\mu_i\) is a state function.  
At constant temperature the exact differential of \(\mu_i\) can be written as  

\[
\left(d\mu_i\right)_T = RT\, d\ln f_i\tag{3}
\]

where \(f_i\) is called the **fugacity of component \(i\)**.  Equation (3) is *the definition* of fugacity; it tells us that the natural logarithm of fugacity is, up to the factor \(RT\), the thermodynamic potential conjugate to the amount of component \(i\) at fixed \(T\).

> **Why a differential?**  
>  Because \(\mu_i\) is only defined up to an additive constant.  By relating *changes* in \(\mu_i\) to *changes* in \(\ln f_i\) we avoid having to guess that constant.  The constant will be fixed later by specifying a **reference (standard) state**.

### 2.2. Integration – introducing the reference state  

Integrate Eq. (3) from a convenient reference state “0” (denoted by a superscript \(0\)) to the actual state of interest:

\[
\int_{\mu_i^{0}}^{\mu_i} d\mu_i = RT\int_{f_i^{0}}^{f_i} \frac{d f_i'}{f_i'}  
\quad\Longrightarrow\quad
\mu_i-\mu_i^{0}=RT\ln\frac{f_i}{f_i^{0}}.\tag{4}
\]

Equation (4) is the **integrated definition** of fugacity.  
The two quantities that still need to be chosen are:

| Symbol | Meaning |
|--------|---------|
| \(\mu_i^{0}\) | Chemical potential of component \(i\) in a *standard state* at the same temperature (and, for gases, the same pressure). |
| \(f_i^{0}\) | Fugacity of component \(i\) **in that same standard state**. |

If we pick the standard state to be an *ideal gas* at the same temperature and pressure as the real fluid, then by definition

\[
f_i^{0}=P \qquad\text{(ideal‑gas fugacity equals the pressure)}\tag{5}
\]

and the standard‑state chemical potential is the ideal‑gas chemical potential \(\mu_i^{\text{ig}}\).  Substituting (5) into (4) gives the **more familiar expression**

\[
\boxed{\;\mu_i = \mu_i^{\text{ig}} + RT\ln\frac{f_i}{P}\;}\tag{6}
\]

which is exactly the relation you saw in the LibreTexts article (they write \(P^{\ominus}\) for the chosen standard pressure, often 1 bar).

### 2.3. Uniqueness – why we cannot multiply by an arbitrary function of \(T\)

Suppose we replace \(f_i\) by \(c(T)f_i\) where \(c(T)\) depends only on temperature.  
Equation (3) would indeed still hold because at constant \(T\),

\[
d\ln[c(T)f_i]=d\ln f_i+\underbrace{d\ln c(T)}_{=0}=d\ln f_i .
\]

However, after **integration** we must also replace the reference fugacity:

\[
\mu_i-\mu_i^{0}=RT\ln\frac{c(T)f_i}{c(T)f_i^{0}}=RT\ln\frac{f_i}{f_i^{0}} .
\]

The factor \(c(T)\) cancels **provided we use the same factor for the reference state**.  Consequently, the *absolute* value of fugacity is not determined until we **declare a standard state** (i.e., we fix \(\mu_i^{0}\) and \(f_i^{0}\)).  The usual convention is the ideal‑gas reference at the same \(T\) and \(P\); this makes the fugacity **unique** for a given real state.

Thus the “arbitrariness” is only apparent; it is removed by the conventional choice of standard state.

### 2.4. Component fugacity in a **mixture**  

For a **gas mixture** the total pressure is \(P\) and the mole fraction of component \(i\) is \(y_i\).  
If the mixture behaves ideally, the chemical potential of component \(i\) is

\[
\mu_i^{\text{ig}} = \mu_i^{\ominus} + RT\ln\frac{y_i P}{P^{\ominus}} .
\]

For a *real* mixture we define the **fugacity coefficient** \(\phi_i\) by

\[
f_i \equiv \phi_i \, y_i P \tag{7}
\]

so that (6) becomes

\[
\mu_i = \mu_i^{\ominus} + RT\ln\frac{y_i P}{P^{\ominus}} + RT\ln\phi_i .
\]

Equation (7) is the *working definition* of the **component fugacity** in a gas mixture.  
The same idea works for liquids, where we use the liquid‑phase standard state (often the pure liquid at the system temperature and 1 bar) and write

\[
f_i = \gamma_i \, x_i \, f_i^{\ast} \quad\text{(liquid)}\tag{8}
\]

with \(\gamma_i\) the activity coefficient and \(f_i^{\ast}\) the fugacity of the pure liquid.

---

## 3. Final answer – concise statement  

1. **Definition (differential form)**  

\[
RT\,d\ln f_i = (d\mu_i)_T
\]

2. **Integrated form (with a chosen standard state)**  

\[
\mu_i = \mu_i^{0} + RT\ln\frac{f_i}{f_i^{0}}
\]

   – If the standard state is the ideal gas at the same \(T\) and \(P\), then \(f_i^{0}=P\) and  

\[
\boxed{\mu_i = \mu_i^{\text{ig}} + RT\ln\frac{f_i}{P}}
\]

3. **Component fugacity in a gas mixture**  

\[
\boxed{f_i = \phi_i \, y_i P}
\]

   where \(\phi_i\) is the fugacity coefficient (dimensionless) that quantifies the deviation from ideal‑gas behaviour.

4. **Uniqueness** – The fugacity is uniquely defined once a **reference (standard) state** is specified; any temperature‑only factor cancels out when the same factor is used for the reference state, so the apparent arbitrariness disappears.

---

## 4. Common mistakes  

| Mistake | Why it is wrong | How to avoid it |
|---------|----------------|-----------------|
| **Treating (1) as an absolute definition** and forgetting to specify a reference state. | Without a reference, \(\mu_i\) and \(f_i\) are defined only up to an additive constant, leading to the “any \(c(T)\) works” confusion. | Always write the integrated form (4) and state the chosen standard state (ideal gas at the same \(T,P\) is the usual convention). |
| **Identifying fugacity with pressure for *any* gas**. | Only true for an *ideal* gas; for real gases a fugacity coefficient \(\phi_i\neq 1\) is needed. | Use \(f_i = \phi_i y_i P\) for real gas mixtures; set \(\phi_i=1\) only after proving the gas is ideal. |
| **Mixing up the pure‑component fugacity \(f_i^{\ast}\) and the mixture fugacity \(f_i\)**. | \(f_i^{\ast}\) is the fugacity of the pure component at the system temperature and a reference pressure; \(f_i\) is the effective pressure that the component experiences in the mixture. | Keep the notation clear: \(f_i^{\ast}\) (pure) vs. \(f_i = \phi_i y_i P\) (mixture). |
| **Using the pressure of the mixture instead of the *partial* pressure** in Eq. (7). | The partial pressure of component \(i\) in an ideal mixture is \(y_i P\); inserting the total pressure would over‑estimate fugacity. | Remember the factor \(y_i\) belongs with the pressure when writing \(f_i = \phi_i y_i P\). |
| **Neglecting temperature dependence of the standard chemical potential \(\mu_i^{0}(T)\)**. | \(\mu_i^{0}\) varies with \(T\); assuming it is constant gives wrong values for \(\mu_i\). | Use tabulated values or equations of state for \(\mu_i^{0}(T)\) (e.g., ideal‑gas reference). |

--- 

**Bottom line:**  
Fugacity is defined through the exact differential relation (1).  By integrating from a well‑chosen standard state—most commonly the ideal gas at the same temperature and pressure—we obtain an explicit, unique expression that links the real‑fluid chemical potential to an “effective pressure” \(f_i\).  In mixtures the component fugacity is simply the product of the mole fraction, the total pressure, and a dimensionless fugacity coefficient that measures non‑ideality.

*Original question: [Chemical (engineering) thermodynamics — how do we define the component fugacity?](https://chemistry.stackexchange.com/questions/195863/chemical-engineering-thermodynamics-how-do-we-define-the-component-fugacity) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
