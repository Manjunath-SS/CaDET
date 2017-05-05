import bs4
import urllib.request
import requests

webpage=str(urllib.request.urlopen("https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=f4585a594fdc47c0a0ca949452a9a906").read())
soup = bs4.BeautifulSoup(webpage)

print(soup.get_text())

f = open('myfile.html', 'w')
f.write(soup.get_text())  # python will convert \n to os.linesep
f.close()
