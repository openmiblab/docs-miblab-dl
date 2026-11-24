# %% [markdown]
# # Kidney on Dixon: batch processing
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_pc_dixon_batch` model to 
# segment kidney parenchyma on Dixon data.

# %% 
import numpy as np
import vreg
import miblab_dl as dl
from miblab_plot import mosaic_overlay

from _data_loader import dixon_batch_case

# %% [markdown]
# ## Download Dixon data

# %%
input_folder = dixon_batch_case()
output_folder = dl.get_cache_dir('Dixon_batch_results')

# %% [markdown]
# ## Use miblab_dl to predict kidney masks

# %%
dl.kidney_pc_dixon_batch(input_folder, output_folder)

# %% [markdown]
# Read the arrays in (data and results)

# %%
case = 'Dixon'   # the case name used when the files were written

in_phase = vreg.read_nifti(input_folder / f'{case}_0001.nii.gz').values
label_image = vreg.read_nifti(output_folder / f'{case}.nii.gz').values

# %%
# ## Sanity check on the results
# assert np.sum(label_image==1) == 79285
print(np.sum(label_image==1))

# %% [markdown]
# ## Display result using mosaic overlay

# %%
# %matplotlib inline

mosaic_overlay(
    in_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.4,
    verbose=0,
)