
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config():

    DEBUG = True


    ALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)


app.config.from_object(Config)



if __name__ == '__main__':
    app.run()