import requests

param = {'Username': 'weixin_45906196'}
r = requests.get('https://www.csdn.net/community/toolbar-api/v1/get-user-info', params=param)
print(r.status_code)
# 获取请求内容
print(r.url)
# 获取相应内容
print(r.text)
print(r.json())
print(r.headers)