import json

f = open('./groups.json')
data = json.load(f)
print(data)
f.close()
