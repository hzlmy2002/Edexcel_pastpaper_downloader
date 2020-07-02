import requests,getpass
import payload,login,retrieve,download
def main():
	subjects=payload.subject
	session=requests.Session()
	print("Download the following exam series,enter the number")
	print("Enter q to exit\n")
	while True:
		no=1
		for i in subjects:
			print(str(no)+"."+i)
			no+=1
		try:
			choice=input("\nYour choice: ")
			if choice == "q":
				print("Exit")
				return 0
			subject=subjects[int(choice)-1]
		except Exception:
			print("Please try again.\n")
			continue
		print("You have selected: "+subject)
		break
	want_login=False
	choice=input("Some files require login to be downloaded,would you like to login? y/N: ")
	if choice.lower() == "y":
		username=input("Username: ")
		password=getpass.getpass("Password: ")
		l=login.Login(session,username,password)
		session=l.start()
		download.download(session,subject,retrieve.retrieve(subject),login=True)
		return 0
	else:
		download.download(session,subject,retrieve.retrieve(subject),login=False)
		return 0

if __name__=="__main__":
	exit(main())