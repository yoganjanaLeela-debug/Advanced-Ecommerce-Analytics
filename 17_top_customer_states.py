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

customers = pd.read_csv(
    DATA_DIR / "olist_customers_dataset.csv"
)

# Select orders with valid customer IDs
orders = orders.dropna(subset=["customer_id"])

# Merge orders with customer details
order_customers = orders.merge(
    customers[["customer_id", "customer_state"]],
    on="customer_id",
    how="left"
)

# Count unique orders by customer state
state_summary = (
    order_customers.groupby("customer_state")["order_id"]
    .nunique()
    .reset_index(name="Order_Count")
    .sort_values("Order_Count", ascending=False)
)

# Select top 10 states
top_states = state_summary.head(10)

# Save report
top_states.to_csv(
    OUTPUT_DIR / "top_customer_states.csv",
    index=False
)

# Create horizontal bar chart
plt.figure(figsize=(10, 7))

plt.barh(
    top_states["customer_state"],
    top_states["Order_Count"]
)

plt.title("Top 10 Customer States by Orders", fontsize=15)
plt.xlabel("Number of Orders")
plt.ylabel("Customer State")
plt.gca().invert_yaxis()
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "top_customer_states.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Customer state analysis completed!")
print(top_states)
print(f"\nChart saved at: {CHART_DIR}")