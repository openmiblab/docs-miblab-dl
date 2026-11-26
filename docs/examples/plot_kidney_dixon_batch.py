# %% [markdown]
# # Kidney on Dixon (batch)
#
# This example shows the use of the {py:func}`~miblab_dl.kidney_dixon_batch` model to 
# segment kidney parenchyma on Dixon data.

# %% 
import vreg
from miblab_plot import mosaic_overlay
import miblab_dl as dl

# %% [markdown]
# ## Download data

# %%
case='Dixon'
input_folder = dl.load_dixon_case_as_batch(case)
output_folder = dl.get_cache_dir('Dixon_batch_results')

# %% [markdown]
# ## Predict kidney masks

# %%
dl.kidney_dixon_batch(input_folder, output_folder)

# %% [markdown]
# ## Display results

# %%
# Read the arrays
out_phase = vreg.read_nifti(input_folder / f'{case}_0000.nii.gz').values
label_image = vreg.read_nifti(output_folder / f'{case}.nii.gz').values

# %%
# Create plot

# %matplotlib inline
mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.4,
    verbose=0,
)