---
layout: question
title: Relating definitions of the k-basis
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Relating definitions of the k-basis'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the question is asking – in plain language  

A student has seen two ways of talking about the **\(k\)‑basis** (often called the *reciprocal* or *momentum* basis) in quantum mechanics / wave‑physics:

1. **“Frequency‑space” picture** – we say that the set of vectors \(\{|k\rangle\}\) spans a space whose coordinate is the **wave‑number** (or frequency) \(k\).  
2. **Operator‑eigenvector picture** – we say that the same set of vectors satisfies  

\[
\hat D\,|k\rangle = i k \,|k\rangle ,\qquad\text{with }\hat D\equiv\frac{d}{dx}\;.
\]

The student wonders how these two descriptions are related. In particular, why does the eigenvalue appear as the *imaginary* number \(i k\), and how does that connect with the idea that the basis “spans frequency space”?

Our job is to show, step‑by‑step, that the two definitions are *exactly the same* thing: the eigenvectors of the differential operator \(\hat D\) are precisely the plane waves \(\exp(i k x)\), which are the building blocks of the Fourier transform. The Fourier coefficients are the components of a state in the \(k\)-basis, i.e. its “coordinates” in frequency space.

---

## 2. Detailed derivation  

### 2.1  The differential operator in the position representation  

In the **position representation** a state \(|\psi\rangle\) is represented by the wave‑function  

\[
\psi(x)=\langle x|\psi\rangle .
\]

The operator \(\hat D\) acts on kets as \(\hat D|\psi\rangle\).  
Its matrix element in the \(|x\rangle\) basis is

\[
\langle x|\hat D|\psi\rangle = \frac{d}{dx}\psi(x) .
\]

Thus, in this representation \(\hat D\) **is** the ordinary derivative with respect to the coordinate \(x\).

---

### 2.2  Solving the eigenvalue equation  

We look for kets \(|k\rangle\) that satisfy  

\[
\hat D|k\rangle = i k |k\rangle .
\]

Take the position representation of both sides:

\[
\langle x|\hat D|k\rangle = \frac{d}{dx}\langle x|k\rangle 
      = i k \,\langle x|k\rangle .
\]

Denote the *position‑space wave‑function* of \(|k\rangle\) by  

\[
\phi_k(x) \equiv \langle x|k\rangle .
\]

The eigenvalue equation becomes the ordinary differential equation  

\[
\frac{d\phi_k(x)}{dx}= i k\,\phi_k(x) .
\]

Its solution is immediate:

\[
\boxed{\;\phi_k(x)=\langle x|k\rangle =\frac{1}{\sqrt{2\pi}}\,e^{i k x}\;},
\]

where we have inserted the conventional normalisation factor \((2\pi)^{-1/2}\).  
Any overall constant would also be an eigenfunction; the factor is chosen so that the eigenkets are **δ‑normalised** (see below).

Thus the eigenvectors of \(\hat D\) are exactly the *plane‑wave* functions \(e^{i k x}\).

---

### 2.3  Orthogonality and completeness of the \(|k\rangle\) set  

Using the chosen normalisation we obtain

