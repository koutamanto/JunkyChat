import requests,json
from datetime import datetime

user_name = "KJunkie"

while True:
    msg = input("type a message:")
    send_date = datetime.now()
    data = json.dumps({"msg":"["+str(send_date)+"] "+"["+user_name+":] "+msg})
    res = requests.post('https://junkychat.herokuapp.com/send',data=data)