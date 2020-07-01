import requests
from bs4 import BeautifulSoup
class Login():
	def __init__(self,session,username,password):
		self.username=username
		self.password=password
		self.session=session
	def get_viewstate(self):
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
		"DNT":"1"
		}
		self.session.headers.update(headers)
		r=self.session.get("https://edexcelonline.pearson.com/Account/Login.aspx")
		soup=BeautifulSoup(r.text,features="html.parser")
		self.viewstate=soup.find(id="__VIEWSTATE")["value"]
		self.ev=soup.find(id="__EVENTVALIDATION")["value"]
	def generate_payload(self):
		payload={
			"__VIEWSTATE":self.viewstate,
			"__EVENTVALIDATION":self.ev,
			"ctl00$DefaultContentHolder$txtUsername":self.username,
			"ctl00$DefaultContentHolder$txtPassword":self.password,
			"ctl00$DefaultContentHolder$btnLogin":"Log in"
		}
		self.payload=payload
	def get_sptoken(self):
		self.session.post("https://edexcelonline.pearson.com/Account/Login.aspx",data=self.payload)
	def start(self):
		self.get_viewstate()
		self.generate_payload()
		self.get_sptoken()
#		print(self.session.cookies)
		return self.session