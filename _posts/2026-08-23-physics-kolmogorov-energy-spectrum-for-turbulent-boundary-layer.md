---
layout: post
title: Kolmogorov/Energy spectrum for turbulent boundary layer
author: StemFix Bot
category: physics
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1.  What the student is asking (plain‑language restatement)

The student has already measured the **3‑D energy spectrum** of a *homogeneous, isotropic* turbulent field by

1. taking a 3‑D Fourier transform of the velocity data (periodic in *x*, *y*, *z*),  
2. binning the Fourier coefficients by the magnitude of the wavenumber **k**, and  
3. obtaining the familiar \(E(k)\sim k^{-5/3}\) inertial‑range law.

Now the student wants to do the same for a **turbulent boundary layer** where the flow is **anisotropic** and **non‑periodic in the wall‑normal direction** (let us call it \(y\)).  

The questions are:

1. **How can we compute an energy spectrum for a fully three‑dimensional turbulent boundary layer?**  
2. **If a 3‑D spectrum is impossible, how do we define “scales” (or a spectrum) in the wall‑normal direction?**  

In other words: *What mathematical tools replace the simple 3‑D FFT when one direction is bounded, and how do we interpret the resulting spectra?*  

Below is a complete, step‑by‑step guide that answers both points.

---

## 2.  Step‑by‑step solution  

### 2.1  Review: Energy spectrum in a homogeneous, isotropic flow  

For a velocity field \(\mathbf{u}(\mathbf{x})\) defined in a periodic box of size \(L_x\times L_y\times L_z\),

1. Compute the discrete Fourier transform (DFT)  

   \[
   \hat{\mathbf{u}}(\mathbf{k}) = \frac{1}{N_x N_y N_z}
   \sum_{n_x=0}^{N_x-1}\!\!\sum_{n_y=0}^{N_y-1}\!\!\sum_{n_z=0}^{N_z-1}
   \mathbf{u}(x_{n_x},y_{n_y},z_{n_z})\,
   e^{-i\mathbf{k}\cdot\mathbf{x}},
   \]

   where \(\mathbf{k}=(k_x,k_y,k_z)=\bigl(2\pi m_x/L_x,2\pi m_y/L_y,2\pi m_z/L_z\bigr)\).

2. The **spectral energy density** (per unit wavenumber) is  

   \[
   E(\mathbf{k}) = \frac12\bigl|\hat{\mathbf{u}}(\mathbf{k})\bigr|^{2}.
   \]

3. Because the flow is isotropic, one can collapse the 3‑D data into a **1‑D spectrum** by binning all modes that have the same wavenumber magnitude  

   \[
   k = \|\mathbf{k}\| = \sqrt{k_x^{2}+k_y^{2}+k_z^{2}} .
   \]

   The binned value  

   \[
   E(k) = \sum_{k\le\|\mathbf{k'}\|<k+\Delta k} E(\mathbf{k'}).
   \]

4. In the inertial range, \(E(k) \propto \varepsilon^{2/3}k^{-5/3}\) (Kolmogorov).

All of the above relies on **periodicity** (or at least statistical homogeneity) in the three directions. In a turbulent boundary layer, only the streamwise (\(x\)) and spanwise (\(z\)) directions are (approximately) homogeneous; the wall‑normal direction (\(y\)) is bounded by the wall and by the free stream, so we cannot use a plain FFT there.

---

### 2.2  What can we still do? – Use the two homogeneous directions

Because the flow is **statistically homogeneous** in \(x\) and \(z\), we can still Fourier‑transform in those two directions **exactly as before**:

\[
\hat{\mathbf{u}}(k_x, y, k_z) 
= \frac{1}{N_x N_z}
\sum_{n_x=0}^{N_x-1}\!\!\sum_{n_z=0}^{N_z-1}
\mathbf{u}(x_{n_x},y, z_{n_z})\,
e^{-i(k_x x_{n_x}+k_z z_{n_z})}.
\]

