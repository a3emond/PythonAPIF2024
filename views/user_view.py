from flask import Blueprint, jsonify, request
from database.__init__ import database
from models.user_model import User
import controllers.user_controller as user_controller

user = Blueprint("user", __name__)

@user.route('/v0/users', methods=['GET'])
def get_users():
    users = []
    for user in database["LS3FALL2024"]["Users"].find():
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users)

@user.route('/v0/users', methods=['POST'])
def add_user():

    user_data = request.json
    print(user_data)

    new_user = User(user_data['name'], user_data['email'], user_data['password'])
    # new_user = {
    #     "email": user_data['email'],
    #     "name": user_data['name'],
    #     "password": user_data['password']
    # }

    # new_user = {
    #     "email": "bob@hotmail.com",
    #     "name": "Bob Bob",
    #     "password": "123456"
    # }

    # result = database["LS3FALL2024"]["Users"].insert_one(new_user)
    # print(result.inserted_id)
    # print(new_user)
    # new_user['id'] = str(result.inserted_id)
    # del new_user['_id']

    created_user = user_controller.create_user(new_user)
    print(created_user)

    return jsonify({'id': str(created_user.inserted_id), 'is_succeded': created_user.acknowledged})