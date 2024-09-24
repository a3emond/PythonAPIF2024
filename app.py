from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Get MongoDB connection string from environment variable
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)

# Select the database
db = client['PythonAPIF2024']
users_collection = db['Users']

@app.route('/')
def home():
    return "Welcome to the API!"

# Route to GET all users and POST new users
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = list(users_collection.find({}, {'_id': 0})) 
        return jsonify(users)
    elif request.method == 'POST':
        new_user = request.json
        users_collection.insert_one(new_user)
        return jsonify({"message": "User created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
