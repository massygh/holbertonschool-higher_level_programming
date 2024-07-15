from flask import Flask, render_template
import json

app = Flask(__name__)

# Route to render items.html with items from items.json
@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
        items_list = data['items']
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
