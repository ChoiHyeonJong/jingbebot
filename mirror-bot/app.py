#-*- coding: utf-8 -*-

from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/keyboard', methods = ["GET", "POST"])
def key():
    return """{ "type" : "text" }"""

@app.route('/message', methods = ["GET", "POST"])
def message():
    talk_info = json.loads(request.get_data())
    print('talk_info :', talk_info)
    content = talk_info['content']
    print('contet :', content)

    return """{ "message" : { "text" :""" + '"' + content + '"' + """}}"""

if __name__ == "__main__":
    app.run()
