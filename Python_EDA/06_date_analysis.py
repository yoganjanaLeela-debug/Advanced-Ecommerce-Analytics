from pathlib import Path
import pandas as pd

# Project folder locations
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "Dataset" / "Raw"
OUTPUT_FOLDER = PROJECT_FOLDER / "Documentation"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Orders dataset
file_path = DATA_FOLDER / "olist_orders_dataset.csv"

df = pd.read_csv(file_path)

# Date columns
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

print("=" * 60)
print("ORDER DATE ANALYSIS")
print("=" * 60)

results = []

for column in date_columns:

    # Convert text into datetime
    df[column] = pd.to_datetime(df[column], errors="coerce")

    missing = int(df[column].isna().sum())

    valid_dates = df[column].dropna()

    if not valid_dates.empty:
        earliest_date = valid_dates.min()
        latest_date = valid_dates.max()
    else:
        earliest_date = None
        latest_date = None

    print(f"\nColumn: {column}")
    print(f"Missing dates: {missing:,}")
    print(f"Earliest date: {earliest_date}")
    print(f"Latest date: {latest_date}")

    results.append({
        "Column": column,
        "Missing_Dates": missing,
        "Earliest_Date": earliest_date,
        "Latest_Date": latest_date,
    })

# Save report
report = pd.DataFrame(results)

output_path = OUTPUT_FOLDER / "date_analysis_report.csv"
report.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("DATE ANALYSIS COMPLETED")
print(f"Report saved to: {output_path}")
print("=" * 60)