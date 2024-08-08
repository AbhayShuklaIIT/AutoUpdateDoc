from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for inventory items
inventory = {}

# Add a new item to the inventory
@app.route('/inventory', methods=['POST'])
def add_item():
    item_data = request.get_json()
    item_id = item_data.get('id')
    if item_id in inventory:
        return jsonify({'message': 'Item already exists'}), 400
    inventory[item_id] = item_data
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
    if item_id not in inventory:
        return jsonify({'message': 'Item not found'}), 404
    item_data = request.get_json()
    inventory[item_id].update(item_data)
    return jsonify({'message': 'Item updated successfully'}), 200

# Delete an item from the inventory
@app.route('/inventory/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in inventory:
        return jsonify({'message': 'Item not found'}), 404
    del inventory[item_id]
    return jsonify({'message': 'Item deleted successfully'}), 200

# List all items in the inventory
@app.route('/inventory', methods=['GET'])
def list_items():
    return jsonify(list(inventory.values())), 200

if __name__ == '__main__':
    app.run(debug=True)