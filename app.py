from flask import Flask, jsonify

from biz import userBiz
from common import dbClient

app = Flask(__name__)


@app.route('/')
def index():
    data = dbClient.get_company()
    return jsonify({'data': data})


@app.route('/company', methods=['POST'])
def add():
    company = dbClient.get_company()
    return jsonify({'company': company})


@app.route('/user', methods=['POST'])
def user_register():
    user = {"user_name": "leoliu"}
    userBiz.add_user(user)
    return jsonify({'success': True})


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = userBiz.get_user_by_id(user_id);
    return jsonify({'user': user})


if __name__ == '__main__':
    app.run(debug=True, port=8080)
