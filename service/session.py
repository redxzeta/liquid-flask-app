from repository.database import *


class SessionService:
    def __init__(self):
        self.__session = CONNECTION.collection["session"]

    def add_session(self, uid, session: dict):
        _id = f"{uid}"
        self.__session.add_by_id(_id, session)
        # return self.__session.find_by_criteria(session)
        return self.__session.find_by_id(_id)

    def get_sessions(self):
        return self.__session.find_all()

    def get_session_by_id(self, _id):
        return self.__session.find_by_id(_id)

    def delete_session(self, _id: int):
        stu = self.__session.find_by_id(_id)
        self.__session.remove_by_id(_id)
        return stu

    def add_game_session(self, game, _id):
        self.__session.update_by_id(_id, key="game_workout", value=game, aggregate=PUSH )
        return self.__session.find_by_id(_id)
