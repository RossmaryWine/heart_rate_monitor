import pandas as pd 
import random
from pathlib import Path
import argparse
import csv

def generate_heart_rate_data(
    output_path: str = "data/heart_rate.csv",
    num_points: int = 5000,
    baseline: int = 78,
    anomaly_chance: float = 0.03
) -> None:
    
    #output_file_specific = output_path + str(anomaly_chance) + ".csv"
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    curr_heartrate = baseline

    for time in range(num_points):
        normal_change = random.randint(-3, 3)
        curr_heartrate += normal_change

        curr_heartrate = max(55, min(curr_heartrate, 105))

        is_anomaly = random.random() < anomaly_chance

        if is_anomaly:

            if random.choice(["spike", "drop"]) == "spike":
                heart_rate = random.randint(120,170)
            else:
                heart_rate = random.randint(35,50)

        else:
            heart_rate = curr_heartrate
        
        rows.append({
            "time": time,
            "heart_rate": heart_rate,
            "is_anom": int(is_anomaly),
        })

    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)

    print(f"Generated {num_points} rows at {output_file}")
    print(df.head())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate fake heart-rate data for anomaly detection."
    )

    parser.add_argument(
        "--output",
        default="data/heart_rate.csv",
        help="Where to save the generated CSV file.",
    )

    parser.add_argument(
        "--num-points",
        type=int,
        default=500,
        help="Number of heart-rate readings to generate.",
    )

    parser.add_argument(
        "--baseline",
        type=int,
        default=78,
        help="Normal heart-rate baseline.",
    )

    parser.add_argument(
        "--anomaly-chance",
        type=float,
        default=0.03,
        help="Chance of a row being an anomaly. Example: 0.03 means 3%%.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    generate_heart_rate_data(
        output_path=args.output,
        num_points=args.num_points,
        baseline=args.baseline,
        anomaly_chance=args.anomaly_chance,
    )