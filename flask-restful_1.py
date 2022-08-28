from flask import Flask, jsonify, url_for
from flask_restful import Api, Resource, reqparse
from settings import DevelopMentConfig

USERS = [
    {"name": "xiaoshulin"},
    {"name": "张三"},
    {"name": "李四"},
    {"name": "Alex"},
]

app = Flask(__name__)
app.config.from_object(DevelopMentConfig())
api = Api()
api.app = app
api.init_app(app)


class Users(Resource):
    def get(self):
        return jsonify(USERS)

    def post(self):
        args = reqparse.RequestParser().add_argument('name', type=str, location='json', required=True,
                                                     help='名字不能为空').parse_args()
        if args['name'] not in USERS:
            USERS.append({"name": args['name']})
        return jsonify(USERS)

    def delete(self):
        USERS = []
        return jsonify(USERS)


api.add_resource(Users, '/api/users', endpoint='user')
app.run()









