# PFE

## Dark Noise
Dark noise images and constants were estimated from a set of dark acquisitions

> **Note:** the raw dark data must already be stored on your local machine. The dark acquisitions used in this project were saved locally and were never uploaded to the PILOT.


To reproduce the calculation of the dark noise images and constants for a given acquisition configuration, run `dark_estimation.py`.

To loop over a set of acquisition parameters, run `dark_estimation_loop.py`, adjusting it to the desired parameters.

In future the data may be uploaded to the PILOT, in which case the `download_data.py` script can be used.

## Gain Conversion

Gain conversion images (gain per pixel) and gain constants (average over pixels in gain image) were calculated from a set of uniformly illuminated acquisitions.

To calculate the gain images for a given camera configuration, run `conversion_gain_estim.py`.

> **Note:** once again, the raw bright data must already be stored on your local machine.

Two methods for calculating a constant gain parameter per camera configuration are implemented compared:

**Flatfield Pair Method:** Expected value and variation of count rate calculated from Photon Transfer Curve using spatial averaging over pixels in a region of interest -> technically only two acquisitions are needed, but here I also averaged temporally (over 500 pairs) because I had 1000 acquisiitons per intensity level. 

**Temporal Estimate Method:** Gain value calculated per pixel from expected value and variation images, which are the temporal everage over 1000 aqcuisitions. The constant gain is then the spatial average within a region of interest. 
