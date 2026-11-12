from pathlib import Path
import pandas as pd

# Locate the project and dataset folders
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "Dataset" / "Raw"
OUTPUT_FOLDER = PROJECT_FOLDER / "Documentation"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# All nine datasets
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
print("MISSING VALUES ANALYSIS")
print("=" * 60)

for filename in csv_files:

    file_path = DATA_FOLDER / filename

    if not file_path.exists():
        print(f"File not found: {filename}")
        continue

    df = pd.read_csv(file_path)

    print(f"\nDataset: {filename}")

    # Calculate missing values for each column
    missing_counts = df.isnull().sum()

    for column, count in missing_counts.items():

        if count > 0:
            percentage = (count / len(df)) * 100

            print(
                f"{column}: {count:,} missing "
                f"({percentage:.2f}%)"
            )

            results.append({
                "Dataset": filename,
                "Column": column,
                "Total_Rows": len(df),
                "Missing_Values": int(count),
                "Missing_Percentage": round(percentage, 2),
            })

    if missing_counts.sum() == 0:
        print("No missing values found.")

# Create a report
report = pd.DataFrame(results)

output_path = OUTPUT_FOLDER / "missing_values_report.csv"

report.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("MISSING VALUES ANALYSIS COMPLETED")
print(f"Report saved to: {output_path}")
print("=" * 60)