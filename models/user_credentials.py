class UserCredentials:
    def __init__(self, user_name=None, password=None, user_id=None):
        self.user_name = user_name
        self.password = password
        self.user_id = user_id

    def json(self):
        return {
            'userName': self.user_name,
            'password': self.password,
            'userId': self.user_id
        }

    @staticmethod
    def json_parse(json):
        user_credentials = UserCredentials()
        user_credentials.user_name = json['userName'] if "userName" in json else None
        user_credentials.password = json['password'] if "password" in json else None
        user_credentials.user_id = json['userId'] if "userId" in json else 0

        return user_credentials
