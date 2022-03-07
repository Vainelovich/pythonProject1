import requests
import json

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)
#
# print(type(texts))
#
# for text in texts:
#     print(text[:150], '\n')

r = requests.get('https://api.github.com')

d = json.loads(r.content)

print(type(d))
print(d['following_url'])

data = {'key': 'value'}

r = requests.post('https://httpbin.org/post', json = json.dumps(data))

print(r.content)