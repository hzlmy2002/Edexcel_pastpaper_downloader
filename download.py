import requests,os

#files:input format:[[filename,size,date(201906),full_url],[...]]

def download(session,subject,file_list,login):
	if not login:
		session=requests.Session()
	try:
		os.mkdir(subject)
	except Exception:
		pass
	try:
		pappers_path=os.path.join(subject,"test_pappers")
		os.mkdir(pappers_path)
	except Exception:
		pass
	try:
		answers_path=os.path.join(subject,"mark_scheme")
		os.mkdir(answers_path)
	except Exception:
		pass	
	print("Totally: "+str(len(file_list))+"\n")
	no=1
	for i in file_list :		
		if not login and "dam/secure" in i[3].lower():
			print("Skip {0}/{1}    {2}    as it requires login.".format(str(no),str(len(file_list),i[0])))
			no+=1
		else:
			print("Download {0}/{1}    {2} {3}".format(str(no),str(len(file_list)),i[0],i[1]),end="\r")
			if "question" in i[0].lower():
				path=os.path.join(os.getcwd(),pappers_path)
				path=os.path.join(path,str(i[2]))
				if not os.path.exists(path):
					os.mkdir(path)
				path=os.path.join(path,i[0])+".pdf"
			elif "scheme" in i[0].lower():
				path=os.path.join(os.getcwd(),answers_path)
				path=os.path.join(path,str(i[2]))
				if not os.path.exists(path):
					os.mkdir(path)
				path=os.path.join(path,i[0])+".pdf"	
			if os.path.exists(path):
				print("Skip {0}/{1}    {2}     as it has been downloaded".format(str(no),str(len(file_list)),i[0]))
				no+=1
				continue
			while True:
				try:
					url=i[3]
					r=session.get(url)
					with open(path,"wb") as file:
						file.write(r.content)
					break
				except Exception as e:
					print(str(e))
					print("Connection error,retrying.\n")
			no+=1
#download(requests.Session(),"ial-maths",[["Question paper - Unit FP1 (6667) - June 2013","137.1 KB",201306,"https://qualifications.pearson.com/content/dam/secure/pdf/A Level/Mathematics/2013/Exam materials/6667_01R_que_20130610.pdf"]],True)