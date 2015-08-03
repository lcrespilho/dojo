import logging
import sys

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', "%H:%M:%S")
#
root = logging.getLogger()
root.setLevel(logging.INFO)
#
ch.setFormatter(formatter)
root.addHandler(ch)