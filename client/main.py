import sys, tkinter, json, requests
from datetime import datetime

user_name = "KJunkie"

def disp_strings(entry_v):
    string = entry_v.get()
    print(string)

def send(event):
    msg = event
    print(msg)
    send_date = datetime.now()
    data = json.dumps({"msg":"["+str(send_date)+"] "+"["+user_name+":] "+msg})
    res = requests.post('https://junkychat.herokuapp.com/send',data=data)
window = tkinter.Tk()

window.geometry("400x300")
window.title("JunkyChat")

canvas = tkinter.Canvas(background="#2f4f4f", width=400, height=300)
canvas.place(x=200, y=150, anchor=tkinter.CENTER)

v = tkinter.StringVar() # Entryの入力を受け取るのに必要
entry = tkinter.Entry(canvas, width=30, textvariable=v)
entry.place(x=200, y=70, anchor=tkinter.CENTER)

label = tkinter.Label(canvas, text="ここに入力結果を表示")
label.place(x=200, y=220, anchor=tkinter.CENTER)

button = tkinter.Button(canvas, text="入力文字列を表示", command=lambda:disp_strings(v))
button.place(x=200, y=150, anchor=tkinter.CENTER)
window.bind('<Return>', send)
window.mainloop()