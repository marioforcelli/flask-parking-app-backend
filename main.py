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
    return jsonify(
        {
            "color" : req_data[0]["color"]
        })
@app.route("/vehicles/list")
def list():
    return jsonify(VehicleServices.list_all_vehicles())


