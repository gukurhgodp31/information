from flask.ext.script import Manager
from flask.ext.session import Session
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from config import Config


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象,存普通数据
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护
CSRFProtect(app)

Session(app)

manager = Manager(app)
# 将app和数据库关联
Migrate(app,db)
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()