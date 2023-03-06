# -*- coding: utf-8 -*-
import json
import random
import requests
import vk_api
import time
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
import bs4
import datetime

from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

#import Sub
import news

def get_button (label, color, payload=" "):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def get_button_url (label, color, payload=" "):
    return {
        "action": {
            "type": "open_link",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def _clean_all_tag_from_str(string_line):
	result = ""
	not_skip = True
	for i in list(string_line):
		if not_skip:
			if i == "<":
				not_skip = False
			else:
				result += i
		else:
			if i == ">":
				not_skip = True
	return result

def new_sub (sub_id):
	global subs_ids
	#if not (sub_id in subs_ids):
	subs=open('subs.txt','a')
	subs.write('\n'+str(sub_id))
	subs.close()
	subs_ids.append(sub_id)
#hp=Sub.get_num(len('.'))

keyboard = {
    "one_time": False,
    "buttons": [

    [get_button(label="Подписаться на рассылку", color="positive")],
    [get_button(label="Новости", color="primary")],
    [get_button(label="Расписание учителей", color="primary")],
    [{
        "action": {
            "type": "open_link",
            "link": "https://vpkl33.ru/?avia_forced_reroute=1",
            "label": "Сайт лицея",
            "payload": "{}"
                    },
    },
    {
        "action": {
            "type": "open_link",
            "link": "https://www.instagram.com/maoy_pkl/",
            "label": "Наш Instagram",
            "payload": "{}"
                    },
    }]
    
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

keyboardSub = {
    "one_time": False,
    "buttons": [

    #[get_button(label="Подписаться на рассылку", color="positive")],
    [get_button(label="Новости", color="positive")],
    [get_button(label="Расписание учителей", color="primary")],
	[{
        "action": {
            "type": "open_link",
            "link": "https://vpkl33.ru/?avia_forced_reroute=1",
            "label": "Сайт лицея",
            "payload": "{}"
                    },
    },
    {
        "action": {
            "type": "open_link",
            "link": "https://www.instagram.com/maoy_pkl/",
            "label": "Наш Instagram",
            "payload": "{}"
                    },
    }]
    
	]
}
keyboardSub = json.dumps(keyboardSub, ensure_ascii=False).encode('utf-8')
keyboardSub = str(keyboardSub.decode('utf-8'))

#token = '0a47706f40db67901d39fe32114970fa1081f8fbfbb32084a875814956348623bb67f5cbc2285d95707b4'
token = 'c3fbda8c673ad09c5f51df03235d1d6ffc81018bf7526adaf9940b3a2960c04371503866d7f27022346a4'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(-2147483648, +2147483648) })

def get_name(user_id):
        request = requests.get("https://vk.com/id" + str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = _clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

def photo_adder(user_id, text, photo):
    vk.method("messages.send", {"peer_id": user_id, "message": text, "attachment": photo, "random_id": random.randint(-2147483648, +2147483648)})

link = 'https://vpkl33.ru/news/'

subs_ids=[]
subs=open('subs.txt','r')
while True:
	string=subs.readline()
	if not string: break
	subs_ids.append(int(string))
subs.close()

i=0
get_news=''

while True:
    try:
        for event in longpoll.listen():
        # Если пришло новое сообщение
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.to_me and event.to_me:
                # Если оно имеет метку для бота
                if event.to_me:
                    Time=datetime.datetime.now()
                    subs_ids=[]
                    subs=open('subs.txt','r')
                    while True:
                        string=subs.readline()
                        if not string: break
                        subs_ids.append(int(string))
                    subs.close()

                    request = event.text

                    print('>>> '+ str(Time.hour)+':'+str(Time.minute) + ' Main: ' + str(get_name(event.user_id))+' : '+str(event.text))
                    with open ('logs.txt','a') as logs_file:
                        logs_file.write('\n'+'>>> '+ str(Time.hour)+':'+str(Time.minute) + ' Main: ' + str(get_name(event.user_id))+' : '+str(event.text))

                    if request == "Тест":
                        vk.method("messages.send", {"peer_id": event.user_id, "message": "Сам ты тест, а я рабочий",'random_id': random.randint(-2147483648, +2147483648) })
                    elif request == "Подписаться на рассылку":
                        if not (event.user_id in subs_ids):
                            new_sub(event.user_id)
                            if event.user_id in subs_ids:
                                vk.method("messages.send", {"peer_id": event.user_id, "message": "Вы успешно подписались на рассылку новостей лицея","keyboard": keyboardSub,'random_id': random.randint(-2147483648, +2147483648) })
                        else:
                            vk.method("messages.send", {"peer_id": event.user_id, "message": "Вы уже подписались на рассылку", "keyboard": keyboardSub,'random_id': random.randint(-2147483648, +2147483648) })

                    elif request == "Новости":
                        vk.method("messages.send", {"peer_id": event.user_id, "message": news.get_news(link,""),'random_id': random.randint(-2147483648, +2147483648) })
                    elif request == "Расписание учителей":
                        photo_adder (event.user_id,"Расписание учителей","photo-40458545_457239197")
                    elif request == "Запусти гуся":
                        for goo in range(1,10):
                            goose.go_goose_go ("217015796")
                    elif (request == "Начать") or (request == "начать") or (request == "Start") or (request == "start"):
                        vk.method("messages.send", {"peer_id": event.user_id, "message": "Меню", "keyboard": keyboard, 'random_id': random.randint(-2147483648, +2147483648)})
                    elif request == "Сайт":
                        vk.method("messages.send", {"peer_id": event.user_id, "message": "Меню", "keyboard": keyboard, 'random_id': random.randint(-2147483648, +2147483648)})
                    else:
                        if '!warning! 1654773' in request:
                            for k in subs_ids:
                                vk.method("messages.send", {"peer_id": k, "message": request[17:],"random_id": random.randint(-2147483648, +2147483648) })
    except requests.exceptions.ReadTimeout:
        print('>>> '+ str(Time.hour)+':'+str(Time.minute) + ' ')
        with open ('logs.txt','a') as logs_file:
            logs_file.write('\n'+'>>>  Опять заскучал')
'''					
elif request == "Send":
						for i in range(10):
							Sub.smth(hp)
'''
'''
print('>>> '+ str(Time.hour)+':'+str(Time.minute) + ' ')
with open ('logs.txt','a') as logs_file:
			logs_file.write('\n'+)
'''