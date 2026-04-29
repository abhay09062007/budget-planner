from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "budget_data.json"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"transactions": []}

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Home route
@app.route("/")
def home():
    data = load_data()
    txs = data["transactions"]

    income = sum(t["amount"] for t in txs if t["type"] == "income")
    expense = sum(t["amount"] for t in txs if t["type"] == "expense")
    balance = income - expense

    return render_template("index.html", txs=txs, income=income, expense=expense, balance=balance)

# Add transaction
@app.route("/add", methods=["POST"])
def add():
    data = load_data()

    t_type = request.form.get("type")
    category = request.form.get("category")
    amount = request.form.get("amount")

    try:
        amount = float(amount)
    except:
        return redirect("/")

    if not category or amount <= 0:
        return redirect("/")

    data["transactions"].insert(0, {
        "type": t_type,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%d %b %Y")
    })

    save_data(data)
    return redirect("/")

# Run app (IMPORTANT CHANGE FOR QR)
if __name__ == "__main__":