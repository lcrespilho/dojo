from base_socket import BaseSocket
from game_session import GameSession
from thread import start_new_thread
from time import time, sleep
from server_log import logging


class GameServer(BaseSocket):
    sessions_host = ''
    sessions_port = 8890
    sessions_socket = None

    api_host = 'localhost'
    api_port = 8891
    api_socket = None

    game_sessions = []
    max_sessions = 20

    def __exit__(self, type, value, traceback):
        self.stop()

    def start(self):
        self.sessions_socket = self._start_server(self.sessions_host, self.sessions_port)
        self.api_socket = self._start_server(self.api_host, self.api_port)

        start_new_thread(self.sessions_janitor, ())
        start_new_thread(self._sessions_manager, ())

        logging.info('Game server running')

        self._main_loop()

    def _accept_session(self, connection, address):
        begin = time()
        logging.info('Session join attempted')

        while time() - begin < 200:
            data = self._receive_dict_async(connection)

            if data and 'session_id' in data and 'player_id' in data:
                for idx, session in enumerate(self.game_sessions):
                    if session.id == data['session_id'] and session.can_player_join(data['player_id']):
                        session.add_player(data['player_id'], connection)
                    return self.game_sessions[idx]

                logging.info('Invalid session id')
                connection.close()
                return None
            elif data and ('session_id' not in data or 'player_id' not in data):
                logging.info('Invalid join')
                connection.close()
                return None

        logging.info('Join failed')
        connection.close()
        return None

    def _main_loop(self):
        while 1:
            connection, address = self.sessions_socket.accept()
            connection.setblocking(False)

            self._send_dict(connection, {"connected": True})

            session = self._accept_session(connection, address)

            if session is not None:
                logging.info('Player joined session %s' % str(session.id))

    def stop(self):
        for session in self.game_sessions:
            session.inactivate_sessions('bye')

        if self.sessions_socket:
            self.sessions_socket.close()

    def _sessions_manager(self):
        while 1:
            connection, address = self.api_socket.accept()
            logging.info('API connected')
            connection.setblocking(False)
            start_new_thread(self._listen_api, (connection,))

    def _listen_api(self, connection):
        begin = time()

        while time() - begin < 200:
            data = self._receive_dict_async(connection)

            if data and 'action' in data:
                if data['action'] == 'create_session':
                    new_session = GameSession(deck_cards=data['deck_cards'], attributes=data['attributes'])
                    start_new_thread(new_session.session_loop, ())
                    self.game_sessions.append(new_session)
                    self._send_dict(connection, {'session_id': new_session.id})
                    break

                elif data['action'] == 'destroy_session' and 'session_id' in data:
                    for idx, session in enumerate(self.game_sessions):
                        if session.id == data['session_id']:
                            self.game_sessions[idx].active = False
                            self._send_dict(connection, {'deleted': True})
                            break

                    self._send_dict(connection, {'deleted': False})
                elif data['action'] == 'get_sessions':
                    session_data = []
                    for session in self.game_sessions:
                        if session.active:
                            session_data.append(session.serialize())
                    self._send_dict(connection, session_data)
                    logging.info('API requested session list')
                    break

        connection.close()
        logging.info('API disconnected')

    def sessions_janitor(self):
        while 1:
            sleep(0.2)

            for idx, session in enumerate(self.game_sessions):
                if idx >= self.max_sessions:
                    session.inactivate_sessions('full')

                session.check_timeout()

                if not session.active:
                    logging.info('Closed session %s' % session.id)
                    session.close()
                    del self.game_sessions[idx]
