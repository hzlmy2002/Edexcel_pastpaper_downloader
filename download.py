import requests,os

#input format:[[filename,size,full_url],[...]]

def download(session,subject,files):
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
	print("Totally: "+str(len(files))+"\n")
	no=1
	for i in files :
		print("Downloading "+i[0]+" "+i[1]+" "+str(no)+"/"+str(len(files)),end="\r")
		url=i[2]
		r=session.get(url=url)
		no+=1
		if "question" in i[0].lower():
			path=os.path.join(os.getcwd(),pappers_path)
			path=os.path.join(path,i[0])
			with open(path,'wb') as f:
				f.write(r.content)
		elif "scheme" in i[0].lower():
			path=os.path.join(os.getcwd(),answers_path)
			path=os.path.join(path,i[0])
			with open(path,'wb') as f:
				f.write(r.content)
	print("Complete!")
#download(requests.Session(),"ial-maths",[["Question paper - Unit FP1 (6667) - June 2013","137.1 KB","https://qualifications.pearson.com/content/dam/pdf/A Level/Mathematics/2013/Exam materials/6667_01R_que_20130610.pdf"]])