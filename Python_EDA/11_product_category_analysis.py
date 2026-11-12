from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project folders
PROJECT_FOLDER = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_FOLDER / "Dataset" / "Cleaned"
OUTPUT_FOLDER = PROJECT_FOLDER / "Documentation"
CHART_FOLDER = OUTPUT_FOLDER / "Charts"

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
CHART_FOLDER.mkdir(parents=True, exist_ok=True)

# Load datasets
items = pd.read_csv(
    DATA_FOLDER / "olist_order_items_dataset.csv"
)

products = pd.read_csv(
    DATA_FOLDER / "olist_products_dataset.csv"
)

translation = pd.read_csv(
    DATA_FOLDER / "product_category_name_translation.csv"
)

# Join order items with products
sales = items.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left",
    validate="many_to_one"
)

# Translate Portuguese category names into English
sales = sales.merge(
    translation,
    on="product_category_name",
    how="left",
    validate="many_to_one"
)

# Use translated category names where available
sales["Category"] = sales[
    "product_category_name_english"
].fillna(sales["product_category_name"])

# Label missing categories
sales["Category"] = sales["Category"].fillna(
    "Unknown Category"
)

# Summarise category performance
category_analysis = (
    sales.groupby("Category", as_index=False)
    .agg(
        Total_Revenue=("price", "sum"),
        Total_Items_Sold=("order_item_id", "count"),
        Unique_Orders=("order_id", "nunique")
    )
)

category_analysis["Total_Revenue"] = (
    category_analysis["Total_Revenue"].round(2)
)

category_analysis = category_analysis.sort_values(
    "Total_Revenue",
    ascending=False
)

# Display top 15 categories
print("=" * 70)
print("PRODUCT CATEGORY ANALYSIS")
print("=" * 70)

print(
    category_analysis.head(15).to_string(index=False)
)

# Save full report
report_path = OUTPUT_FOLDER / "product_category_analysis.csv"

category_analysis.to_csv(report_path, index=False)

# Plot top 10 categories by revenue
top_categories = category_analysis.head(10).sort_values(
    "Total_Revenue"
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_categories["Category"],
    top_categories["Total_Revenue"]
)

plt.title("Top 10 Product Categories by Revenue")
plt.xlabel("Product Revenue (BRL)")
plt.ylabel("Product Category")
plt.tight_layout()

chart_path = CHART_FOLDER / "top_product_categories.png"

plt.savefig(chart_path, dpi=300)
plt.close()

print("\nAnalysis completed successfully!")
print(f"Report saved: {report_path}")
print(f"Chart saved: {chart_path}")