import couchdb
from couchdb.http import PreconditionFailed

from base_connector import BaseConnector


class Connector(BaseConnector):
    def __init__(self, user, pwd, db_name):
        super(self.__class__, self).__init__(user, pwd, db_name)
        self._set_credentials()
        self.connected = False

    def _set_credentials(self):
        credentials = (self.user, self.pwd)
        self.couch_server = couchdb.Server()
        self.couch_server.resource.credentials = credentials

    def connect(self):
        self.db = self.couch_server[self.db_name]
        self.connected = True

    def delete_db(self):
        try:
            self.couch_server.delete(self.db_name)
        except PreconditionFailed:
            print 'DB do not exist'

    def create_db(self):
        try:
            self.couch_server.create(self.db_name)
        except PreconditionFailed:
            print 'DB already exist'

    def save(self, object_to_save):
        if not self.connected:
            self.connect()
        uuid = self.couch_server.uuids(count=1)
        return object_to_save.save(self.db, uuid[0])

    def get(self, id):
        if not self.connected:
            self.connect()
        ad = self.db.get(id)
        return ad
