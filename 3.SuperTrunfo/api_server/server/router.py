from server import api
from server.resources import parent

_base = '/dojo/'

def define_routes():
    api.add_resource(parent.ParentListView, _base + 'parents', methods=['GET', 'POST'])
    api.add_resource(parent.ParentDetailView, _base + 'parents/<string:name>', methods=['GET', 'DELETE', 'PUT'])
