import requests,getpass
import payload,login,retrieve,download
def main():
	subjects=payload.subject
	session=requests.Session()
	print("Download the following exam series,enter the number")
	print("Enter q to exit\n")
	while True:
		for i in range(len(subjects)):
			print(str(i+1)+"."+subjects[i])
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
	print("Select the time range of the exam papers")
	print("Enter q to exit")
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
	choice=input("Some files require login to be downloaded,would you like to login? y/N: ")
	if choice.lower() == "y":
		username=input("Username: ")
		password=getpass.getpass("Password: ")
		l=login.Login(session,username,password)
		session=l.start()
		download.download(session,subject,retrieve.retrieve(subject,from_date,to_date),login=True)
		return 0
	else:
		download.download(session,subject,retrieve.retrieve(subject,from_date,to_date),login=False)
		return 0

if __name__=="__main__":
	exit(main())