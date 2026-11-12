import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Dataset" / "Cleaned"
OUTPUT_DIR = BASE_DIR / "Documentation"
CHART_DIR = OUTPUT_DIR / "Charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load review dataset
reviews = pd.read_csv(
    DATA_DIR / "olist_order_reviews_dataset.csv"
)

# Count each review score
review_summary = (
    reviews["review_score"]
    .value_counts()
    .reindex([1, 2, 3, 4, 5], fill_value=0)
    .sort_index()
    .rename_axis("Review_Score")
    .reset_index(name="Review_Count")
)

# Save report
review_summary.to_csv(
    OUTPUT_DIR / "review_score_distribution.csv",
    index=False
)

# Create chart
plt.figure(figsize=(9, 6))

plt.bar(
    review_summary["Review_Score"],
    review_summary["Review_Count"]
)

plt.title("Customer Review Score Distribution", fontsize=15)
plt.xlabel("Review Score (1 = Lowest, 5 = Highest)")
plt.ylabel("Number of Reviews")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()

# Save chart
plt.savefig(
    CHART_DIR / "review_score_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Review score analysis completed!")
print(review_summary)
print(f"\nChart saved at: {CHART_DIR}")