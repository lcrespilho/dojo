import neomodel as nm
from server.common.views import BaseListView, BaseDetailView
from server.common.models import BaseModel
from .card import Card

""" MODEL """

class Deck(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    cards = nm.RelationshipTo('Card', 'CARD')
    # owner = nm.RelationshipFrom('User', 'USER', cardinality=nm.One)
    attributes = nm.ArrayProperty()

    pk_field = 'name'


def cards_serialize(cards):
    #return [{'name': card.name} for card in cards]
    return "brubs"



""" VIEWS """


class BaseDeckView(object):
    fields = {
        'name': {'type': str, 'required': True},
        'attributes': {'type': dict, },
        #'cards': {'type': str }
    }
    model = Deck


class DeckListView(BaseDeckView, BaseListView):
    pass


class DeckDetailView(BaseDeckView, BaseDetailView):
    pass
