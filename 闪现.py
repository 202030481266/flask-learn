from flask import Flask, get_flashed_messages, flash

app = Flask(__name__)
app.secret_key = 'xiaoshulin'

@app.route('/y1', methods=['GET', ])
def y1():
    flash('月饼', category='y1')
    flash('蛋黄酥', category='y2')
    return "函数y1"


@app.route('/y2', methods=['GET', ])
def y2():
    data = get_flashed_messages(category_filter=['y1'])
    print(data)
    return "函数y2"


if __name__ == '__main__':
    app.run()