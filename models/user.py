# class User:
#     def __init__(self, user_id=None, first_name=None, last_name=None):
#         self.user_id = user_id
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def json(self):
#         return {
#             'firstName': self.first_name,
#             'lastName': self.last_name,
#             'userId': self.user_id
#         }
#
#     @staticmethod
#     def json_parse(json):
#         user = User()
#         User.first_name = json['firstName'] if "firstName" in json else None
#         User.last_name = json['lastName'] if "lastName" in json else None
#         User.user_id = json['userId'] if "userId" in json else None
#         return user
