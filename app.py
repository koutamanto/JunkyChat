# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask,request,render_template,redirect,url_for,jsonify
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
    roomname = request.args.get("roomname")
    datas[roomname] = {"datas":[{"msg":"This is a new room!Enjoy!"}]}
    print(datas)
    with open("data.json","w") as f:
        json.dump(datas, f, indent=4)
    return roomname
@app.route("/rooms")
def rooms():
    with open("data.json","r") as f:
        rooms_data = json.load(f)
    return str(rooms_data.keys())

@app.route("/view")
def view():
    selectedroomname = request.args.get('selectedroomname','')
    with open("data.json","r") as f:
        view_data = json.load(f)
    print(view_data[selectedroomname]["datas"])
    return str(view_data[selectedroomname]["datas"])

@app.route("/send",methods=["POST"])
def send():
    msg = json.loads(request.get_json())["msg"]
    roomname = json.loads(request.get_json())["roomname"]
    datas_list.append(msg)
    datas[roomname]["datas"] = datas_list
    print(datas)
    with open("data.json","w") as f:
        json.dump(datas, f, indent=4)
    return "[success:]" + msg + "sent"

if __name__ == "__main__":
    app.run(debug=True)
