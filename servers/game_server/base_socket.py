from time import time
from server_log import logging
import socket
import sys
import json
import ast


class BaseSocket(object):
    address = None
    last_inter = None
    _buffer_size = 10000

    def _send_dict(self, connection, data):
        try:
            json_data = json.dumps(data)
            json_data = ast.literal_eval(json_data)
            print '!!!!!!!!!!!!!:', json_data
            connection.send(json_data)
        except:
            pass

    def _receive_dict_async(self, connection):
        data = ''
        if not connection:
            return None

        try:
            data_chunk = ''

            while len(data_chunk) >= self._buffer_size or len(data) < 1:
                data_chunk = connection.recv(self._buffer_size)
                print data_chunk
                data += data_chunk
                data_chunk = ''
                self.last_interaction = time()

        except socket.error:
            if len(data) == 0:
                return None

        try:
            data = data.split('\n')[-1]
            json_data = json.loads(data)
            json_data = ast.literal_eval(json_data)
        except ValueError:
            return None

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