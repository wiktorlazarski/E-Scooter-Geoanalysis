import pandas as pd

from geoanalysis_app import constants as C


def load_data():
    return pd.read_csv(C.RAW_DATA_PATH)
