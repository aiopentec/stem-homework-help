---
layout: question
title: Impulsive Friction
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Impulsive Friction'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

## 1. What the problem is asking (in plain language)

A spinning ball hits a rough horizontal floor.  
During the very short impact the floor supplies  

* a **normal impulse** \(I\) (perpendicular to the floor) and  
* a **tangential impulse** caused by friction.

If the ball is slipping at the contact point, Coulomb’s law tells us that the *maximum* possible magnitude of the frictional impulse is \(\mu I\) (the coefficient of friction \(\mu\) times the normal impulse).

Sometimes the impulse \(\mu I\) would be **larger** than the impulse actually needed to bring the relative velocity of the contact point to zero. If we applied the full \(\mu I\) the contact point would start moving the opposite way, which would immediately reverse the direction of friction – an impossibility for a single, instantaneous impulse.

**Question:**  
What is the *actual* frictional impulse that the floor delivers?  
Is it the full \(\mu I\) or is it only the impulse required to stop the slip (the “minimum” impulse)?

---

## 2. Detailed solution (step‑by‑step)

### 2.1. Geometry and notation

| Symbol | Meaning |
|--------|---------|
| \(m\) | mass of the ball |
| \(R\) | radius of the ball |
| \(\mathbf{v}\) | linear velocity of the centre of mass (COM) **just before** impact |
| \(\boldsymbol{\omega}\) | angular velocity **just before** impact (positive when the ball spins clockwise as seen from the right) |
| \(\mathbf{n}\) | unit normal to the floor (upward) |
| \(\mathbf{t}\) | unit tangent in the plane of the floor (horizontal, direction of slip) |
| \(I\) | normal impulse (scalar, positive upward) |
| \(J_t\) | tangential (friction) impulse (scalar, positive opposite to the slip direction) |
| \(\mu\) | coefficient of kinetic (Coulomb) friction |
| \(\mathbf{e}_x,\mathbf{e}_y,\mathbf{e}_z\) | Cartesian basis (take the floor as the \(x\!-\!y\) plane, \(z\) upward) |

The moment of inertia of a solid sphere about its centre is  

\[
I_{\text{cm}} = \frac{2}{5}\,mR^{2}.
\]

### 2.2. Relative velocity at the contact point

Let the ball approach the floor with a horizontal velocity \(v\) (in the \(+x\) direction) and spin with angular velocity \(\omega\) about the \(y\)-axis (so the top of the ball moves forward).  
The velocity of the point of the sphere that contacts the floor is

\[
\mathbf{v}_c = \mathbf{v} + \boldsymbol{\omega}\times(-R\mathbf{n})
            = v\,\mathbf{e}_x - \omega R\,\mathbf{e}_x
            = (v-\omega R)\,\mathbf{e}_x .
\]

Thus the **slip velocity** just before impact is  

\[
u \equiv v_{\text{slip}} = v-\omega R .
\]

If \(u>0\) the contact point slides **forward** relative to the floor; if \(u<0\) it slides **backward**.

### 2.3. Impulse–momentum equations

During the impact the only external impulses are the normal impulse \(I\) and the friction impulse \(J_t\) (both applied at the contact point).  

#### Linear momentum (horizontal)

\[
m(v^{+}-v) = -J_t .
\tag{1}
\]

(The minus sign appears because the friction impulse opposes the slip direction.)

#### Angular momentum about the centre

\[
I_{\text{cm}}(\omega^{+}-\omega) = -R J_t .
\tag{2}
\]

(The torque of the friction impulse about the centre is \(\mathbf{r}\times\mathbf{J}_t = (-R\mathbf{n})\times(-J_t\mathbf{t}) = -R J_t\mathbf{e}_y\).)

#### Post‑impact slip velocity

\[
u^{+}= v^{+}-\omega^{+}R .
\]

Using (1) and (2),

\[
\begin{aligned}
v^{+} &= v - \frac{J_t}{m},\\[4pt]
\omega^{+} &= \omega - \frac{R J_t}{I_{\text{cm}}}.
\end{aligned}
\]

Hence

\[
\begin{aligned}
u^{+} &= \Bigl(v-\frac{J_t}{m}\Bigr) - 
        \Bigl(\omega-\frac{R J_t}{I_{\text{cm}}}\Bigr)R\\[4pt]
      &= (v-\omega R) - J_t\!\left(\frac{1}{m} -\frac{R^{2}}{I_{\text{cm}}}\right).
\end{aligned}
\tag{3}
\]

Introduce the *effective slip‑mass*  

\[
\frac{1}{m_{\text{eff}}}\equiv\frac{1}{m} -\frac{R^{2}}{I_{\text{cm}}}.
\]

For a solid sphere  

\[
\frac{1}{m_{\text{eff}}}= \frac{1}{m}-\frac{R^{2}}{(2/5)mR^{2}}
= \frac{1}{m}-\frac{5}{2m}= -\frac{3}{2m},
\]

