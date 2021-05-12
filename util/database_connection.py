import psycopg2
from psycopg2._psycopg import OperationalError



def crete_connction():
    try:
        conn = psycopg2.connect(database="postgres",
                                user="  ",
                                password="  ",
                                host="  ",
                                port="5432")
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn


connection = crete_connction()