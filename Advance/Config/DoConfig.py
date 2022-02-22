'''
读取配置文件
'''

import configparser

cfg = configparser.ConfigParser()
cfg.read("test.config",encoding="utf-8")

# 单个读取
s = cfg.get("MODE","method")
print(s)

# 读取所有sections
print(cfg.sections())

print(cfg.items("HAMIGUA"))