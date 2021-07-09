from app import db


class Auto(db.Model):
    vin = db.Column(db.String(17), primary_key=True)
    number = db.Column(db.String(15), unique=True)
    brand = db.Column(db.String(15), primary_key=True)
    model = db.Column(db.String(30), primary_key=True)
    make = db.Column(db.Date, primary_key=True)

    def __repr__(self):
        return "<VIN: {}>".format(self.vin)
