'''
读取配置文件
'''

import configparser

class ConfigUtil:
    def doConfig(self,configPath,section,option):
        cfg = configparser.ConfigParser()
        cfg.read(configPath, encoding="utf-8")
        mode = cfg.get(section,option)
        return mode

if __name__ == '__main__':
    mode = ConfigUtil().doConfig("D:\Python\Study\FmApp\Configs\case.config","MYSQL","connect_info")
    print(mode)
    print(type(eval(mode)))
