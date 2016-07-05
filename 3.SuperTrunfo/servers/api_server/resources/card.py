import neomodel as nm
from api_server.common.views import BaseListView, BaseDetailView
from api_server.common.models import BaseModel

""" MODEL """


class Card(nm.StructuredNode, BaseModel):
    name = nm.StringProperty(unique_index=True)
    attributes = nm.JSONProperty()

    pk_field = 'name'


""" VIEWS """


class BaseCardView(object):
    fields = {
        'name': {'type': str, 'required': True},
        'attributes': {'type': dict, }
    }
    model = Card


class CardListView(BaseCardView, BaseListView):
    pass


class CardDetailView(BaseCardView, BaseDetailView):
    pass
