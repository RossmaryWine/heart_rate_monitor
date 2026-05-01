from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")


def inspect_file(file_path: Path) -> None:
    df = pd.read_csv(file_path)

    print("=" * 60)
    print(file_path)
    print("=" * 60)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nBasic info:")
    print(df.info())

    print("\nHeart-rate stats:")
    print(df["heart_rate"].describe())

    print("\nAnomaly counts:")
    print(df["is_anomaly"].value_counts())

    print("\nAnomaly percentage:")
    print(df["is_anomaly"].mean() * 100)


def main() -> None:
    csv_files = sorted(DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/")
        return

    for file_path in csv_files:
        inspect_file(file_path)


if __name__ == "__main__":
    main()