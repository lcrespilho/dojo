from datetime import datetime
import inspect
import sys
import json
import imp

from couchdb.mapping import Document, ViewField, TextField, FloatField
from couchdb.mapping import BooleanField, ListField, DateField


class BasicCouchOperations(Document):
    _id = TextField()
    create_at = DateField(default=datetime.now)

    def save(self, db, uuid=None):
        if not self._id:
            self._id = '{}_{}'.format(self.__predicate__, uuid)
        self.store(db)
        return self

    def delete(self, db):
        try:
            del db[self._id]
        except:
            # TODO: insert log here
            pass

    @classmethod
    def sync(cls, db):
        for element in inspect.getmembers(cls):
            if element[1].__class__.__name__ == 'ViewDefinition':
                attr = getattr(cls, element[0])
                attr.sync(db)


class UserAccess(BasicCouchOperations):
    __predicate__ = 'user_access'
    _id = TextField()  # email here

    type = TextField(default='user_access')
    account_id = TextField()
    account_name = TextField()
    email = TextField()

    all = ViewField(__predicate__, '''function(doc){
                    if(doc.type == 'user_access'){
                        emit(doc._id, doc);
                    }
            }''')

    _by_email = ViewField(__predicate__, '''function(doc){
                    if(doc.type == 'user_access' && doc.email){
                        emit(doc.email, doc);
                    }
            }''',
                         '''function(keys, values){
                            grouped = []
                            var item = {};
                            values.forEach(function(value){
                                grouped.push({account: value.account_id, name: value.account_name, id: value._id});
                            });
                            return grouped;
                         }
                         ''')

    @classmethod
    def get_by_email(cls, db, email=None):
        if email:
            executed_view = cls._by_email(db, reduce=True, group_level=1, key=email, wrapper=None)
        else:
            executed_view = cls._by_email(db, reduce=True, group_level=1, wrapper=None)
        return [(row.key, row.value) for row in executed_view.rows]


def sync_db_objects(db):
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            try:
                obj.sync(db)
            except AttributeError:
                pass
