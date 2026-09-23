# PFE
## Downloading raw data
Run `download_data.py`to download raw v2 data from PILOT.
> **Note:** the raw data for some versions (eg lisaCat) are not stored in dictionaries and so the folder had to be downloaded by hand and then formatted, see second half of script.

## Formating Raw Data
Run `format_data.py`to format the raw data downloaded using `download_data.py`. This script reorders the raw measurements into chronological order (measures may not have been acquired in this order - acquisition order information retrieved from the relevant metadata file), checks dimensions, and bins according to bin_fact. Adjust formatting parameters according to raw data in question if necessary. The final measurement array is saved as `m_binned.npy`, and is of dimensions $(N_y \times \Lambda \times P)$, where $N_y$ is the spatial dimension, $\Lambda$ is the spectral dimension, and $P$ is the number of nonegative patterns applied (twice the number of virtual rows in the case of negative virtual matrices).

## Dark Noise
Dark noise images and constants were estimated from a set of K dark acquisitions:

$$
\hat{\mu}_d(x,y) = \frac{1}{K}\sum_{k=1}^K D_k(x,y) \approx \mathbb{E}[\mathbf{D}]
$$

$$
\hat{\sigma}_d^2(x,y) = \frac{1}{K-1}\sum_{k=1}^K \big(D_k(x,y) - \hat{\mu}_d(x,y)\big)^2 \approx \text{Var}[\mathbf{D}]
$$
> **Note:** the raw dark data must already be stored on your local machine. The dark acquisitions used in this project were saved locally and were never uploaded to the PILOT.


To reproduce the calculation of the dark noise images and constants for a given acquisition configuration, run `dark_estimation.py`.

To loop over a set of acquisition parameters, run `dark_estimation_loop.py`, adjusting it to the desired parameters.

In future the data may be uploaded to the PILOT, in which case the `download_data.py` script can be used.

## Gain Conversion

Gain conversion images (gain per pixel) and gain constants (average over pixels in gain image) were calculated from a set of uniformly illuminated acquisitions using the photon transfer curve.

To calculate the gain images for a given camera configuration, run `conversion_gain_estim.py`.

> **Note:** once again, the raw bright data must already be stored on your local machine.

Two methods for calculating a constant gain parameter per camera configuration are implemented compared:

**Flatfield Pair Method:** Expected value and variation of count rate calculated from Photon Transfer Curve using spatial averaging over pixels in a region of interest -> technically only two acquisitions are needed, but here I also averaged temporally (over 500 pairs) because I had 1000 acquisiitons per intensity level. 

Acquire a flat-field image pair $(Y_1, Y_2)$ under identical illumination and take the difference $D = Y_1 - Y_2$. Since $Y_1, Y_2$ are independent draws of the same random variable $Y$:

$$
\mathbb{E}[D] = 0
$$

$$
\text{Var}[D] = 2\,\text{Var}[Y] = 2(\gamma^2 s + \sigma_d^2)
$$

Differencing cancels any fixed pattern offset but doubles the variance, so

$$
\hat{\sigma}^2 := \frac{\text{Var}[D]}{2} = \gamma^2 s + \sigma_d^2
$$

Let $\hat{S}$ denote the averaged, dark-subtracted mean of $Y_1, Y_2$ — each containing $N$ pixels in total:

$$
\bar{Y}_1 = \frac{1}{N}\sum_{n=1}^N \big(Y_1(n) - \mu_d\big)
$$

$$
\bar{Y}_2 = \frac{1}{N}\sum_{n=1}^N \big(Y_2(n) - \mu_d\big)
$$

$$
\hat{S} = \frac{\bar{Y}_1 + \bar{Y}_2}{2}
$$

From above, the dark-subtracted signal is $\gamma s$, so $\hat{S} \approx \gamma s$. Substituting $s = \hat{S}/\gamma$ gives

$$
\hat{\sigma}^2 = \gamma^2\left(\frac{\hat{S}}{\gamma}\right) + \sigma_d^2 = \gamma\hat{S} + \sigma_d^2
$$

This is a straight line in the directly measurable, dark-subtracted quantity $\hat{S}$: the slope recovers the gain $\gamma$, and the intercept is $\sigma_d^2$.


**Temporal Estimate Method:** Gain value calculated per pixel from expected value and variation images, which are the temporal average over 1000 aqcuisitions. The constant gain is then the spatial average within a region of interest. 
At each illumination level, $N$ repeated exposures are acquired, $\mathbf{Y} = \{Y_1, \dots, Y_N\}$, and the temporal sample mean and variance per pixel are computed as:

$$
\hat{\mu}(x,y) = \frac{1}{N}\sum_{n=1}^N Y_n(x,y), \qquad \hat{\sigma}^2(x,y) = \frac{1}{N-1}\sum_{n=1}^N \big(Y_n(x,y) - \hat{\mu}(x,y)\big)^2
$$

Plotting $(\hat{\mu}, \hat{\sigma}^2)$ pairs and fitting a line gives the gain from the slope. This can be done per pixel, for a full gain map, or using the spatial average of the mean and variance images, for a single scalar gain.

Both methods are implemented in the python script, with adjustable parameters to take into account the various acquisition and reconstruction parameters (i.e; camera gain, binning etc)

## Image covariance prior

To calculate the 1D covariance prior over the rows of a set of natural images (ImageNet dataset) run `covariance_prior.py`with the desired parameters (image size, normalisation etc). The resulting covariance matrix is saved to a data folder. 

## Reconstruction
Ruņ `reconstruction.py` to reconstruct data that has been downloaded from PILOT using `download_data.py`and formatted using `format_data.py`. 

Pseudoinverse and tikhonov reconstruction is implemented, with the option to apply denoising using a UNet() trained by running `train.py`and the desired parameters. 

The reconstructed cubes are plotted as the sum over wavelength channels and per wavelength channel individually. 


# Training Denoiser
To train a UNet() denoiser, run `train.py` with the desired parameters. Trained weights will be saved to a 'model' folder and can then be used during reconstruction. 
