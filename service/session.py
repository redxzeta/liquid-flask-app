from repository.database import *


class SessionService:
    def __init__(self):
        self.__session = CONNECTION.collection["session"]

    def add_session(self, session: dict):
        self.__session.add(session)
        return self.__session.find_by_criteria(session)

    def get_sessions(self):
        return self.__session.find_all()

    def get_session_by_id(self, _id):
        return self.__session.find_by_id(_id)

    def delete_session(self, _id: int):
        stu = self.__session.find_by_id(_id)
        self.__session.remove_by_id(_id)
        return stu
