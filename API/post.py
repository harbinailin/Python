import requests

payload = {'username':'ailin', 'password':'123123'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)
