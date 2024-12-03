from app import db

# class Page1Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     field1 = db.Column(db.String(100), nullable=False)
#     field2 = db.Column(db.String(100), nullable=False)

# class Page2Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     field3 = db.Column(db.String(100), nullable=False)
#     field4 = db.Column(db.String(100), nullable=False)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


