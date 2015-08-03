

class Player:
    connection = None
    id = None

    def __init__(self, connection=None, id=None):
        self.connection = connection
        self.id = id