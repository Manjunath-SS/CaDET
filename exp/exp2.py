import bs4
import urllib.request

webpage=str(urllib.request.urlopen("https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=0ca6ea2df18e4d128f1490601cfa5785").read())
soup = bs4.BeautifulSoup(webpage)

print(soup.get_text())

f = open('myfile.html', 'w')
f.write(soup.get_text())  # python will convert \n to os.linesep
f.close()
