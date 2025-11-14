from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json():
    with open("products.json", "r") as j:
        return json.load(j)

def load_csv():
    data = []
    with open("products.csv", "r") as c:
        csv = csv.DictReader(c)
        for row in csv:
            data.append(row)
    return data

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    loaders = {
        "json": load_json,
        "csv": load_csv
    }

    if source not in loaders:
        return render_template("product_display.html",
                               products=None,
                               error="Wrong source")

    products = loaders[source]()

    if product_id:
        filtered = []
        pid = int(product_id)

        for p in products:
            if int(p["id"]) == pid:
                filtered.append(p)

        if not filtered:
            return render_template("product_display.html",
                                   products=None,
                                   error="Product not found")

        products = filtered

    return render_template("product_display.html",
                           products=products,
                           error=None)
