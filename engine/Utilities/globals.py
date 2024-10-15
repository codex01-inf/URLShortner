import os


class Constants:
    DB_USERNAME = os.environ["MONGO_USERNAME"]
    DB_PASSWORD = os.environ["MONGO_PASSWORD"]
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"]
    SERVER_HOST = os.environ["SERVER_HOST"]
    SERVER_PORT = os.environ["SERVER_PORT"]
    DB = "sample_data"
    COLLECTION = "urls"