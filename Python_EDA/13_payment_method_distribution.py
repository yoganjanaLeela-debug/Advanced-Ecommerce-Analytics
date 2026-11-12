import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Dataset" / "Cleaned"
OUTPUT_DIR = BASE_DIR / "Documentation"
CHART_DIR = OUTPUT_DIR / "Charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load payment dataset
payments = pd.read_csv(
    DATA_DIR / "olist_order_payments_dataset.csv"
)

# Analyze payment methods
payment_summary = (
    payments.groupby("payment_type")
    .agg(
        Payment_Count=("payment_type", "count"),
        Total_Amount=("payment_value", "sum")
    )
    .reset_index()
    .sort_values("Payment_Count", ascending=False)
)

# Save report
payment_summary.to_csv(
    OUTPUT_DIR / "payment_method_distribution.csv",
    index=False
)

# Create chart
plt.figure(figsize=(10, 6))

plt.bar(
    payment_summary["payment_type"],
    payment_summary["Payment_Count"]
)

plt.title("Payment Method Distribution", fontsize=16)
plt.xlabel("Payment Method")
plt.ylabel("Number of Payment Records")
plt.xticks(rotation=30)
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "payment_method_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Payment method analysis completed!")
print(payment_summary)
print(f"\nChart saved at: {CHART_DIR}")