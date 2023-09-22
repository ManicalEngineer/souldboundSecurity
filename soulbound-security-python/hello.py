import socket
import json
from flask import Flask, request, session, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<h1>Hello Erika! Wife of Mine!I love you!</h1>"

@app.route("/api/findtornadocash/")
def echo():
	request_data = request.args
	print(request_data)
	rtn_value = f"Address: {request.args.get('start_address')}"
	return rtn_value	

@app.route("/soulboundsecurity/")
def soulbound():
	return render_template("soulbound.html")

@app.route("/soulboundsecurity/verify/", methods=['POST',  'GET'])
def soulboundVerify():
	if request.method == "GET":
		request_message = request.args.get('message')
		request_UID = request.args.get('userID')
		return render_template("soulbound.html", message=request_message, userID=request_UID)
	else:
		data = request.json
		s = socket.socket()
		port = 65432
		ip = '127.0.0.1'
		s.connect((ip, port))
		data = json.dumps(data)
		s.send(data.encode())
		s.close()
		return "Success", 200
	

if __name__ == "__main__":
        app.run(host='0.0.0.0')
