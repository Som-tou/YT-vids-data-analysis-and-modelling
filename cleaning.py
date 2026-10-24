import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()

yt_data_path = os.getenv("DATASET_PATH") 
yt_df = pd.read_csv(yt_data_path)

yt_df = yt_df.drop_duplicates()

yt_df['has_description'] = yt_df['description'].notna()
yt_df['tags'] = yt_df['tags'].replace('[none]',np.nan)
yt_df['has_tags'] = yt_df['description'].notna()


