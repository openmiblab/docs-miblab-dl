# %% [markdown]
# # Renal sinus fat on Dixon (case)
#
# This example shows the use of the {py:func}`~miblab_dl.rsf_dixon` model to 
# segment renal sinus fat on Dixon data.

# %% 
from miblab_plot import mosaic_overlay
import miblab_dl as dl

# %% [markdown]
# ## Download data

# %%
dixon_array, spacing = dl.load_dixon_case()

# %% [markdown]
# ## Predict renal sinus fat masks

# %%
label_image = dl.rsf_dixon(dixon_array, spacing, verbose=False)

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