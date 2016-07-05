""" We Don't have a name - please, find a name before change anything here!

Usage:
  no_name_yet [ --delete | --install | --update ]

Options:
  --delete                                Delete db and all data
  --install                               Install DB
  --update                                Update and sync db
"""

from server.models import sync_db_objects
from server.db.couch_connector import Connector
from server import application

from docopt import docopt
from raccoon_log.config import config_log

import sys
import os


reload(sys)
sys.setdefaultencoding('UTF8')


def get_config():
    try:
        with open(os.environ['HOME'] + '/.dojo_4.json') as init_file:
            ini_config = eval(init_file.read())
    except IOError:
        ini_config = {
            "LOG_PATH": "/tmp/log",
            "DB_NAME": "dojo_4_db",
            "DB_USER": "admin",
            "DB_PASSWORD": "admin"
        }

    return ini_config


def run():

    args = docopt(__doc__)

    ini_config = get_config()

    config_log(ini_config.get('LOG_PATH'), 'dojo_4', develop=True)

    connector = Connector(ini_config['DB_USER'], ini_config['DB_PASSWORD'], ini_config['DB_NAME'])

    if args.get('--install'):
        print 'Installing DB.'
        connector.create_db()
        print 'created'
        connector.connect()
        print 'Syncing Views.'
        sync_db_objects(connector.db)
        print 'Installing Accounts.'

    elif args.get('--update'):
        connector.connect()
        sync_db_objects(connector.db)

    elif args.get('--delete'):
        print 'Removing DB'
        connector.delete_db()

    else:
        connector.connect()
        application.run(port=8080, debug=True)
        print 'ok'

    sys.exit(0)


if __name__ == '__main__':
    run()