The result is a **2‑D spectral field** that still depends on the wall‑normal coordinate \(y\). For each pair \((k_x,k_z)\) we have a complex vector that varies with \(y\).

#### 2.2.1  2‑D (streamwise–spanwise) energy spectrum at a given wall‑normal location  

Define the **local** spectral density

\[
E(k_x,k_z; y) = \frac12 \bigl| \hat{\mathbf{u}}(k_x, y, k_z) \bigr|^{2}.
\]

If you want a **one‑dimensional** spectrum at a fixed wall‑normal plane (e.g. at \(y=y_0\)), you can collapse the 2‑D data in the usual way:

\[
E(k; y_0)=\sum_{\sqrt{k_x^{2}+k_z^{2}} \in [k,\,k+\Delta k]} E(k_x,k_z; y_0),
\]

which yields a **planar energy spectrum** that is still expected to follow \(k^{-5/3}\) over the inertial range (provided \(y_0\) is not too close to the wall).

---

### 2.3  Extending to a **3‑D** spectrum: treat the wall‑normal direction with a non‑periodic basis  

If we truly want a 3‑D spectral representation, we must replace the Fourier series in \(y\) by a set of orthogonal functions that respect the *boundary conditions*:

| Boundary condition | Suitable basis | Remarks |
|--------------------|----------------|---------|
| No‑slip wall at \(y=0\) and free‑stream (or symmetry) at \(y=h\) | **Chebyshev polynomials** (type‑I or type‑II) or **sine/cosine series** with appropriate parity | Common in DNS of channel / boundary‑layer flow |
| Wall‑bounded, non‑periodic, but still homogeneous in the *statistical* sense | **Discrete Cosine Transform (DCT)** (even extension) or **Discrete Sine Transform (DST)** (odd extension) | Simpler to implement than Chebyshev, retains orthogonality on a uniform grid |
| Complex geometry (curved wall) | **Proper Orthogonal Decomposition (POD)** or **Dynamic Mode Decomposition (DMD)** | Gives a data‑driven modal basis; not a wavenumber spectrum per se, but a scale‑decomposition |

Below we outline the **Chebyshev‑spectral** approach because it is the most widely used in wall‑bounded DNS.

#### 2.3.1  Chebyshev expansion in \(y\)

1. Map the physical wall‑normal interval \([0,\,\delta]\) (or \([0,\,h]\)) to the Chebyshev domain \([-1,\,1]\) via  

   \[
   \eta = 2\frac{y}{\delta} - 1 .
   \]

2. Expand the wall‑normal dependence of each Fourier mode \((k_x,k_z)\) as  

   \[
   \hat{\mathbf{u}}(k_x, y, k_z) = 
   \sum_{n=0}^{N_y-1} \tilde{\mathbf{u}}_{n}(k_x,k_z)\, T_n(\eta),
   \]

   where \(T_n\) is the *n*-th Chebyshev polynomial.

3. The **Chebyshev coefficients** \(\tilde{\mathbf{u}}_{n}\) are obtained with a **Fast Chebyshev Transform (FCT)**, which is analogous to an FFT but uses the cosine recurrence relation.

4. Define the **3‑D spectral energy density**  

   \[
   E(k_x, k_z, n) = \frac12 \bigl| \tilde{\mathbf{u}}_{n}(k_x,k_z) \bigr|^{2}.
   \]

5. If you wish to obtain a **scalar wavenumber magnitude** you can construct a *generalised* wavenumber in the wall‑normal direction:

   \[
   k_y^{(n)} \equiv \frac{n\pi}{\delta}\quad\text{(approximate mapping of Chebyshev index to physical wavenumber)}.
   \]

   Then the **pseudo‑3‑D isotropic spectrum** is built by binning over shells in \((k_x, k_y^{(n)}, k_z)\):

   \[
   E(k) = \sum_{\sqrt{k_x^{2}+k_y^{(n)2}+k_z^{2}} \in [k,\,k+\Delta k]} 
           E(k_x,k_z,n).
   \]

   **Caveat:** Because the wall‑normal direction is not truly homogeneous, the interpretation of \(k_y\) is only *approximate*; nevertheless, the procedure is useful for visualising how energy is distributed across wall‑normal “scales”.

