# %% [markdown]
# # Kidney compartments on Dixon (case)
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_compartments_dixon` model to 
# segment renal parenchyma and renal sinus fat on Dixon data.

# %% 
from miblab_plot import mosaic_overlay
import miblab_dl as dl

# %% [markdown]
# ## Download data

# %%
dixon_array, spacing, _ = dl.load_dixon_case()

# %% [markdown]
# ## Predict renal sinus fat masks

# %%
label_image = dl.kidney_compartments_dixon(dixon_array, spacing, verbose=False)

# %% [markdown]
# ## Display results

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