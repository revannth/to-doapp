#config.py
from pusher import Pusher

DEBUG = True

# configure pusher object
    pusher = Pusher(
      app_id='442574',
	  key='dc8b02b3828c119a75ea',
	  secret='39834eadbe283ebc4f69',
	  cluster='ap2',
	  ssl=True
    )
