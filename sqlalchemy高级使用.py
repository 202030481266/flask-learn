# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import or_, and_
# from sqlalchemy.sql import func
#
#
# # 聚合函数
# User.query.filter_by(role_id=3, username='susan').count()  # 数数
# User.query.with_entities(func.sum(User.id)).all()  # 求和1
# session.query(func.sum(User.id)).scalar()  # 求和2
# User.query.with_entities(func.avg(User.role_id)).all()  # 平均值
# session.query(func.max(Article.read_num).scalar()  # 最大值
# session.query(Article).order_by(Article.read_num.desc()).first()  # 最大值的记录
#
# # 模糊匹配
# Staff.query.filter(Staff.name.like("%a%")).all()
# # 不等于
# Staff.query.filter(Staff.id != 1).all()
# # 大于，小于
# Staff.query.filter(Staff.id>1,Staff.score>1).all()
# # 或
# Staff.query.filter(or_(Staff.id>1, Staff.score<4)).all()
# # 包含
# Staff.query.filter(Staff.name.contains("a")).all()
# # 区间
# Staff.query.filter(Staff.id.between(1,2)).all()
# # 与
# Staff.query.filter(and_(Staff.id>1, Staff.score>2)).all()
# # 字段筛选
# Staff.query.with_entities(Staff.name, Staff.id).all()
# # 去重
# Staff.query.with_entities(Staff.name).distinct().all()
