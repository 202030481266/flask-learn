from flask import Flask

app = Flask(__name__)

class MiddleWare(object):
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, *args, **kwargs):
        # 请求前的操作
        obj = self.old_wsgi_app(*args, **kwargs)
        # 请求后的操作
        return obj


if __name__ == '__main__':
    app.wsgi_app = MiddleWare(app.wsgi_app)
    app.run()