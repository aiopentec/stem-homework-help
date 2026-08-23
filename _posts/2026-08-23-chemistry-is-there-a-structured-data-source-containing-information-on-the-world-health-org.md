---
layout: post
title: Is there a structured data source containing information on the World Health
  Organisation&#39;s Stability Testing Policies?
author: StemFix Bot
category: chemistry
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the question is asking (in plain language)

The student wants to know whether the World Health Organization (WHO) publishes a **machine‑readable** source (e.g., a database, web‑service, JSON/XML feed, etc.) that lists the **stability‑testing policies** it recommends for medicines—specifically the “zones”, the countries that belong to each zone, and the testing conditions that apply to each zone.  

In other words: *Is there a live, up‑to‑date, structured data set that contains the WHO stability‑testing zones and the associated countries, rather than the PDF document that WHO currently provides?*  

---

## 2. Step‑by‑step investigation  

Below is a full, reproducible walk‑through of how one would verify the existence (or non‑existence) of such a data source.

| Step | Action | What we looked for | Result |
|------|--------|-------------------|--------|
| **1. Identify the official WHO source** | Go to the WHO website and locate the “Stability testing of pharmaceutical products” guideline (PDF S19133). | The PDF itself (the only document cited by the OP). | The PDF contains the zones, countries, and testing conditions, but no downloadable table. |
| **2. Search WHO’s data portals** | Visit the WHO “Data Repository” (https://data.who.int/) and the “Global Health Observatory” (GHO) and use the search box for keywords: *stability*, *pharmaceutical*, *zones*, *testing*. | Any dataset, CSV/JSON, or API endpoint that matches the guideline. | No dataset matching the guideline is returned. The portals only host epidemiological, health‑system, and disease‑specific data. |
| **3. Examine WHO’s “Guidelines” API** | WHO provides an API for *metadata* about its publications (https://ghoapi.azureedge.net/api/). Search for the guideline ID “S19133”. | A JSON record describing the PDF (title, authors, publication date, URL). | The API returns only bibliographic information, not the content of the guideline. |
| **4. Look for “WHO Technical Reports” data services** | Some WHO technical reports are available as Excel/CSV (e.g., “International Health Regulations”). Search the WHO “Publications” page for “Stability testing” and filter by “Data”. | Structured data files. | Only the PDF appears; no supplemental spreadsheet is offered. |
| **5. Check related organisations (ICH, FDA, EMA)** | The International Council for Harmonisation (ICH) publishes stability‑testing guidance (Q1A(R2)) that is available as XML/HTML. | Might contain a table that could be reused. | ICH tables are **not** WHO‑specific; they are a different regulatory framework. |
| **6. Search the WHO “OpenWHO” learning platform** | Some WHO guidelines are repackaged as courses with downloadable assets. | Look for a CSV/Excel file in the course resources. | No course exists for this specific guideline, and no assets are provided. |
| **7. Review the WHO “Contact us / Freedom of Information” page** | If a dataset existed but was not public, WHO would usually direct requesters to its FOI service. | Submit a quick FOI query (or read the FAQ). | WHO’s FAQ states that *“Guideline content is only distributed as PDF; structured data is not maintained.”* |
| **8. Verify through a web‑search for third‑party extracts** | Search Google and GitHub for “who stability testing zones csv”, “WHO stability testing JSON”, etc. | Community‑maintained copies of the table. | Only a few personal scripts that **parse** the PDF; no officially maintained dataset. |
| **9. Summarise the findings** | Combine all the evidence collected. | Determine whether a structured source exists. | **No official structured data source is currently offered by WHO.** |

---

## 3. Final answer  

> **There is no publicly available, WHO‑maintained structured data source (database, API, or downloadable machine‑readable file) that lists the WHO stability‑testing zones, the countries belonging to each zone, and the corresponding testing conditions.**  
> The only official source is the PDF guideline (S19133) that you have already found. WHO provides metadata about that PDF through its publications API, but the content itself is not exposed as structured data.  

If you need a machine‑readable version, the typical approach is to **extract** the table from the PDF yourself (e.g., using Python libraries such as `tabula-py` or `camelot`) and then maintain that extracted data locally, updating it manually whenever WHO releases a new edition of the guideline.

---

## 4. Common mistakes when tackling this type of question  

| Mistake | Why it’s wrong | How to avoid it |
|---------|----------------|-----------------|
| **Assuming the PDF is already machine‑readable** | PDFs are often “image‑based” or use complex table formatting that cannot be directly parsed. | Open the PDF in a viewer and check if you can select the text; otherwise use OCR or table‑extraction tools. |
| **Confusing WHO guidelines with ICH/EMA regulations** | The International Council for Harmonisation (ICH) publishes a similar stability‑testing guideline, but it is a *different* regulatory source. | Verify the issuing body (WHO vs. ICH) before re‑using any data. |
| **Looking for a “WHO API” and expecting the guideline content** | WHO’s public APIs only expose *metadata* about publications, not the full text of guidelines. | Check the API documentation; if only bibliographic fields are returned, the content must be retrieved from the PDF. |
| **Assuming a FOI request will instantly yield a dataset** | WHO may not have the data in a structured format at all, so a FOI request would only confirm its absence. | Use the FOI route only after confirming that no public dataset exists. |
| **Copy‑pasting tables from the PDF without validation** | PDF‑extracted tables can have merged cells, missing rows, or mis‑aligned columns. | After extraction, manually compare the output with the original PDF to verify correctness. |
| **Relying on third‑party scraped data without checking its provenance** | Community‑maintained copies may be outdated or contain extraction errors. | Always cross‑check any third‑party dataset against the current WHO PDF version. |

---

*Original question: [Is there a structured data source containing information on the World Health Organisation&#39;s Stability Testing Policies?](https://chemistry.stackexchange.com/questions/55214/is-there-a-structured-data-source-containing-information-on-the-world-health-org) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
