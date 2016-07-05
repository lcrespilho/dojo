import neomodel as nm
from api_server.common.views import BaseListView, BaseDetailView
from card import Card

""" MODEL """


class Deck(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    cards = nm.RelationshipTo('Card', 'CARD')
    attributes = nm.ArrayProperty()

    pk_field = 'name'


""" VIEWS """


class BaseDeckView(object):
    fields = {
        'name': {'type': str, 'required': True},
        'attributes': {'type': dict, },
    }
    model = Deck


class DeckListView(BaseDeckView, BaseListView):
    pass


class DeckDetailView(BaseDeckView, BaseDetailView):
    pass
