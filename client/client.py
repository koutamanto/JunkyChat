import requests,json

data = json.dumps({"msg":"Hey"})
res = requests.post('https://junkychat.herokuapp.com/send',data=data)
print(res)
print(res.text)