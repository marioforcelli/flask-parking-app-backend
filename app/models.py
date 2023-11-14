# from flask import Flask
from sqlalchemy.orm import Mapped, mapped_column
from app.db_conn import db
import enum

class TypeVehicleEnum(enum.Enum):
    motorcycle = 'MOTO'
    car = 'CARRO'

    def __str__(self) -> str:
        return self.value


class Vehicle(db.Model):
    id_vehicle: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    brand : Mapped[str] = mapped_column(db.String)
    color : Mapped[str] = mapped_column(db.String)
    license_plate : Mapped[str] = mapped_column(db.String, unique=True)
    vehicle_type : Mapped[str] = mapped_column(db.Enum(TypeVehicleEnum))

    def __init__(self, brand, color, license_plate, vehicle_type):
        self.brand = brand
        self.color = color
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Company(db.Model):
    id_company: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    cnpj: Mapped[str] = mapped_column(db.String)
    address: Mapped[str] = mapped_column(db.String)
    phone: Mapped[str] = mapped_column(db.String)
    car_spaces: Mapped[int] = mapped_column(db.Integer)
    motorcycle_spaces:  Mapped[int] = mapped_column(db.Integer)

class ParkedVehicles(db.Model):
    id_parked: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    id_company: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('company.id_company'))
    id_vehicle: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('vehicle.id_vehicle'))
    check_in_at: Mapped[str] = mapped_column(db.DateTime)
    check_out_at: Mapped[str] = mapped_column(db.DateTime)

if __name__ == '__main__':
    db.create_all() 