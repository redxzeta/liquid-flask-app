from flask import Blueprint, request, jsonify
from service.session import SessionService

session = Blueprint("session", __name__)
session_service = SessionService()


@session.route('/session/<uid>', methods=['POST'])
def add_student(uid):
    obj = request.get_json()
    return jsonify(
        session_service.add_session(uid=uid, session=obj, )
    )


@session.route('/session', methods=['GET'])
def get_students():
    return jsonify(session_service.get_sessions())


@session.route('/session/<uid>', methods=['GET'])
def get_session_by_id(uid):
    return jsonify(session_service.get_session_by_id(uid))


@session.route('/session/<_id>', methods=['DELETE'])
def delete_student(_id):
    return session_service.delete_session(_id)


@session.route('/session/<_id>', methods=['PUT'])
def put_game_workout(_id):
    obj = request.get_json()
    return jsonify(session_service.add_game_session(game=obj, _id=_id))
