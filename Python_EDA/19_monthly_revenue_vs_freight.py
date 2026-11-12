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
orders = pd.read_csv(
    DATA_DIR / "olist_orders_dataset.csv"
)

items = pd.read_csv(
    DATA_DIR / "olist_order_items_dataset.csv"
)

# Convert purchase timestamp
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

# Merge orders and order items
sales_data = items.merge(
    orders[["order_id", "order_purchase_timestamp"]],
    on="order_id",
    how="inner"
)

# Remove rows with missing purchase dates
sales_data = sales_data.dropna(
    subset=["order_purchase_timestamp"]
)

# Extract month
sales_data["Month"] = (
    sales_data["order_purchase_timestamp"]
    .dt.to_period("M")
    .astype(str)
)

# Calculate monthly revenue and freight
monthly_summary = (
    sales_data.groupby("Month")
    .agg(
        Product_Revenue=("price", "sum"),
        Freight_Charges=("freight_value", "sum"),
        Total_Items=("order_item_id", "count")
    )
    .reset_index()
)

# Save report
monthly_summary.to_csv(
    OUTPUT_DIR / "monthly_revenue_vs_freight.csv",
    index=False
)

# Create comparison chart
plt.figure(figsize=(14, 7))

plt.plot(
    monthly_summary["Month"],
    monthly_summary["Product_Revenue"],
    marker="o",
    label="Product Revenue"
)

plt.plot(
    monthly_summary["Month"],
    monthly_summary["Freight_Charges"],
    marker="s",
    label="Freight Charges"
)

plt.title("Monthly Product Revenue vs Freight Charges", fontsize=15)
plt.xlabel("Month")
plt.ylabel("Amount (BRL)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "monthly_revenue_vs_freight.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Monthly revenue vs freight analysis completed!")
print(monthly_summary)
print(f"\nChart saved at: {CHART_DIR}")