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
    mode = ConfigUtil().doConfig("case.config","MODE","excute_case")
    print(mode)
    print(type(mode))