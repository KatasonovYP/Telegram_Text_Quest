# -*- coding: utf-8 -*-
import boto3
import os, sys
import requests
import random
import json

from Send import *



with open('Story.json', 'r', encoding='utf-8') as fh:
    data = json.load(fh)



def start(act, user_id, text):
    
    if act == 'prompt' and text != 'костюмы':
        text = 'не костюмы'
    
    if act == 'riddle' and text != 'комок':
        text = 'не комок'
    
    if text in data[act]:
        for reply in data[act][text]["text"]:
            send_message(user_id, data[act][text]["text"][reply])
    else:
        send_message(user_id, "Хм, кажется, где-то ошибка...")
    
    if act == 'turn_back' and text == 'обернуться':
        send_photo(user_id, 'https://drive.google.com/file/d/1uacj9Lyxbyuw81nNKSYUTaTTLoyDP7iP/view?usp=sharing')
        send_message(user_id, "Действия: \n\n> Тёплые слова\n> Моргнуть")
    
    next_act = data[act][text]['next_act']
    return next_act