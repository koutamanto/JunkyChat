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
    with open("data.json","r") as f:
        view_data = json.load(f)
    print(view_data)
    return view_data

@app.route("/send",methods=["POST"])
def send():
    sended_data = request.get_data()
    print(sended_data)
    datas_list.append(sended_data)
    datas = {"datas":datas_list}
    print(datas)
    with open("data.json","w") as f:
        json.dump(datas, f, indent=4)
    return "[success:]" + sended_data + "sent"

if __name__ == "__main__":
    app.run(debug=True)
