# %% [markdown]
# # Renal sinus fat on Dixon (case)
#
# This example shows the use of the {py:func}`~miblab_dl.rsf_dixon` model to 
# segment renal sinus fat on Dixon data.

# %% 
import miblab_dl as dl
from miblab_plot import mosaic_overlay

from _data_loader import dixon_case

# %% [markdown]
# ## Download data

# %%
dixon_array, spacing = dixon_case()

# %% [markdown]
# ## Predict renal sinus fat masks

# %%
label_image = dl.rsf_dixon(dixon_array, verbose=False)

# %% [markdown]
# ## Display results

# %%
# %matplotlib inline

out_phase = dixon_array[...,0]
mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.6,
    verbose=0,
)