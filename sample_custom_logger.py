import vic_lim_wx


class test:
    def __init__(self, msg: str):
        self.logger = vic_lim_wx.Vic_Custom_Logger(
            config_file="C:/GIT/Vic_Lim_WX/configuration/config_logger.ini",
            class_name=test.__name__).get_logger()
        self.msg: str = msg

    def get_message(self):
        self.logger.debug(f"Testing {self.msg}, this is log DEBUG")
        self.logger.info(f"Testing {self.msg}, this is log INFO")
        self.logger.warning(f"Testing {self.msg}, this is log WARNING")
        self.logger.error(f"Testing {self.msg}, this is log ERROR")
        self.logger.critical(f"Testing {self.msg}, this is log CRITICAL")


def main():
    test_class = test(msg="Hellowwww")
    test_class.get_message()


if __name__ == "__main__":
    main()
