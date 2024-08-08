from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# In-memory storage for inventory items
inventory = {}

# In-memory storage for sales history
sales_history = {}

# Add a new item to the inventory
@app.route('/inventory', methods=['POST'])
def add_item():
    item_data = request.get_json()
    item_id = item_data.get('id')
    if item_id in inventory:
        return jsonify({'message': 'Item already exists'}), 400
    inventory[item_id] = item_data
    sales_history[item_id] = []
    return jsonify({'message': 'Item added successfully'}), 201

# Get an item from the inventory
@app.route('/inventory/<item_id>', methods=['GET'])
def get_item(item_id):
    item = inventory.get(item_id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify(item), 200

# Update an existing item in the inventory
@app.route('/inventory/<item_id>', methods=['PUT'])
def update_item(item_id):
    item_data = request.get_json()
    if item_id not in inventory:
        return jsonify({'message': 'Item not found'}), 404
    inventory[item_id].update(item_data)
    return jsonify({'message': 'Item updated successfully'}), 200

# Delete an item from the inventory
@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in inventory:
        return jsonify({'message': 'Item not found'}), 404
    del inventory[item_id]
    del sales_history[item_id]
    return jsonify({'message': 'Item deleted successfully'}), 200

# Record a sale
@app.route('/inventory/<item_id>/sale', methods=['POST'])
def record_sale(item_id):
    sale_data = request.get_json()
    quantity_sold = sale_data.get('quantity')
    sale_date = sale_data.get('date', str(datetime.date.today()))
    if item_id not in inventory:
        return jsonify({'message': 'Item not found'}), 404
    sales_history[item_id].append({'quantity': quantity_sold, 'date': sale_date})
    inventory[item_id]['quantity'] -= quantity_sold
    return jsonify({'message': 'Sale recorded successfully'}), 201

# Forecast inventory levels
@app.route('/inventory/<item_id>/forecast', methods=['GET'])
def forecast_item(item_id):
    if item_id not in inventory:
        return jsonify({'message': 'Item not found'}), 404
    
    sales = sales_history.get(item_id, [])
    if not sales:
        return jsonify({'message': 'Not enough data to forecast'}), 400

    # Simple forecasting algorithm: average sales per day
    total_quantity_sold = sum(sale['quantity'] for sale in sales)
    num_days = (datetime.date.today() - datetime.datetime.strptime(sales[0]['date'], '%Y-%m-%d').date()).days + 1
    avg_sales_per_day = total_quantity_sold / num_days

    # Forecast for the next 7 days
    forecast = avg_sales_per_day * 7
    return jsonify({'forecast': forecast}), 200


if __name__ == '__main__':
    app.run(debug=True)