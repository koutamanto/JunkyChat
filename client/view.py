import requests,json,time

b_msg = ""
while True:
    time.sleep(3)
    msg = requests.get('https://junkychat.herokuapp.com/view').text
    if msg != b_msg:
        print(json.loads(msg)["msg"])
    b_msg = msg