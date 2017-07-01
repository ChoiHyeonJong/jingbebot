#-*- coding: utf-8 -*-

from flask import Flask, request
import json
import requests

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

    open_url = 'https://maum.ai/api/dialog/svc-group/ask_mindslab/new'
    open_session = requests.post(open_url)
    open_session = open_session.json()
    session_id = str(open_session.get(u'id'))

    dialog_url = 'https://maum.ai/api/dialog/session/' + session_id + '/talk'
    data = {"message" : content, "language" :"kor"}

    dialog_response = requests.post(dialog_url, json=data)
    dialog_response = dialog_response.json()
    utter = dialog_response.get(u'utter')
   
    return """{ "message" : { "text" :""" + '"' + utter + '"' + """}}"""

if __name__ == "__main__":
    app.run()
