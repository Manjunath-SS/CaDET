import re
import urllib.request
page = urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
extracted_data=page.read()
string_data=str(extracted_data,'utf-8')
final=string_data.replace("\"", "")
regex = r"\[.*\]"
lists=re.findall(regex,final)
print(lists)

my="]"

print(my)
strng=''.join(lists)

for th in strng:

    if th != "]":
        with open("myfile.html", "a") as myfile:
            myfile.write(th)


'''f = open('myfile.html', 'w')
f.write(strng)  # python will convert \n to os.linesep
f.close() '''
