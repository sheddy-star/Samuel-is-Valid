from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def supermarket_checkout():

    receipt = None

    if request.method == "POST":

        # Customer information
        full_name = request.form["full_name"]
        age = int(request.form["age"])
        money = float(request.form["money"])
        membership_status = request.form["membership_status"].strip().lower()

        # Grocery lists
        item_names = []
        item_prices = []

        # Collect 4 items
        for i in range(1, 5):
            name = request.form[f"item_name_{i}"]
            price = float(request.form[f"item_price_{i}"])

            item_names.append(name)
            item_prices.append(price)

        # Add extra item
        extra_item_name = request.form["extra_item_name"]
        extra_item_price = float(request.form["extra_item_price"])

        item_names.append(extra_item_name)
        item_prices.append(extra_item_price)

        # Remove first item
        removed_item = item_names.pop(0)
        removed_price = item_prices.pop(0)

        # Calculations
        total_cost = sum(item_prices)
        average_price = total_cost / len(item_prices)
        highest_price = max(item_prices)
        lowest_price = min(item_prices)

        # Discount
        if total_cost >= 20000 or membership_status == "yes":
            discount_eligibility = "Qualifies for discount"
            total_cost *= 0.90
        else:
            discount_eligibility = "Does not qualify for discount"

        # Name manipulation
        name_uppercase = full_name.upper()
        name_lowercase = full_name.lower()
        first_name = full_name.split()[0] if full_name else ""
        name_char_count = len(full_name)

        # Remaining money
        remaining_money = money - total_cost

        # Receipt
        receipt = {
            "name_uppercase": name_uppercase,
            "name_lowercase": name_lowercase,
            "first_name": first_name,
            "name_char_count": name_char_count,
            "customer_id": "CUST-1001",
            "age": age,
            "items": list(zip(item_names, item_prices)),
            "removed_item": removed_item,
            "removed_price": removed_price,
            "total_cost": total_cost,
            "average_price": average_price,
            "highest_price": highest_price,
            "lowest_price": lowest_price,
            "discount": discount_eligibility,
            "remaining_money": remaining_money
        }

    return render_template("index.html", receipt=receipt)


if __name__ == "__main__":
    app.run(debug=True)
