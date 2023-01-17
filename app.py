from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
# disable the modification tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    """Item model for the database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)

    def __init__(self, name, description=None):
        """initialize the item with name and description"""
        self.name = name
        self.description = description

# create the table in the database
with app.app_context():
    db.create_all()

@app.route('/items', methods=['GET'])
def get_items():
    """Retrieve all items from the database"""
    items = Item.query.all()
    return jsonify([i.to_dict() for i in items])

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Retrieve a specific item by its id from the database"""
    item = Item.query.get(item_id)
    if item:
        return jsonify(item.to_dict())
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def create_item():
    """Create a new item in the database"""
    data = request.get_json()
    item = Item(name=data['name'], description=data.get('description'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item in the database"""
    item = Item.query.get(item_id)
    if item:
        data = request.get_json()
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        db.session.commit()
        return jsonify(item.to_dict())
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an existing item from the database"""
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted'})
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run()
