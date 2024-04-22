from enum import Enum
import logging.config
import yaml


class LoggingMode(str, Enum):
    DEV = "development"
    STAGING = "staging"
    PROD = "production"


class Logger(object):
    def __init__(self, config_path: str, mode: LoggingMode):
        with open(config_path, "rt") as f:
            config = yaml.safe_load(f.read())

        logging.config.dictConfig(config)
        self.logger = logging.getLogger(mode)