#### 2.3.2  Practical algorithm (pseudo‑code)

```python
# data: u[x, y, z]  (x,z periodic, y bounded)
# 1. FFT in x and z
U_kxkz = fft2(u, axes=(0,2))               # shape (Nx, Ny, Nz)

# 2. Chebyshev transform in y for each (kx,kz)
U_hat = np.zeros_like(U_kxkz, dtype=complex)
for ix in range(Nx):
    for iz in range(Nz):
        U_hat[ix,:,iz] = cheb_transform(U_kxkz[ix,:,iz])   # returns N_y coeffs

# 3. Spectral energy
E = 0.5 * np.abs(U_hat)**2                     # shape (Nx, Ny, Nz)

# 4. (optional) map Chebyshev index to k_y and bin in spherical shells
k_y = np.pi * np.arange(Ny) / delta
k_mag = np.sqrt(kx_grid**2 + k_y[:,None,None]**2 + kz_grid**2)
E_shell = bin_into_shells(k_mag, E, dk)
```

---

### 2.4  If you **do not** need a full 3‑D spectrum

Most experimental and DNS analyses of wall‑bounded turbulence use **one‑dimensional spectra** defined on *planar cuts*:

| Spectrum | Definition | Typical use |
|----------|------------|-------------|
| **Streamwise spectrum** \(E_{uu}(k_x; y)\) | \(E_{uu}(k_x; y) = \frac12\sum_{k_z} |\hat{u}(k_x,y,k_z)|^{2}\) | Energy distribution along the streamwise direction at a given \(y\). |
| **Spanwise spectrum** \(E_{uu}(k_z; y)\) | analogous | Checks isotropy in the homogeneous plane. |
| **Pre‑multiplied spectrum** \(k_x E_{uu}(k_x; y)\) | Highlights contribution per logarithmic band. | Useful for identifying the “\(k^{-1}\)” region in the near‑wall logarithmic layer. |
| **Wall‑normal “spectral density”** | \(E_{uu}(y;k_y)\) obtained via Chebyshev/DCT as described above. | Gives a scale‑by‑scale picture of how energy varies with distance from the wall. |

These spectra are **local** in \(y\): each wall‑normal location is treated independently, which is permissible because the flow is *inhomogeneous* only in that direction.

---

### 2.5  Defining **scales** in the wall‑normal direction  

In a boundary layer we use **inner (viscous) scaling** and **outer (geometric) scaling**:

| Region | Length scale | Velocity scale | Typical non‑dimensional coordinate |
|--------|--------------|----------------|------------------------------------|
| Viscous sublayer (\(y^+ \lesssim 5\)) | Viscous length \(\ell_\nu = \nu / u_\tau\) | Friction velocity \(u_\tau\) | \(y^+ = y u_\tau / \nu\) |
| Buffer layer (\(5 \lesssim y^+ \lesssim 30\)) | Same as above | Same | \(y^+\) |
| Logarithmic layer (\(30 \lesssim y^+ \lesssim 0.15 \, Re_\tau\)) | Outer length \(\delta\) (boundary‑layer thickness) | \(u_\tau\) | \(y^+ = y u_\tau/\nu\) and \(y/\delta\) |
| Outer region (\(y/\delta \sim O(1)\)) | \(\delta\) | Free‑stream velocity \(U_\infty\) | \(y/\delta\) |

These non‑dimensional variables replace a single “global” integral length scale

*Original question: [Kolmogorov/Energy spectrum for turbulent boundary layer](https://physics.stackexchange.com/questions/110310/kolmogorov-energy-spectrum-for-turbulent-boundary-layer) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
