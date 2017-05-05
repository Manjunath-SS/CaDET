import re, requests, urllib.request
response=requests.get('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785', verify=False)
extracted_data=response.content
string_data=str(extracted_data,'utf-8')
regex = r"\[.*\]"
lists=re.findall(regex,string_data)
li=''.join(lists)
regex2 = r"\{.*\}"
list2=re.findall(regex2,li)
strng=''.join(list2)
print(string_data)
'''page = urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
extracted_data=page.read()
string_data=str(extracted_data,'utf-8')
final=string_data.replace("\"", "")
regex = r"\[.*\]"
q=re.findall(regex,final)
print(q)'''
