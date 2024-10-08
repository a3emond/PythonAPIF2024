from flask import Blueprint, jsonify, request
from database.__init__ import database
from models.user_model import User
import controllers.user_controller as user_controller
import app_config as config

user = Blueprint("user", __name__)

@user.route('/v0/users', methods=['GET'])
def get_users():
    db = database.database
    collection = db[config.CONST_USER_COLLECTION]
    users = []
    for user in collection.find():
        user['_id'] = str(user['_id'])
        users.append(user)

    return jsonify(users)

@user.route('/v0/users', methods=['POST'])
def add_user():

    user_data = request.json
    print(user_data)

    new_user = User(user_data['name'], user_data['email'], user_data['password'])


    created_user = user_controller.create_user(new_user)
    print(created_user)

    return jsonify({'id': str(created_user.inserted_id), 'is_succeded': created_user.acknowledged})