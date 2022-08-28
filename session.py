from flask import Flask, session

app = Flask(__name__)
app.secret_key('xiaoshulin')

'''
接口处理请求的细节过程
app.__call__ -> wsgi_app() -> request_context() return RequestContext() 返回了一个RequestContex类
    RequestContext()
        - self.request = Request() 请求数据的封装
        - self.session = None
        - push(): ctx调用的方法 -> app.open_session() -> SecureCookieSessionInterface.open_session() 
            return SecureCookieSession(dict)

1、请求刚刚到达
    ctx = RequestContext(...)
        - request
        - session = None
    ctx.push()
        ctx.session = SecureCookieSessionInterface.open_session()
2、视图函数
3、请求结束
    SecureCookieSessionInterface.save_session()
'''


@app.route('/x1', methods=['GET', 'POST'])
def index():
    session['k1'] = 123
    return "Index"


@app.route('/x2', methods=['GET', 'POST'])
def order():
    print(session['k1'])
    return "Order"