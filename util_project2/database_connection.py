import psycopg2
from psycopg2 import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(database="postgres",
                                user="serene",
                                password="samb2021",
                                host="serenesambpostgres.c24uajeyhwge.us-east-1.rds.amazonaws.com",
                                port="5432")
        return conn
    except OperationalError as e:
        print(f"{e}")
        return conn


connection = create_connection()
