from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        print("POST REQUEST RECIEVED")

        name = request.form["name"]
        amount = request.form["amount"]

        print("DATA: ", name, amount)

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("EXPENSES LIST", expenses)

    return render_template(
        "index.html",
        expenses=expenses
    )


if __name__ == "__main__":
    app.run(debug=True)