# -*- coding: utf-8 -*-
import boto3
import json
import os, sys
import requests
import random

from Game import *
from Send import *
from Table import *


 
with open('Format.json', 'r', encoding='utf-8') as fh:
    form = json.load(fh)



def point(event, context):
    
    print(event)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users')
    
    user_id = event['message']['from']['id']
    text = event['message']['text']
    text = text.lower()
    
    if text == '/start':
        act = 'start'
    else:
        act = get_act(event)
    
    if act in form and text in form[act]:
        text = form[act][text]
    
    act = start(act, user_id, text)
    add_user(event, act)
