from pathlib import Path
import pandas as pd

# Project folders
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
print("DUPLICATE RECORDS ANALYSIS")
print("=" * 60)

for filename in csv_files:

    file_path = DATA_FOLDER / filename

    if not file_path.exists():
        print(f"File not found: {filename}")
        continue

    df = pd.read_csv(file_path)

    # Count complete duplicate rows
    duplicate_count = int(df.duplicated().sum())

    # Calculate percentage of duplicate rows
    duplicate_percentage = (
        duplicate_count / len(df) * 100
        if len(df) > 0 else 0
    )

    print(f"\nDataset: {filename}")
    print(f"Total rows: {len(df):,}")
    print(f"Duplicate rows: {duplicate_count:,}")
    print(f"Duplicate percentage: {duplicate_percentage:.2f}%")

    results.append({
        "Dataset": filename,
        "Total_Rows": len(df),
        "Duplicate_Rows": duplicate_count,
        "Duplicate_Percentage": round(duplicate_percentage, 2),
    })

# Create a summary report
report = pd.DataFrame(results)

output_path = OUTPUT_FOLDER / "duplicate_analysis_report.csv"
report.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("DUPLICATE ANALYSIS COMPLETED")
print(f"Report saved to: {output_path}")
print("=" * 60)