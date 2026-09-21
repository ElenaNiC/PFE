# PFE

## Dark Noise

Scripts for estimating dark noise images and constants from dark acquisitions.

> **Note:** the raw dark data must be stored on your local machine. The dark acquisitions used in this project were saved locally and were never uploaded to the PILOT.

### Scripts

| Script | Purpose |
|---|---|
| `dark_estimation.py` | Computes the dark noise images and constants for a single acquisition configuration. |
| `dark_estimation_loop.py` | Runs the same calculation over a set of acquisition parameters. Adjust the parameters at the top of the script. |
| `download_data.py` | Downloads data from the PILOT. Not needed for now, but usable if the data is uploaded there in future. |

### Usage

**Single configuration**

```bash
python dark_estimation.py
```

**Loop over several configurations**

```bash
python dark_estimation_loop.py
```

Before running either script, make sure the raw data folder is on your machine and that the path in the script points to it.
