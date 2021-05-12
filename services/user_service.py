from daos.employee_dao_impl import EmployeeDAOImpl


class UserService:
    user_dao = UserDAOImpl()

    @classmethod
    def create_new_user_credential(cls, user):
        return cls.user_dao.create_new_user(user), 201

    @classmethod
    def all_user_credentials(cls):
        return cls.user_dao.all_users()

    @classmethod
    def get_user_credential_by_id(cls, user_id):
        return cls.user_dao.get_user_id(user_id)

    @classmethod
    def update_user_credential(cls, user):
        return cls.user_dao.update_user(user)

    @classmethod
    def delete_user_credential(cls, user_id):
        return cls.user_dao.delete_user(user_id)

    @classmethod
    def login(cls, username, password):
        return cls.user_dao.get_user_id(username, password)
