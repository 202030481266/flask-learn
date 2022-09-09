from flask import Flask
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from settings import DevelopMentConfig
from random import choice
from datetime import datetime


app = Flask(__name__)
app.config.from_object(DevelopMentConfig())
scheduler = APScheduler()
db = SQLAlchemy(app)


class Card(db.Model):

    __tablename__ = 'cards'
    id = db.Column('card_id', db.Integer, primary_key=True, autoincrement=True)
    content = db.Column('content', db.String(120))


def my_work(id):
    print('Task %s' % id)
    print('Now time is %s' % datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


@app.route('/add')
def add_card():
    string_data = [
        '吴为子',
        '陈德子',
        '叶嘉兵',
        '王子桶'
    ]
    content = choice(string_data)
    new_card = Card(content=content)
    db.session.add(new_card)
    db.session.commit()

    # 创建job
    args = {
        'id': str(new_card.id),
        'name': 'job of %s' % new_card.id,
        'func': __name__ + ':' + 'my_work',
        'trigger': 'interval',
        'args': (new_card.id,),
        'seconds': 5
    }
    scheduler.add_job(**args)
    return '成功添加'


scheduler.init_app(app)
scheduler.start()


if __name__ == '__main__':
    app.run()





