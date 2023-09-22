import os

import vic_lim_wx


def main():
    ini_config_logger_path: str = \
        f"{os.getcwd()}/configuration/config_logger.ini"
    logger_test: vic_lim_wx.LoggerConfig = vic_lim_wx.LoggerConfigFactory(
        config_file_path=ini_config_logger_path
    ).create_logger_config()
    print(logger_test.get_color(log_level="info"))


if __name__ == "__main__":
    main()
