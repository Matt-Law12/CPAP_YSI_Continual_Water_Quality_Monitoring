# this code appends all of the recorded ysi data into one file, filters out any values flagged as out-of-range, and then exprts the cleaned dataset as one complete .csv for visualization

import pandas as pd
import numpy as np
import os

csv_files = [
    r"C:\Users\law_m\Documents\YSI Dash\Data\CPAH2_2022.csv",
    r"C:\Users\law_m\Documents\YSI Dash\Data\cpah2_2023.csv",
    r"C:\Users\law_m\Documents\YSI Dash\Data\cpah2_2024_Q1_Q2_Q3.csv"
]

df_list = []

for file in csv_files:
    df = pd.read_csv(file, low_memory=False)
    if file != r"C:\Users\law_m\Documents\YSI Dash\Data\CPAH2_2022.csv":
        df = df.drop([0]).reset_index(drop=True)
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

combined_df.loc[combined_df["F_DO_mgl"].astype(
    str).str[:4] == "<-3>", "DO_mgl"] = np.nan
combined_df.loc[combined_df["F_DO_pct"].astype(
    str).str[:4] == "<-3>", "DO_pct"] = np.nan
combined_df.loc[combined_df["F_Depth"].astype(
    str).str[:4] == "<-3>", "Depth"] = np.nan
combined_df.loc[combined_df["F_Sal"].astype(
    str).str[:4] == "<-3>", "Sal"] = np.nan
combined_df.loc[combined_df["F_SpCond"].astype(
    str).str[:4] == "<-3>", "SpCond"] = np.nan
combined_df.loc[combined_df["F_Turb"].astype(
    str).str[:4] == "<-3>", "Turb"] = np.nan
combined_df.loc[combined_df["F_pH"].astype(
    str).str[:4] == "<-3>", "pH"] = np.nan
combined_df.loc[combined_df["F_Temp"].astype(
    str).str[:4] == "<-3>", "Temp"] = np.nan

output_path = r"C:\Users\law_m\Documents\YSI Dash\Data\CPAH2_all.csv"
combined_df.to_csv(output_path, index=False)

if os.path.exists(output_path):
    print("All CSV files have been combined into 'CPAH2_all.csv'")
else:
    print("Error: File was not created.")
