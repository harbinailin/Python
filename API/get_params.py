import requests

content = {'page': '1', 'size': '20', 'businessType': 'lately', 'noMore': 'false', 'username': 'weixin_45906196'}
r = requests.get('https://blog.csdn.net/community/home-api/v1/get-business-list', params=content)
print(r.status_code)
print(r.url)
# 返回原始响应体
print(r.raw)
