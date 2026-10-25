---
layout: question
title: Correct naming of clinical studies
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Correct naming of clinical studies'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

### 1. Restate What's Being Asked in Plain Language

The student is asking how to correctly classify clinical studies based on the timeline of data collection relative to when the study is planned and when the patient outcomes (endpoints) actually occur. Specifically, they present two nuanced scenarios:
1. **Scenario I:** A researcher uses existing past records (retrospective data) *and* plans to collect new data moving forward into the future, combining both for a final analysis.
2. **Scenario II:** Patients receive a treatment starting in 2020, a study protocol is written in 2021, and outcomes for patients treated between 2022 and 2024 are evaluated (where the treatments happen in the future relative to the 2021 protocol, but the patient endpoints/outcomes have already occurred by the time the analysis is run).

The goal is to provide the correct epidemiological and statistical terminology for these study designs, explain the reasoning step-by-step, and clarify the distinction between *retrospective* and *prospective* research.

---

### 2. Show Every Step

#### Step 1: Define the Core Statistical Criteria for Study Classification
In clinical research, studies are traditionally classified as **retrospective** or **prospective** based on the temporal relationship between the **initiation of the study (protocol creation/data collection design)** and the **occurrence of the events (outcomes/endpoints)**:
* **Prospective Study:** The study is conceived and designed *before* the patients are enrolled and *before* the outcomes occur. Researchers follow patients forward in time to observe events.
* **Retrospective Study:** The study is conceived and designed *after* the events (outcomes) have already occurred. Researchers look backward at existing records.

#### Step 2: Analyze Scenario I
* **The setup:** A researcher uses an existing sample from past records (retrospective component) *plus* enrolls/collects a new sample moving forward for 1 year with a 1-year follow-up, then analyzes everything together.
* **Step-by-step breakdown:** 
  1. The portion of the data from the past (where outcomes already happened before the study started) is **retrospective**.
  2. The portion of the data collected moving forward in time from a newly enrolled sample is **prospective**.
  3. When a single study design incorporates both historical (retrospective) and newly gathered forward-looking (prospective) data, it is formally called an **ambispective study** (sometimes referred to in literature as a *retrospective-prospective* study).
* **Literature/Naming context:** While "ambispective" is less common in everyday clinical chatter, it is widely recognized in epidemiological methodology (e.g., in dictionaries of epidemiology like those by the International Epidemiological Association) to describe mixed-cohort designs.

#### Step 3: Analyze Scenario II
* **The setup:** Treatment X starts in 2020 without a study protocol. A study protocol is written in 2021. Data collection continues for patients treated from 2022 to 2024, but by the time the researcher analyzes the data, those patients' 1-year progression-free survival (PFS) outcomes have already occurred.
* **Step-by-step breakdown:**
  1. Focus on the critical rule: *When were the outcomes determined relative to the study design/protocol?* 
  2. Although the patients were treated and followed *after* the protocol was established in 2021 (which feels forward-looking), if the outcomes (e.g., 1-year PFS) had **already occurred and were sitting in medical charts** by the time the researchers pulled the data to analyze them, the data collection is fundamentally based on historical records.
  3. Therefore, analyzing data from 2022–2024 under these conditions is still classified as a **retrospective study** (specifically, a retrospective cohort study using an institutional database or registry). 
  4. *Alternative nuance:* If the protocol was active in 2021, and researchers actively tracked patients prospectively from 2022 to 2024—meaning they set up data collection sheets *before* the patients reached their 1-year endpoints—it would be a **prospective observational study**. However, the prompt specifies that the outcomes were already observed, cementing its retrospective nature.

---

### 3. State the Final Answer Clearly

* **Scenario I:** This is an **ambispective study** (or retrospective-prospective study), because it utilizes both historical data (retrospective) and newly followed-up data moving forward (prospective).
* **Scenario II:** This is a **retrospective study**. Even though the treatments and events occurred after the protocol was written (2022–2024), if the outcomes were already observed and pulled from existing records at the time of analysis, the study is retrospective. 

---

### 4. Common Mistakes for This Study Type

* **Mistaking "When the treatment happened" for "Prospective":** A common error is thinking that if a patient was treated *after* a protocol was written, the study is automatically prospective. Prospective vs. retrospective depends strictly on **when the data/outcomes are collected relative to the conception of the study**, not merely the calendar year of the treatment.
* **Confusing "Prospective Data Collection" with "Prospective Study Design":** Simply pulling data from a modern electronic health record (EHR) that was logged yesterday does not make a study prospective. If the data already exist when you decide to do the study, it is retrospective.
* **Overcomplicating Scenario I:** Researchers sometimes try to treat mixed designs as two entirely separate studies. Statistically, they can be analyzed together as a single cohort under an ambispective framework, provided biases between the historical and newly collected groups are properly controlled.

*Original question: [Correct naming of clinical studies](https://stats.stackexchange.com/questions/677504/correct-naming-of-clinical-studies) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
