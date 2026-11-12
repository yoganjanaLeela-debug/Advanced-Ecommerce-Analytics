from pathlib import Path
import pandas as pd

# Project folder locations
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "Dataset" / "Raw"
OUTPUT_FOLDER = PROJECT_FOLDER / "Documentation"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Dataset files
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

results = []

print("=" * 60)
print("DATA TYPES ANALYSIS")
print("=" * 60)

for filename in csv_files:

    file_path = DATA_FOLDER / filename

    if not file_path.exists():
        print(f"File not found: {filename}")
        continue

    df = pd.read_csv(file_path)

    print(f"\nDataset: {filename}")
    print("-" * 60)

    for column in df.columns:

        data_type = str(df[column].dtype)

        print(f"{column}: {data_type}")

        results.append({
            "Dataset": filename,
            "Column": column,
            "Data_Type": data_type,
            "Missing_Values": int(df[column].isnull().sum()),
        })

# Save the results
report = pd.DataFrame(results)

output_path = OUTPUT_FOLDER / "data_types_report.csv"
report.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("DATA TYPES ANALYSIS COMPLETED")
print(f"Report saved to: {output_path}")
print("=" * 60)