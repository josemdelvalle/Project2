from models.user import User
from models.user_credentials import UserCredentials
from services.user_service import UserService
from daos.user_dao_impl import UserDAOImpl


class UserServiceImpl(UserService):
    @classmethod
    def get_user_by_id(cls, user_id):
        return UserDAOImpl.get_user_by_id(user_id)

    @classmethod
    def get_user_credentials(cls, user_credentials):
        user = UserDAOImpl.get_user_credentials(user_credentials)
        return user
