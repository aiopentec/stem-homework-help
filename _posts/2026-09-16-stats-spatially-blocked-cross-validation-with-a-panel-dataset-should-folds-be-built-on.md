---
layout: question
title: Spatially blocked cross-validation with a panel dataset — should folds be built
  on unique locations or all repeated rows?
author: StemFix Bot
category: stats
subject: stats
description: 'Step-by-step statistics solution: Spatially blocked cross-validation
  with a panel dataset — should folds be built on unique locations or all repeated
  rows?'
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1.  Restating the question in plain language  

You have a **panel (longitudinal) data set**:

| Variable | Details |
|----------|----------|
| Spatial unit | 4 800 LSOAs (small areas) in London |
| Time points | 6 (June, July, August for 2019 & 2025) |
| Rows | 6 × 4 800 = 28 800 (each LSOA appears 6 times) |
| Geometry | All rows belonging to the same LSOA have exactly the same latitude‑longitude coordinates. |

You want to use the **`blockCV`** R package (function `cv_spatial`) to create **spatially blocked cross‑validation folds** for a linear model.  

The dilemma is:

* **Option A** – Feed **all 28 800 rows** (including the duplicated coordinates) to `cv_spatial`.  
* **Option B** – First collapse the data to the **4 800 unique locations**, build the folds on those, then copy the fold ID back to the six temporal observations for each LSOA.

You are asking:

1. Will the duplicated points “distort” the block construction or the balance optimisation performed by `cv_spatial`?  
2. What do practitioners usually do when they have a spatio‑temporal panel like this?  

---

## 2.  Step‑by‑step reasoning  

### 2.1  How `cv_spatial` creates blocks  

`cv_spatial` works in three stages (simplified):

| Stage | What happens |
|-------|--------------|
| **(i) Define blocks** | The function either (a) partitions the study area into a regular grid of a user‑specified cell size, or (b) builds blocks from a set of “blocking points” (e.g., centroids) using a distance‐based algorithm. |
| **(ii) Assign each **observation** to a block** | For each row, the function extracts its coordinates and finds the block (grid cell or distance‑based polygon) that contains it. |
| **(iii) Optimise fold allocation** | The function tries to split the *set of blocks* into *k* folds while respecting constraints such as (i) similar numbers of observations per fold, (ii) spatial balance, (iii) optional grouping variables. The optimisation is performed **on the block level**, not on the individual rows. |

Key point: **The optimisation step uses only the *block IDs*; the number of rows inside a block only matters for the “balance” criterion (i.e., how many observations each fold ends up with).**

### 2.2  What happens if we give the function the duplicated rows  

* When we pass **all 28 800 rows**, the function will still **extract the same coordinates** for the six rows that belong to one LSOA.  
* All six rows will be placed in the **same block** (because they have identical coordinates).  
* Consequently, each block will contain **six times the number of observations** compared with a data set that only had one row per LSOA.  

The optimisation routine will therefore try to **balance the *total number of rows* across folds**. Because each block now contributes a multiple of six, the algorithm may have slightly fewer feasible partitions (e.g., you cannot split a block between folds). In practice, this does **not change which rows are grouped together** – the six rows will always stay together – but it **inflates the weight of each block** in the balance calculation.

#### Does this “distort” the block geometry?  
No. The geometric partition (grid cells or distance‑based polygons) is derived *only* from the set of unique coordinates, so adding duplicated rows does **not** change where block borders fall.

#### Does it affect the optimisation?  
* **Yes, marginally** – the balance criterion now works with counts that are multiples of six. If the algorithm tries to equalise the number of observations per fold, it will be constrained to multiples of six, which can make the final folds a bit less evenly balanced (especially when the total number of rows is not a multiple of *k* × 6).  
* The *spatial* separation of folds remains exactly the same, because that part depends only on which **blocks** are assigned to which fold.

### 2.3  What happens if we first collapse to unique locations  

* We feed **4 800 rows** (one per LSOA) to `cv_spatial`.  
* Each block now contains a single observation.  
* The optimisation tries to balance *one* observation per block, so it can achieve a perfectly even split (e.g., 5 000 ÷ 5 = 1 000 rows per fold).  

After the folds are created we **replicate the fold ID** six times for each LSOA (one for each time point). The final data set still has the same spatial grouping (all six rows of a given LSOA are in the same fold) but the **balance optimisation was performed on the un‑weighted blocks**.

### 2.4  Which approach is recommended?  

| Aspect | Option A (all rows) | Option B (unique locations) |
|--------|--------------------|-----------------------------|
| **Spatial block borders** | Identical to Option B (determined from unique coordinates). | Identical to Option A. |
| **Fold composition (which LSOAs are together)** | Identical – all rows of an LSOA stay together. | Identical – all rows of an LSOA stay together. |
| **Balance of observations per fold** | May be slightly unbalanced because the algorithm balances multiples of six. | Exactly balanced (or as close as possible) because each block contributes a single count. |
| **Computation time** | Slightly longer (6× more rows to process, though the heavy work is still on the block level). | Faster (fewer rows). |
| **Risk of “distortion”** | None in geometry, only a minor effect on balance. | None. |
| **Typical practice in the literature** | Rarely used; most authors collapse to unique spatial units before spatial CV. | Standard approach for spatio‑temporal panels. |

