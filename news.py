import requests
import datetime
from bs4 import BeautifulSoup

def get_news (link, current_message):
	try:
		Time=datetime.datetime.now()
		r = requests.get(link).content
		soup = BeautifulSoup(r,'html.parser')
		items = soup.findAll('div',class_='av-heading-wrapper')
		links_ns=[]
		for item in items:
			links_ns.append({
				'title': item.find('h2',class_='post-title entry-title').get_text(strip=True),
				'text': item.find('h2',class_='post-title entry-title').find('a').get('href')
			})

		print('>>> '+str(Time.hour)+':'+str(Time.minute)+' News: Спарсил сайт, забил в массив')
		with open ('logs.txt','a') as logs_file:
			logs_file.write('\n'+'>>> '+str(Time.hour)+':'+str(Time.minute)+' News: Спарсил сайт, забил в массив')

		link2=links_ns[1]['text']
		r2=requests.get(link2).content
		soup2 = BeautifulSoup(r2,'html.parser')
		item = soup2.find('div',class_='entry-content')
		try:
			text=item.find('p').get_text(strip=True)
		except AttributeError:
			pass
		links_ns[1]['text']=text

		message=links_ns[1]['title']+'\n'+'\n'+text+'\n'+'\n'+link2
		
		print('>>> '+ str(Time.hour)+':'+str(Time.minute) +' News: сгенерировал сообщение')
		with open ('logs.txt','a') as logs_file:
			logs_file.write('\n'+'>>> '+ str(Time.hour)+':'+str(Time.minute) +' News: сгенерировал сообщение')

		return (message)
	except IndexError:
		print(list_ns)
		with open ('logs.txt','a') as logs_file:
			logs_file.write('\n'+str(list_ns))
		print('>>> '+ str(Time.hour)+':'+str(Time.minute) +' News: Снова не видит элемент, вернул current_message')
		with open ('logs.txt','a') as logs_file:
			logs_file.write('\n'+'>>> '+ str(Time.hour)+':'+str(Time.minute) +' News: Снова не видит элемент, вернул current_message')
		return current_message