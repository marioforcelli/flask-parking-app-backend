from app.models import Vehicle as v
from app.db_conn import app
from app.services.vehicles import VehicleServices
from flask import Flask, request, jsonify

@app.route("/")
def hello():
    return "Hello, World2221!"


@app.route("/vehicles/create", methods=['post'])
def create():
    req_data = request.get_json()
    data = {
        "brand": req_data[0]["brand"],
        "color": req_data[0]["color"],
        "vehicle_type": req_data[0]["vehicle_type"],
        "license_plate": req_data[0]["license_plate"]
    }
    VehicleServices.create(vehicle_data=data)
    return jsonify(data)

@app.route("/vehicles/list")
def list():
    return jsonify(VehicleServices.list_all_vehicles())


