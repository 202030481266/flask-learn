from datetime import timedelta
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = None
    PRESERVE_CONTEXT_ON_EXCEPTION = None
    SECRET_KEY = None
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)
    USE_X_SENDFILE = False
    LOGGER_NAME = None
    LOGGER_HANDLER_POLICY = 'always'
    SERVER_NAME = None
    APPLICATION_ROOT = None
    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_REFRESH_EACH_REQUEST = True
    MAX_CONTENT_LENGTH = None
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(hours=12)
    TRAP_BAD_REQUEST_ERRORS = False
    TRAP_HTTP_EXCEPTIONS = False
    EXPLAIN_TEMPLATE_LOADING = False
    PREFERRED_URL_SCHEME = 'http'
    JSON_AS_ASCII = True
    JSON_SORT_KEYS = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    TEMPLATES_AUTO_RELOAD = None


class DevelopMentConfig(BaseConfig):
    SECRET_KEY = 'xiaoshulin'
    JSON_AS_ASCII = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/tttt'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = 20  # 设置并发池的大小
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False

    SCHEDULER_JOBSTORES = {
        # set the database url for jobs
        'default': SQLAlchemyJobStore(tablename='jobs',
                                      url=SQLALCHEMY_DATABASE_URI)
    }
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 20}}  # 默认使用ThreadPoolExecutor
    SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}  # 是否忽略服务器宕机时间段内的任务执行以及最大同时工作数量

'''
 {
        'DEBUG':                                get_debug_flag(default=False),  # 是否开启Debug模式
        'TESTING':                              False,                          # 是否开启测试模式
        'PROPAGATE_EXCEPTIONS':                 None,                          
        'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
        'SECRET_KEY':                           None,
        'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
        'USE_X_SENDFILE':                       False,
        'LOGGER_NAME':                          None,
        'LOGGER_HANDLER_POLICY':               'always',
        'SERVER_NAME':                          None,
        'APPLICATION_ROOT':                     None,
        'SESSION_COOKIE_NAME':                  'session',
        'SESSION_COOKIE_DOMAIN':                None,
        'SESSION_COOKIE_PATH':                  None,
        'SESSION_COOKIE_HTTPONLY':              True,
        'SESSION_COOKIE_SECURE':                False,
        'SESSION_REFRESH_EACH_REQUEST':         True,
        'MAX_CONTENT_LENGTH':                   None,
        'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
        'TRAP_BAD_REQUEST_ERRORS':              False,
        'TRAP_HTTP_EXCEPTIONS':                 False,
        'EXPLAIN_TEMPLATE_LOADING':             False,
        'PREFERRED_URL_SCHEME':                 'http',
        'JSON_AS_ASCII':                        True,
        'JSON_SORT_KEYS':                       True,
        'JSONIFY_PRETTYPRINT_REGULAR':          True,
        'JSONIFY_MIMETYPE':                     'application/json',
        'TEMPLATES_AUTO_RELOAD':                None,
    }
'''