**Why practitioners collapse first**  

* The purpose of spatial blocking is to **remove spatial autocorrelation** between training and test data. The temporal dimension is usually handled **separately** (e.g., by adding a temporal hold‑out, using time‑series CV, or including time as a covariate).  
* The block‑creation step is **purely spatial**; it does not need to know that you will later duplicate the block IDs across time.  
* By building blocks on the unique locations you avoid the “multiple‑of‑k” balancing issue and you make the code clearer to readers: *“We created spatial folds based on the 4 800 LSOA centroids, then we used the same folds for every month.”*  

### 2.5  Practical implementation  

```r
library(blockCV)

## 1. Prepare a data frame with ONE row per LSOA
lsoa_unique <- lsoa_panel %>%
  distinct(LSOA_ID, .keep_all = TRUE) %>%      # keep the first time slice
  select(LSOA_ID, lon, lat, everything_else)

## 2. Build spatial blocks (example: 2‑km grid)
spatial_folds <- cv_spatial(
  data = lsoa_unique,
  coords = c("lon", "lat"),
  k = 5,                     # number of folds
  selection = "random",      # or "systematic"
  raster = NULL,             # optional, can pass a raster to define cell size
  spatial_dist = 2000        # block size ≈ 2 km
)

## 3. Propagate fold IDs back to the full panel
lsoa_panel <- lsoa_panel %>%
  left_join(
    spatial_folds %>% select(LSOA_ID, folds), 
    by = "LSOA_ID"
  )
```

The resulting column `folds` can be used directly in `caret`, `mlr3`, `tidymodels`, etc., and each LSOA’s six observations will all belong to the same fold.

If you really want to feed all rows directly, you can do it, but you must be prepared for the slight imbalance described above:

```r
spatial_folds_all <- cv_spatial(
  data = lsoa_panel,
  coords = c("lon", "lat"),
  k = 5,
  selection = "random",
  spatial_dist = 2000
)
# folds are already attached to every row
```

Both give the **same spatial separation**, but the **first method (unique locations)** is the *standard* and the **cleaner** choice.

---

## 3.  Final answer  

**You should build the spatial blocks on the set of *unique* LSOA locations (the N = 4 800 rows) and then copy the resulting fold IDs to the six temporal observations of each LSOA.**  

* This does **not** change the spatial layout of the blocks; the same LSOAs will be kept together regardless of the approach.  
* It avoids the minor imbalance that occurs when the optimisation routine must balance multiples of six observations per block.  
* It reduces computation time and follows the common practice in spatio‑temporal panel modelling, where spatial blocking is performed on the spatial units only and temporal replication is handled afterwards.

---

## 4.  Common mistakes  

| Mistake | Why it’s a problem | How to avoid it |
|---------|--------------------|-----------------|
| **Feeding all duplicated rows and assuming the folds will be perfectly balanced** | The balance algorithm works on block counts, so folds will be balanced only in multiples of the number of duplicates (here, six). This can give uneven training/test sizes. | Collapse to unique locations before creating folds, then replicate the fold ID. |
| **Using the temporal coordinate as part of the spatial block definition** | `cv_spatial` treats the supplied columns as *purely* spatial; adding a time column will either be ignored or cause an error, and you will unintentionally mix temporal information into spatial blocks. | Pass only the true spatial columns (`lon`, `lat`) to `cv_spatial`. Handle temporal splits separately (e.g., a nested time‑series CV). |
| **Assuming that spatial blocks automatically remove temporal autocorrelation** | Spatial blocking only reduces spatial dependence; if measurements from the same LSOA at different times are highly correlated, they will still be in the same training set. | If temporal autocorrelation is a concern, combine spatial blocking with a temporal hold‑out (e.g., leave‑one‑year‑out) or use a spatio‑temporal CV scheme (`blockCV::cv_spatiotemporal`). |
| **Not checking that every LSOA ends up in exactly one fold** | With duplicate rows, a coding mistake can accidentally assign different rows of the same LSOA to different folds, breaking the independence assumption. | After creating folds, verify `table(lsoa_panel$LSOA_ID, lsoa_panel$folds)` – each LSOA should appear in a single column only. |
| **Using a block size that is smaller than the spacing between LSOAs** | If the grid cells are tiny, many cells will contain **zero** observations, leading to empty blocks that the optimiser may drop, altering the intended number of folds. | Choose a block size that yields a reasonable number of non‑empty blocks (e.g., 2–5 km for London LSOAs) and inspect the block map before proceeding. |

---

*Original question: [Spatially blocked cross-validation with a panel dataset — should folds be built on unique locations or all repeated rows?](https://stats.stackexchange.com/questions/677142/spatially-blocked-cross-validation-with-a-panel-dataset-should-folds-be-built) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
