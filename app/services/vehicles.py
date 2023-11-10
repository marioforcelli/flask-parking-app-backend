from app.schemas import VehicleSchema
from app.models import Vehicle as v

class VehicleServices:

    
    def list_all_vehicles():
        vehicle_schema = VehicleSchema(many=True)
        all_vehicles = v.query.all()
        return vehicle_schema.dump(all_vehicles)


