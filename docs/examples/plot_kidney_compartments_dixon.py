# %% [markdown]
# # Kidney compartments on Dixon (case)
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_compartments_dixon` model to 
# segment renal parenchyma and renal sinus fat on Dixon data.

# %% 
import miblab_dl as dl
from miblab_plot import mosaic_overlay

from _data_loader import dixon_case

# %% [markdown]
# ## Download data

# %%
array_4d, spacing = dixon_case()

# %% [markdown]
# ## Predict renal sinus fat masks

# %%
label_image = dl.kidney_compartments_dixon(array_4d, verbose=False)

# %% [markdown]
# ## Display results

# %%
# %matplotlib inline

out_phase = array_4d[...,0]
colors = [
    [1.0, 0.0, 0.0, 0.6],   # red
    [0.0, 1.0, 0.0, 0.6],   # green
    [1.0, 0.0, 0.0, 0.6],   # red
    [0.0, 1.0, 0.0, 0.6],   # green
]
mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    verbose=0,
    colors=colors,
)