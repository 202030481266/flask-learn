from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    class_id = Column(Integer, ForeignKey('classes.id'))


class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, autoincrement=True, primary_key=True)
    caption = Column(String(50))


class StudentToHobby(Base):
    __tablename__ = 'student2hobby'
    id = Column(Integer, autoincrement=True, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    hobby_id = Column(Integer, ForeignKey('hobby.id'))
    __table_args__ = (
        UniqueConstraint('student_id', 'hobby_id', name='uix_sid_hid'),
    )


def init_db():
    engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/tt", max_overflow=5)
    Base.metadata.create_all(engine)  # 创建表


if __name__ == '__main__':
    init_db()











