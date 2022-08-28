from time import sleep
import json
import re
import logging
import pymysql
from DBUtils.PooledDB import PooledDB

# 设置日志格式
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")



# DBUtils.PooledDB.PooledDB(self, creator,
#     mincached=0, maxcached=0, maxshared=0, maxconnections=0, blocking=False, maxusage=None,
#     setsession=None, failures=None, *args, **kwargs)
# Docstring:
#     Set up the DB-API 2 connection pool.
#     creator: either an arbitrary function returning new DB-API 2
#         connection objects or a DB-API 2 compliant database module
#     mincached: initial number of idle connections in the pool
#         (0 means no connections are made at startup)
#     maxcached: maximum number of idle connections in the pool
#         (0 or None means unlimited pool size)
#     maxshared: maximum number of shared connections
#         (0 or None means all connections are dedicated)
#         When this maximum number is reached, connections are
#         shared if they have been requested as shareable.
#     maxconnections: maximum number of connections generally allowed
#         (0 or None means an arbitrary number of connections)
#     blocking: determines behavior when exceeding the maximum
#         (if this is set to true, block and wait until the number of
#         connections decreases, otherwise an error will be reported)
#     maxusage: maximum number of reuses of a single connection
#         (0 or None means unlimited reuse)
#         When this maximum usage number of the connection is reached,
#         the connection is automatically reset (closed and reopened).
#     setsession: optional list of SQL commands that may serve to prepare
#         the session, e.g. ["set datestyle to ...", "set time zone ..."]
#     failures: an optional exception class or a tuple of exception classes
#         for which the connection failover mechanism shall be applied,
#         if the default (OperationalError, InternalError) is not adequate
#     args, kwargs: the parameters that shall be passed to the creator
#         function or the connection constructor of the DB-API 2 module

Pool = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=2,
    maxcached=5,
    blocking=True,
    maxusage=None, # 无限次数
    setsession=[],
    ping=0,
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    database='tt',
    charset='utf8'
)

def main():
    connection = Pool.connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor) # 字典格式
    cursor.execute('select * from tt.users')
    result = cursor.fetchall()
    print(result)
    cursor.close()



if __name__ == "__main__":
    main()
