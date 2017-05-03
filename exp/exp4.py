import re
import urllib.request
page = urllib.request.urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785')
extracted_data=page.read()
string_data=str(extracted_data,'utf-8')
final=string_data.replace("\"", "")
regex = r"\[.*\]"
lists=re.findall(regex,final)
#print(lists)

my="]"
mystr=None
print(my)
strng=''.join(lists)

pattern = r'(author:)|(description:)|(title:)|(url:)|(urlToImage:)|(publishedAt:)'

for match in re.finditer(pattern, final):
    s = match.start()
    e = match.end()
    print( 'Found "%s" at %d:%d' % (final[s:e], s, e))
    #mystr=my+strng

'''st=re.findall(r".*",strng)
print(st)'''

'''f = open('myfile.html', 'w')
f.write(strng)  # python will convert \n to os.linesep
f.close() '''