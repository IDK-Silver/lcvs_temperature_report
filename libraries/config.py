
import os
import configparser

class ConfigDic:
    setting_filename = "setting.ini"

    def __init__(self) -> None:
        pass
    class UserSetting:
        sections = "User_Setting"
        web_url = "Web Url"
        username = "User Name"
        password = "User Passord"


class SystemConfig:
    def __init__(self, default_section) -> None:
        self.default_section = default_section
        self.config_filepath = ConfigDic.setting_filename
        self.config = configparser.ConfigParser()
        self.config.read(self.config_filepath, encoding='utf-8')

        if not os.path.isfile(self.config_filepath):
            print(self.config_filepath)
            self.create_default_config()

    def read(self, key):
        return self.config[self.default_section][key]

    def create_default_config(self):
        user_setting = ConfigDic.UserSetting()
        self.config[user_setting.sections] = {}
        self.config[user_setting.sections][user_setting.web_url] = "http://163.32.74.2/web_ap/student_allin/index.asp"
        self.config[user_setting.sections][user_setting.username] = ""
        self.config[user_setting.sections][user_setting.password] = ""
        with open(ConfigDic.setting_filename, 'w') as configfile:
                self.config.write(configfile)
        



if __name__ == "__main__":
    config = SystemConfig()
    config.read("test")