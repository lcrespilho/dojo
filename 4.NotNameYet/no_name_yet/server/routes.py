from server import views


routes = {
    '/': (views.home, ['GET']),
}
