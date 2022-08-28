from flask import Flask, render_template, redirect
from flask import session, request
from settings import DevelopMentConfig

app = Flask(__name__)
app.config.from_object(DevelopMentConfig)

USER_LIST = {
    '1': {'name': '微微子', 'age': 18},
    '2': {'name': '为为子', 'age': 28},
    '3': {'name': '伟伟子', 'age': 38},
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    # request.args get请求的url中的参数
    # request.form post请求的form表单数据
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'xiaoshulin' and password == '123456':
        # 用户的信息session默认放在浏览器上,所以要使用secret_key参数加密
        session['user_info'] = username
        return redirect('/index')
    else:
        message = '登录失败'
        kwargs = {"message" : message}
        return render_template('login.html', **kwargs)


@app.route('/index')
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    kwargs = {
        'user_list': USER_LIST
    }
    return render_template('index.html', **kwargs)


@app.route('/logout')
def logout():
    # 删除session对象的信息
    session.pop('user_info', None)
    return redirect('/login')


@app.route('/detail')
def detail():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    uid = request.args.get('uid')
    info = USER_LIST.get(uid)
    return render_template('detail.html', info=info)


if __name__ == '__main__':
    app.run(port=5000) # run_simple(host, port, app)
















