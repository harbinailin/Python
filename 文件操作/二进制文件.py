import json

content = [120, 123.21, 'true']
filename = "ywk20202188.json"
with open(filename, 'w') as f:
    json.dump(content, f)

with open(filename) as f:
    content = json.load(f)
print(content)
