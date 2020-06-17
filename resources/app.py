from flask import Flask, request, jsonify
from flask_restful import Api
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)

app.config['MONGO_DBNAME'] = "REST_MONGO"
app.config['MONGO_URI'] = "mongodb+srv://teste:N5LY4U9MC1ht8RQ2@clusterrest-zfaxv.mongodb.net/REST_MONGO?retryWrites" \
                          "=true&w=majority "

mongo = PyMongo(app)


@app.route('/')
def main():
    return "<h1 style='color:black'>Rest API in Flask & MongoDB!</h1>"


@app.route('/users', methods=['GET'])
def get_all_users():
    users = mongo.db.Users

    output = []
    for queue in users.find():
        output.append({'name': queue['name'], 'job': queue['job'], 'age': queue['age'], 'city': queue['city']})
    return jsonify({'result': output})


@app.route('/users/<name>', methods=['GET'])
def get_one_user(name):
    users = mongo.db.Users

    queue = users.find_one({'name': name})
    if queue:
        output = ({'name': queue['name'], 'job': queue['job'], 'age': queue['age'], 'city': queue['city']})
    else:
        output = 'No Results Found'

    return jsonify({'result': output})


@app.route('/users', methods=['POST'])
def add_user():
    users = mongo.db.Users
    name = request.json['name']
    job = request.json['job']
    age = request.json['age']
    city = request.json['city']

    user_id = users.insert({'name': name, 'job': job, 'age': age, 'city': city})
    new_user = users.find_one({'_id': user_id})

    output = {'name': new_user['name'], 'job': new_user['job'], 'age': new_user['age'], 'city': new_user['city']}

    return jsonify({'result': output})


@app.route('/users/<name>', methods=['DELETE'])
def delete_user(name):
    users = mongo.db.Users
    queue = users.find_one({'name': name})
    if queue:
        users.delete_many(queue)
        output = 'User is Removed.'
        return jsonify({'result': output})
    else:
        output = 'User not Found.'
        return jsonify({'result': output})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
