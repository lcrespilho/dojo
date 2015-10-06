import neomodel as nm
from flask_restful import Resource, abort
from servers.api_server.common.views import BaseListView
from .deck import Deck
import socket
import json


class BaseSession(object):
    def connect(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('localhost', 8891)
            sock.connect(server_address)
        except:
            abort(500)

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
    input_fields = {
        'deck_id': {"type": str, "required": True}
    }

    fields = {
        'name': {'type': str, 'required': True},
        'attributes': {'type': dict, }
    }

    def get(self):
        return self._send_message({'action': 'get_sessions'})

    def post(self):
        args = self._parse_arguments()
        try:

            attributes = Deck.nodes.get(name=args['deck_id']).attributes
            cards = [self.serialize(node) for node in Deck.nodes.get(name=args['deck_id']).cards]
        except nm.DoesNotExist:
            abort(404)

        for idx, card in enumerate(cards):
            new_atributes = {}

            for attr_name in card['attributes']:
                if attr_name in attributes:
                    new_atributes[attr_name] = card['attributes'][attr_name]
            cards[idx]['attributes'] = new_atributes

        message = {
            'action': 'create_session',
            'deck_cards': cards,
            'attributes': attributes,
        }
        # return message

        return self._send_message(message)

