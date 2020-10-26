import requests,json,time

b_msg = ""
while True:
    time.sleep(3)
    msg = requests.get('https://junkychat.herokuapp.com/view').text
    if msg != b_msg:
        for data in json.loads(msg)["datas"]:
            data["msg"]
        print()
    b_msg = msg