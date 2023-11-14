from app.models import Vehicle as v
from app.db_conn import app
from app.services.vehicles import VehicleServices
from flask import Flask, request, jsonify, Response

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
    VehicleServices.create_vehicle(vehicle_data=data)
    return jsonify(data)

@app.route("/vehicles/retrieve/<id>")
def get(id):
    vehicle = VehicleServices.get_vehicle(id)
    return jsonify(vehicle), 200


@app.route("/vehicles/list")
def list():
    return jsonify(VehicleServices.list_all_vehicles())

@app.route("/vehicles/delete/<id>", methods=['DELETE'])
def delete(id):
    VehicleServices.delete_vehicle(id)
    res = jsonify({
        'message': 'Veículo deletado'
    })
    return res, 200


@app.route("/vehicles/update/<id>", methods=['POST'])
def update(id):
    vehicle = VehicleServices.get_vehicle(id)

    if not vehicle:
        return {'message': 'Veículo não encontrado'}, 404
    

    req_data = request.get_json()
    data = {
        "brand": req_data[0]["brand"],
        "color": req_data[0]["color"],
        "vehicle_type": req_data[0]["vehicle_type"],
        "license_plate": req_data[0]["license_plate"]
    }
    
    new_vehicle = VehicleServices.update_vehicle(id, data)
    return jsonify(new_vehicle)