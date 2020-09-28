from flask import Flask
from flask import request
from flask import Response
import json

app = Flask(__name__) 
#@就是 decorator 裝飾器 / 修飾器
#反正就是寫上去
@app.route("/") # 就是一般而言的首頁
def hello():
    return "Hello, World!"

    USERS = {}
#申請USER
@app.route("/CreateUsername",methods=["GET"]) 
def CreateUsername():

    cuser = request.get_json()
    print("HELLO",cuser.get("username"))
    username=cuser.get("username")
    
    if not username:
        return Response(
            status=400,
            response=json.dumps({"errmsg": "need username"}, indent=4),
            mimetype="application/json"
            )

    if username in USERS:
        return Response(
            status=406,
            response=json.dumps({"errmsg":"Sorry,User exists"},indent=4),
            mimetype="application/json"
        )
    #先檢查有有沒有填名字，以及有無重複 都沒有才新增到USER    
    USERS[username]= 0 #如何新增的 再問一次...
    
    return Response(
            status=200,
            response=json.dumps({"msg":username}, indent=4),
            mimetype="application/json"
        )

@app.route("/balance/<username>", methods=["GET"])
def balance(username):
    print("HI",username)
    #先檢查 使否有這個USER
    if not username in USERS:
        return Response(
            status=406,
            response=json.dumps({"errmsg": "NG, user not exists"}, indent=4),
            mimetype="application/json"
        )
    ans = {
        "username": username,
        "balance": USERS[username]
        }
    return Response(
            status=200,
            response=json.dumps(ans, indent=4),
            mimetype="application/json"
        )

@app.route("/deposit/<username>", methods=['POST'])
def deposit(username):
    if username not in USERS:
        return Response(
            status=404,
            response=json.dumps({
                "msg": "user not found"
            }),
            mimetype="application/json",
        )
    cuser = request.get_json()
    amount = cuser.get("amount")
    if not amount:
        return Response(
            status=400,
            response=json.dumps({
                "msg": "need amount"
            }),
            mimetype="application/json",
        )
    
    USERS[username] += amount

    return Response(
        status=200,
        response=json.dumps({
            "msg": "deposit OK",
        }),
        mimetype="application/json",
    )

@app.route("/get", methods=['GET'])
def EchoServerPort():
    arg = request.get_json()
    
    
    
   
    
    return  Response(
            status=400,
            response=json.dumps({"args": arg['args'],
                                "headers":arg['headers'],
                                "origin":arg['origin'],
                                "url":arg['url'],
                                },indent=4),
            mimetype="application/json",
        )




if __name__ == "__main__":
    print("Start server")

    host = "0.0.0.0"  #開放給所有人都可以連 改localhost 就只有自己可以連
    port = 3456

    app.run(host=host, port=port,debug=True)
    print("Server shutdonw")