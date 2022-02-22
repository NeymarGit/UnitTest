import requests

# url = "http://apis.juhe.cn/fapig/football/query?key=c8a539e894ac3d89795e182056a85377&type=xijia"
# # data = {"type":"fajia","key":"c8a539e894ac3d89795e182056a85377"}
# response = requests.get(url,verify = False)
# print(response.status_code)
# print(response.headers)
# print(response.text)
#
# url = "https://apis.juhe.cn/fapig/football/query"
# data = {"type":"fajia","key":"c8a539e894ac3d89795e182056a85377"}
# res = requests.post(url,data,verify = False)
# print(res.text)
# print(res.json())


# 登录接口
url_bulid = "http://localhost:8080/jenkins/j_spring_security_check"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
data ={"j_username": "liuyanghe",
    "j_password":"123456"}
response = requests.post(url_bulid, data=data)
print(response.status_code)
print("请求头信息",response.request.headers)
print("响应头信息",response.headers)
# print("响应体信息",response.text)
# print("响应cookies",response.cookies)
# # # 截取登录后返回的cookie
cookie_respone = response.headers["Set-Cookie"][:44]
print(cookie_respone)

print("____________________")


# 构建接口
req = requests.get('http://localhost:8080/jenkins/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)', auth=("liuyanghe", "123456"))
print(req.text)
crumb = req.text[14::]
print(crumb)
print(req.headers)
req_cookie= req.headers["Set-Cookie"][:44]
print(req_cookie)
url_bulid = "http://localhost:8080/jenkins/job/TOMS/build"
# 拼接请求接口需要的cookie
cookie_request = req_cookie + " screenResolution=1920x1080"
print(cookie_request)
head = {"Cookie":cookie_request,"Jenkins-Crumb":crumb}
# data = {"Jenkins-Crumb":crumb}
res = requests.post(url_bulid,headers = head)
print(res.status_code)
print("请求头",res.request.headers)
print("请求体",res.request.body)
print("响应头",res.headers)
print("响应体",res.text)