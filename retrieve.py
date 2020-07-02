import requests
#output format:[[filename,size,full_url],[...]]
def retrieve(subject):
		url="https://l639t95u5a-dsn.algolia.net/1/indexes/qualifications-uk_LIVE_master-content/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&x-algolia-application-id=L639T95U5A&x-algolia-api-key=f79c7a8352e9ffbdaec387bf43612ee6"
		payload='{"params":"query=&filters=category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-report%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-reports%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-Files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FQuestion-paper%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FMark-scheme%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FListening-Examinations-MP3%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FScientific-article%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FPast-question-paper-and-mark-scheme%22%20AND%20(category%3A%22Pearson-UK%3ASpecification-Code%2F'+subject+'%22)"}'
		headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0","Origin":"https://qualifications.pearson.com","content-type":"application/x-www-form-urlencoded"}
		raw_results=[]
		raw_results.append(requests.post(url,data=payload,headers=headers).json())
		if raw_results[0]["nbPages"] != 1:
			payload='{"params":"query=&filters=category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-report%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-reports%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-Files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FQuestion-paper%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FMark-scheme%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FListening-Examinations-MP3%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FScientific-article%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FPast-question-paper-and-mark-scheme%22%20AND%20(category%3A%22Pearson-UK%3ASpecification-Code%2F'+subject+'%22)&page='
			for i in range(1,raw_results[0]["nbPages"]):
				raw_results.append(requests.post(url,headers=headers,data=payload+str(i)+'"}').json())
		results=[]
		for i in raw_results:
			hits=len(i["hits"])
			for j in range(hits):
				tmp=[]
				tmp.append(i["hits"][j]["title"])
				tmp.append(i["hits"][j]["size"])
				tmp.append("https://qualifications.pearson.com"+i["hits"][j]["url"])
				results.append(tmp)
		return results
#print(retrieve("ial-maths"))