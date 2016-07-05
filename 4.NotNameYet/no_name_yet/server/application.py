from routes import routes

from flask import Flask


app = Flask(__name__)


def add_routes():
    for rule, endpoint_info in routes.iteritems():
        route_name = endpoint_info[0].__name__
        app.add_url_rule(rule, route_name, view_func=endpoint_info[0], methods=endpoint_info[1])


def run(port=8080, debug=False, local=True):
    add_routes()
    app.run(host='127.0.0.1' if local else '0.0.0.0', port=port, debug=debug)


def show_routes():
    max_length = max([len(k) for k in routes.routes.keys()]) + 5

    for rule in sorted(routes.routes.keys()):
        print '%s [%s]' % (rule.ljust(max_length), ','.join(routes.routes[rule][1]))