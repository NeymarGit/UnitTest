"""
request工具类
"""


import json
import requests

class RequestUtil:

    def __init__(self,url,body = None,headers = None,cookies = None):
        self.url = url
        self.headers = headers
        self.body = body
        self.cookies = cookies

    def requestGet(self):
        response = requests.get(self.url,headers = self.headers,cookies = self.cookies)
        return response

    def requestPost(self):
        response = requests.post(self.url,data = self.body,headers = self.headers,cookies = self.cookies,verify = False)
        return response


if __name__ == '__main__':
    loginUrl = "https://fmapp.chinafamilymart.com.cn/api/app/login"
    headers = {"deviceId": "CD9FD298-D8BD-4226-B78A-9073F6FC6D1G","Content-Type": "application/json"}
    data = {"mobile":"13262213021","verifyCode":"198258","openChannelCd":"1","newVersion":"true","openId":"","distinctId":"CD9FD298-D8BD-4226-B78A-9073F6FC6D1G","grantTypeCd":"1","jpushId":"101d855909e851a0721","unionId":""}
    res = RequestUtil(loginUrl,json.dumps(data),headers).requestPost()  # bug:body要转化为json格式，不然解析报错
    print(res.status_code)
    print(res.json())
    print(res.json()["code"])
    # print(res.json()["data"]["token"])