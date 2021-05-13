from models.user_credentials import UserCredentials
from services.user_service import UserService
from daos.user_dao_impl import UserDAOImpl


class UserServiceImpl(UserService):
    @classmethod
    def get_user_credentials(cls, user_credentials):
        response = UserDAOImpl.get_user_credentials(user_credentials)
        if response:
            return UserCredentials(response[1], response[2], response[3]).json()
        else:
            return None
