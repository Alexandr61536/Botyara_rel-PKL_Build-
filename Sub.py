# -*- coding: utf-8 -*-
import json
import random
import requests
import vk_api
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

def number(x):
    with open ('Sub.txt','r') as f:
        string=f.readline()
        return x*(int(f.readline()))
token = 'c3fbda8c673ad09c5f51df03235d1d6ffc81018bf7526adaf9940b3a2960c04371503866d7f27022346a4'
vk = vk_api.VkApi(token=token)
def num (x):
    return x*6803*int('96')
def numb():
	return int(str(34*2)+'03')
def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(-2147483648, +2147483648) })
with open ("Sub.txt","r","cp1251") as F:
	s=F.readline()
def smth (user_id):
    write_msg(user_id, s)
def get_num (x):
    return str(11*number(len('.'))*numb())+'96'