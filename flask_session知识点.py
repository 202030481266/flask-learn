from flask import Flask, session
from flask_session import RedisSessionInterface
from redis import Redis

app = Flask(__name__)
app.secret_key = 'xiaoshulin'

# from flask.sessions import SecurCookieSessionInterface
# app.session_interface = SecureCookieSessionInterface()


app.session_interface = RedisSessionInterface(
    redis=Redis(host='127.0.0.1',port=6379,key_prefix='flashxxx')
)
# 将数据存储到了服务器上的redis数据库里面了,不是存在客户端里面



# 另一种实现方式
# python3 对于扩展导入包的语法为 flask_extends 而不是 flask.ext.extends
from flask_session import Session
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='127.0.0.1', port='6379')
Session(app)
# if config['SESSION_TYPE'] == 'redis':
#     session_interface = RedisSessionInterface(
#         config['SESSION_REDIS'], config['SESSION_KEY_PREFIX'],
#         config['SESSION_USE_SIGNER'], config['SESSION_PERMANENT'])


@app.route('/index', methods=['GET', ])
def inde():
    return 'index'



if __name__ == '__main__':
    app.run()



