# import os
try:
    open("__init__.py","w")
except Exception as e:
    print("错误信息为{}".format(e))
    file = open("error.txt","a",encoding="utf-8")
    file.write("\n"+str(e))
    file.close()
finally:
    print("不管上面报不报错，都会执行")