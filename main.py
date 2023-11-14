from app.db_conn import app, db
from app.services.vehicles import VehicleServices
from flask import Flask, request, jsonify, Response
from sqlalchemy.exc import IntegrityError

@app.route("/")
def hello():
    return "Hello, World2221!"


@app.route("/vehicles/create", methods=['post'])
def create():
    try:
        req_data = request.get_json()
        data = {
        "brand": req_data[0]["brand"],
        "color": req_data[0]["color"],
        "vehicle_type": req_data[0]["vehicle_type"],
        "license_plate": req_data[0]["license_plate"]
    }
        VehicleServices.create_vehicle(vehicle_data=data)
        return jsonify(data)
    
    except IntegrityError as e:
        db.session.rollback()
        return {'message': 'Carro já existente na base de dados.'}, 400
    
    except KeyError as e:
        db.session.rollback()
        return {'message': f'O campo {str(e)} é obrigatório'}, 400
    
    except Exception:
        return {'message': 'Erro inesperado'}, 500
    

@app.route("/vehicles/retrieve/<id>")
def get(id):

    try:
        vehicle = VehicleServices.get_vehicle(id)
        if not vehicle:
            db.session.rollback()
            return {'message' : 'Veículo não encontrado'}, 404
        return jsonify(vehicle), 200
    except Exception:
        db.session.rollback()
        return {'message', 'Erro inesperado'}, 500

@app.route("/vehicles/list")
def list():
    try:
        return jsonify(VehicleServices.list_all_vehicles())
    except Exception:
        db.session.rollback()
        return {'message', 'Erro inesperado'}, 500
    

@app.route("/vehicles/delete/<id>", methods=['DELETE'])
def delete(id): 
    
    try:
         VehicleServices.delete_vehicle(id)
    except Exception:
        db.session.rollback()
        return {'message', 'Erro inesperado'}, 500


   

@app.route("/vehicles/update/<id>", methods=['POST'])
def update(id):

    try:
        vehicle = VehicleServices.get_vehicle(id)

        if not vehicle:
            db.session.rollback()
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
    
    except Exception:
        return {'message', 'Erro inesperado'}, 500
