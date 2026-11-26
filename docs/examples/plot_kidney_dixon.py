# %% [markdown]
# # Kidney on Dixon (case)
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_dixon` model to 
# segment kidney parenchyma on Dixon data.

# %% 
from miblab_plot import mosaic_overlay
import miblab_dl as dl

# %% [markdown]
# ## Download data

# %%
dixon_array, spacing = dl.load_dixon_case()

# %% [markdown]
# ## Predict kidney masks

# %%
label_image = dl.kidney_dixon(dixon_array, spacing, verbose=False)

# %% [markdown]
# ## Display results

# %%
# %matplotlib inline
out_phase = dixon_array[...,0]

mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.4,
    verbose=0,
)