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

# Calculate total product value for each order
order_revenue = (
    items.groupby("order_id", as_index=False)
    .agg(Order_Value=("price", "sum"))
)

# Merge purchase dates and order values
order_data = orders[
    ["order_id", "order_purchase_timestamp"]
].merge(
    order_revenue,
    on="order_id",
    how="inner"
)

# Remove rows with missing dates
order_data = order_data.dropna(
    subset=["order_purchase_timestamp"]
)

# Extract month
order_data["Month"] = (
    order_data["order_purchase_timestamp"]
    .dt.to_period("M")
    .astype(str)
)

# Calculate monthly AOV
monthly_aov = (
    order_data.groupby("Month")
    .agg(
        Total_Product_Revenue=("Order_Value", "sum"),
        Total_Orders=("order_id", "nunique")
    )
    .reset_index()
)

monthly_aov["Average_Order_Value"] = (
    monthly_aov["Total_Product_Revenue"]
    / monthly_aov["Total_Orders"]
)

# Save report
monthly_aov.to_csv(
    OUTPUT_DIR / "monthly_average_order_value.csv",
    index=False
)

# Create line chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_aov["Month"],
    monthly_aov["Average_Order_Value"],
    marker="o"
)

plt.title("Monthly Average Order Value (AOV)", fontsize=15)
plt.xlabel("Month")
plt.ylabel("Average Product Value per Order (BRL)")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "monthly_average_order_value.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Monthly AOV analysis completed!")
print(monthly_aov)
print(f"\nChart saved at: {CHART_DIR}")