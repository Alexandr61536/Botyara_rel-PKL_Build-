# -*- coding: utf-8 -*-
import json
import random
import requests
import vk_api
import datetime
from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

import news
import time
def main():
	Time=datetime.datetime.now()
	i=0
	#token = '0a47706f40db67901d39fe32114970fa1081f8fbfbb32084a875814956348623bb67f5cbc2285d95707b4'
	token = 'c3fbda8c673ad09c5f51df03235d1d6ffc81018bf7526adaf9940b3a2960c04371503866d7f27022346a4'
	vk = vk_api.VkApi(token=token)
	link = 'https://vpkl33.ru/news/'
	current_message=news.get_news(link)
	while True:
		Time=datetime.datetime.now()
		time.sleep(10)
		subs_ids=[]
		subs=open('subs.txt','r')
		while True:
			string=subs.readline()
			if not string: break
			subs_ids.append(int(string))
		subs.close()

		print('>>> '+str(Time.hour)+':'+str(Time.minute)+' Sender: собрал id подписчииков из файла в список')
		with open ('logs.txt','a') as logs_file:
			logs_file.write('\n'+'>>> '+str(Time.hour)+':'+str(Time.minute)+' Sender: собрал id подписчииков из файла в список')
		
		if news.get_news(link, current_message)!=current_message:

			print('>>> '+str(Time.hour)+':'+str(Time.minute)+' Sender: увидел обловление на сайте')
			with open ('logs.txt','a') as logs_file:
				logs_file.write('\n'+'>>> '+str(Time.hour)+':'+str(Time.minute)+' Sender: увидел обловление на сайте')

			for k in subs_ids:
				vk.method("messages.send", {"peer_id": k, "message": news.get_news(link,current_message),'random_id': random.randint(-2147483648, +2147483648) })

			print('>>> '+str(Time.hour)+':'+str(Time.minute)+ ' Sender: разослал новость')
			with open ('logs.txt','a') as logs_file:
				logs_file.write('\n'+'>>> '+str(Time.hour)+':'+str(Time.minute)+ ' Sender: разослал новость')

			current_message=news.get_news(link,current_message)

			print('>>> '+str(Time.hour)+':'+str(Time.minute)+ ' Sender: обновил макет сообщения')
			with open ('logs.txt','a') as logs_file:
				logs_file.write('\n'+'>>> '+str(Time.hour)+':'+str(Time.minute)+ ' Sender: обновил макет сообщения')
			print(current_message)
			with open ('logs.txt','a') as logs_file:
				logs_file.write('\n'+current_message)
main()