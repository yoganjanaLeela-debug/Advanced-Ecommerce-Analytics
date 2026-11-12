from pathlib import Path
import pandas as pd

# Find the project folders
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "Dataset" / "Raw"
OUTPUT_FOLDER = PROJECT_FOLDER / "Documentation"

# Create Documentation folder if it doesn't exist
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# All nine dataset files
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

# Store summary information
summary = []

for filename in csv_files:
    file_path = DATA_FOLDER / filename

    print(f"Analysing: {filename}")

    if not file_path.exists():
        print(f"File not found: {filename}")
        continue

    df = pd.read_csv(file_path)

    summary.append({
        "Dataset": filename,
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing_Values": int(df.isnull().sum().sum()),
        "Duplicate_Rows": int(df.duplicated().sum()),
        "Memory_Usage_MB": round(
            df.memory_usage(deep=True).sum() / (1024 ** 2), 2
        ),
    })

# Convert summary into a DataFrame
summary_df = pd.DataFrame(summary)

# Save the report
output_path = OUTPUT_FOLDER / "dataset_summary.csv"
summary_df.to_csv(output_path, index=False)

print("\n" + "=" * 50)
print("DATASET SUMMARY")
print("=" * 50)
print(summary_df.to_string(index=False))

print(f"\nReport saved successfully!")
print(f"Location: {output_path}")