from functools import wraps
from flask import request, Response
import neomodel as nm


class User(nm.StructuredNode):
    name = nm.StringProperty(unique_index=True)
    password = nm.StringProperty()


def check_auth(username, password):
    try:
        User.nodes.get(name=username, password=password)
        return True
    except User.DoesNotExist:
        return False


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated
