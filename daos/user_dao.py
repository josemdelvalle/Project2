from abc import abstractmethod, ABC


class UserDAO(ABC):
    @abstractmethod
    def get_user_by_id(self, user_credentials):
        pass

    @abstractmethod
    def get_user_credentials(self, user_credentials):
        pass
    #
    # @abstractmethod
    # def create_new_user_credential(self, user):
    #     pass
    #
    # @abstractmethod
    # def get_user_credential_by_id(self, user_id):
    #     pass
    #
    # @abstractmethod
    # def all_user_credentials(self):
    #     pass
    #
    # @abstractmethod
    # def update_user_credentials(self, change_user):
    #     pass
    #
    # @abstractmethod
    # def delete_user_credentials(self, user_id):
    #     pass
