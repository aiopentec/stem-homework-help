---
layout: question
title: How do I get the multiplet tree to display in TopSpin 5.0.0 Plot
author: StemFix Bot
category: chemistry
subject: chemistry
description: 'Step-by-step chemistry solution: How do I get the multiplet tree to
  display in TopSpin 5.0.0 Plot'
tags:
- chemistry
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of College Chemistry, 10th Edition](https://www.amazon.com/dp/007181082X?tag=aiopentec20-20).

---

## 1. What the student is really asking  

The student wants to **display the “multiplet tree” (the hierarchical list of coupling partners that TopSpin uses for spin‑system analysis) in the Plot window of Bruker TopSpin 5.0.0** for a 1‑D NMR spectrum. In other words, they need to know which menu commands or shortcuts make the multiplet‑tree overlay appear alongside the trace in the Plot pane.

---

## 2. Step‑by‑step instructions  

Below is a complete, ordered procedure that works for the **standard TopSpin 5.0.0 installation** on Windows (the same steps also apply on macOS/Linux with the same menu names).

| # | Action | Where to find it | What you should see |
|---|--------|------------------|---------------------|
| 1 | **Open the spectrum** | `File → Open` (or press **Ctrl O**) and select your 1‑D data set (e.g., `fid` → `ft`). | The spectrum appears in the **Plot** window with the usual baseline and axis labels. |
| 2 | **Activate the “Multiplet Tree” tool** | In the Plot window, go to **Display → Multiplet tree** (or use the shortcut **Ctrl M**). | The cursor changes to a small “tree” icon and a tiny toolbox appears near the top‑right of the Plot pane. |
| 3 | **Select the peak of interest** | Click **once** on the resonance (peak) whose coupling pattern you want to inspect. | The peak becomes highlighted (usually a thick black line) and the **Multiplet‑tree panel** pops up on the right side of the Plot window. |
| 4 | **Open the Multiplet‑tree panel (if it is hidden)** | If the panel does not appear automatically, press **F9** or click the **“Tree”** button (looks like a small branching diagram) on the toolbar of the Plot window. | A docked panel titled **“Multiplet tree”** appears, showing the root node (the selected peak) and its child nodes (the couplings). |
| 5 | **Expand the tree** | Click the **plus (+) sign** next to the root node, or double‑click the node itself. | All coupling partners are displayed as a hierarchy (e.g., `H‑α → H‑β → H‑γ`). Each node shows the coupling constant (J in Hz) and the multiplicity label (e.g., `d` for doublet). |
| 6 | **Show the tree on the plot (optional overlay)** | With the tree panel open, click the small **“Show on plot”** checkbox (top of the panel). | Small brackets and J‑value labels are drawn directly on the spectrum trace, aligning with the selected peak. |
| 7 | **Adjust visual options** (optional) | Right‑click inside the Multiplet‑tree panel → **Properties**. Here you can change font size, colour of J‑labels, and whether the tree is displayed as a **vertical** or **horizontal** list. | The display updates instantly, letting you tailor the look for presentations or publications. |
| 8 | **Save the layout** (so you don’t lose it) | In the Plot window, go to **File → Save layout** (or press **Ctrl L**) and give the layout a name (e.g., `my_spectrum_with_tree`). | The next time you open this spectrum and load the saved layout (`File → Load layout`), the multiplet tree will re‑appear automatically. |

### Quick‑reference keyboard shortcuts  

| Shortcut | Action |
|----------|--------|
| **Ctrl M** | Toggle the Multiplet‑tree tool on/off |
| **F9** | Show/hide the Multiplet‑tree panel |
| **Ctrl L** | Save the current Plot layout |
| **Ctrl O** | Open a data set |
| **Enter** (while cursor is on a peak) | Same as clicking the peak – opens the tree for that peak |

### What to do if the tree still does not appear  

1. **Check the “Display → Multiplet tree” menu** – the tool must be enabled; otherwise the panel stays hidden.  
2. **Make sure the spectrum is phased and baseline‑corrected** – TopSpin will not generate a tree for a completely unprocessed spectrum (e.g., raw FID). Run `ph` and `bc`.  
3. **Confirm that the spectrum is a 1‑D proton spectrum** – the built‑in multiplet analysis works only for ^1H, ^19F, ^31P, etc., where TopSpin knows the typical spin‑½ pattern.  
4. **Restart TopSpin** – occasionally a UI glitch prevents the panel from opening. A quick restart clears the cache.  

---

## 3. Final answer (concise)  

To display the multiplet tree in TopSpin 5.0.0 Plot:

1. Open the processed 1‑D spectrum.  
2. Enable the tool via **Display → Multiplet tree** (or **Ctrl M**).  
3. Click the peak whose couplings you want to view.  
4. The **Multiplet‑tree panel** appears; expand the nodes to see the full hierarchy.  
5. (Optional) Check “Show on plot” to overlay J‑labels on the spectrum.

That’s all that’s required to view the multiplet tree alongside your spectrum.

---

## 4. Common mistakes & how to avoid them  

| Mistake | Why it happens | How to fix / avoid it |
|---------|----------------|-----------------------|
| **Forgetting to enable the Multiplet‑tree tool** (`Display → Multiplet tree`) | The tool is off by default in a fresh TopSpin session. | Always start by toggling **Ctrl M** or using the menu before clicking a peak. |
| **Clicking the wrong part of the spectrum (noise region)** | Noise peaks have no coupling information, so the tree stays empty. | Zoom in (`z` key) and select a **well‑defined resonance** with a clear envelope. |
| **Using an un‑processed spectrum (raw FID)** | TopSpin cannot calculate J‑values from time‑domain data. | Run `ft`, `ph`, and optionally `bc` before attempting to view the tree. |
| **Viewing the tree on a heteronuclear spectrum (e.g., 13C) without decoupling** | 13C spectra often have low S/N and may be broadband‑decoupled, giving no multiplets. | Ensure the experiment is **not** broadband‑decoupled, or switch to a proton‑detected experiment if you need J‑couplings. |
| **Panel hidden behind another window** | The Multiplet‑tree panel docks at the right side and can be covered by other docked panels. | Use **F9** to force the panel to the front, or drag the panel to a different dock location. |
| **Layout not saved** | After closing TopSpin, the tree disappears, forcing you to redo the steps. | Save the layout with **Ctrl L** and reload it later with **File → Load layout**. |
| **Expecting automatic labeling of all peaks** | TopSpin only builds a tree for the *selected* peak, not for every peak simultaneously. | Repeat the click for each peak you need, or use the “Batch” option in the **Multiplet‑tree** dialog (if available). |

By following the steps above and keeping an eye on these typical pitfalls, you should be able to view and manipulate the multiplet tree for any 1‑D NMR spectrum in TopSpin 5.0.0 without trouble.

*Original question: [How do I get the multiplet tree to display in TopSpin 5.0.0 Plot](https://chemistry.stackexchange.com/questions/195983/how-do-i-get-the-multiplet-tree-to-display-in-topspin-5-0-0-plot) on Chemistry Stack Exchange, licensed CC BY-SA.*

{% endraw %}
