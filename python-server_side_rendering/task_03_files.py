from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to read JSON data
def read_json_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

# Function to read CSV data
def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# Route to display products based on source (json or csv) and optional id
@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')
    
    try:
        if source == 'json':
            products_data = read_json_file('products.json')
        elif source == 'csv':
            products_data = read_csv_file('products.csv')
    except FileNotFoundError:
        return render_template('product_display.html', error='Data file not found')
    
    if id:
        filtered_products = [product for product in products_data if str(product['id']) == id]
        if not filtered_products:
            return render_template('product_display.html', error='Product not found')
        else:
            return render_template('product_display.html', products=filtered_products)
    else:
        return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
