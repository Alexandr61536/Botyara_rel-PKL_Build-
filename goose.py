# -*- coding: utf-8 -*-
import json
import random
import requests
import vk_api
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

token = "f32ba8fc8e1fa7151c5c27d5a51dc0ba37b400da59919eb0a833ac5c5679bfcb86de215b310e1ff46f1ef"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(-2147483648, +2147483648) })

def go_goose_go (user_id):
    write_msg(user_id, "ЗАПУСКАЕМ\n░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░\n▄███▀░◐░░░▌░░░░░░░\n░░░░▌░░░░░▐░░░░░░░\n░░░░▐░░░░░▐░░░░░░░\n░░░░▌░░░░░▐▄▄░░░░░\n░░░░▌░░░░▄▀▒▒▀▀▀▀▄\n░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄\n░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄\n░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄\n░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄\n░░░░░░░░░░░▌▌▌▌░░░░░\n░░░░░░░░░░░▌▌░▌▌░░░░░\n░░░░░░░░░▄▄▌▌▄▌▌░░░░░\nзапускаем гуся работяги")