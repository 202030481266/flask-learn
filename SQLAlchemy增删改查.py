from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)

conn = engine.connect()

# 创建SQL语句，INSERT INTO "user" (id, name) VALUES (:id, :name)
conn.execute(user.insert(),{'id':7,'name':'seven'})
conn.close()

# sql = user.insert().values(id=123, name='wu')
# conn.execute(sql)
# conn.close()

# sql = user.delete().where(user.c.id > 1)

# sql = user.update().values(fullname=user.c.name)
# sql = user.update().where(user.c.name == 'jack').values(name='ed')

# sql = select([user, ])
# sql = select([user.c.id, ])
# sql = select([user.c.name, color.c.name]).where(user.c.id==color.c.id)
# sql = select([user.c.name]).order_by(user.c.name)
# sql = select([user]).group_by(user.c.name)

# result = conn.execute(sql)
# print result.fetchall()
# conn.close()