# PFE

## Dark Noise

Scripts for estimating dark noise images and constants from dark acquisitions.

> **Note:** the raw dark data must be stored on your local machine. The dark acquisitions used in this project were saved locally and were never uploaded to the PILOT.


To reproduce the calculation of the dark noise images and constants for a given acquisition configuration, run `dark_estimation.py`.

To loop over a set of acquisition parameters, run `dark_estimation_loop.py`, adjusting it to the desired parameters.

In future the data may be uploaded to the PILOT, in which case the `download_data.py` script can be used.

