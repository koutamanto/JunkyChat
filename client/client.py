import requests,json

data = json.dumps({"msg":"oppai"})
res = requests.post('https://junkychat.herokuapp.com/send',data=data)
print(res)
print(res.text)