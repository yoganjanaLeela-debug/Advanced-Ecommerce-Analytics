import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Dataset" / "Cleaned"
OUTPUT_DIR = BASE_DIR / "Documentation"
CHART_DIR = OUTPUT_DIR / "Charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load order items dataset
items = pd.read_csv(
    DATA_DIR / "olist_order_items_dataset.csv"
)

# Calculate total freight cost for each order
order_freight = (
    items.groupby("order_id", as_index=False)
    .agg(Total_Freight=("freight_value", "sum"))
)

# Create freight cost categories
bins = [0, 10, 20, 30, 50, float("inf")]
labels = [
    "0-10 BRL",
    "10-20 BRL",
    "20-30 BRL",
    "30-50 BRL",
    "Above 50 BRL"
]

order_freight["Freight_Category"] = pd.cut(
    order_freight["Total_Freight"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Summarize freight cost categories
freight_summary = (
    order_freight["Freight_Category"]
    .value_counts(sort=False)
    .rename_axis("Freight_Category")
    .reset_index(name="Order_Count")
)

# Save report
freight_summary.to_csv(
    OUTPUT_DIR / "freight_cost_distribution.csv",
    index=False
)

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(
    freight_summary["Freight_Category"].astype(str),
    freight_summary["Order_Count"]
)

plt.title("Freight Cost Distribution per Order", fontsize=15)
plt.xlabel("Total Freight Cost per Order (BRL)")
plt.ylabel("Number of Orders")
plt.xticks(rotation=20)
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "freight_cost_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Freight cost analysis completed!")
print(freight_summary)
print(f"\nChart saved at: {CHART_DIR}")