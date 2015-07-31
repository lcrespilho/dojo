import neomodel as nm
from server.common.views import BaseListView, BaseDetailView
from server.common.models import BaseModel
from .card import Card

""" MODEL """

class User(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    password = nm.StringProperty()
    pk_field = "name"



""" VIEWS """


class BaseUserView(object):
    fields = {
        'name': {'type': str, 'required': True},
    }
    input_fields = {
        'name': {'type': str, 'required': True},
        'password': {'type': str, 'required': True},
    }
    model = User


class UserListView(BaseUserView, BaseListView):
    pass


class UserDetailView(BaseUserView, BaseDetailView):
    pass




