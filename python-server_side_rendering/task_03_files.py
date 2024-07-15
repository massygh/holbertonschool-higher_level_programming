from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

# Function to read data from SQLite database
def read_sqlite_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products_data = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products_data]

# Route to display products based on source (json, csv, sql) and optional id
@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')
    
    try:
        if source == 'json':
            products_data = read_json_file('products.json')
        elif source == 'csv':
            products_data = read_csv_file('products.csv')
        elif source == 'sql':
            products_data = read_sqlite_data()
    except FileNotFoundError:
        return render_template('product_display.html', error='Data file not found')
    except sqlite3.Error as e:
        return render_template('product_display.html', error='SQLite error: ' + str(e))
    
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

