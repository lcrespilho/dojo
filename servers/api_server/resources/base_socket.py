import socket
import sys
import json


class BaseSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        server_address = ('localhost', 8891)
        self.sock.connect(server_address)

    def get_sessions(self):
        try:
            message = json.dumps({'action': 'get_sessions'})
            self.sock.sendall(message)

            data = ''
            amount_received = None

            while amount_received is None or amount_received >= 1000:
                data_chunk = self.sock.recv(1000)
                amount_received = len(data_chunk)
                data += data_chunk
        except:
            return None

        self.sock.close()

        return json.loads(data)
