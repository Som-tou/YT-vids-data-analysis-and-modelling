import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()

yt_data_path = os.getenv("DATASET_PATH") 
df = pd.read_csv(yt_data_path)

df = df.drop_duplicates()
df = df.drop_duplicates(["video_id", "trending_date"], keep="last")
df['has_description'] = df['description'].notna()
df['tags'] = df['tags'].replace('[none]',np.nan)
df['has_tags'] = df['description'].notna()
df['trending_date'] = pd.to_datetime(df['trending_date'], format="%y,%d,%m")
df['publish_time'] = pd.to_datetime(df['publish_time'], utc = True)
df.loc[df['ratings_disabled'], ['likes', 'dislikes']] = np.nan
df.loc[df['comments_disabled'], 'comment_count'] = np.nan

