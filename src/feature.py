import pandas as pd


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["rolling_avg_5"] = df["heart_rate"].rolling(window=5).mean()
    df["rolling_std_5"] = df["heart_rate"].rolling(window=5).std()
    df["hr_change"] = df["heart_rate"].diff()
    df["abs_hr_change"] = df["hr_change"].abs()

    df = df.dropna().reset_index(drop=True)

    return df