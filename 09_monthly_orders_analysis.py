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

# Load orders dataset
file_path = DATA_FOLDER / "olist_orders_dataset.csv"
df = pd.read_csv(file_path)

# Convert purchase timestamp to datetime
df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"],
    errors="coerce"
)

# Remove rows without a valid purchase date for this analysis
df = df.dropna(subset=["order_purchase_timestamp"])

# Extract month
df["Order_Month"] = (
    df["order_purchase_timestamp"].dt.to_period("M").astype(str)
)

# Count orders per month
monthly_orders = (
    df.groupby("Order_Month")["order_id"]
    .nunique()
    .reset_index(name="Total_Orders")
)

# Display results
print("=" * 60)
print("MONTHLY ORDERS ANALYSIS")
print("=" * 60)

print(monthly_orders.to_string(index=False))

# Save report
report_path = OUTPUT_FOLDER / "monthly_orders_analysis.csv"
monthly_orders.to_csv(report_path, index=False)

# Create chart
plt.figure(figsize=(14, 6))

plt.plot(
    monthly_orders["Order_Month"],
    monthly_orders["Total_Orders"],
    marker="o"
)

plt.title("Monthly E-Commerce Orders")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()

chart_path = CHART_FOLDER / "monthly_orders_trend.png"
plt.savefig(chart_path, dpi=300)
plt.close()

print("\nAnalysis completed successfully!")
print(f"Report saved: {report_path}")
print(f"Chart saved: {chart_path}")