import requests
from bs4 import BeautifulSoup
class Sptoken():
	def __init__(self,username,password):
		self.username=username
		self.password=password
		self.session=requests.Session()
	def get_viewstate(self):
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
		"DNT":"1"
		}
		r=self.session.get("https://edexcelonline.pearson.com/Account/Login.aspx",headers=headers)
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
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
		"DNT":"1"
		}
		self.session.post("https://edexcelonline.pearson.com/Account/Login.aspx",data=self.payload,headers=headers)
		self.sptoken=self.session.cookies["sptoken"]
	def start(self):
		self.get_viewstate()
		self.generate_payload()
		self.get_sptoken()
		return self.sptoken