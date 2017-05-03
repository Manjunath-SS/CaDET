import re
import urllib.request
page = urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
extracted_data=page.read()
string_data=str(extracted_data,'utf-8')
regex = r"\[.*\]"
lists=re.findall(regex,string_data)
li=''.join(lists)
regex2 = r"\{.*\}"
list2=re.findall(regex2,li)
strng=''.join(list2)
#print(lists)
f = open('myfile.html', 'w')
f.write(strng)  # python will convert \n to os.linesep
f.close()
strng=dict()
for lm in strng:
    print(lm['author'], lm['urlToImage'], lm['publishedAt'], lm['url'])
