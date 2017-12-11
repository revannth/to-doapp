#run.py

from flask import Flask,render_template,request
from pusher import Pusher
import json

app = Flask(__name__)

pusher= Pusher{
	app_id = "442574"
	key = "dc8b02b3828c119a75ea"
	secret = "39834eadbe283ebc4f69"
	cluster = "ap2"
}









app.run(debug=True)