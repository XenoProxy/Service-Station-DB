from app import db


class Auto(db.Model):
    vin = db.Column(db.String(17), primary_key=True)
    number = db.Column(db.String(15), unique=True)
    brand = db.Column(db.String(15), primary_key=True)
    model = db.Column(db.String(30), primary_key=True)
    make = db.Column(db.Date, primary_key=True)
    owner = db.relationship("Clients", bakref=db.backref("", lazy="dynamic"))

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
    id = db.Column(db.Integer, db.ForeignKey("client.id"), primary_key=True)
    name = db.Column(db.String(15),)
    surname = db.Column(db.String(20),)

    def __repr__(self):
        info = "Id:{}\nName:{}\nSurname:{}\n".format(
            self.id,
            self.name,
            self.surname,
        )
        return info
