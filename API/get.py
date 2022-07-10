import requests

r = requests.get('https://ailin.blog.csdn.net/')
# 返回状态码
print(r.status_code)
# 返回文本信息
print(r.text)

