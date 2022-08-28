from flask import Flask, request, session, redirect, render_template

app = Flask(__name__)
app.secret_key = 'xiaoshulin'

@app.before_request
def check_login():
    if request.path == '/login':
        return None
    user = session.get('user_info')
    if not user:
        return redirect('/login')


@app.after_request
def oooo(response):
    print('执行完成后')
    return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    return "login"


@app.route('/index', methods=['GET', 'POST'])
def index():
    print('视图函数x2')
    return "x2"