\[
\langle k'|k\rangle = \int_{-\infty}^{\infty}\!dx\,
      \phi_{k'}^{*}(x)\,\phi_k(x)
   =\frac{1}{2\pi}\int_{-\infty}^{\infty}dx\,
      e^{-i k' x}\,e^{i k x}
   =\delta(k-k') .
\]

Hence the \(|k\rangle\) are **orthogonal** in the Dirac‑δ sense.

The **completeness relation** follows from the Fourier inversion theorem:

\[
\int_{-\infty}^{\infty}\! dk\,|k\rangle\langle k|
   =\int_{-\infty}^{\infty}\! dk\,
      \Bigl(\int\!dx\,|x\rangle\phi_k(x)\Bigr)
      \Bigl(\int\!dx'\,\phi_k^{*}(x')\langle x'|\Bigr)
   =\int\!dx\,|x\rangle\langle x| =\mathbb{1}.
\]

So the set \(\{|k\rangle\}\) *spans* the whole Hilbert space, exactly as a basis does.

---

### 2.4  Expansion of an arbitrary state – the Fourier transform  

Take any square‑integrable wave‑function \(\psi(x)\). Insert the identity \(\mathbb{1}= \int dk\,|k\rangle\langle k|\) :

\[
|\psi\rangle = \int_{-\infty}^{\infty}\! dk\,|k\rangle\langle k|\psi\rangle .
\]

Define the **\(k\)-space (frequency‑space) amplitude**

\[
\tilde\psi(k) \equiv \langle k|\psi\rangle .
\]

In the position representation we have

\[
\psi(x)=\langle x|\psi\rangle
       =\int_{-\infty}^{\infty}\! dk\,
          \langle x|k\rangle\tilde\psi(k)
       =\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\! dk\,
          e^{i k x}\,\tilde\psi(k) .
\]

The inverse relation (obtained by multiplying by \(\langle k|\) ) is

\[
\boxed{\;\tilde\psi(k)=\langle k|\psi\rangle
      =\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\! dx\,
        e^{-i k x}\,\psi(x)\;},
\]

which is precisely the **Fourier transform** of \(\psi(x)\).  

Thus *the coordinates of a state in the \(|k\rangle\) basis are exactly its Fourier components*, i.e. its representation in “frequency space”.

---

### 2.5  Why the eigenvalue is \(i k\) (the 90° rotation)  

The operator \(\hat D = d/dx\) is **anti‑Hermitian**:

\[
\hat D^\dagger = -\frac{d}{dx} = -\hat D .
\]

Multiplying an anti‑Hermitian operator by \(i\) makes it **Hermitian**:

\[
\hat p \equiv -i\hat D = -i\frac{d}{dx}
\]

is the familiar *momentum operator* (in units \(\hbar=1\)). Its eigenvalue equation is  

\[
\hat p|k\rangle = k|k\rangle .
\]

Hence the appearance of the factor \(i\) in the original statement simply reflects the convention of calling the derivative itself the “generator of translations”. The eigenvalue \(i k\) is purely imaginary because the derivative operator rotates a complex exponential by a phase of \(90^\circ\) (multiplication by \(i\)). In physics we usually absorb that \(i\) into the definition of the observable (momentum) so that eigenvalues are real.

---

### 2.6  Summary of the relationship  

| **Frequency‑space picture** | **Operator‑eigenvector picture** |
|-----------------------------|-----------------------------------|
| Basis vectors labelled by a continuous parameter \(k\) (wave‑number). | Kets \(|k\rangle\) satisfy \(\hat D|k\rangle = i k|k\rangle\). |
| Any state \(\psi(x)\) can be written as a Fourier integral over \(k\). | The coefficients \(\tilde\psi(k)=\langle k|\psi\rangle\) are the Fourier amplitudes. |
| Orthogonality: \(\int dx\, e^{i(k-k')x}=2\pi\delta(k-k')\). | Dirac‑δ orthogonality: \(\langle k'|k\rangle = \delta(k-k')\). |
| Completeness: \(\int dk\, e^{ik(x-x')} = 2\pi\delta(x-x')\). | Completeness: \(\int dk\,|k\rangle\langle k| = \mathbb{1}\). |

Consequently, **the “\(k\)-basis” that spans frequency space is precisely the set of eigenkets of the differential operator \(\frac{d}{dx}\); the Fourier transform is the change of representation from the position basis \(\{|x\rangle\}\) to the \(k\)-basis \(\{|k\rangle\}\).**

---

## 3. Final answer  

The two definitions are equivalent:

*The eigenkets of the derivative operator \(\hat D=\frac{d}{dx}\) are the plane‑wave states \(\langle x|k\rangle = (2\pi)^{-1/2}e^{ikx}\). These kets form a continuous, δ‑normalised basis \(\{|k\rangle\}\) that spans the Hilbert space. Expanding any state in this basis yields the Fourier transform, i.e. the coordinates of the state in “frequency space”. The factor \(i\) in the eigenvalue equation simply reflects that \(\hat D\) is anti‑Hermitian; multiplying by \(i\) gives the Hermitian momentum operator whose eigenvalues \(k\) are real.*

---

## 4. Common mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Thinking \(\hat D\) has *real* eigenvalues.** | \(\hat D = d/dx\) is anti‑Hermitian, so its eigenvalues are purely imaginary. | Remember to write the eigenvalue equation as \(\hat D|k\rangle = i k |k\rangle\) (or define \(\hat p=-i\hat D\) to get real eigenvalues). |
| **Forgetting the normalisation factor \((2\pi)^{-1/2}\).** | Without it the orthogonality relation yields a factor of \(2\pi\) instead of a Dirac delta. | Choose the conventional normalisation so that \(\langle k'|k\rangle = \delta(k-k')\). |
| **Confusing the position and momentum (k) bases.** | Writing \(\psi(x)=\int dk\, e^{ikx}\tilde\psi(k)\) without the \(\frac{1}{\sqrt{2\pi}}\) leads to inconsistent inverse transforms. | Derive both forward and inverse Fourier transforms explicitly from the completeness relation. |
| **Treating \(|k\rangle\) as a *vector* in ordinary 3‑D space.** | \(|k\rangle\) lives in abstract Hilbert space; its “components” are functions of the continuous variable \(k\). | Emphasise Dirac notation: \(|k\rangle\) is a ket, \(\langle x|k\rangle\) is its wave‑function. |
| **Assuming the eigenvalue equation holds for *any* function**. | Only the plane waves satisfy \(\frac{d}{dx}f = i k f\). | Verify by substitution: differentiate \(e^{ikx}\) to see it reproduces the same function multiplied by \(ik\). |

By keeping these points in mind, the connection between the frequency‑space basis and the eigenbasis of the differential operator becomes clear and error‑free.

*Original question: [Relating definitions of the k-basis](https://physics.stackexchange.com/questions/875968/relating-definitions-of-the-k-basis) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
