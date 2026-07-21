import mysql.connector


class DatabaseManager:

    def __init__(self, config):
        self.config = config
        self.source_connection = None
        self.destination_connection = None

    def connect_source(self):
        source = self.config.get_source_database()

        self.source_connection = mysql.connector.connect(
            host=source["host"],
            port=source["port"],
            database=source["database"],
            user=source["user"],
            password=source["password"]
        )

    def connect_destination(self):
        destination = self.config.get_destination_database()

        self.destination_connection = mysql.connector.connect(
            host=destination["host"],
            port=destination["port"],
            database=destination["database"],
            user=destination["user"],
            password=destination["password"]
        )

    def get_source_connection(self):
        return self.source_connection

    def get_destination_connection(self):
        return self.destination_connection

    def close_connections(self):
        pass