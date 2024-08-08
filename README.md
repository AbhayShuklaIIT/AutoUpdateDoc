##Flask Inventory Server Documentation
#Introduction
This document provides an overview of the Flask-based Inventory Server, including its setup, usage, and API endpoints. The server allows you to add, update, delete, and retrieve inventory items.

##Prerequisites
Python 3.6 or higher
Flask library
Installation
Install Flask:
Open your terminal or command prompt and run the following command to install Flask:

##bash
pip install Flask
Download the Inventory Server Script:
Save the provided Flask app code into a file named inventory_server.py.

##Running the Server
To run the inventory server, execute the following command in your terminal:

bash
python inventory_server.py
The server will start running on http://127.0.0.1:5000.

##API Endpoints
1. Add a New Item
Endpoint: /inventory
Method: POST
Description: Adds a new item to the inventory.

Request Body:

json
Copy code
{
  "id": "item_id",
  "name": "item_name",
  "quantity": 10,
  "price": 25.50
}
Response:

Success:
json
Copy code
{
  "message": "Item added successfully"
}
Failure (if item already exists):
json
Copy code
{
  "message": "Item already exists"
}
2. Get an Item
Endpoint: /inventory/<item_id>
Method: GET
Description: Retrieves an item from the inventory by its ID.

Response:

Success:
json
Copy code
{
  "id": "item_id",
  "name": "item_name",
  "quantity": 10,
  "price": 25.50
}
Failure (if item not found):
json
Copy code
{
  "message": "Item not found"
}
3. Update an Item
Endpoint: /inventory/<item_id>
Method: PUT
Description: Updates the details of an existing item.

Request Body:

json
Copy code
{
  "name": "updated_name",
  "quantity": 20,
  "price": 30.00
}
Response:

Success:
json
Copy code
{
  "message": "Item updated successfully"
}
Failure (if item not found):
json
Copy code
{
  "message": "Item not found"
}
4. Delete an Item
Endpoint: /inventory/<item_id>
Method: DELETE
Description: Deletes an item from the inventory by its ID.

Response:

Success:
json
Copy code
{
  "message": "Item deleted successfully"
}
Failure (if item not found):
json
Copy code
{
  "message": "Item not found"
}
Error Handling
The server returns appropriate error messages and HTTP status codes for various error conditions, such as item not found or item already exists.

Conclusion
This documentation provides the necessary details to set up and use the Flask-based Inventory Server. You can expand the server's functionality by adding more endpoints and features as needed. If you encounter any issues or have questions, please refer to the Flask documentation or contact the support team.