from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML template inside Python
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Budget Planner</title>
</head>
<body>
    <h1>Budget Planner</h1>

    <form method="POST">
        Income: <input type="number" name="income" required><br><br>
        Expenses: <input type="number" name="expenses" required><br><br>
        <input type="submit" value="Calculate">
    </form>

    {% if result is not none %}
        <h2>Remaining Balance: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        income = float(request.form["income"])
        expenses = float(request.form["expenses"])
        result = income - expenses

    return render_template_string(html, result=result)


# THIS PART FIXES YOUR ERROR
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)