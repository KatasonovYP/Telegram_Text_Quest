# -*- coding: utf-8 -*-
import boto3
import requests
import random
import json
import os, sys



my_token = "1400622989:AAFKL_4MCwwHtuIsYBWng0QczjoALbBO44g"



def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, data=data)
    print(r.json())



def send_photo(chat_id, photo):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendPhoto"
    )
    data = {
        "chat_id": chat_id,
        "photo": photo
    }
    r = requests.post(url, data=data)
    print(r.json())



def send_media_group(chat_id, media):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendMediaGroup"
    )
    data = {
        "chat_id": chat_id,
        "media": json.dumps(media)
    }
    r = requests.post(url, data=data)
    print(r.json())



def delete_message(chat_id, message_id):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="deleteMessage"
    )
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
    }
    r = requests.post(url, data=data)
    print(r.json())
    
 
    
def send_poll(chat_id, question, options):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendPoll"
    )
    data = {
        "chat_id": chat_id,
        "question": question,
        "options": json.dumps(options)
    }
    r = requests.post(url, data=data)
    print(r.json())
    