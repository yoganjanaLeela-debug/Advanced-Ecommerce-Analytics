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

# Load order items and orders
items_path = DATA_FOLDER / "olist_order_items_dataset.csv"
orders_path = DATA_FOLDER / "olist_orders_dataset.csv"

items = pd.read_csv(items_path)
orders = pd.read_csv(orders_path)

# Convert purchase timestamp to datetime
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"],
    errors="coerce"
)

# Keep orders with valid purchase dates
orders = orders.dropna(subset=["order_purchase_timestamp"])

# Extract order month
orders["Order_Month"] = (
    orders["order_purchase_timestamp"].dt.to_period("M").astype(str)
)

# Join order dates with order item prices
sales = items.merge(
    orders[["order_id", "Order_Month"]],
    on="order_id",
    how="inner",
    validate="many_to_one"
)
# Note: September 2018 may be incomplete because
# only one order is present in the available data.
# Calculate monthly product sales revenue
monthly_revenue = (
    sales.groupby("Order_Month", as_index=False)
    .agg(
        Product_Revenue=("price", "sum"),
        Freight_Charges=("freight_value", "sum"),
        Items_Sold=("order_item_id", "count"),
        Unique_Orders=("order_id", "nunique")
    )
)
# Check monthly revenue values
print("\nMonthly Revenue Verification:")
print(
    monthly_revenue[
        ["Order_Month", "Product_Revenue", "Unique_Orders"]
    ].tail(6)
)

monthly_revenue["Product_Revenue"] = monthly_revenue["Product_Revenue"].round(2)
monthly_revenue["Freight_Charges"] = monthly_revenue["Freight_Charges"].round(2)

# Display results
print("=" * 65)
print("MONTHLY E-COMMERCE REVENUE ANALYSIS")
print("=" * 65)
print(monthly_revenue.to_string(index=False))

# Save report
report_path = OUTPUT_FOLDER / "monthly_revenue_analysis.csv"
monthly_revenue.to_csv(report_path, index=False)

# Create revenue trend chart
plt.figure(figsize=(14, 6))

plt.plot(
    monthly_revenue["Order_Month"],
    monthly_revenue["Product_Revenue"],
    marker="o"
)

plt.title("Monthly Product Revenue")
plt.xlabel("Month")
plt.ylabel("Product Revenue (BRL)")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()

chart_path = CHART_FOLDER / "monthly_revenue_trend.png"
plt.savefig(chart_path, dpi=300)
plt.close()

print("\nAnalysis completed successfully!")
print(f"Report saved: {report_path}")
print(f"Chart saved: {chart_path}")