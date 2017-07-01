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

# google transalation api key
api_key = "AIzaSyCCEf-PpInvuJ40BLCk9EaD8pJK2i1WieE"

firstMenu = ['안녕']

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

    # Master Of Jingbebot
    addiction = ""
    if user_key == 'V06qSR5ZGd2C':
        addiction = " , 현종님."
    
    content = userRequest['content'].encode('utf-8')
    print('content :', content) 

    cal_text = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "/", "*", "(", ")", "은", "는"]

    cal_flag = 0
    for i in range(0, len(content)):
        if not content[i] in cal_text:
            cal_flag += 1

    if cal_flag == 0:
        content = content.replace('은', '')
        content = content.replace('는', '')
        output = eval(content)
        
        return """{"message": {"text":""" + '"' + str(output).encode('utf-8') + addiction + '"' + """},"keyboard": {  "type": "text","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""


    elif content.find("번역") > -1:
        # spacing
        content = content.replace("번역", " 번역")
          
        trans_loc = content.rfind("번역")

        query = content[:trans_loc]

        trans = content[trans_loc:]

        lang_list = ["영어", "일본어", "일어", "프랑스어", "불어"]

        for i in range(0, len(lang_list)):
            if query.find(lang_list[i]) > -1:
                 print("yes")

        if query[-1:] == "을" or query[-1:] == "를":
            query = query[:-1]

        target_lang = "en" # default_lang

        if query.find("일본") > -1:
            print(query.find("일본"))
            query = query[:query.find("일본")]
            target = 'ja'
        elif query.find('프랑스') > -1:
            print(query.find("프랑스"))
            query = query[:query.find("프랑스")]
            target = 'fr'

        else:
            target = 'en'

        query = query.strip()
        url = 'https://translation.googleapis.com/language/translate/v2/?key=' + api_key + '&q=' + query + '&source=' + 'ko' + '&target=' + target
        get_url = requests.get(url)
        get_url_text = get_url.text

        # json loads
        json_loads = json.loads(get_url_text)
        output = json_loads['data']['translations'][0]['translatedText']
        output = output.replace("&#39;", "'")
        return """{"message": {"text":""" + '"' + output.encode('utf-8') + addiction + '"' + """},"keyboard": {  "type": "text","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""


    else:
        return """{"message": {"text":""" + '"' + content + '"' + """},"keyboard": {  "type": "text","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""
    
      
@app.route("//keyboard", methods=['GET', 'POST'])
@app.route("/keyboard", methods=['GET', 'POST'])


def key():
    return """{ "type" : "text", "buttons" : """+'["'+'","'.join(firstMenu)+'"]'+"""}"""
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)


