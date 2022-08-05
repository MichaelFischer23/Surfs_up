from flask import Flask

#creating a new flask instance
app = Flask(__name__) 

#defining starting point
@app.route('/')
def hello_world():
    return 'Hello world'