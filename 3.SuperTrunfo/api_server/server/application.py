from server import app, router

def run():
    router.define_routes()
    app.run(host="0.0.0.0", debug=True)