import sqlalchemy创建表的结构 as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/tt", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()  # 相当于cursor

# 单条增加
obj = sa.Classes(name="软件一班")
session.add(obj)
session.commit()

# 多条增加
# obj = [
#     sa.Classes(name='软件二班'),
#     sa.Classes(name='软件三班'),
#     sa.Classes(name='软件四班'),
# ]
# session.add_all(obj)
# session.commit()

# 查询
# result = session.query(sa.Classes).all()
# for res in result:
#     print(res.id, res.name)

# 删除 id > 2 的班级名字
# result = session.query(sa.Classes).filter(sa.Classes.id > 2).delete()
# session.commit()

# 修改
# session.query(Users).filter(Users.id > 0).update({"name": "999"})
# session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"},
#                                                  synchronize_session=False) 字符串相加
# session.query(Users).filter(Users.id > 0).update({"age": Users.age + 1},
#                                                  synchronize_session="evaluate") 表达式运算

# 返回的对象类型
# results = session.query(sa.Classes.id, sa.Classes.name).all()
# for result in results:
#     print(result, type(result), result.id, result.name)

# filter 和 filter_by
# result = session.query(sa.Classes).filter(sa.Classes.name=='软件1班').all()
# result = session.query(sa.Classes).filter_by(name=='软件2班').all()

# 条件查询
# result = session.query(sa.Student).filter(text("id<:value and name=:name")).params(value=2,
#                                                                                    name='alex').order_by(Student.id)
result = session.query(sa.Classes).from_statement(text(
    "SELECT * FROM WHERE name=:name"
)).params(name='alex')

print(result)

session.close()