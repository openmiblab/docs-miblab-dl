# %% [markdown]
# # Renal sinus fat on Dixon (case-by-case)
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
array_4d, spacing = dixon_case()

# %% [markdown]
# ## Predict renal sinus fat masks

# %%
label_image = dl.rsf_dixon(array_4d, verbose=False)

# %% [markdown]
# ## Display results

# %%
# %matplotlib inline

out_phase = array_4d[...,0]
mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.6,
    verbose=0,
)