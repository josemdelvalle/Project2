from flask import jsonify, json
from daos.user_dao import UserDAO
from exceptions.resource_not_found import ResourceNotFound
from models.user_credentials import UserCredentials
from util_project2.database_connection import connection


class UserDAOImpl(UserDAO):
    @classmethod
    def get_user_by_id(cls, user_credentials):
        try:
            sql = "SELECT * FROM users WHERE user_id= %s ;"
            cursor = connection.cursor()
            cursor.execute(sql, [user_credentials.user_id])
            record = cursor.fetchone()
            return record
        except Exception as e:
            return None

    @classmethod
    def get_user_credentials(cls, user_credentials):
        try:
            sql = "SELECT * FROM user_credentials WHERE username= %s AND password_ = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [user_credentials.user_name, user_credentials.password])
            record = cursor.fetchone()
            return record
        except Exception as e:
            return None


pass
# def create_new_user_credential(self, user):
#     sql = "INSERT INTO users VALUES(DEFAULT, %s, %s) RETURNING *"
#     cursor = connection.cursor()
#     cursor.execute(sql, [user.user_username, user.user_password])
#
#     connection.commit()
#     record = cursor.fetchone()
#
#     return UserCredentials(record[0], record[1], record[2]).json()
#
# def get_user_credential_by_id(self, user_id):
#     sql = "SELECT * FROM users WHERE user_id = %s"
#     cursor = connection.cursor()
#     cursor.execute(sql, [user_id])
#
#     record = cursor.fetchone()
#
#     if record:
#         return UserCredentials(record[0], record[1], record[2])
#     else:
#         raise ResourceNotFound(f"User with id: {user_id} - Not Found")
#
# def all_user_credentials(self):
#     sql = "SELECT * FROM users"
#
#     cursor = connection.cursor()
#
#     cursor.execute(sql)
#     records = cursor.fetchall()
#
#
#     user_list = []
#
#     for record in records:
#
#         user = UserCredentials(record[0], record[1], record[2])
#
#         user_list.append(user.json())
#     return user_list
#
# def update_user_credentials(self, change):
#     sql = "UPDATE users SET user_username=%s, user_password=%s WHERE user_id=%s RETURNING * "
#
#     cursor = connection.cursor()
#     # Keep in mind employee_id has to be added in the last column otherwise you will get "tuple index out of
#     # range" error
#     cursor.execute(sql, [change.user_username, change.user_password])
#     connection.commit()
#
#     record = cursor.fetchone()
#     return UserCredentials(record[0], record[1], record[2])
#
# def delete_user_credentials(self, user_id):
#     sql = "DELETE FROM users WHERE user_id=%s"
#     cursor = connection.cursor()
#     cursor.execute(sql, [user_id])
#     connection.commit()
#
# @staticmethod
# def get_user_credentials(username, password):
#     sql = "SELECT * FROM users WHERE user_username=%s AND user_password=%s "
#
#     cursor = connection.cursor()
#     cursor.execute(sql, [username, password])
#
#     connection.commit()
#
#     record = cursor.fetchone()
#
#     if record:
#         return UserCredentials(record[0], record[1], record[2])
