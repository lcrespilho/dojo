from servers.api_server import router, app


def run():
    router.define_routes()
    app.run(host="0.0.0.0", port=5000, debug=True)
