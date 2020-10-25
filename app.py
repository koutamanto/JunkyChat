# coding: utf-8
import requests
from bs4 import BeautifulSoup
from flask import Flask,request,render_template,redirect,url_for
import time,json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/view")
def view():
    with open("/static/data.json","r") as f:
        view_data = json.load(f)
    print(view_data)
    return view_data
@app.route("/send",method=["POST"])
def send():
    sended_data = request.get_data()
    print(sended_data)
    with open("/static/data.json","w") as f:
        json.dump(sended_data, f, indent=4)

if __name__ == "__main__":
    app.run(debug=True)
