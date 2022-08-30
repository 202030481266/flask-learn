from flask import Flask, redirect, render_template, url_for, request
from flask_login import login_required, login_user, logout_user, LoginManager, UserMixin
from settings import DevelopMentConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevelopMentConfig())
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column('username', db.String(120))
    password = db.Column('password', db.String(120))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/index/<string:username>')
@login_required
def index(username):
    return 'Welcome'


@app.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'xiaoshulin' and password == '123456':
            user = User.query.filter_by(username=username).first()
            login_user(user)
            return redirect(url_for('index', username=username))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


if __name__ == "__main__":
    # db.create_all()
    app.run()



