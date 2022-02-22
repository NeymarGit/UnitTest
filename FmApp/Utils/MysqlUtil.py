"""数据库连接"""

import pymysql
from FmApp.Utils.ConfigUtil import ConfigUtil


class MysqlUtil:

    # 查询获取一条数据
    def doMysqlOne(self,sql):
        str = ConfigUtil().doConfig("D:\Python\Study\FmApp\Configs\case.config","MYSQL","connect_info")
        connect_info = eval(str)
        # 创建连接
        conn = pymysql.connect(**connect_info)
        # 创建游标
        curses = conn.cursor()
        # 执行sql
        curses.execute(sql)
        # 获取结果
        data = curses.fetchone() # 只获取一条数据，元组形式

        curses.close()
        conn.close()

        return data

    # 查询获取所有数据
    def doMysqlAll(self,sql):
        str = ConfigUtil().doConfig("D:\Python\Study\FmApp\Configs\case.config","MYSQL","connect_info")
        connect_info = eval(str)
        # 创建连接
        conn = pymysql.connect(**connect_info)
        # 创建游标
        curses = conn.cursor()
        # 执行sql
        curses.execute(sql)
        # 获取结果
        data = curses.fetchall() # 获取所有数据，列表嵌套元祖形式

        curses.close()
        conn.close()

        return data


if __name__ == '__main__':
    sql = "select * from member_info"
    res = MysqlUtil().doMysqlOne(sql)
    print(res)
    print(res[1])