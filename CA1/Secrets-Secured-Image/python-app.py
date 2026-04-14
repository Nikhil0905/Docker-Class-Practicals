import os
import time
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

if not all([db_host, db_user, db_password, db_name]):
    print("Error: Missing database credentials in environment.")
    exit(1)

def connect():
    retries = 5
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_password,
                database=db_name
            )
            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute("SELECT VERSION()")
                db_version = cursor.fetchone()
                print(f"Application has been started and the Database is also Working Fine")
                print(f"[DB CONFIRMED] Connected to MySQL version: {db_version[0]}")
                cursor.close()
                conn.close()
                return True
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            print(f"Retrying in 5 seconds... ({retries} retries left)")
            time.sleep(5)
            retries -= 1
    return False

if __name__ == "__main__":
    if not connect():
        print("Failed to connect to database.")
    
    # keep the container alive to avoid immediate exit
    while True:
        time.sleep(3600)