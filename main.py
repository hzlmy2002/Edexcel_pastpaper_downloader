import requests,getpass,time
import payload,login,retrieve,download
def main():
	subjects=payload.subject
	session=requests.Session()
	print("Tips: This program supports http proxy, you can enable this feature by setting the environment variable HTTP_PROXY or HTTPS_PROXY")
	print('For example: export HTTP_PROXY="http://127.0.0.1:8080"\n')
	print("Download the following exam series, enter the number")
	print("You can exit this program by entering ctrl+C at any time\n")
	while True:
		for i in range(len(subjects)):
			print(str(i+1)+"."+subjects[i])
		try:
			choice=input("\nYour choice: ")
			subject=subjects[int(choice)-1]
		except Exception:
			print("Please try again.\n")
			continue
		print("You have selected: "+subject)
		break
	print("Select the time range of the exam papers")
	print("Enter ctrl+C to exit")
	while True:
		try:
			from_date=int(input("From (Example:201306): "))
			to_date=int(input("To (Example:202001): "))
		except Exception:
			print("Please try again.\n")
			continue
		print("You have selected the time range "+str(from_date)+" to "+str(to_date)+"\n")
		if len(str(from_date)) ==6 and len(str(to_date)) == 6 and from_date <= to_date:
			break
		else:
			print("You have entered an invalied time range, please try again.")
	print("You can enter an optional keyword")
	keyword=input("Your keyword (N for none),default is none: ")
	if keyword == "N" or keyword =="" :
		keyword=""
		print("Your keyword is none")
	elif len(keyword) != 0:
		keyword=keyword.lower()
		print("Your keyword is: "+keyword)
	want_login=input("Some files require login to be downloaded,would you like to login? y/N: ").lower()
	if want_login == "y" or want_login == "yes":
		username=input("Username: ")
		password=getpass.getpass("Password: ")
		l=login.Login(session,username,password)
		session=l.start()
		download.download(session,subject,retrieve.retrieve(subject,keyword,from_date,to_date),login=True)
		return 0
	else:
		download.download(session,subject,retrieve.retrieve(subject,keyword,from_date,to_date),login=False)
		return 0

if __name__=="__main__":
	try:
		print("Edexcel pastpapper downloader v1.2")
		print("Copyright (C) 2020 Minyi_Lei hzlmy2002")
		print("All rights reserved")
		print("For project details,please check: https://github.com/hzlmy2002/edexcel_pastpaper_downloader\n")
		while True:
			main()
			print("\nProgram reset, you can now select another exam series")
			print("Enter ctrl+C to exit.\n")
			time.sleep(3)
	except KeyboardInterrupt:
		print("\nBye!")