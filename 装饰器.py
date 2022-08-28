import functools
from flask import Flask

app = Flask(__name__)


def wrapper(func):
    @functools.wraps(func) # prevent the function name all are the same as inner
    def inner(*args, **kwargs):
        print("A decorator is generated.")
        return func(*args, **kwargs)
    return inner

# put the wrapper after the app.route
@app.route('/index')
@wrapper
def index():
    return "xiaoshulin"


if __name__ == '__main__':
    app.run()









