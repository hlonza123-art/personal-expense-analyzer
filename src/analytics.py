import os
import pandas as pd
import matplotlib.pyplot as plt
from src.storage import FILE_PATH, initialize_storage

def generate_summary():
    initialize_storage()
    df = pd.read_csv(FILE_PATH)
    
    if df.empty:
        print("\nNo expenses recorded yet. Add some entries first.")
        return

    category_totals = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    total_spent = df["Amount"].sum()

    print("\n--- Spending Summary ---")
    for category, amount in category_totals.items():
        print(f"{category:<15} : R{amount:,.2f}")
    print("-" * 28)
    print(f"{'Total Spent':<15} : R{total_spent:,.2f}\n")

    # Export visual chart
    os.makedirs("outputs", exist_ok=True)
    chart_path = os.path.join("outputs", "summary_chart.png")
    
    plt.figure(figsize=(8, 5))
    category_totals.plot(kind="bar", color="#2b5c8f")
    plt.title("Total Spending by Category")
    plt.ylabel("Amount (ZAR)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    
    print(f"Chart saved to {chart_path}")
