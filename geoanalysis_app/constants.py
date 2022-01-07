import os


# DATASET
DATA_DIRECTORY_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# RAW_DATA_PATH = os.path.join(DATA_DIRECTORY_PATH, "data", "data.csv")
RAW_DATA_PATH = os.path.join(DATA_DIRECTORY_PATH, "data", "E-Scooter_500.csv")

# GEOGRAPHY
CHICAGO_COORDINATES = (41.8781, -87.6298)

# DATA FILTERING
TIMES_OF_DAY = ["RANO", "POŁUDNIE", "WIECZÓR", "NOC"]
DAY_TYPES = ["NORMALNY", "ŚWIĄTECZNY"]
