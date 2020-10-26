import sys, tkinter, json, requests
from datetime import datetime

user_name = "KJunkie"

def disp_strings(entry_v):
    string = entry_v.get()
    print(string)

def send(entry_v):
    msg = entry_v.get()
    print(msg)
    send_date = datetime.now()
    data = json.dumps({"msg":"["+str(send_date)+"] "+"["+user_name+":] "+msg})
    res = requests.post('https://junkychat.herokuapp.com/send',data=data)
    view("a")
def view(event):
    msg_list = []
    ret_msg = ""
    msgs = requests.get("https://junkychat.herokuapp.com/view").text
    msgs = eval(msgs)["datas"]
    print(msgs)
    for msg in msgs:
        print(msg)
        ret_msg = ret_msg + "\n" + msg["msg"]
    print(ret_msg)
    label["text"] = ret_msg
window = tkinter.Tk()

window.geometry("1000x750")
window.title("JunkyChat")

canvas = tkinter.Canvas(background="#343a40", width=1000, height=750)
canvas.place(x=500, y=376, anchor=tkinter.CENTER)

v = tkinter.StringVar() # Entryの入力を受け取るのに必要
entry = tkinter.Entry(canvas, width=30, textvariable=v)
entry.place(x=500, y=175, anchor=tkinter.CENTER)

label = tkinter.Label(canvas, text="メッセージ")
label.place(x=500, y=550, anchor=tkinter.CENTER)

button = tkinter.Button(canvas, text="送信", command=lambda:send(v))
button.place(x=500, y=375, anchor=tkinter.CENTER)

window.bind("<Key-r>", view)
window.mainloop()