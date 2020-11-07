from flask import Blueprint, request, jsonify
from service.session import SessionService

session = Blueprint("session", __name__)
session_service = SessionService()


@session.route('/session', methods=['POST'])
def add_student():
    obj = request.get_json()
    return jsonify(
        session_service.add_session(obj)
    )


@session.route('/session', methods=['GET'])
def get_students():
    return jsonify(session_service.get_sessions())


@session.route('/session/<_id>', methods=['DELETE'])
def delete_student(_id):
    return session_service.delete_session(_id)
