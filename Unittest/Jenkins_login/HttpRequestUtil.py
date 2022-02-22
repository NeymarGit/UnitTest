'''封装get和post请求
    传URL和data，返回消息实体'''

import requests


class HttpRequestUtil:
    def __init__(self,url,data = None,cookies = None):
        self.url = url
        self.data = data
        self.cookies = cookies


    def get_request(self):
        res = requests.get(self.url, cookies=self.cookies)
        return res

    def post_request(self):
        res = requests.post(self.url, data=self.data,  cookies=self.cookies)
        return res


if __name__ == '__main__':
    login_url = "http://localhost:8080/jenkins/j_spring_security_check"
    body = {"j_username": "liuyanghe", "j_password": "123456"}
    req = HttpRequestUtil(login_url, body)
    rsp = req.post_request()
    print(rsp.status_code)
    print(rsp.headers)
    print(rsp.text)
    cookie = rsp.headers.__contains__("Set-Cookie")
    print("cookie是：",rsp.cookies)
    print(rsp.request.headers)

