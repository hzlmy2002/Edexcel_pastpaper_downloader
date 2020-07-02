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
			print("Skip "+str(no)+" "+i[0]+" "+str(no)+"/"+str(len(file_list))+" as it requires login.")
			no+=1
		else:
			print("Downloading "+i[0]+" "+i[1]+" "+str(no)+"/"+str(len(file_list)),end="\r")
			url=i[3]
			r=session.get(url=url)
			no+=1
			if "question" in i[0].lower():
				path=os.path.join(os.getcwd(),pappers_path)
				path=os.path.join(path,str(i[2]))
				if not os.path.exists(path):
					os.mkdir(path)
				path=os.path.join(path,i[0])+".pdf"
				with open(path,'wb') as f:
					f.write(r.content)
			elif "scheme" in i[0].lower():
				path=os.path.join(os.getcwd(),answers_path)
				path=os.path.join(path,str(i[2]))
				if not os.path.exists(path):
					os.mkdir(path)
				path=os.path.join(path,i[0])+".pdf"
				with open(path,'wb') as f:
					f.write(r.content)
	print("\n")
	print("Complete!")
#download(requests.Session(),"ial-maths",[["Question paper - Unit FP1 (6667) - June 2013","137.1 KB",201306,"https://qualifications.pearson.com/content/dam/secure/pdf/A Level/Mathematics/2013/Exam materials/6667_01R_que_20130610.pdf"]],True)