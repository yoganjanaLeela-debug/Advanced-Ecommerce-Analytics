import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Dataset" / "Cleaned"
OUTPUT_DIR = BASE_DIR / "Documentation"
CHART_DIR = OUTPUT_DIR / "Charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load datasets
items = pd.read_csv(DATA_DIR / "olist_order_items_dataset.csv")
products = pd.read_csv(DATA_DIR / "olist_products_dataset.csv")

# Calculate revenue for each product
product_revenue = (
    items.groupby("product_id", as_index=False)
    .agg(
        Total_Revenue=("price", "sum"),
        Units_Sold=("order_item_id", "count")
    )
)

# Merge product details
product_revenue = product_revenue.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left"
)

# Select top 10 products
top_products = product_revenue.nlargest(10, "Total_Revenue")
top_products = top_products.sort_values("Total_Revenue")

# Save report
top_products.to_csv(
    OUTPUT_DIR / "top_10_products_revenue.csv",
    index=False
)

# Create chart
plt.figure(figsize=(12, 7))

plt.barh(
    top_products["product_id"].astype(str),
    top_products["Total_Revenue"]
)

plt.title("Top 10 Products by Revenue", fontsize=16)
plt.xlabel("Total Revenue (BRL)")
plt.ylabel("Product ID")
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "top_10_products_revenue.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Top 10 products analysis completed!")
print(top_products)
print(f"\nChart saved at: {CHART_DIR}")