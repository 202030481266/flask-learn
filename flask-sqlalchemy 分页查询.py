# 从get方法中取得页码
page = request.args.get('page', 1, type=int)
# 获取pagination对象
pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=10, error_out=False)

# pagination对象的items方法返回当前页的内容列表
posts = pagination.items


# pagination对象常用属性
# has_next :是否还有下一页
# has_prev :是否还有上一页
# items : 返回当前页的所有内容
# next(error_out=False) : 返回下一页的Pagination对象
# prev(error_out=False) : 返回上一页的Pagination对象
# page : 当前页的页码(从1开始)
# pages : 总页数
# per_page : 每页显示的数量
# prev_num : 上一页页码数
# next_num :下一页页码数
# query :返回 创建这个Pagination对象的查询对象
# total :查询返回的记录总数
# iter_pages(left_edge=2, left_current=2, right_current=5, right_edge=2)

# 增加自定义的属性
coursing_gross = paginate.query.all()
coursing_all = 0

for coursing in coursing_gross:
    if coursing.coursing_count > 0:
        coursing_all += coursing.coast_total

paginate.coursing_all = '{:.2f}'.format(coursing_all)

