import logging

from pathlib import Path

from .logger_config import LoggerConfig
from .logger_config_factory import LoggerConfigFactory
from .logger_custom import CustomLogger


class Vic_Custom_Logger:
    def __init__(self, class_name: str = "",
                 config_file: str = "configuration/config_logger.ini"):
        # Step 1 : Define where your configuration file is
        self.root_dir: str = self._get_root_dir()
        self.ini_config_logger_path: str = f"{self.root_dir}/{config_file}"

        # Step 2 : Create a Logger Config instance
        self.logger_test: LoggerConfig = LoggerConfigFactory(
            config_file_path=self.ini_config_logger_path
        ).create_logger_config()

        # Step 3 : Pass the logger config to CustomLogger
        self.logger: logging.Logger = CustomLogger(
            logger_config=self.logger_test,
            class_name=class_name).get_logger()

    def _get_root_dir(self) -> str:
        return str(Path(__file__).parent.parent.parent.parent)

    def get_logger(self):
        return self.logger

