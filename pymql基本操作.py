import pymysql

# 连接Mysql
conn = pymysql.connect(
    host='127.0.0.1',
    user='自定义用户名(root)',
    password="自定义密码",
    database='数据库名称',
    port=3306,
    charset='utf8'
)

# 创建游标对象
cursor = conn.cursor()

# 编写SQL语句
sql = 'select * from info' # 表名请自行修改为自定义参数
# 纯字符串模式，单参数
cursor.execute(sql)


# 编写增加的sql语句
sql = "insert into info(name,age,gender) values (%s,%s,%s)"
# 使用数组进行赋值插入，即第二个参数使用数组形式
add_data = ['云无月', 4500, '女']
cursor.execute(sql, add_data)


# 编写修改的sql语句
sql = "update info set name=%s where name=%s"
# 第二个参数使用元组形式，实际上可以与上文数组写法完全一致（也可以直接自行拼接字符串）
add_data = ('王牛蛙', '王辟邪')
# 注意len返回的是修改的数目 也就是数据库修改时的数字返回值
len = cursor.execute(sql, add_data)


# 注意，如果要使用dict(JSON)作为sql语句补位，那么补位的位置写法为%(key命)s
# 如下补位为id:
sql = "delete from info where id =%(id)s"
add_data = {
    "name": "岑缨",
    "id" : 28
}
# 执行dict形式的补位
cursor.execute(sql, add_data)


# 关闭游标
cursor.close()
# 关闭连接
conn.close()


# 异常处理和回滚
# 连接Mysql
conn = pymysql.connect(
    host='127.0.0.1',
    user='自定义用户名(root)',
    password="自定义密码",
    database='数据库名称',
    port=3306,
    charset='utf8'
)
try:
    # 创建游标对象
    cursor = conn.cursor()
    # 编写增加/删除/修改的sql语句
	# 编写SQL语句,进行相关操作...
    # ...如：
    sql = "delete from info where id =%(id)s"
    add_data = {
        "name": "岑缨",
        "id" : 28
    }
    # 执行编写的SQL语句
    cursor.execute(sql, add_data)
    # 提交修改
    conn.commit()
    # 关闭，释放资源
    cursor.close()
    print("任务完成")

except Exception as e:
    # 回滚
    conn.rollback()
    print(e)

finally:
    conn.close()



# cursor.fetchone() 获取第一条匹配记录
# cursor.fetchall() 获取所有的匹配记录



