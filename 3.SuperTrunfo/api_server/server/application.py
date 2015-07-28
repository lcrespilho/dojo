from server import app, router
from . import authentication

def run():
    router.define_routes()
    app.run(host="0.0.0.0", debug=True)