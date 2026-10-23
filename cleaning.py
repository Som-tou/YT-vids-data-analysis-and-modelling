import os
import pandas as pd
import numpy
from dotenv import load_dotenv

load_dotenv()

yt_data_path = os.getenv("DATASET_PATH") 
yt_df = pd.read_csv(yt_data_path)

yt_df = yt_df.drop_duplicates()

for col in yt_df.select_dtypes(include=['number']).columns:
    Q1 = yt_df[col].quantile(0.25)
    Q3 = yt_df[col].quantile(0.75)

    IQR = Q3-Q1

    lower_bound = Q1-IQR*1.5
    upper_bound = Q3+IQR*1.5

    yt_df[col] = yt_df[col].clip(lower=lower_bound, upper=upper_bound)

yt_df["description"] = yt_df["description"].fillna("None")
cts = yt_df.loc[yt_df["description"].isna()]
print(cts)

