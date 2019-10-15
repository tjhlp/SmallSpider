from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    # 数据库
    db = SQLAlchemy()
    db.init_app(app)

    return app, db


app, db = create_app("development")

if __name__ == '__main__':
    app.run()
