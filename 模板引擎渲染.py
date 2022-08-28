from flask import render_template, Flask, Markup, redirect
app = Flask(__name__)

app.template_global()
def printf(value):
    return str(value)

def get_input(value):
    return "<input value='%s' />" % value

def gen_input(value):
    return Markup("<input value='%s' />" % value)


@app.route('/new', methods=['GET', ])
def new():
    content = {
        'c1': "xiaoshulin",
        'c2': [1, 2, 3],
        'c3': {'name':'xiaoshulin', 'age':'18'},
        'c4': lambda x: x ** 2,
        'c5': get_input,
        'c6': gen_input
    }
    return render_template('new.html', **content)


@app.route('/old', methods=['GET'])
def old():
    return redirect('/new')


if __name__ == '__main__':
    app.run()











