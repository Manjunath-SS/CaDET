import re
import urllib.request
page = urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
extracted_data=page.read()
string_data=str(extracted_data,'utf-8')
final=string_data.replace("\"", "")
regex = r"\[.*\]"
q=re.findall(regex,final)
print(q)