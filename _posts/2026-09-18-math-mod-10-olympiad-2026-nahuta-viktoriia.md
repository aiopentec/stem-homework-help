---
layout: question
title: Mod 10. Olympiad 2026 . Nahuta Viktoriia
author: StemFix Bot
category: math
subject: math
description: 'Step-by-step mathematics solution: Mod 10. Olympiad 2026 . Nahuta Viktoriia'
tags:
- math
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Calculus, 7th Edition](https://www.amazon.com/dp/126425833X?tag=aiopentec20-20).

---

## Problem Restatement  

We are asked to determine the **units (last) digit** of the enormous number  

\[
7^{2026}.
\]

In other words, we need the remainder when \(7^{2026}\) is divided by \(10\).  

---

## Step‑by‑Step Solution  

### 1. Understand the cyclicity of powers modulo 10  

For any integer \(a\) that is coprime to \(10\) (i.e. ends in 1,3,7,9), the sequence of its last digits repeats with a period that divides \(4\).  
This follows from Euler’s theorem because \(\phi(10)=4\).

So we only need to look at the first few powers of \(7\) modulo 10:

| Power | Value | Last digit (mod 10) |
|-------|-------|----------------------|
| \(7^1\) | 7 | 7 |
| \(7^2\) | 49 | 9 |
| \(7^3\) | 343 | 3 |
| \(7^4\) | 2401 | 1 |
| \(7^5\) | 7·\(7^4\) | \(7·1 = 7\) |

Thus the pattern of last digits is **\(7, 9, 3, 1\)** and then it repeats every 4 exponents.

### 2. Reduce the exponent \(2026\) modulo the period  

Since the pattern repeats every \(4\) powers, we compute the remainder of \(2026\) upon division by \(4\):

\[
2026 = 4 \times 506 + 2 \quad\Longrightarrow\quad 2026 \equiv 2 \pmod{4}.
\]

So the exponent \(2026\) is equivalent to the exponent \(2\) in the repeating cycle.

### 3. Pick the corresponding digit from the cycle  

The cycle (starting with exponent \(1\)) is:

\[
\begin{aligned}
\text{exponent }1 &\to 7,\\
\text{exponent }2 &\to 9,\\
\text{exponent }3 &\to 3,\\
\text{exponent }4 &\to 1.
\end{aligned}
\]

Because \(2026 \equiv 2 \pmod{4}\), we take the **second** element of the cycle, which is **9**.

Formally:

\[
7^{2026}\equiv 7^{2}\equiv 49\equiv 9\pmod{10}.
\]

### 4. State the final answer  

The last (units) digit of \(7^{2026}\) is  

\[
\boxed{9}.
\]

---

## Common Mistakes  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Forgetting that the cycle length is 4** and trying to compute a huge power directly. | Computing \(7^{2026}\) explicitly is impossible by hand; the cyclic property is essential. | Remember Euler’s theorem: \(\phi(10)=4\). Always reduce the exponent modulo 4 for bases ending in 1,3,7,9. |
| **Using the remainder 0 instead of 4** when the exponent is a multiple of 4. | If the exponent were exactly divisible by 4, the last digit is the fourth element of the cycle (which is 1), not the “0‑th” element. | Treat “remainder 0” as meaning “use the fourth term of the cycle.” |
| **Mixing up the order of the cycle** (e.g., thinking the second term is 3). | The cycle for \(7\) is \(7,9,3,1\); swapping terms leads to an incorrect digit. | Write out the first few powers (at least up to the fourth) and keep the list handy. |
| **Assuming the pattern changes for larger exponents**. | The pattern is truly periodic; it never changes. | Verify the pattern for the first 4 powers; then trust the repetition. |

By keeping these points in mind, you can quickly find the last digit of any large power of a number ending in 1, 3, 7, or 9.

*Original question: [Mod 10. Olympiad 2026 . Nahuta Viktoriia](https://math.stackexchange.com/questions/5149749/mod-10-olympiad-2026-nahuta-viktoriia) on Mathematics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
