import configparser
import os
cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(__file__), '.env'))

