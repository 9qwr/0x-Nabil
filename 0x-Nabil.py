import requests
from bs4 import BeautifulSoup
import re,json
import os
from time import sleep
from colorama import Fore
print('''
┊┊╭╮╭╮┊┊┊┊┊┊┊┊
┊┊┊┃┃┃┃┊┊┊┊┊┊┊
┊┊┊┃┃┃┃┊┊┊╭━━━
┊┊╭┛┗┛┗╮┊╭╯Welcome
┊┊┃┈▆┈▆┃┊┃To Download storys snapchat!
┊┊┃┈┈▅┈┃┊╰┳━━━ Developer : @hyy_yy > kaito 
┊┊┃┈╰┻╯┃━━╯┊┊┊ Support : @iictt | 24h
--------
~ My Telegram > :https://t.me/ik48x
~ By : kaito
''')
class daddy_kaito():
	def __init__(self):
		print('________'*5)
		self.kaito = input('[?] Enter Username :')
		urlw = f'https://story.snapchat.com/@{self.kaito}'
		print(urlw)
		self.headers = {
			"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1",
			}
		self.r = requests.get(urlw, headers = self.headers)
		self.download()
	def download(self):
		dum = BeautifulSoup(self.r.content, "html.parser")
		snap = dum.find_all("script")[3].string.strip()
		self.data = json.loads(snap)
		try:
			bitmoji = self.data["props"]["pageProps"]["userProfile"]["publicProfileInfo"]["snapcodeImageUrl"]
			bio = self.data["props"]["pageProps"]["userProfile"]["publicProfileInfo"]["bio"]
			print(f'')
		except KeyError:
			bitmoji = self.data["props"]["pageProps"]["userProfile"]["userInfo"]["snapcodeImageUrl"]
			bio = self.data["props"]["pageProps"]["userProfile"]["userInfo"]["displayName"]
		print(Fore.RED+f'bio : @{self.kaito} -->'	+bio,'\n\n')
		print(Fore.RED+f'bitmoji : @{self.kaito} -->'	+bitmoji,'\n\n')
		print('_______'*6,'\n')
		try:
			for i in self.data["props"]["pageProps"]["story"]["snapList"]:
				file_url = i["snapUrls"]["mediaUrl"]
				print(file_url)
				if file_url == "":
					print("There is a Story but no URL is provided by Snapchat.")
					continue
				r = requests.get(file_url, stream=True, headers=self.headers)
				print(Fore.CYAN+'Wait loading..')
				if "image" in r.headers['Content-Type']:
					file_name = r.headers['ETag'][12] + ".jpeg"
					print(file_name)			
				elif "video" in r.headers['Content-Type']:
					file_name = r.headers['ETag'][12] + ".mp4"
					print(file_name)
				if os.path.isfile(file_name) :
					continue
				
				sleep(0.3)		
				if r.status_code == 200:
					with open(file_name, 'wb') as f:
						for chunk in r:
							f.write(chunk)
				else:
					print(Fore.RED+"Cannot make connection to download media !. support on Telegram @iictt")

		except KeyError:
			print(Fore.RED+"An error occurred and the user story was not found.  Contact support on Telegram @iictt ")
		else:
			print(Fore.GREEN+"\nDownload all snaps completed successfully.[✅]")
daddy_kaito()		
