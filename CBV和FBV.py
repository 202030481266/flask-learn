from flask import Flask, views

app = Flask(__name__)


def wrapper(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

# 两种视图使用的方式
# 两种CBV

class IndexView(views.View):
    methods = ['GET']
    decorators = [wrapper, ]

    def dispatch_request(self):
        print('index')
        return "Index is here."


app.add_url_rule('/index', view_func=IndexView.as_view(name='Index')) # name is endpoint

class IndexView(views.MethodView):
    methods = ['GET', 'POST']
    decorators = [wrapper, ]
    
    def get(self):
        pass
    
    def post(self):
        pass

app.add_url_rule('/index', view_func=IndexView.as_view(name='index'))












