from redis import StrictRedis



class Config():
    """项目配置"""
    DEBUG = True

    """base64.b64encode(os.urandom(48))随机生成SECRET_KEY"""
    SECRET_KEY = 'XiVM9Hw1kxa4au3eHoO35rIRctJaQYhUC2m6nrlQwiRqhTmh6SCs4OgcIULFxtVO'

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # session配置,设置session存储到redis
    SESSION_TYPE = 'redis'
    # 指定session保存的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置session不是永久有效,即过了有效期就失效
    SESSION_PERMANENT = False
    # 设置过期时间,默认值是31天
    PERMANENT_SESSION_LIFETIME = 86400*2
