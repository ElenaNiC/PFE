# PFE
## Dark Noise
To reproduce the calculation of the dark noise images and constants for a given acquisition configuration, run dark_estimation.py
Note the data must first be stored on local machine - the dark acquisitions used in the prjoect were stored directly on local
and never uploaded to the PILOT.

To loop over a set of acquisition parameters run dark_estimation_loop.py, adjusting to the desired parameters
Again, data must already be saved on local - in future maybe data will be uploaded to the PILOT, in which case the
download_data.py script can be used.
