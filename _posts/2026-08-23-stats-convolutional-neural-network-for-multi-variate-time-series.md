---
layout: post
title: Convolutional neural network for multi-variate time series?
author: StemFix Bot
category: stats
tags:
- stats
---

{% raw %}
*As an Amazon Associate, I earn from qualifying purchases.* For more practice problems like this, see [Schaum's Outline of Statistics, 6th Edition](https://www.amazon.com/dp/1260011461?tag=aiopentec20-20).

---

## 1. What the question is asking (plain‑language restatement)

You have many **multivariate time‑series** (MTS) samples.  
Each sample  

\[
\mathbf S \in \mathbb R^{n \times T}
\]

has  

* **n** variables (channels, sensors, features) and  
* **T** time steps (the length of the record).

For every whole sequence you want a **single class label** (e.g. “normal / abnormal”, “activity A / B / C”, …).

The student has found three naïve ways of feeding an MTS to a convolutional neural network (CNN) and asks:

| Idea | How it works | What the student wonders |
|------|--------------|--------------------------|
| **(1) Treat the MTS as an “image” of size n × T** | 2‑D convolutions over the whole matrix | Is there a better architecture? |
| **(2) Use *n* input channels of size 1 × T and apply 1‑D convolutions** | Each variable is a separate channel, filters slide only along the time axis | Same question + handling different lengths |
| **(3) Build *n* independent CNNs (one per variable) and merge their features before the classifier** | Parallel streams that are concatenated later | Same question + variable‑length handling |

The answer must:

1. Explain why some of these designs are reasonable and where they fall short.  
2. Present **state‑of‑the‑art, efficient architectures** for multivariate sequences.  
3. Show **practical tricks for variable‑length series** (padding, masking, global pooling, etc.).  
4. Summarise the final recommendation.  
5. List typical pitfalls (“common mistakes”).

---

## 2. Step‑by‑step reasoning and design choices

### 2.1  Clarify the data layout

| Dimension | Meaning | Typical notation in deep‑learning libraries |
|-----------|---------|---------------------------------------------|
| **Batch** | Number of series processed together | `B` |
| **Channels** | Number of variables (`n`) | `C` |
| **Time** | Length of the series (`T`) | `L` |
| **Spatial (optional)** | If you reshape to an image, you have height = `n`, width = `T` | `H × W` |

Thus a tensor that can be fed to a **1‑D Conv** layer has shape **(B, C, L)**, while a **2‑D Conv** expects **(B, C, H, W)**.  

If you keep the natural ordering (`C = n`, `L = T`) you can use **1‑D convolutions**—the most common and efficient choice for time series.

### 2.2  Review the three proposed ideas

| Idea | Implementation details | Pros | Cons |
|------|------------------------|------|------|
| **(1) “Image” view** (2‑D conv) | Reshape to `(B, 1, n, T)` → 2‑D kernels of size `(k_n, k_t)` | Can learn joint patterns across variables (vertical kernel) **and** along time (horizontal kernel). | The “height” (`n`) is usually **tiny** (often ≤ 10). 2‑D convs become wasteful because many parameters are devoted to the vertical dimension that has little spatial extent. |
| **(2) 1‑D conv with *n* channels** | Input shape `(B, n, T)`. Kernel size `k` only along the time axis. | Very efficient (few parameters). Naturally respects the ordering of variables as separate channels. Captures cross‑channel interactions only via the learned linear combinations inside each filter (the filter has shape `(n, k)`). | If you need **different** temporal receptive fields for each variable, a single filter forces the same kernel size across all channels. |
| **(3) Parallel CNN per variable** | Build `n` independent 1‑D streams, each receives a tensor of shape `(B, 1, T)`. Concatenate their latent vectors before the classifier. | Gives each variable its **own** set of filters → more flexibility, especially when variables have very different dynamics. | Parameter count grows **linearly with n**; training can be slower and prone to over‑fitting if data are limited. Also discards early cross‑channel mixing (the only place they meet is at the concatenation). |

### 2.3  What modern research does

#### 2.3.1  **Temporal Convolutional Networks (TCN)**
* **Core idea**: 1‑D dilated convolutions with causal padding, plus residual blocks.
* **Why it works**: Dilations let a single layer see a large receptive field (e.g., 2⁷ = 128 time steps) without many parameters.
* **Typical architecture** for an MTS classification problem  

```
Input: (B, n, T)               # n channels, T steps
→ Conv1D( C=64, kernel=3, dilation=1 )
→ ReLU
→ Residual block (dilation=2)
→ Residual block (dilation=4)
→ Residual block (dilation=8)
→ GlobalAveragePooling1D()    # collapses time dimension
→ Dense( hidden=128, ReLU )
→ Dense( out=K, softmax )
```

*All variables are processed together; the filter weight tensor has shape `(n, k)` so each filter can combine all channels at each time offset.*

#### 2.3.2  **Inception‑style 1‑D CNN**
* **Core idea**: Parallel filters of *different* temporal lengths (e.g., `k = 3,5,7`) whose outputs are concatenated.
* **Benefit**: Captures both short‑ and long‑range patterns without deep stacking.
* **Typical block**

```
branch1: Conv1D( C=32, k=3, padding='same')
branch2: Conv1D( C=32, k=5, padding='same')
branch3: Conv1D( C=32, k=7, padding='same')
concat → BatchNorm → ReLU
```

Again the input shape is `(B, n, T)`. The block automatically learns **cross‑channel** relationships because each filter spans all `n` channels.

#### 2.3.3  **Hybrid CNN‑RNN / CNN‑Transformer**
* **Why combine?** Convolutions are excellent at extracting local patterns; recurrent/attention layers excel at modelling long‑range dependencies.
* **Simple recipe**  

```
CNN encoder (1‑D or 2‑D) → output shape (B, d, L')
→ (optional) PositionalEncoding
→ Transformer encoder (multi‑head self‑attention)
→ GlobalAveragePooling over L' → FC classifier
```

* The CNN reduces the sequence length (`L' << T`) so the attention module is cheap.

#### 2.3.4  **Depthwise‑Separable 1‑D Conv (a.k.a. Xception for 1‑D)**
* **Core idea**: First apply a **depthwise** convolution (one filter per input channel), then a **pointwise** 1‑× 1 convolution that mixes channels.
* **Benefit**: Same expressive power as a full 1‑D conv but with far fewer parameters—useful when `n` is large (e.g., > 30).

#### 2.3.5  **Graph‑CNN for irregularly coupled variables**
If the `n` variables have a known relational structure (e.g., sensor network, physiological signals), you can treat each variable as a node in a graph and use **graph convolution** to respect that topology before (or instead of) temporal convolutions.

### 2.4  Summarising the **most efficient, general‑purpose design**

| Component | Reason for inclusion | Typical hyper‑parameters |
|-----------|----------------------|--------------------------|
| **Input** | `(B, n, T)` – natural ordering | – |
| **Initial 1‑D Conv** | Immediate cross‑channel mixing; small kernel (3) | `filters = 64`, `kernel = 3`, `padding='same'` |
| **Stack of Dilated Residual Blocks** (TCN style) | Large receptive field with few layers | Dilation rates = `[1, 2, 4, 8]`, each block: `filters=64`, `kernel=3` |
| **Global Average Pooling** | Removes dependence on sequence length, yields a fixed‑size vector | – |
| **Fully‑connected head** | Classification | `Dense(128, ReLU) → Dropout(0.5) → Dense(K, softmax)` |

*If you suspect that very different temporal scales are important, replace the single‑kernel residual blocks with an **Inception‑type** block (multiple kernel sizes in parallel).*

**Why this beats the three naive ideas**

* It processes all variables **jointly** (unlike idea 3) → fewer parameters, earlier cross‑channel learning.  
* It uses **1‑D convolutions**, which are cheaper than 2‑D when the “height” (`n`) is tiny (unlike idea 1).  
* Dilations give a **large receptive field** without deep stacking, so the model can capture long‑range dependencies that a shallow 1‑D conv (idea 2) might miss.  

### 2.5  Dealing with **variable‑length** sequences

In practice, each series may have a different `T_i`. CNNs expect a **uniform length** across a batch. Common strategies:

| Strategy | How it works | When it is appropriate |
|----------|--------------|------------------------|
| **Zero‑padding to the max length in the batch** | Pad shorter series with zeros (or a learned mask value) up to `T_max`. Use a **mask** to ignore padded positions in any pooling or loss. | Small variation in length; padding overhead negligible. |
| **Mask‑aware Global Pooling** | After the final convolution, compute `masked_avg = sum(x * mask) / sum(mask)`. Many deep‑learning frameworks (TensorFlow, PyTorch) let you multiply by a mask before `torch.mean`. | When you want a single vector per series regardless of length. |
| **Adaptive pooling (e.g., `AdaptiveAvgPool1d(output_size=1)`)** | Learns to collapse *any* input length to a fixed‑size output (often 1). | Simpler code; works as long as you do not need to preserve temporal ordering after pooling. |
| **Chunking / Sliding windows** | Split each long series into overlapping windows of a fixed size, classify each window, then aggregate (majority vote, max‑prob). | Very long series where you also want local predictions. |
| **RNN / Transformer after CNN** | CNN reduces length (`L'`), then a recurrent/attention layer can handle variable lengths naturally (by packing sequences). | When you need fine‑grained temporal reasoning beyond what dilated convs provide. |

**Practical tip:**  
Always keep a *binary mask* (`1` for real timesteps, `0` for padded timesteps) and **propagate it** through the network (multiply before any pooling). This prevents the model from learning that “zeros = class 0” or similar artefacts.

### 2.6  Putting everything together – a concrete PyTorch‑style pseudo‑code

```python
import torch, torch.nn as nn

class TCNBlock(nn.Module):
    def __init__(self, C, kernel=3, dilation=1, dropout=0.2):
        super().__init__()
        self.conv = nn.Conv1d(C, C, kernel,
                              padding=(kernel-1)//2 * dilation,
                              dilation=dilation)
        self.bn   = nn.BatchNorm1d(C)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        out = self.conv(x)
        out = self.bn(out)
        out = self.relu(out)
        out = self.dropout(out)
        return out + x               # residual connection

class MVTS_CNN(nn.Module):
    def __init__(self, n_channels, n_classes):
        super().__init__()
        self.head = nn.Conv1d(n_channels, 64, kernel_size=3, padding=1)

        # Dilated residual stack
        self.blocks = nn.ModuleList([
            TCNBlock(64, dilation=1),
            TCNBlock(64, dilation=2),
            TCNBlock(64, dilation=4),
            TCNBlock(64, dilation=8)
        ])

        self.global_pool = nn.AdaptiveAvgPool1d(1)   # shape (B, 64, 1)
        self.fc = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, n_classes)
        )

    def forward(self, x, mask=None):
        """
        x : (B, n, T)   raw time‑series
        mask : (B, T)   1 for real timesteps, 0 for padding (optional)
        """
        out = self.head(x)                     # (B,64,T)
        for blk in self.blocks:
            out = blk(out)

        # optional masking before pooling
        if mask is not None:
            mask = mask.unsqueeze(1)           # (B,1,T)
            out = out * mask

        out = self.global_pool(out).squeeze(-1)   # (B,64)
        return self.fc(out)                       # (B, n_classes)
```

*Key points highlighted in the code*  

* **All variables are processed together** (`Conv1d` with `in_channels=n`).  
* **Dilated residual blocks** give a receptive field of up

*Original question: [Convolutional neural network for multi-variate time series?](https://stats.stackexchange.com/questions/350840/convolutional-neural-network-for-multi-variate-time-series) on Cross Validated (Stats Stack Exchange), licensed CC BY-SA.*

{% endraw %}
