# pip install Flask pymongo

from bson import ObjectId
from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient

app = Flask(__name__)

# Mongo connection
client = MongoClient("mongodb://localhost:27017/")
db = client.finance_DB
users = db.users  # collection name

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Finance Users API (Flask + MongoDB)"})


# GET all users (paginated)
# example: http://127.0.0.1:5001/api/users?pn=1&ps=10
@app.route("/api/users", methods=["GET"])
def get_users():
    data_to_return = []

    page_num = request.args.get("pn", default=1, type=int)
    page_size = request.args.get("ps", default=10, type=int)

    if page_num < 1: page_num = 1
    if page_size < 1: page_size = 10

    page_start = (page_num - 1) * page_size

    try:
        cursor = users.find().skip(page_start).limit(page_size)

        for user in cursor:
            user["_id"] = str(user["_id"])
            data_to_return.append(user)

        return make_response(jsonify(data_to_return), 200)

    except Exception as ex:
        return make_response(jsonify({"Error": "Internal Server Error", "details": str(ex)}), 500)


# GET one user by Mongo _id
# example: http://127.0.0.1:5001/api/users/65f0...abcd
@app.route("/api/users/<string:user_id>", methods=["GET"])
def get_one_user(user_id):
    try:
        doc = users.find_one({"_id": ObjectId(user_id)})
        if not doc:
            return make_response(jsonify({"Error": "User not found"}), 404)

        doc["_id"] = str(doc["_id"])
        return make_response(jsonify(doc), 200)

    except Exception as ex:
        return make_response(jsonify({"Error": "Invalid ID", "details": str(ex)}), 400)


if __name__ == "__main__":
    app.run(debug=True, port=5001)