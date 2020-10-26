# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask,request,render_template,redirect,url_for
import time,json

datas_list = []
rooms_list = []
datas = {}
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/create", methods=["POST"])
def create():
    roomname = request.get_data()
    datas.append({roomname:{"datas":[]}})
    return roomname
@app.route("/view")
def view():
    selectedroomname = request.args.get('selectedroomname', '')
    with open("data.json","r") as f:
        view_data = json.load(f)
    print(view_data[selectedroomname]["datas"])
    return str(view_data)

@app.route("/send",methods=["POST"])
def send():
    sended_data = request.get_data()
    sended_data = json.loads(sended_data)
    print(sended_data)
    datas_list.append(sended_data)
    datas[sended_data["roomname"]]["datas"] = datas_list
    print(datas)
    with open("data.json","w") as f:
        json.dump(datas, f, indent=4)
    return "[success:]" + sended_data + "sent"

if __name__ == "__main__":
    app.run(debug=True)
