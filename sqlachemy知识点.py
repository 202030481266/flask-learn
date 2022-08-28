from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]

Session = sessionmaker(bind=engine)
session = Session()  # 相当于cursor

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    extra = Column(String(32))


def init_db():
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/tt", max_overflow=5)
    Base.metadata.create_all(engine)  # 创建表


def close_db():
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/tt", max_overflow=5)
    Base.metadata.drop_all(engine)  # 删除表


def main():
    # 插入数据记录
    r1 = Users(name='Alex', extra='sb')
    r2 = Users(name='jack', extra='db')
    session.add(r1)
    session.add(r2)

    session.commit()


if __name__ == '__main__':
    init_db()
    main()
    close_db()















