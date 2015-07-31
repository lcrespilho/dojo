__author__ = 'Ariel'
from flask.ext.httpauth import HTTPBasicAuth
from server.resources.user import User
import neomodel as nm

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    try:
        User.nodes.get(name=username)
    except nm.DoesNotExist:
        return False
    return True
