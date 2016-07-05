from datetime import datetime
import inspect
import sys
import json
import imp

from couchdb.mapping import Document, ViewField, TextField, FloatField, DictField
from couchdb.mapping import BooleanField, ListField, DateField, Mapping


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


class Organization(BasicCouchOperations):
    __predicate__ = "organization"
    _id = TextField()
    name = TextField()
    local = ListField(DictField(Mapping.build(
        lat=FloatField(),
        lon=FloatField(),
        address_str=TextField(),
        city=TextField()
    )))
    donation_types = ListField(TextField())
    schedule = TextField()
    doc_type = TextField(default="organization")


    all = ViewField(__predicate__, '''function(doc){
        if(doc.doc_type == "organization"){
            emit(doc._id, doc);
        }
    }''')

    city = ViewField(__predicate__,
        '''function(doc){
            if (doc.doc_type == "organization"){
                doc.local.forEach(function(local){
                    emit (local.city, doc);
                });
            }
         }''')

    @classmethod
    def sync(cls, db):
        cls.all.sync(db)
        cls.city.sync(db)


class Donator(BasicCouchOperations):
    _id = TextField()
    name = TextField()
    doc_type = TextField(default="donator")

    all = ViewField("donator", '''function(doc){
        if(doc.doc_type == "donator"){
            emit(doc._id, doc);
        }
    }''')

    @classmethod
    def sync(cls, db):
        cls.all.sync(db)


def sync_db_objects(db):
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            try:
                obj.sync(db)
            except AttributeError:
                pass

