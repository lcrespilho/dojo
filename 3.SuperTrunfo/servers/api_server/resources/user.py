from api_server.common.views import BaseListView, BaseDetailView
from api_server import authentication

""" MODELS """


class User(authentication.User):
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
