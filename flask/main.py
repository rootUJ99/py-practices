import json
from flask import Flask, make_response, request, url_for 

app = Flask(__name__)

map = {
    "application type": "flask",
    "language": "python"
}

@app.get("/hello/<string:username>")
def hello(username):
    new_map = dict(**map, abc="pqr")
    user = request.args.get("username")
    res = make_response(new_map)
    res.headers.set("Access-Control-Allow-Origin", "*")
    print(user)
    return res 

@app.get("/sayhello")
def sayhello():
    return {
        "hello": "hello from python and flask" 
    }
