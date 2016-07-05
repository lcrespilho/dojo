from abc import abstractmethod, ABCMeta


class BaseConnector(object):
    __metaclass__ = ABCMeta

    def __init__(self, user, pwd, db_name):
        self.user = user
        self.pwd = pwd
        self.db_name = db_name
        self.db = None
        self.connected = False

    @abstractmethod
    def connect(self):
        raise NotImplementedError()

    @abstractmethod
    def save(self, ad):
        raise NotImplementedError()

    @abstractmethod
    def get(self, object_id):
        raise NotImplementedError()
