from pathlib import Path
import pandas as pd

# Project folder paths
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
RAW_FOLDER = PROJECT_FOLDER / "Dataset" / "Raw"
CLEANED_FOLDER = PROJECT_FOLDER / "Dataset" / "Cleaned"

CLEANED_FOLDER.mkdir(parents=True, exist_ok=True)

# CSV files
csv_files = [
    "olist_customers_dataset.csv",
    "olist_geolocation_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_orders_dataset.csv",
    "olist_products_dataset.csv",
    "olist_sellers_dataset.csv",
    "product_category_name_translation.csv",
]

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

for filename in csv_files:

    raw_path = RAW_FOLDER / filename
    cleaned_path = CLEANED_FOLDER / filename

    if not raw_path.exists():
        print(f"File not found: {filename}")
        continue

    # Read original data
    df = pd.read_csv(raw_path)

    original_rows = len(df)

    # Remove exact duplicate rows only
    df = df.drop_duplicates()

    cleaned_rows = len(df)
    removed_rows = original_rows - cleaned_rows

    # Convert order date columns to datetime
    if filename == "olist_orders_dataset.csv":

        date_columns = [
            "order_purchase_timestamp",
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ]

        for column in date_columns:
            df[column] = pd.to_datetime(
                df[column], errors="coerce"
            )

    # Save cleaned copy
    df.to_csv(cleaned_path, index=False)

    print(f"\nFile: {filename}")
    print(f"Original rows: {original_rows:,}")
    print(f"Cleaned rows: {cleaned_rows:,}")
    print(f"Duplicate rows removed: {removed_rows:,}")
    print(f"Saved to: {cleaned_path.name}")

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)