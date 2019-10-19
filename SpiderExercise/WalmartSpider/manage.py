from flask import Flask, jsonify
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


@app.route('/')
def index():
    from modules.data_module import Information
    # 初始化 user 模型，并设置数据并添加到数据库
    info = Information()
    data = info.query.all()
    print(data)

    # 返回注册结果
    return jsonify({'name': '123', 'words': '132'})


if __name__ == '__main__':
    app.run()
