"""
===============
Kidney PC Dixon
===============

These example shows the use of the `~miblab_dl.kidney_pc_dixon` model to 
segment kidney parenchyma on dixon data. 
"""

# %%
# Import packages
# ---------------
import numpy as np
import dbdicom as db
import miblab_dl as dl


# %%
# Download test data
folder = dl.fetch('Dixon')

# %%
# Read DICOM data in a 4D array in the correct order
study = db.studies(folder)[0]
series = [
    'Dixon_post_contrast_out_phase', 
    'Dixon_post_contrast_in_phase', 
    'Dixon_post_contrast_water',
    'Dixon_post_contrast_fat',
]
names = ['out_phase', 'in_phase', 'water', 'fat']
#series = [db.series(folder, contains=name)[0] for name in names]
#arrays = [db.pixel_data(s) for s in series]
arrays = [db.pixel_data(study + [s]) for s in series]
array = np.stack(arrays, axis=-1)

# %%
# Create kidney masks
mask = dl.kidney_pc_dixon(array, verbose=True)

# %%
# Test result
assert np.sum(mask==1) == 79285

# sphinx_gallery_start_ignore
# sphinx_gallery_thumbnail_number = -1
# sphinx_gallery_end_ignore
