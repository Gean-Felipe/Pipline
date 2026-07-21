class DatabaseManager:

    def __init__(self, config):
        self.config = config
        self.source_connection = None
        self.destination_connection = None

    def connect_source(self):
        pass

    def connect_destination(self):
        pass

    def get_source_connection(self):
        return self.source_connection

    def get_destination_connection(self):
        return self.destination_connection

    def close_connections(self):
        pass
        source = self.config.get_source_database()