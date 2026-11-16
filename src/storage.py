import csv
import os
from datetime import datetime

FILE_PATH = os.path.join("data", "expenses.csv")
HEADERS = ["Date", "Category", "Amount", "Note"]

def initialize_storage():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

def add_expense(category: str, amount: float, note: str = ""):
    initialize_storage()
    date_str = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date_str, category.strip().title(), f"{amount:.2f}", note.strip()])

def load_expenses() -> list:
    initialize_storage()
    with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)
