class BaseController:
    def __init__(self, connection):
        self.conn = connection.conn
        self.session = connection.session
        self.query = connection.session.query
        self.delete = connection.session.delete
        self.add = connection.session.add
        self.commit = connection.session.commit
