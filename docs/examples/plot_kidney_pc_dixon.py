# %% [markdown]
# # Kidney on Dixon: case-by-case processing
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_pc_dixon` model to 
# segment kidney parenchyma on Dixon data.

# %% 
import numpy as np
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
# TODO: Check why results are incorrect when the correct spacing is given
# label_image = dl.kidney_pc_dixon(array, spacing, verbose=False)
label_image = dl.kidney_pc_dixon(array_4d, verbose=False)

# %%
# ## Sanity check on the results
# assert np.sum(label_image==1) == 79285
print(np.sum(label_image==1))

# %% [markdown]
# ## Display result using mosaic overlay

# %%
# %matplotlib inline
in_phase = array_4d[...,1]

mosaic_overlay(
    in_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.4,
    verbose=0,
)