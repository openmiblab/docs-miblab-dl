import numpy as np
import dbdicom as db
import vreg
import miblab_dl as dl

def dixon_case():
    folder = dl.fetch('Dixon')

    # Read DICOM data in the correct order. 
    desc = ['out_phase', 'in_phase', 'water', 'fat']
    dicom_series = [db.series(folder, contains=d)[0] for d in desc]
    volumes = [db.volume(series, verbose=0) for series in dicom_series]

    # Convert to a 4D input array and read spacing
    array = np.stack([v.values for v in volumes], axis=-1)
    spacing = volumes[0].spacing

    return array, spacing

def dixon_batch_case(case='Dixon'):
    """Write the Dixon test case as NIfTI files for kidney_dixon_batch.

    The four channels are saved as ``<case>_0000.nii.gz`` (out-phase),
    ``_0001`` (in-phase), ``_0002`` (water) and ``_0003`` (fat). The voxel
    spacing is stored in the affine.

    Returns:
        Path: The folder with the NIfTI files.
    """
    folder = dl.fetch(case)

    # Read DICOM data in the correct order
    desc = ['out_phase', 'in_phase', 'water', 'fat']
    dicom_series = [db.series(folder, contains=d)[0] for d in desc]
    volumes = [db.volume(series, verbose=0) for series in dicom_series]

    batch_folder = dl.get_cache_dir('Dixon_batch')
    for i, volume in enumerate(volumes):
        nifti_file = batch_folder / f'{case}_{i:04d}.nii.gz'
        # for now: save with the incorrect affine
        # When new model is implemented, check that this works correctly
        v = vreg.volume(volume.values, np.eye(4))
        vreg.write_nifti(v, nifti_file)

    return batch_folder