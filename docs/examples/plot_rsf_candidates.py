# %% [markdown]
# # Renal sinus fat from kidney convex hull
#
# This example shows the use of the {py:func}`~miblab_dl.rsf_candidates` 
# function to automatically preselect an estimate of the renal sinus fat. 

# %% 
import numpy as np
from miblab_plot import mosaic_overlay
import miblab_dl as dl

# %% [markdown]
# ## Download data

# %%
dixon_array, spacing, _ = dl.load_dixon_case()

# %% [markdown]
# ## Predict kidney masks

# %%
kidneys = dl.kidney_dixon(dixon_array, spacing, verbose=False)

# %% [markdown]
# ## Compute rsf candidates

# %%
water, fat = dixon_array[..., 2], dixon_array[..., 3]
rsf_candidates = dl.rsf_candidates(fat, water, kidneys, fat_threshold=0.5)

# %% [markdown]
# ## Combine all labels

# %%
# Increment rsf labels so they are different from kidney labels
rsf_candidates[rsf_candidates > 0] += 2

# Combine into one label (rsf takes precedence on overlap)
label_image = np.where(rsf_candidates > 0, rsf_candidates, kidneys)

# %% [markdown]
# ## Display resulting label

# %%
# %matplotlib inline

out_phase = dixon_array[...,0]
opacity = 0.6
colors = [
    [1.0, 0.0, 0.0, opacity],   # red
    [0.0, 1.0, 0.0, opacity],   # green
    [0.0, 1.0, 0.0, opacity],   # green
    [1.0, 0.0, 0.0, opacity],   # red
]
mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    verbose=0,
    colors=colors,
)

# %% [markdown]
# ## Repeat with a lower fat threshold

# %%
# %matplotlib inline
rsf_candidates = dl.rsf_candidates(fat, water, kidneys, fat_threshold=0.2)
rsf_candidates[rsf_candidates > 0] += 2
label_image = np.where(rsf_candidates > 0, rsf_candidates, kidneys)
mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    verbose=0,
    colors=colors,
)