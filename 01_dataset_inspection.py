from pathlib import Path
import pandas as pd

# Locate the Raw dataset folder
DATA_FOLDER = (
    Path(__file__).resolve().parent.parent
    / "Dataset"
    / "Raw"
)

# List of all nine CSV files
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
print("OLIST E-COMMERCE DATASET INSPECTION")
print("=" * 60)

for filename in csv_files:

    file_path = DATA_FOLDER / filename

    print(f"\nDataset: {filename}")
    print("-" * 60)

    if not file_path.exists():
        print("ERROR: File not found!")
        print(f"Expected location: {file_path}")
        continue

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Display dataset dimensions
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")

    # Check missing values
    print(f"Missing values: {df.isnull().sum().sum():,}")

    # Check exact duplicate rows
    print(f"Duplicate rows: {df.duplicated().sum():,}")

    # Display column names
    print("\nColumn names:")
    print(df.columns.tolist())

    # Display first three records
    print("\nFirst 3 rows:")
    print(df.head(3).to_string(index=False))

print("\n" + "=" * 60)
print("INSPECTION COMPLETED")
print("=" * 60)