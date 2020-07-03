import requests,sys
#output format:[[filename,size,date(201906),full_url],[...]]
def retrieve(subject,keyword,from_date,to_date):
	url="https://l639t95u5a-dsn.algolia.net/1/indexes/qualifications-uk_LIVE_master-content/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&x-algolia-application-id=L639T95U5A&x-algolia-api-key=f79c7a8352e9ffbdaec387bf43612ee6"
	payload=r'{"params":"query=&filters=category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-report%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-reports%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-Files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FQuestion-paper%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FMark-scheme%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FListening-Examinations-MP3%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FScientific-article%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FPast-question-paper-and-mark-scheme%22%20AND%20(category%3A%22Pearson-UK%3ASpecification-Code%2F'+'{0}%22)\"}}'.format(subject)
	headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0","Origin":"https://qualifications.pearson.com","content-type":"application/x-www-form-urlencoded"}
	month_transform={
	"january":1,
	"february":2,
	"march":3,
	"april":4,
	"may":5,
	"june":6,
	"july":7,
	"august":8,
	"september":9,
	"october":10,
	"november":11,
	"december":12
	}
	raw_results=[]
	while True:
		try:
			r=requests.post(url,data=payload,headers=headers).json()
			break
		except Exception as e:
			print(str(e))
			print("Connection error,retrying\n")
	raw_results.append(r)
	if raw_results[0]["nbPages"] != 1:			
		for i in range(1,raw_results[0]["nbPages"]):
			payload=r'{"params":"query=&filters=category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-report%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-reports%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-Files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FQuestion-paper%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FMark-scheme%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FListening-Examinations-MP3%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FScientific-article%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FPast-question-paper-and-mark-scheme%22%20AND%20(category%3A%22Pearson-UK%3ASpecification-Code%2F'+'{0}%22)&page={1}\"}}'.format(subject,str(i))
			while True:
				try:
					r=requests.post(url,headers=headers,data=payload).json()
					break
				except Exception as e:
					print(str(e))
					print("Connection error, retrying.\n")
			raw_results.append(r)
	results=[]
	for i in raw_results:
		hits=len(i["hits"])
		for j in range(hits):
			tmp=[]
			file_name=i["hits"][j]["title"]
			if "question" not in file_name.lower() and "scheme" not in file_name.lower():
				continue
			elif keyword not in file_name.lower():
				continue
			tmp.append(file_name)
			tmp.append(i["hits"][j]["size"])
			try:
				year=int(file_name[-4:])
				month=month_transform[file_name.lower().split(" ")[-2]]
				date=year*100+month
				tmp.append(date)
			except Exception as e:
				sys.stderr.write("An exception has occured,details:\n")
				sys.stderr.write("File: "+file_name+"    https://qualifications.pearson.com"+i["hits"][j]["url"]+"\n")
				sys.stderr.write(str(e)+"\n\n")
				continue
			tmp.append("https://qualifications.pearson.com"+i["hits"][j]["url"])
			if not (date >= from_date and date <= to_date):
				continue
			results.append(tmp)
	return results
#print(retrieve("ial-maths"))