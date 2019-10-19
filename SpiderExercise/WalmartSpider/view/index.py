from flask import jsonify

from modules.data_module import Information
from manage import app


@app.route('/index')
def index():
    # 4. 初始化 user 模型，并设置数据并添加到数据库
    info = Information()
    data = info.query.all()

    # try:
    #     db.session.add(user)
    #     db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     # 数据保存错误
    #     return jsonify(errno=400, errmsg="数据保存错误")

    # 6. 返回注册结果
    return jsonify({'data': data})
