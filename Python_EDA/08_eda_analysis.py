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

print("=" * 50)
print("ORDER STATUS ANALYSIS")
print("=" * 50)

# Count orders by status
status_counts = df["order_status"].value_counts().reset_index()
status_counts.columns = ["Order_Status", "Order_Count"]

# Display results
print("\nOrders by Status:")
print(status_counts.to_string(index=False))

# Calculate percentages
status_counts["Percentage"] = (
    status_counts["Order_Count"] / len(df) * 100
).round(2)

print("\nOrder Status Percentages:")
print(status_counts.to_string(index=False))

# Save report
report_path = OUTPUT_FOLDER / "order_status_analysis.csv"
status_counts.to_csv(report_path, index=False)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(
    status_counts["Order_Status"],
    status_counts["Order_Count"]
)

plt.title("E-Commerce Orders by Status")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()

chart_path = CHART_FOLDER / "order_status_chart.png"
plt.savefig(chart_path, dpi=300)
plt.close()

print("\nAnalysis completed successfully!")
print(f"Report saved: {report_path}")
print(f"Chart saved: {chart_path}")