# %% [markdown]
# # Kidney on Dixon: case-by-case processing
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_dixon` model to 
# segment kidney parenchyma on Dixon data.

# %% 
import miblab_dl as dl
from miblab_plot import mosaic_overlay

from _data_loader import dixon_case

# %% [markdown]
# ## Download data

# %%
array_4d, spacing = dixon_case()

# %% [markdown]
# ## Predict kidney masks

# %%
label_image = dl.kidney_dixon(array_4d, verbose=False)

# %% [markdown]
# ## Display results

# %%
# %matplotlib inline
out_phase = array_4d[...,0]

mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.4,
    verbose=0,
)