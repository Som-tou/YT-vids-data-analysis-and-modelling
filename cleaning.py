import os
import pandas as pd
import numpy
from dotenv import load_dotenv

load_dotenv()

yt_data_path = os.getenv("DATASET_PATH") 
yt_df = pd.read_csv(yt_data_path)

print(yt_df.head())