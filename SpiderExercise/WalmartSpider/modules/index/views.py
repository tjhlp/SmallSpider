from flask import jsonify

from models import Information
from manage import app


@app.route('/index')
def index():
    # 初始化 user 模型，并设置数据并添加到数据库
    info = Information()
    data = info.query.all()

    # 返回注册结果
    return jsonify({'data': data})