so that  

\[
m_{\text{eff}} = -\frac{2}{3}m .
\]

(The negative sign simply tells us that a *forward* friction impulse reduces the slip velocity.)

Equation (3) can now be written compactly as  

\[
u^{+}=u - \frac{J_t}{m_{\text{eff}}}.
\tag{4}
\]

### 2.4. Two possible regimes

1. **Slip continues** (Coulomb kinetic friction).  
   The friction magnitude is limited only by the Coulomb bound:

   \[
   |J_t| = \mu I .
   \tag{5}
   \]

   The sign of \(J_t\) is opposite to the sign of \(u\) (it opposes slip).

2. **Sticking (no slip after impact).**  
   This occurs when the impulse needed to bring \(u^{+}\) to zero is **smaller** than the Coulomb limit.  
   The impulse required to stop slip is obtained from (4) by setting \(u^{+}=0\):

   \[
   J_t^{*}= m_{\text{eff}}\,u .
   \tag{6}
   \]

   Its magnitude is  

   \[
   |J_t^{*}| = \bigl|m_{\text{eff}}\bigr|\,|u|.
   \]

   If \(|J_t^{*}| \le \mu I\) the floor can supply exactly that amount, and the contact point will *stick* (relative velocity becomes zero).  

   If \(|J_t^{*}| > \mu I\) the friction limit is reached first; the ball continues to slip and the impulse is \(\pm\mu I\).

### 2.5. Which impulse actually occurs?

The actual frictional impulse is therefore the **minimum** of the two admissible magnitudes:

\[
\boxed{ \; J_t = \operatorname{sgn}(-u)\;\min\!\bigl(\mu I,\;|J_t^{*}|\bigr) \;}
\tag{7}
\]

where  

\[
|J_t^{*}| = \bigl|m_{\text{eff}}\bigr|\,|u|
            = \frac{2}{3}m\,|\,v-\omega R\,| .
\]

In words:

* If the impulse needed to stop the slip, \(\displaystyle \frac{2}{3}m\,|v-\omega R|\), is **smaller** than \(\mu I\), the floor supplies exactly that amount; the contact point sticks and the frictional impulse is **not** the full \(\mu I\).

* If the required impulse is **larger** than \(\mu I\), the friction reaches its Coulomb limit and the impulse is \(\pm\mu I\); slip persists after the impact.

Thus the actual frictional impulse is **never larger** than the impulse required to bring the relative velocity to zero; it is whichever is **smaller** between \(\mu I\) and the “sticking” impulse.

---

## 3. Final answer

The frictional impulse delivered during the impact is  

\[
\boxed{ \displaystyle 
J_t = \operatorname{sgn}(\omega R - v)\,
\min\!\Bigl(\mu I,\;\frac{2}{3}\,m\,|v-\omega R|\Bigr) } .
\]

- The sign is opposite to the initial slip direction (it always opposes the relative motion).  
- If \(\displaystyle \frac{2}{3}m|v-\omega R| \le \mu I\) the contact point sticks after impact and the impulse equals the *minimum* needed to stop slip.  
- If \(\displaystyle \frac{2}{3}m|v-\omega R| > \mu I\) the frictional impulse saturates at the Coulomb limit \(\mu I\) and slip continues.

---

## 4. Common mistakes

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Using \(\mu I\) unconditionally** | Ignores the possibility that the friction needed to stop slip is smaller; would predict a reversal of relative motion that cannot happen in a single impulsive event. | First compute the impulse required to bring the slip velocity to zero (Eq. 6) and compare with \(\mu I\). |
| **Applying the impulse–momentum equations with the wrong sign for \(J_t\)** | Leads to a post‑impact slip velocity with the wrong direction. | Remember that friction always opposes the *relative* motion, i.e. \(J_t\) has opposite sign to the initial slip \(u=v-\omega R\). |
| **Using the translational mass \(m\) instead of the effective slip mass** | The rotational inertia couples to the tangential impulse; neglecting it yields an incorrect required impulse. | Derive the relation \(u^{+}=u-J_t/m_{\text{eff}}\) (or Eq. 3) and keep the term \(-R^{2}/I_{\text{cm}}\). |
| **Assuming the ball will always stick after impact** | Not true when the normal impulse is small or the coefficient of friction is low. | Compare \(|J_t^{*}|\) with \(\mu I\); only stick if the former is the smaller. |
| **Treating the impulse as a force multiplied by a time** | Impulse during a collision is not well‑defined as “force × Δt” because Δt is infinitesimal and unknown; only the integrated quantity matters. | Work directly with impulse–momentum equations; do not try to compute a force magnitude. |

By keeping these points in mind, you will correctly determine the frictional impulse for any impact of a spinning ball on a rough surface.

*Original question: [Impulsive Friction](https://physics.stackexchange.com/questions/876067/impulsive-friction) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
