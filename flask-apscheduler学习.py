from flask import Flask, jsonify, current_app
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
from settings import DevelopMentConfig
from random import choice
from datetime import datetime
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore as BaseSQLAlchemyJobStore
from apscheduler.jobstores.base import BaseJobStore, JobLookupError, ConflictingIdError
from apscheduler.util import maybe_ref, datetime_to_utc_timestamp, utc_timestamp_to_datetime
from apscheduler.job import Job


try:
    import cPickle as pickle
except ImportError:  # pragma: nocover
    import pickle

try:
    from sqlalchemy import (
        create_engine, Table, Column, MetaData, Unicode, Float, LargeBinary, select, and_)
    from sqlalchemy.exc import IntegrityError
    from sqlalchemy.sql.expression import null
except ImportError:  # pragma: nocover
    raise ImportError('SQLAlchemyJobStore requires SQLAlchemy installed')


# 重写jobstore
class SQLAlchemyJobStore(BaseSQLAlchemyJobStore):

    def __init__(self, url=None, engine=None, tablename='apscheduler_jobs', metadata=None,
                 pickle_protocol=pickle.HIGHEST_PROTOCOL, tableschema=None, engine_options=None):
        super(BaseSQLAlchemyJobStore, self).__init__()
        self.pickle_protocol = pickle_protocol
        metadata = maybe_ref(metadata) or MetaData()

        if engine:
            self.engine = maybe_ref(engine)
        elif url:
            self.engine = create_engine(url, **(engine_options or {}))
        else:
            raise ValueError('Need either "engine" or "url" defined')

        # 191 = max key length in MySQL for InnoDB/utf8mb4 tables,
        # 25 = precision that translates to an 8-byte float
        # set the primary key to as job_id
        self.jobs_t = Table(
            tablename, metadata,
            Column('id', Unicode(191, _warn_on_bytestring=False)),
            Column('next_run_time', Float(25), index=True),
            Column('job_state', LargeBinary, nullable=False),
            schema=tableschema
        )  #


app = Flask(__name__)
app.config.from_object(DevelopMentConfig())
db = SQLAlchemy(app)


class Config:
    SCHEDULER_JOBSTORES = {
        # set the database url for jobs
        # 使用同一个数据库，指定metadata
        'default': SQLAlchemyJobStore(tablename='jobs',
                                      metadata=db.metadata,
                                      url='mysql+pymysql://root:123456@localhost:3306/tttt')
    }
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 20}}  # 默认使用ThreadPoolExecutor
    SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}  # 是否忽略服务器宕机时间段内的任务执行以及最大同时工作数量


app.config['SCHEDULER_JOBSTORES'] = Config.SCHEDULER_JOBSTORES
app.config['SCHEDULER_API_ENABLED'] = Config.SCHEDULER_API_ENABLED
app.config['SCHEDULER_JOB_DEFAULTS'] = Config.SCHEDULER_JOB_DEFAULTS


class Card(db.Model):

    __tablename__ = 'cards'
    id = db.Column('card_id', db.Integer, primary_key=True, autoincrement=True)
    content = db.Column('content', db.String(120))


class Job(db.Model):

    __tablename__ = 'jobs'
    __table_args__ = {'extend_existing': True}  # refine the table
    job_id = db.Column('card_id', db.Integer, primary_key=True, autoincrement=True)

    def get_job_id(self):
        return self.job_id


def my_work(job_id, card_id):
    print('Task {} and the card id is {}'.format(job_id, card_id))
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

    job_id = 'monitor' + str(new_card.id)

    # 创建job
    args = {
        'id': job_id,
        'name': 'job of %s' % new_card.id,
        'func': __name__ + ':' + 'my_work',
        'trigger': 'interval',
        'args': (job_id, new_card.id),
        'seconds': 5
    }
    scheduler.add_job(**args)
    return '成功添加'


@app.route('/jobs')
def get_jobs():
    # jobs = db.metadata.tables.get('jobs')
    # job_data = db.session.query(jobs).all()
    # print(job_data)
    job_objects = db.session.query(Job).all()
    for obj in job_objects:
        print(obj.get_job_id())
    return 'success'


scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


if __name__ == '__main__':
    app.run()

# db.create_all()





