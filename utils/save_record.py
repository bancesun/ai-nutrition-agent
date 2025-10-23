import pandas as pd
import os
from datetime import datetime

def save_record(time, name, kcal, carbs, protein, fat):
    df = pd.read_csv("data/records.csv") if os.path.exists("data/records.csv") else pd.DataFrame(
        columns=["time", "food", "kcal", "carbs", "protein", "fat"]
    )
    df.loc[len(df)] = [time, name, kcal, carbs, protein, fat]
    df.to_csv("data/records.csv", index=False)
