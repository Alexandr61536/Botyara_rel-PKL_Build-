# -*- coding: utf-8 -*-
import json
import random
import requests
import vk_api
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

import goose

token = '0a47706f40db67901d39fe32114970fa1081f8fbfbb32084a875814956348623bb67f5cbc2285d95707b4'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(-2147483648, +2147483648) })

while True:
	for event in longpoll.listen():
    # Если пришло новое сообщение
		if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.to_me and event.to_me:
	        # Если оно имеет метку для меня( то есть бота)
			if event.to_me:
	            # Сообщение от пользователя
				request = event.text
				if request == "Тест":
						vk.method("messages.send", {"peer_id": event.user_id, "message": "Сам ты тест, а я рабочий",'random_id': random.randint(-2147483648, +2147483648) })
				elif request == "Запусти гуся":
					goose.go_goose_go ("217015796")