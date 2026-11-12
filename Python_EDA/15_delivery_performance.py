import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Dataset" / "Cleaned"
OUTPUT_DIR = BASE_DIR / "Documentation"
CHART_DIR = OUTPUT_DIR / "Charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load orders dataset
orders = pd.read_csv(
    DATA_DIR / "olist_orders_dataset.csv"
)

# Convert date columns
orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"],
    errors="coerce"
)

orders["order_estimated_delivery_date"] = pd.to_datetime(
    orders["order_estimated_delivery_date"],
    errors="coerce"
)

# Keep orders with both actual and estimated delivery dates
delivery = orders.dropna(
    subset=[
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
).copy()

# Calculate delivery delay
delivery["Delay_Days"] = (
    delivery["order_delivered_customer_date"]
    - delivery["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

# Classify delivery performance
delivery["Delivery_Performance"] = delivery["Delay_Days"].apply(
    lambda days: "Late" if days > 0 else "On Time / Early"
)

# Summarize results
delivery_summary = (
    delivery["Delivery_Performance"]
    .value_counts()
    .reindex(["On Time / Early", "Late"], fill_value=0)
    .rename_axis("Delivery_Performance")
    .reset_index(name="Order_Count")
)

# Save report
delivery_summary.to_csv(
    OUTPUT_DIR / "delivery_performance_report.csv",
    index=False
)

# Save order-level delay details
delivery[
    [
        "order_id",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "Delay_Days",
        "Delivery_Performance"
    ]
].to_csv(
    OUTPUT_DIR / "delivery_delay_details.csv",
    index=False
)

# Create chart
plt.figure(figsize=(9, 6))

plt.bar(
    delivery_summary["Delivery_Performance"],
    delivery_summary["Order_Count"]
)

plt.title("Delivery Performance Analysis", fontsize=15)
plt.xlabel("Delivery Status")
plt.ylabel("Number of Orders")
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "delivery_performance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Delivery performance analysis completed!")
print(delivery_summary)
print(f"\nChart saved at: {CHART_DIR}")