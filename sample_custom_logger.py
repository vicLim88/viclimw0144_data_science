import os
import logging
import vic_lim_wx


def main():

    # Step 1 : Define where your configuration file is
    ini_config_logger_path: str = \
        f"{os.getcwd()}/configuration/config_logger.ini"

    # Step 2 : Create a Logger Config instance
    logger_test: vic_lim_wx.LoggerConfig = vic_lim_wx.LoggerConfigFactory(
        config_file_path=ini_config_logger_path
    ).create_logger_config()

    # Step 3 : Pass the logger config to CustomLogger
    logger: logging.Logger = vic_lim_wx.CustomLogger(
        logger_config=logger_test,
        class_name="test").get_logger()

    # Step 4 : Start using !!!
    logger.debug(msg="Test Debug")
    logger.info(msg="Test Info is working")
    logger.warning(msg="Test Warning is working")
    logger.error(msg="Test Error is working")


if __name__ == "__main__":
    main()
