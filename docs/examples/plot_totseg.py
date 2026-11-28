# %% [markdown]
# # TotalSegmentator on Dixon (case)
#
# This example shows the use of the {py:func}`~miblab_dl.totseg` 
# wrapper for TotalSegmentator omn Dixon data.

# %% 
from miblab_plot import mosaic_overlay
import miblab_dl as dl

# %% [markdown]
# ## Download data

# %%
dixon_array, _, affine = dl.load_dixon_case()

# %% [markdown]
# ## Segment all organs

# %%
out_phase = dixon_array[...,0]
label_image = dl.totseg(out_phase, affine=affine, task='total_mr')

# %% [markdown]
# ## Display results

# %%
# %matplotlib inline

mosaic_overlay(
    out_phase,
    label_image,
    margin=[16,16,2],
    opacity=0.6,
    verbose=0,
)