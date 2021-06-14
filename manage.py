from flask.ext.script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import session

from info import app,db

manager = Manager(app)
# 将app和数据库关联
Migrate(app,db)
# 将迁移命令添加到manager中
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    manager.run()