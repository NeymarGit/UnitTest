"""正则表达式"""

import re
from FmApp.Utils.Memory import Memory

class Regex:

    # 全部匹配，存在列表里面。如果有分组，以元祖的形式表达出来，列表嵌套元祖
    def re_findall(self, regex, str):
        result = re.findall(regex, str)
        return result

    def re_search(self, str):
        # 分组是为了取出user
        regex = '\$\{(.*?)\}'
        while re.search(regex, str):
            group = re.search(regex, str).group()
            group1 = re.search(regex, str).group(1)
            str = str.replace(group, getattr(Memory, group1))
        return str


if __name__ == '__main__':
    str = '{"username":"${user}","password":"1111"}'
    str_new = Regex().re_search(str)
    print(str_new)
