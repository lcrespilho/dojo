from flask_restful import Resource, abort
from api_server.common.views import BaseListView
import socket
# import sys
import json


class BaseSession(object):
    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 8891)
        sock.connect(server_address)

        return sock

    def _send_message(self, json_obj):
        sock = self.connect()
        message = json.dumps(json_obj)
        sock.sendall(message)

        data = ''
        amount_received = None

        while amount_received is None or amount_received >= 1000:
            data_chunk = sock.recv(1000)
            amount_received = len(data_chunk)
            data += data_chunk

        sock.close()

        return json.loads(data)


class SessionListView(BaseSession, BaseListView):
    def get(self):
        return self._send_message({'action': 'get_sessions'})

    def post(self):
        return self._send_message({'action': 'create_session'})

