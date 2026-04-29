from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

transactions = []

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Budget Planner Pro</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #0d1117;
            color: white;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
        }

        .card {
            background: #161b22;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        input, select, button {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: none;
            border-radius: 5px;
        }

        input, select {
            background: #0d1117;
            color: white;
        }

        button {
            background: #238636;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #2ea043;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th, td {
            padding: 10px;
            border-bottom: 1px solid #30363d;
            text-align: center;
        }

        .income {
            color: #2ea043;
        }

        .expense {
            color: #f85149;
        }

        .balance {
            font-size: 20px;
            text-align: right;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>📊 Budget Planner Pro</h1>

    <div class="card">
        <form method="POST">
            <select name="type" required>
                <option value="">Select Type</option>
                <option value="Income">Income</option>
                <option value="Expense">Expense</option>
            </select>

            <select name="category" required>
                <option value="">Select Category</option>
                <option>Salary</option>
                <option>Business</option>
                <option>Food</option>
                <option>Transport</option>
                <option>Shopping</option>
                <option>Bills</option>
            </select>

            <input type="number" name="amount" placeholder="Amount" required>

            <button type="submit">Add Transaction</button>
        </form>
    </div>

    <div class="card">
        <h2>Transaction History</h2>
        <table>
            <tr>
                <th>Type</th>
                <th>Category</th>
                <th>Amount</th>
            </tr>
            {% for t in transactions %}
            <tr>
                <td class="{{ 'income' if t.type == 'Income' else 'expense' }}">
                    {{ t.type }}
                </td>
                <td>{{ t.category }}</td>
                <td>₹ {{ t.amount }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>

    <div class="balance">
        Balance: ₹ {{ balance }}
    </div>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        t_type = request.form["type"]
        category = request.form["category"]
        amount = float(request.form["amount"])

        transactions.append({
            "type": t_type,
            "category": category,
            "amount": amount
        })

        return redirect("/")

    balance = 0
    for t in transactions:
        if t["type"] == "Income":
            balance += t["amount"]
        else:
            balance -= t["amount"]

    return render_template_string(html, transactions=transactions, balance=balance)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)