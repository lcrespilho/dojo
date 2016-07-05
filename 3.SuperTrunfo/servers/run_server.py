from servers.api_server import application
from servers.game_server.game_server import GameServer
import signal
import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print "Wrong number of arguments."
        print "Usage: python run_server.py [game|api]"
    elif sys.argv[1] == 'game':
        server = GameServer()

        def signal_handler(signal, frame):
            server.stop()
            sys.exit(0)


        signal.signal(signal.SIGINT, signal_handler)
        server.start()

    elif sys.argv[1] == 'api':
        application.run()
    else:
        print "Wrong argument. The argument must be game or api."
