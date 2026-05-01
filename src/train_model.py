from pathlib import Path

import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

from features import add_features


TRAIN_FILE = Path("data/hr_3_percent.csv")


FEATURE_COLUMNS = [
    "heart_rate",
    "rolling_avg_5",
    "rolling_std_5",
    "hr_change",
    "abs_hr_change",
]


def main() -> None:
    df = pd.read_csv(TRAIN_FILE)
    df = add_features(df)

    X = df[FEATURE_COLUMNS]
    y_true = df["is_anomaly"]

    model = IsolationForest(
        contamination=0.03,
        random_state=42,
    )

    model.fit(X)

    predictions = model.predict(X)

    # IsolationForest gives:
    #  1  = normal
    # -1  = anomaly
    y_pred = [1 if pred == -1 else 0 for pred in predictions]

    print(classification_report(y_true, y_pred))


if __name__ == "__main__":
    main()