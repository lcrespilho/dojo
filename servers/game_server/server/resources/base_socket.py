from time import time
from server_log import logging
import socket
import sys
import json

class BaseSocket(object):
    address = None
    last_inter = None

    def _send_dict(self, connection, data):
        try:
            json_data = json.dumps(data)
            connection.send(json_data)
        except:
            pass

    def _receive_dict_async(self, connection):
        if not connection:
            return None

        try:
            data = connection.recv(1024)
            self.last_interaction = time()
        except socket.error:
            return None

        try:
            json_data = json.loads(data)
        except ValueError:
            return False

        return json_data

    @staticmethod
    def _start_server(host, port):
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            socket_obj.bind((host, port))
        except socket.error, msg:
            logging.error('Bind failed on %s:%d with message %s' % (host, port, msg[1]))
            sys.exit()

        socket_obj.listen(10)  # What is this argument?

        return socket_obj