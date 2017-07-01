#-*- coding: utf-8 -*-

## Module Import ##
from __future__ import print_function
import json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import httplib2
import os
import datetime
import requests
from urlparse import urlsplit
import urllib2
from os.path import basename

app = Flask(__name__)

@app.route("//message", methods=['GET', 'POST'])
@app.route("/message", methods=['GET', 'POST'])

def message():
    # User Talk Infomation
    userRequest = json.loads(request.get_data())
    print('userRequest :', userRequest)
    insert_type = userRequest['type'].encode('utf-8')
    print('insert_type :', insert_type)
    user_key = userRequest['user_key'].encode('utf-8')
    print('user_key :', user_key)

    content = userRequest['content'].encode('utf-8')
    print('content :', content) 

    return """{"message": {"text":""" + '"' + content + '"' + """},"keyboard": {  "type": "text","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""
    
      
@app.route("//keyboard", methods=['GET', 'POST'])
@app.route("/keyboard", methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
