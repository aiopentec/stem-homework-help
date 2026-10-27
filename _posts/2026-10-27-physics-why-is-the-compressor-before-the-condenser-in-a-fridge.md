---
layout: question
title: Why is the compressor before the condenser in a fridge?
author: StemFix Bot
category: physics
subject: physics
description: 'Step-by-step physics solution: Why is the compressor before the condenser
  in a fridge?'
tags:
- physics
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Physics, 12th Edition](https://www.amazon.com/dp/1259587398?tag=aiopentec20-20).

---

### 1. Restate What's Being Asked in Plain Language

The student is asking a fundamental question about the vapor-compression refrigeration cycle (used in refrigerators and air conditioners): **Why are the components arranged in the specific order of Evaporator $\rightarrow$ Compressor $\rightarrow$ Condenser $\rightarrow$ Expansion Valve (Throttle), rather than any other possible order?** 

Specifically, the student is questioning the role of the compressor. They wonder if compressing the gas makes it "harder" to condense (due to a higher enthalpy difference) and why we can't just put the throttle before the condenser or rearrange the loop entirely.

---

### 2. Show Every Step (The Thermodynamic Reasoning)

To understand why components are in this exact order, let's trace the state of the refrigerant (the working fluid) step-by-step through the standard cycle and see what happens if we try to change it.

#### Step A: Understand the Goal of a Refrigerator
The ultimate goal of a refrigerator is to move heat from the cold interior (low temperature) to the warmer room outside (high temperature). Heat naturally flows from hot to cold, so to reverse this, we must do **work** on the system.

#### Step B: Analyze the Standard Four-Step Cycle
Let's follow the refrigerant through the standard sequence:

1. **Evaporator (Low Pressure, Low Temperature):**
   * *State:* Enters as a cold liquid/vapor mixture.
   * *Action:* It absorbs heat from the inside of the fridge. Because the pressure is low, its boiling point is very low, allowing it to boil (evaporate) at a temperature colder than the fridge interior. 
   * *Result:* We now have a low-pressure, low-temperature **gas**.

2. **Compressor (The Heart of the Cycle):**
   * *State:* Low-pressure gas enters.
   * *Action:* The compressor does mechanical work on the gas, "squishing" it to a high pressure. According to the Ideal Gas Law (and thermodynamics), doing work on a gas increases both its pressure and its temperature.
   * *Result:* We now have a **high-pressure, high-temperature gas**. 
   * *(Addressing the student's concern about enthalpy: While the total enthalpy increases because the compressor adds electrical/mechanical work into the system, the pressure increase dramatically raises the saturation temperature. This is the crucial point—it makes the gas *hotter* than the kitchen air, which means heat can now flow *out* of the refrigerant.)*

3. **Condenser (High Pressure, High Temperature):**
   * *State:* High-pressure, high-temperature gas enters.
   * *Action:* Because the compressor raised the refrigerant's temperature *above* room temperature, heat naturally flows from the refrigerant out into the kitchen. As it loses heat, the gas condenses back into a liquid.
   * *Result:* High-pressure **liquid**.

4. **Expansion Valve / Throttle (Pressure Drop):**
   * *State:* High-pressure liquid enters.
   * *Action:* The valve is a restriction. As the liquid squeezes through, the pressure drops suddenly. This rapid drop causes a portion of the liquid to flash-boil (evaporate), which requires energy. Where does that energy come from? The refrigerant itself. 
   * *Result:* The temperature plummets, resulting in a low-pressure, low-temperature liquid/vapor mix ready to re-enter the evaporator.

#### Step C: What Happens If We Change the Order? (Testing the Student's Alternative)

Let's test the student's proposed alternative order: **Evaporator $\rightarrow$ Throttle $\rightarrow$ Condenser $\rightarrow$ Compressor**.

1. **Evaporator:** Absorbs heat, turns into a low-pressure gas.
2. **Throttle (placed here):** A throttle *drops* pressure. If you put a throttle after the evaporator, the pressure drops even lower, and the temperature drops further. But a throttle does *not* add heat or raise pressure; it only lowers it.
3. **Condenser:** For a gas to condense into a liquid, it must reject heat to the surroundings (room temperature, roughly $20^\circ\text{C}$ or $70^\circ\text{F}$). If the refrigerant just left the evaporator and throttle, it is extremely *cold*. Heat cannot flow from a cold fluid into a warm room. Therefore, condensation **cannot** happen.
4. **Compressor (at the very end):** Finally, the compressor squeezes the gas, raising its temperature and pressure. But the cycle is already over, and the fluid is heading back to the evaporator. 

In short: Without the compressor *before* the condenser, you never raise the pressure and temperature high enough for the refrigerant to reject its heat to the outside room. The thermodynamic cycle collapses because heat would flow in the wrong direction.

---

### 3. Final Answer

The compressor **must** be placed before the condenser because the compressor's job is to raise both the pressure and the temperature of the refrigerant gas through mechanical work. 

* **Before the compressor:** The refrigerant is cold, allowing it to absorb heat from inside the fridge (in the evaporator).
* **After the compressor:** The refrigerant is hot (higher temperature than the room), which allows it to release that heat to the outside environment (in the condenser). 

If you placed the compressor after the condenser, the refrigerant would be too cold to release heat to the room, and the thermodynamic cycle would fail to pump heat "uphill" from cold to hot.

---

### 4. Common Mistakes

* **Confusing Temperature with Enthalpy (Heat Content):** Students often look at enthalpy-pressure ($h$-$P$) charts and think higher enthalpy means it's "harder" to condense. Remember that condensation depends on **temperature gradient**. The compressor increases the pressure so that the saturation temperature of the gas rises *above* room temperature, forcing heat to flow outward.
* **Misunderstanding the Throttle's Function:** A throttle (expansion valve) is not a pump; it cannot raise pressure or push fluid uphill. It only creates a pressure drop, which *lowers* temperature. Placing it in the wrong part of the cycle destroys the necessary pressure differences.
* **Assuming Any Permutation Works:** Thermodynamics relies strictly on the laws of energy transfer. Because heat only flows spontaneously from hot to cold, the working fluid *must* be made hotter than the environment via compression before it reaches the condenser, and colder than the fridge interior via expansion before it reaches the evaporator.

*Original question: [Why is the compressor before the condenser in a fridge?](https://physics.stackexchange.com/questions/877256/why-is-the-compressor-before-the-condenser-in-a-fridge) on Physics Stack Exchange, licensed CC BY-SA.*

{% endraw %}
