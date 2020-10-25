# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask,request,render_template,redirect,url_for
import time,json

datas_list = []

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/view")
def view():
    datas = {"datas":datas_list}
    with open("data.json","r") as f:
        view_data = json.load(f)
    print(view_data)
    return str(view_data)

@app.route("/send",methods=["POST"])
def send():
    datas = {"datas":datas_list}
    sended_data = request.get_data().decode()
    print(sended_data)
    datas["datas"].append(sended_data)
    with open("data.json","w") as f:
        json.dump(datas, f, indent=4)
    return "[success:]" + sended_data + "sent"

if __name__ == "__main__":
    app.run(debug=True)
