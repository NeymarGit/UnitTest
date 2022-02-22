'''封装get和post请求
    传URL和data，返回消息实体'''

import requests


class HtppRequest:

    def get_request(self, url, cookies=None):
        res = requests.get(url, cookies=cookies)
        return res

    def post_request(self, url, data, cookies=None):
        res = requests.post(url, data, cookies=cookies)
        return res


if __name__ == '__main__':
    login_url = "http://localhost:8080/jenkins/j_acegi_security_check"
    body = {"j_username": "liuyanghe", "j_password": "123456"}
    rsp = HtppRequest().post_request(login_url, body)
    print(rsp.headers)
    print(rsp.request.headers)

    myView_url = "http://localhost:8080/jenkins/me/my-views"
