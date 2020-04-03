from flask import Flask, request
import json, os

app = Flask(__name__)

@app.route('/')
def ApiEndpoint():
    #os.environ['']
    pass