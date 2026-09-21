
#%% Download data from PILOT

from pathlib import Path
from spyrit.misc.load_data import download_girder

# where to save data
destination = Path("C:/Users/ceidigh/Documents/PFE/")
print("Copying folder in:", destination)

# download data from the Pilot warehouse
url_pilot = "https://pilot-warehouse.creatis.insa-lyon.fr/api/v1"

datasets = [
    {
        "subfolder": "data/opticalTuningCat2",
        "comment": "SPIHIM/data/setup_v2.02026-06-19_optical_tuning/",
        "files": [
            "6a353465c392eb77b9ec1316",  # obj_cat2_..._zoom_x2/spectral_data.npz
            "6a35344cc392eb77b9ec0fff",  # metadata
            "6a35344cc392eb77b9ec0ffc",  # had
        ],
    },
    {
        "subfolder": "data/opticalTuningCat3",
        "comment": "SPIHIM/data/setup_v2.02026-06-19_optical_tuning/",
        "files": [
            "6a354d7cc392eb77b9ec162b",  # obj_cat3_..._zoom_x2/spectral_data.npz
            "6a354d65c392eb77b9ec131d",  # metadata
            "6a354d65c392eb77b9ec131a",  # had
        ],
    },
    {
        "subfolder": "data/USAF",
        "comment": "SPIHIM/data/setup_v2.02025-06-20_lens_tuning",
        "files": [
            "685522df3978e07db274b8a9",  # obj_USAF_..._zoom_x1/spectral_data.npz
            "685522b53978e07db274b592",  # metadata
            "685522b53978e07db274b58f",  # had
        ],
    },
    {
        "subfolder": "data/USAF2",
        "comment": "SPIHIM/data/setup_v2.02025-06-20_lens_tuning",
        "files": [
            "6855414a3978e07db274cb0e",  # obj_USAF2_..._zoom_x1/spectral_dat.npz
            "6855412b3978e07db274c4f4",  # metadata
            "6855412b3978e07db274c4f1",  # had
        ],
    },
]

for ds in datasets:
    data_subfolder = Path(ds["subfolder"])
    try:
        download_girder(url_pilot, ds["files"], data_subfolder)
    except Exception as e:
        print(f"Unable to download data from the Pilot warehouse ({ds['subfolder']})")
        print(e)

# %%
