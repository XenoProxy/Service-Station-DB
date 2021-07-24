from app import db


class Auto(db.Model):
    vin = db.Column(db.String(17), primary_key=True, nullable=False)
    number = db.Column(db.String(15), unique=True, nullable=False)
    brand = db.Column(db.String(15), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    make = db.Column(db.Date, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("clients.id"))

    def __repr__(self):
        info = "VIN:{}\nNumber:{}\nBrand:{}\nModel:{}\nMake:{}".format(
            self.vin,
            self.number,
            self.brand,
            self.model,
            self.make,
        )
        return info


class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    auto = db.relationship("Auto", backref="owner", lazy="dynamic")

    def __repr__(self):
        info = "Id:{}\nName:{}\nSurname:{}\n".format(
            self.id,
            self.name,
            self.surname,
        )
        return info
