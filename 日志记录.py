def init_logger(app):
    # 创建logs目录，用于存放日志文件
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # 设置RotatingFileHandler类，最大日志文件大小为100kb，只保留10个备份文件，其会自动进行日志文件的切割和清理
    file_handler = RotatingFileHandler('logs/test.log', maxBytes=102400, backupCount=10)
    # logging.Formatter类为日志消息提供自定义格式
    # 分别记录了时间戳、日志记录级别、消息、日志来源的源代码文件和行号
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    # 设置日志类别：分别是DEBUG、INFO、WARNING、ERROR和CRITICAL
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    # 每次服务重新启动，都会登记一条日志
    app.logger.setLevel(logging.INFO)
    app.logger.info('Unischool Server Start!')