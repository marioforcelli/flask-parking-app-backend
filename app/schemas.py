from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
from app.db_conn import app
from app.models import Vehicle, Company, ParkedVehicles, TypeVehicleEnum

ma = Marshmallow(app)

class VehicleSchema(Schema):
    id_vehicle = fields.Int()
    brand = fields.Str(required=True)
    color = fields.Str(required=True)
    vehicle_type = fields.Enum(TypeVehicleEnum)
    license_plate = fields.Str(required=True)



class CompanySchema(Schema):
    class Meta:
        model = Company 
    
    id_company = ma.auto_field()  
    cnpj = ma.auto_field()
    address = ma.auto_field()
    phone = ma.auto_field()
    car_spaces = ma.auto_field()
    motorcycle_spaces = ma.auto_field()