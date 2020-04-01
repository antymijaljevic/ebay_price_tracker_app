#!/usr/bin/python3
#written by antymijaljevic@gmail.com

import requests
from bs4 import BeautifulSoup
import os
import smtplib
import time


os.system('clear')

URL = 'https://www.ebay.ie/itm/Lenovo-Thinkpad-P1-15-6-i7-8850H-HEX-4-3GHz-16GB-RAM-512GB-SSD-IT-20MES00V17/223890089169?hash=item3420e3a4d1:g:QSsAAOSwyWFeNh1m'

headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

def get_price():
	page = requests.get(URL, headers = headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id ='itemTitle').get_text()
	cutTitle = title[16:80]

	price = soup.find(id = 'prcIsum').get_text()
	cutPrice = price[1:6].replace(',','')
	cutPrice = int(cutPrice)

	print(color.BOLD + "Item title: " + color.END + color.RED + cutTitle + color.END)
	print(color.BOLD + "Current price: " + color.END + color.RED + str(cutPrice) + " £" + color.END)

	if (cutPrice < 1125):
		send_email()


def send_email():
	#server set up
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	#log in and mail
	server.login('antymijaljevic@gmail.com', 'xxx')
	subject = 'Price fell down!'
	body = 'Check the Ebay price on link https://www.ebay.ie/itm/Lenovo-Thinkpad-P1-15-6-i7-8850H-HEX-4-3GHz-16GB-RAM-512GB-SSD-IT-20MES00V17/223890089169?hash=item3420e3a4d1:g:QSsAAOSwyWFeNh1m'
	msg = f"subject: {subject}\n\n{body}"
	server.sendmail(
		'antymijaljevic@gmail.com',
		'ante.mijaljevic2017@gmail.com', msg
	)
	print("The E-mail has been sent!")
	server.quit()

while True:
	get_price()
	time.sleep(60*60)
	os.system('clear')
