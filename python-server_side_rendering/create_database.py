import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Vérifier si la table existe déjà
    cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Products';''')
    if cursor.fetchone()[0] == 1:
        print('La table Products existe déjà. Supprimez-la d\'abord pour la recréer.')
        return
    
    # Créer la table Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insérer des données d'exemple
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
