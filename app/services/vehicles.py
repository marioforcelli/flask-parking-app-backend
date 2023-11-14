from app.schemas import VehicleSchema
from app.models import Vehicle
from app.db_conn import db

class VehicleServices:

    
    def list_all_vehicles():
        vehicle_schema = VehicleSchema(many=True)
        all_vehicles = Vehicle.query.all()
        return vehicle_schema.dump(all_vehicles)
    
    def create(vehicle_data):
        new_vehicle = Vehicle(brand=vehicle_data["brand"], 
                              color=vehicle_data["color"], 
                              license_plate=vehicle_data["license_plate"],
                              vehicle_type=vehicle_data["vehicle_type"] )
        db.session.add(new_vehicle)
        db.session.commit()