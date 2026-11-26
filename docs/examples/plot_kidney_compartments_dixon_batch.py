# %% [markdown]
# # Kidney compartments on Dixon (batch)
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_compartments_dixon_batch` model to 
# segment renal parenchyma and renal sinus fat on Dixon data.

# %% 
import vreg
import miblab_dl as dl
from miblab_plot import mosaic_overlay

from _data_loader import dixon_batch_case

# %% [markdown]
# ## Download data

# %%
case='Dixon'
input_folder = dixon_batch_case(case)
output_folder = dl.get_cache_dir('Dixon_batch_results')

# %% [markdown]
# ## Predict renal sinus fat masks

# %%
dl.kidney_compartments_dixon_batch(input_folder, output_folder)

# %% [markdown]
# ## Display results

# %%
# Read the arrays
out_phase = vreg.read_nifti(input_folder / f'{case}_0000.nii.gz').values
label_image = vreg.read_nifti(output_folder / f'{case}.nii.gz').values

# %%
# Create plot
# %matplotlib inline

colors = [
    [1.0, 0.0, 0.0, 0.6],   # red
    [0.0, 1.0, 0.0, 0.6],   # green
    [0.0, 1.0, 0.0, 0.6],   # green
    [1.0, 0.0, 0.0, 0.6],   # red
]
mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.6,
    verbose=0,
    colors=colors
)