# %% [markdown]
# # Kidney PC Dixon
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_pc_dixon` model to 
# segment kidney parenchyma on Dixon data.

# %%
import numpy as np
import dbdicom as db
import miblab_dl as dl

# %% [markdown]
# ## Download test data

# %%
folder = dl.fetch('Dixon')

# %% [markdown]
# ## Read DICOM data in a 4D array in the correct order

# %%
study = db.studies(folder)[0]
series = [
    'Dixon_post_contrast_out_phase', 
    'Dixon_post_contrast_in_phase', 
    'Dixon_post_contrast_water',
    'Dixon_post_contrast_fat',
]
arrays = [db.pixel_data(study + [s]) for s in series]
array = np.stack(arrays, axis=-1)

# %% [markdown]
# ## Create kidney masks

# %%
mask = dl.kidney_pc_dixon(array, verbose=True)

# %%
assert np.sum(mask==1) == 79285