from app.models import Vehicle as v
from app.schemas import VehicleSchema
from app.db_conn import app


@app.route("/")
def hello():
    return "Hello, World2221!"


@app.route("/vehicles/create", methods=['post'])
def create():
    return 'criou'

@app.route("/vehicles/list")
def list():
    vehicle_schema = VehicleSchema(many=True)
    all_vehicles = v.query.all()
    return vehicle_schema.dump(all_vehicles)


