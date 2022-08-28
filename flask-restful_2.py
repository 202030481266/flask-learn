from flask_restful import reqparse
# 请求参数解析器的使用

# {
#   "username": "kuari",
#   "info": "heihei"
# }

# 最简单的类型
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='名字不能为空', required=True)
parser.add_argument('password', type=str, help='密码不能为空', required=True)


# {
#   "username": "kuari",
#   "info": [
#     "handsome", "cheerful", "optimism"
#   ]
# }

# 列表参数（string）
parser.add_argument('info', type=str, action='append', required=True)

# {
#   "username": "kuari",
#   "friends": [
#     {
#       "username": "tom",
#       "age": 20
#     },
#     {
#       "username": "jerry",
#       "age": 20
#     }
#   ]
# }

# 列表参数（字典）
parser.add_argument('friends', type=dict, action='append', required=True)











