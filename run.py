#run.py

from flask import Flask,render_template,request,jsonify
from pusher import Pusher
import json

app = Flask(__name__)

pusher= Pusher(
	app_id = "442574",
	key = "dc8b02b3828c119a75ea",
	secret = "39834eadbe283ebc4f69",
	cluster = "ap2",
	ssl=True
)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/add-todo',methods=['POST'])
def addTodo():
	data = json.loads(request.data) #Loading data from the view to the controller
	pusher.trigger('todo','item-added',data) #Creating a pusher trigger to communicate over the 'todo' channel and sending 'data' over it
	return jsonify(data) #Returning jsonified data to the view

@app.route('/remove-todo/<removed_id>')
def removeTodo(removed_id):
	data = {'id':removed_id} #The parameter passed is first stored into a dictionary
	pusher.trigger('todo','item-removed',data) #Triggering an event to remove the element
	return jsonify(data) #Sending the modified data to the view

@app.route('/update-todo/<updated_id>',methods=['POST'])
def updateTodo(updated_id):
	data = {
	'id':updated_id,
	'completed':json.loads(request.data).get('completed',0)

	}
	pusher.trigger('todo','item-updated',data)
	return jsonify(data)


if __name__ == '__main__':
	app.run(debug=True)
	

