from flask import Flask, render_template
import json
import csv

app = Flask(__name__)

def json():
    with open("products.json", "r") as j:
        return json.load(j)

def csv():
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
        return {'error': 'nothing to load'}

    products = loaders[source]()

    if product_id:
        filtered_products = []
        target_id = int(product_id)

        for p in products:
            if int(p["id"]) == target_id:
                filtered_products.append(p)

        products = filtered_products

        if not products:
            return {'error': 'not product'}
