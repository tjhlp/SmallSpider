# from manage import db


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@13.114.205.255:3306/walmart'
# 跟踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Information(db.Model):
    # 给表重新定义一个名称，默认名称是类名的小写，比如该类默认的表名是user。
    __tablename__ = "Information"
    id = db.Column(db.Integer, primary_key=True)
    Rank = db.Column(db.String(16))
    Shop_Id = db.Column(db.String(32), unique=True)
    Url = db.Column(db.String(200))
    Name = db.Column(db.String(50))
    Price = db.Column(db.Float)
    Star = db.Column(db.String(10))
    Review = db.Column(db.String(10))
    Page = db.Column(db.Integer)
    Shop_name = db.Column(db.String(200))
    Main_Image_url = db.Column(db.String(200))
    Brand = db.Column(db.String(200))
    Category = db.Column(db.String(300))
    Highlights = db.Column(db.String(300))
    Key_World = db.Column(db.String(20))
    Time = db.Column(db.DateTime)

    def __repr__(self):
        return "Goods: %s %s %s %s" % (self.Rank, self.Name, self.Price, self.Page)


db.drop_all()
db.create_all()


@app.route('/')
def index():
    return "hahah"


if __name__ == '__main__':
    app.run(debug=True)





