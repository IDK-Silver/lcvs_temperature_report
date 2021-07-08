import time
import libraries.autoReport
import libraries.config


if __name__ == "__main__":
    
    dic = libraries.config.ConfigDic.UserSetting()
    setting = libraries.config.SystemConfig(dic.sections)
    web = libraries.autoReport.autoReport(setting.read(dic.web_url), setting.read(dic.username), setting.read(dic.password))
    try:
        web.report()
        print("Success Report Body Temperature. This Windows after 5 Second will be close")
        time.sleep(5)
    except:
        print("User Name or Password Error please check setting.ini file is right")
        input("Press Enter")
    web.web_close()

    
    
    

    








