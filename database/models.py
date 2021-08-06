from app import db


class Auto(db.Model):
    vin = db.Column(db.String(17), primary_key=True, nullable=False)
    number = db.Column(db.String(15), unique=True, nullable=False)
    brand = db.Column(db.String(15), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    make = db.Column(db.Date, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("clients.id"))

    def __init__(self, vin, number, brand, model, make):
        self.vin = vin
        self.number = number
        self.brand = brand
        self.model = model
        self.make = make

    def __repr__(self):
        info = "VIN:{}\nNumber:{}\nBrand:{}\nModel:{}\nMake:{}\n".format(
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

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        info = "Id:{}\nName:{}\nSurname:{}\n".format(
            self.id,
            self.name,
            self.surname,
        )
        return info
