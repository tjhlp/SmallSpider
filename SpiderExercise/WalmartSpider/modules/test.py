from manage import db
INDEXES = ['Rank', 'Id', 'Url', 'Name', 'Price', 'Star', 'Review', 'Page', 'Shop_name', 'Main_Image_url', 'Brand',
           'Category', 'Highlights', 'Key_World', 'Time']

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
