from models.user import User
from models.user_credentials_model import UserCredentials
from services.user_service import UserService
from daos.user_dao_impl import UserDAOImpl


class UserServiceImpl(UserService):
    @classmethod
    def get_user_by_id(cls, user_credentials):
        try:
            response = UserDAOImpl.get_user_by_id(user_credentials)
            if response:
                return User(response[0], response[1], response[2])
        except Exception as e:
            return None

    @classmethod
    def get_user_credentials(cls, user_credentials):
        response = UserDAOImpl.get_user_credentials(user_credentials)
        if response:
            return UserCredentials(response[1], response[2], response[3])
        else:
            return None
