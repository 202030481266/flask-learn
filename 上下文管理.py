from flask import Flask, request, session

# 这里的request和session其实都是LocalProxy对象

app = Flask(__name__)


@app.route('/')
def index():
    print(request) # request 是一个 LocalProxy对象，先从 localstack里面获取ctx，再从ctx里面获取request
    request.method # LocalProxy 获取request后，再从request从中提取出method
    session['k1'] = 123 # 调用了LocalProxy的__setitem__方法，先从localstack里面获取了ctx，再从里面获取session，在然后置值
    session['k1'] # LocalProxy的__getitem__方法，从ctx中的session，再去session中获取k1对应的值
    return 'xiaoshulin'



if __name__ == '__main__':
    app.run()



'''
app.__call__()
app.wsgi_app()
    - 1. ctx = request_context(environ) 把原生的请求（带\r\n）的字符串转换为 app框架的Request对象,并且实现了路由匹配
    - 2. push() 处理，放进stack里面
    - 3. finalize_request() save_session 和 after_request
    
上下文管理：wsgi
    - 第一阶段: 将ctx(session,request)放到local对象（一个全局变量）里面
    - 第二阶段: 导入视图函数。
    - 第三阶段: 请求处理完毕，获取session并保存到cookie中，将ctx删除。
'''
