import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)

    # Convert Date column
    df["Date"] = pd.to_datetime(df["Date"])

    return df