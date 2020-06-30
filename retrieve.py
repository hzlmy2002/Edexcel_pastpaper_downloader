import requests
def retrieve(session,subject):
		session=session
		subject=subject
		url="https://l639t95u5a-dsn.algolia.net/1/indexes/qualifications-uk_LIVE_master-content/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.33.0)%3B%20Browser&x-algolia-application-id=L639T95U5A&x-algolia-api-key=f79c7a8352e9ffbdaec387bf43612ee6"
		payload='{"params":"query=&filters=category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-report%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FExaminer-reports%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FData-Files%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FQuestion-paper%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FMark-scheme%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FListening-Examinations-MP3%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FScientific-article%22%20OR%20category%3A%22Pearson-UK%3ADocument-Type%2FPast-question-paper-and-mark-scheme%22%20AND%20(category%3A%22Pearson-UK%3ASpecification-Code%2F'+subject+'%22)"}'
		results=[]
		results.append(session.post(url,data=payload).json())
		if results[0]["nbPages"] != 1:
			for i in range(1,results[0]["nbPages"]):
				results.append(session.post(url,data=payload+'&page='+str(i)).json())
		return results
#print(retrieve(requests.Session(),"ial-maths"))