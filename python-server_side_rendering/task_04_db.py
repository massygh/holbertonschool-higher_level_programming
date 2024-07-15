from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to create the database if it doesn't exist
def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

# Function to fetch products from SQLite database
def fetch_products_from_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products_data = cursor.fetchall()
    conn.close()
    return products_data

@app.route('/products')
def products():
    source = request.args.get('source')

    if source == 'sql':
        try:
            products_data = fetch_products_from_sql()
            return render_template('product_display.html', products=products_data)
        except Exception as e:
            return render_template('product_display.html', error=str(e))

    return render_template('product_display.html', error='Wrong source')

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)
